from fastapi import APIRouter
from domain.Servicios.TipoServicio.TipoServicioModel import TipoServicioModel
from infrastructure.Servicios.TipoServicio.TipoServicioInfrastructure import TipoServicioInfrastructure

router = APIRouter(prefix="/tiposervicio", tags=["Servicios.TipoServicio"])

#Servicios.TipoServicio

#GET
@router.get(
    "/tiposervicioget",
    summary="Metodo TipoServicio Get",
    description="Operacion TipoServicio Get",
    tags=["Servicios.TipoServicio"]
)
async def consultar_tiposervicio_por_id(idtiposervicio: str):
    return TipoServicioInfrastructure.consultar_tiposervicio_por_id(idtiposervicio)

#POST
@router.post(
    "/tiposerviciopost",
    summary="Metodo TipoServicio Post",
    description="Operacion TipoServicio Post",
    tags=["Servicios.TipoServicio"]
)
async def ingresar_tiposervicio(ts: TipoServicioModel):
    return TipoServicioInfrastructure.ingresar_tiposervicio(ts)

#PUT
@router.put(
    "/tiposervicioput",
    summary="Metodo TipoServicio Put",
    description="Operacion TipoServicio Put",
    tags=["Servicios.TipoServicio"]
)
async def modificar_tiposervicio(idtiposervicio: str, ts: TipoServicioModel):
    ts.idtiposervicio = idtiposervicio
    return TipoServicioInfrastructure.modificar_tiposervicio(ts)

@router.put(
    "/descativar tiposervicio",
    summary="Metodo TipoServicio Put",
    description="Operacion TipoServicio Put",
    tags=["Servicios.TipoServicio"]
)
async def desactivar_tiposervicio(idtiposervicio: str):
    return TipoServicioInfrastructure.desactivar_tiposervicio(idtiposervicio)

#DELETE
@router.delete(
    "/tiposerviciodelete",
    summary="Metodo TipoServicio Delete",
    description="Operacion TipoServicio Delete",
    tags=["Servicios.TipoServicio"]
)
async def eliminar_tiposervicio(idtiposervicio: str):
    return TipoServicioInfrastructure.eliminar_tiposervicio(idtiposervicio)