from .base_page import BasePage
from .locators import CartPageLocators

"""методы для cart_page"""

class CartPage(BasePage):

    def should_be_fleece_jacket_in_cart(self):
        assert self.element_text(*CartPageLocators.INVENTORY_ITEM_NAME_LINK).lower() == "Sauce Labs Fleece Jacket".lower(), "There is no fleece jacket in cart"

    def should_be_bolt_t_shirt_in_cart(self):
        assert self.element_text(*CartPageLocators.INVENTORY_SECOND_ITEM_NAME_LINK).lower() == "Sauce Labs Bolt t-shirt".lower(), "There is no Bolt t-shirt in cart"

    def back_to_continue_shopping_from_cart_page(self):
        self.browser.find_element(*CartPageLocators.CONTINUE_SHOPPING_BUTTON_LINK).click()


