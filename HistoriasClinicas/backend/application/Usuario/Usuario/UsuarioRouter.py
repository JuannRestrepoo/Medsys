from fastapi import APIRouter
from domain.Usuario.Usuario.UsuarioModel import UsuarioModel
from infrastructure.Usuario.Usuario.UsuarioInfrastructure import UsuarioInfrastructure

router = APIRouter(prefix="/usuario", tags=["Usuario.Usuario"])

#Usuario.Usuario
#GET
@router.get(
    "/consultarusuarioporid",
    summary = "Consultar Usuario Por ID ",
    description = "Consultar Usuario Por ID - Get",
    tags = ["Usuario.Usuario"]
)
async def consultar_usuario_por_id(idusuario: str):
    return UsuarioInfrastructure.consultar_usuario_por_id(idusuario)

#POST
@router.post(
    "/ingresarusuario",
    summary="Ingresar Usuario",
    description="Ingresar Usuario - Post",
    tags=["Usuario.Usuario"]
)
async def ingresar_usuario(usuario: UsuarioModel):
    return UsuarioInfrastructure.ingresar_usuario(usuario)
#PUT
@router.put(
    "/usuarioput",
    summary="Metodo Usuario Put",
    description="Operacion Usuario put",
    tags=["Usuario.Usuario"]
)
async def modificar_usuario(idusuario: str, usuario: UsuarioModel):
    usuario.idusuario = idusuario
    return UsuarioInfrastructure.modificar_usuario(usuario)


@router.put(
    "/desactivarusuario",
    summary="Metodo Usuario Put",
    description="Operacion Usuario put",
    tags=["Usuario.Usuario"]
)
async def desactivar_usuario(idusuario: str):
    return UsuarioInfrastructure.desactivar_usuario(idusuario)


#DELETE
@router.delete(
    "/usuariodelete",
    summary="Metodo Usuario delete",
    description="Operacion Usuario delete",
    tags=["Usuario.Usuario"]
)
async def eliminar_usuario(idusuario: str):
    return UsuarioInfrastructure.eliminar_usuario(idusuario)
