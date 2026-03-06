from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductPage(BasePage):
    """Page Object for the Product Detail and Listing Pages."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.product_name_header = ".product-information h2"
        self.product_price = ".product-information span span"
        self.quantity_input = "#quantity"
        self.add_to_cart_btn = "button.cart"
        self.continue_shopping_btn = "button[data-dismiss='modal']"
        self.view_cart_modal_link = ".modal-body a[href='/view_cart']"

    def get_product_name(self) -> str:
        self.wait_for_element(self.product_name_header)
        return self.page.locator(self.product_name_header).inner_text()

    def get_price(self) -> str:
        return self.page.locator(self.product_price).inner_text()

    def set_quantity(self, quantity: str):
        self.page.locator(self.quantity_input).fill(quantity)

    def add_to_cart(self):
        self.click(self.add_to_cart_btn)
        self.wait_for_element(self.continue_shopping_btn)

    def proceed_to_cart_from_modal(self):
        self.click(self.view_cart_modal_link)
