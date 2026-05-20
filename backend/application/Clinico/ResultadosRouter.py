from fastapi import APIRouter
import os
from fastapi import UploadFile, File
from domain.Clinico.Resultados.ResultadosModel import ResultadosModel
from infrastructure.Clinico.Resultados.ResultadosInfrastrucure import ResultadosInfrastructure

router = APIRouter(prefix="/resultados", tags=["Clinico.Resultados"])

@router.post(
    "/registrar",
    summary="Registrar resultado",
    description="El profesional registra un resultado para un paciente",
    tags=["Clinico.Resultados"]
)
async def registrar_resultado(resultado: ResultadosModel):
    return ResultadosInfrastructure.registrar_resultado(resultado)

@router.get(
    "/paciente/{documento}",
    summary="Listar resultados de un paciente",
    description="Devuelve todos los resultados asociados al documento del paciente",
    tags=["Clinico.Resultados"]
)
async def listar_resultados_paciente(documento: str):
    return ResultadosInfrastructure.listar_resultados_por_documento(documento)


@router.post("/subir-archivo")
async def subir_archivo(file: UploadFile = File(...)):
    file_path = os.path.join("uploads", file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"archivo": file.filename}