from helpers import BasePage
from data import *


class ShopListPage(BasePage):
    SHOP_MAP = "//button[contains(text(),'Карта')]"
    YANDEX_MAP = '//*[@id="app"]/main/div[2]/div/div/div[3]'

    def open(self):
        self.driver.get('https://5element.by/shops')

    def click_on_shop_map(self):
        self.click_on(self.SHOP_MAP)

    def assert_shop_map(self):
        self.assert_element_is_displayed(self.YANDEX_MAP, True)


