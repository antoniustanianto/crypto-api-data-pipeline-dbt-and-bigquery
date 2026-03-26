WITH base AS (
  SELECT
    asset,
    date,
    avg_price,
    FIRST_VALUE(avg_price) OVER (
      PARTITION BY asset ORDER BY date
    ) AS first_price
  FROM {{ ref('crypto_summary') }}
)

SELECT
  asset,
  date,
  avg_price,
  (avg_price / first_price) * 100 AS indexed_price
FROM base
