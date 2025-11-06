import psycopg2
import psycopg2.extras
from domain.Clinico.RecetaMedica.RecetaMedicaModel import RecetaMedicaModel

class RecetaMedicaInfrastructure:

    @staticmethod
    def ingresar_recetamedica(receta: RecetaMedicaModel):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT spaIngresarRecetaMedica(%s, %s, %s, %s, %s);
                """, (
                    receta.medicamento,
                    receta.dosis,
                    receta.indicaciones,
                    receta.idpaciente,
                    receta.idprofesional
                ))
                conn.commit()
                return {"mensaje": "Receta médica ingresada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

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

#OBTENER RECETAS MEDICAS DE LA BASE DE DATOS PARA QUE SEAN VISIBLES PARA EL PACIENTE
    @staticmethod
    def listar_recetas_por_documento(documento: str):
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
                SELECT r."IdReceta" AS idreceta,
                    r."Medicamento" AS medicamento,
                    r."Dosis" AS dosis,
                    r."Indicaciones" AS indicaciones,
                    r."Activo" AS activo,
                    pr."IdProfesional" AS idprofesional,
                    up."Nombre_Completo" AS nombre_profesional
                FROM "RecetaMedica" r
                JOIN "Paciente" p ON r."IdPaciente" = p."IdPaciente"
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                JOIN "Profesional" pr ON r."IdProfesional" = pr."IdProfesional"
                JOIN "Usuario" up ON pr."IdUsuario" = up."IdUsuario"
                WHERE u."Numero_Documento" = %s
                ORDER BY r."IdReceta" DESC;
                """, (documento,))
                return cur.fetchall()
        except Exception as e:
            return {"error": repr(e)}
        finally:
            if conn:
                conn.close()