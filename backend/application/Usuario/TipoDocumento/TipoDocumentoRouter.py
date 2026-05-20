from fastapi import APIRouter
from domain.Usuario.TipoDocumento.TipoDocumentoModel import TipoDocumentoModel
from infrastructure.Usuario.TipoDocumento.TipoDocumentoInfrastructure import TipoDocumentoInfrastructure

router = APIRouter(prefix="/tipodocumento", tags=["Usuario.TipoDoducumento"])

#Usuario.TipoDocumento


@router.get(
    "/consultar",
    summary="Consultar Tipos de Documento",
    description="Devuelve todos los tipos de documento disponibles"
)
async def consultar_tipodocumentos():
    return TipoDocumentoInfrastructure.consultar_tipodocumentos()

#GET
@router.get(
    "/tipodocumentoget",
    summary="Metodo TipoDocumento Get",
    description="Operacion TipoDocumento Get"
)
async def consultar_tipodocumento_por_id(idtipodocumento: str):
    return TipoDocumentoInfrastructure.consultar_tipodocumento_por_id(idtipodocumento)

#POST
@router.post(
    "/tipodocumentopost",
    summary="Metodo TipoDocumento Post",
    description="Operacion TipoDocumento post",
    tags=["Usuario.TipoDocumento"]
)
async def ingresar_tipodocumento(td: TipoDocumentoModel):
    return TipoDocumentoInfrastructure.ingresar_tipodocumento(td)

#PUT
@router.put(
    "/tipodocumentoput",
    summary="Metodo TipoDocumento Put",
    description="Operacion TipoDocumento put",
    tags=["Usuario.TipoDocumento"]
)
async def modificar_tipodocumento(idtipodocumento: str, td: TipoDocumentoModel):
    td.idtipodocumento = idtipodocumento
    return TipoDocumentoInfrastructure.modificar_tipodocumento(td)

#DELETE
@router.delete(
    "/tipodocumentodelete",
    summary="Metodo TipoDocumento delete",
    description="Operacion TipoDocumento delete",
    tags=["Usuario.TipoDocumento"]
)
async def eliminar_tipodocumento(idtipodocumento: str):
    return TipoDocumentoInfrastructure.eliminar_tipodocumento(idtipodocumento)