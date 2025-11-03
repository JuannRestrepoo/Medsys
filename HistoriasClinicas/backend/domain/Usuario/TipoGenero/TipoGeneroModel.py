from pydantic import BaseModel

class TipoGeneroModel(BaseModel):
    idtipogenero: str
    nombre: str
    activo: bool