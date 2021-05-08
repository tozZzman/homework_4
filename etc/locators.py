from selenium.webdriver.common.by import By


class PagePaths:
    MAIN = 'https://demo.opencart.com/'
    PRODUCT = 'https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49'
    CATALOG = 'https://demo.opencart.com/index.php?route=product/category&path=20'
    LOGIN = 'https://demo.opencart.com/index.php?route=account/login'
    LOGIN_ADMIN = 'https://demo.opencart.com/admin/'


class PageLocators:
    ADD_BASKET = (By.XPATH, '''//button[@onclick="cart.add('40');"]''')
    INPUT_QUALITY = (By.ID, 'input-quantity')
    LIST_VIEW = (By.ID, 'list-view')
    BUTTON_LOGIN = (By.XPATH, '//input[@value="Login"]')
    PASSWORD_ADMIN = (By.ID, 'input-password')
