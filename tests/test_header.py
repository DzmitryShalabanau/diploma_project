import allure

from elements import HeaderElement
from pages import ActionsPage, ShopListPage


@allure.title('Check availability of fifth element logo')
@allure.feature('Check availability of fifth element logo on main page')
def test_fifth_element_logo(driver, open_main_page):
    header = HeaderElement(driver)
    header.assert_fifth_element_logo()


@allure.title('Change city of a user')
@allure.feature('Change city of a user from Minsk to Brest')
def test_change_current_city(driver, open_main_page):
    header = HeaderElement(driver)
    header.click_on_current_city()
    header.change_city()
    header.assert_changed_city()


@allure.title('Search for item')
@allure.feature('Search for notebook from main page search form')
def test_search_for_item(driver, open_main_page):
    header = HeaderElement(driver)
    header.click_on_search_form()
    header.fill_search_form()
    header.click_on_search_button()
    header.assert_search_result()


@allure.title('Check the sign of empty compare section')
@allure.feature('Check the sign of empty compare section from header')
def test_compare_section_is_empty(driver, open_main_page):
    header = HeaderElement(driver)
    header.click_on_compare_section()
    header.assert_compare_section_is_empty()


@allure.title('Check the sign of empty favorites section')
@allure.feature('Check the sign of empty favorites section from header')
def test_favorites_section_is_empty(driver, open_main_page):
    header = HeaderElement(driver)
    header.click_on_favorites_section()
    header.assert_favorites_section_is_empty()


@allure.title('Check relevance of header contacts')
@allure.feature('Check relevance of header contacts of 5element')
def test_check_header_contacts(driver, open_main_page):
    header = HeaderElement(driver)
    header.click_on_header_contacts()
    header.assert_contacts()


@allure.title('Check work of sales page')
@allure.feature('Open sales page and check it is opened')
def test_check_sales_page(driver):
    header = HeaderElement(driver)
    actions = ActionsPage(driver)
    header.open()
    header.click_on_sales()
    actions.assert_sales_page()


@allure.title('Check work of shops map')
@allure.feature('Open shop map page and check presence of shop map')
def test_shops_map(driver):
    header = HeaderElement(driver)
    shop_list = ShopListPage(driver)
    header.open()
    header.click_on_shop_list()
    shop_list.click_on_shop_map()
    shop_list.assert_shop_map_displayed()
