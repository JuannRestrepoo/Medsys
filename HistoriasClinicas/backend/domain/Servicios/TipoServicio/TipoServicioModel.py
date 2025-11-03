from pydantic import BaseModel

class TipoServicioModel(BaseModel):
    idtiposervicio: str
    nombre: str
    descripcion: str 
    activo: bool
