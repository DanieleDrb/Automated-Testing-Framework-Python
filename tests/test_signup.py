import time

import allure
import pytest
from selenium import webdriver
from pages.registration_page import RegistrationPage
from pages.account_succes_page import AccountSuccessPage
from utilities.user_factory import UserFactory
from utilities.utility import (generate_random_name, generate_random_email,
                               generate_random_password, generate_random_phone_number)


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


@pytest.fixture(scope="function")
def account_success_page(setup_teardown):
    def _account_success_page():
        return AccountSuccessPage(setup_teardown)
    yield _account_success_page()


@allure.title("Test User Created Successfully (Click)")
def test_user_created_successfully_click(registration_page, account_success_page):
        user = UserFactory().create_default()
        registration_page.open()
        registration_page.register(user, False)
        account_success_page.assert_account_created_successfully()
        print(account_success_page.account_created() + " --> Registration With Click")


@allure.title("Test User Created Successfully (Press)")
def test_user_created_successfully_press(registration_page, account_success_page):
    user = UserFactory().create_default()

    registration_page.open()
    registration_page.register(user, True)
    time.sleep(3)
    account_success_page.assert_account_created_successfully()
    print(account_success_page.account_created() + " --> Registration With Enter")


@allure.title("Test User Created Successfully (First Name)")
@pytest.mark.parametrize("first_name", [generate_random_name(1), generate_random_name(32)])
def test_user_created_successfully_first_name_1_and_32_characters(first_name, registration_page, account_success_page):
    user = UserFactory().create_default()
    user.set_first_name(first_name)

    registration_page.open()
    registration_page.register(user, False)
    print(account_success_page.account_created() + " --> First Name With 1 and 32 Random Characters")


@allure.title("Test User Created Successfully (Last Name)")
@pytest.mark.parametrize("last_name", [generate_random_name(1), generate_random_name(32)])
def test_user_created_successfully_last_name_1_and_32_characters(last_name, registration_page, account_success_page):
    user = UserFactory().create_default()
    user.set_last_name(last_name)

    registration_page.open()
    registration_page.register(user, False)
    print(account_success_page.account_created() + " --> Last Name With 1 and 32 Random Characters")


@allure.title("Test User Created Successfully (Email)")
@pytest.mark.parametrize("email", [generate_random_email(4), generate_random_email(32)])
def test_user_created_successfully_email_4_and_32_characters(email, registration_page, account_success_page):
    user = UserFactory().create_default()
    user.set_email(email)

    registration_page.open()
    registration_page.register(user, False)
    print(account_success_page.account_created() + " --> Email With Valid Form (x@x.x) With 4 and 32 Random Characters")


@allure.title("Test User Created Successfully (Phone Number)")
@pytest.mark.parametrize("phone", [generate_random_phone_number(3), generate_random_phone_number(32)])
def test_user_created_successfully_phone_number_3_and_32_numbers(phone, registration_page, account_success_page):
    user = UserFactory().create_default()
    user.set_phone_number(phone)

    registration_page.open()
    registration_page.register(user, False)
    print(account_success_page.account_created() + " --> Phone Number With 3 and 32 Random Numbers")


@allure.title("Test User Created Successfully (Password)")
@pytest.mark.parametrize("password", [generate_random_password(4), generate_random_password(20)])
def test_user_created_successfully_password_4_and_20_characters(password, registration_page, account_success_page):
    user = UserFactory().create_default()
    user.set_password(password)

    registration_page.open()
    registration_page.register(user, False)
    print(account_success_page.account_created() + " --> Password With 4 and 20 Random Characters")


@allure.title("Test User Created Successfully (Newsletter Subscribe True)")
def test_user_created_successfully_newsletter_subscribe_true(registration_page, account_success_page):
    user = UserFactory().create_default()
    user.set_subscribe(True)

    registration_page.open()
    registration_page.register(user, False)
    print(account_success_page.account_created() + " --> Subscribe Checked")

