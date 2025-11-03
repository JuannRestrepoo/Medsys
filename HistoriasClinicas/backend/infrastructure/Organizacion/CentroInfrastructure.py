import psycopg2
import psycopg2.extras
from domain.Organizacion.Centro.CentroModel import CentroModel

class CentroInfrastructure:

    # 🔹 Insertar
    @staticmethod
    def ingresar_centro(centro: CentroModel):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarCentro(%s, %s, %s, %s);",
                            (centro.nombre, centro.direccion, centro.telefono, centro.idciudad))
                conn.commit()
                return {"mensaje": "Centro ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Modificar
    @staticmethod
    def modificar_centro(centro: CentroModel):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarCentro(%s, %s, %s, %s, %s);",
                            (centro.idcentro, centro.nombre, centro.direccion, centro.telefono, centro.idciudad))
                conn.commit()
                return {"mensaje": "Centro modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
    @staticmethod
    def desactivar_centro(idcentro: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarCentro(%s);", (idcentro,))
                conn.commit()
                return {"mensaje": f"Centro {idcentro} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()


    # 🔹 Eliminar
    @staticmethod
    def eliminar_centro(idcentro: str):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarCentro(%s);", (idcentro,))
                conn.commit()
                return {"mensaje": f"Centro {idcentro} eliminado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Consultar todos
    @staticmethod
    def consultar_centro():
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarCentro();")
                result = cur.fetchall()
            return result
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Consultar por Id
    @staticmethod
    def consultar_centro_por_id(idcentro: str):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarCentroPorId(%s);", (idcentro,))
                result = cur.fetchone()
            if result:
                return result
            else:
                return {"mensaje": f"No se encontró un centro con Id {idcentro}"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
