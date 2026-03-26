# 🚀 Crypto Data Pipeline & Analytics Dashboard

## 📌 Overview

This project demonstrates an **end-to-end data pipeline** for cryptocurrency analytics, covering data ingestion, transformation, and visualization.

The pipeline collects historical price data for **Bitcoin and Ethereum**, processes it using modern data stack tools, and presents insights through an interactive dashboard.

---

## 🧱 Tech Stack

* **Python** → Data ingestion from API
* **BigQuery** → Data warehouse
* **dbt (Data Build Tool)** → Data transformation & modeling
* **Looker Studio** → Data visualization

---

## 🔄 Data Pipeline Architecture

```
API (CoinGecko)
    ↓
Python (Ingestion)
    ↓
BigQuery (Raw Table)
    ↓
dbt (Staging & Mart Models)
    ↓
Looker Studio (Dashboard)
```

---

## 📊 Data Models

### 🔹 Staging Layer

* `stg_crypto.sql`
* Cleans and standardizes raw data

### 🔹 Mart Layer

* `crypto_summary.sql`
* Aggregates daily metrics:

  * Average price
  * Max price
  * Min price

### 🔹 Analytics Layer

* `crypto_indexed.sql`
* Normalizes price to **Base 100** for fair comparison

---

## 📈 Dashboard Features

* KPI Metrics (BTC & ETH)
* Price Trend Visualization
* Comparative Analysis using Indexed Performance (Base 100)

---

## 📸 Dashboard Preview

![Dashboard](screenshots/dashboard_overview.png)

---

## ⚙️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run ingestion script

```
python ingestion/main.py
```

### 3. Run dbt models

```
dbt run
```

---

## 💡 Key Insights

* Bitcoin has higher absolute price but lower relative growth compared to Ethereum
* Indexed analysis provides a clearer comparison across assets with different scales

---

## 🎯 What I Learned

* Building end-to-end data pipelines
* Data modeling using dbt (staging & mart layers)
* Handling data granularity and aggregation
* Designing business-friendly dashboards

---

## 📬 Contact

Feel free to connect with me on LinkedIn!
