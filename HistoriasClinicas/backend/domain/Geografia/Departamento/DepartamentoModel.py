from pydantic import BaseModel

class DepartamentoModel(BaseModel):
    
    iddepartamento: str
    nombre: str
    activo: bool
    idpais: str