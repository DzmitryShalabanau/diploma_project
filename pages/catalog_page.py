from data import *
from helpers import BasePage


class CataloguePage(BasePage):

    LOWER_PRICE = '//*[@id="filter-price"]/div/div[1]/div/div[1]/input'
    HIGHER_PRICE = '//*[@id="filter-price"]/div/div[1]/div/div[2]/input'
    PRICE_RANGES = '//*[text()="Цена: от 500 до 1000 руб."]'
    INSTALLMENT_PAYMENT = '//div[4]/div/div/label/div[1]'
    INSTALLMENT_PAYMENT_SIGN = '//span[text()="Товары в рассрочку"]'
    DISCOUNT_GOODS = '//div[5]/div/div/label/div[1]'
    DISCOUNT_GOODS_SIGN = '//span[text()="Товары с уценкой"]'
    ACTIONS_FILTER = '//div[@data-target="#filter-actions"]'
    ALL_ACTIONS = '//*[@id="filter-actions"]/div/div[2]/div/label/div[1]'
    ALL_ACTIONS_SIGN = '//span[text()="Акции: ВСЕ акционные товары"]'
    XIAOMI_BRAND_CHECKBOX = '//*[@id="filter-692695"]/div/div[2]/div/label/div[1]'
    BRAND_SELECTED_SIGN = '//span[text()="Бренд: XIAOMI"]'
    SHOW_ALL_YEARS = '//*[@id="filter-726460"]/div/a/span[1]'
    YEAR_2023 = '//*[@id="filter-more-726460"]/div[2]/div/label/div[1]'
    YEAR_2023_SIGN = '//span[text()="Год выхода модели: 2023"]'
    SORT_DROPDOWN = '//div[2]/div/div/div[2]/div/button'
    VALUE_RATING = '//input[@value="rating"]'
    SORT_BY_RATING = '//span[text()="По рейтингу"]'

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







