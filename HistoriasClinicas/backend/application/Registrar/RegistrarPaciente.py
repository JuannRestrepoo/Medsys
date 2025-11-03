# application/webapihistoriasclinicas.py
from fastapi import APIRouter
from domain.Usuario.Paciente.RegistrarPacienteModel import RegistrarPacienteModel
from infrastructure.Usuario.Paciente.RegistrarPacienteInfrastructure import RegistrarPacienteInfrastructure

router = APIRouter(prefix="/paciente", tags=["Paciente"])


@router.post("/registrar")
def registrar_paciente(data: RegistrarPacienteModel):
    return RegistrarPacienteInfrastructure.registrar_paciente(data)
