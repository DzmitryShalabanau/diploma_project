from data import *
from helpers import BasePage


class ActionsPage(BasePage):
    DISCOUNT_LOCATOR = '//*[@id="app"]/main/div[2]/div/div/div[1]/div[1]'

    def open(self):
        self.driver.get(ACTIONS_PAGE_URL)

    def assert_sales_page(self):
        self.assert_element_is_displayed(self.DISCOUNT_LOCATOR, True)


