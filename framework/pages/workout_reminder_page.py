import logging
import re

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage


class WorkoutReminderPage(BasePage):
    LOGGER = logging.getLogger("cubii_workout_reminder_page")

    SET_REMINDER_PERMISSION_POPUP_TEXT_PATTERN = re.compile(
        r"set\s+reminder\s+permission", re.IGNORECASE
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

    CUBII_APP_PERMISSION_VIEW_XPATH = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View"
        "/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]"
        "/android.view.View",
    )
    CUBII_APP_PERMISSION_VIEW_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(15)',
    )

    ALARMS_REMINDERS_TOGGLE_XPATH = (
        AppiumBy.XPATH,
        "//android.widget.ScrollView/android.view.View[2]/android.view.View/android.view.View[2]",
    )
    ALARMS_REMINDERS_TOGGLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(9)',
    )

    PERMISSION_SETTINGS_BACK_BUTTON_XPATH = (
        AppiumBy.XPATH,
        "//android.widget.Button",
    )
    PERMISSION_SETTINGS_BACK_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button")',
    )

    PERMISSION_COMPOSE_BACK_BUTTON_XPATH = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View"
        "/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]"
        "/android.widget.Button",
    )
    PERMISSION_COMPOSE_BACK_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(0)',
    )

    WORKOUT_REMINDER_SCREEN_TITLE = "Workout Reminder"
    WORKOUT_REMINDER_TOOLBAR_TITLE_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title" and @text="Workout Reminder"]',
    )
    WORKOUT_REMINDER_TOOLBAR_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/toolbar_title").text("Workout Reminder")',
    )

    WORKOUT_REMINDER_TITLE_ID = "com.cubii:id/txtWorkoutReminderTitle"
    WORKOUT_REMINDER_TITLE = (
        AppiumBy.ID,
        WORKOUT_REMINDER_TITLE_ID,
    )
    WORKOUT_REMINDER_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/txtWorkoutReminderTitle")',
    )
    WORKOUT_REMINDER_TITLE_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/txtWorkoutReminderTitle"]',
    )

    NO_WORKOUT_REMINDERS_TEXT = "No Workout Reminders"
    NO_WORKOUT_REMINDERS_ID = "com.cubii:id/textView54"
    NO_WORKOUT_REMINDERS = (AppiumBy.ID, NO_WORKOUT_REMINDERS_ID)
    NO_WORKOUT_REMINDERS_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/textView54")',
    )
    NO_WORKOUT_REMINDERS_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/textView54"]',
    )
    NO_WORKOUT_REMINDERS_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="com.cubii:id/textView54" and @text="{NO_WORKOUT_REMINDERS_TEXT}"]',
    )

    SET_REMINDER_HINT_TEXT = "Set a reminder and never miss a day of workout."
    SET_REMINDER_HINT_ID = "com.cubii:id/txtGrpOptionEditGroup"
    SET_REMINDER_HINT = (AppiumBy.ID, SET_REMINDER_HINT_ID)
    SET_REMINDER_HINT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/txtGrpOptionEditGroup")',
    )
    SET_REMINDER_HINT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/txtGrpOptionEditGroup"]',
    )
    SET_REMINDER_HINT_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="com.cubii:id/txtGrpOptionEditGroup" '
        f'and @text="{SET_REMINDER_HINT_TEXT}"]',
    )

    def _short_wait(self, timeout: int | None = None) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout or Settings.EXPLICIT_WAIT)

    def _is_visible(self, locator: tuple, timeout: int = 3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def _click_if_present(self, locators: tuple[tuple, ...], timeout: int = 4, label: str = "element") -> bool:
        for locator in locators:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    ec.element_to_be_clickable(locator)
                )
                element.click()
                self.LOGGER.info("Clicked `%s` via `%s`.", label, locator[1])
                return True
            except TimeoutException:
                continue
        self.LOGGER.info("`%s` not present; continuing.", label)
        return False

    def _popup_title_visible(self, timeout: int = 3) -> bool:
        try:
            for el in self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView"):
                if not el.is_displayed():
                    continue
                text = (el.text or el.get_attribute("text") or "").strip()
                if text and self.SET_REMINDER_PERMISSION_POPUP_TEXT_PATTERN.search(text):
                    self.LOGGER.info("Set Reminder Permission popup title found: %r.", text)
                    return True
        except Exception as exc:
            self.LOGGER.debug("Popup title scan skipped: %s", exc)
        return False

    def is_set_reminder_permission_popup_present(self, timeout: int = 4) -> bool:
        turn_on_visible = self._is_visible(self.TURN_ON_BUTTON, timeout=timeout) or self._is_visible(
            self.TURN_ON_BUTTON_XPATH, timeout=1
        )
        if not turn_on_visible:
            self.LOGGER.info("Set Reminder Permission popup not present (TURN ON not visible).")
            return False
        if self._popup_title_visible(timeout=2):
            return True
        self.LOGGER.info(
            "TURN ON visible without matching popup title; treating as Set Reminder Permission popup."
        )
        return True

    def verify_set_reminder_permission_popup_if_present(self) -> bool:
        """Verify popup when TURN ON is shown; no-op when popup is absent."""
        if not self.is_set_reminder_permission_popup_present():
            return False
        for locator in (
            self.TURN_ON_BUTTON,
            self.TURN_ON_BUTTON_UIAUTOMATOR,
            self.TURN_ON_BUTTON_XPATH,
        ):
            if self._is_visible(locator, timeout=2):
                self.LOGGER.info("Set Reminder Permission popup verified via `%s`.", locator[1])
                return True
        raise AssertionError(
            "Set Reminder Permission popup expected but TURN ON button could not be verified."
        )

    def tap_turn_on_on_set_reminder_permission_popup(self) -> bool:
        return self._click_if_present(
            (self.TURN_ON_BUTTON, self.TURN_ON_BUTTON_UIAUTOMATOR, self.TURN_ON_BUTTON_XPATH),
            timeout=Settings.EXPLICIT_WAIT,
            label="TURN ON (Set Reminder Permission)",
        )

    def handle_set_reminder_permission_popup_if_present(self) -> bool:
        """If the permission popup is shown, complete the full permission flow."""
        if not self.verify_set_reminder_permission_popup_if_present():
            return False
        if not self.tap_turn_on_on_set_reminder_permission_popup():
            raise AssertionError(
                "Set Reminder Permission popup was visible but TURN ON could not be tapped."
            )
        self.LOGGER.info("TURN ON tapped; continuing with alarm permission settings.")
        if not self.tap_cubii_app_on_alarm_permission_settings():
            raise AssertionError(
                "Set Reminder Permission flow: Cubii app entry not found on permission settings."
            )
        if not self.tap_allow_alarms_and_reminders_toggle():
            raise AssertionError(
                "Set Reminder Permission flow: alarms and reminders toggle not found."
            )
        first_back = self.tap_permission_settings_back_button()
        self.tap_permission_compose_back_button(fallback_after_first_back=first_back)
        self.LOGGER.info(
            "Set Reminder Permission flow completed (popup through toggle and both back taps)."
        )
        return True

    def tap_cubii_app_on_alarm_permission_settings(self) -> bool:
        return self._click_if_present(
            (
                self.CUBII_APP_PERMISSION_VIEW_XPATH,
                self.CUBII_APP_PERMISSION_VIEW_UIAUTOMATOR,
            ),
            timeout=Settings.EXPLICIT_WAIT,
            label="Cubii app (alarm permission settings)",
        )

    def tap_allow_alarms_and_reminders_toggle(self) -> bool:
        for locator in (
            self.ALARMS_REMINDERS_TOGGLE_XPATH,
            self.ALARMS_REMINDERS_TOGGLE_UIAUTOMATOR,
        ):
            try:
                toggle = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT).until(
                    ec.element_to_be_clickable(locator)
                )
                checked = str(toggle.get_attribute("checked")).lower() == "true"
                self.LOGGER.info(
                    "Alarms and reminders toggle checked=%s via `%s`.", checked, locator[1]
                )
                if not checked:
                    toggle.click()
                    self.LOGGER.info("Alarms and reminders toggle switched ON.")
                else:
                    self.LOGGER.info("Alarms and reminders toggle already ON.")
                return True
            except TimeoutException:
                continue
        self.LOGGER.info("Alarms and reminders toggle not present; continuing.")
        return False

    def tap_permission_settings_back_button(self) -> bool:
        clicked = self._click_if_present(
            (
                self.PERMISSION_SETTINGS_BACK_BUTTON_XPATH,
                self.PERMISSION_SETTINGS_BACK_BUTTON_UIAUTOMATOR,
            ),
            timeout=4,
            label="permission settings back (android.widget.Button)",
        )
        if clicked:
            return True
        self.LOGGER.info("Permission settings back button not found; using Android back.")
        self.driver.back()
        return True

    def tap_permission_compose_back_button(self, fallback_after_first_back: bool = False) -> bool:
        clicked = self._click_if_present(
            (
                self.PERMISSION_COMPOSE_BACK_BUTTON_XPATH,
                self.PERMISSION_COMPOSE_BACK_BUTTON_UIAUTOMATOR,
            ),
            timeout=4,
            label="permission compose back (android.widget.Button instance 0)",
        )
        if clicked:
            return True
        if fallback_after_first_back:
            self.LOGGER.info(
                "Compose back button not found after first back; using Android back."
            )
            self.driver.back()
        else:
            self.LOGGER.info("Compose back button not present; continuing.")
        return clicked

    def _assert_visible_one_of(
        self, locators: tuple[tuple, ...], description: str, wait: WebDriverWait | None = None
    ) -> None:
        wait = wait or self._short_wait()
        for locator in locators:
            try:
                wait.until(ec.visibility_of_element_located(locator))
                self.LOGGER.info("%s verified via `%s`.", description, locator[1])
                return
            except TimeoutException:
                continue
        raise AssertionError(f"Workout Reminder screen: {description} not visible.")

    def _is_no_workout_reminder_empty_state_visible(self, timeout: int = 3) -> bool:
        return self._is_visible(self.NO_WORKOUT_REMINDERS_TEXT_XPATH, timeout=timeout) or self._is_visible(
            self.NO_WORKOUT_REMINDERS, timeout=1
        )

    def _assert_visible_text_one_of(
        self,
        locators: tuple[tuple, ...],
        expected_text: str,
        description: str,
        wait: WebDriverWait | None = None,
    ) -> None:
        wait = wait or self._short_wait()
        last_text = None
        for locator in locators:
            try:
                element = wait.until(ec.visibility_of_element_located(locator))
                last_text = (element.text or element.get_attribute("text") or "").strip()
                if last_text == expected_text:
                    self.LOGGER.info("%s verified: %r via `%s`.", description, last_text, locator[1])
                    return
            except TimeoutException:
                continue
        raise AssertionError(
            f"Workout Reminder screen: {description} not visible or text mismatch. "
            f"Expected {expected_text!r}, got {last_text!r}."
        )

    def verify_no_workout_reminder_empty_state_if_present(self) -> None:
        """When no reminders exist, verify empty-state title and hint message."""
        if not self._is_no_workout_reminder_empty_state_visible():
            self.LOGGER.info(
                "No empty-state message (`textView54`) visible; skipping no-reminder verification."
            )
            return
        self.LOGGER.info("Empty Workout Reminder state detected; verifying messages.")
        wait = self._short_wait()
        self._assert_visible_text_one_of(
            (
                self.NO_WORKOUT_REMINDERS_TEXT_XPATH,
                self.NO_WORKOUT_REMINDERS,
                self.NO_WORKOUT_REMINDERS_UIAUTOMATOR,
                self.NO_WORKOUT_REMINDERS_XPATH,
            ),
            self.NO_WORKOUT_REMINDERS_TEXT,
            "No Workout Reminders (`textView54`)",
            wait=wait,
        )
        self._assert_visible_text_one_of(
            (
                self.SET_REMINDER_HINT_TEXT_XPATH,
                self.SET_REMINDER_HINT,
                self.SET_REMINDER_HINT_UIAUTOMATOR,
                self.SET_REMINDER_HINT_XPATH,
            ),
            self.SET_REMINDER_HINT_TEXT,
            "Set a reminder hint (`txtGrpOptionEditGroup`)",
            wait=wait,
        )
        self.LOGGER.info("No Workout Reminder empty state verified.")

    def verify_workout_reminder_screen_visible(self) -> None:
        self.LOGGER.info("Verifying Workout Reminder screen is visible.")
        wait = self._short_wait()
        self._assert_visible_one_of(
            (
                self.WORKOUT_REMINDER_TOOLBAR_TITLE_XPATH,
                self.WORKOUT_REMINDER_TOOLBAR_TITLE_UIAUTOMATOR,
            ),
            f"toolbar title {self.WORKOUT_REMINDER_SCREEN_TITLE!r}",
            wait=wait,
        )
        self._assert_visible_one_of(
            (
                self.WORKOUT_REMINDER_TITLE,
                self.WORKOUT_REMINDER_TITLE_UIAUTOMATOR,
                self.WORKOUT_REMINDER_TITLE_XPATH,
            ),
            "Workout title (`txtWorkoutReminderTitle`)",
            wait=wait,
        )
        self.LOGGER.info("Workout Reminder screen verified (toolbar and Workout title).")
