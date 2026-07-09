import logging  # Enable log output for Non-BLE flow steps
import math
import os  # Read optional CUBII_NON_BLE_NAME from environment
import random
import re
import time  # Short wait for model picker layout after NEXT
import calendar  # English month names for Android date picker content-desc
from datetime import date, datetime, timedelta  # Compute current/past date-time for manual workout input

from appium.webdriver.common.appiumby import AppiumBy  # Appium locator strategies (ID, XPath, UIAutomator)
from selenium.common.exceptions import TimeoutException  # Raised when explicit wait times out
from selenium.webdriver.support import expected_conditions as ec  # Predicate factories for WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait  # Explicit wait helper (no hard sleeps)

from framework.config.settings import Settings  # Framework timeout and config defaults
from framework.pages.base_page import BasePage  # Shared driver and base wait from parent class


class NonBleConnectionPage(BasePage):  # Page object for Cubii Non-BLE connection UI
    LOGGER = logging.getLogger("cubii_non_ble_page")  # Logger namespace for this page

    # Home — pairing CTAs vs Add Workout (connected). Only these locators drive Home entry / skip pairing.
    #
    # LET'S GO: empty-day card (id, UiAutomator, XPath).
    NO_WORKOUT_FOR_A_DAY_CARD_ID = "com.cubii:id/noWorkoutForADayCard"
    NO_WORKOUT_FOR_A_DAY_CARD_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/noWorkoutForADayCard")'
    )
    NO_WORKOUT_FOR_A_DAY_CARD_XPATH = (
        '//android.view.ViewGroup[@resource-id="com.cubii:id/noWorkoutForADayCard"]'
    )
    # CONNECT NEW DEVICE (id, UiAutomator, XPath).
    BTN_CONNECT_NEW_DEVICE_ID = "com.cubii:id/btnConnectDisconnect"
    BTN_CONNECT_NEW_DEVICE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnConnectDisconnect")'
    )
    BTN_CONNECT_NEW_DEVICE_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/btnConnectDisconnect"]'
    )
    # ADD WORKOUT 1 & 2 (connected Home — skip pairing when visible).
    IMG_NON_BLE_BANNER_ID = "com.cubii:id/imgNonBleBanner"
    IMG_NON_BLE_BANNER_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/imgNonBleBanner")'
    )
    IMG_NON_BLE_BANNER_XPATH = (
        '//android.widget.ImageView[@resource-id="com.cubii:id/imgNonBleBanner"]'
    )
    ADD_WORKOUT_IMAGE_VIEW_35_ID = "com.cubii:id/imageView35"
    ADD_WORKOUT_IMAGE_VIEW_35_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/imageView35")'
    )
    ADD_WORKOUT_IMAGE_VIEW_35_XPATH = (
        '//android.widget.ImageView[@resource-id="com.cubii:id/imageView35"]'
    )

    # Device type selection  # Section: Bluetooth vs Non-Bluetooth picker
    BLUETOOTH_DEVICE_PARENT_XPATH = (  # First model row container (Bluetooth option)
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[1]'  # XPath to Bluetooth row
    )
    NON_BLE_DEVICE_PARENT_XPATH = (  # Second model row container (Non-BLE option)
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[2]'  # XPath to Non-BLE row
    )
    NON_BLE_DEVICE_TAP_XPATH = (  # Clickable ViewGroup under Non-BLE row
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[2]'  # Parent FrameLayout index 2
        "/android.view.ViewGroup"  # Child group to tap for selection
    )
    BTN_NEXT_ID = "com.cubii:id/btnModelSelectionNext"  # NEXT on model/type selection screens

    # Details screen  # Section: name entry after model pick
    DETAILS_SCREEN_ID = "com.cubii:id/cnsBleSearchingParent"  # Root container for Cubii details
    CUBII_NAME_INPUT_ID = "com.cubii:id/edtCubiiName"  # EditText for user-defined Cubii name
    CUBII_MODEL_NAME_ID = "com.cubii:id/txtCubiiId"  # Read-only chosen model label
    BTN_SAVE_ID = "com.cubii:id/btn_done"  # SAVE to confirm Non-BLE device

    # Optional popups  # Section: dialogs that may appear after save
    DO_NOT_SHOW_AGAIN_ID = "com.cubii:id/cbDoNotShowAgain"  # Optional checkbox on tip dialog
    GOT_IT_CHIIR_ID = "com.cubii:id/btnChiirMotivatedGotIt"  # Optional GOT IT (motivation) button
    GOT_IT_CHANGE_MODES_ID = "com.cubii:id/btnGotItChangeModes"  # FIRST connection FTUE GOT IT

    # Post connection validations  # Section: Home screen after pairing
    DEVICE_CARD_ID = "com.cubii:id/lytConnectDisconnect"  # Device control card container
    DEVICE_NAME_TEXT_ID = "com.cubii:id/txtCubiiNameOrConnectStateText"  # Device name line on card
    DEVICE_DETAILS_TEXT_ID = "com.cubii:id/txtConnectionTimeDetails"  # Connection detail line on card
    DEVICE_DETAILS_TEXT_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtConnectionTimeDetails"]'
    )
    DEVICE_DETAILS_TEXT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtConnectionTimeDetails")'
    )
    CHANGE_DEVICE_BTN_ID = "com.cubii:id/btnChangeDevices"  # Change device button on Home
    # Broader than By.ID: some builds use TextView/ImageButton; card scope matches Home layout.
    CHANGE_DEVICE_XPATH_ANY = '//*[@resource-id="com.cubii:id/btnChangeDevices"]'
    CHANGE_DEVICE_CARD_SCOPED_XPATH = (
        '//android.view.ViewGroup[@resource-id="com.cubii:id/lytConnectDisconnect"]'
        '//*[@resource-id="com.cubii:id/btnChangeDevices"]'
    )
    CHANGE_DEVICE_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btnChangeDevices")'

    # Add / Edit Manual Workout screen — after tapping Add Workout from Home (Non-BLE).
    TXT_ADD_EDIT_WORKOUT_TITLE_ID = "com.cubii:id/txtAddEditWorkoutTitle"
    TXT_ADD_EDIT_WORKOUT_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtAddEditWorkoutTitle"]'
    )
    ADD_MANUAL_WORKOUT_TITLE_EXPECTED = "Add Workout"
    EDIT_MANUAL_WORKOUT_TITLE_EXPECTED = "Edit Workout"
    ADD_WORKOUT_SCREEN_START_DATE_ID = "com.cubii:id/textView83"
    ADD_WORKOUT_SCREEN_START_DATE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView83"]'
    )
    ADD_WORKOUT_SCREEN_START_TIME_ID = "com.cubii:id/textView85"
    ADD_WORKOUT_SCREEN_START_TIME_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView85"]'
    )
    ADD_WORKOUT_SCREEN_DURATION_ID = "com.cubii:id/textView82"
    ADD_WORKOUT_SCREEN_DURATION_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView82"]'
    )
    ADD_WORKOUT_SCREEN_STRIDES_ID = "com.cubii:id/textView89"
    ADD_WORKOUT_SCREEN_STRIDES_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView89"]'
    )
    ADD_WORKOUT_SCREEN_RESISTANCE_ID = "com.cubii:id/textView90"
    ADD_WORKOUT_SCREEN_RESISTANCE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView90"]'
    )
    START_DATE_VALUE_ID = "com.cubii:id/txtStartDateWorkout"
    START_TIME_VALUE_ID = "com.cubii:id/txtStartTimeWorkout"
    DURATION_FIELD_ID = "com.cubii:id/edtHours"
    DURATION_HOURS_PICKER_ID = "com.cubii:id/options1"
    DURATION_MINUTES_PICKER_ID = "com.cubii:id/options2"
    DURATION_SUBMIT_BUTTON_ID = "com.cubii:id/btnSubmit"
    STRIDES_INPUT_ID = "com.cubii:id/editTextManualWorkoutStrides"
    RESISTANCE_SLIDER_ID = "com.cubii:id/seekBar"
    SAVE_MANUAL_WORKOUT_BUTTON_ID = "com.cubii:id/btnSaveManualEntry"
    TIME_VALIDATION_ERROR_ID = "com.cubii:id/txtTimeErrorText"
    TIME_VALIDATION_ERROR_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtTimeErrorText"]'
    )
    STRIDES_VALIDATION_ERROR_ID = "com.cubii:id/txtStridesErrorText"
    STRIDES_VALIDATION_ERROR_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtStridesErrorText"]'
    )
    TIME_VALIDATION_ERROR_EXPECTED_TEXT = "You cannot enter data for future time"
    TIME_VALIDATION_ERROR_OVERLAP_TEXT = "This time is overlapping another workout entry."
    MANUAL_CONFIRMATION_POPUP_CARD_ID = "com.cubii:id/cardChiirMotivatedParent"
    MANUAL_CONFIRMATION_TITLE_ID = "com.cubii:id/txtManualEntryInfoTitle"
    MANUAL_CONFIRMATION_CALORIES_LAYOUT_ID = "com.cubii:id/caloriesLayout"
    MANUAL_CONFIRMATION_DISTANCE_LAYOUT_ID = "com.cubii:id/distanceLayout"
    MANUAL_CONFIRMATION_DURATION_LAYOUT_ID = "com.cubii:id/durationLayout"
    MANUAL_CONFIRMATION_STRIDES_VALUE_ID = "com.cubii:id/stridesTextView"
    MANUAL_CONFIRMATION_CALORIES_VALUE_ID = "com.cubii:id/caloriesTextView"
    MANUAL_CONFIRMATION_DISTANCE_VALUE_ID = "com.cubii:id/distanceTextView"
    MANUAL_CONFIRMATION_DURATION_VALUE_ID = "com.cubii:id/durationTextView"
    MANUAL_CONFIRMATION_GOT_IT_BUTTON_ID = "com.cubii:id/btnManualEntryInfoGotIt"
    MANUAL_CONFIRMATION_GOT_IT_BUTTON_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnManualEntryInfoGotIt"]'
    )
    MANUAL_CONFIRMATION_GOT_IT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnManualEntryInfoGotIt")'
    )
    ANDROID_OK_BUTTON_ID = "android:id/button1"
    TIME_PICKER_CONTAINER_XPATH = (
        '//android.widget.TimePicker[@resource-id="android:id/timePicker"]/android.widget.LinearLayout'
    )
    TIME_PICKER_RADIAL_ID = "android:id/radial_picker"
    TIME_PICKER_AM_LABEL_ID = "android:id/am_label"
    TIME_PICKER_PM_LABEL_ID = "android:id/pm_label"
    TIME_PICKER_HOURS_CHIP_ID = "android:id/hours"
    TIME_PICKER_MINUTES_CHIP_ID = "android:id/minutes"
    DATE_PICKER_CONTAINER_XPATH = '//android.widget.DatePicker'
    IN_PROGRESS_TAB_CANDIDATE_LOCATORS = (
        (AppiumBy.ID, "com.cubii:id/navigation_progress"),
        (AppiumBy.ID, "com.cubii:id/navigation_activity"),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Progress")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Progress")'),
        (AppiumBy.XPATH, '//*[contains(@text, "Progress")]'),
    )
    # Progress / In Progress — Add Manual Workout (header or FAB-style control).
    BTN_ADD_MANUAL_WORKOUT_ID = "com.cubii:id/btnAddManualWorkout"
    BTN_ADD_MANUAL_WORKOUT_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnAddManualWorkout"]'
    )
    BTN_ADD_MANUAL_WORKOUT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnAddManualWorkout")'
    )
    # Bottom nav Home — order: content-desc (Material), first nav icon (legacy layouts), UiAutomator fallbacks.
    HOME_TAB_CANDIDATE_LOCATORS = (
        (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Home"]'),
        (
            AppiumBy.XPATH,
            '(//android.widget.ImageView[@resource-id="com.cubii:id/navigation_bar_item_icon_view"])[1]',
        ),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Home")'),
    )
    ACTIVITY_LOG_ROW_ID = "com.cubii:id/cnsLayoutActivityLogRoot"
    ACTIVITY_LOG_TIME_ID = "com.cubii:id/txtWorkoutDayTime"
    ACTIVITY_LOG_MANUAL_INDICATOR_ID = "com.cubii:id/linLayoutManualOptionIndicator"
    ACTIVITY_LOG_METRIC_VALUE_1_ID = "com.cubii:id/txtMetricsValue1"
    ACTIVITY_LOG_METRIC_VALUE_2_ID = "com.cubii:id/txtMetricsValue2"
    ACTIVITY_LOG_METRIC_VALUE_3_ID = "com.cubii:id/txtMetricsValue3"
    ACTIVITY_LOG_METRIC_VALUE_4_ID = "com.cubii:id/txtMetricsValue4"

    # Cubii model picker — XPath + UiAutomator per product (QA locators; visibility depends on scroll position).
    CUBII_GO_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[1]'
        "/android.view.ViewGroup"
    )
    CUBII_GO_UIAUTOMATOR = 'new UiSelector().className("android.view.ViewGroup").instance(5)'

    CUBII_JR1_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[2]'
        "/android.view.ViewGroup"
    )
    CUBII_JR1_UIAUTOMATOR = 'new UiSelector().className("android.view.ViewGroup").instance(7)'

    CUBII_JR2_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[1]'
        "/android.view.ViewGroup"
    )
    CUBII_JR2_UIAUTOMATOR = 'new UiSelector().className("android.view.ViewGroup").instance(5)'

    CUBII_TOTAL_BODY_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[2]'
        "/android.view.ViewGroup"
    )
    CUBII_TOTAL_BODY_UIAUTOMATOR = 'new UiSelector().className("android.view.ViewGroup").instance(7)'

    CUBII_MOVE_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[3]'
        "/android.view.ViewGroup"
    )
    CUBII_MOVE_UIAUTOMATOR = 'new UiSelector().className("android.view.ViewGroup").instance(9)'

    CUBII_GROOVE_NAVY_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[1]'
        "/android.view.ViewGroup"
    )
    CUBII_GROOVE_NAVY_UIAUTOMATOR = 'new UiSelector().className("android.view.ViewGroup").instance(5)'

    CUBII_GROOVE_LAVENDER_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[2]'
        "/android.view.ViewGroup"
    )
    CUBII_GROOVE_LAVENDER_UIAUTOMATOR = 'new UiSelector().className("android.view.ViewGroup").instance(7)'

    CUBII_GROOVE_SAND_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[2]'
        "/android.view.ViewGroup"
    )
    CUBII_GROOVE_SAND_UIAUTOMATOR = 'new UiSelector().className("android.view.ViewGroup").instance(7)'

    CUBII_MODEL_LOCATORS = (
        ("Cubii Go", CUBII_GO_XPATH, CUBII_GO_UIAUTOMATOR),
        ("Cubii JR1", CUBII_JR1_XPATH, CUBII_JR1_UIAUTOMATOR),
        ("Cubii JR2", CUBII_JR2_XPATH, CUBII_JR2_UIAUTOMATOR),
        ("Cubii Total Body", CUBII_TOTAL_BODY_XPATH, CUBII_TOTAL_BODY_UIAUTOMATOR),
        ("Cubii Move", CUBII_MOVE_XPATH, CUBII_MOVE_UIAUTOMATOR),
        ("Cubii Groove Navy", CUBII_GROOVE_NAVY_XPATH, CUBII_GROOVE_NAVY_UIAUTOMATOR),
        ("Cubii Groove Lavender", CUBII_GROOVE_LAVENDER_XPATH, CUBII_GROOVE_LAVENDER_UIAUTOMATOR),
        ("Cubii Groove Sand", CUBII_GROOVE_SAND_XPATH, CUBII_GROOVE_SAND_UIAUTOMATOR),
    )

    MODEL_LABEL_VISIBILITY_ALIASES = {
        "Cubii Groove Lavender": ("Cubii Groover Lavender",),
    }

    def __init__(self, driver):  # Construct page with Appium driver instance
        super().__init__(driver)  # Initialize BasePage wait and driver reference

    def is_non_ble_device_already_connected_on_home(self, timeout=None):
        """True if any Home Add Workout entry is visible (connected-home — skip pairing wizard).

        Pairing is driven only from LET'S GO / CONNECT NEW DEVICE / empty-day card via
        `_tap_home_entry_cta`; Add Workout locators mean manual entry is available, not “tap to pair”.
        """
        wait_sec = timeout if timeout is not None else int(
            os.getenv("CUBII_NON_BLE_ALREADY_CONNECTED_PROBE_SEC", "10")
        )
        per = max(1.5, float(wait_sec) / 6.0)

        def _wait_any_add_workout_visible():
            for by, val in self._add_workout_entry_locators():
                try:
                    WebDriverWait(self.driver, per).until(
                        ec.visibility_of_element_located((by, val))
                    )
                    return True
                except TimeoutException:
                    continue
            return False

        for attempt in (1, 2):
            if self._any_add_workout_displayed_now():
                self.LOGGER.info(
                    "Non-BLE skip: Add Workout entry visible on Home (connected; skip pairing)."
                )
                return True
            if _wait_any_add_workout_visible():
                self.LOGGER.info(
                    "Non-BLE skip: Add Workout entry visible after short wait."
                )
                return True
            if attempt == 1:
                self._scroll_home_content_down_small()
                time.sleep(0.2)
        return False

    def _any_add_workout_displayed_now(self):  # Fast poll; no explicit wait
        for by, val in self._add_workout_entry_locators():
            try:
                for candidate in self.driver.find_elements(by, val):
                    if candidate.is_displayed():
                        return True
            except Exception:
                continue
        return False

    def connect_non_ble_device_end_to_end(self, cubii_name=None):  # Run full Non-BLE flow from Home
        name = cubii_name or os.getenv("CUBII_NON_BLE_NAME", "QA NonBLE Cubii")  # Resolve display name from arg or env
        self.LOGGER.info("Step Started: Non-BLE device end-to-end flow.")  # Log flow start for reports
        if self.is_non_ble_device_already_connected_on_home():
            self.LOGGER.info(
                "Skipping Non-BLE pairing: Add Workout visible on Home (already connected)."
            )
            return
        try:  # Catch Selenium timeouts and assertion failures in one block
            self._tap_home_entry_cta()  # Tap LET'S GO or CONNECT NEW DEVICE
            self._select_non_ble_device_type()  # Choose Non-Bluetooth path
            self._click_model_selection_next()  # Advance past device type screen
            self._tap_visible_model_card_on_picker()  # Whatever model is showing — select it (no list scroll)
            self._click_model_selection_next()  # Advance after model selection
            self._fill_cubii_details_and_save(name)  # Enter name, assert model text, SAVE
            self._handle_optional_popups()  # Dismiss optional dialogs if shown
            self.LOGGER.info("Step Passed: Non-BLE device end-to-end flow completed.")  # Log successful completion
        except (TimeoutException, AssertionError) as exc:  # Map wait/assert failures to single error type
            self.LOGGER.exception("Non-BLE flow failed: %s", exc)  # Record stack trace for debugging
            raise AssertionError(f"Non-BLE end-to-end flow failed. Error: {exc}") from exc  # Fail scenario with context

    def validate_non_ble_connected_state(self):  # Assert Home shows connected Non-BLE UI
        self.LOGGER.info("Step Started: Validate Non-BLE connected state on Home.")  # Log validation phase start

        add_workout = self._wait_visible_any_add_workout_on_home()
        assert add_workout.is_displayed(), (
            "No Add Workout entry visible on Home (expected imgNonBleBanner or imageView35)."
        )
        self.LOGGER.info(
            "Step Passed: Add Workout entry visible on Home (`imgNonBleBanner` or `imageView35`)."
        )

        card = self._wait_visible(AppiumBy.ID, self.DEVICE_CARD_ID, "Device Card")  # Wait for device card layout
        assert card.is_displayed(), "Device card is not visible."  # Ensure card is on screen
        self.LOGGER.info("Step Passed: Device card is visible.")  # Log card presence

        name_el = self._wait_visible(AppiumBy.ID, self.DEVICE_NAME_TEXT_ID, "Device Name")  # Wait for name TextView
        assert (name_el.text or "").strip(), "Device name is empty."  # Name must not be blank
        try:
            details_el = self._wait_visible(
                AppiumBy.ID,
                self.DEVICE_DETAILS_TEXT_ID,
                "Connection Details",
                timeout=int(os.getenv("CUBII_HOME_CONNECTION_DETAILS_WAIT_SEC", "5")),
            )
            details_txt = (details_el.text or "").strip()
            if details_txt:
                self.LOGGER.info(
                    "Step Passed: Device name and connection details visible (name=%s).",
                    (name_el.text or "").strip(),
                )
            else:
                self.LOGGER.warning(
                    "Connection Details TextView visible but empty; some builds omit copy."
                )
        except TimeoutException:
            self.LOGGER.warning(
                "Connection Details (`%s`) not found in optional window; continuing validation.",
                self.DEVICE_DETAILS_TEXT_ID,
            )

        self.LOGGER.info(
            "Step Passed: Device name visible (`%s`).",
            (name_el.text or "").strip(),
        )

        change_btn = self._wait_visible_change_device_on_home()  # Scroll Home until Change Device is on-screen, then find it
        assert change_btn.is_displayed(), "Change Device control is not visible."
        self.LOGGER.info("Step Passed: Change Device is visible.")

    def open_add_manual_workout_from_home(self):  # Step 1–2 bridge: probe Add Workout → tap → wait for editor screen
        self.LOGGER.info("Step Started: Add Manual Workout — probe Add Workout on Home / connect Non-BLE if absent.")
        if self._probe_and_click_visible_add_workout_entry():
            self.LOGGER.info(
                "Add Workout entry was visible and tapped; validating whether editor opens."
            )
            if self._is_manual_workout_screen_visible(timeout=10):
                self.LOGGER.info(
                    "Manual workout screen became visible after first Add Workout tap."
                )
                return
            if self._click_first_visible_add_workout_entry():
                self.LOGGER.info(
                    "Retried Add Workout tap after first transition timeout; checking editor screen again."
                )
                if self._is_manual_workout_screen_visible(timeout=10):
                    self.LOGGER.info(
                        "Manual workout screen became visible after second Add Workout tap."
                    )
                    return
            self.LOGGER.warning(
                "Add Workout tap succeeded but manual workout screen did not appear. "
                "Likely disconnected/intermediate state; returning to Home and running Non-BLE connect flow."
            )
        else:
            self.LOGGER.info(
                "No Add Workout entry after Home probe scrolls; running Non-BLE connection flow."
            )
        self._return_to_home_surface_before_connect_flow()
        self.connect_non_ble_device_end_to_end()
        self._wait_visible_any_add_workout_on_home()
        if not self._click_first_visible_add_workout_entry():
            raise AssertionError(
                "Add Workout entry not clickable after Non-BLE pairing "
                "(expected imgNonBleBanner or imageView35)."
            )
        self.LOGGER.info("Clicked Add Workout entry after pairing; continuing to editor screen.")

        if not self._is_manual_workout_screen_visible(timeout=Settings.EXPLICIT_WAIT):
            raise AssertionError(
                "Failed to navigate to Add Manual Workout screen after Add Workout tap. "
                "Neither title nor core manual workout fields became visible."
            )
        self.LOGGER.info(
            "Step Passed: Navigated past Add Workout tap; Add / Edit workout title is visible."
        )

    def _is_manual_workout_screen_visible(self, timeout=6):
        locators = (
            (AppiumBy.ID, self.TXT_ADD_EDIT_WORKOUT_TITLE_ID, "Add Workout title"),
            (AppiumBy.ID, self.START_DATE_VALUE_ID, "Start Date value"),
            (AppiumBy.ID, self.START_TIME_VALUE_ID, "Start Time value"),
            (AppiumBy.ID, self.STRIDES_INPUT_ID, "Strides input"),
        )
        deadline = time.monotonic() + max(1, int(timeout))
        while time.monotonic() < deadline:
            for by, value, label in locators:
                try:
                    el = WebDriverWait(self.driver, 1).until(
                        ec.visibility_of_element_located((by, value))
                    )
                    if el.is_displayed():
                        self.LOGGER.info(
                            "Manual workout screen probe matched `%s` via locator=(%s, %s).",
                            label,
                            by,
                            value,
                        )
                        return True
                except Exception:
                    continue
            time.sleep(0.2)
        return False

    def verify_add_manual_workout_screen(self):  # Step 2–3: title copy + mandatory field rows visible (and boxed)
        self.LOGGER.info(
            "Step Started: Validate Add Manual Workout screen — title text and manual entry rows."
        )
        title_via_id = self._wait_visible(
            AppiumBy.ID, self.TXT_ADD_EDIT_WORKOUT_TITLE_ID, "Add Workout screen title"
        )
        observed = (title_via_id.text or "").strip()
        assert observed == self.ADD_MANUAL_WORKOUT_TITLE_EXPECTED, (
            f"Expected workout title {self.ADD_MANUAL_WORKOUT_TITLE_EXPECTED!r}, got {observed!r}."
        )
        self.LOGGER.info("Title assertion passed: `%s`.", observed)

        start_date_el = self._wait_visible(
            AppiumBy.ID, self.ADD_WORKOUT_SCREEN_START_DATE_ID, "Start Date label (textView83)"
        )
        self._assert_label_has_display_box(start_date_el, "Start Date")
        self.LOGGER.info("Field visible & boxed: Start Date (textView83).")

        start_time_el = self._wait_visible(
            AppiumBy.ID, self.ADD_WORKOUT_SCREEN_START_TIME_ID, "Start Time label (textView85)"
        )
        self._assert_label_has_display_box(start_time_el, "Start Time")
        self.LOGGER.info("Field visible & boxed: Start Time (textView85).")

        duration_el = self._wait_visible(
            AppiumBy.ID, self.ADD_WORKOUT_SCREEN_DURATION_ID, "Duration label (textView82)"
        )
        self._assert_label_has_display_box(duration_el, "Duration")
        self.LOGGER.info("Field visible & boxed: Duration (textView82).")

        strides_el = self._wait_visible(
            AppiumBy.ID, self.ADD_WORKOUT_SCREEN_STRIDES_ID, "Strides label (textView89)"
        )
        self._assert_label_has_display_box(strides_el, "Strides")
        self.LOGGER.info("Field visible & boxed: Strides (textView89).")

        resistance_el = self._wait_visible(
            AppiumBy.ID,
            self.ADD_WORKOUT_SCREEN_RESISTANCE_ID,
            "Resistance label (textView90)",
        )
        self._assert_label_has_display_box(resistance_el, "Resistance")
        self.LOGGER.info("Field visible & boxed: Resistance (textView90).")

        secondary_checks = (
            (AppiumBy.XPATH, self.ADD_WORKOUT_SCREEN_START_DATE_XPATH, "Start Date XPath"),
            (AppiumBy.XPATH, self.TXT_ADD_EDIT_WORKOUT_TITLE_XPATH, "Title XPath"),
        )
        for by, val, lbl in secondary_checks:
            try:
                el = WebDriverWait(self.driver, 3).until(
                    ec.visibility_of_element_located((by, val))
                )
                self.LOGGER.debug("Secondary XPath still visible for %s.", lbl)
                assert el.is_displayed()
            except TimeoutException:
                self.LOGGER.debug("Secondary locator optional miss (non-fatal): %s", lbl)

        self.LOGGER.info(
            "Step Passed: Add Manual Workout UI — title, Start Date/Time, Duration, Strides, Resistance present."
        )

    def select_start_date_current_and_confirm(self):
        self.LOGGER.info("Step: Select Start Date (current date) and click OK.")
        start_date_field = self._wait_clickable(
            AppiumBy.ID, self.START_DATE_VALUE_ID, "Start Date value field"
        )
        start_date_field.click()
        self._wait_visible(
            AppiumBy.XPATH, self.DATE_PICKER_CONTAINER_XPATH, "Date picker container", timeout=8
        )
        self._wait_clickable(
            AppiumBy.ID, self.ANDROID_OK_BUTTON_ID, "Date picker OK button", timeout=8
        ).click()
        value_after = (self._wait_visible(
            AppiumBy.ID, self.START_DATE_VALUE_ID, "Start Date value after save"
        ).text or "").strip()
        assert value_after, "Start Date value is empty after confirming current date."
        self.LOGGER.info("Step Passed: Start Date selected as `%s`.", value_after)

    def select_start_date_yesterday_and_confirm(self):
        """
        Open Start Date picker, move to previous calendar month when required (today is the 1st),
        tap yesterday's day, OK. Asserts field parses to calendar yesterday (locale-flexible).
        """
        yesterday = date.today() - timedelta(days=1)
        self.LOGGER.info(
            "Step: Select Start Date as yesterday (%s) and confirm.",
            yesterday.isoformat(),
        )
        start_date_field = self._wait_clickable(
            AppiumBy.ID, self.START_DATE_VALUE_ID, "Start Date value field"
        )
        start_date_field.click()
        self._wait_visible(
            AppiumBy.XPATH, self.DATE_PICKER_CONTAINER_XPATH, "Date picker container", timeout=8
        )
        time.sleep(0.35)

        today = date.today()
        need_prev_month = not (
            yesterday.year == today.year and yesterday.month == today.month
        )
        if need_prev_month:
            if self._click_calendar_previous_month_button():
                time.sleep(0.5)
            else:
                self.LOGGER.warning(
                    "Previous-month button not found; attempting day tap for day=%s anyway.",
                    yesterday.day,
                )

        tapped = self._try_tap_calendar_day_by_content_desc(
            yesterday
        ) or self._try_tap_calendar_day_number(yesterday.day)
        if not tapped:
            raise AssertionError(
                f"Could not tap calendar day {yesterday.day} for yesterday ({yesterday.isoformat()})."
            )

        self._wait_clickable(
            AppiumBy.ID, self.ANDROID_OK_BUTTON_ID, "Date picker OK button", timeout=8
        ).click()
        value_after = (self._wait_visible(
            AppiumBy.ID, self.START_DATE_VALUE_ID, "Start Date value after save"
        ).text or "").strip()
        assert value_after, "Start Date value is empty after confirming yesterday."
        parsed = self._parse_start_date_field_to_date(value_after)
        assert parsed is not None, f"Could not parse Start Date field value: {value_after!r}"
        assert parsed == yesterday, (
            f"Expected Start Date {yesterday.isoformat()}, parsed field as {parsed.isoformat()} "
            f"(raw={value_after!r})."
        )
        self.LOGGER.info("Step Passed: Start Date selected as yesterday (`%s`).", value_after)

    def _click_calendar_previous_month_button(self):
        """Material / framework date pickers: go one month back."""
        candidates = (
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().descriptionContains("Previous")',
                "Previous month (description Contains Previous)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().descriptionContains("previous")',
                "Previous month (description Contains previous)",
            ),
            (
                AppiumBy.XPATH,
                '//android.widget.ImageButton[contains(@content-desc,"Previous")]',
                "Previous month ImageButton content-desc",
            ),
            (AppiumBy.ID, "android:id/prev", "android:id/prev"),
            (
                AppiumBy.XPATH,
                '//*[contains(@resource-id,"prev") and (@clickable="true" or @focusable="true")]',
                "resource-id contains prev clickable",
            ),
        )
        for by, loc, label in candidates:
            if self._click_if_present(by, loc, label, timeout=2):
                return True
        return False

    def _try_tap_calendar_day_by_content_desc(self, target_date):
        """
        Stock Android calendar (month_view): day cells are android.view.View with
        content-desc like '09 May 2026' and often empty text — TextView locators miss them.
        Month names must match the picker (English); strftime %%B is locale-dependent.
        """
        month_en = calendar.month_name[target_date.month]
        candidates = [
            f"{target_date.day:02d} {month_en} {target_date.year}",
            f"{target_date.day} {month_en} {target_date.year}",
        ]
        seen = []
        for cd in candidates:
            if cd in seen:
                continue
            seen.append(cd)
            xpaths = (
                f'//*[@resource-id="android:id/month_view"]//android.view.View[@content-desc="{cd}"]',
                f'//android.view.View[@content-desc="{cd}"]',
            )
            for xp in xpaths:
                try:
                    nodes = self.driver.find_elements(AppiumBy.XPATH, xp)
                except Exception:
                    continue
                for node in nodes:
                    if not node.is_displayed():
                        continue
                    if self._click_calendar_day_element(node, cd):
                        return True
            try:
                el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, cd)
                if el.is_displayed() and self._click_calendar_day_element(el, cd):
                    return True
            except Exception:
                pass
            try:
                safe = cd.replace('"', '\\"')
                els = self.driver.find_elements(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().className("android.view.View").description("{safe}")',
                )
                for el in els:
                    if el.is_displayed() and self._click_calendar_day_element(el, cd):
                        return True
            except Exception:
                continue
        return False

    def _try_tap_calendar_day_number(self, day_int):
        """Tap a visible day cell matching day_int. Supports legacy DatePicker + Material dialogs."""
        day_str = str(int(day_int))
        day_strings = [day_str]
        if day_int < 10:
            day_strings.append(day_str.zfill(2))

        xpath_patterns = (
            '//android.widget.DatePicker//android.widget.TextView[@text="{d}"]',
            '//android.widget.DatePicker//android.widget.CheckedTextView[@text="{d}"]',
            '//*[contains(@resource-id,"date_picker") or contains(@resource-id,"datepicker")]'
            '//android.widget.TextView[@text="{d}"]',
            '//*[contains(@resource-id,"mtrl") or contains(@resource-id,"material")]'
            '//android.widget.TextView[@text="{d}"]',
            '//*[contains(@resource-id,"month")]//*[contains(@resource-id,"grid")]'
            '//android.widget.TextView[@text="{d}"]',
            '//android.widget.GridLayout//android.widget.TextView[@text="{d}"]',
            '//*[contains(@class,"RecyclerView")]//android.widget.TextView[@text="{d}"]',
            '//android.widget.Button[@text="{d}"]',
            '//*[@resource-id="android:id/month_view"]//android.view.View[@text="{d}"]',
        )

        for d in day_strings:
            for pattern in xpath_patterns:
                xp = pattern.format(d=d)
                try:
                    nodes = self.driver.find_elements(AppiumBy.XPATH, xp)
                except Exception:
                    continue
                visible = [n for n in nodes if n.is_displayed()]
                if not visible:
                    continue
                for prefer_clickable in (True, False):
                    for node in reversed(visible):
                        try:
                            if prefer_clickable:
                                if str(node.get_attribute("clickable")).lower() == "false":
                                    continue
                            if self._click_calendar_day_element(node, d):
                                return True
                        except Exception:
                            continue

        for d in day_strings:
            try:
                els = self.driver.find_elements(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().className("android.widget.TextView").text("{d}")',
                )
                visible = [e for e in els if e.is_displayed()]
                for node in reversed(visible):
                    if self._click_calendar_day_element(node, d):
                        return True
            except Exception:
                continue
        return False

    def _click_calendar_day_element(self, node, day_label):
        """Click day cell; fall back to tapGesture at bounds center if WebDriver click fails."""
        try:
            node.click()
            self.LOGGER.info("Tapped calendar day `%s`.", day_label)
            return True
        except Exception as exc:
            self.LOGGER.debug("WebDriver click on day `%s` failed: %s", day_label, exc)
        try:
            rect = node.rect
            cx = int(rect["x"] + rect["width"] / 2)
            cy = int(rect["y"] + rect["height"] / 2)
            self.driver.execute_script("mobile: clickGesture", {"x": cx, "y": cy})
            self.LOGGER.info(
                "Tapped calendar day `%s` via coordinate (%s,%s).", day_label, cx, cy
            )
            return True
        except Exception as exc:
            self.LOGGER.debug("Coordinate tap for day `%s` failed: %s", day_label, exc)
            return False

    def _parse_start_date_field_to_date(self, raw):
        """Parse Start Date field text to datetime.date (US MDY first, then DMY, ISO)."""
        text = (raw or "").strip()
        if not text:
            return None
        take = text.split()[0] if text else text
        for fmt in ("%m/%d/%Y", "%m/%d/%y", "%Y-%m-%d"):
            try:
                return datetime.strptime(take[:10], fmt).date()
            except ValueError:
                continue
        m = re.match(
            r"^(\d{1,2})/(\d{1,2})/(\d{4})$",
            take,
        )
        if m:
            a, b, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
            try:
                return date(y, a, b)
            except ValueError:
                try:
                    return date(y, b, a)
                except ValueError:
                    return None
        return None

    def select_start_time_past_and_confirm(self):
        self.LOGGER.info("Step: Select Start Time as current time minus 1 hour 1 minute and click OK.")
        target_past = datetime.now() - timedelta(hours=1, minutes=1)
        observed_time = ""
        max_attempts = 2

        for idx in range(1, max_attempts + 1):
            start_time_field = self._wait_clickable(
                AppiumBy.ID, self.START_TIME_VALUE_ID, "Start Time value field"
            )
            start_time_field.click()
            self._wait_visible(
                AppiumBy.XPATH, self.TIME_PICKER_CONTAINER_XPATH, "Time picker container", timeout=8
            )

            hour_set = self._try_set_picker_text(
                "android:id/hours", target_past.strftime("%I").lstrip("0") or "12"
            )
            minute_set = self._try_set_picker_text(
                "android:id/minutes", target_past.strftime("%M")
            )
            if not (hour_set and minute_set):
                self._set_time_using_radial_picker(target_past)
            self._set_picker_meridiem_if_present(target_past.strftime("%p"))

            self._wait_clickable(
                AppiumBy.ID, self.ANDROID_OK_BUTTON_ID, "Time picker OK button", timeout=8
            ).click()

            observed_time = (self._wait_visible(
                AppiumBy.ID, self.START_TIME_VALUE_ID, "Start Time value after save"
            ).text or "").strip()
            assert observed_time, "Start Time value is empty after confirming picker."
            if self._is_displayed_time_strictly_past(observed_time):
                self._last_selected_start_time = observed_time
                self.LOGGER.info(
                    "Step Passed: Start Time selected near current-1h target `%s` (observed `%s`, attempt %s).",
                    target_past.strftime("%I:%M %p"),
                    observed_time,
                    idx,
                )
                return
            self.LOGGER.warning(
                "Observed Start Time `%s` is not past after attempt %s for target `%s`; retrying once.",
                observed_time,
                idx,
                target_past.strftime("%I:%M %p"),
            )

        raise AssertionError(
            "Could not set Start Time to a past value near current-1h1m target. "
            f"Target={target_past.strftime('%I:%M %p')}, last observed={observed_time!r}"
        )

    def select_start_time_random_past_and_confirm(self):
        now_local = datetime.now()
        minutes_since_midnight = (now_local.hour * 60) + now_local.minute
        # Pick any valid past minute from today relative to current clock time.
        minutes_back = random.randint(1, max(1, minutes_since_midnight))
        target_past = datetime.now() - timedelta(minutes=minutes_back)
        self.LOGGER.info(
            "Step: Select Start Time as random past time (%s minutes back from now): `%s`.",
            minutes_back,
            target_past.strftime("%I:%M %p"),
        )
        observed_time = ""
        max_attempts = 2

        for idx in range(1, max_attempts + 1):
            start_time_field = self._wait_clickable(
                AppiumBy.ID, self.START_TIME_VALUE_ID, "Start Time value field"
            )
            start_time_field.click()
            self._wait_visible(
                AppiumBy.XPATH, self.TIME_PICKER_CONTAINER_XPATH, "Time picker container", timeout=8
            )

            hour_set = self._try_set_picker_text(
                self.TIME_PICKER_HOURS_CHIP_ID, target_past.strftime("%I").lstrip("0") or "12"
            )
            minute_set = self._try_set_picker_text(
                self.TIME_PICKER_MINUTES_CHIP_ID, target_past.strftime("%M")
            )
            if not (hour_set and minute_set):
                self._set_time_using_radial_picker(target_past)
            self._set_picker_meridiem_if_present(target_past.strftime("%p"))

            self._wait_clickable(
                AppiumBy.ID, self.ANDROID_OK_BUTTON_ID, "Time picker OK button", timeout=8
            ).click()

            observed_time = (self._wait_visible(
                AppiumBy.ID, self.START_TIME_VALUE_ID, "Start Time value after save"
            ).text or "").strip()
            assert observed_time, "Start Time value is empty after confirming picker."
            if self._is_displayed_time_strictly_past(observed_time):
                self._last_selected_start_time = observed_time
                self.LOGGER.info(
                    "Step Passed: Start Time selected as random past `%s` (observed `%s`, attempt %s).",
                    target_past.strftime("%I:%M %p"),
                    observed_time,
                    idx,
                )
                return
            self.LOGGER.warning(
                "Observed Start Time `%s` is not past after attempt %s for random target `%s`; retrying once.",
                observed_time,
                idx,
                target_past.strftime("%I:%M %p"),
            )

        raise AssertionError(
            "Could not set Start Time to random past value. "
            f"Target={target_past.strftime('%I:%M %p')}, last observed={observed_time!r}"
        )

    def select_duration_and_submit(self):
        self.LOGGER.info("Step: Open Duration picker and set duration (custom override or Start-Time-based).")
        duration_after = ""
        target_hours, target_minutes = 0, 0
        target_text = ""

        # Keep primary behavior as one attempt; only retry when result is out-of-range.
        max_apply_attempts = 4
        for attempt in range(1, max_apply_attempts + 1):
            duration_field = self._wait_clickable(AppiumBy.ID, self.DURATION_FIELD_ID, "Duration field")
            duration_before = (duration_field.text or "").strip()
            target_hours, target_minutes = self._resolve_duration_target()
            target_text = f"{str(target_hours).zfill(2)}:{str(target_minutes).zfill(2)}"
            duration_field.click()
            hours_picker = self._wait_visible(
                AppiumBy.ID, self.DURATION_HOURS_PICKER_ID, "Duration hours picker", timeout=8
            )
            minutes_picker = self._wait_visible(
                AppiumBy.ID, self.DURATION_MINUTES_PICKER_ID, "Duration minutes picker", timeout=8
            )

            # First try direct value set for duration pickers with strict 2-digit verification.
            hours_set = self._try_set_duration_picker_value(
                self.DURATION_HOURS_PICKER_ID, str(target_hours).zfill(2)
            )
            minutes_set = self._try_set_duration_picker_value(
                self.DURATION_MINUTES_PICKER_ID, str(target_minutes).zfill(2)
            )

            bef_h, bef_m = self._parse_duration_text(duration_before)
            before_total_min = bef_h * 60 + bef_m
            # 00:00 is invalid for this flow; wheels often ignore flaky send_keys — always swipe pickers from zero state.
            if before_total_min < 1:
                hours_set = minutes_set = False
                self.LOGGER.info(
                    "Duration was 00:00 before pick; skipping direct typing and using wheel gestures only."
                )
            elif attempt >= 2:
                # Previous attempt kept an invalid/zero duration; avoid repeating send_keys that can lie about success.
                hours_set = minutes_set = False
                self.LOGGER.info(
                    "Duration retry attempt %s: using wheel gestures only.", attempt
                )

            # Fallback: rotate wheel by delta from currently displayed duration.
            if not (hours_set and minutes_set):
                curr_h, curr_m = self._parse_duration_text(duration_before)
                delta_h = target_hours - curr_h
                delta_m = target_minutes - curr_m
                if delta_h != 0:
                    self._rotate_duration_wheel(
                        hours_picker,
                        steps=max(1, abs(delta_h)),
                        logical_name="Duration hours picker",
                        direction="up" if delta_h > 0 else "down",
                    )
                if delta_m != 0:
                    self._rotate_duration_wheel(
                        minutes_picker,
                        steps=max(1, int(round(abs(delta_m) / 5.0)) or 1),
                        logical_name="Duration minutes picker",
                        direction="up" if delta_m > 0 else "down",
                    )

            picker_hours = self._read_duration_picker_digits(hours_picker)
            picker_minutes = self._read_duration_picker_digits(minutes_picker)
            picker_text = f"{picker_hours or '??'}:{picker_minutes or '??'}"
            if picker_hours != str(target_hours).zfill(2) or picker_minutes != str(target_minutes).zfill(2):
                raise AssertionError(
                    "Duration picker did not reach target before submit. "
                    f"Target={target_text!r}, picker={picker_text!r}. "
                    "Refusing to submit an invalid/default duration."
                )

            self._wait_clickable(
                AppiumBy.ID, self.DURATION_SUBMIT_BUTTON_ID, "Duration Submit button", timeout=8
            ).click()
            duration_after = (self._wait_visible(
                AppiumBy.ID, self.DURATION_FIELD_ID, "Duration field after submit"
            ).text or "").strip()
            if not self._is_valid_duration_text(duration_after):
                raise AssertionError(
                    f"Duration format invalid after submit: {duration_after!r} (expected HH:MM with MM 00-59)."
                )

            if self._is_duration_within_allowed_range(duration_after):
                if duration_after == duration_before:
                    self.LOGGER.warning(
                        "Duration remained unchanged after selection (before=%s, target=%s, after=%s).",
                        duration_before,
                        target_text,
                        duration_after,
                    )
                break

            self.LOGGER.warning(
                "Observed duration out of allowed range after attempt %s/%s "
                "(before=%s, target=%s, after=%s). Retrying correction.",
                attempt,
                max_apply_attempts,
                duration_before,
                target_text,
                duration_after,
            )

        if not self._is_duration_within_allowed_range(duration_after):
            raise AssertionError(
                "Duration did not land in allowed range (00:01 to 05:00). "
                f"Observed={duration_after!r}, last_target={target_text!r}."
            )
        self._last_selected_duration = duration_after or duration_before
        self.LOGGER.info(
            "Step Passed: Duration submitted from bottom sheet (target=%s:%s, observed=%s).",
            str(target_hours).zfill(2),
            str(target_minutes).zfill(2),
            self._last_selected_duration,
        )

    def _resolve_duration_target(self):
        """
        Resolve duration target in this priority:
        1) explicit custom value from CUBII_MANUAL_WORKOUT_DURATION (if set)
        2) random duration in allowed range (default behavior)

        Supported custom formats:
        - "1m", "2min", "2 minutes"
        - "1h", "2hr", "2 hours"
        - "1h1m", "2h 2m", "1 hour 1 minute"
        - "01:30" (HH:MM)
        """
        raw_custom = (os.getenv("CUBII_MANUAL_WORKOUT_DURATION", "") or "").strip()
        if not raw_custom or raw_custom.strip().lower() in {"random", "rand", "random24h", "random_24h"}:
            # The duration wheel moves in 5-minute steps, so random targets must align with it.
            total_minutes = random.randint(1, 60) * 5
            hours = total_minutes // 60
            minutes = total_minutes % 60
            self.LOGGER.info(
                "Using random duration%s -> %s:%s.",
                f" from CUBII_MANUAL_WORKOUT_DURATION={raw_custom!r}" if raw_custom else " (default)",
                str(hours).zfill(2),
                str(minutes).zfill(2),
            )
            return hours, minutes

        parsed = self._parse_custom_duration_value(raw_custom)
        if parsed is None:
            raise AssertionError(
                "Unsupported CUBII_MANUAL_WORKOUT_DURATION format. "
                f"Got {raw_custom!r}. Examples: 1m, 2m, 1h, 1h1m, 2h 2m, 01:30, random."
            )
        hours, minutes = parsed
        total_minutes = (hours * 60) + minutes
        if not (1 <= total_minutes <= 300):
            raise AssertionError(
                "CUBII_MANUAL_WORKOUT_DURATION out of allowed range. "
                f"Got {raw_custom!r} -> {str(hours).zfill(2)}:{str(minutes).zfill(2)}; "
                "allowed range is 00:01 to 05:00."
            )
        self.LOGGER.info(
            "Using custom duration from CUBII_MANUAL_WORKOUT_DURATION=%r -> %s:%s.",
            raw_custom,
            str(hours).zfill(2),
            str(minutes).zfill(2),
        )
        return hours, minutes

    def _parse_custom_duration_value(self, raw_value):
        text = (raw_value or "").strip().lower()
        if not text:
            return None

        # HH:MM
        hhmm = re.fullmatch(r"(\d{1,2}):(\d{1,2})", text)
        if hhmm:
            hours = int(hhmm.group(1))
            minutes = int(hhmm.group(2))
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return hours, minutes
            return None

        compact = re.sub(r"\s+", "", text)
        # Normalize common words to compact h/m tokens for easier parse.
        compact = compact.replace("hours", "h").replace("hour", "h")
        compact = compact.replace("hrs", "h").replace("hr", "h")
        compact = compact.replace("minutes", "m").replace("minute", "m")
        compact = compact.replace("mins", "m").replace("min", "m")

        # Combined form: XhYm / Xh / Ym
        combo = re.fullmatch(r"(?:(\d{1,2})h)?(?:(\d{1,2})m)?", compact)
        if combo:
            h_raw, m_raw = combo.groups()
            if h_raw is None and m_raw is None:
                return None
            hours = int(h_raw) if h_raw is not None else 0
            minutes = int(m_raw) if m_raw is not None else 0
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return hours, minutes
            return None

        return None

    def _try_set_duration_picker_value(self, resource_id, value):
        target = str(value).zfill(2)
        try:
            picker_input = WebDriverWait(self.driver, 2).until(
                ec.visibility_of_element_located((AppiumBy.ID, resource_id))
            )
            picker_input.click()
            try:
                picker_input.clear()
            except Exception:
                pass
            picker_input.send_keys(target)
            observed = (picker_input.text or "").strip()
            if not observed:
                observed = (picker_input.get_attribute("text") or "").strip()
            digits = "".join(ch for ch in observed if ch.isdigit())
            if digits == target:
                self.LOGGER.info(
                    "Set duration picker `%s` to `%s` (observed `%s`).",
                    resource_id,
                    target,
                    observed,
                )
                return True
            self.LOGGER.info(
                "Duration picker `%s` did not strictly match `%s` (observed `%s`).",
                resource_id,
                target,
                observed,
            )
            return False
        except Exception:
            self.LOGGER.debug("Duration picker not editable for `%s`.", resource_id)
            return False

    def _read_duration_picker_digits(self, picker_element):
        for attr in ("text", "value", "content-desc"):
            try:
                observed = (
                    picker_element.text
                    if attr == "text"
                    else picker_element.get_attribute(attr)
                )
            except Exception:
                observed = ""
            digits = "".join(ch for ch in (observed or "") if ch.isdigit())
            if digits:
                return digits[-2:].zfill(2)
        return ""

    def enter_valid_strides_value(self, strides_value=None):
        self.LOGGER.info("Step: Enter valid Strides value.")
        resolved_value = strides_value
        if resolved_value is None:
            raw_cfg = (os.getenv("CUBII_MANUAL_WORKOUT_STRIDES", "") or "").strip().lower()
            if raw_cfg and raw_cfg not in {"random", "rand"}:
                resolved_value = raw_cfg
            else:
                # Default randomized valid strides input for broader coverage.
                resolved_value = str(random.randint(50, 500))
        strides_input = self._wait_visible(
            AppiumBy.ID, self.STRIDES_INPUT_ID, "Strides input field"
        )
        self._send_keys(strides_input, str(resolved_value), label="Strides input field")
        observed = (strides_input.text or "").strip()
        assert observed, "Strides input did not retain entered value."
        self._last_entered_strides = observed
        self.LOGGER.info("Step Passed: Strides entered as `%s`.", observed)

    def enter_zero_strides_value(self):
        self.LOGGER.info("Step: Enter zero Strides value.")
        strides_input = self._wait_visible(
            AppiumBy.ID, self.STRIDES_INPUT_ID, "Strides input field"
        )
        self._send_keys(strides_input, "0", label="Strides input field")
        observed = (strides_input.text or "").strip()
        assert observed in {"0", "0.0"}, f"Expected zero strides value, got {observed!r}."
        self._last_entered_strides = observed
        self.LOGGER.info("Step Passed: Zero Strides entered as `%s`.", observed)

    def set_valid_resistance_level(self):
        self.LOGGER.info("Step: Set valid resistance level by moving slider right.")
        slider = self._wait_visible(
            AppiumBy.ID, self.RESISTANCE_SLIDER_ID, "Resistance slider"
        )
        rect = slider.rect
        start_x = int(rect["x"] + (rect["width"] * 0.25))
        end_x = int(rect["x"] + (rect["width"] * 0.75))
        y = int(rect["y"] + (rect["height"] * 0.5))
        self.driver.execute_script(
            "mobile: dragGesture",
            {"startX": start_x, "startY": y, "endX": end_x, "endY": y},
        )
        self.LOGGER.info("Step Passed: Resistance slider dragged to a valid level.")

    def tap_save_manual_workout(self):
        self.LOGGER.info("Step: Tap Save button on Add Manual Workout.")
        self._wait_clickable(
            AppiumBy.ID, self.SAVE_MANUAL_WORKOUT_BUTTON_ID, "Save Manual Workout button"
        ).click()
        self.LOGGER.info("Step Passed: Save button tapped.")
        time.sleep(3)

    def verify_save_button_disabled_on_add_workout(self):
        self.LOGGER.info("Step: Verify Save button is disabled on Add Workout when required fields are missing.")
        save_btn = self._wait_visible(
            AppiumBy.ID, self.SAVE_MANUAL_WORKOUT_BUTTON_ID, "Save Manual Workout button", timeout=8
        )
        enabled_attr = str(save_btn.get_attribute("enabled")).lower()
        clickable_attr = str(save_btn.get_attribute("clickable")).lower()
        actionable = enabled_attr == "true" and clickable_attr == "true"
        if not actionable:
            self.LOGGER.info(
                "Step Passed: Save button is disabled/non-clickable (enabled=%s, clickable=%s).",
                enabled_attr,
                clickable_attr,
            )
            return

        # Defensive check: if the control is actionable, ensure it does not proceed to confirmation.
        save_btn.click()
        time.sleep(1)
        if self._is_present(AppiumBy.ID, self.MANUAL_CONFIRMATION_POPUP_CARD_ID, timeout=1):
            raise AssertionError(
                "Save button is actionable and opened confirmation popup; expected disabled behavior."
            )
        raise AssertionError(
            f"Save button appears enabled/clickable (enabled={enabled_attr}, clickable={clickable_attr}); "
            "expected disabled behavior."
        )


    def verify_manual_workout_saved_without_errors(self):
        self.LOGGER.info("Step: Validate no manual workout validation errors are present.")
        error_fragments = ("required", "invalid", "please enter", "must be", "cannot")
        candidate_labels = (
            "textinput_error",
            "tvError",
            "error",
            "textinputError",
        )
        for rid in candidate_labels:
            for el in self.driver.find_elements(AppiumBy.XPATH, f'//*[@resource-id="{rid}"]'):
                txt = (el.text or "").strip().lower()
                if txt and any(fragment in txt for fragment in error_fragments):
                    raise AssertionError(f"Validation error displayed on manual workout form: {txt!r}")

        # Broad safety net for inline error messages if resource-id is unknown.
        for el in self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView"):
            txt = (el.text or "").strip().lower()
            if txt and any(fragment in txt for fragment in error_fragments):
                if "add workout" in txt or "calories" in txt or "miles" in txt:
                    continue
                if len(txt) < 70:
                    raise AssertionError(f"Potential validation error text detected: {txt!r}")
        self.LOGGER.info("Step Passed: No validation errors found after Save.")

    def verify_future_time_error_if_present(self):
        """
        Conditional validator used by random-past-time scenario.
        Returns True only when a known retryable time-validation message is visible.
        Raises assertion if an unexpected message appears in txtTimeErrorText.
        """
        retryable_messages = {
            self.TIME_VALIDATION_ERROR_EXPECTED_TEXT.strip().lower().rstrip("."),
            self.TIME_VALIDATION_ERROR_OVERLAP_TEXT.strip().lower().rstrip("."),
        }
        elements = []
        try:
            elements.extend(self.driver.find_elements(AppiumBy.ID, self.TIME_VALIDATION_ERROR_ID))
        except Exception:
            pass
        try:
            elements.extend(self.driver.find_elements(AppiumBy.XPATH, self.TIME_VALIDATION_ERROR_XPATH))
        except Exception:
            pass

        seen = set()
        for el in elements:
            if id(el) in seen:
                continue
            seen.add(id(el))
            if not el.is_displayed():
                continue
            observed = (el.text or "").strip()
            observed_norm = observed.lower().rstrip(".")
            if not observed_norm:
                continue
            if observed_norm in retryable_messages:
                self.LOGGER.info(
                    "Retryable time validation displayed as expected: `%s`.",
                    observed,
                )
                return True
            raise AssertionError(
                "Unexpected time validation error text. "
                f"Expected one of {sorted(retryable_messages)!r}, got={observed!r}"
            )
        self.LOGGER.info(
            "No retryable time validation error displayed after Save; proceeding with success validation path."
        )
        return False

    def verify_strides_validation_error(self, expected_message):
        """Assert strides field inline error matches after Save (e.g. duration cap exceeded)."""
        self.LOGGER.info("Step: Verify strides validation error text.")
        expected = (expected_message or "").strip()
        assert expected, "Expected strides error message must be non-empty."
        error_el = self._wait_visible(
            AppiumBy.ID,
            self.STRIDES_VALIDATION_ERROR_ID,
            "Strides validation error (txtStridesErrorText)",
            timeout=12,
        )
        observed = (error_el.text or "").strip()
        assert observed, "Strides validation error element visible but text is empty."
        assert observed == expected, (
            f"Unexpected strides validation text. Expected={expected!r}, observed={observed!r}"
        )
        self.LOGGER.info("Step Passed: Strides validation error matches `%s`.", observed)

    def verify_manual_workout_confirmation_popup_details(self):
        self.LOGGER.info("Step: Verify manual workout confirmation pop-up, title, and workout details.")
        popup_card = self._wait_visible(
            AppiumBy.ID,
            self.MANUAL_CONFIRMATION_POPUP_CARD_ID,
            "Manual workout confirmation pop-up card",
            timeout=12,
        )
        assert popup_card.is_displayed(), "Manual workout confirmation pop-up card is not visible."

        title_el = self._wait_visible(
            AppiumBy.ID,
            self.MANUAL_CONFIRMATION_TITLE_ID,
            "Manual workout confirmation pop-up title",
            timeout=8,
        )
        title_text = (title_el.text or "").strip()
        assert title_text, "Manual workout confirmation title is empty."
        expected_fragments = ("manual", "workout", "saved", "added", "entry", "success")
        assert any(fragment in title_text.lower() for fragment in expected_fragments), (
            f"Unexpected confirmation title text: {title_text!r}"
        )

        calories_layout = self._wait_visible(
            AppiumBy.ID, self.MANUAL_CONFIRMATION_CALORIES_LAYOUT_ID, "Calories layout"
        )
        distance_layout = self._wait_visible(
            AppiumBy.ID, self.MANUAL_CONFIRMATION_DISTANCE_LAYOUT_ID, "Distance layout"
        )
        duration_layout = self._wait_visible(
            AppiumBy.ID, self.MANUAL_CONFIRMATION_DURATION_LAYOUT_ID, "Duration layout"
        )

        calories_text = (calories_layout.text or "").strip()
        distance_text = (distance_layout.text or "").strip()
        duration_text = (duration_layout.text or "").strip()

        # Validate by presence/visibility of the summary layouts (container ids), since
        # layout container .text may be empty depending on Android view hierarchy.
        assert calories_layout.is_displayed(), "Calories layout is not visible in confirmation pop-up."
        assert distance_layout.is_displayed(), "Distance layout is not visible in confirmation pop-up."
        assert duration_layout.is_displayed(), "Duration layout is not visible in confirmation pop-up."

        strides_value_text = (self._wait_visible(
            AppiumBy.ID,
            self.MANUAL_CONFIRMATION_STRIDES_VALUE_ID,
            "Confirmation strides value",
            timeout=8,
        ).text or "").strip()
        calories_value_text = (self._wait_visible(
            AppiumBy.ID,
            self.MANUAL_CONFIRMATION_CALORIES_VALUE_ID,
            "Confirmation calories value",
            timeout=8,
        ).text or "").strip()
        distance_value_text = (self._wait_visible(
            AppiumBy.ID,
            self.MANUAL_CONFIRMATION_DISTANCE_VALUE_ID,
            "Confirmation miles value",
            timeout=8,
        ).text or "").strip()
        duration_value_text = (self._wait_visible(
            AppiumBy.ID,
            self.MANUAL_CONFIRMATION_DURATION_VALUE_ID,
            "Confirmation duration value",
            timeout=8,
        ).text or "").strip()

        strides_num = self._extract_first_number(strides_value_text)
        calories_num = self._extract_first_number(calories_value_text)
        distance_num = self._extract_first_number(distance_value_text)
        assert strides_num is not None and strides_num > 0, (
            f"Invalid strides value in confirmation pop-up: {strides_value_text!r}"
        )
        assert calories_num is not None and calories_num >= 0, (
            f"Invalid calories value in confirmation pop-up: {calories_value_text!r}"
        )
        assert distance_num is not None and distance_num >= 0, (
            f"Invalid miles value in confirmation pop-up: {distance_value_text!r}"
        )
        assert duration_value_text, "Duration value is empty in confirmation pop-up."
        got_it_button = self._wait_clickable(
            AppiumBy.ID,
            self.MANUAL_CONFIRMATION_GOT_IT_BUTTON_ID,
            "Manual workout confirmation GOT IT button",
            timeout=8,
        )
        got_it_button.click()
        self.LOGGER.info(
            "Step Passed: Confirmation pop-up validated and GOT IT clicked (title, strides, calories, distance, duration)."
        )

    def _is_manual_workout_editor_foreground(self):
        """True when Add/Edit workout full-screen is visible (blocks bottom navigation)."""
        try:
            els = self.driver.find_elements(AppiumBy.ID, self.TXT_ADD_EDIT_WORKOUT_TITLE_ID)
            return any(e.is_displayed() for e in els)
        except Exception:
            return False

    def _leave_manual_workout_editor_if_blocking_navigation(self):
        """Press Android back until the manual workout editor is dismissed so bottom tabs work."""
        for attempt in range(1, 5):
            if not self._is_manual_workout_editor_foreground():
                return
            self.LOGGER.info(
                "Manual workout editor is foreground; pressing back (%s/4) before Progress tab.",
                attempt,
            )
            try:
                self.driver.back()
            except Exception as exc:
                self.LOGGER.debug("Back press failed: %s", exc)
            time.sleep(0.7)
        if self._is_manual_workout_editor_foreground():
            self.LOGGER.warning(
                "Manual workout editor may still be visible after back presses; attempting Progress tab anyway."
            )

    def _tap_activity_log_row(self, row):
        """Tap row container; fall back to center-point clickGesture if WebDriver click fails."""
        try:
            row.click()
        except Exception as exc:
            self.LOGGER.debug("Row WebDriver click failed; using coordinate tap (%s).", exc)
            rect = row.rect
            cx = int(rect["x"] + rect["width"] / 2)
            cy = int(rect["y"] + rect["height"] / 2)
            self.driver.execute_script("mobile: clickGesture", {"x": cx, "y": cy})

    def open_first_manual_workout_for_edit(self):
        self.LOGGER.info("Step: Open first manual workout card for editing.")
        rows = self._wait_activity_rows_on_in_progress(timeout=12)
        if not rows:
            try:
                size = self.driver.get_window_size()
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "left": int(size["width"] * 0.1),
                        "top": int(size["height"] * 0.35),
                        "width": int(size["width"] * 0.8),
                        "height": int(size["height"] * 0.45),
                        "direction": "down",
                        "percent": 0.35,
                    },
                )
                time.sleep(0.5)
            except Exception:
                pass
            rows = self._wait_activity_rows_on_in_progress(timeout=8)
        assert rows, "No activity log rows found; cannot edit manual workout."

        for idx, row in enumerate(rows, start=1):
            try:
                manual_badges = row.find_elements(AppiumBy.ID, self.ACTIVITY_LOG_MANUAL_INDICATOR_ID)
                if not manual_badges or not any(b.is_displayed() for b in manual_badges):
                    continue
                self._tap_activity_log_row(row)
                time.sleep(0.6)
                WebDriverWait(self.driver, 12).until(
                    lambda d: self._find_visible_edit_workout_title()
                )
                self.LOGGER.info(
                    "Step Passed: Opened manual workout row %s for editing.", idx
                )
                return
            except TimeoutException:
                self.LOGGER.warning("Edit title did not appear after tapping row_index=%s.", idx)
                if self._is_manual_workout_editor_foreground():
                    try:
                        self.driver.back()
                    except Exception:
                        pass
                    time.sleep(0.5)
            except Exception as exc:
                self.LOGGER.debug("Skipping row %s: %s", idx, exc)
                continue

        raise AssertionError(
            "No manual workout row opened Edit Workout (manual tag + tap → Edit title)."
        )

    def _find_visible_edit_workout_title(self):
        try:
            el = self.driver.find_element(AppiumBy.ID, self.TXT_ADD_EDIT_WORKOUT_TITLE_ID)
        except Exception:
            return False
        if not el.is_displayed():
            return False
        if (el.text or "").strip() != self.EDIT_MANUAL_WORKOUT_TITLE_EXPECTED:
            return False
        return el

    def verify_edit_workout_screen_displayed(self):
        title_el = self._wait_visible(
            AppiumBy.ID,
            self.TXT_ADD_EDIT_WORKOUT_TITLE_ID,
            "Edit Workout title",
            timeout=Settings.EXPLICIT_WAIT,
        )
        observed = (title_el.text or "").strip()
        assert observed == self.EDIT_MANUAL_WORKOUT_TITLE_EXPECTED, (
            f"Expected title {self.EDIT_MANUAL_WORKOUT_TITLE_EXPECTED!r}, got {observed!r}."
        )
        self.LOGGER.info("Step Passed: Edit Workout screen title matched.")

    def verify_edited_manual_workout_details_in_in_progress(self):
        self.LOGGER.info(
            "Step: Verify edited manual workout visible with expected time and strides."
        )
        expected_time = str(getattr(self, "_last_selected_start_time", "") or "").strip()
        expected_strides = str(getattr(self, "_last_entered_strides", "") or "").strip()
        assert expected_time, "_last_selected_start_time must be set after editing Start Time."
        assert expected_strides, "_last_entered_strides must be set after editing Strides."

        rows = self._wait_activity_rows_on_in_progress(timeout=12)
        if not rows:
            try:
                size = self.driver.get_window_size()
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "left": int(size["width"] * 0.1),
                        "top": int(size["height"] * 0.35),
                        "width": int(size["width"] * 0.8),
                        "height": int(size["height"] * 0.45),
                        "direction": "down",
                        "percent": 0.35,
                    },
                )
                time.sleep(0.5)
            except Exception:
                pass
            rows = self._wait_activity_rows_on_in_progress(timeout=6)
        assert rows, "No activity log rows on In Progress after edit."

        def _norm(s):
            return " ".join((s or "").split()).lower().replace("\u202f", " ")

        exp_t = _norm(expected_time)
        for row in rows:
            try:
                manual_badges = row.find_elements(AppiumBy.ID, self.ACTIVITY_LOG_MANUAL_INDICATOR_ID)
                if not manual_badges or not any(b.is_displayed() for b in manual_badges):
                    continue
                time_txt = ""
                for node in row.find_elements(AppiumBy.ID, self.ACTIVITY_LOG_TIME_ID):
                    if (node.text or "").strip():
                        time_txt = (node.text or "").strip()
                        break
                if not time_txt or _norm(time_txt) != exp_t:
                    continue
                metric_ids = (
                    self.ACTIVITY_LOG_METRIC_VALUE_1_ID,
                    self.ACTIVITY_LOG_METRIC_VALUE_2_ID,
                    self.ACTIVITY_LOG_METRIC_VALUE_3_ID,
                    self.ACTIVITY_LOG_METRIC_VALUE_4_ID,
                )
                stride_found = False
                for metric_id in metric_ids:
                    for node in row.find_elements(AppiumBy.ID, metric_id):
                        txt = (node.text or "").strip()
                        if expected_strides in txt:
                            stride_found = True
                            break
                    if stride_found:
                        break
                if stride_found:
                    self.LOGGER.info(
                        "Step Passed: Edited manual row found (time=%r, strides=%r).",
                        time_txt,
                        expected_strides,
                    )
                    return
            except Exception:
                continue

        raise AssertionError(
            f"Could not find manual row matching time {expected_time!r} and strides {expected_strides!r}."
        )

    def open_in_progress_tab(self):
        self.LOGGER.info("Step: Open In Progress tab.")
        self._leave_manual_workout_editor_if_blocking_navigation()
        self._dismiss_in_progress_ftue_overlays_if_present()
        for by, locator in self.IN_PROGRESS_TAB_CANDIDATE_LOCATORS:
            try:
                for el in self.driver.find_elements(by, locator):
                    if not el.is_displayed():
                        continue
                    try:
                        if not el.is_enabled():
                            continue
                    except Exception:
                        pass
                    el.click()
                    time.sleep(1)
                    self.LOGGER.info(
                        "Step Passed: Opened In Progress tab using locator=(%s, %s).",
                        by,
                        locator,
                    )
                    return
            except Exception:
                continue
        raise AssertionError(
            "Could not open In Progress tab. Please provide a stable In Progress tab locator."
        )

    def tap_add_manual_workout_on_progress_tab(self):
        """Tap Add Manual Workout on Progress/In Progress (`btnAddManualWorkout`)."""
        self.LOGGER.info("Step: Tap Add Manual Workout button on Progress/In Progress.")
        self._dismiss_in_progress_ftue_overlays_if_present()
        per = int(os.getenv("CUBII_ADD_MANUAL_WORKOUT_BTN_WAIT_SEC", "8"))
        for by, locator, title in (
            (AppiumBy.ID, self.BTN_ADD_MANUAL_WORKOUT_ID, "Add Manual Workout (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.BTN_ADD_MANUAL_WORKOUT_UIAUTOMATOR,
                "Add Manual Workout (UiAutomator)",
            ),
            (AppiumBy.XPATH, self.BTN_ADD_MANUAL_WORKOUT_XPATH, "Add Manual Workout (XPath)"),
        ):
            if self._click_if_present(by, locator, title, timeout=per):
                time.sleep(0.8)
                self.LOGGER.info("Step Passed: Add Manual Workout tapped via %s.", title)
                return
        raise AssertionError(
            "Add Manual Workout button not found (`com.cubii:id/btnAddManualWorkout`)."
        )

    def refresh_page_pull_down(self):
        """Pull-to-refresh on the current native screen (e.g. In Progress list)."""
        self.LOGGER.info("Step: Pull-to-refresh (reload list content).")
        size = self.driver.get_window_size()
        w = int(size["width"])
        h = int(size["height"])
        pct = float(os.getenv("CUBII_PULL_REFRESH_PERCENT", "0.85"))
        self.driver.execute_script(
            "mobile: swipeGesture",
            {
                "left": int(w * 0.2),
                "top": int(h * 0.12),
                "width": int(w * 0.6),
                "height": int(h * 0.4),
                "direction": "down",
                "percent": pct,
            },
        )
        time.sleep(float(os.getenv("CUBII_AFTER_PULL_REFRESH_PAUSE_SEC", "1.5")))
        self.LOGGER.info("Step Passed: Pull-to-refresh gesture completed.")

    def open_home_tab(self):
        self.LOGGER.info("Step: Open Home tab.")
        self._leave_manual_workout_editor_if_blocking_navigation()
        self._dismiss_in_progress_ftue_overlays_if_present()
        for by, locator in self.HOME_TAB_CANDIDATE_LOCATORS:
            try:
                for el in self.driver.find_elements(by, locator):
                    if not el.is_displayed():
                        continue
                    try:
                        if not el.is_enabled():
                            continue
                    except Exception:
                        pass
                    el.click()
                    time.sleep(1)
                    self.LOGGER.info(
                        "Step Passed: Opened Home tab using locator=(%s, %s).",
                        by,
                        locator,
                    )
                    return
            except Exception:
                continue
        raise AssertionError(
            "Could not open Home tab. Please provide a stable Home tab locator."
        )

    def _dismiss_in_progress_ftue_overlays_if_present(self):
        """
        Best-effort dismissal of onboarding overlays that can block bottom-tab clicks.
        Multi-pass to handle stacked dialogs.
        """
        for attempt in range(1, 4):
            clicked_any = False
            # Reuse known app-level FTUE/overlay buttons first.
            clicked_any = self._click_if_present(
                AppiumBy.ID, self.GOT_IT_CHIIR_ID, "GOT IT (Chiir motivated)", timeout=1
            ) or clicked_any
            clicked_any = self._click_if_present(
                AppiumBy.ID, self.GOT_IT_CHANGE_MODES_ID, "GOT IT (Change modes)", timeout=1
            ) or clicked_any
            clicked_any = self._click_if_present(
                AppiumBy.ID,
                self.MANUAL_CONFIRMATION_GOT_IT_BUTTON_ID,
                "GOT IT (Manual confirmation)",
                timeout=1,
            ) or clicked_any
            # Generic text fallback for unexpected FTUE popups.
            clicked_any = self._click_if_present(
                AppiumBy.XPATH,
                '//*[contains(translate(@text, "goti", "GOTI"), "GOT IT")]',
                "GOT IT (generic text)",
                timeout=1,
            ) or clicked_any
            if not clicked_any:
                if attempt > 1:
                    self.LOGGER.info(
                        "No blocking FTUE overlays detected before opening In Progress (pass=%s).",
                        attempt,
                    )
                break
            self.LOGGER.info(
                "Dismissed one or more FTUE overlays before opening In Progress (pass=%s).",
                attempt,
            )
            time.sleep(0.4)

    def verify_manual_workout_visible_in_in_progress(self):
        self.LOGGER.info("Step: Verify manual workout is visible in In Progress activity log.")
        rows = self._wait_activity_rows_on_in_progress(timeout=12)
        if not rows:
            # One light list nudge and re-check helps when rows render lazily below the fold.
            try:
                size = self.driver.get_window_size()
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "left": int(size["width"] * 0.1),
                        "top": int(size["height"] * 0.35),
                        "width": int(size["width"] * 0.8),
                        "height": int(size["height"] * 0.45),
                        "direction": "down",
                        "percent": 0.35,
                    },
                )
                time.sleep(0.5)
            except Exception:
                pass
            rows = self._wait_activity_rows_on_in_progress(timeout=4)
        assert rows, "No activity log rows found on In Progress screen."

        # Dynamic row strategy: iterate rows and pass on first manual-tagged row with core values.
        for idx, row in enumerate(rows, start=1):
            try:
                manual_badges = row.find_elements(AppiumBy.ID, self.ACTIVITY_LOG_MANUAL_INDICATOR_ID)
                if not manual_badges or not any(b.is_displayed() for b in manual_badges):
                    continue

                time_nodes = row.find_elements(AppiumBy.ID, self.ACTIVITY_LOG_TIME_ID)
                has_time = any((n.text or "").strip() for n in time_nodes)
                if not has_time:
                    continue

                metric_ids = (
                    self.ACTIVITY_LOG_METRIC_VALUE_1_ID,
                    self.ACTIVITY_LOG_METRIC_VALUE_2_ID,
                    self.ACTIVITY_LOG_METRIC_VALUE_3_ID,
                    self.ACTIVITY_LOG_METRIC_VALUE_4_ID,
                )
                metric_texts = []
                for metric_id in metric_ids:
                    for node in row.find_elements(AppiumBy.ID, metric_id):
                        txt = (node.text or "").strip()
                        if txt:
                            metric_texts.append(txt)
                if metric_texts:
                    self.LOGGER.info(
                        "Step Passed: Manual workout row found in In Progress (row_index=%s, metrics=%s).",
                        idx,
                        metric_texts,
                    )
                    return
            except Exception:
                continue

        raise AssertionError(
            "Manual workout row not found in In Progress activity log "
            "(manual tag + time + metrics)."
        )

    def _wait_activity_rows_on_in_progress(self, timeout=10):
        deadline = time.monotonic() + max(1, int(timeout))
        while time.monotonic() < deadline:
            rows = self.driver.find_elements(AppiumBy.ID, self.ACTIVITY_LOG_ROW_ID)
            if rows:
                return rows
            # Fallback signal: if manual indicators are already present, row roots may be delayed.
            indicators = self.driver.find_elements(AppiumBy.ID, self.ACTIVITY_LOG_MANUAL_INDICATOR_ID)
            if indicators:
                self.LOGGER.info(
                    "Manual indicators detected before row roots resolved; retrying row lookup."
                )
            time.sleep(0.4)
        return []

    def _add_workout_entry_locators(self):  # ADD WORKOUT 1 & 2 only (imgNonBleBanner, imageView35).
        return (
            (AppiumBy.ID, self.IMG_NON_BLE_BANNER_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.IMG_NON_BLE_BANNER_UIAUTOMATOR),
            (AppiumBy.XPATH, self.IMG_NON_BLE_BANNER_XPATH),
            (AppiumBy.ID, self.ADD_WORKOUT_IMAGE_VIEW_35_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.ADD_WORKOUT_IMAGE_VIEW_35_UIAUTOMATOR),
            (AppiumBy.XPATH, self.ADD_WORKOUT_IMAGE_VIEW_35_XPATH),
        )

    def _click_first_visible_add_workout_entry(self):  # True if a tap was delivered on any Add Workout target
        for by, val in self._add_workout_entry_locators():
            try:
                for candidate in self.driver.find_elements(by, val):
                    if not candidate.is_displayed():
                        continue
                    candidate.click()
                    self.LOGGER.info(
                        "Clicked Add Workout entry using strategy=%s resource=%s.", by, val
                    )
                    return True
            except Exception as exc:
                self.LOGGER.debug("Add Workout locator attempt skipped: %s %s (%s)", by, val, exc)
                continue
        return False

    def _probe_and_click_visible_add_workout_entry(self):  # Light Home scroll rounds before declaring “not visible”
        rounds = int(os.getenv("CUBII_HOME_ADD_WORKOUT_PROBE_ROUNDS", "4"))
        for round_ix in range(max(1, rounds)):
            if self._click_first_visible_add_workout_entry():
                return True
            self.LOGGER.debug("Add Workout probe round %s: no visible entry; scrolling Home lightly.", round_ix + 1)
            self._scroll_home_content_down_small()
            time.sleep(0.2)
        return False

    def _assert_label_has_display_box(self, element, logical_name):  # Weak “readable / aligned” signal without visual compare
        size = element.size
        ok = bool(size.get("height", 0) > 8 and size.get("width", 0) > 8)
        assert ok, f"{logical_name} view has negligible on-screen footprint (height/width)."  # Guards zero-height overlays
        self.LOGGER.debug(
            "`%s` bounding box roughly %sx%s px.", logical_name, size.get("width"), size.get("height")
        )

    def _scroll_home_content_down_small(self):  # Nudge Home scroll; device card actions can sit below the fold
        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.1),
                "top": int(size["height"] * 0.25),
                "width": int(size["width"] * 0.8),
                "height": int(size["height"] * 0.5),
                "direction": "down",
                "percent": float(os.getenv("CUBII_HOME_VALIDATION_SCROLL_PERCENT", "0.35")),
            },
        )

    def _wait_visible_any_add_workout_on_home(self, timeout=None):  # imgNonBleBanner / imageView35 on Home
        wait_sec = timeout or Settings.EXPLICIT_WAIT
        deadline = time.monotonic() + wait_sec
        locators_flat = self._add_workout_entry_locators()
        scroll_enabled = os.getenv(
            "CUBII_HOME_ADD_WORKOUT_ENABLE_SCROLL", "0"
        ).strip().lower() in ("1", "true", "yes")
        if scroll_enabled:
            initial = int(os.getenv("CUBII_HOME_ADD_WORKOUT_INITIAL_SCROLLS", "1"))
            for _ in range(max(0, initial)):
                if time.monotonic() >= deadline:
                    break
                self._scroll_home_content_down_small()

        scroll_round = 0
        self.LOGGER.info(
            "Waiting visible: Add Workout (`imgNonBleBanner`, `imageView35`%s).",
            "; light Home scroll enabled" if scroll_enabled else "; no Home scroll",
        )
        while time.monotonic() < deadline:
            for by, val in locators_flat:
                try:
                    el = WebDriverWait(self.driver, 1).until(
                        ec.visibility_of_element_located((by, val))
                    )
                    self.LOGGER.info("Element Found: Add Workout entry (strategy=%s).", by)
                    return el
                except TimeoutException:
                    continue
            scroll_round += 1
            if scroll_enabled:
                self._scroll_home_content_down_small()
                if scroll_round == 1 or scroll_round % 4 == 0:
                    self.LOGGER.info(
                        "Add Workout entry not visible yet; light Home scroll (round %s).",
                        scroll_round,
                    )
            time.sleep(0.15)
        raise TimeoutException(
            "Add Workout not found: none of `imgNonBleBanner`, `imageView35` visible on Home."
        )

    def _wait_visible_change_device_on_home(self, timeout=None):  # Match HomePage-style discovery; ID-only often misses
        wait_sec = timeout or Settings.EXPLICIT_WAIT
        deadline = time.monotonic() + wait_sec
        locators = (
            (AppiumBy.ID, self.CHANGE_DEVICE_BTN_ID),
            (AppiumBy.XPATH, self.CHANGE_DEVICE_XPATH_ANY),
            (AppiumBy.XPATH, self.CHANGE_DEVICE_CARD_SCOPED_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.CHANGE_DEVICE_UIAUTOMATOR),
        )
        max_scrolls = int(os.getenv("CUBII_HOME_CHANGE_DEVICE_SCROLL_ATTEMPTS", "5"))
        scrolls_done = 0
        self.LOGGER.info("Waiting visible: Change Device (multi-locator + optional Home scroll).")
        while time.monotonic() < deadline:
            for by, val in locators:
                try:
                    el = WebDriverWait(self.driver, 1).until(
                        ec.visibility_of_element_located((by, val))
                    )
                    self.LOGGER.info("Element Found: Change Device (strategy=%s).", by)
                    return el
                except TimeoutException:
                    continue
            if scrolls_done < max_scrolls:
                self._scroll_home_content_down_small()
                scrolls_done += 1
            else:
                time.sleep(0.3)
        raise TimeoutException(
            "Change Device (`btnChangeDevices`) not found or not visible on Home after scroll retries."
        )

    def is_home_screen_ready(self):  # True if a recognizable Home surface is present (varies by connection state)
        probes = (
            (AppiumBy.ID, self.NO_WORKOUT_FOR_A_DAY_CARD_ID, "LET'S GO card (noWorkoutForADayCard)"),
            (AppiumBy.ID, self.BTN_CONNECT_NEW_DEVICE_ID, "CONNECT NEW DEVICE (btnConnectDisconnect)"),
            (AppiumBy.ID, self.IMG_NON_BLE_BANNER_ID, "Add Workout 1 (imgNonBleBanner)"),
            (AppiumBy.ID, self.ADD_WORKOUT_IMAGE_VIEW_35_ID, "Add Workout 2 (imageView35)"),
            (AppiumBy.ID, self.DEVICE_CARD_ID, "Device card (lytConnectDisconnect)"),
        )
        for by, rid, label in probes:
            if self._is_present(by, rid, timeout=4):
                self.LOGGER.info("Home screen ready: found %s (`%s`).", label, rid)
                return True
        return False

    # --- Internal steps ---  # Marker: private flow methods below

    def _tap_home_entry_cta(self):  # Pairing only: LET'S GO card, then CONNECT NEW DEVICE (no Add Workout banners).
        self.LOGGER.info(
            "Step: Tap pairing CTA — noWorkoutForADayCard (LET'S GO), then btnConnectDisconnect (CONNECT NEW DEVICE)."
        )
        per_strategy = int(os.getenv("CUBII_HOME_PAIRING_CTA_WAIT_SEC", "2"))
        for by, val in (
            (AppiumBy.ID, self.NO_WORKOUT_FOR_A_DAY_CARD_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.NO_WORKOUT_FOR_A_DAY_CARD_UIAUTOMATOR),
            (AppiumBy.XPATH, self.NO_WORKOUT_FOR_A_DAY_CARD_XPATH),
        ):
            if self._click_if_present(by, val, "LET'S GO (noWorkoutForADayCard)", timeout=per_strategy):
                self.LOGGER.info("Step Passed: LET'S GO / empty-day card tapped via %s.", val)
                return
        for by, val in (
            (AppiumBy.ID, self.BTN_CONNECT_NEW_DEVICE_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.BTN_CONNECT_NEW_DEVICE_UIAUTOMATOR),
            (AppiumBy.XPATH, self.BTN_CONNECT_NEW_DEVICE_XPATH),
        ):
            if self._click_if_present(by, val, "CONNECT NEW DEVICE (btnConnectDisconnect)", timeout=per_strategy):
                self.LOGGER.info("Step Passed: CONNECT NEW DEVICE tapped via %s.", val)
                return
        raise AssertionError(
            "No pairing entry on Home: try noWorkoutForADayCard (LET'S GO) or btnConnectDisconnect "
            "(CONNECT NEW DEVICE). If imgNonBleBanner / imageView35 are visible, device is already connected — "
            "pairing is skipped."
        )

    def _return_to_home_surface_before_connect_flow(self, max_back_presses=3):
        if self.is_home_screen_ready():
            self.LOGGER.info("Home surface already visible before connect-flow recovery.")
            return
        for attempt in range(max(1, int(max_back_presses))):
            try:
                self.driver.back()
            except Exception as exc:
                self.LOGGER.debug("Back navigation attempt %s failed: %s", attempt + 1, exc)
            time.sleep(0.6)
            if self.is_home_screen_ready():
                self.LOGGER.info(
                    "Recovered to Home surface before connect-flow (back attempts=%s).",
                    attempt + 1,
                )
                return
        self.LOGGER.warning(
            "Could not confidently confirm Home surface before connect-flow after %s back attempts; proceeding.",
            max_back_presses,
        )

    def _select_non_ble_device_type(self):  # Verify both types visible; select Non-BLE
        self.LOGGER.info(  # Explain validation intent
            "Step: Verify Bluetooth and Non-Bluetooth options; select Non-Bluetooth."  # Log message string
        )
        self._wait_visible(AppiumBy.XPATH, self.BLUETOOTH_DEVICE_PARENT_XPATH, "Bluetooth Device")  # Assert BT row exists
        self.LOGGER.info("Element Found: Bluetooth Device option.")  # Confirmation log
        self._wait_visible(AppiumBy.XPATH, self.NON_BLE_DEVICE_PARENT_XPATH, "Non-Bluetooth Device")  # Assert Non-BLE row
        self.LOGGER.info("Element Found: Non-Bluetooth Device option.")  # Confirmation log

        tap_target = AppiumBy.XPATH, self.NON_BLE_DEVICE_TAP_XPATH  # Tuple locator for readable click target
        elem = self._wait_visible(*tap_target, "Non-Bluetooth tap target")  # Wait until tappable ViewGroup visible
        elem.click()  # Activate Non-Bluetooth selection
        self.LOGGER.info("Step Passed: Non-Bluetooth Device selected.")  # Log selection done

    def _click_model_selection_next(self):  # Tap NEXT button on current selection screen
        next_btn = self._wait_clickable(AppiumBy.ID, self.BTN_NEXT_ID, "NEXT")  # Wait until button clickable
        next_btn.click()  # Submit current screen
        self.LOGGER.info("Step Passed: NEXT tapped.")  # Log advancement

    def _label_match_candidates(self, canonical_display_name):
        aliases = self.MODEL_LABEL_VISIBILITY_ALIASES.get(canonical_display_name, ())
        return (canonical_display_name,) + tuple(aliases)

    def _try_click_clickable(self, by, value, label, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable((by, value))
            )
            element.click()
            self.LOGGER.info("Step Passed: Clicked `%s`.", label)
            return True
        except TimeoutException:
            self.LOGGER.info("Not clickable within %ss: `%s`.", timeout, label)
            return False

    def _is_model_row_displayed(self, xpath, uia_sel):
        try:
            for el in self.driver.find_elements(AppiumBy.XPATH, xpath):
                try:
                    if el.is_displayed():
                        return True
                except Exception:
                    continue
        except Exception:
            pass
        try:
            el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, uia_sel)
            return el.is_displayed()
        except Exception:
            return False

    def _tap_model_row(self, display_name, xpath, uia_sel):
        if self._try_click_clickable(
            AppiumBy.XPATH, xpath, f"{display_name} (XPath)", timeout=5
        ):
            return True
        if self._try_click_clickable(
            AppiumBy.ANDROID_UIAUTOMATOR, uia_sel, f"{display_name} (UiAutomator)", timeout=5
        ):
            return True
        for cand in self._label_match_candidates(display_name):
            safe = cand.replace('"', '\\"')
            text_uia = f'new UiSelector().textContains("{safe}").instance(0)'
            if self._try_click_clickable(
                AppiumBy.ANDROID_UIAUTOMATOR,
                text_uia,
                f"{display_name} (textContains→{cand})",
                timeout=4,
            ):
                return True
        return False

    def _tap_visible_model_card_on_picker(self):  # Use per-model locators; tap first row that is on-screen (no scroll)
        self.LOGGER.info("Step: Select visible Cubii model via row locators (no list scroll).")
        deadline = time.monotonic() + float(os.getenv("CUBII_MODEL_PICKER_WAIT_SEC", "12"))
        while time.monotonic() < deadline:
            for display_name, xpath, uia_sel in self.CUBII_MODEL_LOCATORS:
                if not self._is_model_row_displayed(xpath, uia_sel):
                    continue
                try:
                    for el in self.driver.find_elements(AppiumBy.XPATH, xpath):
                        if el.is_displayed():
                            el.click()
                            self.LOGGER.info("Step Passed: Selected visible model `%s` (XPath click).", display_name)
                            return
                except Exception:
                    pass
                if self._tap_model_row(display_name, xpath, uia_sel):
                    self.LOGGER.info("Step Passed: Selected visible model `%s`.", display_name)
                    return
            time.sleep(0.35)
        raise AssertionError(
            "No Cubii model row matched as visible on the model selection screen (check locators vs UI)."
        )

    def _fill_cubii_details_and_save(self, cubii_name):  # Detail screen assertions and SAVE
        self.LOGGER.info("Step: Cubii details screen — name, model text, SAVE.")  # Log phase

        self._wait_visible(  # Confirm details layout loaded
            AppiumBy.ID, self.DETAILS_SCREEN_ID, "Cubii details screen container"  # Wait for root id
        )
        self.LOGGER.info("Element Found: Cubii details screen.")  # Screen detected

        name_input = self._wait_visible(  # Locate name field
            AppiumBy.ID, self.CUBII_NAME_INPUT_ID, "Cubii Name Input"  # EditText id and label
        )
        self._send_keys(name_input, cubii_name, label="Cubii Name Input")  # Clear and type Cubii name

        model_el = self._wait_visible(  # Read model summary text
            AppiumBy.ID, self.CUBII_MODEL_NAME_ID, "Cubii Model Name"  # TextView resource id
        )
        model_text = (model_el.text or "").strip()  # Normalize displayed model string
        assert model_text, "Cubii model name is not displayed."  # Requirement: non-empty model label
        self.LOGGER.info("Step Passed: Model name displayed: `%s`.", model_text)  # Evidence in logs

        save_btn = self._wait_clickable(AppiumBy.ID, self.BTN_SAVE_ID, "SAVE")  # Wait for SAVE clickable
        save_btn.click()  # Persist Non-BLE device configuration
        self.LOGGER.info("Step Passed: SAVE tapped.")  # Confirm save interaction

    def _handle_optional_popups(self):  # Best-effort dismiss of dialogs that may not appear
        self.LOGGER.info("Step: Optional popups — Do Not Show Again, GOT IT.")  # Describe optional handling
        try:  # Swallow unexpected errors so flow can continue
            self._click_if_present(  # Tap checkbox if shown
                AppiumBy.ID, self.DO_NOT_SHOW_AGAIN_ID, "Do Not Show Again", timeout=2  # Short optional wait
            )
            self._click_if_present(  # First GOT IT variant
                AppiumBy.ID, self.GOT_IT_CHIIR_ID, "GOT IT (Chiir motivated)", timeout=3  # Medium optional wait
            )
            self._click_if_present(  # FTUE GOT IT after first connection modes tip
                AppiumBy.ID,  # Locate by Android id
                self.GOT_IT_CHANGE_MODES_ID,  # Button resource id string
                "GOT IT (Change modes)",  # Log-friendly name
                timeout=4,  # Slightly longer for delayed dialog
            )
            self.LOGGER.info("Step Passed: Optional popups handled.")  # All optional taps attempted
        except Exception as exc:  # Prevent optional UI from crashing main flow
            self.LOGGER.info("Optional popup handling ended safely: %s", exc)  # Record reason without failing

    # --- Reusable helpers (explicit waits) ---  # Shared wait/send utilities

    def _wait_visible(self, by, value, label, timeout=None):  # Block until element is visible
        wait_sec = timeout or Settings.EXPLICIT_WAIT  # Use override or framework default seconds
        self.LOGGER.info(
            "Waiting visible: %s | locator=(%s, %s) | timeout=%ss",
            label,
            by,
            value,
            wait_sec,
        )  # Announce wait target in logs
        try:
            el = WebDriverWait(self.driver, wait_sec).until(  # Create scoped wait driver
                ec.visibility_of_element_located((by, value))  # Predicate: element Location and visibility
            )
            self.LOGGER.info("Element Found: %s", label)  # Confirm element matched
            return el  # Return WebElement instance to caller
        except Exception as exc:
            self.LOGGER.error(
                "Locator wait failed (visible): %s | locator=(%s, %s) | timeout=%ss | error=%s",
                label,
                by,
                value,
                wait_sec,
                exc,
            )
            raise

    def _wait_clickable(self, by, value, label, timeout=None):  # Block until element clickable
        wait_sec = timeout or Settings.EXPLICIT_WAIT  # Resolve timeout seconds for this lookup
        self.LOGGER.info(
            "Waiting clickable: %s | locator=(%s, %s) | timeout=%ss",
            label,
            by,
            value,
            wait_sec,
        )  # Log which control we wait on
        try:
            el = WebDriverWait(self.driver, wait_sec).until(  # Poll until clickable or timeout
                ec.element_to_be_clickable((by, value))  # Predicate: displayed and enabled
            )
            self.LOGGER.info("Element Found: %s", label)  # Confirmation for debugging
            return el  # Pass element back for interactions
        except Exception as exc:
            self.LOGGER.error(
                "Locator wait failed (clickable): %s | locator=(%s, %s) | timeout=%ss | error=%s",
                label,
                by,
                value,
                wait_sec,
                exc,
            )
            raise

    def _click_if_present(self, by, value, label, timeout=3):  # Tap only if appears within timeout
        try:  # Treat missing element as non-failure
            el = WebDriverWait(self.driver, timeout).until(  # Bounded wait per optional control
                ec.visibility_of_element_located((by, value))  # Find when visible on screen
            )
            el.click()  # Fire tap on discovered element
            self.LOGGER.info("Step Passed: Clicked `%s`.", label)  # Successful optional tap
            return True  # Signal control was interacted with
        except TimeoutException:  # Expected when popup absent
            self.LOGGER.info(
                "Optional element not shown: `%s` | locator=(%s, %s) | timeout=%ss",
                label,
                by,
                value,
                timeout,
            )  # Explain skip in logs
            return False  # Signal control was skipped

    def _send_keys(self, element, value, label="field"):  # Type into an EditText cleanly
        element.clear()  # Remove any prefilled characters
        element.send_keys(value)  # Type requested string sequence
        self.LOGGER.info("Step Passed: Entered text in `%s`.", label)  # Audit trail for inputs

    def _is_present(self, by, value, timeout=2):  # Boolean probe without asserting
        try:  # Silence timeout errors for negative checks
            WebDriverWait(self.driver, timeout).until(  # Short expectation window
                ec.presence_of_element_located((by, value))  # In DOM hierarchy (maybe not displayed)
            )
            return True  # Element existed before timeout exhausted
        except TimeoutException:  # Element never appeared within window
            return False  # Report absent for branching logic

    def _try_set_picker_text(self, resource_id, value):
        try:
            picker_input = WebDriverWait(self.driver, 2).until(
                ec.visibility_of_element_located((AppiumBy.ID, resource_id))
            )
            picker_input.click()
            try:
                picker_input.clear()
            except Exception:
                # Some Material clock chips are not editable text fields.
                pass
            picker_input.send_keys(value)

            # Guard: treat as success only when picker reflects requested value.
            observed = (picker_input.text or "").strip()
            if not observed:
                observed = (picker_input.get_attribute("text") or "").strip()
            if not observed:
                observed = (picker_input.get_attribute("content-desc") or "").strip()

            normalized_observed = "".join(ch for ch in observed if ch.isdigit())
            normalized_expected = "".join(ch for ch in str(value) if ch.isdigit())
            if normalized_observed.endswith(normalized_expected) and normalized_expected:
                self.LOGGER.info(
                    "Set picker `%s` to `%s` (observed `%s`).",
                    resource_id,
                    value,
                    observed,
                )
                return True

            self.LOGGER.info(
                "Picker `%s` did not reflect `%s` (observed `%s`); using fallback picker strategy.",
                resource_id,
                value,
                observed,
            )
            return False
        except Exception:
            self.LOGGER.debug("Picker input not editable for `%s`.", resource_id)
            return False

    def _set_time_using_radial_picker(self, target_dt):
        # Ensure radial picker exists before attempting content-desc based taps.
        radial = self._wait_visible(
            AppiumBy.ID, self.TIME_PICKER_RADIAL_ID, "Time radial picker", timeout=4
        )

        hour_12 = int(target_dt.strftime("%I"))  # 1..12
        minute_exact = int(target_dt.strftime("%M"))  # 0..59
        minute_rounded = int(round(minute_exact / 5.0) * 5) % 60

        # Make sure picker is in hour-selection mode before hour tap.
        self._tap_if_present_quiet(AppiumBy.ID, self.TIME_PICKER_HOURS_CHIP_ID)

        # Tap hour on radial clock.
        if not self._tap_radial_clock_value(radial, hour_12, is_minute=False):
            self.LOGGER.warning("Could not tap radial hour value `%s`.", hour_12)
        selected_hour = self._read_picker_chip_text(self.TIME_PICKER_HOURS_CHIP_ID)
        if selected_hour:
            self.LOGGER.info(
                "Picker hour chip after tap: `%s` (target `%s`).",
                selected_hour,
                hour_12,
            )

        # Switch to minute mode and tap nearest 5-minute tick.
        self._tap_if_present_quiet(AppiumBy.ID, self.TIME_PICKER_MINUTES_CHIP_ID)
        if not self._tap_radial_clock_value(radial, minute_rounded, is_minute=True):
            self.LOGGER.warning(
                "Could not tap radial minute value `%s` (rounded from `%s`).",
                str(minute_rounded).zfill(2),
                str(minute_exact).zfill(2),
            )
        selected_minute = self._read_picker_chip_text(self.TIME_PICKER_MINUTES_CHIP_ID)
        if selected_minute:
            self.LOGGER.info(
                "Picker minute chip after tap: `%s` (target `%s`).",
                selected_minute,
                str(minute_rounded).zfill(2),
            )

    def _tap_time_value_from_picker(self, value_text):
        candidates = (
            (AppiumBy.ACCESSIBILITY_ID, value_text),
            (AppiumBy.XPATH, f'//*[@content-desc="{value_text}"]'),
            (AppiumBy.XPATH, f'//*[contains(@content-desc, "{value_text}")]'),
            (AppiumBy.XPATH, f'//*[@text="{value_text}"]'),
        )
        for by, locator in candidates:
            try:
                el = WebDriverWait(self.driver, 1).until(
                    ec.element_to_be_clickable((by, locator))
                )
                el.click()
                self.LOGGER.info("Tapped time picker value `%s` using %s.", value_text, by)
                return True
            except Exception:
                continue
        return False

    def _tap_if_present_quiet(self, by, locator):
        try:
            for el in self.driver.find_elements(by, locator):
                if el.is_displayed():
                    el.click()
                    return True
        except Exception:
            return False
        return False

    def _set_picker_meridiem_if_present(self, target_meridiem):
        label = target_meridiem.strip().upper()
        if label not in {"AM", "PM"}:
            return False
        target_id = self.TIME_PICKER_AM_LABEL_ID if label == "AM" else self.TIME_PICKER_PM_LABEL_ID
        try:
            btn = WebDriverWait(self.driver, 2).until(
                ec.visibility_of_element_located((AppiumBy.ID, target_id))
            )
            btn.click()
            checked = str(btn.get_attribute("checked")).lower() == "true"
            self.LOGGER.info(
                "Time picker meridiem set to `%s` via `%s` (checked=%s).",
                label,
                target_id,
                checked,
            )
            return checked or True
        except TimeoutException:
            pass
        self.LOGGER.debug("AM/PM picker toggle not found; leaving current meridiem.")
        return False

    def _tap_radial_clock_value(self, radial_element, value, is_minute=False):
        rect = radial_element.rect
        center_x = rect["x"] + (rect["width"] / 2.0)
        center_y = rect["y"] + (rect["height"] / 2.0)
        radius = min(rect["width"], rect["height"]) * 0.38

        if is_minute:
            # Clock minute positions: 0 at top, then clockwise in 6-degree steps.
            step_index = int(value) % 60
            degrees = step_index * 6
        else:
            # Hours: 12 at top, then clockwise in 30-degree steps.
            hour = int(value) % 12
            degrees = hour * 30

        radians = math.radians(degrees - 90)  # shift so 0deg is at 12 o'clock
        tap_x = int(center_x + radius * math.cos(radians))
        tap_y = int(center_y + radius * math.sin(radians))

        try:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": tap_x, "y": tap_y},
            )
            self.LOGGER.info(
                "Tapped radial %s value `%s` at (%s,%s).",
                "minute" if is_minute else "hour",
                value,
                tap_x,
                tap_y,
            )
            return True
        except Exception as exc:
            self.LOGGER.debug(
                "Radial tap failed for %s value `%s`: %s",
                "minute" if is_minute else "hour",
                value,
                exc,
            )
            return False

    def _read_picker_chip_text(self, resource_id):
        try:
            el = self.driver.find_element(AppiumBy.ID, resource_id)
            txt = (el.text or "").strip()
            if txt:
                return txt
            return (el.get_attribute("text") or "").strip()
        except Exception:
            return ""

    def _assert_displayed_time_is_past(self, observed_time_text):
        observed = observed_time_text.strip().upper().replace(" ", "")
        now_local = datetime.now()
        parse_formats = ("%I:%M%p", "%H:%M")
        parsed_today = None
        for fmt in parse_formats:
            try:
                parsed = datetime.strptime(observed, fmt)
                parsed_today = now_local.replace(
                    hour=parsed.hour, minute=parsed.minute, second=0, microsecond=0
                )
                break
            except ValueError:
                continue
        assert parsed_today is not None, f"Unsupported time format for Start Time: {observed_time_text!r}"
        if parsed_today > now_local:
            parsed_today = parsed_today - timedelta(days=1)
        assert parsed_today < now_local, (
            f"Expected Start Time to be in the past, got {observed_time_text!r} (now={now_local.strftime('%I:%M %p')})."
        )

    def _is_displayed_time_strictly_past(self, observed_time_text):
        """
        True only when observed time is at least 1 minute older than current time.
        This prevents current-minute values from being treated as past.
        """
        observed = observed_time_text.strip().upper().replace(" ", "")
        now_local = datetime.now()
        parse_formats = ("%I:%M%p", "%H:%M")
        parsed_today = None
        for fmt in parse_formats:
            try:
                parsed = datetime.strptime(observed, fmt)
                parsed_today = now_local.replace(
                    hour=parsed.hour, minute=parsed.minute, second=0, microsecond=0
                )
                break
            except ValueError:
                continue
        if parsed_today is None:
            return False
        if parsed_today > now_local:
            parsed_today = parsed_today - timedelta(days=1)
        return parsed_today <= (now_local - timedelta(minutes=1))

    def _resolve_past_datetime_from_time_text(self, observed_time_text):
        observed = (observed_time_text or "").strip().upper().replace(" ", "")
        if not observed:
            return None
        now_local = datetime.now()

        # Explicit AM/PM is unambiguous.
        if observed.endswith("AM") or observed.endswith("PM"):
            try:
                parsed = datetime.strptime(observed, "%I:%M%p")
                resolved = now_local.replace(
                    hour=parsed.hour, minute=parsed.minute, second=0, microsecond=0
                )
                if resolved > now_local:
                    resolved = resolved - timedelta(days=1)
                return resolved
            except ValueError:
                return None

        # Ambiguous clock text like "2:50" (no AM/PM):
        # try both 24h interpretations (hour and hour+12), then pick nearest valid past.
        try:
            parsed_24 = datetime.strptime(observed, "%H:%M")
        except ValueError:
            return None

        base_hour = int(parsed_24.hour)
        minute = int(parsed_24.minute)
        candidates = []
        for hour in {base_hour, (base_hour + 12) % 24}:
            dt = now_local.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if dt > now_local:
                dt = dt - timedelta(days=1)
            candidates.append(dt)

        # Choose the closest value in the past to avoid 12-hour drift.
        candidates.sort(key=lambda dt: now_local - dt)
        return candidates[0] if candidates else None

    def _compute_duration_target_from_selected_start_time(self):
        selected_time_text = ""
        try:
            selected_time_text = (self._wait_visible(
                AppiumBy.ID, self.START_TIME_VALUE_ID, "Start Time value for duration compute", timeout=3
            ).text or "").strip()
        except Exception:
            selected_time_text = ""
        if not selected_time_text:
            selected_time_text = str(getattr(self, "_last_selected_start_time", "")).strip()
        selected_start_dt = self._resolve_past_datetime_from_time_text(selected_time_text)
        if selected_start_dt is None:
            # Safe fallback when start time was not captured.
            self.LOGGER.warning(
                "No usable selected Start Time captured; defaulting duration target to 01:00."
            )
            return 1, 0
        elapsed_minutes = int((datetime.now() - selected_start_dt).total_seconds() // 60)
        elapsed_minutes = max(1, elapsed_minutes)
        target_hours = min(23, elapsed_minutes // 60)
        target_minutes = elapsed_minutes % 60
        self.LOGGER.info(
            "Computed duration target from Start Time `%s`: %s minute(s) -> %s:%s.",
            selected_time_text,
            elapsed_minutes,
            str(target_hours).zfill(2),
            str(target_minutes).zfill(2),
        )
        return target_hours, target_minutes

    def _parse_duration_text(self, duration_text):
        raw = (duration_text or "").strip()
        if ":" in raw:
            left, right = raw.split(":", 1)
            try:
                return max(0, int(left)), max(0, int(right))
            except ValueError:
                pass
        number = self._extract_first_number(raw)
        if number is None:
            return 0, 0
        minutes_total = int(number)
        return minutes_total // 60, minutes_total % 60

    def _is_valid_duration_text(self, duration_text):
        raw = (duration_text or "").strip()
        match = re.fullmatch(r"(\d{1,2}):(\d{2})", raw)
        if not match:
            return False
        minutes = int(match.group(2))
        return 0 <= minutes <= 59

    def _is_duration_within_allowed_range(self, duration_text):
        raw = (duration_text or "").strip()
        match = re.fullmatch(r"(\d{1,2}):(\d{2})", raw)
        if not match:
            return False
        hours = int(match.group(1))
        minutes = int(match.group(2))
        total = (hours * 60) + minutes
        return 1 <= total <= 300

    def _extract_first_number(self, text_value):
        text = (text_value or "").strip()
        if not text:
            return None
        chars = []
        dot_seen = False
        started = False
        for ch in text:
            if ch.isdigit():
                chars.append(ch)
                started = True
                continue
            if ch == "." and started and not dot_seen:
                chars.append(ch)
                dot_seen = True
                continue
            if started:
                break
        try:
            return float("".join(chars)) if chars else None
        except ValueError:
            return None

    def _rotate_duration_wheel(self, wheel_element, steps, logical_name, direction="up"):
        """Rotate iOS-style wheel/picker using swipe gestures inside element bounds."""
        rect = wheel_element.rect
        if rect.get("height", 0) <= 0 or rect.get("width", 0) <= 0:
            raise AssertionError(f"{logical_name} has invalid bounds; cannot rotate picker wheel.")
        if direction not in {"up", "down"}:
            raise AssertionError(f"Invalid wheel rotation direction for {logical_name}: {direction!r}")

        left = int(rect["x"] + (rect["width"] * 0.15))
        top = int(rect["y"] + (rect["height"] * 0.15))
        width = int(rect["width"] * 0.7)
        height = int(rect["height"] * 0.7)
        for _ in range(max(1, int(steps))):
            self.driver.execute_script(
                "mobile: swipeGesture",
                {
                    "left": left,
                    "top": top,
                    "width": width,
                    "height": height,
                    "direction": direction,
                    "percent": 0.6,
                },
            )
            time.sleep(0.15)
        self.LOGGER.info(
            "Rotated `%s` by %s step(s), direction=%s.",
            logical_name,
            max(1, int(steps)),
            direction,
        )
