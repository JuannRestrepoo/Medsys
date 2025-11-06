from pydantic import BaseModel

class UsuarioModel(BaseModel):
    idusuario: str | None = None
    idciudad: str
    idtipodocumento: str
    idtipogenero: str
    nombre_completo: str
    correo: str
    contrasena: str   
    rol: str
    numero_documento: str
    direccion: str
    fecha_nacimiento: str   
    activo: bool
    telefono: str
