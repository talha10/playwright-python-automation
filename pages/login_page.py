from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object for the Authentication (Login/Signup) Page."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_email_input = "input[data-qa='login-email']"
        self.login_password_input = "input[data-qa='login-password']"
        self.login_button = "button[data-qa='login-button']"
        self.signup_name_input = "input[data-qa='signup-name']"
        self.signup_email_input = "input[data-qa='signup-email']"
        self.signup_button = "button[data-qa='signup-button']"
        self.error_message = "p[style='color: red;']"

    def enter_email(self, email: str):
        self.fill(self.login_email_input, email)

    def enter_password(self, password: str):
        self.fill(self.login_password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def get_error_message(self) -> str:
        self.wait_for_element(self.error_message)
        return self.page.locator(self.error_message).inner_text()
    
    def fill_signup(self, name: str, email: str):
        self.fill(self.signup_name_input, name)
        self.fill(self.signup_email_input, email)
        self.click(self.signup_button)
