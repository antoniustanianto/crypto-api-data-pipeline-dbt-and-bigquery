from google.cloud import bigquery

client = bigquery.Client.from_service_account_json(
    "json file location"
)

print("✅ Connected!")