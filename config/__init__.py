"""
Configuration package for unified Data Scraping framework.
"""

from .settings import settings
from .schemas import STANDARD_HEADERS, ZOHO_CRM_HEADERS, create_standard_lead
from .constants import USER_AGENTS, DEFAULT_KEYWORDS, DEFAULT_LOCATIONS

SPREADSHEET_ID_ODOO = getattr(settings, "SPREADSHEET_ID_ODOO", "")
SPREADSHEET_ID_ZOHO = getattr(settings, "SPREADSHEET_ID_ZOHO", "")
HEADERS = STANDARD_HEADERS
SERVICE_ACCOUNT_INFO = settings.get_service_account_info() if hasattr(settings, "get_service_account_info") else {}
CREDENTIALS_FILE = getattr(settings, "CREDENTIALS_FILE", "")

__all__ = [
    "settings",
    "STANDARD_HEADERS",
    "ZOHO_CRM_HEADERS",
    "create_standard_lead",
    "USER_AGENTS",
    "DEFAULT_KEYWORDS",
    "DEFAULT_LOCATIONS",
    "SPREADSHEET_ID_ODOO",
    "SPREADSHEET_ID_ZOHO",
    "HEADERS",
    "SERVICE_ACCOUNT_INFO",
    "CREDENTIALS_FILE",
]
