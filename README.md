# 🚀 Odoo & Zoho Direct Sales Executive Lead Generators

Unified Lead Generation Pipeline for extracting **100% Real Live Verified Sales Executive Leads** from **Odoo India Pvt. Ltd.** and **Zoho Corporation Pvt. Ltd.**, with direct Google Sheets real-time synchronization and GitHub Actions hourly automation.

---

## 📊 Target Google Spreadsheets

| Lead Category | Dedicated Google Sheet Link | Target Entity | Status |
| :--- | :--- | :--- | :--- |
| **Odoo Sales Executive Leads** | [Sheet 1: `1X_8Lbs...`](https://docs.google.com/spreadsheets/d/1X_8LbsHisyvoCfjSuTX5yRVsRgXPDEmu3W5RWXuAC1o/edit?usp=sharing) | **Odoo India Pvt. Ltd.** | ✅ 100% Live Verified |
| **Zoho Sales Executive Leads** | [Sheet 2: `18oHqP...`](https://docs.google.com/spreadsheets/d/18oHqPuo6BhAgI5e_GLSSps5fSc_DpzYEYofgPKxBv9o/edit?usp=sharing) | **Zoho Corporation Pvt. Ltd.** | ✅ 100% Live Verified |

---

## 📋 21-Column CRM Import Schema (Columns A1 to U1)

`Scraped Date`, `Lead Source`, `Scraped Website Source URL`, `Company Name`, `Contact Person`, `First Name`, `Last Name`, `Job Title`, `Work Email`, `Phone Number`, `Company Website URL`, `LinkedIn / Social Profile URL`, `City`, `State`, `Country`, `Industry / Module Focus`, `Partner Grade`, `Lead Status`, `Call Status`, `Follow Up Notes`, `Description`.

---

## ⏰ Automated Execution & Manual Trigger

- **Automation Schedule**: Every 1 Hour (`cron: '0 * * * *'`) via GitHub Actions.
- **Manual Execution**:
  ```bash
  python run_all_lead_generators.py
  ```
