from fastapi import APIRouter
from domain.Usuario.Paciente.PacienteModel import PacienteModel
from infrastructure.Usuario.Paciente.PacienteInfrastructure import PacienteInfrastructure
router = APIRouter(prefix="/paciente", tags=["Usuario.Paciente"])

#Endpoint Perfil Pciente
@router.get(
    "/consultar_paciente_usuario",
    summary="Consultar Paciente con datos de Usuario",
    description="Devuelve datos del paciente junto con los datos básicos del usuario",
    tags=["Usuario.Paciente"]
)
async def consultar_paciente_usuario(idusuario: str):
    return PacienteInfrastructure.consultar_paciente_usuario(idusuario)



#API PARA OBTENER PACIENTE POR DOCUMENTO
@router.get("/documento/{documento}")
def obtener_paciente_por_documento(documento: str):
    return PacienteInfrastructure.obtener_paciente_por_documento(documento)

#Usuario.Paciente
#GET
@router.get(
    "/consultarpacienteporid",
    summary = "Consultar Paciente Por ID",
    description = "Consultar Paciente Por ID - Get",
    tags = ["Usuario.Paciente"]
)
async def consultar_paciente_por_id(idpaciente: str):
    return PacienteInfrastructure.consultar_paciente_por_id(idpaciente)

#POST
@router.post(
    "/ingresarpaciente",
    summary="Ingresar Paciente",
    description="Ingresar Paciente- Post",
    tags=["Usuario.Paciente"]
)

async def ingresar_paciente(paciente: PacienteModel):
    return PacienteInfrastructure.ingresar_paciente(paciente)

#PUT


@router.put(
    "/modificarpaciente",
    summary="Modificar Paciente",
    description="Modificar Paciente - Put",
    tags=["Usuario.Paciente"]
)
async def modificar_paciente(idpaciente: str, paciente: PacienteModel):
    paciente.idpaciente = idpaciente
    return PacienteInfrastructure.modificar_paciente(paciente)

@router.put(
    "/deactivarpaciente",
    summary="Desactivar Paciente",
    description="Desactivar Paciente - Put",
    tags=["Usuario.Paciente"]
)
async def desactivar_paciente(idpaciente: str):
    return PacienteInfrastructure.desactivar_paciente(idpaciente)

#DELETE
@router.delete(
    "/eliminarpaciente",
    summary="Eliminar Paciente",
    description="Eliminar Paciente - Delete",
    tags=["Usuario.Paciente"]
)
async def eliminar_paciente(idpaciente: str):
    return PacienteInfrastructure.eliminar_paciente(idpaciente)

