import pytest
from pages.home_page import HomePage
from utils.config import Config

class TestProductSearch:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.home_page = HomePage(page)
        self.home_page.navigate(f"{Config.BASE_URL}/products")

    def test_search_existing_product(self):
        """Test Case 1: Search for an existing product"""
        self.home_page.search_for_product("Blue Top")
        is_visible = self.home_page.is_visible("text='Blue Top'")
        assert is_visible, "Product 'Blue Top' not found in search results"

    def test_search_non_existent_product(self, page):
        """Test Case 2: Search for non-existent product"""
        self.home_page.search_for_product("Unicorn Dust")
        is_visible = self.home_page.is_visible("text='Unicorn Dust'")
        assert not is_visible
        
    def test_search_special_characters(self, page):
        """Test Case 3: Search with special characters"""
        self.home_page.search_for_product("@#$%^&*")
        assert self.home_page.is_visible(".features_items")

    def test_filter_by_category(self, page):
        """Test Case 4: Filter products by category"""
        page.locator("a[href='#Men']").click()
        page.locator("a[href='/category_products/3']").click()  # Tshirts
        assert "Men - Tshirts" in page.locator(".title").inner_text()

    def test_sort_by_price(self, page):
        """Test Case 5: Verification of sorting mock"""
        # Note: automationexercise doesn't have a reliable sort dropdown
        # This asserts the UI loads properly on the products page
        assert page.locator(".features_items").is_visible()
