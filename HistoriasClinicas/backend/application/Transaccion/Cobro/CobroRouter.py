from fastapi import APIRouter
from domain.Transaccion.Cobro.CobroModel import CobroModel
from infrastructure.Transaccion.Cobro.CobroInfrastructure import CobroInfrastructure

router = APIRouter(prefix="/cobro", tags=["Transaccion.Cobro"])

#Transaccion.Cobro
#GET
@router.get(
    "/cobroget",
    summary="Metodo Cobro Get",
    description="Operacion Cobro Get",
    tags=["Transaccion.Cobro"]
)
async def consultar_cobro_por_id(idcobro: str):
    return CobroInfrastructure.consultar_cobro_por_id(idcobro)

#POST
@router.post(
    "/cobropost",
    summary="Metodo Cobro Post",
    description="Operacion Cobro Post",
    tags=["Transaccion.Cobro"]
)
async def ingresar_cobro(cobro: CobroModel):
    return CobroInfrastructure.ingresar_cobro(cobro)
#PUT
@router.put(
    "/cobroput",
    summary="Metodo Cobro Put",
    description="Operacion Cobro Put",
    tags=["Transaccion.Cobro"]
)
async def modificar_cobro(idcobro: str, cobro: CobroModel):
    cobro.idcobro = idcobro
    return CobroInfrastructure.modificar_cobro(cobro)

@router.put(
    "/deactivarcobro",
    summary="Metodo Cobro Put",
    description="Operacion Cobro Put",
    tags=["Transaccion.Cobro"]
)
async def desactivar_cobro(idcobro: str):
    return CobroInfrastructure.desactivar_cobro(idcobro)
#DELETE
@router.delete(
    "/cobrodelete",
    summary="Metodo Cobro Delete",
    description="Operacion Cobro Delete",
    tags=["Transaccion.Cobro"]
)
async def eliminar_cobro(idcobro: str):
    return CobroInfrastructure.eliminar_cobro(idcobro)
