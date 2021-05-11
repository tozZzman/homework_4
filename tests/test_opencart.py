import etc.locators as lc


def test_search_title(browser, url, helper):
    browser.get(url)
    helper.check_title(title='Your Store', timeout=3)


def test_search_items_on_the_home_page(browser, helper, url):
    browser.get(lc.PagePaths.MAIN)
    helper.is_element_present(*lc.HomePageLocators.ADD_TO_BASKET)
    helper.is_element_present(*lc.HomePageLocators.ADD_TO_WISHLIST)
    helper.is_element_present(*lc.HomePageLocators.COMPARE)
    helper.is_text_present(*lc.HomePageLocators.PRICE, text='$602.00')
    helper.is_text_present(*lc.HomePageLocators.PRICE_TAX, text='Ex Tax: $500.00')


def test_search_items_on_the_product_page(browser, helper, url):
    browser.get(lc.PagePaths.PRODUCT)
    helper.is_element_present(*lc.ProductPageLocators.INPUT_QUALITY)
    helper.is_element_present(*lc.ProductPageLocators.ADD_TO_CART)
    helper.is_element_present(*lc.ProductPageLocators.BACK_TO_HOME)
    helper.is_text_present(*lc.ProductPageLocators.PRODUCT_NAME, text='Samsung Galaxy Tab 10.1')
    helper.is_text_present(*lc.ProductPageLocators.PRICE, text='$241.99')


def test_search_items_on_the_catalog_page(browser, helper, url):
    browser.get(lc.PagePaths.CATALOG)
    helper.is_element_present(*lc.CatalogPageLocators.LIST_VIEW)
    helper.is_element_present(*lc.CatalogPageLocators.GRID_VIEW)
    helper.is_element_present(*lc.CatalogPageLocators.COMPARE_TOTAL)
    helper.is_text_present(*lc.CatalogPageLocators.SORT_BY, text='Default')
    helper.is_text_present(*lc.CatalogPageLocators.SHOW, text='15')


def test_search_items_on_the_login_page(browser, helper, url):
    browser.get(lc.PagePaths.LOGIN)
    helper.is_element_present(*lc.LoginPageLocators.BUTTON_LOGIN)
    helper.is_element_present(*lc.LoginPageLocators.BUTTON_CONTINIUE)
    helper.is_element_present(*lc.LoginPageLocators.EMAIL)
    helper.is_element_present(*lc.LoginPageLocators.PASSWORD)
    helper.is_text_present(*lc.LoginPageLocators.NAME_FORM, text='Returning Customer')


def test_search_items_on_the_login_admin_page(browser, helper, url):
    browser.get(lc.PagePaths.LOGIN_ADMIN)
    helper.is_element_present(*lc.LoginAdminPageLocators.LOGIN_ADMIN)
    helper.is_element_present(*lc.LoginAdminPageLocators.PASSWORD_ADMIN)
    helper.is_element_present(*lc.LoginAdminPageLocators.FORGOTTEN_PASSWORD)
    helper.is_element_present(*lc.LoginAdminPageLocators.BUTTON_LOGIN)
    helper.is_text_present(*lc.LoginAdminPageLocators.NAME_FORM, text='Please enter your login details.')