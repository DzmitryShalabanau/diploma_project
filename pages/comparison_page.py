import allure

from helpers import BasePage
from locators import ComparisonLocators


class ComparisonPage(BasePage, ComparisonLocators):

    @allure.step('Add item to comparison')
    def add_item_to_comparison(self):
        self.click_on(self.ADD_TO_COMPARISON_BUTTON)

    @allure.step('Move to comparison')
    def move_to_compare_section(self):
        self.click_on(self.COMPARE_SECTION)
        self.click_on(self.MOVE_TO_COMPARE_BUTTON)

    @allure.step('Assert item added to comparison')
    def assert_item_added_to_comparison(self):
        self.assert_element_is_present(self.MICE_COMPARISON)

    @allure.step('Clear comparison list')
    def clear_comparison_list(self):
        self.click_on(self.CLEAR_COMPARISON_LIST_BUTTON)

    @allure.step('Assert comparison list cleared')
    def assert_comparison_list_cleared(self):
        self.assert_text_in_element(self.NO_ITEMS_TO_COMPARE, 'Пока не добавлено ни одного товара для сравнения.')

    @allure.step('Click on add item button')
    def click_on_add_item_button(self):
        self.click_on(self.ADD_ITEM_BUTTON)

    @allure.step('Add second item to comparison')
    def add_second_item_to_comparison(self):
        self.click_on(self.ADD_SECOND_ITEM_TO_COMPARISON_BUTTON)

    @allure.step('Assert second item added to comparison')
    def assert_second_item_added_to_comparison(self):
        self.assert_text_in_element(self.TWO_ITEMS_IN_LIST_SIGN, '2')

    @allure.step('Delete one item from comparison')
    def delete_item(self):
        self.click_on(self.DELETE_G_102)

    @allure.step('Assert item deleted from comparison')
    def assert_item_deleted_from_comparison(self):
        self.assert_element_is_present(self.G_102)
