from fastapi import APIRouter
from domain.Geografia.Departamento.DepartamentoModel import DepartamentoModel
from infrastructure.Geografia.Departamento.DepartamentoInfrastructure import DepartamentoInfrastructure

router = APIRouter(prefix="/departamento", tags=["Geografia.Departamento"])

#Geografia.Departamento

#CONSULTAR DEPARTAMENTOS
@router.get(
    "/consultardepartamento",
    summary = "Consultar Departamento",
    description = "Consultar Departamento - SELECT",
    tags = ["Geografia.Departamento"]
)

async def consultar_departamento():
    return DepartamentoInfrastructure.consultar_departamento()

#CONSULTAR DEPARTAMENTO PORT ID
@router.get(
    "/consultardepartamentoporid",
    summary = "Consultar Departamento",
    description = "Consultar Departamento Por ID - SELECT",
    tags = ["Geografia.Departamento"]
)

async def consultar_departamento_por_id(iddepartamento: str):
    return DepartamentoInfrastructure.consultar_departamento_por_id(iddepartamento)

#INGRESAR DEPARTAMENTO
@router.post(
    "/ingresardepartamento",
    summary="Ingresar departamento",
    description="Ingresar departamento - Insert",
    tags=["Geografia.Departamento"]
)
async def ingresar_departamento(departamentomodel: DepartamentoModel):
    result = DepartamentoInfrastructure.ingresar_departamento(departamentomodel)
    return result
    
#MODIFCAR  DEPARTAMENTO
@router.put(
    "/modificardepartamento",
    
    summary="Modificar Departamento",
    description="Modificar Departamento - Put",
    tags=["Geografia.Departamento"]
)
async def modificar_departamento(iddepartamento: str, departamento: DepartamentoModel):
    departamento.iddepartamento = iddepartamento
    return DepartamentoInfrastructure.modificar_departamento(departamento)
#DESACTIVAR DEPARTAMENTO{

@router.put(
    "/deactivardepartamento",
    
    summary="Modificar Departamento",
    description="Modificar Departamento - Put",
    tags=["Geografia.Departamento"]
)
async def desactivar_departamento(iddepartamento: str):
    return DepartamentoInfrastructure.desactivar_departamento(iddepartamento)
#ELIMNINAR DEPARTAMENTO
@router.delete(
    "/eliminardepartamento",
    summary="Eliminar Departamento",
    description="Eliminar Departamento - Delete",
    tags=["Geografia.Departamento"]
)
async def eliminar_departamento(iddepartamento: str):
    result = DepartamentoInfrastructure.eliminar_departamento(iddepartamento)
    return result