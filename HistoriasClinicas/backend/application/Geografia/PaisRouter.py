from fastapi import APIRouter
from domain.Geografia.Pais.PaisModel import PaisModel
from infrastructure.Geografia.Pais.PaisInfrastructure import PaisInfrastructure

router = APIRouter(prefix="/pais", tags=["Geografia.Pais"])
#Geografia.Pais

#CONSULTAR PAISES
@router.get(
    "/consultarpaises",
    summary = "Consultar Paises",
    description = "Consultar Paises - Select",
    tags = ["Geografia.Pais"]
)
async def consultar_pais():
    return PaisInfrastructure.consultar_pais()

#CONSULTAR PAIS POR ID
@router.get(
    "/consultarpaisid",
    summary="Consultar Pais Id",
    description="Consultar Pais Id - Select",
    tags=["Geografia.Pais"]
)
async def consultar_pais_por_id(idpais: str):
    return PaisInfrastructure.consultar_pais_por_id(idpais)

#CONSULTAR PAISES ACTIVOS
@router.get(
    "/paisesactivos",
    summary="Listar Países Activos",
    description="Obtiene todos los países que están activos (Activo = 1)",
    tags=["Geografia.Pais"]
)
async def listar_paises_activos():
    result = PaisInfrastructure.listar_paises_activos()
    return result


#INGRESAR PAIS
@router.post(
    "/ingresarpais",
    summary="Ingresar Pais",
    description="Ingresar Pais - Insert",
    tags=["Geografia.Pais"]
)
async def ingresar_pais(paismodel: PaisModel):
    result = PaisInfrastructure.ingresar_pais(paismodel)
    return {"message": "País insertado correctamente", "resultado": result}
    
#MODIFICAR PAIS
@router.put(
    "/modificarpais",
    
    summary="Modificar Pais ",
    description="Modificar Pais - Update",
    tags=["Geografia.Pais"]
)
async def modificar_pais(idpais: str, paismodel: PaisModel):
    paismodel.idpais = idpais   
    result = PaisInfrastructure.modificar_pais(paismodel)
    return result

#ELIMINAR PAIS
@router.delete(
    "/retirarpais",
    summary="Retirar Pais",
    description="Retirar Pais - delete",
    tags=["Geografia.Pais"]
)
async def eliminar_pais(idpais: str):
    result = PaisInfrastructure.eliminar_pais(idpais)
    return result

#DESACTIVAR PAIS

@router.put(
    "/desactivarpais",
    summary="Desactivar País",
    description="Desactiva un país (borrado lógico, Activo = 0)",
    tags=["Geografia.Pais"]
)
async def desactivar_pais(idpais: str):
    result = PaisInfrastructure.desactivar_pais(idpais)
    return result
