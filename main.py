from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.get("/api/rates")
async def get_rates():
    try:
        with open("data/latest.json", "r") as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

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
