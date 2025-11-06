import uvicorn
import os
from application.webapihistoriasclinicas import app
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# 👉 Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👉 Crear carpeta uploads si no existe
os.makedirs("uploads", exist_ok=True)

# 👉 Montar carpeta estática en /uploads
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
