import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, WAIT_UNTIL=5):
        self.driver = driver
        self.WAIT_UNTIL = WAIT_UNTIL

    @allure.step('Wait for element visible on page')
    def wait_for_visible(self, locator):
        try:
            return WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} is not clickable"

    @allure.step('Wait for element clickable on page')
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.element_to_be_clickable((By.XPATH, locator)))

    @allure.step('Click on element')
    def click_on(self, locator):
        element = self.wait_for_visible(locator)
        element.click()

    @allure.step('JS click on element')
    def hard_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Get url of page')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Click on checkbox')
    def check_checkbox(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    @allure.step('Click on selected checkbox')
    def uncheck_checkbox(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        if element.is_selected():
            element.click()
        else:
            print("The element is already selected")

    @allure.step('Scroll down')
    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, window.innerHeight);")

    @allure.step('Scroll to element on page')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    @allure.step('Click on radio button')
    def select_radio_button(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    @allure.step('Select element from dropdown')
    def dropdown_select(self, locator, value):
        element = Select(self.driver.find_element(By.XPATH, locator))
        element.select_by_value(value)

    @allure.step('Get input text from element')
    def get_input_text(self, locator, text):
        element = self.driver.find_element(By.XPATH, locator)
        element.clear()
        element.send_keys(text)
        element.get_attribute(text)

    @allure.step('Get element attribute')
    def get_attribute(self, locator, attribute_name):
        element = self.driver.find_element(By.XPATH, locator)
        element.get_attribute(attribute_name)

    @allure.step('Wait for element is displayed on page')
    def wait_for_element_is_displayed(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        time.sleep(5)
        if element.is_displayed():
            pass
        else:
            return print(f"Element {locator} is  not displayed")

    @allure.step('Wait for element is enabled on page')
    def wait_for_element_is_enabled(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        time.sleep(5)
        if element.is_enabled():
            pass
        else:
            return print(f"Element {locator} is  not enabled")

    @allure.step('Assert element is enabled on page')
    def assert_element_is_enabled(self, locator, expected_result):
        element = self.driver.find_element(By.XPATH, locator)
        assert element.is_enabled() == expected_result, "Element is not enabled"

    @allure.step('Assert element is displayed on page')
    def assert_element_is_displayed(self, locator, expected_result):
        element = self.driver.find_element(By.XPATH, locator)
        assert element.is_displayed() == expected_result, "Element is not displayed"

    @allure.step('Fill text in element')
    def fill(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Clear text from element')
    def clear(self, locator):
        element = self.wait_for_visible(locator)
        element.clear()

    @allure.step('Assert text in element')
    def assert_text_in_element(self, locator, expected_result):
        element = self.driver.find_element(By.XPATH, locator)
        assert element.text == expected_result, "Text not the same"

    @allure.step('Wait for element to be located on page')
    def wait_for_presence_of_element_located(self, locator):
        try:
            return WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.presence_of_element_located((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} is not clickable"

    @allure.step('Assert actual URL of page')
    def assert_actual_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

    @allure.step('Switch to iframe')
    def switch_to_iframe(self):
        self.driver.switch_to.frame(self.wait_for_visible('//iframe'))

    @allure.step('Set display none')
    def set_display_none(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script('arguments[0].setAttribute("display", arguments[1])', element, 'none')

    @allure.step('Prompt alert')
    def prompt_alert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.send_keys("Answer")
        alert.accept()

    @allure.step('Open new window in browser')
    def open_new_window(self):
        self.driver.execute_script("window.open()")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.driver.close()

    @allure.step('Switch to new window in browser')
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Assert element is present on page')
    def assert_element_is_present(self, locator):
        try:
            self.wait_for_visible(locator)
        except Exception:
            assert False, f"Element {locator} is not present on the page"

    @allure.step('Assert element is not present on page')
    def assert_element_is_not_present(self, locator):
        try:
            self.wait_for_visible(locator)
            assert False, f"Element {locator} is present on the page"
        except Exception:
            pass

    @allure.step('Assert value in element attribute')
    def assert_value_in_element_attribute(self, locator, attribute, expected_result):
        element = self.wait_for_visible(locator)
        value = element.get_attribute(attribute)
        assert value == expected_result, "Attribute value not the same"

    @allure.step('Add cookie')
    def add_cookie(self, name, value):
        self.driver.add_cookie({'name': name, 'value': value})
        self.driver.refresh()

    @allure.step('Delete cookies')
    def delete_cookies(self):
        self.driver.delete_cookies()
        self.driver.refresh()
