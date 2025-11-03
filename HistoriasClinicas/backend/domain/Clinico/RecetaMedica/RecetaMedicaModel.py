from pydantic import BaseModel

class RecetaMedicaModel(BaseModel):
    idreceta: str
    iddiagnostico: str
    medicamento: str
    dosis: str
    indicaciones: str
    activo: bool
