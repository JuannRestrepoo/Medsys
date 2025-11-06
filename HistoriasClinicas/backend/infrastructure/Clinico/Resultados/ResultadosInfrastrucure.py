import psycopg2
import psycopg2.extras
from domain.Clinico.Resultados.ResultadosModel import ResultadosModel

class ResultadosInfrastructure:

    @staticmethod
    def registrar_resultado(resultado: ResultadosModel):
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
                    INSERT INTO "Resultados"(
                        "IdPaciente", "IdProfesional", "Titulo", "Descripcion", "Archivo", "Activo"
                    )
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, (
                    resultado.idpaciente,
                    resultado.idprofesional,
                    resultado.titulo,
                    resultado.descripcion,
                    resultado.archivo,
                    resultado.activo
                ))
                conn.commit()
                return {"mensaje": "Resultado registrado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

    @staticmethod
    def listar_resultados_por_documento(documento: str):
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
                SELECT r."IdResultado" AS idresultado,
                       r."Titulo" AS titulo,
                       r."Descripcion" AS descripcion,
                       r."Archivo" AS archivo,
                       r."Fecha_Creacion" AS fecha,
                       r."Activo" AS activo,
                       pr."IdProfesional" AS idprofesional,
                       up."Nombre_Completo" AS nombre_profesional
                FROM "Resultados" r
                JOIN "Paciente" p ON r."IdPaciente" = p."IdPaciente"
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                JOIN "Profesional" pr ON r."IdProfesional" = pr."IdProfesional"
                JOIN "Usuario" up ON pr."IdUsuario" = up."IdUsuario"
                WHERE u."Numero_Documento" = %s
                ORDER BY r."Fecha_Creacion" DESC;
                """, (documento,))
                return cur.fetchall()
        except Exception as e:
            return {"error": repr(e)}
        finally:
            if conn:
                conn.close()
