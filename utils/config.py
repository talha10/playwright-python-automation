import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Centralized configuration loaded from environment variables."""
    BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))
    BROWSER_TYPE = os.getenv("BROWSER_TYPE", "chromium")
    
    # Global Timeouts
    TIMEOUT_MS = 15000
    NAVIGATION_TIMEOUT_MS = 30000
