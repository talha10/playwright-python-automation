from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    """Page Object for the Main Storefront Page."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.home_menu_link = "a[href='/']"
        self.products_menu_link = "a[href='/products']"
        self.cart_menu_link = "a[href='/view_cart']"
        self.login_menu_link = "a[href='/login']"
        self.contact_menu_link = "a[href='/contact_us']"
        self.logout_menu_link = "a[href='/logout']"
        
        self.search_input = "#search_product"
        self.submit_search = "#submit_search"
        self.features_items_container = ".features_items"

    def click_login_signup_menu(self):
        self.click(self.login_menu_link)
        
    def click_cart_menu(self):
        self.click(self.cart_menu_link)

    def is_user_logged_in(self) -> bool:
        return self.is_visible(self.logout_menu_link)

    def search_for_product(self, product_name: str):
        self.fill(self.search_input, product_name)
        self.click(self.submit_search)
        self.wait_for_element(self.features_items_container)
