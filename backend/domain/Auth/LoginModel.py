from pydantic import BaseModel

class LoginModel(BaseModel):
    correo: str
    contrasena: str
