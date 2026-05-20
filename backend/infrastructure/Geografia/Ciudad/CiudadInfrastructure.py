import psycopg2
import psycopg2.extras
from domain.Geografia.Ciudad.CiudadModel import CiudadModel

class CiudadInfrastructure:

    # 🔹 Insertar
    @staticmethod
    def ingresar_ciudad(ciudad: CiudadModel):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='admin123',
                host='127.0.0.1',
                port='5433'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarCiudad(%s, %s);",
                            (ciudad.nombre, ciudad.iddepartamento))
                conn.commit()
                return {"mensaje": "Ciudad ingresada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Modificar
    @staticmethod
    def modificar_ciudad(ciudad: CiudadModel):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='admin123',
                host='127.0.0.1',
                port='5433'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarCiudad(%s, %s, %s);",
                            (ciudad.idciudad, ciudad.nombre, ciudad.iddepartamento))
                conn.commit()
                return {"mensaje": "Ciudad modificada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
    @staticmethod
    def desactivar_ciudad(idciudad: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='admin123', host='127.0.0.1', port='5433')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarCiudad(%s);", (idciudad,))
                conn.commit()
                return {"mensaje": f"Ciudad {idciudad} desactivada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Eliminar
    @staticmethod
    def eliminar_ciudad(idciudad: str):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='admin123',
                host='127.0.0.1',
                port='5433'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarCiudad(%s);", (idciudad,))
                conn.commit()
                return {"mensaje": f"Ciudad {idciudad} eliminada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Consultar todas
    @staticmethod
    def consultar_ciudad():
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='admin123',
                host='127.0.0.1',
                port='5433'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarCiudad();")
                result = cur.fetchall()
            return result
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Consultar por Id
    @staticmethod
    def consultar_ciudad_por_id(idciudad: str):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='admin123',
                host='127.0.0.1',
                port='5433'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarCiudadPorId(%s);", (idciudad,))
                result = cur.fetchone()
            if result:
                return result
            else:
                return {"mensaje": f"No se encontró una ciudad con Id {idciudad}"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
