from .base_page import BasePage
from .locators import ProductsPageLocators
from selenium.webdriver.support.ui import Select

"""методы для product_page"""


class ProductsPage(BasePage):

    def should_be_products_page(self):
        assert self.element_text(
            *ProductsPageLocators.HEADER_LINK).lower() == "products", "Current page is not products page"

    def add_product_to_cart(self, product_add_button):
        self.browser.find_element(*product_add_button).click()

    def add_to_cart_product_button_became_remove(self, product_remove_button):
        assert self.element_text(
            *product_remove_button).lower() == "remove", "Button is not 'remove' yet"

    def go_to_cart_page_from_product_page(self):
        self.browser.find_element(*ProductsPageLocators.CART_LINK).click()

    def product_price_list_type_float(self):
        return [float(i[1:]) for i in self.elements_text_list(*ProductsPageLocators.PRODUCTS_PRICE_LINK)]

    def select_product_sort_by_index(self, index):
        select = Select(self.browser.find_element(
            *ProductsPageLocators.PRODUCT_SORT_LINK))
        select.select_by_index(index)

    def comparison_low_to_high(self, manual_sort, after_web_sort):
        assert sorted(
            manual_sort) == after_web_sort, "Low to high sort does not work"
