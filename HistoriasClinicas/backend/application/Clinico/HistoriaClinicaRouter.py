from fastapi import APIRouter
from domain.Clinico.HistoriaClinica.HistoriaClinicaModel import  HistoriaClinicaModel
from infrastructure.Clinico.HistoriaClinica.HistoriaClinicaInfrastructure import HistoriaClinicaInfrastructure
import psycopg2
import psycopg2.extras

router = APIRouter(prefix="/historiaclinica", tags=["Clinico.HistoriaClinica"])



##RESOLVER DOCUMENTO -- ID PACIENTE

@router.get(
    "/paciente/{documento}",
    summary="Listar historias clínicas de un paciente",
    description="Devuelve todas las historias clínicas asociadas al documento del paciente",
    tags=["Clinico.HistoriaClinica"]
)
async def listar_historias_paciente(documento: str):
    return HistoriaClinicaInfrastructure.listar_historias_por_documento(documento)



##historias clinicas recientes


@router.get("/recientes/{idprofesional}")
async def historias_recientes(idprofesional: str):
    # 🔧 Conexión directa a la BD con tus credenciales
    conn = psycopg2.connect(
        dbname='dbaMedSys',
        user='postgres',
        password='',        # si tu usuario no tiene contraseña, lo dejas vacío
        host='127.0.0.1',
        port='5432'
    )
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                '''
                SELECT h."IdHistoria" as idhistoria,
                       u."Nombre_Completo" as paciente,
                       u."Numero_Documento" as documento,
                       h."Fecha_Creacion" as fecha,
                       h."Antecedentes" as antecedentes,
                       h."Observaciones" as observaciones
                FROM "HistoriaClinica" h
                JOIN "Paciente" p ON h."IdPaciente" = p."IdPaciente"
                JOIN "Usuario" u ON p."IdUsuario" = u."IdUsuario"
                WHERE h."IdProfesional" = %s
                ORDER BY h."Fecha_Creacion" DESC
                LIMIT 5
                ''',
                (idprofesional,)
            )
            return cur.fetchall()
    finally:
        conn.close()


#Clinico.HistoriaClinica
#GET
@router.get(
    "/consultarhistoriaclinica",
    summary = "Consultar Historia Clinica (ID)",
    description = "Consultar Historia Clinica (ID) - Get",
    tags = ["Clinico.HistoriaClinica"]
)
async def consultar_historiaclinica_por_id(idhistoria: str):
    return HistoriaClinicaInfrastructure.consultar_historiaclinica_por_id(idhistoria)


#POST

@router.post(
    "/ingresarhistoriaclinica",
    summary="Ingresar Historia Clinica",
    description="Ingresar Historia Clinica - Post",
    tags=["Clinico.HistoriaClinica"]
)

async def ingresar_historiaclinica(historia: HistoriaClinicaModel):
    return HistoriaClinicaInfrastructure.ingresar_historiaclinica(historia)

#PUT
@router.put(
    "/historiaclinicaput",
    summary="Metodo HistoriaClinica Put",
    description="Operacion HistoriaClinica put",
    tags=["Clinico.HistoriaClinica"]
)
async def modificar_historiaclinica(idhistoria: str, historia: HistoriaClinicaModel):
    historia.idhistoria = idhistoria
    return HistoriaClinicaInfrastructure.modificar_historiaclinica(historia)

#DELETE
@router.put(
    "/desactivarhistoriaclinica",
    summary="Desactivar HistoriaClinica delete",
    description="Desactivar HistoriaClinica delete",
    tags=["Clinico.HistoriaClinica"]
)
async def desactivar_historiaclinica(idhistoria: str):
    return HistoriaClinicaInfrastructure.desactivar_historiaclinica(idhistoria)

@router.delete(
    "/historiaclinicadelete",
    summary="Metodo HistoriaClinica delete",
    description="Operacion HistoriaClinica delete",
    tags=["Clinico.HistoriaClinica"]
)
async def eliminar_historiaclinica(idhistoria: str):
    return HistoriaClinicaInfrastructure.eliminar_historiaclinica(idhistoria)
