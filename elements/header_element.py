from helpers import BasePage


class HeaderElement(BasePage):
    LOGO = '//img[@src="/resources/images/logo_.svg"]'
    DISCOUNT = '//span[@class="h-discounts__text"]'
    CURRENT_CITY = '//div[text()="Минск"]'
    NEW_CITY = '//div[text()="Брест"]'
    FINAL_CITY = '//div[text()="Брест"]'
    SHOPS = '//a[text()="Магазины"]'
    SEARCH_FORM = '//form[@class="h-search__form"]'
    SEARCH_FORM_FOR_FILL = '//input[@maxlength="90"]'
    SEARCH_BUTTON = '//div[1]/form/div/button[2]'
    SEARCH_RESULT = '//div[text()="Результаты поиска «notebook»"]'
    SMARTPHONES_CATALOGUE = '//a[@href="/catalog/377-smartfony"]'

    def open(self):
        self.driver.get('https://5element.by/')

    def assert_fifth_element_logo(self):
        self.assert_element_is_present(self.LOGO)

    def click_on_sales(self):
        self.click_on(self.DISCOUNT)

    def click_on_current_city(self):
        self.click_on(self.CURRENT_CITY)

    def change_city(self):
        self.click_on(self.NEW_CITY)

    def assert_changed_city(self):
        self.assert_element_is_displayed(self.FINAL_CITY, True)

    def click_on_shop_list(self):
        self.click_on(self.SHOPS)

    def click_on_search_form(self):
        self.click_on(self.SEARCH_FORM)

    def fill_search_form(self):
        self.wait_for_visible(self.SEARCH_FORM_FOR_FILL)
        self.fill(self.SEARCH_FORM_FOR_FILL, 'notebook')

    def click_on_search_button(self):
        self.click_on(self.SEARCH_BUTTON)

    def assert_search_result(self):
        self.assert_element_is_displayed(self.SEARCH_RESULT, True)

    def click_on_smartphones(self):
        self.click_on(self.SMARTPHONES_CATALOGUE)










