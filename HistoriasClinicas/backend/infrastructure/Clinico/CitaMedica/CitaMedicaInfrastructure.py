import psycopg2
import psycopg2.extras
from domain.Clinico.CitaMedica.CitaMedicaModel import CitaMedicaModel

class CitaMedicaInfrastructure:

    @staticmethod
    def ingresar_citamedica(cita: CitaMedicaModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarCitaMedica(%s,%s,%s,%s,%s,%s);",
                            (cita.idpaciente, cita.idprofesional,
                             cita.fecha, cita.hora, cita.motivo, cita.estado))
                conn.commit()
                return {"mensaje": "Cita médica ingresada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_citamedica(cita: CitaMedicaModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarCitaMedica(%s,%s,%s,%s,%s,%s,%s,%s);",
                            (cita.idcita, cita.idpaciente, cita.idprofesional,
                             cita.fecha, cita.hora, cita.motivo, cita.estado,
                             '1' if cita.activo else '0'))
                conn.commit()
                return {"mensaje": "Cita médica modificada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Desactivar (borrado lógico)
    @staticmethod
    def desactivar_citamedica(idcita: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarCitaMedica(%s);", (idcita,))
                conn.commit()
                return {"mensaje": f"Cita médica {idcita} desactivada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Eliminar (borrado físico)
    @staticmethod
    def eliminar_citamedica(idcita: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarCitaMedica(%s);", (idcita,))
                conn.commit()
                return {"mensaje": f"Cita médica {idcita} eliminada físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_citamedica_por_id(idcita: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarCitaMedicaPorId(%s);", (idcita,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Cita médica no encontrada"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()