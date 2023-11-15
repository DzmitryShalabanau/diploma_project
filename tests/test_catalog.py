import allure
from pages import CatalogPage


@allure.title('Select smartphones price ranges')
@allure.feature('Select smartphone prices from 500 to 1000')
def test_select_smartphones_price_ranges(driver):
    catalog = CatalogPage(driver)
    catalog.open()
    catalog.select_price_of_smartphones()
    catalog.assert_price_ranges()


@allure.title('Select installment payment items')
@allure.feature('Select installment payment smartphones')
def test_select_installment_payment_smartphones(driver):
    catalog = CatalogPage(driver)
    catalog.open()
    catalog.select_installment_goods()
    catalog.assert_installment_goods_selected()


@allure.title('Select items with discount')
@allure.feature('Select smartphones with discount')
def test_select_discounted_goods(driver):
    catalog = CatalogPage(driver)
    catalog.open()
    catalog.select_discount_goods()
    catalog.assert_discount_goods_selected()


@allure.title('Select items on sale')
@allure.feature('Select smartphones on sale')
def test_select_hit_devices(driver):
    catalog = CatalogPage(driver)
    catalog.open()
    catalog.select_all_hit_devices()
    catalog.assert_hits_selected()


@allure.title('Select one brand items')
@allure.feature('Select XIAOMI smartphones')
def test_select_goods_by_brand(driver):
    catalog = CatalogPage(driver)
    catalog.open()
    catalog.select_xiaomi_brand()
    catalog.assert_brand_is_selected()


@allure.title('Select 2023 year items')
@allure.feature('Select 2023 year smartphones')
def test_select_year_2023_goods(driver):
    catalog = CatalogPage(driver)
    catalog.open()
    catalog.show_all_years()
    catalog.select_year_2023()
    catalog.assert_year_2023_selected()


@allure.title('Sort items by rating')
@allure.feature('Sort smartphones by rating')
def test_sort_goods_by_rating(driver):
    catalog = CatalogPage(driver)
    catalog.open()
    catalog.select_goods_by_rating()
    catalog.assert_sort_by_rating_is_selected()


@allure.title('Select city of client')
@allure.feature('Change current city from Minsk to Brest')
def test_select_city_of_client(driver):
    catalog = CatalogPage(driver)
    catalog.open()
    catalog.click_on_city_list()
    catalog.select_city_of_a_client()
    catalog.assert_actual_city_is_selected()
