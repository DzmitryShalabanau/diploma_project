import allure

from data import *
from pages import LoginPage


@allure.title('Login as user')
@allure.feature('Login as TEST_USER with email')
def test_login(driver):
    login = LoginPage(driver)
    login.open()
    login.click_on_login_button()
    login.fill_email(TEST_USER['email'])
    login.fill_password(TEST_USER['password'])
    login.click_on_submit()
    login.click_on_personal_account()
    login.assert_login_success()


@allure.title('Logout as user')
@allure.feature('Logout as TEST_USER from personal cabinet of 5element')
def test_logout(driver):
    login = LoginPage(driver)
    login.login(TEST_USER)
    login.logout()
    login.assert_logout_success()


@allure.title('Login as user with invalid email')
@allure.feature('Login TEST_USER with invalid email')
def test_login_with_invalid_email(driver):
    login = LoginPage(driver)
    login.open()
    login.click_on_login_button()
    login.fill_email(TEST_USER['invalid_email'])
    login.fill_password(TEST_USER['password'])
    login.click_on_submit()
    login.assert_invalid_email_entered()


@allure.title('Login as user with invalid password')
@allure.feature('Login TEST_USER with invalid password')
def test_login_with_invalid_password(driver):
    login = LoginPage(driver)
    login.open()
    login.click_on_login_button()
    login.fill_email(TEST_USER['email'])
    login.fill_password(TEST_USER['invalid_password'])
    login.click_on_submit()
    login.assert_invalid_password_entered()


@allure.title('Restore login password')
@allure.feature('Restore login password and send it to email of a user')
def test_restore_login_password(driver):
    login = LoginPage(driver)
    login.open()
    login.click_on_login_button()
    login.click_on_restore_password()
    login.fill_email_for_restore(TEST_USER['email'])
    login.get_restore_code()
    login.assert_send_code_button_is_present()
