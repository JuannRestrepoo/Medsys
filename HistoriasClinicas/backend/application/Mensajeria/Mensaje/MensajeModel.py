from pydantic import BaseModel
from datetime import datetime

class MensajeModel(BaseModel):
    idmensaje: str
    idconversacion: str
    idremitente: str
    iddestinatario: str
    contenido: str
    fecha: datetime
    leido: bool
    activo: bool
