from playwright.sync_api import Page
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page Object for the Shopping Cart."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items = "#cart_info_table tbody tr"
        self.checkout_btn = ".check_out"
        self.empty_cart_msg = "#empty_cart p.text-center b"
        self.total_amount = ".cart_total_price"

    def get_items(self) -> list:
        self.wait_for_element(self.cart_items)
        return self.page.locator(self.cart_items).all()

    def update_quantity(self, item_index: int, quantity: str):
        qty_input = self.page.locator(f"{self.cart_items}:nth-child({item_index + 1}) .cart_quantity_button input")
        qty_input.fill(quantity)
        
    def remove_item(self, item_index: int):
        remove_btn = self.page.locator(f"{self.cart_items}:nth-child({item_index + 1}) .cart_quantity_delete")
        remove_btn.click()

    def get_total(self) -> str:
        self.wait_for_element(self.total_amount)
        return self.page.locator(self.total_amount).inner_text()
        
    def proceed_to_checkout(self):
        self.click(self.checkout_btn)
