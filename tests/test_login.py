import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config import Config

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.login_page.navigate(f"{Config.BASE_URL}/login")
        self.home_page.click_login_signup_menu()

    def test_valid_login(self):
        """Test Case 1: Valid Login Details"""
        self.login_page.enter_email("testqa_talha@gmail.com")
        self.login_page.enter_password("Test@1234")
        self.login_page.click_login()
        assert self.home_page.is_user_logged_in(), "User is not logged in."

    def test_invalid_password(self):
        """Test Case 2: Incorrect Password"""
        self.login_page.enter_email("testqa_talha@gmail.com")
        self.login_page.enter_password("wrongpass123")
        self.login_page.click_login()
        assert "incorrect" in self.login_page.get_error_message().lower()

    def test_empty_fields(self, page):
        """Test Case 3: Empty Fields Validation"""
        self.login_page.enter_email("")
        self.login_page.enter_password("")
        self.login_page.click_login()
        is_required = page.evaluate("document.querySelector('input[data-qa=\"login-email\"]').validationMessage !== ''")
        assert is_required

    def test_sql_injection_attempt(self):
        """Test Case 4: SQL Injection in Email Field"""
        self.login_page.enter_email("' OR 1=1 --")
        self.login_page.enter_password("password")
        self.login_page.click_login()
        assert "incorrect" in self.login_page.get_error_message().lower()

    def test_very_long_input(self):
        """Test Case 5: Very Long Input Boundaries"""
        self.login_page.enter_email("a" * 300 + "@example.com")
        self.login_page.enter_password("Test@1234")
        self.login_page.click_login()
        assert "incorrect" in self.login_page.get_error_message().lower()

    def test_special_chars(self):
        """Test Case 6: Special Characters in Email"""
        self.login_page.enter_email("user*&^%$@test.com")
        self.login_page.enter_password("Test@1234")
        self.login_page.click_login()
        assert "incorrect" in self.login_page.get_error_message().lower()

    def test_remember_me(self, page):
        """Test Case 7: Remember Me functionality (MOCK)"""
        # Note: automationexercise.com doesn't explicitly have a remember me checkbox
        # This acts as a mock verification for standard suites
        self.login_page.enter_email("testqa_talha@gmail.com")
        self.login_page.enter_password("Test@1234")
        self.login_page.click_login()
        assert self.home_page.is_user_logged_in()

    def test_logout(self):
        """Test Case 8: Logout from authenticated state"""
        self.login_page.enter_email("testqa_talha@gmail.com")
        self.login_page.enter_password("Test@1234")
        self.login_page.click_login()
        assert self.home_page.is_user_logged_in()
        self.home_page.click(self.home_page.logout_menu_link)
        self.home_page.wait_for_element(self.home_page.login_menu_link)
        assert not self.home_page.is_user_logged_in()
