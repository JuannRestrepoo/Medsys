import psycopg2
import psycopg2.extras
from domain.Transaccion.DetalleCobro.DetalleCobroModel import DetalleCobroModel

class DetalleCobroInfrastructure:

    @staticmethod
    def ingresar_detallecobro(det: DetalleCobroModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarDetalleCobro(%s,%s,%s,%s);",
                            (det.idcobro, det.idproductoservicio,
                             det.cantidad, det.subtotal))
                conn.commit()
                return {"mensaje": "Detalle de cobro ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_detallecobro(det: DetalleCobroModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarDetalleCobro(%s,%s,%s,%s,%s,%s);",
                            (det.iddetalle, det.idcobro, det.idproductoservicio,
                             det.cantidad, det.subtotal,
                             '1' if det.activo else '0'))
                conn.commit()
                return {"mensaje": "Detalle de cobro modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def desactivar_detallecobro(iddetalle: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarDetalleCobro(%s);", (iddetalle,))
                conn.commit()
                return {"mensaje": f"Detalle de cobro {iddetalle} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_detallecobro(iddetalle: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarDetalleCobro(%s);", (iddetalle,))
                conn.commit()
                return {"mensaje": f"Detalle de cobro {iddetalle} eliminado físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_detallecobro_por_id(iddetalle: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarDetalleCobroPorId(%s);", (iddetalle,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Detalle de cobro no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
