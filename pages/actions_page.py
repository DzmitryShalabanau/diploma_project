from data import *
from helpers import BasePage
from locators import ActionsLocators


class ActionsPage(BasePage, ActionsLocators):

    def open(self):
        self.driver.get(ACTIONS_PAGE_URL)

    def assert_sales_page(self):
        self.assert_element_is_displayed(self.DISCOUNT_LOCATOR, True)


