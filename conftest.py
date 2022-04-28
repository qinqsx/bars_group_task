import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""Функция для изменения языка через cmd"""


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Choose browser language, for exmpl: ru")


"""Функция для назначения условий запуска и закрытия браузера при проведении теста"""


@pytest.fixture(scope="class")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
