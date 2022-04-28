

"""Инициализация браузера, базовые методы для удобства читаемости и облегчения написания и корректировки кода"""


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def element_text(self, how, what):
        return self.browser.find_element(how, what).text

    def elements_text_list(self, how, what):
        return [i.text for i in self.browser.find_elements(how, what)]            #метод для создания списка текста содержащегося в выбранных элементах

    def send_text(self, how, what, text):
        text_area = self.browser.find_element(how, what)
        text_area.send_keys(text)




