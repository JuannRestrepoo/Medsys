from pydantic import BaseModel

class EstadoPagoModel(BaseModel):
    idestadopago: str
    nombre: str
    activo: bool
