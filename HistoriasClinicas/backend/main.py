import uvicorn
from application.webapihistoriasclinicas import app
from fastapi.middleware.cors import CORSMiddleware

# 👉 Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def start():
    uvicorn.run(
        "application.webapihistoriasclinicas:app",
        host="127.0.0.1",
        port=7000,
        reload=True
    )

if __name__ == '__main__':
    start()
