from fastapi import APIRouter
from domain.Transaccion.DetalleCobro.DetalleCobroModel import DetalleCobroModel
from infrastructure.Transaccion.DetalleCobro.DetalleCobroInfrastructure import DetalleCobroInfrastructure
router = APIRouter(prefix="/detallecobro", tags=["Transaccion.DetalleCobro"])

#Transaccion.DetalleCobro
#GET
@router.get(
    "/detallecobroget",
    summary="Metodo DetalleCobro Get",
    description="Operacion DetalleCobro Get",
    tags=["Transaccion.DetalleCobro"]
)
async def consultar_detallecobro_por_id(iddetalle: str):
    return DetalleCobroInfrastructure.consultar_detallecobro_por_id(iddetalle)

#POST
@router.post(
    "/detallecobropost",
    summary="Metodo DetalleCobro Post",
    description="Operacion DetalleCobro Post",
    tags=["Transaccion.DetalleCobro"]
)
async def ingresar_detallecobro(det: DetalleCobroModel):
    return DetalleCobroInfrastructure.ingresar_detallecobro(det)

#PUT
@router.put(
    "/detallecobroput",
    summary="Metodo DetalleCobro Put",
    description="Operacion DetalleCobro Put",
    tags=["Transaccion.DetalleCobro"]
)
async def modificar_detallecobro(iddetalle: str, det: DetalleCobroModel):
    det.iddetalle = iddetalle
    return DetalleCobroInfrastructure.modificar_detallecobro(det)

@router.put(
    "/desactivar detallecobro",
    summary="Metodo DetalleCobro Put",
    description="Operacion DetalleCobro Put",
    tags=["Transaccion.DetalleCobro"]
)
async def desactivar_detallecobro(iddetalle: str):
    return DetalleCobroInfrastructure.desactivar_detallecobro(iddetalle)

#DELETE
@router.delete(
    "/detallecobrodelete",
    summary="Metodo DetalleCobro Delete",
    description="Operacion DetalleCobro Delete",
    tags=["Transaccion.DetalleCobro"]
)
async def eliminar_detallecobro(iddetalle: str):
    return DetalleCobroInfrastructure.eliminar_detallecobro(iddetalle)