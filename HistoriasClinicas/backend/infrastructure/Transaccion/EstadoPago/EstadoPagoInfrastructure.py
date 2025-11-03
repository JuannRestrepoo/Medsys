import psycopg2
import psycopg2.extras
from domain.Transaccion.EstadoPago.EstadoPagoModel import EstadoPagoModel

class EstadoPagoInfrastructure:

    @staticmethod
    def ingresar_estadopago(ep: EstadoPagoModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarEstadoPago(%s);", (ep.nombre,))
                conn.commit()
                return {"mensaje": "Estado de pago ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_estadopago(ep: EstadoPagoModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarEstadoPago(%s,%s,%s);",
                            (ep.idestadopago, ep.nombre,
                             '1' if ep.activo else '0'))
                conn.commit()
                return {"mensaje": "Estado de pago modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def desactivar_estadopago(idestadopago: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarEstadoPago(%s);", (idestadopago,))
                conn.commit()
                return {"mensaje": f"Estado de pago {idestadopago} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_estadopago(idestadopago: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarEstadoPago(%s);", (idestadopago,))
                conn.commit()
                return {"mensaje": f"Estado de pago {idestadopago} eliminado físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_estadopago_por_id(idestadopago: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarEstadoPagoPorId(%s);", (idestadopago,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Estado de pago no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
