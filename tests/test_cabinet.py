from data import *
from pages import PersonalCabinetPage


# 3
def test_fill_personal_data(driver, login):
    cabinet = PersonalCabinetPage(driver)
    cabinet.click_on_personal_data()
    cabinet.fill_personal_data(TEST_USER_DATA)
    cabinet.choose_female_gender()
    cabinet.save_personal_data()
    cabinet.click_on_personal_account()
    cabinet.assert_saved_personal_data(TEST_USER_DATA)


# 4
def test_subscribe_to_email_newsletter(driver, login, delete_subscribes):
    cabinet = PersonalCabinetPage(driver)
    cabinet.click_on_my_subscribes()
    cabinet.check_regular_mailing()
    cabinet.check_policy_agree()
    cabinet.save_subscribes()
    cabinet.assert_subscribes_saved_changes()


# 5
def test_unsubscribe_to_email_newsletter(driver, login):
    cabinet = PersonalCabinetPage(driver)
    cabinet.click_on_my_subscribes()
    cabinet.check_regular_mailing()
    cabinet.check_policy_agree()
    cabinet.save_subscribes()
    cabinet.click_on_sub_ok_button()
    cabinet.uncheck_regular_mailing()
    cabinet.save_subscribes()
    cabinet.assert_subscribes_saved_changes()


# 6
def test_select_favorite_shop(driver, login, delete_shop):
    cabinet = PersonalCabinetPage(driver)
    cabinet.click_on_my_shop_button()
    cabinet.select_shop()
    cabinet.assert_if_favorite_shop_is_selected()


# 7
def test_delete_favorite_shop(driver, login):
    cabinet = PersonalCabinetPage(driver)
    cabinet.click_on_my_shop_button()
    cabinet.select_shop()
    cabinet.delete_favorite_shop()
    cabinet.assert_if_favorite_shop_is_deleted()


# 8
def test_add_delivery_address(driver, login, delete_address):
    cabinet = PersonalCabinetPage(driver)
    cabinet.click_on_delivery_address()
    cabinet.click_on_address_form()
    cabinet.fill_delivery_address_form(TEST_USER_ADDRESS)
    cabinet.set_address_to_default()
    cabinet.save_address_settings()
    cabinet.assert_added_address()


# 9
def test_delete_delivery_address(driver, login):
    cabinet = PersonalCabinetPage(driver)
    cabinet.click_on_delivery_address()
    cabinet.click_on_address_form()
    cabinet.fill_delivery_address_form(TEST_USER_ADDRESS)
    cabinet.set_address_to_default()
    cabinet.save_address_settings()
    cabinet.click_on_delivery_address()
    cabinet.delete_address()
    cabinet.confirm_delete_address()
    cabinet.assert_if_address_is_deleted()
