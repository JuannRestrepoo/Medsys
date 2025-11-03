from pydantic import BaseModel

class CentroModel(BaseModel):
    
    idcentro: str
    nombre: str
    direccion: str
    telefono: str
    idciudad: str
    activo: bool