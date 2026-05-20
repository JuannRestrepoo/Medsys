from pydantic import BaseModel
from datetime import date

class HistoriaClinicaModel(BaseModel): 
    idhistoria: str | None = None
    idpaciente: str 
    fecha_creacion: date 
    antecedentes: str 
    observaciones: str 
    activo: bool
    idprofesional: str