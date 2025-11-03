import psycopg2
import psycopg2.extras
from domain.Clinico.RecetaMedica.RecetaMedicaModel import RecetaMedicaModel

class RecetaMedicaInfrastructure:

    @staticmethod
    def ingresar_recetamedica(receta: RecetaMedicaModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarRecetaMedica(%s,%s,%s,%s);",
                            (receta.iddiagnostico, receta.medicamento,
                             receta.dosis, receta.indicaciones))
                conn.commit()
                return {"mensaje": "Receta médica ingresada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_recetamedica(receta: RecetaMedicaModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarRecetaMedica(%s,%s,%s,%s,%s,%s);",
                            (receta.idreceta, receta.iddiagnostico,
                             receta.medicamento, receta.dosis,
                             receta.indicaciones,
                             '1' if receta.activo else '0'))
                conn.commit()
                return {"mensaje": "Receta médica modificada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def desactivar_recetamedica(idreceta: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarRecetaMedica(%s);", (idreceta,))
                conn.commit()
                return {"mensaje": f"Receta médica {idreceta} desactivada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_recetamedica(idreceta: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarRecetaMedica(%s);", (idreceta,))
                conn.commit()
                return {"mensaje": f"Receta médica {idreceta} eliminada físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_recetamedica_por_id(idreceta: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarRecetaMedicaPorId(%s);", (idreceta,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Receta médica no encontrada"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
