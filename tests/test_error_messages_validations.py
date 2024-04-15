
import allure
import pytest
from selenium import webdriver
from pages.registration_page import RegistrationPage
from utilities.user_factory import UserFactory
from utilities.utility import (generate_random_name, generate_random_not_valid_email,
                               generate_random_phone_number, generate_random_password)


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


@allure.title("Test Error First Name Validation: {first_name}")
@pytest.mark.parametrize("first_name", [generate_random_name(0), generate_random_name(33)])
def test_error_first_name_validation_0_and_33_characters(first_name, registration_page):

    user = UserFactory().create_default()
    user.set_first_name(first_name)

    with allure.step("Performing registration with invalid first name"):
        registration_page.open()
        registration_page.register(user, False)

    with allure.step("Verifying first name validation"):
        registration_page.assert_first_name_validation()
        print(registration_page.first_name_error())


@allure.title("Test Error Last Name Validation: {last_name}")
@pytest.mark.parametrize("last_name", [generate_random_name(0), generate_random_name(33)])
def test_error_last_name_validation_0_and_33_characters(last_name, registration_page):

    user = UserFactory().create_default()
    user.set_last_name(last_name)

    with allure.step("Performing registration with invalid last name"):
        registration_page.open()
        registration_page.register(user, False)

    with allure.step("Verifying last name validation"):
        registration_page.assert_last_name_validation()
        print(registration_page.last_name_error())


@allure.title("Test Error Email Validation: {not_valid_email}")
@pytest.mark.parametrize("not_valid_email", [generate_random_not_valid_email(4), generate_random_not_valid_email(32)])
def test_error_email_validation(not_valid_email, registration_page):

    user = UserFactory().create_default()
    user.set_email(not_valid_email)

    with allure.step("Performing registration with invalid email"):
        registration_page.open()
        registration_page.register(user, False)

    with allure.step("Verifying email validation"):
        registration_page.assert_email_validation()
        print(registration_page.email_error())


@allure.title("Test Error Phone Number Validation: {phone_number}")
@pytest.mark.parametrize("phone_number", [generate_random_phone_number(2), generate_random_phone_number(33)])
def test_error_phone_validation_2_and_33_numbers(phone_number, registration_page):

    user = UserFactory().create_default()
    user.set_phone_number(phone_number)

    with allure.step("Performing registration with invalid phone number"):
        registration_page.open()
        registration_page.register(user, False)

    with allure.step("Verifying phone number validation"):
        registration_page.assert_telephone_validation()
        print(registration_page.telephone_error())


@allure.title("Test Error Password Validation: {password}")
@pytest.mark.parametrize("password", [generate_random_password(3), generate_random_password(21)])
def test_error_password_validation_3_and_21_characters(password, registration_page):

    user = UserFactory().create_default()
    user.set_password(password)

    with allure.step("Performing registration with invalid password"):
        registration_page.open()
        registration_page.register(user, False)

    with allure.step("Verifying password validation"):
        registration_page.assert_password_validation()
        print(registration_page.password_error())


@allure.title("Test Error Password Confirm Validation: {password_confirm}")
@pytest.mark.parametrize("password_confirm", [generate_random_password(4), generate_random_password(20)])
def test_error_password_confirm_validation_3_and_21_characters(password_confirm, registration_page):

    user = UserFactory().create_default()
    user.set_password_confirm(password_confirm)

    with allure.step("Performing registration with different password confirm"):
        registration_page.open()
        registration_page.register(user, False)

    with allure.step("Verifying password confirm validation"):
        registration_page.assert_password_confirm_validation()
        print(registration_page.password_confirm_error())


@allure.title("Test Error Privacy Policy Validation: {privacy_policy}")
def test_error_privacy_policy_validation(registration_page):

    user = UserFactory().create_default()

    with allure.step("Clicking on privacy policy box"):
        registration_page.open()
        registration_page.privacy_policy_box().click()

    with allure.step("Performing registration without accepting privacy policy"):
        registration_page.register(user, False)

    with allure.step("Verifying privacy policy agreement validation"):
        registration_page.assert_privacy_policy_agreement_validation()
        print(registration_page.privacy_policy_error())

