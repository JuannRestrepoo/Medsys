from fastapi import APIRouter, HTTPException
from domain.Auth.LoginModel import LoginModel
from infrastructure.Usuario.Usuario.UsuarioInfrastructure import UsuarioInfrastructure
from infrastructure.Usuario.Profesional.ProfesionalInfrastructure import ProfesionalInfrastructure
from infrastructure.Usuario.Login.LoginInfrastructure import LoginInfrastructure
import jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, Request

router = APIRouter(prefix="/auth", tags=["Auth"])

SECRET_KEY = "super_secret_key"  # cámbialo por variable de entorno
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60




@router.post("/login-paciente", summary="Login de Paciente")
async def login_paciente(data: LoginModel, request: Request): #Agregas 'request' aquí
    ip_cliente = request.client.host #Capturas la IP real del cliente
    return LoginInfrastructure.login_paciente(data.correo, data.contrasena, ip_cliente)

@router.post("/login-profesional", summary="Login de Profesional")
async def login_profesional(data: LoginModel, request: Request): #Agregas 'request' aquí
    ip_cliente = request.client.host # Capturas la IP real del cliente
    return LoginInfrastructure.login_profesional(data.correo, data.contrasena, ip_cliente)