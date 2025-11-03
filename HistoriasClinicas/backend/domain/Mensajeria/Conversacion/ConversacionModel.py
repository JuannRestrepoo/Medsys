from pydantic import BaseModel
from datetime import datetime

class ConversacionModel(BaseModel):
    idconversacion: str
    idpaciente: str
    idprofesional: str
    creado_en: datetime
    activo: bool
