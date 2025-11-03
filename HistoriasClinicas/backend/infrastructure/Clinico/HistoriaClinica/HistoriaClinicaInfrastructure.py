import psycopg2
import psycopg2.extras
from domain.Clinico.HistoriaClinica.HistoriaClinicaModel import HistoriaClinicaModel

class HistoriaClinicaInfrastructure:

    @staticmethod
    def ingresar_historiaclinica(historia: HistoriaClinicaModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarHistoriaClinica(%s,%s,%s,%s);",
                            (historia.idpaciente, historia.fecha_creacion,
                             historia.antecedentes, historia.observaciones))
                conn.commit()
                return {"mensaje": "HistoriaClinica ingresada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_historiaclinica(historia: HistoriaClinicaModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarHistoriaClinica(%s,%s,%s,%s,%s,%s);",
                            (historia.idhistoria, historia.idpaciente,
                             historia.fecha_creacion, historia.antecedentes,
                             historia.observaciones,
                             '1' if historia.activo else '0'))
                conn.commit()
                return {"mensaje": "HistoriaClinica modificada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Desactivar (borrado lógico)
    @staticmethod
    def desactivar_historiaclinica(idhistoria: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarHistoriaClinica(%s);", (idhistoria,))
                conn.commit()
                return {"mensaje": f"HistoriaClinica {idhistoria} desactivada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Eliminar (borrado físico)
    @staticmethod
    def eliminar_historiaclinica(idhistoria: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarHistoriaClinica(%s);", (idhistoria,))
                conn.commit()
                return {"mensaje": f"HistoriaClinica {idhistoria} eliminada físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_historiaclinica_por_id(idhistoria: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarHistoriaClinicaPorId(%s);", (idhistoria,))
                result = cur.fetchone()
                return result if result else {"mensaje": "HistoriaClinica no encontrada o inactiva"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_historiaclinica_por_id(idhistoria: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarHistoriaClinicaPorId(%s);", (idhistoria,))
                result = cur.fetchone()
                return result if result else {"mensaje": "HistoriaClinica no encontrada"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()