from data import *
from helpers import BasePage
from locators import ShopListLocators


class ShopListPage(BasePage, ShopListLocators):

    def open(self):
        self.driver.get(SHOP_LIST_PAGE_URL)

    def click_on_shop_map(self):
        self.click_on(self.SHOP_MAP)

    def assert_shop_map(self):
        self.assert_element_is_displayed(self.YANDEX_MAP, True)


