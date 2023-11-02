
from pages import CataloguePage


def test_select_smartphones_price_ranges(driver):
    catalog = CataloguePage(driver)
    catalog.open()
    catalog.select_price_of_smartphones()
    catalog.assert_price_ranges()


def test_select_installment_payment_smartphones(driver):
    catalog = CataloguePage(driver)
    catalog.open()
    catalog.select_installment_goods()
    catalog.assert_installment_goods_selected()


def test_select_discounted_goods(driver):
    catalog = CataloguePage(driver)
    catalog.open()
    catalog.select_discounted_goods()
    catalog.assert_discount_goods_selected()


def test_select_goods_on_sale(driver):
    catalog = CataloguePage(driver)
    catalog.open()
    catalog.select_all_goods_on_sale()
    catalog.assert_goods_on_sale_selected()


def test_select_goods_by_brand(driver):
    catalog = CataloguePage(driver)
    catalog.open()
    catalog.select_xiaomi_brand()
    catalog.assert_brand_is_selected()


def test_select_year_2023_goods(driver):
    catalog = CataloguePage(driver)
    catalog.open()
    catalog.show_all_years()
    catalog.select_year_2023()
    catalog.assert_year_2023_selected()


def test_sort_goods_by_rating(driver):
    catalog = CataloguePage(driver)
    catalog.open()
    catalog.select_goods_by_rating()
    catalog.assert_if_sort_by_rating_is_selected()


def test_select_city_of_aclient(driver):
    catalog = CataloguePage(driver)
    catalog.open()
    catalog.click_on_city_list()
    catalog.select_city_of_a_client()
    catalog.assert_if_actual_city_is_selected()
