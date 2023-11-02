from elements import HeaderElement
from pages import ActionsPage, ShopListPage


def test_check_sales_page(driver):
    header = HeaderElement(driver)
    actions = ActionsPage(driver)
    header.open()
    header.click_on_sales()
    actions.assert_sales_page()


def test_shops_map(driver):
    header = HeaderElement(driver)
    shop_list = ShopListPage(driver)
    header.open()
    header.click_on_shop_list()
    shop_list.click_on_shop_map()
    shop_list.assert_shop_map()
