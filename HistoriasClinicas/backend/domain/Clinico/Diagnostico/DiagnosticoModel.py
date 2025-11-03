from pydantic import BaseModel

class DiagnosticoModel(BaseModel):
    iddiagnostico: str
    idcita: str
    descripcion: str
    observaciones: str 
    activo: bool