import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import Url


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = webdriver
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(Url.STELLAR_BURGER)
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.get(Url.STELLAR_BURGER)
    yield driver
    driver.quit()