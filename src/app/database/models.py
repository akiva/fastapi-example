from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Table,
)
from sqlalchemy.sql import func
from .database import Base

# SQLAlchemy models

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(50))
    created_date = Column(DateTime, default=func.now(), nullable=False)
