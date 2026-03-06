from playwright.sync_api import Page, expect

class BasePage:
    """Base class for all Page Objects containing common methods."""
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def wait_for_element(self, selector: str, state: str = "visible"):
        self.page.wait_for_selector(selector, state=state)

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"reports/screenshots/{name}.png", full_page=True)

    def verify_title(self, title: str):
        expect(self.page).to_have_title(title)
