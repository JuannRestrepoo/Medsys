from fastapi import APIRouter
from domain.Transaccion.EstadoPago.EstadoPagoModel import EstadoPagoModel
from infrastructure.Transaccion.EstadoPago.EstadoPagoInfrastructure import EstadoPagoInfrastructure
router = APIRouter(prefix="/estadopago", tags=["Transaccion.EstadoPago"])
#Transaccion.EstadoPago
#GET
@router.get(
    "/estadopagoget",
    summary="Metodo EstadoPago Get",
    description="Operacion EstadoPago Get",
    tags=["Transaccion.EstadoPago"]
)
async def consultar_estadopago_por_id(idestadopago: str):
    return EstadoPagoInfrastructure.consultar_estadopago_por_id(idestadopago)

#POST
@router.post(
    "/estadopagopost",
    summary="Metodo EstadoPago Post",
    description="Operacion EstadoPago Post",
    tags=["Transaccion.EstadoPago"]
)
async def ingresar_estadopago(ep: EstadoPagoModel):
    return EstadoPagoInfrastructure.ingresar_estadopago(ep)

#PUT
@router.put(
    "/estadopagoput",
    summary="Metodo EstadoPago Put",
    description="Operacion EstadoPago Put",
    tags=["Transaccion.EstadoPago"]
)
async def modificar_estadopago(idestadopago: str, ep: EstadoPagoModel):
    ep.idestadopago = idestadopago
    return EstadoPagoInfrastructure.modificar_estadopago(ep)

@router.put(
    "/deactivarestadopago",
    summary="Metodo EstadoPago Put",
    description="Operacion EstadoPago Put",
    tags=["Transaccion.EstadoPago"]
)
async def desactivar_estadopago(idestadopago: str):
    return EstadoPagoInfrastructure.desactivar_estadopago(idestadopago)

#DELETE
@router.delete(
    "/estadopagodelete",
    summary="Metodo EstadoPago Delete",
    description="Operacion EstadoPago Delete",
    tags=["Transaccion.EstadoPago"]
)
async def eliminar_estadopago(idestadopago: str):
    return EstadoPagoInfrastructure.eliminar_estadopago(idestadopago)