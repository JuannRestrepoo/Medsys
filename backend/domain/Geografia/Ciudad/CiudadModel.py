from pydantic import BaseModel

class CiudadModel(BaseModel):
    
    idciudad: str
    nombre: str
    activo: bool
    iddepartamento: str
    