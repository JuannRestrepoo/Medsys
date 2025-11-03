from fastapi import APIRouter
from domain.Clinico.HistoriaClinica.HistoriaClinicaModel import  HistoriaClinicaModel
from infrastructure.Clinico.HistoriaClinica.HistoriaClinicaInfrastructure import HistoriaClinicaInfrastructure

router = APIRouter(prefix="/historiaclinica", tags=["Clinico.HistoriaClinica"])


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
