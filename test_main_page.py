from .pages.login_page import LoginPage
from .pages.products_page import ProductsPage
from .pages.locators import LoginPageLocators
from .pages.locators import ProductsPageLocators
from .pages.cart_page import CartPage

"""Задание 1"""


class TestAddingProductsToCart:
    def test_log_in_user_with_open_products_page(self, browser):
        link = LoginPageLocators.URL
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.log_in_user(LoginPageLocators.USER_NAME,
                               LoginPageLocators.USER_PASS)
        product_page = ProductsPage(browser, browser.current_url)
        product_page.should_be_products_page()
        print("1. Авторизация, открытие главной страницы")

    def test_added_fleece_jacket_to_cart_with_changed_to_remove_button(self, browser):
        product_page = ProductsPage(browser, browser.current_url)
        product_page.add_product_to_cart(
            ProductsPageLocators.SAUCE_LABS_FLEECE_JACKET_ADD_BUTTON_LINK)
        product_page.add_to_cart_product_button_became_remove(
            ProductsPageLocators.SAUCE_LABS_FLEECE_JACKET_REMOVE_BUTTON_LINK)
        print("2. Добавление товара Sauce Labs Fleece Jacket в корзину")

    def test_go_to_cart_page_with_fleece_jacket_product(self, browser):
        product_page = ProductsPage(browser, browser.current_url)
        product_page.go_to_cart_page_from_product_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_fleece_jacket_in_cart()
        print("3. Переход в корзину")

    def test_back_to_products_page_from_cart(self, browser):
        cart_page = CartPage(browser, browser.current_url)
        cart_page.back_to_continue_shopping_from_cart_page()
        product_page = ProductsPage(browser, browser.current_url)
        product_page.should_be_products_page()
        print("4. Нажатие кнопки CONTINUE SHOPPING")

    def test_added_bolt_t_shirt_to_cart_with_changed_to_remove_button(self, browser):
        product_page = ProductsPage(browser, browser.current_url)
        product_page.add_product_to_cart(
            ProductsPageLocators.SAUCE_LABS_BOLT_T_SHIRT_ADD_BUTTON_LINK)
        product_page.add_to_cart_product_button_became_remove(
            ProductsPageLocators.SAUCE_LABS_BOLT_T_SHIRT_REMOVE_BUTTON_LINK)
        print("5. Добавление товар Sauce Labs Bolt T-Shirt в корзину")

    def test_go_to_cart_page_with_fleece_jacket_and_bolt_t_shirt_products(self, browser):
        product_page = ProductsPage(browser, browser.current_url)
        product_page.go_to_cart_page_from_product_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_fleece_jacket_in_cart()
        cart_page.should_be_bolt_t_shirt_in_cart()
        print("6. Переход в корзину")


"""Задание 2"""


class TestSortingProducts:
    def test_log_in_user_with_open_products_page(self, browser):
        link = LoginPageLocators.URL
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.log_in_user(LoginPageLocators.USER_NAME,
                               LoginPageLocators.USER_PASS)
        product_page = ProductsPage(browser, browser.current_url)
        product_page.should_be_products_page()
        print("1. Авторизация, открытие главной страницы")

    def test_sorting_products_price_low_to_high(self, browser):
        product_page = ProductsPage(browser, browser.current_url)
        # создаю переменную в которой хранится список цен до сортировки
        before_sort_price_list = product_page.product_price_list_type_float()
        product_page.select_product_sort_by_index(2)
        # создаю переменную в которой хранится список цен после сортировки
        after_sort_price_list = product_page.product_price_list_type_float()
        # сравниваю отсортированную первую переменную со второй перменной отсортированной на сайте
        product_page.comparison_low_to_high(
            before_sort_price_list, after_sort_price_list)
        print("2. Сортировка товара по возрастанию цены")
