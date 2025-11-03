from pydantic import BaseModel

class CitaMedicaModel(BaseModel):
    idcita: str
    idpaciente: str
    idprofesional: str
    fecha: str
    hora: str
    motivo: str
    estado: str
    activo: bool
