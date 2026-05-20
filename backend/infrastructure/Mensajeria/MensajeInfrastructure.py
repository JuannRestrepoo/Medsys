import psycopg2
import psycopg2.extras
import hmac
import hashlib
import logging
from datetime import datetime
from cryptography.fernet import Fernet

logger_seguridad = logging.getLogger('SEGURIDAD')
CLAVE_SECRETA_HMAC = b"MedSys_Clave_Ultra_Secreta_2026"

LLAVE_SECRETA = b'nxbZbg1jRb06DwNFARC6O5mV1EljlmmtOkiX-QtzO_w='
cipher_suite = Fernet(LLAVE_SECRETA)

class MensajeInfrastructure:

    @staticmethod
    def enviar_mensaje(id_remitente: str, id_destinatario: str, contenido: str, ip_cliente: str):
        # ─── NUEVA VALIDACIÓN: ALERTA POR ENVÍO TRAS LAS 9:00 PM ───
        ahora = datetime.now()
        hora_actual = ahora.time()
        hora_limite = datetime.strptime("21:00:00", "%H:%M:%S").time() # 9:00 PM
        
        if hora_actual > hora_limite:
            logger_seguridad.warning(
                f"SUSPICIOUS_ACTIVITY | IP: {ip_cliente} | Alerta: Envío de mensaje fuera de horario laboral "
                f"({ahora.strftime('%H:%M:%S')}). Remitente: {id_remitente} -> Destinatario: {id_destinatario}"
            )
        # ──────────────────────────────────────────────────────────

        # 1. INTEGRIDAD: Firma digital HMAC sobre el texto plano antes de encriptar
        firma = hmac.new(CLAVE_SECRETA_HMAC, contenido.encode('utf-8'), hashlib.sha256).hexdigest()
        
        # 2. CONFIDENCIALIDAD: Cifrado simétrico AES sobre el contenido
        contenido_cifrado = cipher_suite.encrypt(contenido.encode('utf-8')).decode('utf-8')
        
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbaMedSys", user="postgres", password="admin123", host="127.0.0.1", port="5433"
            )
            with conn.cursor() as cur:
                # Insertamos el contenido cifrado y la firma de integridad en Postgres
                cur.execute(
                    '''
                    INSERT INTO "Mensaje" ("IdRemitente", "IdDestinatario", "Contenido", "Firma_Integridad")
                    VALUES (%s, %s, %s, %s)
                    RETURNING "IdMensaje", "Fecha_Envio";
                    ''',
                    (id_remitente, id_destinatario, contenido_cifrado, firma)
                )
                res = cur.fetchone()
                conn.commit()
                
                return {
                    "mensaje": "Mensaje enviado y cifrado de forma segura", 
                    "idmensaje": str(res[0]),
                    "fecha": res[1].strftime("%Y-%m-%d %H:%M:%S")
                }
                
        except Exception as e:
            if conn: conn.rollback()
            logger_seguridad.error(f"SYSTEM_ERROR | IP: {ip_cliente} | Error al guardar mensaje: {str(e)}")
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def obtener_historial_chat(id_doctor: str, id_paciente: str, ip_cliente: str):
        """
        Consulta bidireccional limpia adaptada al fetch de React
        que desencripta y verifica la integridad de cada burbuja.
        """
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbaMedSys", user="postgres", password="admin123", host="127.0.0.1", port="5433"
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                # Trae el chat mutuo ordenado cronológicamente
                cur.execute(
                    '''
                    SELECT "IdMensaje", "IdRemitente", "IdDestinatario", "Contenido", "Firma_Integridad", "Fecha_Envio"
                    FROM "Mensaje"
                    WHERE ("IdRemitente" = %s AND "IdDestinatario" = %s)
                       OR ("IdRemitente" = %s AND "IdDestinatario" = %s)
                    ORDER BY "Fecha_Envio" ASC;
                    ''',
                    (id_doctor, id_paciente, id_paciente, id_doctor)
                )
                mensajes = cur.fetchall()
                
                mensajes_verificados = []
                for msg in mensajes:
                    try:
                        # 1. DESENCRIPTAR: Devolvemos el texto a string plano
                        contenido_cifrado = msg["Contenido"].encode('utf-8')
                        texto_plano = cipher_suite.decrypt(contenido_cifrado).decode('utf-8')
                        
                        # 2. VERIFICAR INTEGRIDAD: Validamos el HMAC sobre el texto recuperado
                        mac_calculado = hmac.new(CLAVE_SECRETA_HMAC, texto_plano.encode('utf-8'), hashlib.sha256).hexdigest()
                        
                        if hmac.compare_digest(msg["Firma_Integridad"], mac_calculado):
                            estado = "✅ Verificado (Cifrado e Íntegro)"
                            texto_final = texto_plano
                        else:
                            # Alerta de alteration maliciosa detectada
                            logger_seguridad.critical(
                                f"INTEGRITY_VIOLATION | IP: {ip_cliente} | ¡ALERTA! El mensaje ID {msg['IdMensaje']} fue manipulado en la base de datos."
                            )
                            estado = "❌ CORRUMPIDO"
                            texto_final = "⚠️ ERROR CRÍTICO: Este mensaje fue alterado de forma externa y bloqueado por seguridad."
                    
                    except Exception:
                        # Respaldo por si quedan registros antiguos en texto plano sin cifrar en la BD
                        texto_final = msg["Contenido"]
                        estado = "⚠️ Texto plano heredado"

                    # Formato mapeado perfectamente para el renderizado del JSX
                    mensajes_verificados.append({
                        "idmensaje": str(msg["IdMensaje"]),
                        "idremitente": str(msg["IdRemitente"]),
                        "iddestinatario": str(msg["IdDestinatario"]),
                        "contenido": texto_final,
                        "fecha": msg["Fecha_Envio"].strftime("%Y-%m-%d %H:%M:%S") if msg["Fecha_Envio"] else None,
                        "estado_seguridad": estado
                    })
                        
                return mensajes_verificados
                
        except Exception as e:
            logger_seguridad.error(f"SYSTEM_ERROR | IP: {ip_cliente} | Error al listar mensajes: {str(e)}")
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def listar_contactos_chat(ip_cliente: str):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbaMedSys", user="postgres", password="admin123", host="127.0.0.1", port="5433"
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                # Solución Bit(1) robusta con casteo explícito ::bit
                cur.execute('''
                    SELECT "IdUsuario", "Nombre_Completo" 
                    FROM "Usuario" 
                    WHERE "Rol" = 'Paciente' AND "Activo" = '1'::bit
                    ORDER BY "Nombre_Completo" ASC;
                ''')
                usuarios = cur.fetchall()
                
                return [{
                    "id": str(u["IdUsuario"]),
                    "nombre": u["Nombre_Completo"], 
                    "ultimo_msg": "Haz clic para iniciar la conversación"
                } for u in usuarios]
        except Exception as e:
            logger_seguridad.error(f"SYSTEM_ERROR | IP: {ip_cliente} | Error al listar contactos: {str(e)}")
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def listar_profesionales_salud(ip_cliente: str):
        """
        Busca todos los usuarios con rol Médico/Doctor activos en el sistema 
        para que el paciente los visualice en su bandeja.
        """
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbaMedSys", user="postgres", password="admin123", host="127.0.0.1", port="5433"
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                # Adaptado a la estructura real de tu tabla "Usuario" y control de bit activo
                cur.execute('''
                    SELECT "IdUsuario", "Nombre_Completo" 
                    FROM "Usuario" 
                    WHERE "Rol" IN ('Doctor', 'Medico', 'Profesional') AND "Activo" = '1'::bit
                    ORDER BY "Nombre_Completo" ASC;
                ''')
                medicos = cur.fetchall()
                
                return [{
                    "id": str(m["IdUsuario"]),
                    "nombre": m["Nombre_Completo"],
                    "ultimo_msg": "Haz clic para abrir el historial clínico"
                } for m in medicos]
                
        except Exception as e:
            logger_seguridad.error(f"SYSTEM_ERROR | IP: {ip_cliente} | Error al listar profesionales: {str(e)}")
            return {"error": str(e)}
        finally:
            if conn: conn.close()