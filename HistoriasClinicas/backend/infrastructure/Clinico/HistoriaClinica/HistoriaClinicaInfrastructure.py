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
                cur.execute("SELECT spaIngresarHistoriaClinica(%s,%s,%s,%s,%s);",
                            (historia.idpaciente, historia.idprofesional, historia.fecha_creacion,
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




    @staticmethod
    def listar_historias_por_documento(documento: str):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432',
                options='-c client_encoding=UTF8'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("""
                SELECT h."IdHistoria" AS idhistoria,
                       h."Fecha_Creacion" AS fecha,
                       h."Antecedentes" AS antecedentes,
                       h."Observaciones" AS observaciones,
                       pr."IdProfesional" AS idprofesional,
                       up."Nombre_Completo" AS nombre_profesional,
                       pr."Cargo" AS cargo
                FROM "HistoriaClinica" h
                JOIN "Paciente" p ON h."IdPaciente" = p."IdPaciente"
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                JOIN "Profesional" pr ON h."IdProfesional" = pr."IdProfesional"
                JOIN "Usuario" up ON pr."IdUsuario" = up."IdUsuario"
                WHERE u."Numero_Documento" = %s
                ORDER BY h."Fecha_Creacion" DESC;
                """, (documento,))
                return cur.fetchall()
        except Exception as e:
            return {"error": repr(e)}
        finally:
            if conn:
                conn.close()

