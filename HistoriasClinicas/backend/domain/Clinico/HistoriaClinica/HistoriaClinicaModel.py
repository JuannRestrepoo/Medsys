from pydantic import BaseModel

class HistoriaClinicaModel(BaseModel): 
    idhistoria: str 
    idpaciente: str 
    fecha_creacion: str 
    antecedentes: str 
    observaciones: str 
    activo: bool