from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MethodsHelpers:
    def __init__(self, browser):
        self.browser = browser

    def check_title(self, title, timeout):
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.title_is(title=title))
        except TimeoutException:
            raise TimeoutError("Не дождались заголовка страницы")

    def is_element_present(self, how, what, timeout=1):
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutError(f"Элемент не был найден в течение {timeout} секунд(-ы)")

    def is_text_present(self, how, what, text, timeout=1):
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            raise TimeoutError(f"Текст не был найден в течение {timeout} секунд(-ы)")
