from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import tiempo

app = FastAPI(title="API FastAPI Tiempo")

# 🔹 Configurar CORS
origins = [
    "http://localhost:4200",          # Angular en desarrollo
    "https://penalista-tools.netlify.app",  # tu dominio en producción (ajústalo si cambia)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # puedes usar ["*"] si quieres permitir todo
    allow_credentials=True,
    allow_methods=["*"],          # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],          # Permitir todos los headers
)

# 🔹 Registrar routers
app.include_router(tiempo.router)

@app.get("/")
def root():
    return {"message": "API FastAPI conectada con MySQL Aiven ✅"}
