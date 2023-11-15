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

    def wait_for_visible(self, locator):
        try:
            return WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} is not clickable"

    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.element_to_be_clickable((By.XPATH, locator)))

    def click_on(self, locator):
        element = self.wait_for_visible(locator)
        element.click()

    def hard_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_current_url(self):
        return self.driver.current_url

    def check_checkbox(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    def uncheck_checkbox(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        if element.is_selected():
            element.click()
        else:
            print("The element is already selected")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, window.innerHeight);")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def select_radio_button(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    def dropdown_select(self, locator, value):
        element = Select(self.driver.find_element(By.XPATH, locator))
        element.select_by_value(value)

    def get_input_text(self, locator, text):
        element = self.driver.find_element(By.XPATH, locator)
        element.clear()
        element.send_keys(text)
        element.get_attribute(text)

    def get_attribute(self, locator, attribute_name):
        element = self.driver.find_element(By.XPATH, locator)
        element.get_attribute(attribute_name)

    def wait_for_element_is_displayed(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        time.sleep(5)
        if element.is_displayed():
            pass
        else:
            return print(f"Element {locator} is  not displayed")

    def wait_for_element_is_enabled(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        time.sleep(5)
        if element.is_enabled():
            pass
        else:
            return print(f"Element {locator} is  not enabled")

    def assert_element_is_enabled(self, locator, expected_result):
        element = self.driver.find_element(By.XPATH, locator)
        assert element.is_enabled() == expected_result, "Element is not enabled"

    def assert_element_is_displayed(self, locator, expected_result):
        element = self.driver.find_element(By.XPATH, locator)
        assert element.is_displayed() == expected_result, "Element is not displayed"

    def fill(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def clear(self, locator):
        element = self.wait_for_visible(locator)
        element.clear()

    def assert_text_in_element(self, locator, expected_result):
        element = self.driver.find_element(By.XPATH, locator)
        assert element.text == expected_result, "Text not the same"

    def wait_for_presence_of_element_located(self, locator):
        try:
            return WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.presence_of_element_located((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} is not clickable"

    def assert_actual_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

    def switch_to_iframe(self):
        self.driver.switch_to.frame(self.wait_for_visible('//iframe'))

    def set_display_none(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script('arguments[0].setAttribute("display", arguments[1])', element, 'none')

    def prompt_alert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.send_keys("Answer")
        alert.accept()

    def open_new_window(self):
        self.driver.execute_script("window.open()")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.driver.close()

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def assert_element_is_present(self, locator):
        try:
            self.wait_for_visible(locator)
        except Exception as e:
            assert False, f"Element {locator} is not present on the page"

    def assert_element_is_not_present(self, locator):
        try:
            self.wait_for_visible(locator)
            assert False, f"Element {locator} is present on the page"
        except Exception as e:
            pass

    def assert_value_in_element_attribute(self, locator, attribute, expected_result):
        element = self.wait_for_visible(locator)
        value = element.get_attribute(attribute)
        assert value == expected_result, "Attribute value not the same"

    def add_cookie(self, name, value):
        self.driver.add_cookie({'name': name, 'value': value})
        self.driver.refresh()

    def delete_cookies(self):
        self.driver.delete_cookies()
        self.driver.refresh()







