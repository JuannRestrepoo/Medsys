from fastapi import APIRouter
from domain.Organizacion.Centro.CentroModel import  CentroModel
from infrastructure.Organizacion.CentroInfrastructure import CentroInfrastructure
from infrastructure.Usuario.Profesional.ProfesionalInfrastructure import ProfesionalInfrastructure
router = APIRouter(prefix="/centro", tags=["Organizacion.Centro"])



#Profesionales de un centro:

@router.get("/profesionales/centro/{idcentro}")
def listar_profesionales_centro(idcentro: str):
    return ProfesionalInfrastructure.listar_profesionales_centro(idcentro)


#Organizacion.Centro

#CONSULTAR CENTROS EN CIUDAD
@router.get(
    "/consultarcentros",
    summary="Consultar Centros",
    description="Consultar Centros - SELECT",
    tags=["Organizacion.Centro"]
)
async def consultar_centro():
    return CentroInfrastructure.consultar_centro()

#CONSULTAR CENTRO POR ID
@router.get(
    "/consultarcentroporid",
    summary="Consultar Centro Por ID",
    description="Consultar Centro Por ID - SELECT",
    tags=["Organizacion.Centro"]
)
async def consultar_centro_por_id(idcentro: str):
    return CentroInfrastructure.consultar_centro_por_id(idcentro)

#INGRESAR CENTRO 
@router.post(
    "/ingresarcentro",
    summary="Ingresar Centro",
    description="Ingresar Centro - Post",
    tags=["Organizacion.Centro"]
)
async def ingresar_centro(centromodel: CentroModel):
    return CentroInfrastructure.ingresar_centro(centromodel)

#MODIFICAR CENTRO 
@router.put(
    "/modificarcentro",
    summary="Modificar Centro Put",
    description="Modificar Centro - Put",
    tags=["Organizacion.Centro"]
)
async def modificar_centro(idcentro: str, centro: CentroModel):
    centro.idcentro = idcentro
    return CentroInfrastructure.modificar_centro(centro)

#DESACTIVAR CENTRO

@router.put(
    "/desactivarcentro",
    summary="Modificar Centro Put",
    description="Modificar Centro - Put",
    tags=["Organizacion.Centro"]
)
async def desactivar_centro(idcentro: str):
    return CentroInfrastructure.desactivar_centro(idcentro)


#ELIMINAR CENTRO 
@router.delete(
    "/eliminarcentro",
    summary="Eliminar Centro",
    description="Eliminar Centro - Delete",
    tags=["Organizacion.Centro"]
)
async def eliminar_centro(idcentro: str):
    return CentroInfrastructure.eliminar_centro(idcentro)