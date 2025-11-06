from pydantic import BaseModel

class RecetaMedicaModel(BaseModel):
    idreceta: str
    medicamento: str
    dosis: str
    indicaciones: str
    activo: bool
    idpaciente: str
    idprofesional: str