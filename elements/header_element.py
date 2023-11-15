import allure
from helpers import BasePage
from locators import HeaderLocators
from data import *


class HeaderElement(BasePage, HeaderLocators):
    @allure.step('Open main page')
    def open(self):
        self.driver.get(DOMAIN)

    @allure.step('Assert fifth element logo')
    def assert_fifth_element_logo(self):
        self.assert_element_is_present(self.LOGO)

    @allure.step('Click on sales page')
    def click_on_sales(self):
        self.click_on(self.DISCOUNT)

    @allure.step('Click on current city of a user')
    def click_on_current_city(self):
        self.click_on(self.CURRENT_CITY)

    @allure.step('Change citi of a user')
    def change_city(self):
        self.click_on(self.NEW_CITY)

    @allure.step('Assert changed city')
    def assert_changed_city(self):
        self.assert_element_is_displayed(self.FINAL_CITY, True)

    @allure.step('Click on shop list')
    def click_on_shop_list(self):
        self.click_on(self.SHOPS)

    @allure.step('Click on search form')
    def click_on_search_form(self):
        self.click_on(self.SEARCH_FORM)

    @allure.step('Fill request')
    def fill_search_form(self):
        self.wait_for_visible(self.SEARCH_FORM_FOR_FILL)
        self.fill(self.SEARCH_FORM_FOR_FILL, 'notebook')

    @allure.step('Click on search button')
    def click_on_search_button(self):
        self.click_on(self.SEARCH_BUTTON)

    @allure.step('Assert search result')
    def assert_search_result(self):
        self.assert_element_is_displayed(self.SEARCH_RESULT, True)

    @allure.step('Click on compare section')
    def click_on_compare_section(self):
        self.click_on(self.COMPARE_SECTION)

    @allure.step('Assert compare section is empty')
    def assert_compare_section_is_empty(self):
        self.assert_text_in_element(self.EMPTY_COMPARE, 'Пока не добавлено ни одного товара для сравнения')

    @allure.step('Click on favorites section')
    def click_on_favorites_section(self):
        self.click_on(self.FAVORITES)

    @allure.step('Assert favorites section is empty')
    def assert_favorites_section_is_empty(self):
        self.assert_text_in_element(self.EMPTY_FAVORITES, 'У нас столько замечательных товаров, а в Избранном у Вас – пусто :(')

    @allure.step('Click on header contacts')
    def click_on_header_contacts(self):
        self.click_on(self.CONTACTS)

    @allure.step('Assert MTS number')
    def assert_mts_number(self):
        self.assert_text_in_element(self.MTS_NUMBER, CONTACTS['mts'])

    @allure.step('Assert A1 number')
    def assert_a1_number(self):
        self.assert_text_in_element(self.A1_NUMBER, CONTACTS['a1'])

    @allure.step('Assert LIFE number')
    def assert_life_number(self):
        self.assert_text_in_element(self.LIFE_NUMBER, CONTACTS['life'])

    @allure.step('Assert CITY number')
    def assert_city_number(self):
        self.assert_text_in_element(self.CITY_NUMBER, CONTACTS['city_number'])

    @allure.step('Assert EMAIL')
    def assert_email(self):
        self.assert_text_in_element(self.EMAIL, CONTACTS['email'])

    @allure.step('Assert contacts')
    def assert_contacts(self):
        self.assert_mts_number()
        self.assert_a1_number()
        self.assert_life_number()
        self.assert_city_number()
        self.assert_email()

    def search_for_item_to_compare(self):
        self.wait_for_visible(self.SEARCH_FORM_FOR_FILL)
        self.fill(self.SEARCH_FORM_FOR_FILL, USER_ITEMS['item_3'])
