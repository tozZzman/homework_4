import os
import sys

sys.path.append(os.path.normpath(os.path.join(
    os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))), '..')))

import pytest
from selenium import webdriver
from etc.helper import MethodsHelpers


def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     help='Browser selection flag',
                     choices=['chrome', 'firefox', 'opera'],
                     default='chrome')
    parser.addoption('--url',
                     action='store',
                     help='Flag for selecting url',
                     default='https://demo.opencart.com/')


@pytest.fixture(scope='function')
def browser(request):
    br = request.config.getoption('--browser')

    if br == 'chrome':
        driver = webdriver.Chrome()
    elif br == 'firefox':
        driver = webdriver.Firefox()
    elif br == 'opera':
        driver = webdriver.Opera()
    else:
        raise ValueError(f"Driver not suported: {br}")

    request.addfinalizer(driver.quit)

    return driver


@pytest.fixture(scope='function')
def url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='function')
def helper(browser):
    return MethodsHelpers(browser)
