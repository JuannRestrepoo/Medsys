import psycopg2
import psycopg2.extras
from domain.Servicios.TipoServicio.TipoServicioModel import TipoServicioModel

class TipoServicioInfrastructure:

    @staticmethod
    def ingresar_tiposervicio(ts: TipoServicioModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarTipoServicio(%s,%s);",
                            (ts.nombre, ts.descripcion))
                conn.commit()
                return {"mensaje": "Tipo de servicio ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_tiposervicio(ts: TipoServicioModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarTipoServicio(%s,%s,%s,%s);",
                            (ts.idtiposervicio, ts.nombre, ts.descripcion,
                             '1' if ts.activo else '0'))
                conn.commit()
                return {"mensaje": "Tipo de servicio modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def desactivar_tiposervicio(idtiposervicio: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarTipoServicio(%s);", (idtiposervicio,))
                conn.commit()
                return {"mensaje": f"Tipo de servicio {idtiposervicio} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_tiposervicio(idtiposervicio: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarTipoServicio(%s);", (idtiposervicio,))
                conn.commit()
                return {"mensaje": f"Tipo de servicio {idtiposervicio} eliminado físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_tiposervicio_por_id(idtiposervicio: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarTipoServicioPorId(%s);", (idtiposervicio,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Tipo de servicio no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
