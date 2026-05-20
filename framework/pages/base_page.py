from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Settings.EXPLICIT_WAIT)

    def find_by_accessibility_id(self, locator):
        return self.wait.until(
            ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, locator))
        )

    def tap_by_accessibility_id(self, locator):
        self.find_by_accessibility_id(locator).click()

    def is_visible_by_accessibility_id(self, locator):
        try:
            self.wait.until(
                ec.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, locator))
            )
            return True
        except Exception:
            return False

    def get_visible_element_by_index(self, locator, index, element_name="element"):
        elements = self.wait.until(ec.visibility_of_all_elements_located(locator))
        zero_based_index = index - 1
        if zero_based_index < 0 or zero_based_index >= len(elements):
            raise TimeoutException(
                f"{element_name} index {index} is not available. Total found: {len(elements)}"
            )
        return elements[zero_based_index]
