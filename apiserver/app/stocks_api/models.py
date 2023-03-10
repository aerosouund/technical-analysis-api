from __future__ import annotations
from datetime import datetime
from app import db  # noqa
from sqlalchemy import BigInteger, Column, Date, DateTime, ForeignKey, Integer, String



class Stock(db.Model):
    __tablename__ = "stock_data"

    id = Column(BigInteger, primary_key=True)
    person_id = Column(Integer, ForeignKey(Person.id), nullable=False)
    coordinate = Column(Geometry("POINT"), nullable=False)
    creation_time = Column(DateTime, nullable=False, default=datetime.utcnow)