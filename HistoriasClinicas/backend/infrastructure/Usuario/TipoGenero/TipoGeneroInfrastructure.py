import psycopg2
import psycopg2.extras
from domain.Usuario.TipoGenero.TipoGeneroModel import TipoGeneroModel

class TipoGeneroInfrastructure:

    @staticmethod
    def ingresar_tipogenero(tg: TipoGeneroModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres', password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarTipoGenero(%s);", (tg.nombre,))
                conn.commit()
                return {"mensaje": "TipoGenero ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_tipogenero(tg: TipoGeneroModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres', password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarTipoGenero(%s,%s);",
                            (tg.idtipogenero, tg.nombre,))
                conn.commit()
                return {"mensaje": "TipoGenero modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_tipogenero(idtipogenero: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres', password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarTipoGenero(%s);", (idtipogenero,))
                conn.commit()
                return {"mensaje": f"TipoGenero {idtipogenero} eliminado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_tipogenero_por_id(idtipogenero: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres', password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarTipoGeneroPorId(%s);", (idtipogenero,))
                result = cur.fetchone()
                return result if result else {"mensaje": "TipoGenero no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
