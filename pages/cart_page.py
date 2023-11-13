import allure
from data import *
from helpers import BasePage
from locators import CartLocators


class CartPage(BasePage, CartLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open cart page')
    def open(self):
        self.driver.get(CART_PAGE_URL)

    @allure.step('Click on search form')
    def click_on_search_form(self):
        self.click_on(self.SEARCH_FORM)

    @allure.step('Fill search form')
    def search_for_item(self):
        self.fill(self.ITEM_SEARCH, USER_ITEMS['item_1'])

    @allure.step('Add item')
    def add_item(self):
        self.click_on(self.ADD_TO_CART_BUTTON)

    @allure.step('Move to cart')
    def move_to_cart(self):
        self.click_on(self.MOVE_TO_CART_BUTTON)

    @allure.step('Assert if item is added to cart')
    def assert_if_item_is_added_to_cart(self):
        self.assert_text_in_element(self.ADDED_ITEM, 'Смартфон Xiaomi Redmi 10C 4GB/128GB Graphite Gray EU')

    @allure.step('Add item to cart')
    def add_item_to_cart(self):
        self.click_on_search_form()
        self.search_for_item()
        self.add_item()
        self.move_to_cart()

    @allure.step('Delete item from cart')
    def delete_item_from_cart(self):
        self.click_on(self.DELETE_BUTTON)

    @allure.step('Assert item is deleted from cart')
    def assert_item_is_deleted_from_cart(self):
        self.assert_element_is_not_present(self.ADDED_ITEM)

    @allure.step('Open service list')
    def open_service_list(self):
        self.click_on(self.ADD_SERVICE_TRIGGER)

    @allure.step('Add service for item')
    def add_service_for_item(self):
        self.click_on(self.ADD_SERVICE_BUTTON)

    @allure.step('Assert service is added')
    def assert_service_is_added(self):
        self.assert_element_is_present(self.ADDED_SERVICE)

    @allure.step('Fill wrong promotional code')
    def enter_wrong_promotional_code(self):
        self.fill(self.PROMOTIONAL_CODE_FIELD, 'QAP14')

    @allure.step('Apply promotional code')
    def apply_promotional_code(self):
        self.click_on(self.CODE_APPLY_BUTTON)

    @allure.step('Assert wrong promotional code entered')
    def assert_wrong_promotional_code_entered(self):
        self.assert_element_is_present(self.CODE_NOT_FOUND)
