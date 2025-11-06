from pydantic import BaseModel

class ResultadosModel(BaseModel):
    idresultado: str | None = None
    idpaciente: str
    idprofesional: str
    titulo: str
    descripcion: str | None = None
    archivo: str | None = None
    activo: bool = True
