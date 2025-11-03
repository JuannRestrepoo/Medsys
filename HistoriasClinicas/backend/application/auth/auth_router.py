from fastapi import APIRouter, HTTPException
from domain.Auth.LoginModel import LoginModel
from infrastructure.Usuario.Usuario.UsuarioInfrastructure import UsuarioInfrastructure
from infrastructure.Usuario.Profesional.ProfesionalInfrastructure import ProfesionalInfrastructure
import jwt
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth", tags=["Auth"])

SECRET_KEY = "super_secret_key"  # cámbialo por variable de entorno
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

@router.post("/login")
def login(login: LoginModel):
    return UsuarioInfrastructure.verificar_credenciales(login)
