import allure
from pages import CartPage


@allure.title('Add item to cart')
@allure.feature('Add item to cart from main page through search')
def test_add_item_to_cart(driver, open_main_page):
    cart = CartPage(driver)
    cart.click_on_search_form()
    cart.search_for_item()
    cart.add_item()
    cart.move_to_cart()
    cart.assert_if_item_is_added_to_cart()


@allure.title('Delete item from cart')
@allure.feature('Delete item from cart, when it is the only one in it')
def test_delete_item_from_cart(driver, open_main_page):
    cart = CartPage(driver)
    cart.add_item_to_cart()
    cart.delete_item_from_cart()
    cart.assert_item_is_deleted_from_cart()


@allure.title('Add service to item from cart')
@allure.feature('Add defence service to smartphone')
def test_add_service_to_item_from_cart(driver, open_main_page):
    cart = CartPage(driver)
    cart.add_item_to_cart()
    cart.open_service_list()
    cart.add_service_for_item()
    cart.assert_service_is_added()


@allure.title('Fill wrong promotional code')
@allure.feature('Fill wrong promotional code QAP14')
def test_enter_wrong_promotional_code_in_cart(driver, open_main_page):
    cart = CartPage(driver)
    cart.add_item_to_cart()
    cart.enter_wrong_promotional_code()
    cart.apply_promotional_code()
    cart.assert_wrong_promotional_code_entered()
