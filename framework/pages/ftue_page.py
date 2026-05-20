import logging
import os

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage


class FTUEPage(BasePage):
    LOGGER = logging.getLogger("cubii_ftue_page")

    EMAIL = os.getenv("CUBII_TEST_EMAIL", "neha01@yopmail.com")
    PASSWORD = os.getenv("CUBII_TEST_PASSWORD", "123123s")

    LOGIN_INPUT_COMMON = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/editText"]',
    )
    EMAIL_FALLBACK = (
        AppiumBy.XPATH,
        '//android.widget.EditText[contains(@text,"Email") or contains(@hint,"Email")]',
    )
    PASSWORD_FALLBACK = (
        AppiumBy.XPATH,
        '//android.widget.EditText[contains(@text,"Password") or contains(@hint,"Password")]',
    )
    SIGN_IN_BUTTON = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@resource-id="com.cubii:id/cnsLayoutSignIn"]',
    )

    TURN_ON_BUTTON = (AppiumBy.ID, "com.cubii:id/btnAlarmDetailTurnOn")
    TURN_ON_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/btnAlarmDetailTurnOn")',
    )
    TURN_ON_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btnAlarmDetailTurnOn"]',
    )
    CUBII_PERMISSION_VIEW_XPATH = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View",
    )
    CUBII_PERMISSION_VIEW_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(12)',
    )
    ALARM_TOGGLE = (
        AppiumBy.XPATH,
        "//android.widget.ScrollView/android.view.View[2]/android.view.View/android.view.View[2]",
    )
    ALARM_TOGGLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(9)',
    )
    BACK1_BUTTON = (
        AppiumBy.XPATH,
        "//android.widget.Button",
    )
    BACK1_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button")',
    )
    BACK2_BUTTON = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.Button",
    )
    BACK2_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(0)',
    )

    START_TODAY_BUTTON = (AppiumBy.ID, "com.cubii:id/button")
    START_TODAY_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/button")',
    )
    START_TODAY_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/button"]',
    )
    CLOSE_TAB_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Close tab")
    CLOSE_TAB_BUTTON_ID = (AppiumBy.ID, "com.android.chrome:id/close_button")
    CLOSE_TAB_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.android.chrome:id/close_button")',
    )
    CLOSE_TAB_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Close tab"]',
    )

    NEXT_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.cubii:id/btnNext"]')
    NEXT1_BUTTON = (AppiumBy.ID, "com.cubii:id/btnNextMovedMenu")
    NEXT2_BUTTON = (AppiumBy.ID, "com.cubii:id/btnNextStudio")
    NEXT3_BUTTON = (AppiumBy.ID, "com.cubii:id/btnNextWellnessJournii")
    NEXT4_BUTTON = (AppiumBy.ID, "com.cubii:id/btnNextCommunitii")
    NEXT5_BUTTON = (AppiumBy.ID, "com.cubii:id/btnNextProgress")
    NEXT6_BUTTON = (AppiumBy.ID, "com.cubii:id/cvNext")
    NEXT7_BUTTON = (AppiumBy.ID, "com.cubii:id/btnNextHomeMetric")
    NEXT8_BUTTON = (AppiumBy.ID, "com.cubii:id/btnNextConfigureAvatar")
    NEXT9_BUTTON = (AppiumBy.ID, "com.cubii:id/btnNextConfigureAvatar")
    GOT_IT_BUTTON = (AppiumBy.ID, "com.cubii:id/btnGotIt")
    YES_BUTTON = (AppiumBy.ID, "com.cubii:id/btnYes")
    YES_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/btnYes")',
    )
    YES_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btnYes"]',
    )
    ALLOW_BUTTON = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    ALLOW_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.android.permissioncontroller:id/permission_allow_button")',
    )
    ALLOW_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]',
    )

    PROGRESS_TAB = (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Progress"]')
    COMMUNITII_TAB = (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Communitii"]')
    WELLNESS_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@resource-id="com.cubii:id/viewWellnessJourniiHighlight"]',
    )
    STUDIO_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@resource-id="com.cubii:id/viewStudioHighlight"]',
    )
    HOME_TAB = (
        AppiumBy.XPATH,
        '(//android.widget.ImageView[@resource-id="com.cubii:id/navigation_bar_item_icon_view"])[1]',
    )
    HOME_TAB_CONTENT_DESC = (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Home"]')
    GET_STARTED_BUTTON = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btnGetStarted"]',
    )
    HOME_SCREEN_INDICATOR = (
        AppiumBy.XPATH,
        '//*[contains(@content-desc,"Progress") or @resource-id="com.cubii:id/navigation_bar_item_icon_view"]',
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.wellness_dynamic_handled_once = False

    def wait_for_element(self, locator, timeout=None, visible=True):
        timeout = timeout or Settings.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, timeout)
        condition = ec.visibility_of_element_located(locator) if visible else ec.presence_of_element_located(locator)
        return wait.until(condition)

    def click_if_present(
        self, locator, timeout=3, optional=True, label="element", trigger_dynamic=True
    ):
        try:
            element = self.wait_for_element(locator, timeout=timeout, visible=True)
            element.click()
            self.LOGGER.info("Clicked `%s`.", label)
            if trigger_dynamic:
                self.handle_wellness_journii_webview()
            return True
        except TimeoutException:
            self.LOGGER.info("`%s` not present; continuing.", label)
            if optional:
                return False
            raise

    def click_with_fallbacks(self, locators, timeout=3, label="element", trigger_dynamic=True):
        for locator in locators:
            if self.click_if_present(
                locator,
                timeout=timeout,
                optional=True,
                label=label,
                trigger_dynamic=trigger_dynamic,
            ):
                return True
        self.LOGGER.info("`%s` not found using any configured locator.", label)
        return False

    def launch_application(self):
        self.LOGGER.info("Launching Cubii app for FTUE scenario.")
        if Settings.APP_PACKAGE:
            self.driver.activate_app(Settings.APP_PACKAGE)
            self.LOGGER.info("Activated `%s`.", Settings.APP_PACKAGE)

    def login(self):
        self.LOGGER.info("Starting login flow.")
        self.wait_for_element(self.SIGN_IN_BUTTON, timeout=Settings.EXPLICIT_WAIT)

        email_field = self._resolve_email_field()
        password_field = self._resolve_password_field()
        email_field.clear()
        email_field.send_keys(self.EMAIL)
        self.LOGGER.info("Email entered.")
        password_field.clear()
        password_field.send_keys(self.PASSWORD)
        self.LOGGER.info("Password entered.")

        self.click_if_present(self.SIGN_IN_BUTTON, timeout=6, optional=False, label="SIGN IN")

    def handle_permission_flow(self):
        self.LOGGER.info("Handling permission flow.")
        turn_on_visible = self.click_with_fallbacks(
            [self.TURN_ON_BUTTON, self.TURN_ON_BUTTON_UIAUTOMATOR, self.TURN_ON_BUTTON_XPATH],
            timeout=4,
            label="TURN ON",
        )
        toggle_visible = self.is_element_present(self.ALARM_TOGGLE, timeout=3)

        if not turn_on_visible and not toggle_visible:
            self.LOGGER.info("Permission flow not visible; skipping all permission steps.")
            return

        self.LOGGER.info("Permission flow detected; executing permission handling steps.")
        cubii_clicked = self.click_if_present(
            self.CUBII_PERMISSION_VIEW_XPATH,
            timeout=2,
            optional=True,
            label="Cubii permission view (xpath)",
        )
        if not cubii_clicked:
            self.click_if_present(
                self.CUBII_PERMISSION_VIEW_UIAUTOMATOR,
                timeout=2,
                optional=True,
                label="Cubii permission view (uiautomator)",
            )
        self.handle_wellness_journii_webview()

        try:
            toggle = self.wait_for_element(self.ALARM_TOGGLE, timeout=4)
            checked = str(toggle.get_attribute("checked")).lower() == "true"
            self.LOGGER.info("Alarm toggle checked state: %s", checked)
            if not checked:
                toggle.click()
                self.LOGGER.info("Alarm toggle switched ON.")
        except TimeoutException:
            self.LOGGER.info("Alarm toggle XPath not found; trying UiAutomator locator.")
            try:
                toggle = self.wait_for_element(self.ALARM_TOGGLE_UIAUTOMATOR, timeout=3)
                checked = str(toggle.get_attribute("checked")).lower() == "true"
                self.LOGGER.info("Alarm toggle checked state (UiAutomator): %s", checked)
                if not checked:
                    toggle.click()
                    self.LOGGER.info("Alarm toggle switched ON via UiAutomator locator.")
            except TimeoutException:
                self.LOGGER.info("Alarm toggle screen not shown; skipping.")

        first_back_clicked = self.click_if_present(
            self.BACK1_BUTTON, timeout=2, optional=True, label="permission back 1 (xpath)"
        )
        if not first_back_clicked:
            first_back_clicked = self.click_if_present(
                self.BACK1_BUTTON_UIAUTOMATOR,
                timeout=2,
                optional=True,
                label="permission back 1 (uiautomator)",
            )
        if first_back_clicked:
            self.LOGGER.info("First back button handled on permission flow.")

        second_back_clicked = self.click_if_present(
            self.BACK2_BUTTON, timeout=2, optional=True, label="permission back 2 (xpath)"
        )
        if not second_back_clicked:
            second_back_clicked = self.click_if_present(
                self.BACK2_BUTTON_UIAUTOMATOR,
                timeout=2,
                optional=True,
                label="permission back 2 (uiautomator)",
            )
        if second_back_clicked:
            self.LOGGER.info("Second back button handled on permission flow.")
        elif first_back_clicked:
            self.LOGGER.info("Second back button not visible; falling back to Android back action.")
            self.driver.back()

        self.handle_wellness_journii_webview()

    def handle_wellness_journii_webview(self):
        if self.wellness_dynamic_handled_once:
            self.LOGGER.info(
                "Dynamic Start Today flow already handled once; skipping further checks."
            )
            return False

        start_today_clicked = self.click_with_fallbacks(
            [self.START_TODAY_BUTTON, self.START_TODAY_BUTTON_UIAUTOMATOR, self.START_TODAY_BUTTON_XPATH],
            timeout=2,
            label="Start Today",
            trigger_dynamic=False,
        )
        if start_today_clicked:
            self.LOGGER.info("Dynamic flow detected: clicked Start Today.")
        else:
            self.LOGGER.info("Dynamic flow not detected on this checkpoint.")
            return False

        switched_to_webview = False
        try:
            contexts = self.driver.contexts
            self.LOGGER.info("Available contexts: %s", contexts)
            webview_context = next((ctx for ctx in contexts if "WEBVIEW" in ctx.upper()), None)
            if webview_context:
                self.driver.switch_to.context(webview_context)
                switched_to_webview = True
                self.LOGGER.info("Context switched to `%s`.", webview_context)
            else:
                self.LOGGER.warning("WEBVIEW context not available; trying Close tab in NATIVE_APP.")

            if switched_to_webview:
                self.driver.switch_to.context("NATIVE_APP")
                self.LOGGER.info("Switched back to NATIVE_APP before tapping Close tab.")

            self.click_with_fallbacks(
                [
                    self.CLOSE_TAB_BUTTON,
                    self.CLOSE_TAB_BUTTON_ID,
                    self.CLOSE_TAB_BUTTON_UIAUTOMATOR,
                    self.CLOSE_TAB_BUTTON_XPATH,
                ],
                timeout=5,
                label="Close tab",
                trigger_dynamic=False,
            )
            self.wellness_dynamic_handled_once = True
            self.LOGGER.info("Marked dynamic Start Today flow as handled once.")
            self.LOGGER.info("WebView/Chrome close tab handling completed.")
            return True
        except WebDriverException as exc:
            self.LOGGER.warning("WebView handling failed, continuing execution. Error: %s", exc)
            try:
                self.driver.switch_to.context("NATIVE_APP")
            except WebDriverException:
                pass
            return False

    def handle_ftue_walkthrough(self):
        self.LOGGER.info("Handling FTUE walkthrough Next1 to Next9 sequence.")
        walkthrough_steps = [
            ("Next1", self.NEXT1_BUTTON),
            ("Next2", self.NEXT2_BUTTON),
            ("Next3", self.NEXT3_BUTTON),
            ("Next4", self.NEXT4_BUTTON),
            ("Next5", self.NEXT5_BUTTON),
            ("Next6", self.NEXT6_BUTTON),
            ("Next7", self.NEXT7_BUTTON),
            ("Next8", self.NEXT8_BUTTON),
            ("Next9", self.NEXT9_BUTTON),
        ]
        for index, (label, locator) in enumerate(walkthrough_steps, start=1):
            # Per requirement: skip dynamic Start Today checks from Next2 through Got It.
            trigger_dynamic = index == 1
            self.click_if_present(
                locator,
                timeout=3,
                optional=True,
                label=label,
                trigger_dynamic=trigger_dynamic,
            )
            if trigger_dynamic:
                self.handle_wellness_journii_webview()

        # Fallback for variants that still expose generic btnNext.
        self.click_if_present(
            self.NEXT_BUTTON,
            timeout=2,
            optional=True,
            label="Generic Next fallback",
            trigger_dynamic=False,
        )
        self.click_if_present(
            self.GOT_IT_BUTTON, timeout=4, optional=True, label="Got It", trigger_dynamic=False
        )

    def handle_notification_and_progress_ftue(self):
        self.LOGGER.info("Handling notification permission and Progress FTUE.")
        self.click_with_fallbacks(
            [self.YES_BUTTON, self.YES_BUTTON_UIAUTOMATOR, self.YES_BUTTON_XPATH],
            timeout=4,
            label="Notification Yes",
        )
        self.click_with_fallbacks(
            [self.ALLOW_BUTTON, self.ALLOW_BUTTON_UIAUTOMATOR, self.ALLOW_BUTTON_XPATH],
            timeout=4,
            label="System Allow",
        )

        self.click_if_present(self.PROGRESS_TAB, timeout=6, optional=True, label="Progress tab")
        self.click_if_present(self.NEXT_BUTTON, timeout=4, optional=True, label="Progress Next")
        self.click_if_present(self.GOT_IT_BUTTON, timeout=4, optional=True, label="Progress Got It")
        self.handle_wellness_journii_webview()

    def navigate_wellness_and_return_home(self):
        self.LOGGER.info("Navigating to Wellness Journii and returning Home.")
        self.click_if_present(self.WELLNESS_TAB, timeout=6, optional=True, label="Wellness Journii tab")
        self.click_if_present(self.GET_STARTED_BUTTON, timeout=4, optional=True, label="Get Started")
        self.click_if_present(self.HOME_TAB, timeout=6, optional=True, label="Home tab")

    def validate_tab_navigation(self):
        self.LOGGER.info("Validating navigation across key tabs.")
        for locator, label in [
            (self.HOME_TAB, "Home tab"),
            (self.PROGRESS_TAB, "Progress tab"),
            (self.COMMUNITII_TAB, "Communitii tab"),
            (self.WELLNESS_TAB, "Wellness Journii tab"),
            (self.STUDIO_TAB, "Cubii Studio+ tab"),
        ]:
            self.click_if_present(locator, timeout=6, optional=True, label=label)
            self.handle_wellness_journii_webview()
        self.LOGGER.info("Tab validation completed. Navigating back to Home tab.")
        self.click_if_present(self.HOME_TAB, timeout=6, optional=True, label="Home tab final")
        self.handle_wellness_journii_webview()

    def execute_ftue_dynamic_flow(self):
        self.launch_application()
        self.handle_wellness_journii_webview()
        initial_state = self.ensure_logged_in_or_on_home()
        ftue_present = self.is_ftue_present() if initial_state in ("home", "ftue_only") else None
        if initial_state == "home" and ftue_present:
            self.LOGGER.info("CASE: already_logged_in_ftue_present -> performing FTUE flow.")
        if initial_state == "home" and not ftue_present:
            self.LOGGER.info("CASE: already_logged_in_ftue_absent_skip -> skipping FTUE flow.")
            self.LOGGER.info(
                "User already logged in and no FTUE indicators found. Skipping FTUE flow."
            )
            return
        if initial_state == "ftue_only":
            self.LOGGER.info(
                "CASE: app_reopened_ftue_present_without_login_or_home -> performing FTUE flow."
            )
        self.handle_wellness_journii_webview()
        self.handle_permission_flow()
        self.handle_wellness_journii_webview()
        self.handle_ftue_walkthrough()
        self.handle_wellness_journii_webview()
        self.handle_notification_and_progress_ftue()
        self.handle_wellness_journii_webview()
        self.navigate_wellness_and_return_home()
        self.handle_wellness_journii_webview()
        self.validate_tab_navigation()
        self.handle_wellness_journii_webview()

    def ensure_logged_in_or_on_home(self):
        self.LOGGER.info("Determining initial app state (Home already logged in vs Login screen).")
        for attempt in range(1, 4):
            if self.is_element_present(self.HOME_SCREEN_INDICATOR, timeout=3):
                self.LOGGER.info("User is already logged in; Home screen detected.")
                return "home"

            if self.is_element_present(self.SIGN_IN_BUTTON, timeout=2):
                self.LOGGER.info("Login screen detected; executing login steps.")
                self.login()
                return "login"

            if self.is_ftue_present():
                self.LOGGER.info(
                    "FTUE indicators detected without explicit Home/Login screen (attempt %s).",
                    attempt,
                )
                return "ftue_only"

            self.LOGGER.info(
                "State unresolved on attempt %s; checking dynamic popup and retrying.", attempt
            )
            self.handle_wellness_journii_webview()

        self.LOGGER.info(
            "State remains unresolved after retries; skipping forced login and continuing safely."
        )
        return "unknown"

    def _resolve_email_field(self):
        fields = self.driver.find_elements(*self.LOGIN_INPUT_COMMON)
        if len(fields) >= 2:
            self.LOGGER.info("Using duplicated login locator index 1 for email.")
            return self.get_visible_element_by_index(self.LOGIN_INPUT_COMMON, 1, "login input field")
        self.LOGGER.info("Using email fallback locator.")
        return self.wait_for_element(self.EMAIL_FALLBACK, timeout=5)

    def _resolve_password_field(self):
        fields = self.driver.find_elements(*self.LOGIN_INPUT_COMMON)
        if len(fields) >= 2:
            self.LOGGER.info("Using duplicated login locator index 2 for password.")
            return self.get_visible_element_by_index(self.LOGIN_INPUT_COMMON, 2, "login input field")
        self.LOGGER.info("Using password fallback locator.")
        return self.wait_for_element(self.PASSWORD_FALLBACK, timeout=5)

    def is_element_present(self, locator, timeout=2):
        try:
            self.wait_for_element(locator, timeout=timeout, visible=True)
            return True
        except TimeoutException:
            return False

    def is_ftue_present(self):
        self.LOGGER.info("Checking whether FTUE elements are currently present.")
        ftue_indicators = [
            (self.TURN_ON_BUTTON, "TURN ON"),
            (self.NEXT1_BUTTON, "Next1"),
            (self.NEXT2_BUTTON, "Next2"),
            (self.NEXT3_BUTTON, "Next3"),
            (self.NEXT4_BUTTON, "Next4"),
            (self.NEXT5_BUTTON, "Next5"),
            (self.NEXT6_BUTTON, "Next6"),
            (self.NEXT7_BUTTON, "Next7"),
            (self.NEXT8_BUTTON, "Next8"),
            (self.NEXT9_BUTTON, "Next9"),
            (self.GOT_IT_BUTTON, "Got It"),
            (self.YES_BUTTON, "Notification Yes"),
            (self.GET_STARTED_BUTTON, "Get Started"),
            (self.START_TODAY_BUTTON, "Start Today"),
        ]
        for locator, label in ftue_indicators:
            if self.is_element_present(locator, timeout=1):
                self.LOGGER.info("FTUE indicator detected: `%s`.", label)
                return True
        self.LOGGER.info("No FTUE indicators detected.")
        return False

