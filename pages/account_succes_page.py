from selenium.webdriver.common.by import By
from selenium import webdriver


class AccountSuccessPage:

    def __init__(self, driver):
        self.driver = driver

    def main_heading(self):
        return self.driver.find_element(By.TAG_NAME, "h1")

    def account_created(self):
        return self.main_heading().text.strip()

    def assert_account_created_successfully(self):
        assert self.account_created() == "Your Account Has Been Created!"
