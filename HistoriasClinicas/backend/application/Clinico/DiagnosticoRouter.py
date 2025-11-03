from fastapi import APIRouter
from domain.Clinico.Diagnostico.DiagnosticoModel import DiagnosticoModel
from infrastructure.Clinico.Diagnostico.DiagnosticoInfrastrucure import DiagnosticoInfrastructure

router = APIRouter(prefix="/diagnostico", tags=["Clinico.Diagnostico"])

#Clinico.Diagnostico
#GET
@router.get(
    "/diagnosticoget",
    summary = "Metodo Diagnostico Get",
    description = "Operacion Diagnostico Get",
    tags = ["Clinico.Diagnostico"]
)
async def consultar_diagnostico_por_id(iddiagnostico: str):
    return DiagnosticoInfrastructure.consultar_diagnostico_por_id(iddiagnostico)
#POST
@router.post(
    "/diagnosticopost",

    summary="Metodo Diagnostico Post",
    description="Operacion Diagnostico post",
    tags=["Clinico.Diagnostico"]
)
async def ingresar_diagnostico(diag: DiagnosticoModel):
    return DiagnosticoInfrastructure.ingresar_diagnostico(diag)
#PUT
@router.put(
    "/desactivardiagnostico",
    summary="Metodo Diagnostico Put",
    description="Operacion Diagnostico put",
    tags=["Clinico.Diagnostico"]
)
async def desactivar_diagnostico(iddiagnostico: str):
    return DiagnosticoInfrastructure.desactivar_diagnostico(iddiagnostico)


@router.put(
    "/diagnosticoput",
    summary="Metodo Diagnostico Put",
    description="Operacion Diagnostico put",
    tags=["Clinico.Diagnostico"]
)
async def modificar_diagnostico(iddiagnostico: str, diag: DiagnosticoModel):
    diag.iddiagnostico = iddiagnostico
    return DiagnosticoInfrastructure.modificar_diagnostico(diag)

#DELETE
@router.delete(
    "/diagnosticodelete",
    summary="Metodo Diagnostico delete",
    description="Operacion Diagnostico delete",
    tags=["Clinico.Diagnostico"]
)
async def eliminar_diagnostico(iddiagnostico: str):
    return DiagnosticoInfrastructure.eliminar_diagnostico(iddiagnostico)
