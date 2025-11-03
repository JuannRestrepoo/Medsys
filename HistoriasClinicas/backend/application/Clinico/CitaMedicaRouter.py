from fastapi import APIRouter
from domain.Clinico.CitaMedica.CitaMedicaModel import  CitaMedicaModel
from infrastructure.Clinico.CitaMedica.CitaMedicaInfrastructure import CitaMedicaInfrastructure

router = APIRouter(prefix="/citamedica", tags=["Clinico.CitaMedica"])
#Clinico.CitaMedica
#GET
@router.get(
    "/consultarcitamedica",
    summary = "Consultar Cita Medica",
    description = "Consultar Cita Medica - Get",
    tags = ["Clinico.CitaMedica"]
)
async def consultar_citamedica_por_id(idcita: str):
    return CitaMedicaInfrastructure.consultar_citamedica_por_id(idcita)

#POST

@router.post(
    "/ingresarcitamedica",
    summary="Ingresar Cita Medica",
    description="Ingresar Cita Medica - Post",
    tags=["Clinico.CitaMedica"]
)
async def ingresar_citamedica(cita: CitaMedicaModel):
    return CitaMedicaInfrastructure.ingresar_citamedica(cita)
    
    

#PUT
@router.put(
    "/modificarcitamedica",
    summary="Modificar Cita Medica",
    description="Modificar Cita Medica - Put",
    tags=["Clinico.CitaMedica"]
)
async def modificar_citamedica(idcita: str, cita: CitaMedicaModel):
    cita.idcita = idcita
    return CitaMedicaInfrastructure.modificar_citamedica(cita)

@router.put(
    "/desactivarcitamedica",
    summary="Desactivar Cita Medica",
    description="Modificar Cita Medica - Put",
    tags=["Clinico.CitaMedica"]
)
async def desactivar_citamedica(idcita: str):
    return CitaMedicaInfrastructure.desactivar_citamedica(idcita)
#DELETE

@router.delete(
    "/eliminarcitamedica",
    summary="Eliminar CitaMedica",
    description="Operacion CitaMedica delete",
    tags=["Clinico.CitaMedica"]
)
async def eliminar_citamedica(idcita: str):
    return CitaMedicaInfrastructure.eliminar_citamedica(idcita)