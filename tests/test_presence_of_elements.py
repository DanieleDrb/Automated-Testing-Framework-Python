
import allure
import pytest
from selenium import webdriver
from pages.registration_page import RegistrationPage


@pytest.fixture(scope="function")
def setup_teardown():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def registration_page(setup_teardown):
    def _registration_page():
        return RegistrationPage(setup_teardown)
    yield _registration_page()


@allure.title("Test Presence Of Main Heading Validation: ")
def test_presence_of_main_heading(registration_page):

    with allure.step("Open Registration Page And Get Text Of Main Heading"):
        registration_page.open()
        actual_main_heading = registration_page.main_heading().text

    with allure.step("Verify The Main Heading"):
        assert "Register" in actual_main_heading
        allure.attach(f"Actual Login Page Link : {actual_main_heading}", name="Register Account")
        print(f" The Main Heading {actual_main_heading} is present")


@allure.title("Test Presence Of Login Page Link")
def test_presence_of_login_page_link(registration_page):

    with allure.step("Open Registration Page And Get Text Of Login Page Link"):
        registration_page.open()
        actual_login_page_link = registration_page.login_page_link().text

    with allure.step("Verify The Login Page Link"):
        assert actual_login_page_link == "login page"
        allure.attach(f"Actual Login Page Link : {actual_login_page_link}", name="Login Page Link")
        print(f" The Login Page Link {actual_login_page_link} is present")


@allure.title("Test Presence Of First Name Label")
def test_presence_of_first_name(registration_page):

    with allure.step("Open Registration Page And Get Text Of First Name Label"):
        registration_page.open()
        actual_first_name_label = registration_page.first_name_label().text

    with allure.step("Verify The First Name Label"):
        assert actual_first_name_label == "First Name"
        allure.attach(f"Actual Login Page Link : {actual_first_name_label}", name="First Name")
        print(f" The First Name Label {actual_first_name_label} is present")


@allure.title("Test Presence Of Last Name Label")
def test_presence_of_last_name(registration_page):

    with allure.step("Open Registration Page And Get Text Of Last Name Label"):
        registration_page.open()
        actual_last_name = registration_page.last_name_label().text

    with allure.step("Verify The Last Name Label"):
        assert actual_last_name == "Last Name"
        allure.attach(f"Actual Login Page Link : {actual_last_name}", name="Last Name")
        print(f" The Last Name Label {actual_last_name} is present")


@allure.title("Test Presence Of Email Label")
def test_presence_of_email(registration_page):

    with allure.step("Open Registration Page And Get Text Of Email Label"):
        registration_page.open()
        actual_email = registration_page.email_label().text

    with allure.step("Verify The Email Label"):
        assert actual_email == "E-mail"
        allure.attach(f"Actual Login Page Link : {actual_email}", name="E-mail")
        print(f" The Email Label {actual_email} is present")


@allure.title("Test Presence Of Phone Number Label")
def test_presence_of_phone_number(registration_page):

    with allure.step("Open Registration Page And Get Text Of Phone Number Label"):
        registration_page.open()
        actual_phone_number = registration_page.telephone_label().text

    with allure.step("Verify The Phone Number Label"):
        assert actual_phone_number == "Telephone"
        allure.attach(f"Actual Login Page Link : {actual_phone_number}", name="Email")
        print(f" The Phone Number Label {actual_phone_number} is present")


@allure.title("Test Presence Of Password Label")
def test_presence_of_password(registration_page):

    with allure.step("Open Registration Page And Get Text Of Password Label"):
        registration_page.open()
        actual_password = registration_page.password_label().text

    with allure.step("Verify The Paswword Label"):
        assert actual_password == "Password"
        allure.attach(f"Actual Password : {actual_password}", name="Password")
        print(f" The Password Label {actual_password} is present")


@allure.title("Test Presence Of Password Confirm Label")
def test_presence_of_password_confirm(registration_page):
    with allure.step("Open Registration Page And Get Text Of Password Confirm Label"):
        registration_page.open()
        actual_password_confirm = registration_page.password_confirm_label().text
    with allure.step("Verify The Password Confirm Label"):
        assert actual_password_confirm == "Password Confirm"
        allure.attach(f"Actual Password Confirm Label : {actual_password_confirm}", name="Password Confirm")
        print(f" The Password Confirm Label {actual_password_confirm} is present")


@allure.title("Test Presence Of Subscribe Label")
def test_presence_of_subscribe(registration_page):
    with allure.step("Open Registration Page And Get Text Of Subscribe Label"):
        registration_page.open()
        actual_subscribe= registration_page.subscribe_label().text
    with allure.step("Verify The Subscribe Label"):
        assert actual_subscribe == "Subscribe"
        allure.attach(f"Actual Subscribe Label : {actual_subscribe}", name="Subscribe")
        print(f" The Subscribe Label {actual_subscribe} is present")


@allure.title("Test Presence Of Privacy Policy Popup")
def test_presence_of_privacy_policy(registration_page):
    with allure.step("Open Registration Page And Get Text Of Privacy Policy Popup"):
        registration_page.open()
        registration_page.open_privacy_policy()
        actual_header_privacy_policy_popup = registration_page.privacy_policy_popup()
    with allure.step("Verify The Privacy Policy Popup"):
        assert actual_header_privacy_policy_popup == "Privacy Policy"
        allure.attach(f"Actual Privacy Policy Popup : {actual_header_privacy_policy_popup}", name="Privacy Popup")
        print(f" The Privacy Policy Popup Window {actual_header_privacy_policy_popup} is present")


@allure.title("Test Presence Of Placeholder")
def test_presence_of_placeholder(registration_page):
    with allure.step("Open Registration Page And Get Text Of Placeholder"):
        registration_page.open()
        actual_element_first_name = registration_page.element_first_name()
    with allure.step("Verify The Phone Number Label"):
        registration_page.assert_placeholder("First Name", actual_element_first_name)
        allure.attach(f"Actual Placeholder First Name : {actual_element_first_name}", name="First Name Placeholder")

