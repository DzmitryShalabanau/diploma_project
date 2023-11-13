import allure

from elements import HeaderElement
from pages import ComparisonPage


@allure.title('Add item to comparison')
@allure.feature('Add item to comparison from header search form')
def test_add_item_to_comparison(driver, open_main_page):
    header = HeaderElement(driver)
    compare = ComparisonPage(driver)
    header.click_on_search_form()
    header.search_for_item_to_compare()
    compare.add_item_to_comparison()
    compare.move_to_compare_section()
    compare.assert_item_added_to_comparison()


@allure.title('Add one more item to comparison list')
@allure.feature('Add one more mouse to compare from compare page')
def test_add_one_more_item_to_comparison_list(driver, open_main_page, add_item_to_comparison):
    compare = ComparisonPage(driver)
    compare.click_on_add_item_button()
    compare.add_second_item_to_comparison()
    compare.move_to_compare_section()
    compare.assert_second_item_added_to_comparison()


@allure.title('Clear comparison list')
@allure.feature('Delete all items from comparison page')
def test_clear_comparison_list(driver, open_main_page, add_item_to_comparison):
    compare = ComparisonPage(driver)
    compare.clear_comparison_list()
    compare.assert_comparison_list_cleared()


@allure.title('Delete item from comparison')
@allure.feature('Delete one item from comparison')
def test_delete_item_from_comparison(driver, open_main_page, add_items_to_comparison):
    compare = ComparisonPage(driver)
    compare.delete_item()
    compare.assert_item_deleted_from_comparison()
