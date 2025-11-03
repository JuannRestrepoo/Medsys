from fastapi import APIRouter
from domain.Servicios.ProductoServicio.ProductoServicioModel import ProductoServicioModel
from infrastructure.Servicios.ProductoServicio.ProductoServicioInfrastructure import ProductoServicioInfrastructure

router = APIRouter(prefix="/productoservicio", tags=["Servicios.ProductoServicio"])

#Servicios.ProductoServicio
#GET
@router.get(
    "/productoservicioget",
    summary = "Metodo ProductoServicio Get",
    description = "Operacion ProductoServicio Get",
    tags = ["Servicios.ProductoServicio"]
)
async def consultar_productoservicio_por_id(idproductoservicio: str):
    return ProductoServicioInfrastructure.consultar_productoservicio_por_id(idproductoservicio)

#POST
@router.post(
    "/productoserviciopost",
    summary="Metodo ProductoServicio Post",
    description="Operacion ProductoServicio post",
    tags=["Servicios.ProductoServicio"]
)
async def ingresar_productoservicio(ps: ProductoServicioModel):
    return ProductoServicioInfrastructure.ingresar_productoservicio(ps)
#PUT
@router.put(
    "/desactivarproductoservicio",
    summary="Metodo ProductoServicio Put",
    description="Operacion ProductoServicio put",
    tags=["Servicios.ProductoServicio"]
)
async def desactivar_productoservicio(idproductoservicio: str):
    return ProductoServicioInfrastructure.desactivar_productoservicio(idproductoservicio)

@router.put(
    "/modificarproductoservicio",
    summary="Metodo ProductoServicio Put",
    description="Operacion ProductoServicio put",
    tags=["Servicios.ProductoServicio"]
)
async def modificar_productoservicio(idproductoservicio: str, ps: ProductoServicioModel):
    ps.idproductoservicio = idproductoservicio
    return ProductoServicioInfrastructure.modificar_productoservicio(ps)

#DELETE
@router.delete(
    "/productoserviciodelete",
    summary="Metodo ProductoServicio delete",
    description="Operacion ProductoServicio delete",
    tags=["Servicios.ProductoServicio"]
)
async def eliminar_productoservicio(idproductoservicio: str):
    return ProductoServicioInfrastructure.eliminar_productoservicio(idproductoservicio)