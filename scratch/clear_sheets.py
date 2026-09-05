import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import gspread
from google.oauth2.service_account import Credentials

CREDENTIALS_FILE = r"d:\infonix\sheet-sync-504707-85df40232946.json"
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
gc = gspread.authorize(creds)

HEADERS = [
    "Scraped Date",
    "Lead Source",
    "Scraped Website Source URL",
    "Company Name",
    "Contact Person",
    "First Name",
    "Last Name",
    "Job Title",
    "Work Email",
    "Phone Number",
    "Company Website URL",
    "LinkedIn / Social Profile URL",
    "City",
    "State",
    "Country",
    "Industry / Module Focus",
    "Partner Grade",
    "Lead Status",
    "Call Status",
    "Follow Up Notes",
    "Description"
]

print("Clearing Sheet 1 (Odoo)...", flush=True)
odoo_sheet = gc.open_by_key("1X_8LbsHisyvoCfjSuTX5yRVsRgXPDEmu3W5RWXuAC1o").sheet1
odoo_sheet.clear()
odoo_sheet.update(range_name="A1", values=[HEADERS])
print("[✓] Sheet 1 (Odoo) cleared successfully.", flush=True)

print("Clearing Sheet 2 (Zoho)...", flush=True)
zoho_sheet = gc.open_by_key("18oHqPuo6BhAgI5e_GLSSps5fSc_DpzYEYofgPKxBv9o").sheet1
zoho_sheet.clear()
zoho_sheet.update(range_name="A1", values=[HEADERS])
print("[✓] Sheet 2 (Zoho) cleared successfully.", flush=True)
