import base64
import logging
import os
import struct
import time
import zlib

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage
from framework.pages.non_ble_connection import NonBleConnectionPage


class SettingsPage(BasePage):
    """App Settings screen — theme (Select Style) and cross-tab dark-mode checks."""

    LOGGER = logging.getLogger("cubii_settings_page")

    SETTINGS_SCREEN_TITLE = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title" and @text="Settings"]',
    )
    SETTINGS_SCREEN_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/toolbar_title").text("Settings")',
    )

    THEME_SEGMENT_GROUP = (AppiumBy.ID, "com.cubii:id/sbg_theme")
    THEME_SEGMENT_GROUP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/sbg_theme"]',
    )

    DARK_MODE_OPTION = (
        AppiumBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/sbg_theme"]'
        "/android.widget.FrameLayout/android.widget.LinearLayout[3]/android.view.View[1]",
    )
    DARK_MODE_OPTION_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(5)',
    )

    LIGHT_MODE_OPTION = (
        AppiumBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/sbg_theme"]'
        "/android.widget.FrameLayout/android.widget.LinearLayout[3]/android.view.View[2]",
    )
    LIGHT_MODE_OPTION_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(6)',
    )

    DISTANCE_SEGMENT_GROUP = (AppiumBy.ID, "com.cubii:id/sbg_distance")
    DISTANCE_SEGMENT_GROUP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/sbg_distance"]',
    )
    KMS_OPTION = (
        AppiumBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/sbg_distance"]'
        "/android.widget.FrameLayout/android.widget.LinearLayout[3]/android.view.View[1]",
    )
    KMS_OPTION_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(10)',
    )
    MILES_OPTION = (
        AppiumBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/sbg_distance"]'
        "/android.widget.FrameLayout/android.widget.LinearLayout[3]/android.view.View[2]",
    )
    MILES_OPTION_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(11)',
    )

    METRIC_TITLE_POPUP = (AppiumBy.ID, "com.cubii:id/txtMetricTitle")
    METRIC_TITLE_POPUP_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/txtMetricTitle")',
    )
    METRIC_TITLE_POPUP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/txtMetricTitle"]',
    )

    METRIC_CHANGED_DONE_BUTTON = (AppiumBy.ID, "com.cubii:id/btnMetricChangedDone")
    METRIC_CHANGED_DONE_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/btnMetricChangedDone")',
    )
    METRIC_CHANGED_DONE_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btnMetricChangedDone"]',
    )
    METRIC_CHANGED_DONE_BUTTON_CLASS = (AppiumBy.CLASS_NAME, "android.widget.Button")

    BACK_BUTTON_NAVIGATE_UP = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    BACK_BUTTON_NAVIGATE_UP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Navigate up"]',
    )
    BACK_BUTTON_NAVIGATE_UP_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Navigate up")',
    )
    BACK_BUTTON_CLASS_NAME = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")

    CONTENT_ROOT_LOCATORS = (
        (AppiumBy.ID, "android:id/content"),
        (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]',
        ),
        (AppiumBy.ID, "com.cubii:id/coordinator"),
        (AppiumBy.ID, "com.cubii:id/toolbar"),
        (
            AppiumBy.XPATH,
            '//com.google.android.material.bottomnavigation.BottomNavigationView',
        ),
        (
            AppiumBy.XPATH,
            '//*[contains(@resource-id, "navigation_bar")]',
        ),
    )

    PRIMARY_TEXT_LOCATORS = (
        (
            AppiumBy.XPATH,
            '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title"]',
        ),
        (
            AppiumBy.XPATH,
            '//android.widget.TextView[@resource-id="com.cubii:id/textView22"]',
        ),
        (
            AppiumBy.XPATH,
            '//android.widget.TextView[@resource-id="com.cubii:id/iv_logo"]/../..',
        ),
    )

    # Bottom-nav Home tabs — sample header chrome (white vs #262626).
    THEME_CHROME_SAMPLE_REGIONS = (
        (0.05, 0.11, 0.05, 0.95),
        (0.05, 0.10, 0.02, 0.18),
        (0.05, 0.10, 0.82, 0.98),
    )

    # More / My Account — teal header is bright in both themes; sample the dark menu cards.
    THEME_MORE_MENU_SAMPLE_REGIONS = (
        (0.38, 0.52, 0.12, 0.88),
        (0.52, 0.68, 0.12, 0.88),
        (0.68, 0.82, 0.12, 0.88),
    )
    THEME_MY_ACCOUNT_SAMPLE_REGIONS = (
        (0.38, 0.52, 0.08, 0.92),
        (0.52, 0.66, 0.08, 0.92),
        (0.66, 0.80, 0.08, 0.92),
    )
    # My Account light mode — sample white/light card bodies (not teal header).
    THEME_MY_ACCOUNT_LIGHT_SAMPLE_REGIONS = (
        (0.42, 0.56, 0.14, 0.86),
        (0.56, 0.70, 0.14, 0.86),
        (0.70, 0.82, 0.14, 0.86),
    )

    # Settings list body (below toolbar) — dark list background when DARK theme is on.
    THEME_SETTINGS_BODY_SAMPLE_REGIONS = (
        (0.14, 0.22, 0.06, 0.94),
        (0.28, 0.38, 0.06, 0.94),
        (0.42, 0.52, 0.06, 0.94),
    )

    MORE_MENU_LIST = (AppiumBy.ID, "com.cubii:id/rv_more")
    MORE_MENU_TITLE = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title" and @text="More"]',
    )
    MORE_MENU_PROFILE_NAME = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/textView22"]',
    )
    MY_ACCOUNT_TITLE = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title" and @text="My Account"]',
    )
    DARK_THEME_LABEL = (
        AppiumBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/sbg_theme"]'
        '//*[@text="DARK"]',
    )
    LIGHT_THEME_LABEL = (
        AppiumBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/sbg_theme"]'
        '//*[@text="LIGHT"]',
    )
    SELECT_STYLE_LABEL = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Select Style"]',
    )

    def __init__(self, driver, non_ble_connection_page=None):
        super().__init__(driver)
        self._non_ble = non_ble_connection_page or NonBleConnectionPage(driver)

    def verify_settings_screen_visible(self) -> None:
        """Assert the Settings screen toolbar title is visible."""
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator in (
            self.SETTINGS_SCREEN_TITLE,
            self.SETTINGS_SCREEN_TITLE_UIAUTOMATOR,
        ):
            try:
                wait.until(ec.visibility_of_element_located(locator))
                self.LOGGER.info("Settings screen verified via `%s`.", locator[1])
                return
            except TimeoutException:
                continue
        raise AssertionError("Settings screen title was not visible.")

    def tap_dark_mode(self) -> None:
        """Tap the DARK option in Select Style (`sbg_theme`)."""
        self.LOGGER.info("Tapping DARK theme option on Settings screen.")
        self.verify_settings_screen_visible()
        for locator in (
            self.DARK_MODE_OPTION,
            self.DARK_MODE_OPTION_UIAUTOMATOR,
            self.THEME_SEGMENT_GROUP,
            self.THEME_SEGMENT_GROUP_XPATH,
        ):
            try:
                element = self.wait.until(ec.element_to_be_clickable(locator))
                element.click()
                time.sleep(float(os.getenv("CUBII_AFTER_DARK_MODE_TAP_SEC", "1.0")))
                self.LOGGER.info("DARK theme option tapped via `%s`.", locator[1])
                break
            except TimeoutException:
                self.LOGGER.info(
                    "DARK theme locator `%s` failed; trying next.", locator[1]
                )
        else:
            raise TimeoutException(
                "DARK theme option could not be located on the Settings screen."
            )

        if not self._current_screen_uses_dark_theme(
            "Settings",
            sample_regions=self.THEME_SETTINGS_BODY_SAMPLE_REGIONS,
        ):
            raise AssertionError(
                "Dark theme was not applied on the Settings screen after tapping DARK."
            )
        self.LOGGER.info("Dark theme confirmed on Settings screen after DARK tap.")

    def tap_light_mode(self) -> None:
        """Tap the LIGHT option in Select Style (`sbg_theme`)."""
        self.LOGGER.info("Tapping LIGHT theme option on Settings screen.")
        self.verify_settings_screen_visible()
        for locator in (
            self.LIGHT_MODE_OPTION,
            self.LIGHT_MODE_OPTION_UIAUTOMATOR,
            self.THEME_SEGMENT_GROUP,
            self.THEME_SEGMENT_GROUP_XPATH,
        ):
            try:
                element = self.wait.until(ec.element_to_be_clickable(locator))
                element.click()
                time.sleep(float(os.getenv("CUBII_AFTER_LIGHT_MODE_TAP_SEC", "1.0")))
                self.LOGGER.info("LIGHT theme option tapped via `%s`.", locator[1])
                break
            except TimeoutException:
                self.LOGGER.info(
                    "LIGHT theme locator `%s` failed; trying next.", locator[1]
                )
        else:
            raise TimeoutException(
                "LIGHT theme option could not be located on the Settings screen."
            )

        if not self._current_screen_uses_light_theme(
            "Settings",
            sample_regions=self.THEME_SETTINGS_BODY_SAMPLE_REGIONS,
        ):
            raise AssertionError(
                "Light theme was not applied on the Settings screen after tapping LIGHT."
            )
        self.LOGGER.info("Light theme confirmed on Settings screen after LIGHT tap.")

    def tap_kms(self) -> None:
        """Tap the KMS option in Distance Unit (`sbg_distance`)."""
        self.LOGGER.info("Tapping KMS distance unit option on Settings screen.")
        self.verify_settings_screen_visible()
        for locator in (
            self.KMS_OPTION,
            self.KMS_OPTION_UIAUTOMATOR,
            self.DISTANCE_SEGMENT_GROUP,
            self.DISTANCE_SEGMENT_GROUP_XPATH,
        ):
            try:
                element = self.wait.until(ec.element_to_be_clickable(locator))
                element.click()
                time.sleep(float(os.getenv("CUBII_AFTER_KMS_TAP_SEC", "1.0")))
                self.LOGGER.info("KMS distance unit option tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "KMS distance unit locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException(
            "KMS distance unit option could not be located on the Settings screen."
        )

    def tap_miles(self) -> None:
        """Tap the Miles option in Distance Unit (`sbg_distance`)."""
        self.LOGGER.info("Tapping Miles distance unit option on Settings screen.")
        self.verify_settings_screen_visible()
        for locator in (
            self.MILES_OPTION,
            self.MILES_OPTION_UIAUTOMATOR,
            self.DISTANCE_SEGMENT_GROUP,
            self.DISTANCE_SEGMENT_GROUP_XPATH,
        ):
            try:
                element = self.wait.until(ec.element_to_be_clickable(locator))
                element.click()
                time.sleep(float(os.getenv("CUBII_AFTER_MILES_TAP_SEC", "1.0")))
                self.LOGGER.info(
                    "Miles distance unit option tapped via `%s`.", locator[1]
                )
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Miles distance unit locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException(
            "Miles distance unit option could not be located on the Settings screen."
        )

    def verify_distance_unit_popup_miles_to_km(self) -> None:
        """Assert the distance-unit confirmation popup title is Miles -> KM."""
        expected = (
            os.getenv("CUBII_DISTANCE_UNIT_POPUP_TITLE", "Miles -> KM") or "Miles -> KM"
        ).strip()
        self.LOGGER.info(
            "Verifying distance unit popup title (`txtMetricTitle`) is %r.", expected
        )
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator in (
            self.METRIC_TITLE_POPUP,
            self.METRIC_TITLE_POPUP_UIAUTOMATOR,
            self.METRIC_TITLE_POPUP_XPATH,
        ):
            try:
                element = wait.until(ec.visibility_of_element_located(locator))
                title_text = (
                    (element.text or "")
                    + " "
                    + (element.get_attribute("text") or "")
                ).strip()
                if not title_text:
                    continue
                normalized = " ".join(title_text.split())
                if expected.lower() in normalized.lower() or self._matches_miles_to_km(
                    normalized
                ):
                    self.LOGGER.info(
                        "Distance unit popup verified via `%s`: %r.",
                        locator[1],
                        title_text,
                    )
                    return
                raise AssertionError(
                    f"Distance unit popup title was {title_text!r}; expected {expected!r}."
                )
            except TimeoutException:
                self.LOGGER.info(
                    "Distance unit popup locator `%s` failed; trying next.", locator[1]
                )
            except AssertionError:
                raise
        raise AssertionError(
            f"Distance unit popup title (`txtMetricTitle`) was not visible with {expected!r}."
        )

    def verify_distance_unit_popup_km_to_miles(self) -> None:
        """Assert the distance-unit confirmation popup title is KM -> Miles."""
        expected = (
            os.getenv("CUBII_DISTANCE_UNIT_POPUP_KM_TO_MILES_TITLE", "KM -> Miles")
            or "KM -> Miles"
        ).strip()
        self.LOGGER.info(
            "Verifying distance unit popup title (`txtMetricTitle`) is %r.", expected
        )
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator in (
            self.METRIC_TITLE_POPUP,
            self.METRIC_TITLE_POPUP_UIAUTOMATOR,
            self.METRIC_TITLE_POPUP_XPATH,
        ):
            try:
                element = wait.until(ec.visibility_of_element_located(locator))
                title_text = (
                    (element.text or "")
                    + " "
                    + (element.get_attribute("text") or "")
                ).strip()
                if not title_text:
                    continue
                normalized = " ".join(title_text.split())
                if expected.lower() in normalized.lower() or self._matches_km_to_miles(
                    normalized
                ):
                    self.LOGGER.info(
                        "Distance unit popup verified via `%s`: %r.",
                        locator[1],
                        title_text,
                    )
                    return
                raise AssertionError(
                    f"Distance unit popup title was {title_text!r}; expected {expected!r}."
                )
            except TimeoutException:
                self.LOGGER.info(
                    "Distance unit popup locator `%s` failed; trying next.", locator[1]
                )
            except AssertionError:
                raise
        raise AssertionError(
            f"Distance unit popup title (`txtMetricTitle`) was not visible with {expected!r}."
        )

    @staticmethod
    def _matches_miles_to_km(title_text: str) -> bool:
        lowered = title_text.lower()
        return "miles" in lowered and ("km" in lowered or "kms" in lowered)

    @staticmethod
    def _matches_km_to_miles(title_text: str) -> bool:
        lowered = title_text.lower()
        return ("km" in lowered or "kms" in lowered or "lm" in lowered) and (
            "miles" in lowered
        )

    def tap_metric_changed_done_ok(self) -> None:
        """Tap OK on the distance-unit confirmation popup (`btnMetricChangedDone`)."""
        self.LOGGER.info("Tapping OK on distance unit confirmation popup.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator in (
            self.METRIC_CHANGED_DONE_BUTTON,
            self.METRIC_CHANGED_DONE_BUTTON_UIAUTOMATOR,
            self.METRIC_CHANGED_DONE_BUTTON_XPATH,
            self.METRIC_CHANGED_DONE_BUTTON_CLASS,
        ):
            try:
                element = wait.until(ec.element_to_be_clickable(locator))
                element.click()
                time.sleep(float(os.getenv("CUBII_AFTER_METRIC_POPUP_OK_SEC", "0.8")))
                self.LOGGER.info(
                    "Distance unit popup OK tapped via `%s`.", locator[1]
                )
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Distance unit popup OK locator `%s` failed; trying next.",
                    locator[1],
                )
        raise TimeoutException(
            "OK button (`btnMetricChangedDone`) could not be located on the popup."
        )

    def tap_back_button(self) -> None:
        """Tap toolbar Navigate up (back)."""
        self.LOGGER.info("Tapping back button (`Navigate up`).")
        for locator in (
            self.BACK_BUTTON_NAVIGATE_UP,
            self.BACK_BUTTON_NAVIGATE_UP_XPATH,
            self.BACK_BUTTON_NAVIGATE_UP_UIAUTOMATOR,
            self.BACK_BUTTON_CLASS_NAME,
        ):
            try:
                element = self.wait.until(ec.element_to_be_clickable(locator))
                element.click()
                time.sleep(float(os.getenv("CUBII_AFTER_SETTINGS_BACK_SEC", "0.6")))
                self.LOGGER.info("Back button tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Back button locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException(
            "Back button (`Navigate up`) could not be located."
        )

    def verify_more_screen_dark_mode(self) -> None:
        """Assert the More menu is visible and rendered with dark-theme surfaces."""
        self.LOGGER.info("Verifying More menu screen is in dark mode.")
        self._assert_more_screen_visible()
        self._assert_menu_list_visible(self.MORE_MENU_LIST, "More menu list (`rv_more`)")
        if not self._current_screen_uses_dark_theme(
            "More menu",
            sample_regions=self.THEME_MORE_MENU_SAMPLE_REGIONS,
        ):
            raise AssertionError(
                "More menu screen does not appear to be in dark mode."
            )
        self.LOGGER.info("More menu dark mode verified.")

    def verify_my_account_screen_dark_mode(self, home_page) -> None:
        """Assert My Account is visible and rendered with dark-theme surfaces."""
        self.LOGGER.info("Verifying My Account screen is in dark mode.")
        home_page.verify_my_account_screen_visible()
        self._assert_screen_title_visible(self.MY_ACCOUNT_TITLE, "My Account")
        if not self._current_screen_uses_dark_theme(
            "My Account",
            sample_regions=self.THEME_MY_ACCOUNT_SAMPLE_REGIONS,
            max_luminance=float(
                os.getenv("CUBII_MY_ACCOUNT_DARK_LUMINANCE_MAX", "85")
            ),
        ):
            raise AssertionError(
                "My Account screen does not appear to be in dark mode."
            )
        self.LOGGER.info("My Account dark mode verified.")

    def verify_settings_screen_dark_mode(self) -> None:
        """Assert Settings is open, DARK is selected, and the list uses dark surfaces."""
        self.LOGGER.info("Verifying Settings screen is in dark mode.")
        self.verify_settings_screen_visible()
        self._assert_dark_theme_segment_selected()
        if not self._current_screen_uses_dark_theme(
            "Settings",
            sample_regions=self.THEME_SETTINGS_BODY_SAMPLE_REGIONS,
        ):
            raise AssertionError(
                "Settings screen does not appear to be in dark mode."
            )
        self.LOGGER.info("Settings dark mode verified (DARK selected + dark surfaces).")

    def verify_my_account_screen_light_mode(self, home_page) -> None:
        """Assert My Account is visible and rendered with light-theme surfaces."""
        self.LOGGER.info("Verifying My Account screen is in light mode.")
        home_page.verify_my_account_screen_visible()
        self._assert_screen_title_visible(self.MY_ACCOUNT_TITLE, "My Account")
        min_light = float(os.getenv("CUBII_MY_ACCOUNT_LIGHT_LUMINANCE_MIN", "100"))
        dark_max = float(os.getenv("CUBII_MY_ACCOUNT_DARK_LUMINANCE_MAX", "85"))
        if self._current_screen_uses_light_theme(
            "My Account",
            sample_regions=self.THEME_MY_ACCOUNT_LIGHT_SAMPLE_REGIONS,
            min_luminance=min_light,
        ):
            self.LOGGER.info("My Account light mode verified.")
            return

        luminance = self._screenshot_luminance_for_regions(
            self.THEME_MY_ACCOUNT_LIGHT_SAMPLE_REGIONS
        )
        if luminance is not None and luminance > dark_max:
            self.LOGGER.info(
                "My Account light mode verified via fallback: luminance=%.1f > dark max=%.1f.",
                luminance,
                dark_max,
            )
            return

        raise AssertionError(
            "My Account screen does not appear to be in light mode."
        )

    def verify_settings_screen_light_mode(self) -> None:
        """Assert Settings is open, LIGHT is selected, and the list uses light surfaces."""
        self.LOGGER.info("Verifying Settings screen is in light mode.")
        self.verify_settings_screen_visible()
        self._assert_light_theme_segment_selected()
        if not self._current_screen_uses_light_theme(
            "Settings",
            sample_regions=self.THEME_SETTINGS_BODY_SAMPLE_REGIONS,
        ):
            raise AssertionError(
                "Settings screen does not appear to be in light mode."
            )
        self.LOGGER.info("Settings light mode verified (LIGHT selected + light surfaces).")

    def _assert_screen_title_visible(self, locator, label: str) -> None:
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        try:
            wait.until(ec.visibility_of_element_located(locator))
            self.LOGGER.info("%s screen title verified via `%s`.", label, locator[1])
        except TimeoutException as exc:
            raise AssertionError(f"{label} screen title was not visible.") from exc

    def _assert_more_screen_visible(self) -> None:
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator, label in (
            (self.MORE_MENU_TITLE, "More toolbar title"),
            (self.MORE_MENU_PROFILE_NAME, "More menu profile name"),
        ):
            try:
                wait.until(ec.visibility_of_element_located(locator))
                self.LOGGER.info("More menu header verified via %s.", label)
                return
            except TimeoutException:
                continue
        raise AssertionError(
            "More menu screen was not visible (expected More title or profile name)."
        )

    def _assert_menu_list_visible(self, locator, label: str) -> None:
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        try:
            wait.until(ec.visibility_of_element_located(locator))
            self.LOGGER.info("%s verified via `%s`.", label, locator[1])
        except TimeoutException as exc:
            raise AssertionError(f"{label} was not visible.") from exc

    def _assert_dark_theme_segment_selected(self) -> None:
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator in (
            self.DARK_THEME_LABEL,
            self.SELECT_STYLE_LABEL,
            self.THEME_SEGMENT_GROUP,
            self.THEME_SEGMENT_GROUP_XPATH,
        ):
            try:
                wait.until(ec.visibility_of_element_located(locator))
                self.LOGGER.info(
                    "Settings dark theme control verified via `%s`.", locator[1]
                )
                return
            except TimeoutException:
                continue
        raise AssertionError(
            "Settings Select Style / DARK theme segment was not visible."
        )

    def _assert_light_theme_segment_selected(self) -> None:
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator in (
            self.LIGHT_THEME_LABEL,
            self.SELECT_STYLE_LABEL,
            self.THEME_SEGMENT_GROUP,
            self.THEME_SEGMENT_GROUP_XPATH,
        ):
            try:
                wait.until(ec.visibility_of_element_located(locator))
                self.LOGGER.info(
                    "Settings light theme control verified via `%s`.", locator[1]
                )
                return
            except TimeoutException:
                continue
        raise AssertionError(
            "Settings Select Style / LIGHT theme segment was not visible."
        )

    def verify_dark_mode_on_all_tabs(
        self,
        *,
        communitii_page,
        wellness_journii_page,
        cubii_studio_page,
        ftue_page=None,
    ) -> None:
        """
        Confirm dark theme on Home, Progress, Communitii, Wellness Journii,
        and Cubii Studio bottom-nav tabs.
        """
        self.LOGGER.info("Verifying dark theme on all bottom-nav tabs.")

        tab_openers = (
            ("Home", lambda: self._non_ble.open_home_tab()),
            ("Progress", lambda: self._non_ble.open_in_progress_tab()),
            ("Communitii", lambda: communitii_page.open_communitii_tab()),
            (
                "Wellness Journii",
                lambda: self._open_wellness_tab(wellness_journii_page, ftue_page),
            ),
            ("Cubii Studio", lambda: cubii_studio_page.open_cubii_studio_tab()),
        )

        failures: list[str] = []
        for tab_name, open_tab in tab_openers:
            open_tab()
            pause = float(os.getenv("CUBII_AFTER_TAB_THEME_CHECK_SEC", "1.0"))
            time.sleep(pause)
            if self._current_screen_uses_dark_theme(tab_name):
                self.LOGGER.info("Dark theme verified on `%s` tab.", tab_name)
                continue
            failures.append(tab_name)

        if failures:
            raise AssertionError(
                "Dark theme was not verified on tab(s): " + ", ".join(failures) + "."
            )
        self.LOGGER.info("Dark theme verified on all bottom-nav tabs.")

    def _open_wellness_tab(self, wellness_journii_page, ftue_page) -> None:
        wellness_journii_page.open_wellness_journii_tab()
        if ftue_page is not None and hasattr(ftue_page, "handle_wellness_journii_webview"):
            ftue_page.handle_wellness_journii_webview()

    def _current_screen_uses_dark_theme(
        self,
        screen_label: str,
        *,
        sample_regions: tuple[tuple[float, float, float, float], ...] | None = None,
        max_luminance: float | None = None,
    ) -> bool:
        regions = sample_regions or self.THEME_CHROME_SAMPLE_REGIONS
        threshold = max_luminance if max_luminance is not None else float(
            os.getenv("CUBII_DARK_THEME_LUMINANCE_MAX", "140")
        )
        min_text_lum = float(os.getenv("CUBII_DARK_THEME_TEXT_LUMINANCE_MIN", "180"))

        def screenshot_probe() -> float | None:
            return self._screenshot_luminance_for_regions(regions)

        def get_colors_probe() -> float | None:
            return self._sample_screen_luminance_for_regions(regions)

        checks = (
            ("screenshot", screenshot_probe),
            ("getColors_screen", get_colors_probe),
            ("getColors_element", self._sample_content_element_luminance),
            ("surface_background", self._surface_background_luminance),
        )
        for strategy, probe in checks:
            luminance = probe()
            if luminance is None:
                continue
            is_dark = luminance < threshold
            self.LOGGER.info(
                "%s screen [%s] luminance=%.1f (max dark=%.1f) -> dark=%s",
                screen_label,
                strategy,
                luminance,
                threshold,
                is_dark,
            )
            return is_dark

        if self._screen_has_light_primary_text(min_text_lum):
            self.LOGGER.info(
                "%s screen dark theme inferred from light primary text color.",
                screen_label,
            )
            return True

        self.LOGGER.warning(
            "%s screen: no dark-theme signal detected with any strategy.", screen_label
        )
        return False

    def _current_screen_uses_light_theme(
        self,
        screen_label: str,
        *,
        sample_regions: tuple[tuple[float, float, float, float], ...] | None = None,
        min_luminance: float | None = None,
    ) -> bool:
        regions = sample_regions or self.THEME_CHROME_SAMPLE_REGIONS
        min_light = min_luminance if min_luminance is not None else float(
            os.getenv("CUBII_LIGHT_THEME_LUMINANCE_MIN", "140")
        )

        def screenshot_probe() -> float | None:
            return self._screenshot_luminance_for_regions(regions)

        def get_colors_probe() -> float | None:
            return self._sample_screen_luminance_for_regions(regions)

        checks = (
            ("screenshot", screenshot_probe),
            ("getColors_screen", get_colors_probe),
            ("getColors_element", self._sample_content_element_luminance),
            ("surface_background", self._surface_background_luminance),
        )
        for strategy, probe in checks:
            luminance = probe()
            if luminance is None:
                continue
            is_light = luminance >= min_light
            self.LOGGER.info(
                "%s screen [%s] luminance=%.1f (min light=%.1f) -> light=%s",
                screen_label,
                strategy,
                luminance,
                min_light,
                is_light,
            )
            return is_light

        self.LOGGER.warning(
            "%s screen: no light-theme signal detected with any strategy.", screen_label
        )
        return False

    def _screenshot_luminance_for_regions(
        self,
        regions: tuple[tuple[float, float, float, float], ...],
    ) -> float | None:
        try:
            png_bytes = base64.b64decode(self.driver.get_screenshot_as_base64())
        except Exception as exc:
            self.LOGGER.debug("Screenshot capture failed: %s", exc)
            return None

        grid = self._decode_png_rgb_grid(png_bytes)
        if not grid:
            return None

        width, height, rows = grid
        pixels = self._sample_theme_chrome_pixels(
            width,
            height,
            rows,
            regions=regions,
            max_samples=int(os.getenv("CUBII_DARK_THEME_SCREENSHOT_SAMPLES", "120")),
        )
        if not pixels:
            return None
        luminances = [self._luminance(*rgb) for rgb in pixels]
        return self._median(luminances)

    def _sample_screen_luminance_for_regions(
        self,
        regions: tuple[tuple[float, float, float, float], ...],
    ) -> float | None:
        size = self.driver.get_window_size()
        width = int(size["width"])
        height = int(size["height"])
        luminances: list[float] = []
        for top_ratio, bottom_ratio, left_ratio, right_ratio in regions:
            left = int(width * ((left_ratio + right_ratio) / 2))
            top = int(height * ((top_ratio + bottom_ratio) / 2))
            value = self._sample_point_luminance(left, top)
            if value is not None:
                luminances.append(value)
        if not luminances:
            return None
        return sum(luminances) / len(luminances)

    def _sample_screen_luminance(self) -> float | None:
        return self._sample_screen_luminance_for_regions(self.THEME_CHROME_SAMPLE_REGIONS)

    def _sample_content_element_luminance(self) -> float | None:
        for by, locator in self.CONTENT_ROOT_LOCATORS:
            try:
                element = self.driver.find_element(by, locator)
            except Exception:
                continue
            luminance = self._luminance_from_get_colors_result(
                self._execute_get_colors(element=element)
            )
            if luminance is not None:
                return luminance
        return None

    def _surface_background_luminance(self) -> float | None:
        threshold = float(os.getenv("CUBII_DARK_THEME_LUMINANCE_MAX", "140"))
        dark_surfaces = 0
        checked = 0
        for by, locator in self.CONTENT_ROOT_LOCATORS:
            try:
                element = self.driver.find_element(by, locator)
            except Exception:
                continue
            for attr in ("background", "backgroundColor", "backgroundTint"):
                try:
                    raw = element.get_attribute(attr) or ""
                except Exception:
                    continue
                if not raw:
                    continue
                rgb = self._parse_hex_color(raw)
                if not rgb:
                    continue
                checked += 1
                if self._luminance(*rgb) < threshold:
                    dark_surfaces += 1
        if checked == 0:
            return None
        if dark_surfaces > 0:
            return (threshold - 1.0)
        return threshold + 1.0

    def _screen_has_light_primary_text(self, min_text_luminance: float) -> bool:
        for by, locator in self.PRIMARY_TEXT_LOCATORS:
            try:
                element = self.driver.find_element(by, locator)
                if not element.is_displayed():
                    continue
            except Exception:
                continue
            for attr in ("textColor", "color", "drawableTint"):
                try:
                    raw = element.get_attribute(attr) or ""
                except Exception:
                    continue
                rgb = self._parse_hex_color(raw)
                if rgb and self._luminance(*rgb) >= min_text_luminance:
                    return True
        return False

    def _sample_point_luminance(self, left: int, top: int) -> float | None:
        return self._luminance_from_get_colors_result(
            self._execute_get_colors(left=left, top=top)
        )

    def _execute_get_colors(
        self,
        *,
        left: int | None = None,
        top: int | None = None,
        element=None,
    ) -> object | None:
        if element is not None:
            payloads = (
                {"element": element, "feature": "pixel"},
                {"element": element},
                {"element": element.id},
            )
        else:
            payloads = (
                {"left": left, "top": top, "width": 1, "height": 1},
                {"left": left, "top": top, "width": 1, "height": 1, "feature": "pixel"},
            )
        for payload in payloads:
            try:
                return self.driver.execute_script("mobile: getColors", payload)
            except Exception as exc:
                self.LOGGER.debug("mobile:getColors payload=%s failed: %s", payload, exc)
        return None

    def _luminance_from_get_colors_result(self, result: object | None) -> float | None:
        if not result:
            return None

        entries: list[object] = []
        if isinstance(result, dict):
            colors = result.get("colors")
            if isinstance(colors, list):
                entries.extend(colors)
            for key in ("hex", "color", "value"):
                if key in result:
                    entries.append(result[key])
        elif isinstance(result, list):
            entries.extend(result)

        luminances: list[float] = []
        for entry in entries:
            hex_value = ""
            if isinstance(entry, str):
                hex_value = entry
            elif isinstance(entry, dict):
                hex_value = (
                    entry.get("hex")
                    or entry.get("color")
                    or entry.get("value")
                    or ""
                )
            rgb = self._parse_hex_color(str(hex_value))
            if rgb:
                luminances.append(self._luminance(*rgb))

        if not luminances:
            return None
        return sum(luminances) / len(luminances)

    def _sample_theme_chrome_pixels(
        self,
        width: int,
        height: int,
        rows: list[list[tuple[int, int, int]]],
        *,
        regions: tuple[tuple[float, float, float, float], ...],
        max_samples: int,
    ) -> list[tuple[int, int, int]]:
        pixels: list[tuple[int, int, int]] = []
        for top_ratio, bottom_ratio, left_ratio, right_ratio in regions:
            row_start = int(height * top_ratio)
            row_end = int(height * bottom_ratio)
            col_start = int(width * left_ratio)
            col_end = int(width * right_ratio)
            step_y = max(1, (row_end - row_start) // 4 or 1)
            step_x = max(1, (col_end - col_start) // 8 or 1)

            for row_idx in range(row_start, min(row_end, len(rows)), step_y):
                row = rows[row_idx]
                for col_idx in range(col_start, min(col_end, len(row)), step_x):
                    pixels.append(row[col_idx])
                    if len(pixels) >= max_samples:
                        return pixels
        return pixels

    @staticmethod
    def _decode_png_rgb_grid(
        png_bytes: bytes,
    ) -> tuple[int, int, list[list[tuple[int, int, int]]]] | None:
        if not png_bytes.startswith(b"\x89PNG\r\n\x1a\n"):
            return None

        width = height = 0
        bit_depth = 0
        color_type = 0
        idat = bytearray()
        offset = 8
        while offset + 8 <= len(png_bytes):
            length = struct.unpack(">I", png_bytes[offset : offset + 4])[0]
            chunk_type = png_bytes[offset + 4 : offset + 8]
            data = png_bytes[offset + 8 : offset + 8 + length]
            if chunk_type == b"IHDR":
                width, height, bit_depth, color_type, *_ = struct.unpack(
                    ">IIBBBBB", data
                )
            elif chunk_type == b"IDAT":
                idat.extend(data)
            elif chunk_type == b"IEND":
                break
            offset += 12 + length

        if width <= 0 or height <= 0 or bit_depth != 8 or color_type not in (2, 6):
            return None

        bytes_per_pixel = 3 if color_type == 2 else 4
        stride = width * bytes_per_pixel
        try:
            raw = zlib.decompress(bytes(idat))
        except zlib.error:
            return None

        rows: list[list[tuple[int, int, int]]] = []
        pos = 0
        prev_row = [0] * stride
        for _row_idx in range(height):
            if pos >= len(raw):
                break
            filter_type = raw[pos]
            pos += 1
            scanline = list(raw[pos : pos + stride])
            pos += stride
            if len(scanline) != stride:
                break
            reconstructed = SettingsPage._png_unfilter_scanline(
                filter_type, scanline, prev_row, bytes_per_pixel
            )
            prev_row = reconstructed
            rows.append(
                [
                    (
                        reconstructed[idx],
                        reconstructed[idx + 1],
                        reconstructed[idx + 2],
                    )
                    for idx in range(0, stride, bytes_per_pixel)
                ]
            )
        if not rows:
            return None
        return width, height, rows

    @staticmethod
    def _median(values: list[float]) -> float:
        ordered = sorted(values)
        mid = len(ordered) // 2
        if len(ordered) % 2:
            return ordered[mid]
        return (ordered[mid - 1] + ordered[mid]) / 2

    @staticmethod
    def _png_unfilter_scanline(
        filter_type: int, row: list[int], prev: list[int], bpp: int
    ) -> list[int]:
        out = row[:]
        if filter_type == 0:
            return out
        if filter_type == 1:
            for i in range(len(out)):
                left = out[i - bpp] if i >= bpp else 0
                out[i] = (out[i] + left) & 0xFF
            return out
        if filter_type == 2:
            for i in range(len(out)):
                out[i] = (out[i] + prev[i]) & 0xFF
            return out
        if filter_type == 3:
            for i in range(len(out)):
                left = out[i - bpp] if i >= bpp else 0
                up = prev[i]
                out[i] = (out[i] + ((left + up) // 2)) & 0xFF
            return out
        if filter_type == 4:
            for i in range(len(out)):
                left = out[i - bpp] if i >= bpp else 0
                up = prev[i]
                up_left = prev[i - bpp] if i >= bpp else 0
                out[i] = (out[i] + SettingsPage._paeth_predictor(left, up, up_left)) & 0xFF
            return out
        return out

    @staticmethod
    def _paeth_predictor(left: int, up: int, up_left: int) -> int:
        p = left + up - up_left
        p_left = abs(p - left)
        p_up = abs(p - up)
        p_up_left = abs(p - up_left)
        if p_left <= p_up and p_left <= p_up_left:
            return left
        if p_up <= p_up_left:
            return up
        return up_left

    @staticmethod
    def _parse_hex_color(hex_value: str) -> tuple[int, int, int] | None:
        if not hex_value:
            return None
        value = hex_value.strip().lstrip("#")
        if value.lower().startswith("0x"):
            value = value[2:]
        if len(value) == 8:
            value = value[2:]
        if len(value) != 6:
            return None
        try:
            return (
                int(value[0:2], 16),
                int(value[2:4], 16),
                int(value[4:6], 16),
            )
        except ValueError:
            return None

    @staticmethod
    def _luminance(red: int, green: int, blue: int) -> float:
        return 0.299 * red + 0.587 * green + 0.114 * blue
