import psycopg2
import psycopg2.extras
from domain.Clinico.Diagnostico.DiagnosticoModel import DiagnosticoModel

class DiagnosticoInfrastructure:

    @staticmethod
    def ingresar_diagnostico(diag: DiagnosticoModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarDiagnostico(%s,%s,%s);",
                            (diag.idcita, diag.descripcion, diag.observaciones))
                conn.commit()
                return {"mensaje": "Diagnóstico ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_diagnostico(diag: DiagnosticoModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarDiagnostico(%s,%s,%s,%s,%s);",
                            (diag.iddiagnostico, diag.idcita,
                             diag.descripcion, diag.observaciones,
                             '1' if diag.activo else '0'))
                conn.commit()
                return {"mensaje": "Diagnóstico modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def desactivar_diagnostico(iddiagnostico: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarDiagnostico(%s);", (iddiagnostico,))
                conn.commit()
                return {"mensaje": f"Diagnóstico {iddiagnostico} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_diagnostico(iddiagnostico: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarDiagnostico(%s);", (iddiagnostico,))
                conn.commit()
                return {"mensaje": f"Diagnóstico {iddiagnostico} eliminado físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_diagnostico_por_id(iddiagnostico: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarDiagnosticoPorId(%s);", (iddiagnostico,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Diagnóstico no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
