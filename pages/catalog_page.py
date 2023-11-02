from data import *
from helpers import BasePage
from locators import CatalogueLocators


class CataloguePage(BasePage, CatalogueLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get(SMARTPHONES_CATALOGUE_URL)

    def select_price_of_smartphones(self):
        self.fill(self.LOWER_PRICE, '500')
        self.click_on(self.HIGHER_PRICE)
        self.clear(self.HIGHER_PRICE)
        self.fill(self.HIGHER_PRICE, '1000')
        self.click_on(self.LOWER_PRICE)

    def assert_price_ranges(self):
        self.wait_for_visible(self.PRICE_RANGES)
        self.assert_element_is_present(self.PRICE_RANGES)

    def select_installment_goods(self):
        self.check_checkbox(self.INSTALLMENT_PAYMENT)

    def assert_installment_goods_selected(self):
        self.wait_for_visible(self.INSTALLMENT_PAYMENT_SIGN)
        self.assert_text_in_element(self.INSTALLMENT_PAYMENT_SIGN, 'Товары в рассрочку')

    def select_discounted_goods(self):
        self.check_checkbox(self.DISCOUNT_GOODS)

    def assert_discount_goods_selected(self):
        self.wait_for_visible(self.DISCOUNT_GOODS_SIGN)
        self.assert_text_in_element(self.DISCOUNT_GOODS_SIGN, 'Товары с уценкой')

    def select_all_goods_on_sale(self):
        self.click_on(self.ACTIONS_FILTER)
        self.check_checkbox(self.ALL_ACTIONS)

    def assert_goods_on_sale_selected(self):
        self.wait_for_visible(self.ALL_ACTIONS_SIGN)
        self.assert_text_in_element(self.ALL_ACTIONS_SIGN, 'Акции: ВСЕ акционные товары')

    def select_xiaomi_brand(self):
        self.check_checkbox(self.XIAOMI_BRAND_CHECKBOX)

    def assert_brand_is_selected(self):
        self.wait_for_visible(self.XIAOMI_BRAND_CHECKBOX)
        self.assert_text_in_element(self.BRAND_SELECTED_SIGN, 'Бренд: XIAOMI')

    def show_all_years(self):
        self.scroll_to_element(self.SHOW_ALL_YEARS)
        self.hard_click(self.SHOW_ALL_YEARS)

    def select_year_2023(self):
        self.scroll_to_element(self.YEAR_2023)
        self.hard_click(self.YEAR_2023)

    def assert_year_2023_selected(self):
        self.wait_for_visible(self.YEAR_2023_SIGN)
        self.scroll_to_element(self.YEAR_2023_SIGN)
        self.assert_text_in_element(self.YEAR_2023_SIGN, 'Год выхода модели: 2023')

    def select_goods_by_rating(self):
        self.click_on(self.SORT_DROPDOWN)
        self.hard_click(self.VALUE_RATING)

    def assert_if_sort_by_rating_is_selected(self):
        self.wait_for_visible(self.SORT_BY_RATING)
        self.assert_text_in_element(self.SORT_BY_RATING, 'По рейтингу')

    def click_on_city_list(self):
        self.click_on(self.CATALOGUE_CITY_LIST)

    def select_city_of_a_client(self):
        self.click_on(self.CITY_OF_A_CLIENT_TO_SELECT)

    def assert_if_actual_city_is_selected(self):
        self.assert_element_is_present(self.FINAL_ACTUAL_CITY)







