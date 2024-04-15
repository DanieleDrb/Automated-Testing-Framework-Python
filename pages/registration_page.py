from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

    def main_heading(self):
        return self.driver.find_element(By.TAG_NAME, "h1")

    def error_summary(self):
        return self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")

    def login_page_link(self):
        return self.driver.find_element(By.XPATH, "//a[normalize-space()='login page']")

    def first_name_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#input-firstname")

    def first_name_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='input-firstname']")

    def first_name_error(self):
        return (self.driver.find_element
                (By.XPATH,
                    "//div[contains(text(),'First Name must be between 1 and 32 characters!')]").text)

    def last_name_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#input-lastname")

    def last_name_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='input-lastname']")

    def last_name_error(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]").text

    def email_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#input-email")

    def email_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='input-email']")

    def email_error(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(text(),'E-Mail Address does not appear to be valid!')]").text

    def telephone_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#input-telephone")

    def telephone_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='input-telephone']")

    def telephone_error(self):
        return (self.driver.find_element
                (By.XPATH,
                    "//div[normalize-space()='Telephone must be between 3 and 32 characters!']").text)

    def password_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#input-password")

    def password_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='input-password']")

    def password_error(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(text(),'Password must be between 4 and 20 characters!')]").text

    def password_confirm_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#input-confirm")

    def password_confirm_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='input-confirm']")

    def password_confirm_error(self):
        return self.driver.find_element(By.XPATH, "//div[@class='text-danger']").text

    def newsletter_subscribe_yes(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='input-newsletter-yes']")

    def newsletter_subscribe_no(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='input-newsletter-no']")

    def privacy_policy_error(self):
        return self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text

    def subscribe_label(self):
        return self.driver.find_element(By.XPATH, "//label[normalize-space()='Subscribe']")

    def privacy_policy_box(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='input-agree']")

    def privacy_policy_link(self):
        return self.driver.find_element(By.TAG_NAME, "b")

    def open_privacy_policy(self):
        self.privacy_policy_link().click()

    def continue_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[value='Continue']")

    def get_error_message(self, input_label):
        error_message_locator = f"//label[text()='{input_label}']//following-sibling::div/div"
        return self.driver.find_element(By.XPATH, error_message_locator).text

    def assert_first_name_validation(self):
        actual_error = self.get_error_message("First Name")
        assert actual_error == "First Name must be between 1 and 32 characters!"

    def assert_last_name_validation(self):
        actual_error = self.get_error_message("Last Name")
        assert actual_error == "Last Name must be between 1 and 32 characters!"

    def assert_email_validation(self):
        actual_error = self.get_error_message("E-Mail")
        assert actual_error == "E-Mail Address does not appear to be valid!"

    def assert_telephone_validation(self):
        actual_error = self.get_error_message("Telephone")
        assert actual_error == "Telephone must be between 3 and 32 characters!"

    def assert_password_validation(self):
        actual_error = self.get_error_message("Password")
        assert actual_error == "Password must be between 4 and 20 characters!"

    def assert_password_confirm_validation(self):
        actual_error = self.get_error_message("Password Confirm")
        assert actual_error == "Password confirmation does not match password!"

    def assert_privacy_policy_agreement_validation(self):
        assert self.error_summary().text == "Warning: You must agree to the Privacy Policy!"

    def get_placeholder(self, element):
        return element.get_attribute("placeholder")

    def assert_placeholder(self, expected_text, element):
        actual_placeholder = self.get_placeholder(element)
        assert actual_placeholder == expected_text

    def element_first_name(self):
        return self.driver.find_element(By.ID, "input-firstname")

    def privacy_policy_popup(self):
        return self.driver.find_element(By.TAG_NAME, "h4").text

    def register(self, user, use_enter):
        if user.get_first_name() != "":
            self.first_name_input().send_keys(user.get_first_name())

        if user.get_last_name() != "":
            self.last_name_input().send_keys(user.get_last_name())

        if user.get_email() != "":
            self.email_input().send_keys(user.get_email())

        if user.get_phone_number() != "":
            self.telephone_input().send_keys(user.get_phone_number())

        if user.get_password() != "":
            self.password_input().send_keys(user.get_password())

        if user.get_password_confirm() != "":
            self.password_confirm_input().send_keys(user.get_password_confirm())

        if user.get_subscribe():
            if not self.newsletter_subscribe_yes().is_selected():
                self.newsletter_subscribe_yes().click()
            elif not self.newsletter_subscribe_no().is_selected():
                self.newsletter_subscribe_no().click()

        if user.get_privacy_policy():
            self.privacy_policy_box().click()

        if use_enter:
            self.continue_button().send_keys(Keys.ENTER)
        else:
            self.continue_button().click()








