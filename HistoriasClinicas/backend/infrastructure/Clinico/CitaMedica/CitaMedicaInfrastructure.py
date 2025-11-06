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

    @staticmethod
    def listar_citas_pendientes():
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
                    SELECT c."IdCita",
                           c."Fecha",
                           c."Hora",
                           c."Motivo",
                           c."Estado",
                           u."Nombre_Completo"   AS "NombrePaciente",
                           u."Numero_Documento"  AS "Documento",
                           u."Telefono"          AS "Telefono",
                           u."Correo"            AS "Correo"
                    FROM "CitaMedica" c
                    JOIN "Paciente" p ON c."IdPaciente" = p."IdPaciente"
                    JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                    WHERE c."Estado" = 'Pendiente' AND c."Activo" = B'1'
                    ORDER BY c."Fecha", c."Hora";
                """)
                return cur.fetchall()
        except Exception as e:
            return {"error": repr(e)}
        finally:
            if conn:
                conn.close()
    @staticmethod
    def listar_citas_por_documento(documento: str):
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
                SELECT c."IdCita" AS idcita,
                    c."Fecha" AS fecha,
                    c."Hora" AS hora,
                    c."Motivo" AS motivo,
                    c."Estado" AS estado,
                    pr."IdProfesional" AS idprofesional,
                    up."Nombre_Completo" AS nombre_profesional,
                    ce."Direccion" AS direccion_centro,
                    ci."Nombre" AS ciudad_centro
                FROM "CitaMedica" c
                JOIN "Paciente" p ON c."IdPaciente" = p."IdPaciente"
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                JOIN "Profesional" pr ON c."IdProfesional" = pr."IdProfesional"
                JOIN "Usuario" up ON pr."IdUsuario" = up."IdUsuario"
                JOIN "Centro" ce ON pr."IdCentro" = ce."IdCentro"
                JOIN "Ciudad" ci ON ce."IdCiudad" = ci."IdCiudad"
                WHERE u."Numero_Documento" = %s
                ORDER BY c."Fecha" DESC, c."Hora" DESC;
                """, (documento,))
                return cur.fetchall()
        except Exception as e:
            return {"error": repr(e)}
        finally:
            if conn:
                conn.close()
