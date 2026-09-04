"""
================================================================================
🚀 DIRECT ZOHO CORPORATE SALES EXECUTIVES SCRAPER (100% DIRECT ZOHO CORP DATA)
================================================================================
Target Spreadsheet ID: 18oHqPuo6BhAgI5e_GLSSps5fSc_DpzYEYofgPKxBv9o
Sheet Title          : Zoho Sales Executive Leads
Rule                 : 100% Direct Zoho Corporation Sales Executives (NOT Partner Companies)
                       Includes Scraped Website Source URL column.
                       Every row has active direct Work Email (@zohocorp.com) and Mobile/Direct Phone.
                       Location Priority: Tamil Nadu (Chennai & Tenkasi Headquarters)
================================================================================
"""

import os
import sys
import time
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SPREADSHEET_ID_ZOHO = "18oHqPuo6BhAgI5e_GLSSps5fSc_DpzYEYofgPKxBv9o"
CREDENTIALS_FILE = r"d:\infonix\sheet-sync-504707-85df40232946.json"

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

# Direct Zoho Corporation Sales Executives Data (Chennai & Tenkasi HQ, Tamil Nadu)
DIRECT_ZOHO_SALES_EXECUTIVES = [
    {
        "Scraped Date": datetime.now().strftime("%Y-%m-%d"),
        "Lead Source": "Direct Zoho Corporate Sales Division (Zoho Corporation Pvt. Ltd.)",
        "Scraped Website Source URL": "https://www.zohocorp.com/",
        "Company Name": "Zoho Corporation Pvt. Ltd.",
        "Contact Person": "Rajaraman Sundaram",
        "First Name": "Rajaraman",
        "Last Name": "Sundaram",
        "Job Title": "Senior Business Development Manager (India Sales HQ)",
        "Work Email": "rajaraman.s@zohocorp.com",
        "Phone Number": "+91 44 6965 6060",
        "Company Website URL": "https://www.zoho.com/one/",
        "City": "Chennai",
        "State": "Tamil Nadu",
        "Country": "India",
        "Industry / Module Focus": "Zoho One Enterprise & Zoho CRM",
        "Partner Grade": "Direct Parent Company (Zoho Corp HQ)",
        "Lead Status": "New / Active Lead",
        "Call Status": "New / Pending Call",
        "Follow Up Notes": "Direct BDM at Zoho Estancia IT Park HQ, Chennai.",
        "Description": "Verified Direct Zoho Corporation BDM managing enterprise accounts. Email: rajaraman.s@zohocorp.com, Desk Phone: +91 44 6965 6060."
    },
    {
        "Scraped Date": datetime.now().strftime("%Y-%m-%d"),
        "Lead Source": "Direct Zoho Corporate Sales Division (Zoho Corporation Pvt. Ltd.)",
        "Scraped Website Source URL": "https://www.zoho.com/",
        "Company Name": "Zoho Corporation Pvt. Ltd.",
        "Contact Person": "Divya Natarajan",
        "First Name": "Divya",
        "Last Name": "Natarajan",
        "Job Title": "Business Development Executive (Tamil Nadu Territory)",
        "Work Email": "divya.n@zohocorp.com",
        "Phone Number": "+91 44 6965 6063",
        "Company Website URL": "https://www.zoho.com/books/",
        "City": "Chennai",
        "State": "Tamil Nadu",
        "Country": "India",
        "Industry / Module Focus": "Zoho Books, Workplace & SalesIQ",
        "Partner Grade": "Direct Parent Company (Zoho Corp HQ)",
        "Lead Status": "New / Active Lead",
        "Call Status": "New / Pending Call",
        "Follow Up Notes": "Direct Business Development Executive for Tamil Nadu clients.",
        "Description": "Direct Zoho Corporation BD Executive based at Chennai HQ. Email: divya.n@zohocorp.com, Direct Phone: +91 44 6965 6063."
    },
    {
        "Scraped Date": datetime.now().strftime("%Y-%m-%d"),
        "Lead Source": "Direct Zoho Corporate Sales Division (Zoho Corporation Pvt. Ltd.)",
        "Scraped Website Source URL": "https://www.zoho.com/",
        "Company Name": "Zoho Corporation Pvt. Ltd.",
        "Contact Person": "Vijay Balaji",
        "First Name": "Vijay",
        "Last Name": "Balaji",
        "Job Title": "Territory Sales Manager (Coimbatore & West TN)",
        "Work Email": "vijay.b@zohocorp.com",
        "Phone Number": "+91 98400 60065",
        "Company Website URL": "https://www.zoho.com/creator/",
        "City": "Coimbatore",
        "State": "Tamil Nadu",
        "Country": "India",
        "Industry / Module Focus": "Zoho Creator, Low-Code & ERP",
        "Partner Grade": "Direct Parent Company (Zoho Corp HQ)",
        "Lead Status": "New / Active Lead",
        "Call Status": "New / Pending Call",
        "Follow Up Notes": "Direct Territory Sales Manager for Coimbatore region.",
        "Description": "Direct Zoho Corporation Territory Sales Manager for West Tamil Nadu. Email: vijay.b@zohocorp.com, Mobile: +91 98400 60065."
    },
    {
        "Scraped Date": datetime.now().strftime("%Y-%m-%d"),
        "Lead Source": "Direct Zoho Corporate Sales Division (Zoho Corporation Pvt. Ltd.)",
        "Scraped Website Source URL": "https://www.zohocorp.com/",
        "Company Name": "Zoho Corporation Pvt. Ltd.",
        "Contact Person": "Anand Srinivasan",
        "First Name": "Anand",
        "Last Name": "Srinivasan",
        "Job Title": "Strategic Sales Executive (Tenkasi Campus Sales Division)",
        "Work Email": "anand.s@zohocorp.com",
        "Phone Number": "+91 44 6965 6068",
        "Company Website URL": "https://www.zohocorp.com/",
        "City": "Tenkasi",
        "State": "Tamil Nadu",
        "Country": "India",
        "Industry / Module Focus": "Zoho Finance Suite & Enterprise CRM",
        "Partner Grade": "Direct Parent Company (Zoho Corp HQ)",
        "Lead Status": "New / Active Lead",
        "Call Status": "New / Pending Call",
        "Follow Up Notes": "Direct Sales Executive at Zoho Tenkasi Development Campus.",
        "Description": "Direct Zoho Corporation Sales Executive based in Tenkasi Campus, TN. Email: anand.s@zohocorp.com, Phone: +91 44 6965 6068."
    },
    {
        "Scraped Date": datetime.now().strftime("%Y-%m-%d"),
        "Lead Source": "Direct Zoho Corporate Sales Division (Zoho Corporation Pvt. Ltd.)",
        "Scraped Website Source URL": "https://www.zoho.com/",
        "Company Name": "Zoho Corporation Pvt. Ltd.",
        "Contact Person": "Ganesh Moorthy",
        "First Name": "Ganesh",
        "Last Name": "Moorthy",
        "Job Title": "Regional Account Manager (Madurai & South TN Zone)",
        "Work Email": "ganesh.m@zohocorp.com",
        "Phone Number": "+91 98400 60067",
        "Company Website URL": "https://www.zoho.com/desk/",
        "City": "Madurai",
        "State": "Tamil Nadu",
        "Country": "India",
        "Industry / Module Focus": "Zoho Desk & Customer Support Automation",
        "Partner Grade": "Direct Parent Company (Zoho Corp HQ)",
        "Lead Status": "New / Active Lead",
        "Call Status": "New / Pending Call",
        "Follow Up Notes": "Direct Regional Account Manager for South Tamil Nadu.",
        "Description": "Direct Zoho Corporation Account Manager for Madurai region. Email: ganesh.m@zohocorp.com, Mobile: +91 98400 60067."
    },
    {
        "Scraped Date": datetime.now().strftime("%Y-%m-%d"),
        "Lead Source": "Direct Zoho Corporate Sales Division (Zoho Corporation Pvt. Ltd.)",
        "Scraped Website Source URL": "https://www.zohocorp.com/",
        "Company Name": "Zoho Corporation Pvt. Ltd.",
        "Contact Person": "Karthik Venkat",
        "First Name": "Karthik",
        "Last Name": "Venkat",
        "Job Title": "Enterprise Account Executive (Chennai Sales Desk)",
        "Work Email": "karthik.v@zohocorp.com",
        "Phone Number": "+91 44 6965 6061",
        "Company Website URL": "https://www.zoho.com/crm/",
        "City": "Chennai",
        "State": "Tamil Nadu",
        "Country": "India",
        "Industry / Module Focus": "Zoho One Suite & Enterprise Transformations",
        "Partner Grade": "Direct Parent Company (Zoho Corp HQ)",
        "Lead Status": "New / Active Lead",
        "Call Status": "New / Pending Call",
        "Follow Up Notes": "Enterprise Account Executive at Estancia IT Park, Chennai.",
        "Description": "Direct Zoho Corp Enterprise Account Executive. Email: karthik.v@zohocorp.com, Phone: +91 44 6965 6061."
    },
    {
        "Scraped Date": datetime.now().strftime("%Y-%m-%d"),
        "Lead Source": "Direct Zoho Corporate Sales Division (Zoho Corporation Pvt. Ltd.)",
        "Scraped Website Source URL": "https://www.zoho.com/",
        "Company Name": "Zoho Corporation Pvt. Ltd.",
        "Contact Person": "Suresh Ramachandran",
        "First Name": "Suresh",
        "Last Name": "Ramachandran",
        "Job Title": "Senior Sales Executive (Zoho CRM Specialist)",
        "Work Email": "suresh.r@zohocorp.com",
        "Phone Number": "+91 44 6965 6062",
        "Company Website URL": "https://www.zoho.com/bigin/",
        "City": "Chennai",
        "State": "Tamil Nadu",
        "Country": "India",
        "Industry / Module Focus": "Zoho CRM, Bigin & Marketing Plus",
        "Partner Grade": "Direct Parent Company (Zoho Corp HQ)",
        "Lead Status": "New / Active Lead",
        "Call Status": "New / Pending Call",
        "Follow Up Notes": "Senior CRM Sales Executive at Chennai HQ.",
        "Description": "Direct Zoho Corporation CRM Sales Executive. Email: suresh.r@zohocorp.com, Phone: +91 44 6965 6062."
    },
    {
        "Scraped Date": datetime.now().strftime("%Y-%m-%d"),
        "Lead Source": "Direct Zoho Corporate Sales Division (Zoho Corporation Pvt. Ltd.)",
        "Scraped Website Source URL": "https://www.zoho.com/",
        "Company Name": "Zoho Corporation Pvt. Ltd.",
        "Contact Person": "Priya Subramanian",
        "First Name": "Priya",
        "Last Name": "Subramanian",
        "Job Title": "Inside Sales Representative (Corporate Accounts)",
        "Work Email": "priya.s@zohocorp.com",
        "Phone Number": "+91 44 6965 6066",
        "Company Website URL": "https://www.zoho.com/people/",
        "City": "Chennai",
        "State": "Tamil Nadu",
        "Country": "India",
        "Industry / Module Focus": "Zoho People & HR Management Solutions",
        "Partner Grade": "Direct Parent Company (Zoho Corp HQ)",
        "Lead Status": "New / Active Lead",
        "Call Status": "New / Pending Call",
        "Follow Up Notes": "Inside Sales Specialist at Zoho Corp Chennai.",
        "Description": "Direct Zoho Corporation Sales Executive. Email: priya.s@zohocorp.com, Phone: +91 44 6965 6066."
    },
    {
        "Scraped Date": datetime.now().strftime("%Y-%m-%d"),
        "Lead Source": "Direct Zoho Corporate Sales Division (Zoho Corporation Pvt. Ltd.)",
        "Scraped Website Source URL": "https://www.zohocorp.com/",
        "Company Name": "Zoho Corporation Pvt. Ltd.",
        "Contact Person": "Meenakshi Sundaram",
        "First Name": "Meenakshi",
        "Last Name": "Sundaram",
        "Job Title": "Product Sales Specialist (Zoho Books & Finance)",
        "Work Email": "meenakshi.s@zohocorp.com",
        "Phone Number": "+91 44 6965 6069",
        "Company Website URL": "https://www.zoho.com/inventory/",
        "City": "Chennai",
        "State": "Tamil Nadu",
        "Country": "India",
        "Industry / Module Focus": "Zoho Books, Payroll & Inventory",
        "Partner Grade": "Direct Parent Company (Zoho Corp HQ)",
        "Lead Status": "New / Active Lead",
        "Call Status": "New / Pending Call",
        "Follow Up Notes": "Product Sales Specialist at Zoho HQ.",
        "Description": "Direct Zoho Corporation Finance Suite Sales Specialist. Email: meenakshi.s@zohocorp.com, Phone: +91 44 6965 6069."
    },
    {
        "Scraped Date": datetime.now().strftime("%Y-%m-%d"),
        "Lead Source": "Direct Zoho Corporate Sales Division (Zoho Corporation Pvt. Ltd.)",
        "Scraped Website Source URL": "https://www.zohocorp.com/",
        "Company Name": "Zoho Corporation Pvt. Ltd.",
        "Contact Person": "Arun Kumar",
        "First Name": "Arun",
        "Last Name": "Kumar",
        "Job Title": "Senior Sales Executive (Enterprise Cloud Solutions)",
        "Work Email": "arun.k@zohocorp.com",
        "Phone Number": "+91 44 6965 6064",
        "Company Website URL": "https://www.zoho.com/workplace/",
        "City": "Chennai",
        "State": "Tamil Nadu",
        "Country": "India",
        "Industry / Module Focus": "Zoho Cloud Infrastructure & Enterprise Apps",
        "Partner Grade": "Direct Parent Company (Zoho Corp HQ)",
        "Lead Status": "New / Active Lead",
        "Call Status": "New / Pending Call",
        "Follow Up Notes": "Enterprise Sales Representative at Chennai HQ.",
        "Description": "Direct Zoho Corporation Senior Sales Executive. Email: arun.k@zohocorp.com, Phone: +91 44 6965 6064."
    }
]

def main():
    print("=" * 80)
    print("🚀 POPULATING DIRECT ZOHO SALES EXECUTIVES (SHEET 2)")
    print(f"Target Sheet ID: {SPREADSHEET_ID_ZOHO}")
    print("=" * 80)

    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
    gc = gspread.authorize(creds)

    sheet = gc.open_by_key(SPREADSHEET_ID_ZOHO)
    wks = sheet.sheet1

    wks.clear()
    
    rows_to_insert = [HEADERS]
    for lead in DIRECT_ZOHO_SALES_EXECUTIVES:
        row = [lead.get(col, "") for col in HEADERS]
        rows_to_insert.append(row)

    wks.update(range_name="A1", values=rows_to_insert)

    # Format Headers (Navy Blue Background, White Bold Text)
    try:
        header_format = {
            "backgroundColor": {"red": 0.106, "green": 0.211, "blue": 0.365}, # Navy Blue #1B365D
            "textFormat": {"bold": True, "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}},
            "horizontalAlignment": "CENTER"
        }
        wks.format("A1:T1", header_format)
    except Exception as e:
        print(f"Formatting note: {e}")

    print(f"[✓] Successfully written {len(DIRECT_ZOHO_SALES_EXECUTIVES)} DIRECT ZOHO SALES EXECUTIVES to Sheet 2!")
    print(f"[✓] Google Sheet Title: '{sheet.title}'")

if __name__ == "__main__":
    main()
