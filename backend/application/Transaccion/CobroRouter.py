from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import psycopg2
import psycopg2.extras
import os

router = APIRouter()

# --- Registrar Cobro ---
@router.post("/cobro/registrar")
async def registrar_cobro(payload: dict):
    conn = psycopg2.connect(
        dbname="dbaMedSys",
        user="postgres",
        password="",
        host="127.0.0.1",
        port="5432"
    )
    try:
        with conn.cursor() as cur:
            cur.execute(
                '''
                INSERT INTO "Cobro" 
                ("IdPaciente","IdProfesional","IdCentro","ProductoServicio","Total","Activo","Fecha")
                VALUES (%s,%s,%s,%s,%s,%s,%s)
                RETURNING "IdCobro"
                ''',
                (
                    payload["idpaciente"],
                    payload["idprofesional"],
                    payload["idcentro"],        # 👈 ahora sí lo mandamos
                    payload["productoservicio"],
                    payload["total"],
                    payload["activo"],
                    payload["fecha"]
                )
            )
            idcobro = cur.fetchone()[0]
            conn.commit()
        return {"mensaje": "Cobro registrado", "idcobro": idcobro}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()



# --- Generar Factura ---
@router.post("/cobro/{idcobro}/generar-factura")
async def generar_factura(idcobro: str):
    conn = psycopg2.connect(
        dbname="dbaMedSys",
        user="postgres",
        password="",
        host="127.0.0.1",
        port="5432"
    )
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            # Buscar el cobro
            cur.execute('SELECT * FROM "Cobro" WHERE "IdCobro" = %s', (idcobro,))
            cobro = cur.fetchone()
            if not cobro:
                raise HTTPException(status_code=404, detail="Cobro no encontrado")

            # Crear archivo de factura
            os.makedirs("uploads/facturas", exist_ok=True)
            nombre_archivo = f"factura_{idcobro}.txt"
            ruta = os.path.join("uploads", "facturas", nombre_archivo)

            with open(ruta, "w", encoding="utf-8") as f:
                f.write("FACTURA\n")
                f.write(f"ID Cobro: {cobro['IdCobro']}\n")
                f.write(f"Servicio: {cobro['ProductoServicio']}\n")
                f.write(f"Fecha: {cobro['Fecha']}\n")
                f.write(f"Monto: {cobro['Total']}\n")
                f.write(f"Profesional: {cobro['IdProfesional']}\n")
                f.write(f"Paciente: {cobro['IdPaciente']}\n")

            # Actualizar la BD con el nombre del archivo
            cur.execute(
                'UPDATE "Cobro" SET "ArchivoFactura" = %s WHERE "IdCobro" = %s',
                (nombre_archivo, idcobro)
            )
            conn.commit()

        # Devolver el archivo generado
        return FileResponse(ruta, media_type="text/plain", filename=nombre_archivo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


@router.get("/cobro/paciente/{documento}")
async def listar_cobros_paciente(documento: str):
    conn = psycopg2.connect(
        dbname="dbaMedSys",
        user="postgres",
        password="",
        host="127.0.0.1",
        port="5432"
    )
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            # 1. Buscar paciente por documento en la tabla Usuario
            cur.execute(
                '''
                SELECT p."IdPaciente"
                FROM "Paciente" p
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                WHERE u."Numero_Documento" = %s
                ''',
                (documento,)
            )
            paciente = cur.fetchone()
            if not paciente:
                raise HTTPException(status_code=404, detail="Paciente no encontrado")

            # 2. Listar cobros del paciente
            cur.execute(
                '''
                SELECT c."IdCobro" as idcobro,
                       c."Fecha" as fecha,
                       c."ProductoServicio" as productoservicio,
                       c."Total" as total,
                       c."Activo" as activo,
                       c."ArchivoFactura" as archivofactura,
                       u_prof."Nombre_Completo" as nombre_profesional,
                       ce."Nombre" as nombre_centro
                FROM "Cobro" c
                JOIN "Profesional" pr ON c."IdProfesional" = pr."IdProfesional"
                JOIN "Usuario" u_prof ON pr."IdUsuario" = u_prof."IdUsuario"
                JOIN "Centro" ce ON c."IdCentro" = ce."IdCentro"
                WHERE c."IdPaciente" = %s
                ORDER BY c."Fecha" DESC
                ''',
                (paciente["IdPaciente"],)
            )
            cobros = cur.fetchall()

        return cobros
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
