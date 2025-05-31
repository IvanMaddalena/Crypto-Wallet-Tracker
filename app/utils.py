
import httpx

def fetch_current_price(symbol: str) -> float:
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd"
        response = httpx.get(url)
        return response.json().get(symbol.lower(), {}).get("usd", 0.0)
    except Exception:
        return 0.0

def calculate_pnl(amount: float, purchase_price: float, current_price: float) -> float:
    return round((current_price - purchase_price) * amount, 2)
