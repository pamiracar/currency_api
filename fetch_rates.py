import requests
import xml.etree.ElementTree as ET
import json
from datetime import datetime
import os

def fetch_tcmb():
    print("TCMB veri çekme başladı...")

    url = "https://www.tcmb.gov.tr/kurlar/today.xml"
    response = requests.get(url, timeout=10)
    print("Status Code:", response.status_code)
    if response.status_code != 200:
        print("API çağrısı başarısız.")
        return

    tree = ET.ElementTree(ET.fromstring(response.content))
    root = tree.getroot()

    rates = {}
    for currency in root.findall("Currency"):
        code = currency.get("CurrencyCode")
        forex_selling = currency.find("ForexSelling")
        if forex_selling is not None and forex_selling.text:
            try:
                rates[code] = float(forex_selling.text.replace(",", "."))
                print(f"{code}: {rates[code]}")
            except ValueError:
                continue

    result = {
        "base": "TRY",
        "date": datetime.now().strftime("%Y %m %d"),
        "rates": rates,
    }

    os.makedirs("data", exist_ok=True)
    with open("data/latest.json", "w") as f:
        json.dump(result, f, indent=2)

    print("TCMB verisi kaydedildi: data/latest.json")

if __name__ == "__main__":
    fetch_tcmb()
