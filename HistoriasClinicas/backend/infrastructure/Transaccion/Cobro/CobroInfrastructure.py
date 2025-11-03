import psycopg2
import psycopg2.extras
from domain.Transaccion.Cobro.CobroModel import CobroModel

class CobroInfrastructure:

    @staticmethod
    def ingresar_cobro(cobro: CobroModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarCobro(%s,%s,%s,%s);",
                            (cobro.idestadopago, cobro.idpaciente,
                             cobro.fecha, cobro.total))
                conn.commit()
                return {"mensaje": "Cobro ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_cobro(cobro: CobroModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarCobro(%s,%s,%s,%s,%s,%s);",
                            (cobro.idcobro, cobro.idestadopago, cobro.idpaciente,
                             cobro.fecha, cobro.total,
                             '1' if cobro.activo else '0'))
                conn.commit()
                return {"mensaje": "Cobro modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def desactivar_cobro(idcobro: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarCobro(%s);", (idcobro,))
                conn.commit()
                return {"mensaje": f"Cobro {idcobro} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_cobro(idcobro: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarCobro(%s);", (idcobro,))
                conn.commit()
                return {"mensaje": f"Cobro {idcobro} eliminado físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_cobro_por_id(idcobro: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarCobroPorId(%s);", (idcobro,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Cobro no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()