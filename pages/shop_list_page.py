import allure

from data import *
from helpers import BasePage
from locators import ShopListLocators


class ShopListPage(BasePage, ShopListLocators):

    @allure.step('Open shop list page')
    def open(self):
        self.driver.get(SHOP_LIST_PAGE_URL)

    @allure.step('Click on shop map')
    def click_on_shop_map(self):
        self.click_on(self.SHOP_MAP)

    @allure.step('Assert shop map displayed')
    def assert_shop_map_displayed(self):
        self.assert_element_is_displayed(self.YANDEX_MAP, True)
