import logging
import random
import string
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage


class SignupPage(BasePage):
    LOGGER = logging.getLogger("cubii_signup_page")

    SIGN_UP_WITH_EMAIL_CARD = (AppiumBy.ID, "com.cubii:id/cardSignUpWithEmail")
    FIRST_NAME_INPUT = (AppiumBy.ID, "com.cubii:id/et_first_name")
    LAST_NAME_INPUT = (AppiumBy.ID, "com.cubii:id/et_last_name")
    EMAIL_INPUT = (AppiumBy.ID, "com.cubii:id/et_email")
    PASSWORD_INPUT = (AppiumBy.ID, "com.cubii:id/et_password")
    REPEAT_PASSWORD_INPUT = (AppiumBy.ID, "com.cubii:id/et_repeat_password")
    BIRTHDAY_INPUT = (AppiumBy.ID, "com.cubii:id/et_birthday")
    TERMS_CHECKBOX = (AppiumBy.ID, "com.cubii:id/chkBoxTerms")
    SIGN_UP_BUTTON = (AppiumBy.ID, "com.cubii:id/btn_create")
    SIGN_UP_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btn_create"]',
    )
    SIGN_UP_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/btn_create")',
    )
    TEXTINPUT_ERROR_ID = "com.cubii:id/textinput_error"
    SIGNUP_FIELD_ERROR_MESSAGES = {
        "first name": "Please enter your first name",
        "last name": "Please enter your last name",
        "email": "Please enter your email",
        "password": "Please enter a password",
        "repeat password": "Please enter repeat password",
        "birthday": "Please select your birthday",
    }
    DATE_PICKER_OK_BUTTON = (AppiumBy.ID, "android:id/button1")

    DATE_PICKER_PREV_MONTH_BUTTONS = (
        (AppiumBy.ACCESSIBILITY_ID, "Previous month"),
        (
            AppiumBy.XPATH,
            '//android.widget.ImageButton[contains(@content-desc,"Previous month")]',
        ),
    )
    DATE_PICKER_DAY_CELLS = (
        AppiumBy.XPATH,
        '//android.view.View[@clickable="true" and @enabled="true" '
        'and string-length(normalize-space(@text))>0 and '
        'translate(@text,"0123456789","")=""]',
    )

    PASSWORD_VALUE = "123123s"

    def launch_application(self):
        self.LOGGER.info("Launching Cubii application explicitly for sign-up scenario.")
        if Settings.APP_PACKAGE and Settings.APP_ACTIVITY:
            try:
                self.driver.execute_script(
                    "mobile: startActivity",
                    {
                        "appPackage": Settings.APP_PACKAGE,
                        "appActivity": Settings.APP_ACTIVITY,
                        "component": f"{Settings.APP_PACKAGE}/{Settings.APP_ACTIVITY}",
                    },
                )
                self.LOGGER.info(
                    "Started app using mobile:startActivity `%s/%s`.",
                    Settings.APP_PACKAGE,
                    Settings.APP_ACTIVITY,
                )
                return
            except WebDriverException as exc:
                self.LOGGER.warning(
                    "mobile:startActivity failed, falling back to activate_app. Error: %s",
                    exc,
                )

        if Settings.APP_PACKAGE:
            self.driver.activate_app(Settings.APP_PACKAGE)
            self.LOGGER.info("Activated app package `%s`.", Settings.APP_PACKAGE)

        self._wait_for_signup_entry_point()

    def _wait_for_signup_entry_point(self):
        """Wait until sign-up card or email form is visible after app launch."""
        self.LOGGER.info("Waiting for sign-up entry screen to load.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)

        def _entry_ready(_driver):
            if _driver.find_elements(*self.FIRST_NAME_INPUT):
                return True
            if _driver.find_elements(*self.SIGN_UP_WITH_EMAIL_CARD):
                return True
            return False

        wait.until(_entry_ready)
        self.LOGGER.info("Sign-up entry screen is ready.")

    def _is_signup_form_visible(self, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(self.FIRST_NAME_INPUT)
            )
            return True
        except TimeoutException:
            return False

    def _click_with_stale_retry(self, locator, timeout=None, label="element", retries=3):
        timeout = timeout or Settings.EXPLICIT_WAIT
        last_err = None
        for attempt in range(1, retries + 1):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    ec.element_to_be_clickable(locator)
                )
                element.click()
                self.LOGGER.info("Clicked `%s` (attempt %s).", label, attempt)
                return
            except (StaleElementReferenceException, TimeoutException) as exc:
                last_err = exc
                self.LOGGER.info(
                    "`%s` click attempt %s did not succeed (%s); retrying.",
                    label,
                    attempt,
                    type(exc).__name__,
                )
                time.sleep(0.5)
        raise AssertionError(
            f"Unable to click `{label}` after {retries} attempts. Last error: {last_err}"
        )

    def open_signup_with_email(self):
        self.LOGGER.info("Opening Sign Up with Email screen.")
        if self._is_signup_form_visible(timeout=2):
            self.LOGGER.info("Sign-up email form already visible; skipping card tap.")
            return

        self._click_with_stale_retry(
            self.SIGN_UP_WITH_EMAIL_CARD,
            label="Sign up with email card",
        )

    def verify_sign_up_button_disabled(self):
        """Assert SIGN UP (`btn_create`) is visible and disabled on an empty form."""
        self.LOGGER.info("Verifying SIGN UP button is disabled when no data is entered.")
        self._scroll_into_view(self.SIGN_UP_BUTTON, max_swipes=6)
        button, label = self._locate_sign_up_button()
        self.LOGGER.info("SIGN UP button located for disabled check (%s).", label)

        try:
            live_enabled = button.is_enabled()
        except WebDriverException as exc:
            raise AssertionError(
                f"Could not read SIGN UP button enabled state: {exc}"
            ) from exc

        enabled_attr = None
        clickable_attr = None
        try:
            enabled_attr = button.get_attribute("enabled")
        except WebDriverException:
            pass
        try:
            clickable_attr = button.get_attribute("clickable")
        except WebDriverException:
            pass

        is_disabled = live_enabled is False or (
            enabled_attr is not None and str(enabled_attr).lower() == "false"
        )
        if not is_disabled:
            raise AssertionError(
                "SIGN UP (`btn_create`) should be disabled when no sign-up data is entered; "
                f"is_enabled={live_enabled!r}, enabled attribute={enabled_attr!r}, "
                f"clickable attribute={clickable_attr!r}."
            )

        self.LOGGER.info(
            "SIGN UP button is disabled as expected (is_enabled=%s, enabled=%s, clickable=%s).",
            live_enabled,
            enabled_attr,
            clickable_attr,
        )

    def _locate_sign_up_button(self, timeout=None):
        wait = WebDriverWait(self.driver, timeout or Settings.EXPLICIT_WAIT)
        last_err = None
        locators = (
            (self.SIGN_UP_BUTTON, "SIGN UP (id)"),
            (self.SIGN_UP_BUTTON_XPATH, "SIGN UP (xpath)"),
            (self.SIGN_UP_BUTTON_UIAUTOMATOR, "SIGN UP (UiAutomator)"),
        )
        for locator, label in locators:
            try:
                element = wait.until(ec.visibility_of_element_located(locator))
                return element, label
            except TimeoutException as exc:
                last_err = exc
        raise AssertionError(
            "SIGN UP (`btn_create`) not visible on sign-up form. "
            f"Last error: {last_err!r}"
        )

    def verify_signup_field_error_message(self, field_label, expected_message):
        """Assert ``textinput_error`` shows the expected validation message for a field."""
        self.LOGGER.info(
            "Verifying sign-up error message for %s: %r",
            field_label,
            expected_message,
        )
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        locators = (
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{self.TEXTINPUT_ERROR_ID}" '
                f'and @text="{expected_message}"]',
                "textinput_error (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("{self.TEXTINPUT_ERROR_ID}")'
                f'.text("{expected_message}")',
                "textinput_error (UiAutomator id+text)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{expected_message}")',
                "textinput_error (UiAutomator text)",
            ),
        )
        last_err = None
        for by, locator, label in locators:
            try:
                element = wait.until(ec.visibility_of_element_located((by, locator)))
                observed = (element.text or "").strip()
                if observed != expected_message:
                    raise AssertionError(
                        f"Sign-up {field_label} error mismatch via {label}: "
                        f"expected {expected_message!r}, got {observed!r}."
                    )
                self.LOGGER.info(
                    "Sign-up %s validation error verified via %s: %r",
                    field_label,
                    label,
                    observed,
                )
                return
            except (TimeoutException, AssertionError) as exc:
                last_err = exc
                continue

        raise AssertionError(
            f"Sign-up {field_label} validation error not visible. "
            f"Expected text: {expected_message!r}. Last error: {last_err!r}"
        )

    def generate_signup_data(self):
        token = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
        first_name = f"Auto{token[:3].title()}"
        last_name = f"User{token[3:].title()}"
        email = f"cubii.qa.{token}@yopmail.com"
        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": self.PASSWORD_VALUE,
            "repeat_password": self.PASSWORD_VALUE,
        }

    def fill_signup_form(self, signup_data):
        self._enter_text(self.FIRST_NAME_INPUT, signup_data["first_name"], "first name")
        self._enter_text(self.LAST_NAME_INPUT, signup_data["last_name"], "last name")
        self._enter_text(self.EMAIL_INPUT, signup_data["email"], "email")
        self._enter_text(self.PASSWORD_INPUT, signup_data["password"], "password")
        self._enter_text(
            self.REPEAT_PASSWORD_INPUT,
            signup_data["repeat_password"],
            "repeat password",
        )

    def select_random_birthdate_and_confirm(self):
        self.LOGGER.info("Selecting a random birthdate from date picker.")
        self._scroll_into_view(self.BIRTHDAY_INPUT, max_swipes=6)
        self.wait.until(ec.element_to_be_clickable(self.BIRTHDAY_INPUT)).click()

        self._scroll_random_months_back(max_months=18)
        day_selected = self._select_random_day_cell()
        self.LOGGER.info("Random birthday day selected: %s", day_selected)
        self.wait.until(ec.element_to_be_clickable(self.DATE_PICKER_OK_BUTTON)).click()

    def accept_terms_only(self):
        self.LOGGER.info("Accepting terms and conditions checkbox.")
        self._scroll_into_view(self.TERMS_CHECKBOX, max_swipes=6)
        terms = self.wait.until(ec.visibility_of_element_located(self.TERMS_CHECKBOX))
        checked = str(terms.get_attribute("checked")).lower() == "true"
        if not checked:
            terms.click()
            self.LOGGER.info("Terms checkbox checked.")
        else:
            self.LOGGER.info("Terms checkbox already checked.")

    def tap_sign_up_button(self):
        self.LOGGER.info("Tapping SIGN UP button (`btn_create`).")
        self._scroll_into_view(self.SIGN_UP_BUTTON, max_swipes=3)
        button, label = self._locate_sign_up_button()
        try:
            if button.is_enabled():
                button.click()
                self.LOGGER.info("Clicked `%s`.", label)
                return
        except WebDriverException as exc:
            self.LOGGER.info(
                "Direct click on `%s` failed (%s); using clickGesture.", label, exc
            )

        rect = button.rect
        x = int(rect["x"] + rect["width"] / 2)
        y = int(rect["y"] + rect["height"] / 2)
        self.driver.execute_script("mobile: clickGesture", {"x": x, "y": y})
        self.LOGGER.info("Tapped `%s` via clickGesture at (%s, %s).", label, x, y)

    def accept_terms_and_signup(self):
        self.LOGGER.info("Accepting terms and tapping SIGN UP.")
        self.accept_terms_only()
        self.tap_sign_up_button()

    def _enter_text(self, locator, value, label):
        self.LOGGER.info("Entering %s.", label)
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def _scroll_random_months_back(self, max_months=18):
        steps = random.randint(0, max_months)
        if steps == 0:
            return

        self.LOGGER.info("Scrolling date picker %s month(s) backwards.", steps)
        short_wait = WebDriverWait(self.driver, 2)
        for _ in range(steps):
            clicked = False
            for locator in self.DATE_PICKER_PREV_MONTH_BUTTONS:
                try:
                    short_wait.until(ec.element_to_be_clickable(locator)).click()
                    clicked = True
                    break
                except TimeoutException:
                    continue
            if not clicked:
                self.LOGGER.info(
                    "Previous month control is not visible; continuing with current month."
                )
                break
            time.sleep(0.1)

    def _select_random_day_cell(self):
        day_cells = self.wait.until(ec.presence_of_all_elements_located(self.DATE_PICKER_DAY_CELLS))
        valid_cells = [
            cell
            for cell in day_cells
            if (cell.text or "").strip().isdigit() and cell.is_enabled() and cell.is_displayed()
        ]
        if not valid_cells:
            raise AssertionError("No selectable day cells found in date picker.")

        target = random.choice(valid_cells)
        chosen_day = target.text.strip()
        target.click()
        return chosen_day

    def _scroll_into_view(self, locator, max_swipes=5):
        for _ in range(max_swipes):
            if self.driver.find_elements(*locator):
                return
            self._swipe_up()
        if not self.driver.find_elements(*locator):
            raise AssertionError(f"Element not found after scrolling: {locator}")

    def _swipe_up(self):
        size = self.driver.get_window_size()
        x = size["width"] // 2
        start_y = int(size["height"] * 0.78)
        end_y = int(size["height"] * 0.35)
        self.driver.swipe(x, start_y, x, end_y, 350)
        time.sleep(0.2)

