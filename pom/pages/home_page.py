from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pom.pages.base_page import BasePage


class HomePage(BasePage):
    username = (By.ID, "user-name")
    password = (By.NAME, "password")
    button = (By.ID, "login-button")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def load_page(self):
        self.driver.get('https://www.saucedemo.com/')

    def login(self, username_text, password_text):
        self.do_send_keys(self.username, username_text)
        self.do_send_keys(self.password, password_text)
        self.do_click(self.button)
