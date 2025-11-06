import psycopg2
import psycopg2.extras
from domain.Transaccion.CobroModel import CobroModel

class CobroInfrastructure:

    @staticmethod
    def registrar_cobro(cobro: CobroModel):
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
                # 1. Buscar el centro asociado al profesional
                cur.execute("""
                    SELECT "IdCentro"
                    FROM "Profesional"
                    WHERE "IdProfesional" = %s
                """, (cobro.idprofesional,))
                row = cur.fetchone()
                if not row:
                    return {"error": "No se encontró centro para el profesional"}
                idcentro = row[0]

                # 2. Insertar el cobro con el centro encontrado
                cur.execute("""
                    INSERT INTO "Cobro"(
                        "IdPaciente", "IdProfesional", "IdCentro",
                        "ProductoServicio", "Total", "Activo"
                    )
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING "IdCobro";
                """, (
                    cobro.idpaciente,
                    cobro.idprofesional,
                    idcentro,
                    cobro.productoservicio,
                    cobro.total,
                    cobro.activo
                ))
                idcobro = cur.fetchone()[0]
                conn.commit()
                return {"mensaje": "Cobro registrado correctamente", "idcobro": idcobro}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

    @staticmethod
    def listar_cobros_por_paciente(documento: str):
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
                SELECT c."IdCobro" AS idcobro,
                       c."Fecha" AS fecha,
                       c."ProductoServicio" AS productoservicio,
                       c."Total" AS total,
                       c."Activo" AS activo,
                       pr."IdProfesional" AS idprofesional,
                       up."Nombre_Completo" AS nombre_profesional,
                       ce."Nombre" AS nombre_centro
                FROM "Cobro" c
                JOIN "Paciente" p ON c."IdPaciente" = p."IdPaciente"
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                JOIN "Profesional" pr ON c."IdProfesional" = pr."IdProfesional"
                JOIN "Usuario" up ON pr."IdUsuario" = up."IdUsuario"
                JOIN "Centro" ce ON c."IdCentro" = ce."IdCentro"
                WHERE u."Numero_Documento" = %s
                ORDER BY c."Fecha" DESC;
                """, (documento,))
                return cur.fetchall()
        except Exception as e:
            return {"error": repr(e)}
        finally:
            if conn:
                conn.close()
