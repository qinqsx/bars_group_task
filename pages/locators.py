from selenium.webdriver.common.by import By


"""Классы с локаторами для страниц и ссылки на них, для улучшения читаемости кода, так же в случае изменения селектора или ссылки на тот или иной объект упрощает корректировку"""

class LoginPageLocators:
    USER_NAME = "performance_glitch_user"
    USER_PASS = "secret_sauce"
    URL = "https://www.saucedemo.com/"

    USERNAME_FORM_LINK = (By.NAME, "user-name")
    PASSWORD_FORM_LINK = (By.NAME, "password")
    LOGIN_BUTTON_LINK = (By.NAME, "login-button")

class ProductsPageLocators:
    HEADER_LINK = (By.CLASS_NAME, "title")
    SAUCE_LABS_FLEECE_JACKET_ADD_BUTTON_LINK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")
    SAUCE_LABS_FLEECE_JACKET_REMOVE_BUTTON_LINK = (By.CSS_SELECTOR, "#remove-sauce-labs-fleece-jacket")
    SAUCE_LABS_BOLT_T_SHIRT_ADD_BUTTON_LINK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    SAUCE_LABS_BOLT_T_SHIRT_REMOVE_BUTTON_LINK = (By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    PRODUCTS_PRICE_LINK = (By.CSS_SELECTOR, ".inventory_item_price")
    PRODUCT_SORT_LINK = (By.TAG_NAME, "select")

class CartPageLocators:
    INVENTORY_ITEM_NAME_LINK = (By.CSS_SELECTOR, ".inventory_item_name")
    INVENTORY_SECOND_ITEM_NAME_LINK= (By.CSS_SELECTOR, "#item_1_title_link .inventory_item_name")
    CONTINUE_SHOPPING_BUTTON_LINK = (By.ID, "continue-shopping")