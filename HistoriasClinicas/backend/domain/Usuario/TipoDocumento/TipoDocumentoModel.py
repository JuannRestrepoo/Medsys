from pydantic import BaseModel

class TipoDocumentoModel(BaseModel):
    idtipodocumento: str
    nombre: str
    descripcion: str 
    activo: bool
