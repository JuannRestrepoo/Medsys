from fastapi import APIRouter
from domain.Geografia.Ciudad.CiudadModel import CiudadModel
from infrastructure.Geografia.Ciudad.CiudadInfrastructure import CiudadInfrastructure

router = APIRouter(prefix="/ciudad", tags=["Geografia.Ciudad"])

# CONSULTAR CIUDADES
@router.get(
    "/consultarciudad",
    summary="Consultar Ciudad",
    description="Consultar Ciudad - SELECT"
)
async def consultar_ciudad():
    return CiudadInfrastructure.consultar_ciudad()

# CONSULTAR CIUDADES POR ID
@router.get(
    "/consultarciudadporid",
    summary="Consultar Ciudad Por ID",
    description="Consultar Ciudad Por ID - SELECT"
)
async def consultar_ciudad_por_id(idciudad: str):
    return CiudadInfrastructure.consultar_ciudad_por_id(idciudad)

# INGRESAR CIUDAD
@router.post(
    "/ingresarciudad",
    summary="Ingresar Ciudad",
    description="Ingresar Ciudad - POST"
)
async def ingresar_ciudad(ciudadmodel: CiudadModel):
    return CiudadInfrastructure.ingresar_ciudad(ciudadmodel)

# MODIFICAR CIUDAD
@router.put(
    "/modificarciudad",
    summary="Modificar Ciudad",
    description="Modificar Ciudad - PUT"
)
async def modificar_ciudad(idciudad: str, ciudad: CiudadModel):
    ciudad.idciudad = idciudad
    return CiudadInfrastructure.modificar_ciudad(ciudad)

# DESACTIVAR CIUDAD
@router.put(
    "/desactivarciudad",
    summary="Desactivar Ciudad",
    description="Desactivar Ciudad - PUT"
)
async def desactivar_ciudad(idciudad: str):
    return CiudadInfrastructure.desactivar_ciudad(idciudad)

# ELIMINAR CIUDAD
@router.delete(
    "/eliminarciudad",
    summary="Eliminar Ciudad",
    description="Eliminar Ciudad - DELETE"
)
async def eliminar_ciudad(idciudad: str):
    return CiudadInfrastructure.eliminar_ciudad(idciudad)