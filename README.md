# 💸 Currency API

This is a public and open-source **Currency API** built with **FastAPI** in Python.  
It fetches live exchange rates directly from the **Central Bank of Turkey (TCMB)** and exposes them as simple REST endpoints.

🔗 **Live API:** [https://currency-api-a1i1.onrender.com](https://currency-api-a1i1.onrender.com)

---

## 🧩 Endpoints

### ✅ `/api/rates`
Returns all exchange rates **based on TRY**.

**Example response:**
```json
{
  "base": "TRY",
  "date": "2025-07-06",
  "rates": {
    "USD": 32.50,
    "EUR": 35.90,
    "GBP": 42.80
  }
}
```

---

### ✅ `/api/rate?target=USD`
Returns 1 TRY in the specified currency.

**Example:**
```
GET /api/rate?target=USD
```

**Response:**
```json
{
  "base": "TRY",
  "target": "USD",
  "rate": 0.0308
}
```

---

### 🧠 `/api/all`  
Returns exchange rates between **all supported currencies**, based on TRY as the base source.  
Every currency is calculated as a "base", using the ratio of values from TCMB.

**Example Response (partial):**
```json
{
  "USD": {
    "EUR": 1.09375,
    "GBP": 1.28125,
    "TRY": 32.0
  },
  "EUR": {
    "USD": 0.9142,
    "GBP": 1.1714,
    "TRY": 35.0
  },
  "TRY": {
    "USD": 0.03125,
    "EUR": 0.02857
  }
}
```

---

## ⚙️ Tech Stack

- Python 3
- FastAPI
- Hosted on Render.com
- Data from [TCMB (Central Bank of Turkey)](https://www.tcmb.gov.tr/kurlar/today.xml)

---

## 🚀 How It Works

1. `fetch_rates.py` pulls XML data from TCMB daily.
2. It parses and converts it into `latest.json`.
3. `main.py` (FastAPI) reads this JSON and exposes REST endpoints.

---

## 📁 Project Structure

```
currency_api/
├── fetch_rates.py       # Data fetcher (from TCMB XML)
├── main.py              # FastAPI backend
├── data/
│   └── latest.json      # Stored currency data
└── requirements.txt     # Python dependencies
```

---

## 💬 Use Cases

- Mobile apps (e.g. Flutter)
- Location-based currency detection
- Currency converters
- Finance dashboards

---

## 🧑‍💻 Developer

Built by [@Pamir](https://github.com/pamiracar)  
Use it freely, clone it, extend it, or power your next app with it 🔥
