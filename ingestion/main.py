import requests
import pandas as pd
from google.cloud import bigquery
from datetime import datetime, timezone

# 🔧 SETUP
PROJECT_ID = "de-crypto-project-491302"
TABLE_ID = "de-crypto-project-491302.crypto_data.raw_prices"

# 🔌 BigQuery client
client = bigquery.Client.from_service_account_json(
    "json file loc"
)

# 🪙 Assets
assets = ["bitcoin", "ethereum"]

all_data = []

for asset in assets:
    print(f"Fetching {asset}...")

    url = f"https://api.coingecko.com/api/v3/coins/{asset}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "30"
    }

    response = requests.get(url, params=params)
    data = response.json()

    prices = data["prices"]  # format: [timestamp, price]

    for item in prices:
        ts = datetime.fromtimestamp(item[0] / 1000, tz=timezone.utc)
        price = item[1]

        all_data.append({
            "asset": asset,
            "price": price,
            "timestamp": ts
        })

# 📊 Convert ke DataFrame
df = pd.DataFrame(all_data)

print(df.head())
print(f"Total rows: {len(df)}")

# 🚀 Load ke BigQuery
job = client.load_table_from_dataframe(df, TABLE_ID)
job.result()

print("✅ Historical data (30 days) berhasil masuk ke BigQuery!")
