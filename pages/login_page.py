from .base_page import BasePage
from .locators import LoginPageLocators

"""методы для login_page"""


class LoginPage(BasePage):

    def log_in_user(self, name, password):
        self.send_text(*LoginPageLocators.USERNAME_FORM_LINK, name)
        self.send_text(*LoginPageLocators.PASSWORD_FORM_LINK, password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_LINK).click()
