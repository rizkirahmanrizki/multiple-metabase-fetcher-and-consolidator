# 📊 Google Sheets Metabase Sync (Python)

This project helps you **automatically move data from Metabase (or any BI tool)** into **Google Sheets** using Python.

Instead of manually exporting data every day or week, this script does it for you — **fast, automatic, and reliable**.

---

# 🧠 What This Project Does (Simple Explanation)

Think of this as a **data pipeline**:

```
Metabase (API)
      ↓
Python Script (this project)
      ↓
Google Sheets (multiple tabs/files)
      ↓
Combined into 1 master sheet
```

### In plain English:

* It **pulls data from Metabase dashboards**
* It **writes the data into Google Sheets**
* It **clears old data first (so no duplicates)**
* It can **handle large datasets safely**
* It **combines multiple sheets into one master sheet**

---

# 🎯 Why This Exists

Google Apps Script has limits:

* ❌ Timeout (6 minutes)
* ❌ Struggles with large datasets

This Python version solves that:

* ✅ No timeout (can run longer)
* ✅ Handles big data (chunk writing)
* ✅ Better error handling
* ✅ More scalable (can run on server / scheduler)

---

# 🚀 What Happens When You Run It

When you run:

```bash
python src/main.py
```

The script will:

### 1. 🔐 Authenticate

* Connect to Google Sheets using a service account
* Read your Metabase session token

---

### 2. 📥 Fetch Data

* Call Metabase API for each dataset:

  * CD
  * Transit
  * Direct
  * Milkrun

---

### 3. 🧹 Clean Data

* Format datetime fields
* Prepare rows for Google Sheets

---

### 4. 📄 Update Google Sheets

For each dataset:

* Clear old data
* Write new data (in chunks to avoid limits)

---

### 5. 📊 Create a Master Sheet

* Combine all sheets into one:
  → **"Consolidated"**

---

### 6. 🔔 (Optional) Notify

* Send message to Google Chat

---

# 📁 Project Structure (Beginner Friendly)

```
src/
│
├── main.py        → Runs everything (start here)
├── config.py      → Settings (IDs, URLs, credentials)
├── sheets.py      → Talks to Google Sheets
├── metabase.py    → Fetches data from API
├── utils.py       → Small helpers (formatting, cleaning)
```

---

# ⚙️ Setup Guide

## 1. Install Python packages

```bash
pip install -r requirements.txt
```

---

## 2. Setup credentials

Copy the example file:

```bash
cp .env.example .env
```

Fill in:

* Google Service Account details
* Metabase URL
* Sheet IDs

---

## 3. Share your Google Sheets

IMPORTANT ⚠️

You must share each sheet with your service account email:

```
your-service-account@project.iam.gserviceaccount.com
```

Otherwise you’ll get:

* ❌ 404 errors
* ❌ Permission denied

---

## 4. Run the script

```bash
python src/main.py
```

---

# 🧩 Key Concepts (Beginner Notes)

### 🔹 What is Metabase API?

It lets you **programmatically download data** from dashboards.

---

### 🔹 What is a Service Account?

A special Google account used by code (not a human).

---

### 🔹 Why chunking?

Google Sheets has limits.
So we write data in small batches instead of all at once.

---

### 🔹 Why clear sheet first?

To avoid:

* duplicate data
* outdated rows

---

# ⚠️ Common Errors & Fixes

### ❌ 404 Not Found

👉 Sheet ID wrong OR not shared
✔ Fix: Share sheet with service account

---

### ❌ Grid limit error

👉 Too much data for sheet
✔ Fix: Increase sheet rows OR split data

---

### ❌ No data returned

👉 API issue or wrong parameters
✔ Fix: Check Metabase query

---

# 📈 What You Can Use This For

* Daily / weekly reporting
* Operations dashboards
* BI → Google Sheets sync
* Lightweight ETL pipelines

---

# 🧠 Summary

This project is:

> A simple automation tool that moves data from Metabase into Google Sheets — safely and automatically.

---

# 🚀 Future Improvements (Optional)

* Run automatically (cron / scheduler)
* Deploy to cloud (Cloud Run)
* Add data transformations (pandas)
* Parallel jobs (faster)

---

If you're new to this:
👉 Start with `main.py` and follow the flow step by step.
