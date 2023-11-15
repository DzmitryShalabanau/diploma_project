
from elements import HeaderElement


def test_fifth_element_logo(driver):
    header = HeaderElement(driver)
    header.open()
    header.assert_fifth_element_logo()


def test_change_current_city(driver):
    header = HeaderElement(driver)
    header.open()
    header.click_on_current_city()
    header.change_city()
    header.assert_changed_city()


def test_search_for_item(driver):
    header = HeaderElement(driver)
    header.open()
    header.click_on_search_form()
    header.fill_search_form()
    header.click_on_search_button()
    header.assert_search_result()














