import logging
import math
import os
import random
import re
import time
from datetime import datetime, timedelta

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

    WORKOUT_REMINDER_SCREEN_TITLE = "Workout Reminders"
    WORKOUT_REMINDER_TOOLBAR_TITLE_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/txtWorkoutReminderTitle" and @text="Workout Reminders"]',
    )
    WORKOUT_REMINDER_TOOLBAR_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/txtWorkoutReminderTitle").text("Workout Reminders")',
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

    # Add Reminder flow
    ADD_REMINDER_BUTTON = (AppiumBy.ID, "com.cubii:id/btnAddWorkoutReminder")
    ADD_REMINDER_BUTTON_CLASS = (AppiumBy.CLASS_NAME, "android.widget.Button")
    ADD_REMINDER_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/btnAddWorkoutReminder")',
    )
    ADD_REMINDER_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btnAddWorkoutReminder"]',
    )

    ADD_REMINDER_TOOLBAR_TITLE = (AppiumBy.ID, "com.cubii:id/toolbar_title")
    ADD_REMINDER_TOOLBAR_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/toolbar_title")',
    )
    ADD_REMINDER_TOOLBAR_TITLE_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title"]',
    )

    ADD_REMINDER_TIME_PICKER = (AppiumBy.ID, "com.cubii:id/timePicker")
    ADD_REMINDER_TIME_PICKER_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/timePicker")',
    )
    ADD_REMINDER_TIME_PICKER_XPATH = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@resource-id="com.cubii:id/timePicker"]',
    )
    ADD_REMINDER_DAYS_LAYOUT = (AppiumBy.ID, "com.cubii:id/ll_days")
    ADD_REMINDER_DAYS_LAYOUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/ll_days")',
    )
    ADD_REMINDER_DAYS_LAYOUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/ll_days"]',
    )
    ADD_REMINDER_CLOCK_HAND = (AppiumBy.ID, "com.cubii:id/material_clock_hand")
    ADD_REMINDER_CLOCK_HAND_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/material_clock_hand")',
    )
    ADD_REMINDER_CLOCK_HAND_XPATH = (
        AppiumBy.XPATH,
        '//android.view.View[@resource-id="com.cubii:id/material_clock_hand"]',
    )
    ADD_REMINDER_CLOCK_FACE = (AppiumBy.ID, "com.cubii:id/material_clock_face")
    ADD_REMINDER_CLOCK_FACE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/material_clock_face")',
    )
    ADD_REMINDER_CLOCK_FACE_XPATH = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@resource-id="com.cubii:id/material_clock_face"]',
    )
    ADD_REMINDER_AM_BUTTON = (
        AppiumBy.ID,
        "com.cubii:id/material_clock_period_am_button",
    )
    ADD_REMINDER_AM_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/material_clock_period_am_button")',
    )
    ADD_REMINDER_AM_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.RadioButton[@resource-id="com.cubii:id/material_clock_period_am_button"]',
    )
    ADD_REMINDER_PM_BUTTON = (
        AppiumBy.ID,
        "com.cubii:id/material_clock_period_pm_button",
    )
    ADD_REMINDER_PM_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/material_clock_period_pm_button")',
    )
    ADD_REMINDER_PM_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.RadioButton[@resource-id="com.cubii:id/material_clock_period_pm_button"]',
    )
    ADD_REMINDER_HOUR_TV = (AppiumBy.ID, "com.cubii:id/material_hour_tv")
    ADD_REMINDER_HOUR_TV_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/material_hour_tv")',
    )
    ADD_REMINDER_HOUR_TV_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/material_hour_tv"]',
    )
    ADD_REMINDER_MINUTE_TV = (AppiumBy.ID, "com.cubii:id/material_minute_tv")
    ADD_REMINDER_MINUTE_TV_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/material_minute_tv")',
    )
    ADD_REMINDER_MINUTE_TV_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/material_minute_tv"]',
    )
    REMINDER_NAME_INPUT = (AppiumBy.ID, "com.cubii:id/edtReminderText")
    REMINDER_NAME_INPUT_CLASS = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    REMINDER_NAME_INPUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/edtReminderText")',
    )
    REMINDER_NAME_INPUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/edtReminderText"]',
    )
    SAVE_REMINDER_BUTTON = (AppiumBy.ID, "com.cubii:id/btn_set_reminder")
    SAVE_REMINDER_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/btn_set_reminder")',
    )
    SAVE_REMINDER_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btn_set_reminder"]',
    )
    SAVED_REMINDER_TIME = (AppiumBy.ID, "com.cubii:id/txtWorkoutTime")
    SAVED_REMINDER_TIME_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/txtWorkoutTime")',
    )
    SAVED_REMINDER_TIME_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/txtWorkoutTime"]',
    )
    SAVED_REMINDER_DAYS = (AppiumBy.ID, "com.cubii:id/txtWorkoutReminderDays")
    SAVED_REMINDER_DAYS_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/txtWorkoutReminderDays")',
    )
    SAVED_REMINDER_DAYS_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/txtWorkoutReminderDays"]',
    )
    FIRST_REMINDER_CARD_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").instance(5)',
    )
    FIRST_REMINDER_CARD_XPATH = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_workout_reminders_list"]'
        '/android.widget.FrameLayout[1]/android.view.ViewGroup',
    )
    WORKOUT_REMINDER_SWITCH = (AppiumBy.ID, "com.cubii:id/swWorkoutReminderItem")
    WORKOUT_REMINDER_SWITCH_CLASS = (AppiumBy.CLASS_NAME, "android.widget.Switch")
    WORKOUT_REMINDER_SWITCH_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/swWorkoutReminderItem")',
    )
    WORKOUT_REMINDER_SWITCH_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Switch[@resource-id="com.cubii:id/swWorkoutReminderItem"]',
    )
    REMOVE_REMINDER_OPTION = (AppiumBy.ID, "com.cubii:id/menu_remove")
    REMOVE_REMINDER_OPTION_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/menu_remove")',
    )
    REMOVE_REMINDER_OPTION_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/menu_remove"]',
    )
    WORKOUT_REMINDER_CANCEL_NAV_UP_ACCESSIBILITY_ID = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    WORKOUT_REMINDER_CANCEL_NAV_UP_CLASS = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")
    WORKOUT_REMINDER_CANCEL_NAV_UP_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Navigate up")',
    )
    WORKOUT_REMINDER_CANCEL_NAV_UP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Navigate up"]',
    )
    MORE_BACK_OPTION = (AppiumBy.ID, "com.cubii:id/iv_back")
    MORE_BACK_OPTION_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/iv_back")',
    )
    MORE_BACK_OPTION_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/iv_back"]',
    )
    REMOVE_REMINDER_CHECKBOX = (AppiumBy.ID, "com.cubii:id/cb_remove")
    REMOVE_REMINDER_CHECKBOX_CLASS = (AppiumBy.CLASS_NAME, "android.widget.CheckBox")
    REMOVE_REMINDER_CHECKBOX_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/cb_remove")',
    )
    REMOVE_REMINDER_CHECKBOX_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.CheckBox[@resource-id="com.cubii:id/cb_remove"]',
    )
    ADD_REMINDER_CLOCK_VALUE_XPATH_TMPL = (
        '//android.view.View[contains(@content-desc,"{value}")]'
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

    def tap_add_reminder_button(self) -> None:
        self.LOGGER.info("Tapping Add Reminder button.")
        clicked = self._click_if_present(
            (
                self.ADD_REMINDER_BUTTON,
                self.ADD_REMINDER_BUTTON_UIAUTOMATOR,
                self.ADD_REMINDER_BUTTON_XPATH,
                self.ADD_REMINDER_BUTTON_CLASS,
            ),
            timeout=Settings.EXPLICIT_WAIT,
            label="ADD REMINDER (`btnAddWorkoutReminder`)",
        )
        if not clicked:
            raise AssertionError("ADD REMINDER button not found or not tappable.")

    def verify_add_reminder_screen_visible(self) -> None:
        self.LOGGER.info("Verifying Add Reminder screen.")
        wait = self._short_wait()
        self._assert_visible_one_of(
            (
                self.ADD_REMINDER_TOOLBAR_TITLE,
                self.ADD_REMINDER_TOOLBAR_TITLE_UIAUTOMATOR,
                self.ADD_REMINDER_TOOLBAR_TITLE_XPATH,
            ),
            "Add Reminder toolbar title (`toolbar_title`)",
            wait=wait,
        )

        title = ""
        try:
            title = wait.until(
                ec.visibility_of_element_located(self.ADD_REMINDER_TOOLBAR_TITLE)
            ).text.strip()
        except Exception:
            pass
        if title and title.lower() not in {"add reminder", "edit reminder"}:
            raise AssertionError(
                f"Unexpected reminder toolbar title text. Got: {title!r}"
            )
        self.LOGGER.info("Add/Edit Reminder screen verified. title=%r", title)

    def set_workout_reminder_time(self) -> None:
        self.LOGGER.info("Setting reminder time on Add Reminder screen.")
        wait = self._short_wait()
        self._assert_visible_one_of(
            (
                self.ADD_REMINDER_TIME_PICKER,
                self.ADD_REMINDER_TIME_PICKER_UIAUTOMATOR,
                self.ADD_REMINDER_TIME_PICKER_XPATH,
            ),
            "time picker (`timePicker`)",
            wait=wait,
        )
        self._assert_visible_one_of(
            (
                self.ADD_REMINDER_DAYS_LAYOUT,
                self.ADD_REMINDER_DAYS_LAYOUT_UIAUTOMATOR,
                self.ADD_REMINDER_DAYS_LAYOUT_XPATH,
            ),
            "days layout (`ll_days`)",
            wait=wait,
        )
        self._assert_visible_one_of(
            (
                self.ADD_REMINDER_CLOCK_HAND,
                self.ADD_REMINDER_CLOCK_HAND_UIAUTOMATOR,
                self.ADD_REMINDER_CLOCK_HAND_XPATH,
            ),
            "clock hand (`material_clock_hand`)",
            wait=wait,
        )
        self._assert_visible_one_of(
            (
                self.ADD_REMINDER_HOUR_TV,
                self.ADD_REMINDER_HOUR_TV_UIAUTOMATOR,
                self.ADD_REMINDER_HOUR_TV_XPATH,
            ),
            "hour selector (`material_hour_tv`)",
            wait=wait,
        )
        self._assert_visible_one_of(
            (
                self.ADD_REMINDER_MINUTE_TV,
                self.ADD_REMINDER_MINUTE_TV_UIAUTOMATOR,
                self.ADD_REMINDER_MINUTE_TV_XPATH,
            ),
            "minute selector (`material_minute_tv`)",
            wait=wait,
        )

        period_present = False
        for loc in (
            self.ADD_REMINDER_AM_BUTTON,
            self.ADD_REMINDER_AM_BUTTON_UIAUTOMATOR,
            self.ADD_REMINDER_AM_BUTTON_XPATH,
            self.ADD_REMINDER_PM_BUTTON,
            self.ADD_REMINDER_PM_BUTTON_UIAUTOMATOR,
            self.ADD_REMINDER_PM_BUTTON_XPATH,
        ):
            if self._is_visible(loc, timeout=1):
                period_present = True
                break
        if not period_present:
            raise AssertionError(
                "Neither AM nor PM period selector is visible on Add Reminder time picker."
            )
        randomize = os.getenv("CUBII_REMINDER_RANDOMIZE", "1").strip().lower() not in (
            "0",
            "false",
            "no",
        )
        if randomize:
            # Default to 5-minute increments to match the visible minute marks.
            minute_step = max(1, int(os.getenv("CUBII_REMINDER_MINUTE_STEP", "5")))
            minute_values = list(range(0, 60, minute_step))
            if not minute_values:
                minute_values = [0]
            target_hour = random.randint(1, 12)
            target_minute = random.choice(minute_values)
            target_period = random.choice(["AM", "PM"])
            all_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
            day_count = random.randint(1, len(all_days))
            days = random.sample(all_days, k=day_count)
            days.sort(key=all_days.index)
            self.LOGGER.info(
                "Random reminder generated: %02d:%02d %s | days=%s",
                target_hour,
                target_minute,
                target_period,
                ",".join(days),
            )
        else:
            target_hour = int(os.getenv("CUBII_REMINDER_TARGET_HOUR", "2"))
            target_minute = int(os.getenv("CUBII_REMINDER_TARGET_MINUTE", "35"))
            target_period = os.getenv("CUBII_REMINDER_TARGET_PERIOD", "PM").strip().upper()
            target_days = os.getenv("CUBII_REMINDER_TARGET_DAYS", "Mon,Wed,Fri")
            days = [d.strip() for d in target_days.split(",") if d.strip()]

        self._set_reminder_period(target_period)
        self._set_time_picker_value(target_hour, target_minute)
        self._select_reminder_days(days)
        self._expected_reminder = {
            "hour": target_hour,
            "minute": target_minute,
            "period": target_period,
            "days": days,
        }
        self.LOGGER.info(
            "Reminder time set and days selected: %02d:%02d %s | days=%s",
            target_hour,
            target_minute,
            target_period,
            ",".join(days),
        )

    def set_workout_reminder_name(self) -> None:
        self.LOGGER.info("Setting workout reminder name.")
        wait = self._short_wait()
        field = None
        for locator in (
            self.REMINDER_NAME_INPUT,
            self.REMINDER_NAME_INPUT_UIAUTOMATOR,
            self.REMINDER_NAME_INPUT_XPATH,
            self.REMINDER_NAME_INPUT_CLASS,
        ):
            try:
                field = wait.until(ec.visibility_of_element_located(locator))
                self.LOGGER.info("Reminder name input located via `%s`.", locator[1])
                break
            except TimeoutException:
                continue
        if field is None:
            raise AssertionError("Reminder name input (`edtReminderText`) not found.")

        configured_name = os.getenv("CUBII_REMINDER_NAME", "").strip()
        name = configured_name or f"Reminder {random.randint(1000, 9999)}"
        try:
            field.clear()
        except Exception:
            pass
        field.click()
        field.send_keys(name)
        self._hide_keyboard_after_text_entry()
        self._expected_reminder_name = name
        self.LOGGER.info("Workout reminder name set to: %r", name)

    def _hide_keyboard_after_text_entry(self) -> None:
        """Hide soft keyboard so lower-screen actions like SAVE are reachable."""
        try:
            self.driver.hide_keyboard()
            time.sleep(float(os.getenv("CUBII_AFTER_HIDE_KEYBOARD_SEC", "0.5")))
            self.LOGGER.info("Soft keyboard hidden after reminder name entry.")
            return
        except Exception as exc:
            self.LOGGER.debug("hide_keyboard failed after reminder name entry: %s", exc)
        try:
            self.driver.press_keycode(4)
            time.sleep(float(os.getenv("CUBII_AFTER_HIDE_KEYBOARD_SEC", "0.5")))
            self.LOGGER.info("Android back used to hide soft keyboard after reminder name entry.")
        except Exception as exc:
            self.LOGGER.debug("Android back keyboard fallback failed: %s", exc)

    def tap_first_workout_reminder(self) -> None:
        self.LOGGER.info("Opening first saved Workout Reminder item.")
        wait = self._short_wait()
        for locator in (
            self.FIRST_REMINDER_CARD_UIAUTOMATOR,
            self.FIRST_REMINDER_CARD_XPATH,
        ):
            try:
                el = wait.until(ec.element_to_be_clickable(locator))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_REMINDER_CARD_TAP_SEC", "0.6")))
                self.LOGGER.info("First reminder item tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                continue
        raise AssertionError("First reminder item not found or not tappable.")

    def edit_workout_reminder_time_days_and_name(self) -> None:
        self.LOGGER.info("Editing Workout Reminder: random time, all days, random name.")
        self.verify_add_reminder_screen_visible()
        title = self._visible_text_one_of(
            (
                self.ADD_REMINDER_TOOLBAR_TITLE,
                self.ADD_REMINDER_TOOLBAR_TITLE_UIAUTOMATOR,
                self.ADD_REMINDER_TOOLBAR_TITLE_XPATH,
            ),
            "Edit Reminder toolbar title (`toolbar_title`)",
        )
        if title.lower() != "edit reminder":
            raise AssertionError(f"Expected Edit Reminder toolbar title, got {title!r}.")
        target_hour = random.randint(1, 12)
        target_minute = random.choice(list(range(0, 60, 5)))
        target_period = random.choice(["AM", "PM"])
        all_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

        self._set_reminder_period(target_period)
        self._set_time_picker_value(target_hour, target_minute)
        self._select_all_reminder_days(all_days)
        self.set_workout_reminder_name()
        self._expected_reminder = {
            "hour": target_hour,
            "minute": target_minute,
            "period": target_period,
            "days": all_days,
        }
        self.LOGGER.info(
            "Edited reminder values: %02d:%02d %s | days=%s",
            target_hour,
            target_minute,
            target_period,
            ",".join(all_days),
        )

    def set_workout_reminder_for_next_minute(self) -> None:
        """Set a deterministic reminder for roughly one minute ahead and select today's day."""
        lead_sec = int(os.getenv("CUBII_REMINDER_NOTIFICATION_LEAD_SEC", "75"))
        target = datetime.now() + timedelta(seconds=lead_sec)
        target_hour_24 = target.hour
        target_hour = target_hour_24 % 12 or 12
        target_minute = target.minute
        target_period = "AM" if target_hour_24 < 12 else "PM"
        today = target.strftime("%a")

        self.LOGGER.info(
            "Notification reminder target generated: %02d:%02d %s | day=%s | lead_sec=%s",
            target_hour,
            target_minute,
            target_period,
            today,
            lead_sec,
        )
        self._set_reminder_period(target_period)
        self._set_time_picker_value(target_hour, target_minute)
        self._select_reminder_days([today])
        self._expected_reminder = {
            "hour": target_hour,
            "minute": target_minute,
            "period": target_period,
            "days": [today],
        }
        self._expected_reminder_notification_target = target

    def wait_for_scheduled_reminder_notification(self) -> None:
        """Wait until after the scheduled reminder time, then pull down notifications."""
        target = getattr(self, "_expected_reminder_notification_target", None)
        post_target_wait = int(os.getenv("CUBII_REMINDER_NOTIFICATION_POST_WAIT_SEC", "20"))
        if target is None:
            wait_sec = int(os.getenv("CUBII_REMINDER_NOTIFICATION_WAIT_SEC", "90"))
        else:
            wait_sec = max(5, int((target - datetime.now()).total_seconds()) + post_target_wait)

        self.LOGGER.info(
            "Waiting %ss for reminder notification, then opening notification shade.",
            wait_sec,
        )
        time.sleep(wait_sec)
        self.driver.open_notifications()
        time.sleep(float(os.getenv("CUBII_AFTER_OPEN_NOTIFICATIONS_SEC", "2.0")))
        self.LOGGER.info("Android notification shade opened.")

    def verify_workout_reminder_notification_displayed(self) -> None:
        expected = getattr(self, "_expected_reminder", None) or {}
        expected_time = ""
        if expected:
            expected_time = f"{int(expected['hour']):02d}:{int(expected['minute']):02d} {expected['period']}"

        title_text = "It’s time for your workout"
        self._wait_for_notification_text(
            title_text,
            resource_id="android:id/title",
            description="workout reminder notification title",
        )
        self._wait_for_notification_text(
            "Your workout starts at",
            resource_id="android:id/text",
            description="workout reminder notification body",
        )

        page_text = self._notification_shade_text()
        normalized = page_text.lower()
        required_any = ("cubii", "workout", "reminder")
        if not any(token in normalized for token in required_any):
            raise AssertionError(
                "Workout reminder notification not found. "
                f"Expected Cubii/workout/reminder text. Notification shade text={page_text!r}"
            )

        if "workout" not in normalized:
            raise AssertionError(
                f"Notification shade opened, but workout reminder text was not found: {page_text!r}"
            )

        if expected_time and expected_time.lower() not in normalized:
            self.LOGGER.warning(
                "Expected reminder time %r not found in notification text; continuing because "
                "Cubii workout notification is present. text=%r",
                expected_time,
                page_text,
            )
        self.LOGGER.info("Workout reminder notification verified. text=%r", page_text)

    def close_notification_panel(self) -> None:
        """Close Android notification shade after notification validation."""
        self.LOGGER.info("Closing Android notification panel.")
        try:
            self.driver.back()
        except Exception:
            try:
                self.driver.press_keycode(4)
            except Exception as exc:
                raise AssertionError(
                    f"Could not close Android notification panel. Error: {exc}"
                ) from exc
        time.sleep(float(os.getenv("CUBII_AFTER_CLOSE_NOTIFICATIONS_SEC", "1.0")))
        self.LOGGER.info("Android notification panel close action completed.")

    def tap_workout_reminder_notification(self) -> None:
        """Tap the visible workout reminder notification in the Android shade."""
        self.LOGGER.info("Tapping workout reminder notification.")
        self.verify_workout_reminder_notification_displayed()
        title_locator = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@resource-id="android:id/title" '
            'and contains(@text,"It’s time for your workout")]',
        )
        body_locator = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@resource-id="android:id/text" '
            'and contains(@text,"Your workout starts at")]',
        )
        for locator in (title_locator, body_locator):
            try:
                el = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_NOTIFICATION_TAP_SEC", "1.0")))
                self.LOGGER.info("Workout reminder notification tapped via `%s`.", locator[1])
                return
            except Exception:
                continue
        raise AssertionError("Workout reminder notification was visible but not tappable.")

    def _wait_for_notification_text(self, text: str, resource_id: str, description: str) -> None:
        wait_sec = int(os.getenv("CUBII_REMINDER_NOTIFICATION_VERIFY_WAIT_SEC", "30"))
        locators = (
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{text}")'),
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{resource_id}" and contains(@text,"{text}")]',
            ),
        )
        last_error = None
        deadline = time.monotonic() + wait_sec
        while time.monotonic() < deadline:
            for locator in locators:
                try:
                    WebDriverWait(self.driver, 2).until(
                        ec.visibility_of_element_located(locator)
                    )
                    self.LOGGER.info("%s verified via `%s`.", description, locator[1])
                    return
                except Exception as exc:
                    last_error = exc
            time.sleep(1)
        raise AssertionError(
            f"{description} not visible after {wait_sec}s. Expected text={text!r}. "
            f"Last error={last_error!r}. Notification shade text={self._notification_shade_text()!r}"
        )

    def _notification_shade_text(self) -> str:
        parts = []
        try:
            source = self.driver.page_source or ""
            parts.append(source)
        except Exception:
            pass
        for by, locator in (
            (AppiumBy.XPATH, "//*[contains(@text,'Cubii')]"),
            (AppiumBy.XPATH, "//*[contains(@text,'workout')]"),
            (AppiumBy.XPATH, "//*[contains(@text,'Workout')]"),
            (AppiumBy.XPATH, "//*[contains(@text,'reminder')]"),
            (AppiumBy.XPATH, "//*[contains(@text,'Reminder')]"),
        ):
            try:
                for el in self.driver.find_elements(by, locator):
                    text = (el.text or el.get_attribute("text") or "").strip()
                    if text:
                        parts.append(text)
            except Exception:
                continue
        return " ".join(parts)

    def _set_reminder_period(self, period: str) -> None:
        period = period.upper()
        if period == "AM":
            candidates = (
                self.ADD_REMINDER_AM_BUTTON,
                self.ADD_REMINDER_AM_BUTTON_UIAUTOMATOR,
                self.ADD_REMINDER_AM_BUTTON_XPATH,
            )
        elif period == "PM":
            candidates = (
                self.ADD_REMINDER_PM_BUTTON,
                self.ADD_REMINDER_PM_BUTTON_UIAUTOMATOR,
                self.ADD_REMINDER_PM_BUTTON_XPATH,
            )
        else:
            raise AssertionError(f"Unsupported reminder period: {period!r}. Use AM or PM.")
        clicked = self._click_if_present(candidates, timeout=4, label=f"{period} period button")
        if not clicked:
            raise AssertionError(f"Could not select reminder period button: {period}.")

    def _set_time_picker_value(self, hour: int, minute: int) -> None:
        if hour < 1 or hour > 12:
            raise AssertionError(f"Reminder hour must be between 1 and 12. Got: {hour}")
        if minute < 0 or minute > 59:
            raise AssertionError(f"Reminder minute must be between 0 and 59. Got: {minute}")

        self._click_if_present(
            (
                self.ADD_REMINDER_HOUR_TV,
                self.ADD_REMINDER_HOUR_TV_UIAUTOMATOR,
                self.ADD_REMINDER_HOUR_TV_XPATH,
            ),
            timeout=4,
            label="hour selector",
        )
        self._tap_clock_face_value(str(hour), value=int(hour), mode="hour")

        self._click_if_present(
            (
                self.ADD_REMINDER_MINUTE_TV,
                self.ADD_REMINDER_MINUTE_TV_UIAUTOMATOR,
                self.ADD_REMINDER_MINUTE_TV_XPATH,
            ),
            timeout=4,
            label="minute selector",
        )
        self._tap_clock_face_value(f"{minute:02d}", value=int(minute), mode="minute")

    def _tap_clock_face_value(self, value_text: str, value: int | None = None, mode: str = "minute") -> None:
        wait_sec = int(os.getenv("CUBII_REMINDER_CLOCK_VALUE_WAIT_SEC", "6"))
        value_xpath = self.ADD_REMINDER_CLOCK_VALUE_XPATH_TMPL.format(value=value_text)
        for locator in (
            (AppiumBy.XPATH, value_xpath),
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().descriptionContains("{value_text}")'),
        ):
            try:
                el = WebDriverWait(self.driver, wait_sec).until(
                    ec.element_to_be_clickable(locator)
                )
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_REMINDER_CLOCK_TAP_SEC", "0.3")))
                self.LOGGER.info("Reminder picker value tapped: %s via %s", value_text, locator[0])
                return
            except Exception:
                continue
        if value is not None:
            self._tap_clock_face_coordinate(value=value, mode=mode)
            return
        raise AssertionError(f"Could not tap reminder picker value: {value_text!r}.")

    def _tap_clock_face_coordinate(self, value: int, mode: str) -> None:
        """
        Material clock only exposes 5-minute labels in accessibility. For exact
        minutes like 33, tap the clock-face coordinate calculated from the dial.
        """
        face = None
        for locator in (
            self.ADD_REMINDER_CLOCK_FACE,
            self.ADD_REMINDER_CLOCK_FACE_UIAUTOMATOR,
            self.ADD_REMINDER_CLOCK_FACE_XPATH,
            self.ADD_REMINDER_TIME_PICKER,
        ):
            try:
                face = WebDriverWait(self.driver, 3).until(
                    ec.visibility_of_element_located(locator)
                )
                break
            except Exception:
                continue
        if face is None:
            raise AssertionError(f"Could not locate clock face to tap {mode} value {value}.")

        rect = face.rect
        cx = rect["x"] + rect["width"] / 2
        cy = rect["y"] + rect["height"] / 2
        radius = min(rect["width"], rect["height"]) * float(
            os.getenv("CUBII_REMINDER_CLOCK_RADIUS_FACTOR", "0.40")
        )

        if mode == "hour":
            angle_degrees = (value % 12) * 30
        elif mode == "minute":
            angle_degrees = value * 6
        else:
            raise AssertionError(f"Unsupported clock picker mode: {mode!r}")

        angle = math.radians(angle_degrees)
        x = int(round(cx + radius * math.sin(angle)))
        y = int(round(cy - radius * math.cos(angle)))

        try:
            self.driver.execute_script("mobile: clickGesture", {"x": x, "y": y})
        except Exception:
            self.driver.tap([(x, y)])
        time.sleep(float(os.getenv("CUBII_AFTER_REMINDER_CLOCK_TAP_SEC", "0.3")))
        self.LOGGER.info(
            "Reminder picker value tapped by coordinate: mode=%s value=%s x=%s y=%s",
            mode,
            value,
            x,
            y,
        )

    def _select_reminder_days(self, days: list[str]) -> None:
        if not days:
            raise AssertionError("No reminder days provided to select.")
        for day in days:
            day_xpath = (
                f'//*[@resource-id="com.cubii:id/ll_days"]//*[translate(@text,'
                f' "abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ")="{day.upper()}"]'
            )
            try:
                el = WebDriverWait(self.driver, 5).until(
                    ec.element_to_be_clickable((AppiumBy.XPATH, day_xpath))
                )
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_REMINDER_DAY_TAP_SEC", "0.2")))
                self.LOGGER.info("Reminder day selected: %s", day)
            except Exception as exc:
                raise AssertionError(f"Could not select reminder day {day!r}. Error: {exc}") from exc

    def _select_all_reminder_days(self, days: list[str]) -> None:
        if not days:
            raise AssertionError("No reminder days provided to select.")
        for day in days:
            day_xpath = (
                f'//*[@resource-id="com.cubii:id/ll_days"]//*[translate(@text,'
                f' "abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ")="{day.upper()}"]'
            )
            try:
                el = WebDriverWait(self.driver, 5).until(
                    ec.element_to_be_clickable((AppiumBy.XPATH, day_xpath))
                )
                checked = str(el.get_attribute("checked")).strip().lower() == "true"
                selected = str(el.get_attribute("selected")).strip().lower() == "true"
                if checked or selected:
                    self.LOGGER.info("Reminder day already selected: %s", day)
                    continue
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_REMINDER_DAY_TAP_SEC", "0.2")))
                self.LOGGER.info("Reminder day selected for all-days edit: %s", day)
            except Exception as exc:
                raise AssertionError(f"Could not select reminder day {day!r}. Error: {exc}") from exc

    def tap_save_reminder_button(self) -> None:
        self.LOGGER.info("Tapping SAVE reminder button.")
        clicked = self._click_if_present(
            (
                self.SAVE_REMINDER_BUTTON,
                self.SAVE_REMINDER_BUTTON_UIAUTOMATOR,
                self.SAVE_REMINDER_BUTTON_XPATH,
            ),
            timeout=Settings.EXPLICIT_WAIT,
            label="SAVE reminder (`btn_set_reminder`)",
        )
        if not clicked:
            raise AssertionError("SAVE reminder button not found or not tappable.")

    def toggle_workout_reminder_off(self) -> None:
        self.LOGGER.info("Toggling Workout Reminder switch OFF if currently enabled.")
        wait = self._short_wait()
        switch = None
        for locator in (
            self.WORKOUT_REMINDER_SWITCH,
            self.WORKOUT_REMINDER_SWITCH_UIAUTOMATOR,
            self.WORKOUT_REMINDER_SWITCH_XPATH,
            self.WORKOUT_REMINDER_SWITCH_CLASS,
        ):
            try:
                switch = wait.until(ec.element_to_be_clickable(locator))
                self.LOGGER.info("Workout reminder switch located via `%s`.", locator[1])
                break
            except TimeoutException:
                continue
        if switch is None:
            raise AssertionError("Workout reminder switch (`swWorkoutReminderItem`) not found.")

        checked = str(switch.get_attribute("checked")).strip().lower() == "true"
        self.LOGGER.info("Workout reminder switch initial checked=%s", checked)
        if checked:
            switch.click()
            time.sleep(float(os.getenv("CUBII_AFTER_REMINDER_TOGGLE_SEC", "0.5")))
            checked_after = str(switch.get_attribute("checked")).strip().lower() == "true"
            if checked_after:
                raise AssertionError("Workout reminder switch is still ON after toggle attempt.")
            self.LOGGER.info("Workout reminder switch toggled OFF successfully.")
        else:
            self.LOGGER.info("Workout reminder switch already OFF; no toggle needed.")

    def tap_remove_reminder_option(self) -> None:
        self.LOGGER.info("Tapping REMOVE option (`menu_remove`).")
        wait = self._short_wait()
        option = None
        for locator in (
            self.REMOVE_REMINDER_OPTION,
            self.REMOVE_REMINDER_OPTION_UIAUTOMATOR,
            self.REMOVE_REMINDER_OPTION_XPATH,
        ):
            try:
                option = wait.until(ec.element_to_be_clickable(locator))
                self.LOGGER.info("REMOVE option located via `%s`.", locator[1])
                break
            except TimeoutException:
                continue
        if option is None:
            raise AssertionError("REMOVE option (`menu_remove`) not found or not tappable.")

        text = (option.text or option.get_attribute("text") or "").strip().upper()
        if text and text != "REMOVE":
            raise AssertionError(
                f"Expected REMOVE option text to be 'REMOVE', got {text!r}."
            )
        option.click()
        time.sleep(float(os.getenv("CUBII_AFTER_REMOVE_OPTION_TAP_SEC", "0.4")))
        self.LOGGER.info("REMOVE option tapped successfully.")

    def select_reminder_for_removal(self) -> None:
        self.LOGGER.info("Selecting reminder checkbox for removal (`cb_remove`).")
        wait = self._short_wait()
        checkbox = None
        for locator in (
            self.REMOVE_REMINDER_CHECKBOX,
            self.REMOVE_REMINDER_CHECKBOX_UIAUTOMATOR,
            self.REMOVE_REMINDER_CHECKBOX_XPATH,
            self.REMOVE_REMINDER_CHECKBOX_CLASS,
        ):
            try:
                checkbox = wait.until(ec.element_to_be_clickable(locator))
                self.LOGGER.info("Reminder checkbox located via `%s`.", locator[1])
                break
            except TimeoutException:
                continue
        if checkbox is None:
            raise AssertionError("Reminder checkbox (`cb_remove`) not found or not tappable.")

        checked = str(checkbox.get_attribute("checked")).strip().lower() == "true"
        if not checked:
            checkbox.click()
            time.sleep(float(os.getenv("CUBII_AFTER_REMINDER_CHECKBOX_TAP_SEC", "0.3")))
            checked = str(checkbox.get_attribute("checked")).strip().lower() == "true"
            if not checked:
                raise AssertionError("Reminder checkbox (`cb_remove`) did not become selected.")
        self.LOGGER.info("Reminder checkbox selected for removal.")

    def click_remove_selected_reminder_button(self) -> None:
        self.LOGGER.info("Clicking remove action button for selected reminder.")
        # App uses btnAddWorkoutReminder as context action in both add/remove states.
        clicked = self._click_if_present(
            (
                self.ADD_REMINDER_BUTTON,
                self.ADD_REMINDER_BUTTON_UIAUTOMATOR,
                self.ADD_REMINDER_BUTTON_XPATH,
            ),
            timeout=Settings.EXPLICIT_WAIT,
            label="remove action (`btnAddWorkoutReminder`)",
        )
        if not clicked:
            raise AssertionError(
                "Remove action button (`btnAddWorkoutReminder`) not found or not tappable."
            )

    def tap_workout_reminder_cancel_button(self) -> None:
        self.LOGGER.info("Tapping Workout Reminder cancel button (`Navigate up`).")
        wait = self._short_wait()
        for locator in (
            self.WORKOUT_REMINDER_CANCEL_NAV_UP_ACCESSIBILITY_ID,
            self.WORKOUT_REMINDER_CANCEL_NAV_UP_CLASS,
            self.WORKOUT_REMINDER_CANCEL_NAV_UP_UIAUTOMATOR,
            self.WORKOUT_REMINDER_CANCEL_NAV_UP_XPATH,
        ):
            try:
                el = wait.until(ec.element_to_be_clickable(locator))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_REMINDER_CANCEL_TAP_SEC", "0.4")))
                self.LOGGER.info("Workout Reminder cancel tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                continue
        raise AssertionError("Workout Reminder cancel button (`Navigate up`) not found.")

    def tap_more_back_option(self) -> None:
        self.LOGGER.info("Tapping More back option (`iv_back`).")
        wait = self._short_wait()
        for locator in (
            self.MORE_BACK_OPTION,
            self.MORE_BACK_OPTION_UIAUTOMATOR,
            self.MORE_BACK_OPTION_XPATH,
        ):
            try:
                el = wait.until(ec.element_to_be_clickable(locator))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_MORE_BACK_TAP_SEC", "0.4")))
                self.LOGGER.info("More back option tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                continue
        raise AssertionError("More back option (`iv_back`) not found or not tappable.")

    def verify_saved_workout_reminder(self) -> None:
        self.LOGGER.info("Verifying saved Workout Reminder row.")
        expected = getattr(self, "_expected_reminder", None) or {
            "hour": int(os.getenv("CUBII_REMINDER_TARGET_HOUR", "2")),
            "minute": int(os.getenv("CUBII_REMINDER_TARGET_MINUTE", "35")),
            "period": os.getenv("CUBII_REMINDER_TARGET_PERIOD", "PM").strip().upper(),
            "days": [
                d.strip()
                for d in os.getenv("CUBII_REMINDER_TARGET_DAYS", "Mon,Wed,Fri").split(",")
                if d.strip()
            ],
        }

        time_text = self._visible_text_one_of(
            (
                self.SAVED_REMINDER_TIME,
                self.SAVED_REMINDER_TIME_UIAUTOMATOR,
                self.SAVED_REMINDER_TIME_XPATH,
            ),
            "saved reminder time (`txtWorkoutTime`)",
        )
        days_text = self._visible_text_one_of(
            (
                self.SAVED_REMINDER_DAYS,
                self.SAVED_REMINDER_DAYS_UIAUTOMATOR,
                self.SAVED_REMINDER_DAYS_XPATH,
            ),
            "saved reminder days (`txtWorkoutReminderDays`)",
        )

        hour = int(expected["hour"])
        minute = int(expected["minute"])
        period = str(expected["period"]).upper()
        time_pattern = rf"\b0?{hour}:{minute:02d}\s*{period}\b"
        if not re.search(time_pattern, time_text, re.IGNORECASE):
            raise AssertionError(
                f"Saved reminder time mismatch. Expected pattern {time_pattern!r}, got {time_text!r}."
            )

        days_upper = days_text.upper()
        missing_days = [day for day in expected["days"] if day.upper() not in days_upper]
        if missing_days:
            raise AssertionError(
                f"Saved reminder days mismatch. Missing {missing_days!r} in {days_text!r}."
            )

        self.LOGGER.info(
            "Saved Workout Reminder verified: time=%r days=%r",
            time_text,
            days_text,
        )

    def _visible_text_one_of(self, locators: tuple[tuple, ...], description: str) -> str:
        wait = self._short_wait()
        last_text = ""
        for locator in locators:
            try:
                el = wait.until(ec.visibility_of_element_located(locator))
                last_text = (el.text or el.get_attribute("text") or "").strip()
                if last_text:
                    self.LOGGER.info("%s text=%r via `%s`.", description, last_text, locator[1])
                    return last_text
            except TimeoutException:
                continue
        raise AssertionError(
            f"Workout Reminder screen: {description} not visible or text empty. Last text={last_text!r}."
        )
