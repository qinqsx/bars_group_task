from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def autorise_user(self, name, password):
        self.send_text(*LoginPageLocators.USERNAME_FORM_LINK, name)
        self.send_text(*LoginPageLocators.PASSWORD_FORM_LINK, password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_LINK).click()
