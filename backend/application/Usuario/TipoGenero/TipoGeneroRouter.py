from fastapi import APIRouter
from domain.Usuario.TipoGenero.TipoGeneroModel import TipoGeneroModel
from infrastructure.Usuario.TipoGenero.TipoGeneroInfrastructure import TipoGeneroInfrastructure

router = APIRouter(prefix="/tipogenero", tags=["Usuario.TipoGenero"])

#Usuario.TipoGenero
#GET
@router.get(
    "/tipogeneroget",
    summary = "Metodo TipoGenero Get",
    description = "Operacion TipoGenero Get",
    tags = ["Usuario.TipoGenero"]
)
async def consultar_tipogenero_por_id(idtipogenero: str):
    return TipoGeneroInfrastructure.consultar_tipogenero_por_id(idtipogenero)

#POST
@router.post(
    "/tipogeneropost",
    summary="Metodo TipoGenero Post",
    description="Operacion TipoGenero post",
    tags=["Usuario.TipoGenero"]
)
async def ingresar_tipogenero(tg: TipoGeneroModel):
    return TipoGeneroInfrastructure.ingresar_tipogenero(tg)


#PUT
@router.put(
    "/tipogeneroput",
    summary="Metodo TipoGenero Put",
    description="Operacion TipoGenero put",
    tags=["Usuario.TipoGenero"]
)
async def modificar_tipogenero(idtipogenero: str, tg: TipoGeneroModel):
    tg.idtipogenero = idtipogenero
    return TipoGeneroInfrastructure.modificar_tipogenero(tg)

#DELETE
@router.delete(
    "/tipogenerodelete",
    summary="Metodo TipoGenero delete",
    description="Operacion TipoGenero delete",
    tags=["Usuario.TipoGenero"]
)
async def eliminar_tipogenero(idtipogenero: str):
    return TipoGeneroInfrastructure.eliminar_tipogenero(idtipogenero)