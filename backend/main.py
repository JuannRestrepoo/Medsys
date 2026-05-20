import uvicorn
import logging
import os
from application.webapihistoriasclinicas import app
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles





# Configuración global de los logs de seguridad
logging.basicConfig(
    filename='medsys_security.log',  # Nombre del archivo que se creará automáticamente
    level=logging.WARNING,           # Guarda solo eventos importantes (WARNING, ERROR, CRITICAL)
    format='[%(asctime)s] [%(levelname)s] [MÓDULO: %(name)s] -> %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'    # Formato de fecha y hora colombiana/estándar
)


# Creamos el registrador específico para el módulo de seguridad
logger_seguridad = logging.getLogger('SEGURIDAD')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


os.makedirs("uploads", exist_ok=True)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

def start():
    uvicorn.run(
        "application.webapihistoriasclinicas:app",
        host="127.0.0.1",
        port=7000,
        reload=True
    )

if __name__ == '__main__':
    start()
