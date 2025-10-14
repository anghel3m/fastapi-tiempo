from sqlalchemy import Column, Integer, String, SmallInteger, Date, Boolean
from .database import Base

class DimTiempo(Base):
    __tablename__ = "dim_tiempo"

    FechaSK = Column(Integer, primary_key=True, index=True)
    Fecha = Column(Date, nullable=False)
    Anio = Column(SmallInteger, nullable=False)
    Trimestre = Column(SmallInteger, nullable=False)
    Mes = Column(SmallInteger, nullable=False)
    Semana = Column(SmallInteger, nullable=False)
    Dia = Column(SmallInteger, nullable=False)
    DiaSemana = Column(SmallInteger, nullable=False)
    NTrimestre = Column(String(7), nullable=False)
    NMes = Column(String(15), nullable=False)
    NMes3L = Column(String(3), nullable=False)
    NSemana = Column(String(11), nullable=False)
    NDia = Column(String(15), nullable=False)
    NDiaSemana = Column(String(15), nullable=False)
    Laborable = Column(Boolean, default=True)
    HorasLaborales = Column(String(45))
    Festivo = Column(Boolean, default=False)
