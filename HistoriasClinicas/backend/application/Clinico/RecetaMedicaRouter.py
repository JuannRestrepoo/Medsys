from fastapi import APIRouter
from domain.Clinico.RecetaMedica.RecetaMedicaModel import RecetaMedicaModel
from infrastructure.Clinico.RecetaMedica.RecetaMedicaInfrastructure import RecetaMedicaInfrastructure

router = APIRouter(prefix="/recetamedica", tags=["Clinico.RecetaMedica"])

#Clinico.RecetaMedica
#GET
@router.get(
    "/recetamedicaget",
    summary = "Metodo RecetaMedica Get",
    description = "Operacion RecetaMedica Get",
    tags = ["Clinico.RecetaMedica"]
)
async def consultar_recetamedica_por_id(idreceta: str):
    return RecetaMedicaInfrastructure.consultar_recetamedica_por_id(idreceta)

#POST
@router.post(
    "/recetamedicapost",
    summary="Metodo RecetaMedica Post",
    description="Operacion RecetaMedica post",
    tags=["Clinico.RecetaMedica"]
)
async def ingresar_recetamedica(receta: RecetaMedicaModel):
    return RecetaMedicaInfrastructure.ingresar_recetamedica(receta)

#PUT
@router.put(
    "/desactivarrecetamedica",
    summary="Metodo RecetaMedica Put",
    description="Operacion RecetaMedica put",
    tags=["Clinico.RecetaMedica"]
)
async def desactivar_recetamedica(idreceta: str):
    return RecetaMedicaInfrastructure.desactivar_recetamedica(idreceta)
@router.put(
    "/recetamedicaput",
    summary="Metodo RecetaMedica Put",
    description="Operacion RecetaMedica put",
    tags=["Clinico.RecetaMedica"]
)
async def modificar_recetamedica(idreceta: str, receta: RecetaMedicaModel):
    receta.idreceta = idreceta
    return RecetaMedicaInfrastructure.modificar_recetamedica(receta)

#DELETE
@router.delete(
    "/recetamedicadelete",
    summary="Metodo RecetaMedica delete",
    description="Operacion RecetaMedica delete",
    tags=["Clinico.RecetaMedica"]
)
async def eliminar_recetamedica(idreceta: str):
    return RecetaMedicaInfrastructure.eliminar_recetamedica(idreceta)