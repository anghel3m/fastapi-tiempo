from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import DimTiempo

router = APIRouter(prefix="/tiempo", tags=["Tiempo"])

@router.get("/")
def listar_todo(db: Session = Depends(get_db)):
    return db.query(DimTiempo).limit(20).all()
