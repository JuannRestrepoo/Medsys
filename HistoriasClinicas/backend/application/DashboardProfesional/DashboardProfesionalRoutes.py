from fastapi import APIRouter, HTTPException
import psycopg2
import psycopg2.extras

dashboard_router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

def get_conn():
    return psycopg2.connect(
        dbname="dbaMedSys",
        user="postgres",
        password="",
        host="127.0.0.1",
        port="5432"
    )

# ------------------- CITAS -------------------

@dashboard_router.get("/citas/hoy/{idprofesional}")
async def citas_hoy(idprofesional: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                '''SELECT * FROM "CitaMedica"
                   WHERE "IdProfesional" = %s
                   AND DATE("Fecha") = CURRENT_DATE''',
                (idprofesional,)
            )
            return cur.fetchall()
    finally:
        conn.close()

@dashboard_router.get("/citas/semana/{idprofesional}")
async def citas_semana(idprofesional: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                '''SELECT * FROM "CitaMedica"
                   WHERE "IdProfesional" = %s
                   AND DATE("Fecha") BETWEEN CURRENT_DATE AND CURRENT_DATE + interval '7 days' ''',
                (idprofesional,)
            )
            return cur.fetchall()
    finally:
        conn.close()

@dashboard_router.get("/citas/pendientes")
async def citas_pendientes():
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute('SELECT * FROM "CitaMedica" WHERE "Estado" = %s', ("Pendiente",))
            return cur.fetchall()
    finally:
        conn.close()

# ------------------- PACIENTES -------------------

@dashboard_router.get("/pacientes/{idprofesional}")
async def pacientes_profesional(idprofesional: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                '''
                SELECT DISTINCT p."IdPaciente" as idpaciente,
                                u."Nombre_Completo" as nombre,
                                u."Numero_Documento" as documento
                FROM "CitaMedica" c
                JOIN "Paciente" p ON c."IdPaciente" = p."IdPaciente"
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                WHERE c."IdProfesional" = %s
                ORDER BY p."IdPaciente" DESC
                ''',
                (idprofesional,)
            )
            return cur.fetchall()
    finally:
        conn.close()

@dashboard_router.get("/pacientes/recientes/{idprofesional}")
async def pacientes_recientes(idprofesional: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                '''
                SELECT DISTINCT ON (p."IdPaciente")
                    p."IdPaciente" as idpaciente,
                    u."Nombre_Completo" as nombre,
                    u."Numero_Documento" as documento,
                    c."Fecha" as fecha
                FROM "CitaMedica" c
                JOIN "Paciente" p ON c."IdPaciente" = p."IdPaciente"
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                WHERE c."IdProfesional" = %s
                ORDER BY p."IdPaciente", c."Fecha" DESC
                LIMIT 5
                ''',
                (idprofesional,)
            )
            return cur.fetchall()
    finally:
        conn.close()

# ------------------- HISTORIAS -------------------

@dashboard_router.get("/historias/{idprofesional}")
async def historias_profesional(idprofesional: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                '''SELECT h."IdHistoria" as idhistoria,
                          u."Nombre_Completo" as paciente,
                          h."Fecha_Creacion" as fecha
                   FROM "HistoriaClinica" h
                   JOIN "Paciente" p ON h."IdPaciente" = p."IdPaciente"
                   JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                   WHERE h."IdProfesional" = %s
                   ORDER BY h."Fecha_Creacion" DESC''',
                (idprofesional,)
            )
            return cur.fetchall()
    finally:
        conn.close()

# ------------------- RECETAS -------------------

@dashboard_router.get("/recetas/pendientes/{idprofesional}")
async def recetas_pendientes(idprofesional: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                '''
                SELECT r."IdReceta" as idreceta,
                       u."Nombre_Completo" as paciente,
                       r."Medicamento" as medicamento
                FROM "RecetaMedica" r
                JOIN "Paciente" p ON r."IdPaciente" = p."IdPaciente"
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                WHERE r."IdProfesional" = %s
                ORDER BY r."IdReceta" DESC
                ''',
                (idprofesional,)
            )
            return cur.fetchall()
    finally:
        conn.close()

# ------------------- PACIENTES NUEVOS -------------------

@dashboard_router.get("/pacientes/nuevos/{idprofesional}")
async def pacientes_nuevos(idprofesional: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                '''
                SELECT DISTINCT ON (p."IdPaciente")
                       p."IdPaciente" as idpaciente,
                       u."Nombre_Completo" as nombre,
                       u."Numero_Documento" as documento,
                       c."Fecha" as fecha_cita,
                       'Nuevo' as flag
                FROM "CitaMedica" c
                JOIN "Paciente" p ON c."IdPaciente" = p."IdPaciente"
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                WHERE c."IdProfesional" = %s
                  AND c."Fecha" >= CURRENT_DATE - interval '7 days'
                ORDER BY p."IdPaciente", c."Fecha" DESC
                ''',
                (idprofesional,)
            )
            return cur.fetchall()
    finally:
        conn.close()


# ------------------- MENSAJES FUNCIONALIDAD POSTERIOR(AUN NO)-------------------

#@dashboard_router.get("/mensajes/{idprofesional}")
#async def mensajes_profesional(idprofesional: str):
#    conn = get_conn()
#    try:
#        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
#            cur.execute(
#                '''SELECT * FROM "Mensaje"
#                   WHERE "IdProfesional" = %s
#                   ORDER BY "Fecha" DESC''',
#                (idprofesional,)
#            )
#            return cur.fetchall()
#    finally:
#        conn.close()

# ------------------- REPORTES -------------------

@dashboard_router.get("/reportes/{idprofesional}")
async def reporte_profesional(idprofesional: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            # Total de citas finalizadas
            cur.execute(
                '''
                SELECT COUNT(*) as atendidos
                FROM "CitaMedica"
                WHERE "IdProfesional" = %s AND "Estado" = %s
                ''',
                (idprofesional, "Finalizada")
            )
            atendidos = cur.fetchone()["atendidos"]

        return {"atendidos": atendidos, "frecuentes": []}
    finally:
        conn.close()

# ------------------- CONFIGURACIÓN -------------------

@dashboard_router.get("/perfil/{idprofesional}")
async def perfil_profesional(idprofesional: str):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute('SELECT * FROM "Profesional" WHERE "IdProfesional" = %s', (idprofesional,))
            return cur.fetchone()
    finally:
        conn.close()

@dashboard_router.put("/perfil/{idprofesional}/disponibilidad")
async def actualizar_disponibilidad(idprofesional: str, payload: dict):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                'UPDATE "Profesional" SET "Disponibilidad" = %s WHERE "IdProfesional" = %s',
                (payload.get("disponibilidad"), idprofesional)
            )
            conn.commit()
        return {"mensaje": "Disponibilidad actualizada"}
    finally:
        conn.close()
