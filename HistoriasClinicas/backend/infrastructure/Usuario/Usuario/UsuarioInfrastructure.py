import psycopg2
import uuid
import datetime
from passlib.context import CryptContext
from domain.Usuario.Usuario.UsuarioModel import UsuarioModel
from domain.Auth.LoginModel import LoginModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UsuarioInfrastructure:

    @staticmethod
    def ingresar_usuario(usuario: UsuarioModel):
        conn = None
        try:
            # 1. Contraseña en claro → hash bcrypt
            contrasena_clara = str(usuario.contrasena).strip()
            if len(contrasena_clara.encode("utf-8")) > 72:
                return {"error": "La contraseña no puede superar los 72 caracteres"}
            hashed_password = pwd_context.hash(contrasena_clara)

            # 2. Convertir tipos a lo que espera Postgres
            idciudad = str(uuid.UUID(usuario.idciudad))
            idtipodocumento = str(uuid.UUID(usuario.idtipodocumento))
            idtipogenero = str(uuid.UUID(usuario.idtipogenero))
            fecha_nac = datetime.date.fromisoformat(usuario.fecha_nacimiento)

            # 3. Conexión y ejecución del SP
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT spaIngresarUsuario(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',
                    (
                        idciudad,
                        idtipodocumento,
                        idtipogenero,
                        usuario.nombre_completo,
                        usuario.correo,
                        hashed_password,
                        usuario.rol,
                        usuario.numero_documento,
                        usuario.direccion,
                        fecha_nac
                    )
                )
                conn.commit()
                return {"mensaje": "Usuario ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

    @staticmethod
    def modificar_usuario(usuario: UsuarioModel):
        try:
            # Si viene una contraseña nueva, la hasheamos
            hashed_password = pwd_context.hash(usuario.contrasena_hash) if usuario.contrasena_hash else None

            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT "spaModificarUsuario"(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',
                    (
                        usuario.idusuario, usuario.idciudad, usuario.idtipodocumento,
                        usuario.idtipogenero, usuario.nombre_completo, usuario.correo,
                        hashed_password, usuario.rol, usuario.numero_documento,
                        usuario.direccion, usuario.fecha_nacimiento,
                        '1' if usuario.activo else '0'
                    )
                )
                conn.commit()
                return {"mensaje": "Usuario modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
    @staticmethod

    def desactivar_usuario(idusuario: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarUsuario(%s);", (idusuario,))
                conn.commit()
                return {"mensaje": f"Usuario {idusuario} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:  conn.close()

    @staticmethod
    def eliminar_usuario(idusuario: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarUsuario(%s);", (idusuario,))
                conn.commit()
                return {"mensaje": f"Usuario {idusuario} eliminado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_usuario_por_id(idusuario: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarUsuarioPorId(%s);", (idusuario,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Usuario no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()


    @staticmethod
    def verificar_credenciales(login: LoginModel):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                # Buscar usuario por correo
                cur.execute(
                    'SELECT "Contrasena_Hash", "IdUsuario", "Rol", "Nombre_Completo" '
                    'FROM "Usuario" WHERE "Correo" = %s AND "Activo" = B\'1\';',
                    (login.correo,)
                )
                
                row = cur.fetchone()

                if not row:
                    return {"error": "Usuario no encontrado o inactivo"}

                contrasena_hash, idusuario, rol, nombre = row

                # Verificar contraseña
                if pwd_context.verify(login.contrasena, contrasena_hash):
                    return {
                        "mensaje": "Login exitoso",
                        "idusuario": str(idusuario),
                        "rol": rol,
                        "nombre": nombre
                    }
                else:
                    return {"error": "Contraseña incorrecta"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

