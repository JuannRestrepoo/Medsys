from pydantic import BaseModel
from datetime  import date
class CitaMedicaModel(BaseModel):
    idcita: str
    idpaciente: str
    idprofesional: str
    fecha: date
    hora: str
    motivo: str
    estado: str
    activo: bool
