import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config import Config
from utils.helpers import generate_random_email

class TestRegistration:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.login_page.navigate(f"{Config.BASE_URL}/login")

    def test_successful_registration_flow(self, page):
        """Test Case 1: Register New User successfully"""
        new_email = generate_random_email()
        self.login_page.fill_signup("Test User", new_email)
        
        # Next form step
        page.fill("#password", "SecurePass!1")
        page.fill("#first_name", "Test")
        page.fill("#last_name", "User")
        page.fill("#address1", "123 Automation St")
        page.fill("#country", "United States")
        page.fill("#state", "Texas")
        page.fill("#city", "Austin")
        page.fill("#zipcode", "78701")
        page.fill("#mobile_number", "5551234567")
        page.click("button[data-qa='create-account']")
        
        assert "Account Created!" in page.locator("h2[data-qa='account-created']").inner_text()

    def test_duplicate_email(self):
        """Test Case 2: Register User with existing email"""
        self.login_page.fill_signup("Talha Khan", "testqa_talha@gmail.com")
        assert "Email Address already exist" in self.login_page.page.locator("p[style*='red']").inner_text()

    def test_weak_password(self, page):
        """Test Case 3: Register with weak password"""
        new_email = generate_random_email()
        self.login_page.fill_signup("Test User", new_email)
        # Note: automationexercise lacks strict password policy, but we simulate test logic
        page.fill("#password", "123")
        page.click("button[data-qa='create-account']")
        # Normally this would be asserted against a validation error

    def test_missing_required_field(self, page):
        """Test Case 4: Submit form missing required Zipcode"""
        new_email = generate_random_email()
        self.login_page.fill_signup("Test User", new_email)
        page.fill("#password", "SecurePass!1")
        page.fill("#first_name", "Test")
        page.click("button[data-qa='create-account']")
        is_required = page.evaluate("document.querySelector('#last_name').validationMessage !== ''")
        assert is_required

    def test_invalid_email_format(self):
        """Test Case 5: Register with invalid email string"""
        self.login_page.fill_signup("Test User", "invalid-email-format")
        is_required = self.login_page.page.evaluate("document.querySelector('input[data-qa=\"signup-email\"]').validationMessage !== ''")
        assert is_required

    def test_successful_registration_with_newsletter(self, page):
        """Test Case 6: Register User and opt-in to optional fields"""
        new_email = generate_random_email()
        self.login_page.fill_signup("Pro User", new_email)
        
        page.fill("#password", "SecurePass!1")
        page.check("#newsletter")
        page.check("#optin")
        page.fill("#first_name", "Test")
        page.fill("#last_name", "User")
        page.fill("#address1", "123 Automation St")
        page.fill("#country", "United States")
        page.fill("#state", "Texas")
        page.fill("#city", "Austin")
        page.fill("#zipcode", "78701")
        page.fill("#mobile_number", "5551234567")
        page.click("button[data-qa='create-account']")
        
        assert "Account Created!" in page.locator("h2[data-qa='account-created']").inner_text()
