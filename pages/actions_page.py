import allure
from helpers import BasePage
from locators import ActionsLocators


class ActionsPage(BasePage, ActionsLocators):

    @allure.step('Assert actions page')
    def assert_sales_page(self):
        self.assert_element_is_displayed(self.DISCOUNT_LOCATOR, True)
