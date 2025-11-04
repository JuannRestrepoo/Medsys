import psycopg2
import psycopg2.extras
from domain.Usuario.Profesional.ProfesionalModel import ProfesionalModel

class ProfesionalInfrastructure:

    @staticmethod
    def ingresar_profesional(profesional: ProfesionalModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                # Activo se pone por defecto en la BD
                cur.execute("SELECT spaIngresarProfesional(%s,%s,%s);",
                            (profesional.idusuario, profesional.idcentro, profesional.cargo))
                conn.commit()
                return {"mensaje": "Profesional ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_profesional(profesional: ProfesionalModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarProfesional(%s,%s,%s,%s,%s);",
                            (profesional.idprofesional, profesional.idusuario,
                             profesional.idcentro, profesional.cargo,
                             '1' if profesional.activo else '0'))
                conn.commit()
                return {"mensaje": "Profesional modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
    
    @staticmethod
    def desactivar_profesional(idprofesional: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarProfesional(%s);", (idprofesional,))
                conn.commit()
                return {"mensaje": f"Profesional {idprofesional} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()


    @staticmethod
    def eliminar_profesional(idprofesional: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarProfesional(%s);", (idprofesional,))
                conn.commit()
                return {"mensaje": f"Profesional {idprofesional} eliminado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_profesional_por_id(idprofesional: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarProfesionalPorId(%s);", (idprofesional,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Profesional no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()


    @staticmethod
    def consultar_por_usuario(idusuario: str):
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
                cur.execute("""
                    SELECT idprofesional, idusuario, idcentro, cargo, activo
                    FROM profesional
                    WHERE idusuario = %s
                """, (idusuario,))
                row = cur.fetchone()
                if not row:
                    return None
                return {
                    "idprofesional": row[0],
                    "idusuario": row[1],
                    "idcentro": row[2],
                    "cargo": row[3],
                    "activo": row[4]
                }
        except Exception as e:
            print("Error en consultar_por_usuario:", e)
            return None
        finally:
            if conn:
                conn.close()

#perfil profesional
    @staticmethod
    def consultar_profesional_usuario(idusuario: str):
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
                cur.execute(
                    '''
                    SELECT u."Nombre_Completo",
                           u."Correo",
                           u."Telefono",
                           p."Cargo"

                    FROM "Usuario" u
                    JOIN "Profesional" p ON u."IdUsuario" = p."IdUsuario"
                    WHERE u."IdUsuario" = %s
                    ''',
                    (idusuario,)
                )
                result = cur.fetchone()
                return result if result else {"mensaje": "Profesional no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()