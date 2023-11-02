from elements import HeaderElement


def test_fifth_element_logo(driver, open_main_page):
    header = HeaderElement(driver)
    header.assert_fifth_element_logo()


def test_change_current_city(driver, open_main_page):
    header = HeaderElement(driver)
    header.click_on_current_city()
    header.change_city()
    header.assert_changed_city()


def test_search_for_item(driver, open_main_page):
    header = HeaderElement(driver)
    header.click_on_search_form()
    header.fill_search_form()
    header.click_on_search_button()
    header.assert_search_result()


def test_compare_section_is_empty(driver, open_main_page):
    header = HeaderElement(driver)
    header.click_on_compare_section()
    header.assert_compare_section_is_empty()


def test_favorites_section_is_empty(driver, open_main_page):
    header = HeaderElement(driver)
    header.click_on_favorites_section()
    header.assert_favorites_section_is_empty()


def test_check_header_contacts(driver, open_main_page):
    header = HeaderElement(driver)
    header.click_on_header_contacts()
    header.assert_contacts()
