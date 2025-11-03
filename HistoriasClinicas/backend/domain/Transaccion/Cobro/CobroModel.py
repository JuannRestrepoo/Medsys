from pydantic import BaseModel

class CobroModel(BaseModel):
    idcobro: str
    idestadopago: str
    idpaciente: str
    fecha: str
    total: float
    activo: bool
