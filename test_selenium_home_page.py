import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.selenium_home_page import SeleniumHomePage


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=chrome_options)

    yield browser

    time.sleep(5)
    browser.quit()


def test_selenium_home_page_title(driver):
    home_page = SeleniumHomePage(driver)

    home_page.open()

    assert "Selenium" in home_page.get_page_title()


def test_documentation_link(driver):
    home_page = SeleniumHomePage(driver)

    home_page.open()
    home_page.click_documentation()

    assert "documentation" in driver.current_url.lower()