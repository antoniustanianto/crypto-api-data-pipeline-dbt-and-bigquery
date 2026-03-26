SELECT
  asset,
  price AS price_usd,
  TIMESTAMP(timestamp) AS timestamp
FROM `de-crypto-project-491302.crypto_data.raw_prices`
