# 💰 Crypto Wallet Tracker API

A lightweight and fast REST API to track your cryptocurrency purchases, calculate real-time profit/loss, and export reports.  
Built with FastAPI, SQLite, SQLAlchemy, and CoinGecko API. 🚀

---

## 🔍 Features

- 💰 Track purchased cryptocurrencies with quantity, price, and exchange
- 💵 Real-time price updates via CoinGecko
- 📊 Calculate profit/loss per asset
- 📁 Export your wallet to CSV
- 🌐 Interactive API docs via Swagger UI

---

## ⚙️ Tech Stack

| Layer       | Technology                 |
|-------------|----------------------------|
| API         | FastAPI                    |
| ORM         | SQLAlchemy                 |
| DB          | SQLite                     |
| Schema      | Pydantic                   |
| HTTP Client | httpx                      |
| Price Feed  | CoinGecko API              |
| Export      | pandas                     |

---

## 📁 Project Structure

```
crypto-wallet-tracker/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app
│   ├── models.py          # Asset DB model
│   ├── schemas.py         # Pydantic schemas
│   ├── routes.py          # API endpoints
│   ├── utils.py           # Helpers (API calls, PnL)
│   └── database.py        # DB config
├── .env                   # API + DB config
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/crypto-wallet-tracker.git
cd crypto-wallet-tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) to interact with the API.

---

## 📌 API Overview

### Assets
- `POST /assets/` → Add a new crypto asset
- `GET /assets/` → List all tracked assets
- `GET /assets/{id}/report` → Get current value and PnL for asset

### Export
- `GET /export/` → Download your wallet in CSV format

---

## 📬 Author

Developed by **Ivan Maddalena**  
📫 Email: ivan.maddalena00@gmail.com  
🔗 [GitHub Profile](https://github.com/IvanMaddalena)

---

## 📜 License

This project is licensed under the MIT License.
