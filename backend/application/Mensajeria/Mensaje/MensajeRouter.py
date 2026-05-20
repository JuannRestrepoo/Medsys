from fastapi import APIRouter, Request
from domain.Mensajeria.Mensaje.MensajeModel import MensajeModel
from infrastructure.Mensajeria.MensajeInfrastructure import MensajeInfrastructure

router = APIRouter(prefix="/mensajes", tags=["Módulo Mensajes MedSys"])

@router.post("/enviar")
async def enviar_mensaje(data: MensajeModel, request: Request):
    ip_cliente = request.client.host
    return MensajeInfrastructure.enviar_mensaje(
        data.idremitente, 
        data.iddestinatario, 
        data.contenido, 
        ip_cliente
    )

@router.get("/bandeja/{id_usuario}")
async def ver_bandeja(id_usuario: str, request: Request):
    ip_cliente = request.client.host
    return MensajeInfrastructure.listar_mensajes_usuario(id_usuario, ip_cliente)

@router.get("/contactos")
async def obtener_contactos(request: Request):
    ip_cliente = request.client.host
    return MensajeInfrastructure.listar_contactos_chat(ip_cliente)

@router.get("/chat/{id_doctor}/{id_paciente}")
async def obtener_historial_chat(id_doctor: str, id_paciente: str, request: Request):
    ip_cliente = request.client.host
    # Llama al método optimizado que desencripta y verifica el HMAC bit a bit
    return MensajeInfrastructure.obtener_historial_chat(id_doctor, id_paciente, ip_cliente)


# Agrega este endpoint en tu MensajeRouter.py

@router.get("/medicos-disponibles")
async def obtener_medicos_para_paciente(request: Request):
    ip_cliente = request.client.host
    # Llamamos a una nueva función de infraestructura especializada
    return MensajeInfrastructure.listar_profesionales_salud(ip_cliente)