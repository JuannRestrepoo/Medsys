from pydantic import BaseModel

class ProfesionalModel(BaseModel):
    idprofesional: str
    idusuario: str
    idcentro: str
    cargo: str
    activo: bool
