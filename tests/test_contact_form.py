import pytest
from pages.home_page import HomePage
from utils.config import Config

class TestContactForm:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.home_page = HomePage(page)
        self.home_page.navigate(f"{Config.BASE_URL}/contact_us")

    def test_submit_valid_form(self, page):
        """Test Case 1: Submit contact form with valid data"""
        page.fill("input[data-qa='name']", "QA Tester")
        page.fill("input[data-qa='email']", "testqa@example.com")
        page.fill("input[data-qa='subject']", "Test Automation Inquiry")
        page.fill("textarea[data-qa='message']", "This is an automated test message.")
        
        # Handle file upload mock if required, though optional in this form
        
        # Accept JS conform alert automatically
        page.on("dialog", lambda dialog: dialog.accept())
        page.click("input[data-qa='submit-button']")
        
        assert "Success! Your details have been submitted successfully." in page.locator(".status").inner_text()

    def test_submit_missing_fields(self, page):
        """Test Case 2: Submit with missing required details"""
        page.fill("input[data-qa='name']", "QA Tester")
        # Missing Email
        page.fill("input[data-qa='subject']", "Test Automation Inquiry")
        page.click("input[data-qa='submit-button']")
        
        # Assert HTML5 validation blocks submission
        is_required = page.evaluate("document.querySelector('input[data-qa=\"email\"]').validationMessage !== ''")
        assert is_required

    def test_verify_confirmation_message(self, page):
        """Test Case 3: Verify success message UI presentation"""
        self.test_submit_valid_form(page)
        # Extra explicit check for the alert-success banner presence
        assert page.locator(".alert-success").is_visible()
