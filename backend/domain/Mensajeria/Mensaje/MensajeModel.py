from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MensajeModel(BaseModel):
    idmensaje: Optional[str] = None      
    idconversacion: Optional[str] = None 
    idremitente: str                     
    iddestinatario: str # 👈 AGREGA ESTA LÍNEA EXACTAMENTE AQUÍ
    contenido: str                       
    fecha: Optional[datetime] = None     
    leido: Optional[bool] = False
    activo: Optional[bool] = True