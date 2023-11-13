import allure
from helpers import BasePage
from locators import CabinetLocators


class PersonalCabinetPage(BasePage, CabinetLocators):

    @allure.step('Click on personal data')
    def click_on_personal_data(self):
        self.click_on(self.PERSONAL_DATA)

    @allure.step('Fill surname')
    def fill_surname(self, surname):
        self.fill(self.USER_SURNAME, surname)

    @allure.step('Fill name')
    def fill_name(self, name):
        self.fill(self.USER_NAME, name)

    @allure.step('Fill lastname')
    def fill_lastname(self, lastname):
        self.fill(self.USER_LASTNAME, lastname)

    @allure.step('Fill birthday')
    def fill_birthday(self, birthday):
        self.fill(self.USER_BIRTHDAY, birthday)

    @allure.step('Fill personal data')
    def fill_personal_data(self, user):
        self.fill_surname(user['surname'])
        self.fill_name(user['name'])
        self.fill_lastname(user['lastname'])
        self.fill_birthday(user['birthday'])

    @allure.step('Chose gender')
    def choose_female_gender(self):
        self.select_radio_button(self.FEMALE_GENDER)

    @allure.step('Saver user data')
    def save_personal_data(self):
        self.click_on(self.SAVE_PERSONAL_BUTTON)

    @allure.step('Click on personal account')
    def click_on_personal_account(self):
        self.click_on(self.ACCOUNT_LOCATOR)

    @allure.step('Assert saved personal data')
    def assert_saved_personal_data(self, user):
        self.assert_text_in_element(self.SAVED_DATA, user['saved_data'])

    @allure.step('Click on my subscribes')
    def click_on_my_subscribes(self):
        self.click_on(self.MY_SUBSCRIBES)

    @allure.step('Click on regular mailing checkbox')
    def check_regular_mailing(self):
        self.check_checkbox(self.REGULAR_MAILING)

    @allure.step('Click on selected regular mailing checkbox')
    def uncheck_regular_mailing(self):
        self.check_checkbox(self.REGULAR_MAILING)

    @allure.step('Click on policy agree checkbox')
    def check_policy_agree(self):
        self.check_checkbox(self.POLICY_AGREE)

    @allure.step('Save subscribes')
    def save_subscribes(self):
        self.click_on(self.SAVE_SUBSCRIBES)

    @allure.step('Click on subscribes ok button')
    def click_on_sub_ok_button(self):
        self.click_on(self.SUB_OK_BUTTON)

    @allure.step('Assert subscribes saved changes')
    def assert_subscribes_done(self):
        self.assert_element_is_not_present(self.POLICY_AGREE)

    @allure.step('Assert subscribes canceled')
    def assert_subscribes_canceled(self):
        self.assert_element_is_present(self.POLICY_AGREE)

    @allure.step('Click on my shop button')
    def click_on_my_shop_button(self):
        self.click_on(self.MY_SHOP)

    @allure.step('Select shop')
    def select_shop(self):
        self.scroll_down()
        self.click_on(self.FAVORITE_SHOP_TO_CHOOSE)

    @allure.step('Favorite shop is selected')
    def assert_if_favorite_shop_is_selected(self):
        self.assert_element_is_not_present(self.FAVORITE_SHOP)

    @allure.step('Delete favorite shop')
    def delete_favorite_shop(self):
        self.click_on(self.DELETE_FAVORITE_SHOP_BUTTON)

    @allure.step('Assert favorite shop is deleted')
    def assert_if_favorite_shop_is_deleted(self):
        self.assert_element_is_not_present(self.FAVORITE_SHOP)

    @allure.step('Click on delivery address')
    def click_on_delivery_address(self):
        self.click_on(self.DELIVERY_ADDRESS)

    @allure.step('Click on address form')
    def click_on_address_form(self):
        self.click_on(self.ADD_ADDRESS_FORM)

    @allure.step('Fill city')
    def fill_city(self, city):
        self.fill(self.CITY_TO_FILL, city)
        self.click_on(self.SELECT_CITY)

    @allure.step('Fill street')
    def fill_street(self, street):
        self.fill(self.STREET_TO_FILL, street)
        self.click_on(self.SELECT_STREET)

    @allure.step('Fill house number')
    def fill_house_number(self, house):
        self.fill(self.HOUSE_TO_FILL, house)

    @allure.step('Fill apartment number')
    def fill_apartment_number(self, apartment):
        self.fill(self.APARTMENT_TO_FILL, apartment)

    @allure.step('Fill delivery adress form')
    def fill_delivery_address_form(self, user):
        self.fill_city(user['city'])
        self.fill_street(user['street'])
        self.fill_house_number(user['house'])
        self.fill_apartment_number(user['apartment'])

    @allure.step('Set address to default')
    def set_address_to_default(self):
        self.check_checkbox(self.SET_TO_DEFAULT_ADDRESS_CHECKBOX)

    @allure.step('Save address settings')
    def save_address_settings(self):
        self.click_on(self.SAVE_ADDRESS_BUTTON)

    @allure.step('Assert added address')
    def assert_added_address(self):
        self.assert_element_is_present(self.ADDRESS_IS_PRESENT)

    @allure.step('Delete address')
    def delete_address(self):
        self.click_on(self.DELETE_ADDRESS)

    @allure.step('Confirm delete address')
    def confirm_delete_address(self):
        self.click_on(self.CONFIRM_DELETE)

    @allure.step('Assert if address is deleted')
    def assert_if_address_is_deleted(self):
        self.assert_element_is_not_present(self.FAVORITE_SHOP)
