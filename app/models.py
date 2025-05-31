
from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base
from datetime import datetime

class CryptoAsset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    symbol = Column(String, index=True)
    amount = Column(Float)
    purchase_price = Column(Float)
    exchange = Column(String)
    purchase_date = Column(DateTime, default=datetime.utcnow)
