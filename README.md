# Currency API (TRY-based)

This is a simple currency exchange rate API built with Python and FastAPI, powered by **live data from the Central Bank of Turkey (TCMB)**. The API provides real-time exchange rates relative to the Turkish Lira (TRY).

🌐 **Live URL**: [https://currency-api-a1i1.onrender.com](https://currency-api-a1i1.onrender.com)

---

## 🔧 Endpoints

### `GET /api/rates`

Returns all exchange rates based on Turkish Lira (TRY).

#### Response:
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
