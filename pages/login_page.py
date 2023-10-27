from data import *
from helpers import BasePage


class LoginPage(BasePage):

    LOGIN_BUTTON = '//a[@class="h-drop h-user"]'
    USER_EMAIL = '//input[@name="login"]'
    PASSWORD = '//input[@type="password"]'
    LOGIN = '//form[@action="/"]//div[@class="form-group"]//button[@type="submit"]//span[text()="Войти"]'
    ACCOUNT_LOCATOR = '//div[@class="h-drop h-user hovered"]'
    CABINET_LOCATOR = '//div[text()="Личный кабинет"]'
    LOGIN_SUCCESS = '//*[text()="Hanna Shalabanava"]'
    LOGOUT_BUTTON = '//li[@class="account-menu__item"]//a[@href="/cabinet/logout"]'
    USER_NOT_FOUND = '//span[text()="Пользователь не найден."]'
    INVALID_PASSWORD = '//span[text()="Пароль неверный"]'
    RESTORE_PASSWORD = '//*[text()="Забыли пароль?"]'
    EMAIL_FOR_RESTORE = '//div[@class="f-group"]//input[@placeholder="Ваш email или номер телефона"]'
    GET_RESTORE_CODE_BUTTON = '//button[@class="btn btn--lg btn--block"]//span[text()="Получить код"]'
    SEND_RESTORE_CODE_BUTTON = '//span[text()="Отправить код"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get(DOMAIN)

    def click_on_login_button(self):
        self.click_on(self.LOGIN_BUTTON)

    def fill_email(self, email):
        self.fill(self.USER_EMAIL, email)

    def fill_password(self, password):
        self.fill(self.PASSWORD, password)

    def click_on_submit(self):
        self.click_on(self.LOGIN)

    def click_on_personal_account(self):
        self.click_on(self.ACCOUNT_LOCATOR)

    def assert_login_success(self):
        self.assert_text_in_element(self.LOGIN_SUCCESS, 'Hanna Shalabanava')

    def logout(self):
        self.click_on(self.LOGOUT_BUTTON)

    def assert_logout_success(self):
        self.assert_element_is_present(self.LOGIN_BUTTON)

    def login(self, user):
        self.open()
        self.click_on_login_button()
        self.fill_email(user['email'])
        self.fill_password(user['password'])
        self.click_on_submit()
        self.click_on_personal_account()

    def assert_invalid_email_entered(self):
        self.assert_element_is_present(self.USER_NOT_FOUND)

    def assert_invalid_password_entered(self):
        self.assert_element_is_present(self.INVALID_PASSWORD)

    def click_on_restore_password(self):
        self.click_on(self.RESTORE_PASSWORD)

    def fill_email_for_restore(self, email):
        self.fill(self.EMAIL_FOR_RESTORE, email)

    def get_restore_code(self):
        self.click_on(self.GET_RESTORE_CODE_BUTTON)

    def assert_send_code_button_is_present(self):
        self.assert_element_is_present(self.SEND_RESTORE_CODE_BUTTON)

