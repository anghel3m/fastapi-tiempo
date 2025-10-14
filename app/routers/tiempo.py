from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from ..database import get_db
from ..models import DimTiempo

# Crear router
router = APIRouter(prefix="/tiempo", tags=["Tiempo"])

# Ruta 1: Listar registros de DimTiempo
@router.get("/")
def listar_todo(db: Session = Depends(get_db)):
    return db.query(DimTiempo).limit(20).all()

# Ruta 2: Calcular diferencia entre fechas
@router.get("/fechas")
def calcular_diferencia(
    fecha_inicio: str = Query(..., description="Fecha inicial en formato YYYY-MM-DD"),
    fecha_fin: str = Query(..., description="Fecha final en formato YYYY-MM-DD")
):
    try:
        # Convertir a datetime
        f_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        f_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de fecha incorrecto. Usa YYYY-MM-DD")

    # Validar orden
    if f_inicio >= f_fin:
        raise HTTPException(status_code=400, detail="La fecha inicial debe ser menor que la fecha final")

    # Calcular días calendario
    dias_calendario = (f_fin - f_inicio).days

    # Calcular días hábiles (lunes a viernes)
    dias_habiles = 0
    dia_actual = f_inicio
    while dia_actual < f_fin:
        if dia_actual.weekday() < 5:  # Lunes=0, Viernes=4
            dias_habiles += 1
        dia_actual += timedelta(days=1)

    return {
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "dias_calendario": dias_calendario,
        "dias_habiles": dias_habiles
    }
