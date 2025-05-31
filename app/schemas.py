
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AssetCreate(BaseModel):
    name: str
    symbol: str
    amount: float
    purchase_price: float
    exchange: str

class Asset(BaseModel):
    id: int
    name: str
    symbol: str
    amount: float
    purchase_price: float
    exchange: str
    purchase_date: datetime

    class Config:
        orm_mode = True
