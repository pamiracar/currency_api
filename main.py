from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Tüm kurları döner
@app.get("/api/rates")
async def get_rates():
    try:
        with open("data/latest.json", "r") as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Belirli bir hedef kurun oranını döner (TRY → hedef)
@app.get("/api/rate")
async def get_specific_rate(
    target: str = Query(..., description="Hedef döviz, örn: USD")
):
    try:
        with open("data/latest.json", "r") as f:
            data = json.load(f)
            rates = data.get("rates", {})
            target = target.upper()

            if target not in rates:
                return JSONResponse(content={"error": f"{target} bulunamadı"}, status_code=404)

            base = data.get("base", "TRY")
            base_value = rates.get(base, 1.0)
            rate = rates[target] / base_value if base_value else None

            return {
                "base": base,
                "target": target,
                "rate": round(rate, 6)
            }

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Dövizler arası dönüşüm: base → target
@app.get("/api/convert")
async def convert_currency(
    base: str = Query(..., description="Baz döviz birimi (örn: USD)"),
    target: str = Query(..., description="Hedef döviz birimi (örn: EUR)"),
    amount: float = Query(1.0, description="Çevrilecek miktar")
):
    try:
        with open("data/latest.json", "r") as f:
            data = json.load(f)
            rates = data.get("rates", {})

            base = base.upper()
            target = target.upper()

            if base not in rates or target not in rates:
                return JSONResponse(content={"error": f"{base} veya {target} bulunamadı"}, status_code=400)

            base_rate = rates[base]
            target_rate = rates[target]

            # Hesap: amount * (target / base)
            result = amount * (target_rate / base_rate)

            return {
                "base": base,
                "target": target,
                "amount": amount,
                "result": round(result, 6)
            }

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/api/all")
async def get_all_conversions():
    try:
        with open("data/latest.json", "r") as f:
            data = json.load(f)
            rates = data.get("rates", {})
            date = data.get("date", None)

            all_rates = {}

            for base_currency, base_value in rates.items():
                base_conversions = {}
                for target_currency, target_value in rates.items():
                    if base_currency != target_currency:
                        base_conversions[target_currency] = round(target_value / base_value, 6)
                # TRY'yi de dahil et
                base_conversions["TRY"] = round(1 / base_value, 6)
                all_rates[base_currency] = base_conversions

            # TRY'nin diğerlerine oranı doğrudan yaz
            try_conversions = {}
            for target_currency, value in rates.items():
                try_conversions[target_currency] = round(value, 6)
            all_rates["TRY"] = try_conversions

            return {
                "date": date,
                "data": all_rates
            }

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
