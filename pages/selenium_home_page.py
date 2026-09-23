from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumHomePage:
    URL = "https://www.selenium.dev/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def get_page_title(self):
        return self.driver.title

    def click_documentation(self):
        documentation_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Documentation")
            )
        )
        documentation_link.click()
