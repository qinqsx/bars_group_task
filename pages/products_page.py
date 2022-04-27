from .base_page import BasePage
from .locators import ProductsPageLocators

class ProductsPage(BasePage):

    def should_be_products_page(self):
        assert self.element_text(*ProductsPageLocators.HEADER_LINK).lower() == "products", "Current page is not products page"

    def add_product_to_cart(self, product_add_button):
        self.browser.find_element(*product_add_button).click()

    def add_to_cart_product_button_became_remove(self, product_remove_button):
        assert self.element_text(*product_remove_button).lower() == "remove", "Button is not 'remove' yet"

    def go_to_cart_page_from_product_page(self):
        self.browser.find_element(*ProductsPageLocators.CART_LINK).click()