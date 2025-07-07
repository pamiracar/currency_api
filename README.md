# Currency API (TRY-based)

This is a simple currency exchange rate API built with Python and FastAPI, powered by **live data from the Central Bank of Turkey (TCMB)**. The API provides real-time exchange rates relative to the Turkish Lira (TRY).

🌐 **Live URL**: https://currency-api-a1i1.onrender.com

---

## 🔧 Endpoints

### GET /api/rates

Returns all exchange rates based on Turkish Lira (TRY).

**Example Response:**
```json
{
  "base": "TRY",
  "date": "2025-07-06",
  "rates": {
    "USD": 32.50,
    "EUR": 35.90,
    "GBP": 42.80,
    ...
  }
}
```

---

### GET /api/rate?target={currency_code}

Returns the exchange rate of 1 TRY to the selected currency.

**Example Request:**
```
GET /api/rate?target=USD
```

**Example Response:**
```json
{
  "base": "TRY",
  "target": "USD",
  "rate": 0.0308
}
```

---

## 📦 Tech Stack

- Python 3
- FastAPI
- Requests
- Hosted on Render.com

---

## 🚀 How It Works

1. Data is fetched directly from the [TCMB (Central Bank of Turkey)](https://www.tcmb.gov.tr/kurlar/today.xml) via their public XML feed.
2. Rates are parsed, converted to JSON, and saved into `data/latest.json`.
3. FastAPI serves this JSON via the `/api/rates` and `/api/rate` endpoints.

---

## 📂 Project Structure

```
currency_api/
├── fetch_rates.py       # Pulls data from TCMB
├── main.py              # FastAPI server
├── data/
│   └── latest.json      # Stores current rates
└── requirements.txt     # Dependencies
```

---

## 🧪 Try It Live

- All rates: https://currency-api-a1i1.onrender.com/api/rates  
- Specific rate: https://currency-api-a1i1.onrender.com/api/rate?target=USD

---

## 🧑‍💻 Author

Developed by **Pamir** with 💪 — feel free to use, fork or improve.

