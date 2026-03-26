SELECT
  asset,
  DATE(timestamp) AS date,
  AVG(price_usd) AS avg_price,
  MAX(price_usd) AS max_price,
  MIN(price_usd) AS min_price,
  COUNT(*) AS total_records
FROM {{ ref('stg_crypto') }}
GROUP BY asset, date