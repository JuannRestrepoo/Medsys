import psycopg2
import psycopg2.extras
from domain.Usuario.TipoDocumento.TipoDocumentoModel import TipoDocumentoModel

class TipoDocumentoInfrastructure:

    @staticmethod
    def ingresar_tipodocumento(td: TipoDocumentoModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres', password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarTipoDocumento(%s,%s);", (td.nombre, td.descripcion))
                conn.commit()
                return {"mensaje": "TipoDocumento ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_tipodocumento(td: TipoDocumentoModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres', password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarTipoDocumento(%s,%s);",
                            (td.nombre, td.descripcion))
                conn.commit()
                return {"mensaje": "TipoDocumento modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_tipodocumento(idtipodocumento: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres', password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarTipoDocumento(%s);", (idtipodocumento,))
                conn.commit()
                return {"mensaje": f"TipoDocumento {idtipodocumento} eliminado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_tipodocumento_por_id(idtipodocumento: str):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarTipoDocumentoPorId(%s);", (idtipodocumento,))
                result = cur.fetchone()
                return result if result else {"mensaje": "TipoDocumento no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()



    @staticmethod
    def consultar_tipodocumentos():
            conn = None
            try:
                conn = psycopg2.connect(
                    dbname='dbaMedSys',
                    user='postgres',
                    password='',
                    host='127.0.0.1',
                    port='5432'
                )
                with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                    # Aquí puedes usar un SELECT directo o un SP si ya lo tienes
                    cur.execute('SELECT "IdTipoDocumento","Nombre" FROM "TipoDocumento"')
                    rows = cur.fetchall()
                    return rows if rows else []
            except Exception as e:
                return {"error": str(e)}
            finally:
                if conn:
                    conn.close()