import psycopg2
import psycopg2.extras
from fastapi import APIRouter

portal_paciente_router = APIRouter()

# Conexión a la BD
def get_conn():
    return psycopg2.connect(
        dbname='dbaMedSys',
        user='postgres',
        password='',   # si tu usuario no tiene contraseña, lo dejas vacío
        host='127.0.0.1',
        port='5432'
    )

# -----------------------------
# 📅 Citas próximas del paciente
# -----------------------------
@portal_paciente_router.get("/paciente/citas/proximas/{idpaciente}")
async def citas_proximas(idpaciente: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                '''
                SELECT c."IdCita", c."Fecha", c."Hora", p."Nombre_Completo" as profesional
                FROM "CitaMedica" c
                JOIN "Profesional" pr ON c."IdProfesional" = pr."IdProfesional"
                JOIN "Usuario" p ON pr."IdUsuario" = p."IdUsuario"
                WHERE c."IdPaciente" = %s AND c."Estado" = 'Pendiente'
                ORDER BY c."Fecha" ASC, c."Hora" ASC
                LIMIT 3
                ''',
                (idpaciente,)
            )
            return cur.fetchall()
    finally:
        conn.close()

# -----------------------------
# 💊 Recetas activas del paciente
# -----------------------------
@portal_paciente_router.get("/paciente/recetas/activas/{idpaciente}")
async def recetas_activas(idpaciente: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                '''
                SELECT r."IdReceta",
                       r."Medicamento",
                       r."Dosis",
                       r."Indicaciones",
                       u."Nombre_Completo" AS profesional
                FROM "RecetaMedica" r
                JOIN "Profesional" p ON r."IdProfesional" = p."IdProfesional"
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                WHERE r."IdPaciente" = %s AND r."Activo" = B'1'
                ORDER BY r."IdReceta" DESC
                ''',
                (idpaciente,)
            )
            return cur.fetchall()
    finally:
        conn.close()

# -----------------------------------------------
# 📂 Resultados pendientes de ver o descargar
# -----------------------------------------------
@portal_paciente_router.get("/paciente/resultados/pendientes/{idpaciente}")
async def resultados_pendientes(idpaciente: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                '''
                SELECT r."IdResultado",
                       r."Titulo",
                       r."Descripcion",
                       r."Archivo",
                       r."Fecha_Creacion",
                       r."Activo"
                FROM "Resultados" r
                WHERE r."IdPaciente" = %s AND r."Activo" = true
                ORDER BY r."Fecha_Creacion" DESC
                ''',
                (idpaciente,)
            )
            rows = cur.fetchall()
            return {"pendientes": len(rows), "resultados": rows}
    finally:
        conn.close()
