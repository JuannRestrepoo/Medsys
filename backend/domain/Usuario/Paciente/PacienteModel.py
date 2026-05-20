from pydantic import BaseModel

class PacienteModel(BaseModel):
    idpaciente: str
    idusuario: str
    grupo_sanguineo: str
    alergias: str 
    antecedentes: str 
    edad: str
    activo: bool