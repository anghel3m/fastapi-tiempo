from fastapi import FastAPI
from .routers import tiempo

app = FastAPI(title="API FastAPI Tiempo")

app.include_router(tiempo.router)

@app.get("/")
def root():
    return {"message": "API FastAPI conectada con MySQL Aiven ✅"}
