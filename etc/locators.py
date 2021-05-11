from selenium.webdriver.common.by import By


class PagePaths:
    MAIN = 'https://demo.opencart.com/'
    PRODUCT = 'https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49'
    CATALOG = 'https://demo.opencart.com/index.php?route=product/category&path=20'
    LOGIN = 'https://demo.opencart.com/index.php?route=account/login'
    LOGIN_ADMIN = 'https://demo.opencart.com/admin/'


class HomePageLocators:
    ADD_TO_BASKET = (By.XPATH, '''//button[@onclick="cart.add('43');"]''')
    ADD_TO_WISHLIST = (By.XPATH, '''//button[@onclick="wishlist.add('43');"]''')
    COMPARE = (By.XPATH, '''//button[@onclick="compare.add('43');"]''')
    PRICE = (By.CSS_SELECTOR, 'div.product-layout:nth-child(1) .price')
    PRICE_TAX = (By.CSS_SELECTOR, 'div.product-layout:nth-child(1) .price-tax')


class ProductPageLocators:
    INPUT_QUALITY = (By.ID, 'input-quantity')
    ADD_TO_CART = (By.CSS_SELECTOR, 'button#button-cart')
    BACK_TO_HOME = (By.CSS_SELECTOR, '.fa.fa-home')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content div.col-sm-4 h1')
    PRICE = (By.CSS_SELECTOR, '#content div.col-sm-4 ul li h2')


class CatalogPageLocators:
    LIST_VIEW = (By.ID, 'list-view')
    GRID_VIEW = (By.ID, 'grid-view')
    COMPARE_TOTAL = (By.ID, 'compare-total')
    SORT_BY = (By.XPATH, '//select[@id="input-sort"]/option[@selected="selected"]')
    SHOW = (By.XPATH, '//select[@id="input-limit"]/option[@selected="selected"]')


class LoginPageLocators:
    BUTTON_LOGIN = (By.XPATH, '//input[@value="Login"]')
    BUTTON_CONTINIUE = (By.CSS_SELECTOR, "#content .row div.col-sm-6:nth-child(1) a")
    EMAIL = (By.ID, 'input-email')
    PASSWORD = (By.ID, 'input-password')
    NAME_FORM = (By.CSS_SELECTOR, "#content .row div.col-sm-6:nth-child(2) h2")


class LoginAdminPageLocators:
    LOGIN_ADMIN = (By.ID, 'input-username')
    PASSWORD_ADMIN = (By.ID, 'input-password')
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, '.help-block')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '.btn.btn-primary')
    NAME_FORM = (By.CSS_SELECTOR, '.panel-heading')