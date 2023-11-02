from helpers import BasePage
from locators import HeaderLocators
from data import *


class HeaderElement(BasePage, HeaderLocators):

    def open(self):
        self.driver.get(DOMAIN)

    def assert_fifth_element_logo(self):
        self.assert_element_is_present(self.LOGO)

    def click_on_sales(self):
        self.click_on(self.DISCOUNT)

    def click_on_current_city(self):
        self.click_on(self.CURRENT_CITY)

    def change_city(self):
        self.click_on(self.NEW_CITY)

    def assert_changed_city(self):
        self.assert_element_is_displayed(self.FINAL_CITY, True)

    def click_on_shop_list(self):
        self.click_on(self.SHOPS)

    def click_on_search_form(self):
        self.click_on(self.SEARCH_FORM)

    def fill_search_form(self):
        self.wait_for_visible(self.SEARCH_FORM_FOR_FILL)
        self.fill(self.SEARCH_FORM_FOR_FILL, 'notebook')

    def click_on_search_button(self):
        self.click_on(self.SEARCH_BUTTON)

    def assert_search_result(self):
        self.assert_element_is_displayed(self.SEARCH_RESULT, True)

    def click_on_smartphones(self):
        self.click_on(self.SMARTPHONES_CATALOGUE)

    def click_on_compare_section(self):
        self.click_on(self.COMPARE)

    def assert_compare_section_is_empty(self):
        self.assert_text_in_element(self.EMPTY_COMPARE, 'Пока не добавлено ни одного товара для сравнения')

    def click_on_favorites_section(self):
        self.click_on(self.FAVORITES)

    def assert_favorites_section_is_empty(self):
        self.assert_text_in_element(self.EMPTY_FAVORITES, 'У нас столько замечательных товаров, а в Избранном у Вас – пусто :(')

    def click_on_header_contacts(self):
        self.click_on(self.CONTACTS)

    def assert_mts_number(self):
        self.assert_text_in_element(self.MTS_NUMBER, CONTACTS['mts'])

    def assert_a1_number(self):
        self.assert_text_in_element(self.A1_NUMBER, CONTACTS['a1'])

    def assert_life_number(self):
        self.assert_text_in_element(self.LIFE_NUMBER, CONTACTS['life'])

    def assert_city_number(self):
        self.assert_text_in_element(self.CITY_NUMBER, CONTACTS['city_number'])

    def assert_email(self):
        self.assert_text_in_element(self.EMAIL, CONTACTS['email'])

    def assert_contacts(self):
        self.assert_mts_number()
        self.assert_a1_number()
        self.assert_life_number()
        self.assert_city_number()
        self.assert_email()












