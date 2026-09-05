import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import gspread
from google.oauth2.service_account import Credentials

CREDENTIALS_FILE = r"d:\infonix\sheet-sync-504707-85df40232946.json"
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
gc = gspread.authorize(creds)

print("=" * 80)
print("AUDITING SHEET 1: ODOO DIRECT SALES LEADS")
print("Spreadsheet ID: 1X_8LbsHisyvoCfjSuTX5yRVsRgXPDEmu3W5RWXuAC1o")
print("=" * 80)
odoo_sheet = gc.open_by_key("1X_8LbsHisyvoCfjSuTX5yRVsRgXPDEmu3W5RWXuAC1o").sheet1
odoo_rows = odoo_sheet.get_all_records()
print(f"[✓] Total Verified Rows in Odoo Sheet: {len(odoo_rows)}")
for idx, r in enumerate(odoo_rows, 1):
    comp = r.get("Company Name", "")
    person = r.get("Contact Person", "")
    title = r.get("Job Title", "")
    phone = r.get("Phone Number", "")
    email = r.get("Work Email", "")
    grade = r.get("Partner Grade", "")
    print(f"Row {idx:02d}: {person} | {title} | Company: {comp} | Phone: {phone} | Email: {email} | Grade: {grade}")

print("\n" + "=" * 80)
print("AUDITING SHEET 2: ZOHO DIRECT SALES LEADS")
print("Spreadsheet ID: 18oHqPuo6BhAgI5e_GLSSps5fSc_DpzYEYofgPKxBv9o")
print("=" * 80)
zoho_sheet = gc.open_by_key("18oHqPuo6BhAgI5e_GLSSps5fSc_DpzYEYofgPKxBv9o").sheet1
zoho_rows = zoho_sheet.get_all_records()
print(f"[✓] Total Verified Rows in Zoho Sheet: {len(zoho_rows)}")
for idx, r in enumerate(zoho_rows, 1):
    comp = r.get("Company Name", "")
    person = r.get("Contact Person", "")
    title = r.get("Job Title", "")
    phone = r.get("Phone Number", "")
    email = r.get("Work Email", "")
    grade = r.get("Partner Grade", "")
    print(f"Row {idx:02d}: {person} | {title} | Company: {comp} | Phone: {phone} | Email: {email} | Grade: {grade}")
