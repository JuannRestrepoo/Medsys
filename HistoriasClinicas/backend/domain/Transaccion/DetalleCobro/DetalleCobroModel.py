from pydantic import BaseModel

class DetalleCobroModel(BaseModel):
    iddetalle: str
    idcobro: str
    idproductoservicio: str
    cantidad: int
    subtotal: float
    activo: bool
