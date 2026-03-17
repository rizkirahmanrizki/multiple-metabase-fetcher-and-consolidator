# 📊 Google Sheets Metabase Sync (Python)

This project helps you **automatically move data from multiple Metabase queries (or any BI tool)** into **Google Sheets** using Python.

Instead of manually exporting data every day or week, this script does it for you — **fast, automatic, and reliable**.

---

# 🧠 What This Project Does

This script automates a common workflow:

```id="flow2"
Data Source API → Python Script → Google Sheets → Combined Report
```

### In simple terms:

* It retrieves data from one or more API endpoints
* It writes each dataset into a Google Sheet
* It clears old data before updating
* It combines multiple datasets into a single “master” sheet

---

# 🎯 Use Cases

You can use this project for:

* 📈 Business reporting
* 📊 Dashboard data pipelines
* 🔄 Scheduled data sync (daily / weekly)
* 🧾 Operational tracking in Google Sheets

---

# 🚀 How It Works

When you run the script:

```bash id="run2"
python src/main.py
```

It performs the following steps:

### 1. 🔐 Connect to Google Sheets

Uses a service account to access your spreadsheets.

---

### 2. 📥 Fetch Data from API

Calls one or more API endpoints to retrieve data.

Each dataset is defined as a “job” in the code.

---

### 3. 🧹 Prepare Data

* Cleans formatting (e.g. date/time fields)
* Structures rows for Google Sheets

---

### 4. 📄 Update Sheets

For each dataset:

* Clears existing content
* Writes fresh data (in chunks to handle large volumes)

---

### 5. 📊 Create a Combined Sheet

All datasets are merged into one **consolidated sheet** for easier analysis.

---

### 6. 🔔 Optional Notification

Can send a message (e.g. to Google Chat) after completion.

---

# 📁 Project Structure

```id="structure2"
src/
│
├── main.py        → Main script (runs everything)
├── config.py      → Configuration (IDs, settings)
├── sheets.py      → Google Sheets integration
├── metabase.py    → API data fetching
├── utils.py       → Helper functions
```

---

# ⚙️ Setup

## 1. Install dependencies

```bash id="install2"
pip install -r requirements.txt
```

---

## 2. Configure environment

```bash id="env2"
cp .env.example .env
```

Fill in your credentials and configuration values.

---

## 3. Share your Google Sheets

Make sure your target sheets are shared with your service account email.

---

## 4. Run the script

```bash id="run3"
python src/main.py
```

---

# 🧩 Key Concepts

### 🔹 API Data Source

The script pulls data from an external system via API (e.g. BI platform, database service, etc.).

---

### 🔹 Google Service Account

A special Google account used by the script to access Sheets automatically.

---

### 🔹 Chunked Writing

Large datasets are written in smaller batches to avoid Google Sheets limits.

---

### 🔹 Consolidation

Multiple datasets are merged into one final sheet for easier reporting.

---

# ⚠️ Common Issues

### Sheet not updating

* Check permissions (share with service account)

### No data returned

* Verify API endpoint or parameters

### Large dataset issues

* Ensure your sheet has enough rows/columns

---

# 🧠 Summary

This project is a **lightweight data pipeline**:

> It moves data from an API into Google Sheets automatically, safely handling large datasets and combining results into a single report.

---

# 🚀 Possible Improvements

* Schedule execution (cron / scheduler)
* Deploy to cloud (Cloud Run, VM)
* Add data transformations (pandas)
* Parallel processing for faster jobs

---

