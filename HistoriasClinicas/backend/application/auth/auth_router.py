from fastapi import APIRouter, HTTPException
from domain.Auth.LoginModel import LoginModel
from infrastructure.Usuario.Usuario.UsuarioInfrastructure import UsuarioInfrastructure
from infrastructure.Usuario.Profesional.ProfesionalInfrastructure import ProfesionalInfrastructure
from infrastructure.Usuario.Login.LoginInfrastructure import LoginInfrastructure
import jwt
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth", tags=["Auth"])

SECRET_KEY = "super_secret_key"  # cámbialo por variable de entorno
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60



@router.post("/login-paciente", summary="Login de Paciente")
async def login_paciente(data: LoginModel):
    return LoginInfrastructure.login_paciente(data.correo, data.contrasena)

@router.post("/login-profesional", summary="Login de Profesional")
async def login_profesional(data: LoginModel):
    return LoginInfrastructure.login_profesional(data.correo, data.contrasena)