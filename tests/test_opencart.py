from etc.locators import PagePaths, PageLocators
import pytest


def test_search_title(browser, url, helper):
    browser.get(url)
    helper.check_title(title='Your Store', timeout=3)


@pytest.mark.parametrize('url, locator', ((PagePaths.MAIN, PageLocators.ADD_BASKET),
                                          (PagePaths.PRODUCT, PageLocators.INPUT_QUALITY),
                                          (PagePaths.CATALOG, PageLocators.LIST_VIEW),
                                          (PagePaths.LOGIN, PageLocators.BUTTON_LOGIN),
                                          (PagePaths.LOGIN_ADMIN, PageLocators.PASSWORD_ADMIN)))
def test_search_items_on_the_pages(browser, helper, url, locator):
    browser.get(url)
    helper.is_element_present(*locator, timeout=2)
