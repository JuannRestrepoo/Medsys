import psycopg2
import psycopg2.extras
from core.Security.security import verify_password

import logging

# Configuración del archivo físico de auditoría

logger_seguridad = logging.getLogger('SEGURIDAD')

class LoginInfrastructure:

    @staticmethod
    def login_paciente(correo: str, contrasena: str,ip_cliente: str):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbaMedSys",
                user="postgres",
                password="admin123",
                host="127.0.0.1",
                port="5433"
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                # Buscar usuario y datos del paciente
                cur.execute(
                    '''
                    SELECT u."IdUsuario",
                        u."Correo",
                        u."Contrasena_Hash",
                        u."Rol",
                        u."Nombre_Completo",
                        u."Numero_Documento",
                        p."IdPaciente"
                    FROM "Usuario" u
                    JOIN "Paciente" p ON u."IdUsuario" = p."IdUsuario"
                    WHERE u."Correo" = %s
                    ''',
                    (correo,)
                )
                user = cur.fetchone()
                
                # ─── DETECCIÓN DE INCIDENTES (PACIENTE) ───
                if not user:
                    logger_seguridad.warning(f"AUTH_FAILED | IP: {ip_cliente} | Intento de login con correo inexistente en Pacientes: '{correo}'")
                    return {"error": "Usuario no encontrado"}
                    
                if not verify_password(contrasena, user["Contrasena_Hash"]):
                    logger_seguridad.warning(f"AUTH_FAILED | IP: {ip_cliente} | Contraseña incorrecta para el Paciente: '{correo}'")
                    return {"error": "Credenciales inválidas"}
                    
                if user["Rol"].strip().upper() != "PACIENTE":
                    logger_seguridad.warning(f"ROLE_VIOLATION | IP: {ip_cliente} | Usuario '{correo}' intentó ingresar como Paciente pero tiene rol: '{user['Rol']}'")
                    return {"error": "Este usuario no es un paciente"}

                return {
                    "mensaje": "Login exitoso",
                    "idusuario": user["IdUsuario"],
                    "idpaciente": user["IdPaciente"],
                    "rol": user["Rol"],
                    "nombre": user["Nombre_Completo"],
                    "numero_documento": user["Numero_Documento"],
                }
        except Exception as e:
            # También detectamos fallos catastróficos de base de datos o conexión
            logger_seguridad.error(f"SYSTEM_ERROR | IP: {ip_cliente} | Excepción en login_paciente: {str(e)}")
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()


    @staticmethod
    def login_profesional(correo: str, contrasena: str,ip_cliente: str):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbaMedSys",
                user="postgres",
                password="admin123",
                host="127.0.0.1",
                port="5433"
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                # Buscar usuario
                cur.execute(
                    '''
                    SELECT "IdUsuario","Correo","Contrasena_Hash","Rol","Nombre_Completo"
                    FROM "Usuario"
                    WHERE "Correo" = %s
                    ''',
                    (correo,)
                )
                user = cur.fetchone()
                
                # ─── DETECCIÓN DE INCIDENTES (PROFESIONAL) ───
                if not user:
                    logger_seguridad.warning(f"AUTH_FAILED |IP: {ip_cliente} | Intento de login con correo inexistente en Profesionales: '{correo}'")
                    return {"error": "Usuario no encontrado"}
                    
                if not verify_password(contrasena, user["Contrasena_Hash"]):
                    logger_seguridad.warning(f"AUTH_FAILED | IP: {ip_cliente} | Contraseña incorrecta para el Profesional: '{correo}'")
                    return {"error": "Credenciales inválidas"}
                    
                if user["Rol"].strip().upper() != "PROFESIONAL":
                    logger_seguridad.warning(f"ROLE_VIOLATION | IP: {ip_cliente} | Usuario '{correo}' intentó ingresar como Profesional pero tiene rol: '{user['Rol']}'")
                    return {"error": "Este usuario no tiene rol de profesional"}

                # Buscar profesional y su centro + ciudad
                cur.execute(
                    '''
                    SELECT p."IdProfesional",
                           c."IdCentro",
                           c."Nombre" AS centro_nombre,
                           c."Direccion",
                           c."Telefono",
                           ci."Nombre" AS ciudad_nombre
                    FROM "Profesional" p
                    JOIN "Centro" c ON p."IdCentro" = c."IdCentro"
                    JOIN "Ciudad" ci ON c."IdCiudad" = ci."IdCiudad"
                    WHERE p."IdUsuario" = %s
                    ''',
                    (user["IdUsuario"],)
                )
                prof = cur.fetchone()
                if not prof:
                    logger_seguridad.error(f"INTEGRITY_ERROR | Usuario '{correo}' autenticado con rol Profesional, pero no existe registro asociado en la tabla Profesional.")
                    return {"error": "El usuario existe pero no está registrado en la tabla Profesional"}

                return {
                    "mensaje": "Login exitoso",
                    "idusuario": user["IdUsuario"],
                    "idprofesional": prof["IdProfesional"],
                    "rol": user["Rol"],
                    "nombre": user["Nombre_Completo"],
                    "centro": {
                        "idcentro": prof["IdCentro"],
                        "nombre": prof["centro_nombre"],
                        "direccion": prof["Direccion"],
                        "telefono": prof["Telefono"],
                        "ciudad": prof["ciudad_nombre"]
                    }
                }
        except Exception as e:
            logger_seguridad.error(f"SYSTEM_ERROR | Excepción en login_profesional: {str(e)}")
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()
