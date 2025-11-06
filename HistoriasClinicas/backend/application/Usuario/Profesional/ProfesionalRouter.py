from fastapi import APIRouter
from domain.Usuario.Profesional.ProfesionalModel import ProfesionalModel
from infrastructure.Usuario.Profesional.ProfesionalInfrastructure import ProfesionalInfrastructure
router = APIRouter(prefix="/profesional", tags=["Usuario.Profesional"])



#ENDPOINT PERFIL PROFESIONAL

@router.get(
    "/consultar_profesional_usuario",
    summary="Consultar Profesional con datos de Usuario",
    description="Devuelve datos del profesional junto con los datos básicos del usuario",
    tags=["Usuario.Profesional"]
)
async def consultar_profesional_usuario(idusuario: str):
    return ProfesionalInfrastructure.consultar_profesional_usuario(idusuario)


#ENDPOINT QUE DEVUELVE LOS PROFESIUONALES DEL CENTRO EN EL CUAL SE REGISTRO EL PACIENTE
@router.get("/paciente/{idusuario}/profesionales")
def listar_profesionales_para_paciente(idusuario: str):
    return ProfesionalInfrastructure.listar_profesionales_para_paciente(idusuario)





#Usuario.Profesional
#GET
@router.get(
    "/empleadoget",
    summary = "Metodo Empleado Get",
    description = "Operacion Empleado Get",
    tags = ["Usuario.Profesional"]
)
async def consultar_profesional_por_id(idprofesional: str):
    return ProfesionalInfrastructure.consultar_profesional_por_id(idprofesional)

#POST
@router.post(
    "/empleadopost",
    summary="Metodo Empleado Post",
    description="Operacion Empleado post",
    tags=["Usuario.Profesional"]
)
async def ingresar_profesional(profesional: ProfesionalModel):
    return ProfesionalInfrastructure.ingresar_profesional(profesional)
#PUT


@router.put(
    "/empleadoput",
    summary="Metodo Empleado Put",
    description="Operacion Empleado put",
    tags=["Usuario.Profesional"]
)
async def modificar_profesional(idprofesional: str, profesional: ProfesionalModel):
    profesional.idprofesional = idprofesional
    return ProfesionalInfrastructure.modificar_profesional(profesional)

@router.put(
    "/desactivarprofesional",
    summary="Metodo Empleado Put",
    description="Operacion Empleado put",
    tags=["Usuario.Profesional"]
)
async def desactivar_profesional(idprofesional: str):
    return ProfesionalInfrastructure.desactivar_profesional(idprofesional)



#DELETE
@router.delete(
    "/empleadodelete",
    summary="Metodo Empleado delete",
    description="Operacion Empleado delete",
    tags=["Usuario.Profesional"]
)
async def eliminar_profesional(idprofesional: str):
    return ProfesionalInfrastructure.eliminar_profesional(idprofesional)
