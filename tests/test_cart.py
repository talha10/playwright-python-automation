import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config import Config

class TestCart:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.home_page = HomePage(page)
        self.product_page = ProductPage(page)
        self.cart_page = CartPage(page)
        self.home_page.navigate(f"{Config.BASE_URL}/products")

    def test_add_single_item(self):
        """Test Case 1: Add a single item to cart"""
        self.page.locator("a[href='/product_details/1']").click()
        self.product_page.add_to_cart()
        self.product_page.proceed_to_cart_from_modal()
        assert len(self.cart_page.get_items()) == 1

    def test_add_multiple_items(self):
        """Test Case 2: Add multiple items to cart"""
        self.page.locator(".add-to-cart").first.click()
        self.product_page.page.locator("button[data-dismiss='modal']").click()
        self.page.locator(".add-to-cart").nth(2).click()
        self.product_page.proceed_to_cart_from_modal()
        assert len(self.cart_page.get_items()) == 2

    def test_update_quantity(self):
        """Test Case 3: Update item quantity in cart"""
        self.page.locator("a[href='/product_details/1']").click()
        self.product_page.set_quantity("3")
        self.product_page.add_to_cart()
        self.product_page.proceed_to_cart_from_modal()
        qty = self.page.locator(".cart_quantity button").first.inner_text()
        assert qty == "3"

    def test_remove_item(self):
        """Test Case 4: Remove item from cart"""
        self.test_add_single_item()
        self.cart_page.remove_item(0)
        assert self.cart_page.is_visible(self.cart_page.empty_cart_msg)

    def test_cart_persists_after_refresh(self, page):
        """Test Case 5: Cart retains items after page refresh"""
        self.test_add_single_item()
        page.reload()
        assert len(self.cart_page.get_items()) == 1

    def test_empty_cart_state(self):
        """Test Case 6: Empty cart validation"""
        self.cart_page.navigate(f"{Config.BASE_URL}/view_cart")
        assert self.cart_page.is_visible(self.cart_page.empty_cart_msg)
