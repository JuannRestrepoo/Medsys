from pydantic import BaseModel

class ProductoServicioModel(BaseModel):
    idproductoservicio: str
    idtiposervicio: str
    nombre: str
    descripcion: str 
    precio: float
    activo: bool
