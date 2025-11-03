from pydantic import BaseModel
from datetime import date

class RegistrarPacienteModel(BaseModel):
    nombre: str
    documento: str
    correo: str
    telefono: str
    direccion: str
    genero: str
    idciudad: str
    idtipodocumento: str
    grupo_sanguineo: str
    alergias: str
    antecedentes: str
    edad: str
    fecha_nacimiento: date   # 👈 nuevo campo

