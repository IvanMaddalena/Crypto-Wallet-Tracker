
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import AssetCreate, Asset
from app.models import CryptoAsset
from app.database import SessionLocal
from app.utils import fetch_current_price, calculate_pnl
from fastapi.responses import StreamingResponse
import io
import pandas as pd

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/assets/", response_model=Asset)
def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
    db_asset = CryptoAsset(**asset.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@router.get("/assets/", response_model=list[Asset])
def list_assets(db: Session = Depends(get_db)):
    return db.query(CryptoAsset).all()

@router.get("/assets/{asset_id}/report")
def report_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = db.query(CryptoAsset).get(asset_id)
    if not asset:
        return {"error": "Asset not found"}
    price = fetch_current_price(asset.symbol)
    pnl = calculate_pnl(asset.amount, asset.purchase_price, price)
    return {
        "symbol": asset.symbol,
        "amount": asset.amount,
        "purchase_price": asset.purchase_price,
        "current_price": price,
        "profit_loss": pnl
    }

@router.get("/export/")
def export_assets(db: Session = Depends(get_db)):
    assets = db.query(CryptoAsset).all()
    df = pd.DataFrame([{
        "name": a.name,
        "symbol": a.symbol,
        "amount": a.amount,
        "purchase_price": a.purchase_price,
        "exchange": a.exchange,
        "purchase_date": a.purchase_date
    } for a in assets])
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    stream.seek(0)
    return StreamingResponse(stream, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=wallet.csv"})
