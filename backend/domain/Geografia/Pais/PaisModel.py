from pydantic import BaseModel

class PaisModel(BaseModel):
    
    idpais: str
    nombre: str
    activo: bool