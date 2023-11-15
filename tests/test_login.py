from data import TEST_USER
from pages import LoginPage


# 1
def test_login(driver):
    login = LoginPage(driver)
    login.open()
    login.click_on_login_button()
    login.fill_email(TEST_USER['email'])
    login.fill_password(TEST_USER['password'])
    login.click_on_submit()
    login.click_on_personal_account()
    login.assert_login_success()


# 2
def test_logout(driver):
    login = LoginPage(driver)
    login.login(TEST_USER)
    login.logout()
    login.assert_logout_success()


def test_login_with_invalid_email(driver):
    login = LoginPage(driver)
    login.open()
    login.click_on_login_button()
    login.fill_email(TEST_USER['invalid_email'])
    login.fill_password(TEST_USER['password'])
    login.click_on_submit()
    login.assert_invalid_email_entered()


def test_login_with_invalid_password(driver):
    login = LoginPage(driver)
    login.open()
    login.click_on_login_button()
    login.fill_email(TEST_USER['email'])
    login.fill_password(TEST_USER['invalid_password'])
    login.click_on_submit()
    login.assert_invalid_password_entered()


def test_restore_login_password(driver):
    login = LoginPage(driver)
    login.open()
    login.click_on_login_button()
    login.click_on_restore_password()
    login.fill_email_for_restore(TEST_USER['email'])
    login.get_restore_code()
    login.assert_send_code_button_is_present()







