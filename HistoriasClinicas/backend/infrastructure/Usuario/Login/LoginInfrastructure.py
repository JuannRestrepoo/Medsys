import psycopg2
import psycopg2.extras
from core.Security.security import verify_password

class LoginInfrastructure:

    @staticmethod
    def login_paciente(correo: str, contrasena: str):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbaMedSys",
                user="postgres",
                password="",
                host="127.0.0.1",
                port="5432"
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                # Buscar usuario por correo
                cur.execute(
                    'SELECT "IdUsuario","Correo","Contrasena_Hash","Rol","Nombre_Completo" '
                    'FROM "Usuario" WHERE "Correo" = %s',
                    (correo,)
                )
                user = cur.fetchone()
                if not user:
                    return {"error": "Usuario no encontrado"}
                if not verify_password(contrasena, user["Contrasena_Hash"]):
                    return {"error": "Credenciales inválidas"}
                if user["Rol"].strip().upper() != "PACIENTE":
                    return {"error": "Este usuario no es un paciente"}
                return {
                    "mensaje": "Login exitoso",
                    "idusuario": user["IdUsuario"],
                    "rol": user["Rol"],
                    "nombre": user["Nombre_Completo"]
                }
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

    @staticmethod
    def login_profesional(correo: str, contrasena: str):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbaMedSys",
                user="postgres",
                password="",
                host="127.0.0.1",
                port="5432"
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                # Primero buscar usuario
                cur.execute(
                    'SELECT "IdUsuario","Correo","Contrasena_Hash","Rol","Nombre_Completo" '
                    'FROM "Usuario" WHERE "Correo" = %s',
                    (correo,)
                )
                user = cur.fetchone()
                if not user:
                    return {"error": "Usuario no encontrado"}
                if not verify_password(contrasena, user["Contrasena_Hash"]):
                    return {"error": "Credenciales inválidas"}
                if user["Rol"].strip().upper() != "PROFESIONAL":
                    return {"error": "Este usuario no tiene rol de profesional"}

                # Verificar que esté en la tabla Profesional
                cur.execute(
                    'SELECT "IdProfesional" FROM "Profesional" WHERE "IdUsuario" = %s',
                    (user["IdUsuario"],)
                )
                prof = cur.fetchone()
                if not prof:
                    return {"error": "El usuario existe pero no está registrado en la tabla Profesional"}

                return {
                    "mensaje": "Login exitoso",
                    "idusuario": user["IdUsuario"],
                    "idprofesional": prof["IdProfesional"],
                    "rol": user["Rol"],
                    "nombre": user["Nombre_Completo"]
                }
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()
