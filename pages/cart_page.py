from data import *
from helpers import BasePage
from locators import CartLocators


class CartPage(BasePage, CartLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get(CART_PAGE_URL)

    def click_on_search_form(self):
        self.click_on(self.SEARCH_FORM)

    def search_for_item(self):
        self.fill(self.ITEM_SEARCH, USER_ITEMS['item_1'])

    def add_item(self):
        self.click_on(self.ADD_TO_CART_BUTTON)

    def move_to_cart(self):
        self.click_on(self.MOVE_TO_CART_BUTTON)

    def assert_if_item_is_added_to_cart(self):
        self.assert_text_in_element(self.ADDED_ITEM, 'Смартфон Xiaomi Redmi 10C 4GB/128GB Graphite Gray EU')

    def add_item_to_cart(self):
        self.click_on_search_form()
        self.search_for_item()
        self.add_item()
        self.move_to_cart()

    def delete_item_from_cart(self):
        self.click_on(self.DELETE_BUTTON)

    def assert_item_is_deleted_from_cart(self):
        self.assert_element_is_not_present(self.ADDED_ITEM)

    def open_service_list(self):
        self.click_on(self.ADD_SERVICE_TRIGGER)

    def add_service_for_item(self):
        self.click_on(self.ADD_SERVICE_BUTTON)

    def assert_service_is_added(self):
        self.assert_element_is_present(self.ADDED_SERVICE)

    def add_one_more_item(self):
        self.hard_fill(self.NUMBER_BUTTON, '2')

    def assert_number_of_items_added(self):
        self.assert_text_in_element(self.NUMBER_OF_ITEMS, '(2)')

    def enter_wrong_promotional_code(self):
        self.fill(self.PROMOTIONAL_CODE_FIELD, 'QAP14')

    def apply_promotional_code(self):
        self.click_on(self.CODE_APPLY_BUTTON)

    def assert_wrong_promotional_code_entered(self):
        self.assert_element_is_present(self.CODE_NOT_FOUND)


