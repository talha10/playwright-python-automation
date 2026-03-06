import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config

@pytest.fixture(scope="session")
def browser():
    """Session level browser instance."""
    with sync_playwright() as p:
        browser_type = getattr(p, Config.BROWSER_TYPE)
        browser = browser_type.launch(
            headless=Config.HEADLESS,
            slow_mo=Config.SLOW_MO,
            args=["--disable-popup-blocking"]
        )
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Provides a fresh authenticated-free page instance per test."""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True
    )
    # Start tracing for failure debugging
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page = context.new_page()
    yield page
    
    context.tracing.stop()
    context.close()

@pytest.fixture(scope="function")
def authenticated_page(browser):
    """Provides a page pre-authenticated via cookies/localstorage (Placeholder logic)."""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    page = context.new_page()
    
    # 1. Navigate to login
    page.goto(f"{Config.BASE_URL}/login")
    
    # 2. Enter valid static credentials
    page.fill("input[data-qa='login-email']", "testqa_talha@gmail.com")
    page.fill("input[data-qa='login-password']", "Test@1234")
    page.click("button[data-qa='login-button']")
    
    # 3. Wait for dashboard / authentication state
    page.wait_for_selector("a[href='/logout']")
    
    yield page
    context.close()
