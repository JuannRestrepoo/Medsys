from pydantic import BaseModel
from typing import Optional
from typing import Dict
class CobroModel(BaseModel):
    idcobro: Optional[str] = None
    idpaciente: str
    idprofesional: str
    productoservicio: str
    total: float
    activo: bool = True
    fecha: Optional[str] = None


class CentroModel(BaseModel):
    nombre: str
    direccion: str
    ciudad: str
    telefono: str

class FacturaPayload(BaseModel):
    paciente: str
    documento: str
    servicio: str
    fecha: str
    monto: float
    profesional: str
    centro: CentroModel
