import allure
from data import *
from helpers import BasePage
from locators import CatalogueLocators


class CatalogPage(BasePage, CatalogueLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open smartphones catalog')
    def open(self):
        self.driver.get(SMARTPHONES_CATALOG_URL)

    @allure.step('Select_prices')
    def select_price_of_smartphones(self):
        self.fill(self.LOWER_PRICE, '500')
        self.click_on(self.HIGHER_PRICE)
        self.clear(self.HIGHER_PRICE)
        self.fill(self.HIGHER_PRICE, '1000')
        self.click_on(self.LOWER_PRICE)

    @allure.step('Assert price ranges')
    def assert_price_ranges(self):
        self.wait_for_visible(self.PRICE_RANGES)
        self.assert_element_is_present(self.PRICE_RANGES)

    @allure.step('Select installment goods')
    def select_installment_goods(self):
        self.check_checkbox(self.INSTALLMENT_PAYMENT)

    @allure.step('Assert installment goods selected')
    def assert_installment_goods_selected(self):
        self.wait_for_visible(self.INSTALLMENT_PAYMENT_SIGN)
        self.assert_text_in_element(self.INSTALLMENT_PAYMENT_SIGN, 'Товары в рассрочку')

    @allure.step('Select discount goods')
    def select_discount_goods(self):
        self.check_checkbox(self.DISCOUNT_GOODS)

    @allure.step('Assert discount goods selected')
    def assert_discount_goods_selected(self):
        self.wait_for_visible(self.DISCOUNT_GOODS_SIGN)
        self.assert_text_in_element(self.DISCOUNT_GOODS_SIGN, 'Товары с уценкой')

    @allure.step('Select all goods on sale')
    def select_all_hit_devices(self):
        self.click_on(self.ACTIONS_FILTER)
        self.hard_click(self.HITS)

    @allure.step('Assert all goods on sale selected')
    def assert_hits_selected(self):
        self.wait_for_visible(self.HITS_SIGN)
        self.assert_text_in_element(self.HITS_SIGN, 'Акции: Лидеры продаж')

    @allure.step('Select xiaomi brand')
    def select_xiaomi_brand(self):
        self.check_checkbox(self.XIAOMI_BRAND_CHECKBOX)

    @allure.step('Assert brand is selected')
    def assert_brand_is_selected(self):
        self.wait_for_visible(self.XIAOMI_BRAND_CHECKBOX)
        self.assert_text_in_element(self.BRAND_SELECTED_SIGN, 'Бренд: XIAOMI')

    @allure.step('Show all years')
    def show_all_years(self):
        self.scroll_to_element(self.SHOW_ALL_YEARS)
        self.hard_click(self.SHOW_ALL_YEARS)

    @allure.step('Select year 2023')
    def select_year_2023(self):
        self.scroll_to_element(self.YEAR_2023)
        self.hard_click(self.YEAR_2023)

    @allure.step('Assert year 2023 selected')
    def assert_year_2023_selected(self):
        self.wait_for_visible(self.YEAR_2023_SIGN)
        self.scroll_to_element(self.YEAR_2023_SIGN)
        self.assert_text_in_element(self.YEAR_2023_SIGN, 'Год выхода модели: 2023')

    @allure.step('Select goods by rating')
    def select_goods_by_rating(self):
        self.click_on(self.SORT_DROPDOWN)
        self.hard_click(self.VALUE_RATING)

    @allure.step('Assert sort by rating is selected')
    def assert_sort_by_rating_is_selected(self):
        self.wait_for_visible(self.SORT_BY_RATING)
        self.assert_text_in_element(self.SORT_BY_RATING, 'По рейтингу')

    @allure.step('Click on city list')
    def click_on_city_list(self):
        self.click_on(self.CATALOGUE_CITY_LIST)

    @allure.step('Select city of a client')
    def select_city_of_a_client(self):
        self.click_on(self.CITY_OF_A_CLIENT_TO_SELECT)

    @allure.step('Assert actual city is selected')
    def assert_actual_city_is_selected(self):
        self.assert_element_is_present(self.FINAL_ACTUAL_CITY)
