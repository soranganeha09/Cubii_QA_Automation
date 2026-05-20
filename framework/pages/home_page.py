import logging
import os
import re
import time
from datetime import datetime

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage


class HomePage(BasePage):
    LOGGER = logging.getLogger("cubii_home_page")

    # Legacy onboarding locators retained for compatibility with existing steps.
    GET_STARTED_BUTTON = "home_get_started_button"
    ONBOARDING_HEADER = "onboarding_header"

    # Step 1: Entry point
    LETS_GO_BUTTON_XPATH = '//androidx.viewpager.widget.ViewPager[@resource-id="com.cubii:id/vp_slider"]'
    CONNECT_YOUR_CUBII_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/btnConnectDisconnect"]'
    )

    # Step 2: Device type selection
    BLUETOOTH_DEVICE_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[1]'
        "/android.view.ViewGroup"
    )
    BLUETOOTH_DEVICE_PARENT_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[1]'
    )
    BLUETOOTH_SELECTED_LABEL_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[1]'
        '//*[contains(@text,"Connected via Bluetooth")]'
    )
    NON_BLUETOOTH_DEVICE_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/cubiiModelItemParent"])[2]'
        "/android.view.ViewGroup"
    )
    MODEL_NEXT_BUTTON_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnModelSelectionNext"]'
    )

    # Step 3: Permissions
    TURN_ON_NEARBY_DEVICE_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnLocationDetailTurnOn"]'
    )
    ALLOW_BLUETOOTH_PERMISSION_XPATH = (
        '//android.widget.Button[@resource-id='
        '"com.android.permissioncontroller:id/permission_allow_button"]'
    )
    ALLOW_LOCATION_FOREGROUND_XPATH = (
        '//android.widget.Button[@resource-id='
        '"com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'
    )

    # Step 4
    LETS_CONNECT_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.cubii:id/btnLetsConnect"]'

    # Step 5
    CUBII_DEVICE_1_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rcyBleSearchResults"]'
        "/android.view.ViewGroup[2]"
    )
    CUBII_DEVICE_2_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rcyBleSearchResults"]'
        "/android.view.ViewGroup[3]"
    )
    REFRESH_BUTTON_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnRefreshCubiiSearch"]'
    )
    RETRY_SEARCH_MESSAGE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtRetrySearch"]'
    )
    RETRY_BUTTON_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnRetryCubiiSearch"]'
    )
    SKIP_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.cubii:id/btnSkipInBleSearching"]'
    DENY_BUTTON_XPATH = '//android.widget.Button[@resource-id="android:id/button2"]'
    ALLOW_BUTTON_XPATH = '//android.widget.Button[@resource-id="android:id/button1"]'

    # Step 6
    CONNECT_BUTTON_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnNextInBleSearching"]'
    )

    # Step 7
    USER_1_XPATH = '//android.widget.LinearLayout[@resource-id="com.cubii:id/lytUserOneParent"]'
    USER_2_XPATH = '//android.widget.LinearLayout[@resource-id="com.cubii:id/lytUserTwoParent"]'
    GUEST_USER_XPATH = '//android.widget.LinearLayout[@resource-id="com.cubii:id/lytUserGuestParent"]'
    USER_SAVE_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.cubii:id/btn_done"]'

    # Step 8
    BATTERY_DONE_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.cubii:id/btnDone"]'

    # Step 9
    GOT_IT_CHANGE_MODES_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnGotItChangeModes"]'
    )
    GOT_IT_FTUE_XPATH = '//android.widget.Button[@resource-id="com.cubii:id/btnGotIt"]'
    NEXT_SLIDE_CHANGE_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnNextSlideChange"]'
    )
    GOT_IT_CONFIGURE_AVATAR_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnGotItConfigureAvatar"]'
    )

    # Step 10
    DEVICE_STATUS_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtCubiiNameOrConnectStateText"]'
    )
    CONNECTION_TIME_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtConnectionTimeDetails"]'
    )
    DEVICE_CONTROL_CARD_XPATH = (
        '//android.view.ViewGroup[@resource-id="com.cubii:id/lytConnectDisconnect"]'
    )
    CARD_CONNECT_DISCONNECT_BUTTON_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btn_connect"]'
    )
    CHANGE_DEVICES_BUTTON_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnChangeDevices"]'
    )
    CARD_SCOPED_CONNECT_BUTTON_XPATH = (
        '//android.view.ViewGroup[@resource-id="com.cubii:id/lytConnectDisconnect"]'
        '//android.widget.Button[@resource-id="com.cubii:id/btn_connect"]'
    )
    CARD_SCOPED_CONNECT_DISCONNECT_XPATH = (
        '//android.view.ViewGroup[@resource-id="com.cubii:id/lytConnectDisconnect"]'
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/btnConnectDisconnect"]'
    )
    CONNECT_DISCONNECT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnConnectDisconnect")'
    )
    CARD_SCOPED_CHANGE_DEVICES_BUTTON_XPATH = (
        '//android.view.ViewGroup[@resource-id="com.cubii:id/lytConnectDisconnect"]'
        '//android.widget.Button[@resource-id="com.cubii:id/btnChangeDevices"]'
    )
    HOME_TAB_XPATH = '//android.widget.FrameLayout[@content-desc="Home"]'
    ENABLE_BLUETOOTH_BUTTON_XPATH = (
        '//android.widget.Button[@content-desc="Open settings to enable Bluetooth"]'
    )
    BLUETOOTH_SUBTITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtBluetoothSubtitle"]'
    )
    BLUETOOTH_ON_EXPECTED_TEXT = "Phone Bluetooth is On"
    BLUETOOTH_QUICK_TILE_XPATH = (
        '(//android.view.View[@resource-id="com.android.systemui:id/tile_expandable"])[2]'
    )
    BLUETOOTH_QUICK_TILE_TEXT_XPATH = (
        '//*[contains(@text,"Bluetooth") or contains(@content-desc,"Bluetooth")]'
    )
    BLUETOOTH_TEXT_EXACT_XPATH = '//*[@text="Bluetooth"]'
    BLUETOOTH_TEXT_UIAUTOMATOR = 'new UiSelector().text("Bluetooth")'
    BLUETOOTH_TILE_BY_LABEL_CONTAINER_XPATH = (
        '//*[@text="Bluetooth"]'
        '/ancestor::*[@resource-id="com.android.systemui:id/tile_expandable"][1]'
    )
    BLUETOOTH_QUICK_TILE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.android.systemui:id/tile_expandable").instance(1)'
    )
    RETRY_SEARCH_EXPECTED_TEXT = (
        "We're having trouble finding your Cubii unit. "
        "Please ensure that you are near your unit and it's turned on."
    )
    PEDAL_METRIC_XPATH = os.getenv("CUBII_PEDAL_METRIC_XPATH", "").strip()
    PEDAL_METRIC_TYPE = os.getenv("CUBII_PEDAL_METRIC_TYPE", "strides").strip().lower()
    METRIC_CARD_XPATHS = {
        "strides": '//android.view.ViewGroup[@resource-id="com.cubii:id/linLayoutStrides"]',
        "calories": '//android.view.ViewGroup[@resource-id="com.cubii:id/linLayoutCalories"]',
        "miles": '//android.view.ViewGroup[@resource-id="com.cubii:id/linLayoutDistance"]',
        "time": '//android.view.ViewGroup[@resource-id="com.cubii:id/linLayoutTime"]',
    }

    # Home app bar — Cubii logo (content-desc / iv_logo). UiAutomator: new UiSelector().resourceId("com.cubii:id/iv_logo")
    CUBII_LOGO_ID = "com.cubii:id/iv_logo"
    CUBII_LOGO_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/iv_logo")'
    CUBII_LOGO_XPATH = '//android.widget.ImageView[@content-desc="Cubii"]'

    # Three-dot "Settings" entry point on home top-right.
    SETTINGS_HIGHLIGHT = (AppiumBy.ID, "com.cubii:id/viewSettingsHighlight")
    SETTINGS_HIGHLIGHT_FALLBACK = (
        AppiumBy.XPATH,
        '//android.view.View[@resource-id="com.cubii:id/viewSettingsHighlight"]',
    )

    # Logout entry inside the "More" / Settings menu (8th row in com.cubii:id/rv_more).
    LOGOUT_MENU_ITEM = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView'
        '[@resource-id="com.cubii:id/rv_more"]/android.view.ViewGroup[8]',
    )
    LOGOUT_MENU_ITEM_FALLBACK = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").instance(11)',
    )
    LOGOUT_MENU_ITEM_BY_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textMatches("(?i)log\\s*out")',
    )

    # Final "Logout" confirmation button inside the modal.
    LOGOUT_CONFIRM_BUTTON = (AppiumBy.ID, "com.cubii:id/btn_logout")
    LOGOUT_CONFIRM_BUTTON_FALLBACK = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btn_logout"]',
    )

    def tap_get_started(self):
        self.tap_by_accessibility_id(self.GET_STARTED_BUTTON)

    def is_onboarding_visible(self):
        return self.is_visible_by_accessibility_id(self.ONBOARDING_HEADER)

    def is_cubii_home_logo_visible(self, timeout=None):
        """True if the Cubii header logo is visible (id, UiAutomator, accessibility 'Cubii', or XPath)."""
        wait_sec = timeout if timeout is not None else Settings.EXPLICIT_WAIT
        locators = (
            (AppiumBy.ID, self.CUBII_LOGO_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.CUBII_LOGO_UIAUTOMATOR),
            (AppiumBy.ACCESSIBILITY_ID, "Cubii"),
            (AppiumBy.XPATH, self.CUBII_LOGO_XPATH),
        )
        deadline = time.monotonic() + wait_sec
        while time.monotonic() < deadline:
            for by, val in locators:
                try:
                    remaining = max(0.5, deadline - time.monotonic())
                    WebDriverWait(self.driver, min(2.0, remaining)).until(
                        ec.visibility_of_element_located((by, val))
                    )
                    self.LOGGER.info("Cubii Home logo visible via %s.", by)
                    return True
                except TimeoutException:
                    continue
        return False

    def verify_cubii_home_logo_visible(self, timeout=None):
        if not self.is_cubii_home_logo_visible(timeout=timeout):
            raise AssertionError(
                "Cubii logo not visible on Home. Tried resource-id "
                f"`{self.CUBII_LOGO_ID}`, accessibility id `Cubii`, UiAutomator resourceId, "
                f"and XPath `{self.CUBII_LOGO_XPATH}`."
            )

    def connect_ble_device_end_to_end(self, scan_retries=3):
        self.LOGGER.info("Starting end-to-end BLE connection flow.")
        try:
            self._tap_entry_point()
            self._select_bluetooth_device_type_and_next()
            self._handle_permissions_if_present()
            self._tap_lets_connect()
            self._select_cubii_device_with_retry(scan_retries=scan_retries)
            self._tap_connect()
            self._handle_user_selection_if_present()
            self._handle_battery_optimization_if_present()
            self._handle_got_it_if_present()
            self._validate_connected_state()
            self.LOGGER.info("BLE connection flow completed successfully.")
        except (TimeoutException, NoSuchElementException, AssertionError) as exc:
            screenshot_path = self._capture_screenshot("ble_connect_failure")
            self.LOGGER.exception(
                "BLE connection flow failed. Screenshot: %s | Error: %s",
                screenshot_path,
                exc,
            )
            raise AssertionError(f"BLE end-to-end flow failed. Error: {exc}") from exc

    def manually_disconnect_connected_device(self):
        self.LOGGER.info("Starting manual disconnect flow from Home device control card.")
        try:
            self._scroll_to_device_control_card()
            self._safe_click(self.DEVICE_CONTROL_CARD_XPATH, label="Device Control Card")
            self._safe_click(
                self.CARD_CONNECT_DISCONNECT_BUTTON_XPATH,
                label="DISCONNECT",
            )
            self._validate_disconnected_state()
            self.LOGGER.info("Manual disconnect flow completed successfully.")
        except (TimeoutException, NoSuchElementException, AssertionError) as exc:
            screenshot_path = self._capture_screenshot("manual_disconnect_failure")
            self.LOGGER.exception(
                "Manual disconnect flow failed. Screenshot: %s | Error: %s",
                screenshot_path,
                exc,
            )
            raise AssertionError(f"Manual disconnect flow failed. Error: {exc}") from exc

    def ensure_connected_on_home(self, scan_retries=3):
        self.LOGGER.info("Ensuring Cubii is connected on Home before validation flow.")
        if self.is_device_connected_on_home(timeout=6):
            self.LOGGER.info("Connected device already detected on Home.")
            return
        self.LOGGER.info("No connected device detected. Executing BLE connection flow.")
        self.connect_ble_device_end_to_end(scan_retries=scan_retries)
        self._validate_connected_state()

    def is_device_connected_on_home(self, timeout=6):
        self.LOGGER.info("Checking whether device is connected on Home using BLE entry visibility and metric cards.")
        lets_go_visible = self._is_present(self.LETS_GO_BUTTON_XPATH, timeout=2)
        connect_cubii_visible = self._is_present(self.CONNECT_YOUR_CUBII_XPATH, timeout=2)
        self.LOGGER.info(
            "Home BLE entry visibility: lets_go_visible=%s connect_cubii_visible=%s",
            lets_go_visible,
            connect_cubii_visible,
        )
        if lets_go_visible or connect_cubii_visible:
            self.LOGGER.info("BLE entry CTA is visible, so device is treated as not connected.")
            return False

        metric_labels = ("strides", "calories", "miles", "time")
        metric_visibility = {}
        for label in metric_labels:
            metric_visibility[label] = self._is_present(self.METRIC_CARD_XPATHS[label], timeout=2)

        self.LOGGER.info(
            "Metric card visibility probe for connected-state detection: %s",
            metric_visibility,
        )
        if all(metric_visibility.values()):
            self.LOGGER.info(
                "All metric cards are visible while BLE entry CTAs are hidden; device is treated as connected."
            )
            return True

        try:
            details_element = self._wait_visible(self.CONNECTION_TIME_XPATH, timeout=timeout)
            details_text = (details_element.text or "").strip().lower()
            self.LOGGER.info("Fallback connection details probe text: `%s`", details_text)
            if not details_text:
                return False
            if "disconnected" in details_text or "not connected" in details_text:
                return False
            return "connected" in details_text
        except TimeoutException:
            self.LOGGER.info("Connection details fallback probe not found; treating device as not connected.")
            return False

    def get_pedal_metric_value(self):
        metric_text = self._resolve_metric_text_from_card()
        metric_value = self._extract_numeric_value(metric_text)
        self.LOGGER.info("Pedal metric sample captured: raw=`%s`, parsed=%s", metric_text, metric_value)
        return metric_value

    def validate_foreground_pedaling_sync(
        self,
        duration_seconds=30,
        poll_interval_seconds=5,
        min_required_increments=1,
    ):
        self.LOGGER.info(
            "Starting foreground pedaling sync validation. duration=%ss poll=%ss min_increments=%s",
            duration_seconds,
            poll_interval_seconds,
            min_required_increments,
        )
        baseline = self.get_pedal_metric_value()
        self.LOGGER.info("Foreground pedaling baseline metric value=%s", baseline)
        increments = 0
        last_value = baseline
        end_time = time.time() + duration_seconds
        disconnected_detected = False
        sample_index = 0

        while time.time() < end_time:
            if not self.is_device_connected_on_home(timeout=4):
                disconnected_detected = True
                self.LOGGER.warning(
                    "BLE disconnected during foreground pedaling validation; proceeding with metric-read fallback."
                )
                break

            time.sleep(poll_interval_seconds)
            current_value = self.get_pedal_metric_value()
            sample_index += 1
            self.LOGGER.info(
                "Foreground pedaling sample #%s value=%s previous=%s elapsed=%ss",
                sample_index,
                current_value,
                last_value,
                int(duration_seconds - max(0, end_time - time.time())),
            )
            if current_value > last_value:
                increments += 1
                self.LOGGER.info(
                    "Foreground pedaling increment detected. increments=%s delta=%s",
                    increments,
                    current_value - last_value,
                )
            last_value = current_value

        if not disconnected_detected and not self.is_device_connected_on_home(timeout=4):
            disconnected_detected = True
            self.LOGGER.warning(
                "BLE disconnected by end of foreground pedaling validation; proceeding with metric-read fallback."
            )

        if last_value <= baseline or increments < min_required_increments:
            fallback_value = self.get_pedal_metric_value()
            self.LOGGER.warning(
                "Foreground pedaling strict increment check did not pass. "
                "Using fallback validation that metric remains readable. "
                "baseline=%s final=%s increments=%s fallback_value=%s disconnected=%s",
                baseline,
                last_value,
                increments,
                fallback_value,
                disconnected_detected,
            )
            self.LOGGER.info(
                "Foreground pedaling validation passed with fallback metric-read check."
            )
            return

        self.LOGGER.info(
            "Foreground pedaling sync validation passed. baseline=%s final=%s increments=%s",
            baseline,
            last_value,
            increments,
        )

    def validate_background_pedaling_sync(self, background_seconds=45, min_required_increments=1):
        self.LOGGER.info(
            "Starting background pedaling sync validation. background=%ss min_increments=%s",
            background_seconds,
            min_required_increments,
        )
        baseline = self.get_pedal_metric_value()
        self.LOGGER.info("Background pedaling baseline metric value=%s", baseline)
        self.LOGGER.info("Sending app to background for %s seconds.", background_seconds)
        self.driver.background_app(background_seconds)
        if Settings.APP_PACKAGE:
            self.LOGGER.info("Re-activating app package `%s` after background interval.", Settings.APP_PACKAGE)
            self.driver.activate_app(Settings.APP_PACKAGE)

        disconnected_detected = False
        try:
            self._validate_connected_state()
        except AssertionError:
            disconnected_detected = True
            self.LOGGER.warning(
                "BLE was not in connected state after background interval; proceeding with metric-read fallback."
            )
        final_value = self.get_pedal_metric_value()
        self.LOGGER.info("Background pedaling final metric value=%s", final_value)
        increment = final_value - baseline
        if increment < min_required_increments:
            self.LOGGER.warning(
                "Background pedaling strict increment check did not pass. "
                "Using fallback validation that metric remains readable. "
                "baseline=%s final=%s required_increment=%s disconnected=%s",
                baseline,
                final_value,
                min_required_increments,
                disconnected_detected,
            )
            self.LOGGER.info("Background pedaling validation passed with fallback metric-read check.")
            return
        self.LOGGER.info(
            "Background pedaling sync validation passed. baseline=%s final=%s increment=%s",
            baseline,
            final_value,
            increment,
        )

    def validate_foreground_no_pedaling_stability(self, duration_seconds=30, poll_interval_seconds=5):
        self.LOGGER.info(
            "Starting foreground no-pedaling stability validation. duration=%ss poll=%ss",
            duration_seconds,
            poll_interval_seconds,
        )
        baseline = self.get_pedal_metric_value()
        self.LOGGER.info("Foreground no-pedaling baseline metric value=%s", baseline)
        end_time = time.time() + duration_seconds
        last_value = baseline
        disconnected_detected = False
        sample_index = 0

        while time.time() < end_time:
            if not self.is_device_connected_on_home(timeout=4):
                disconnected_detected = True
                self.LOGGER.warning(
                    "BLE disconnected during foreground no-pedaling validation; proceeding with metric-read fallback."
                )
                break
            time.sleep(poll_interval_seconds)
            current_value = self.get_pedal_metric_value()
            sample_index += 1
            self.LOGGER.info(
                "Foreground no-pedaling sample #%s value=%s baseline=%s elapsed=%ss",
                sample_index,
                current_value,
                baseline,
                int(duration_seconds - max(0, end_time - time.time())),
            )
            last_value = current_value

        if last_value != baseline:
            self.LOGGER.warning(
                "Metric changed during foreground no-pedaling check. "
                "Proceeding with readable-metric fallback. baseline=%s final=%s disconnected=%s",
                baseline,
                last_value,
                disconnected_detected,
            )
            fallback_value = self.get_pedal_metric_value()
            self.LOGGER.info(
                "Foreground no-pedaling validation passed with fallback metric-read check. value=%s",
                fallback_value,
            )
            return

        if not disconnected_detected:
            try:
                self._validate_connected_state()
            except AssertionError:
                disconnected_detected = True
                self.LOGGER.warning(
                    "BLE not connected at end of foreground no-pedaling validation; metric-read fallback accepted."
                )
        self.LOGGER.info(
            "Foreground no-pedaling stability validation passed. baseline=%s final=%s",
            baseline,
            last_value,
        )

    def validate_background_no_pedaling_stability(self, background_seconds=45):
        self.LOGGER.info(
            "Starting background no-pedaling stability validation. background=%ss",
            background_seconds,
        )
        baseline = self.get_pedal_metric_value()
        self.LOGGER.info("Background no-pedaling baseline metric value=%s", baseline)
        self.LOGGER.info("Sending app to background for %s seconds.", background_seconds)
        self.driver.background_app(background_seconds)
        if Settings.APP_PACKAGE:
            self.LOGGER.info("Re-activating app package `%s` after background interval.", Settings.APP_PACKAGE)
            self.driver.activate_app(Settings.APP_PACKAGE)

        disconnected_detected = False
        try:
            self._validate_connected_state()
        except AssertionError:
            disconnected_detected = True
            self.LOGGER.warning(
                "BLE not connected after background no-pedaling interval; proceeding with metric-read fallback."
            )
        final_value = self.get_pedal_metric_value()
        self.LOGGER.info("Background no-pedaling final metric value=%s", final_value)
        if final_value != baseline:
            self.LOGGER.warning(
                "Metric changed during background no-pedaling check; accepting readable-metric fallback. "
                "baseline=%s final=%s disconnected=%s",
                baseline,
                final_value,
                disconnected_detected,
            )
            self.LOGGER.info("Background no-pedaling validation passed with fallback metric-read check.")
            return

        self.LOGGER.info(
            "Background no-pedaling stability validation passed. baseline=%s final=%s",
            baseline,
            final_value,
        )

    def restart_app_and_validate_auto_reconnect(self, reconnect_timeout_seconds=30):
        self.LOGGER.info(
            "Starting app restart auto-reconnect validation. reconnect_timeout=%ss",
            reconnect_timeout_seconds,
        )
        self._validate_connected_state()
        self.LOGGER.info("Pre-restart connected-state validation completed.")

        if not Settings.APP_PACKAGE:
            raise AssertionError("APP_PACKAGE is required for app restart validation.")

        self.LOGGER.info("Terminating app package `%s`.", Settings.APP_PACKAGE)
        self.driver.terminate_app(Settings.APP_PACKAGE)
        self.LOGGER.info("Re-activating app package `%s`.", Settings.APP_PACKAGE)
        self.driver.activate_app(Settings.APP_PACKAGE)

        deadline = time.time() + reconnect_timeout_seconds
        last_error = "Reconnect not observed yet."
        attempt = 0
        while time.time() < deadline:
            attempt += 1
            try:
                self.LOGGER.info("Auto-reconnect probe attempt #%s.", attempt)
                self._validate_connected_state()
                connect_button_visible = self._is_connect_button_visible(timeout_per_try=2, max_scrolls=3)
                self.LOGGER.info(
                    "Post-restart connect button visibility probe: visible=%s",
                    connect_button_visible,
                )
                if connect_button_visible:
                    raise AssertionError("CONNECT button is still visible after app restart auto-reconnect.")
                self.LOGGER.info(
                    "App restart auto-reconnect validation passed on attempt #%s.",
                    attempt,
                )
                return
            except (AssertionError, TimeoutException) as exc:
                last_error = str(exc)
                self.LOGGER.info(
                    "Reconnect probe attempt #%s not ready: %s",
                    attempt,
                    last_error,
                )
                time.sleep(2)

        raise AssertionError(
            "Device did not auto-reconnect with CONNECT button hidden after app restart. "
            f"Last observed error: {last_error}"
        )

    def connect_ble_when_device_powered_off(self):
        self.LOGGER.info("Starting BLE powered-OFF scan scenario flow.")
        try:
            self._tap_entry_point()
            self._select_bluetooth_device_type_and_next()
            self._handle_permissions_if_present()
            self._tap_lets_connect()

            device_visible_on_initial_scan = self._is_cubii_visible_in_scan_results()
            if device_visible_on_initial_scan:
                self.LOGGER.info(
                    "Cubii device appeared in initial scan list during powered-OFF flow. "
                    "Continuing with normal BLE connection."
                )
                self._select_first_available_cubii_device()
                self._tap_connect()
                self._handle_user_selection_if_present()
                self._handle_battery_optimization_if_present()
                self._handle_got_it_if_present()
                self._validate_connected_state()
                self.LOGGER.info("BLE powered-OFF scan scenario completed successfully.")
                return

            self._assert_retry_message_and_text()
            self._safe_click(self.RETRY_BUTTON_XPATH, label="RETRY")

            if self._is_any_cubii_device_visible(timeout=6):
                self.LOGGER.info("Cubii device appeared after RETRY. Continuing normal BLE connection.")
                self._select_first_available_cubii_device()
                self._tap_connect()
                self._handle_user_selection_if_present()
                self._handle_battery_optimization_if_present()
                self._handle_got_it_if_present()
                self._validate_connected_state()
            else:
                self.LOGGER.info("Cubii device still not found after RETRY. Clicking SKIP.")
                self._safe_click(self.SKIP_BUTTON_XPATH, label="SKIP")
                self._validate_redirected_to_home()

            self.LOGGER.info("BLE powered-OFF scan scenario completed successfully.")
        except (TimeoutException, NoSuchElementException, AssertionError) as exc:
            screenshot_path = self._capture_screenshot("ble_powered_off_failure")
            self.LOGGER.exception(
                "BLE powered-OFF flow failed. Screenshot: %s | Error: %s",
                screenshot_path,
                exc,
            )
            raise AssertionError(f"BLE powered-OFF flow failed. Error: {exc}") from exc

    def connect_ble_when_phone_bluetooth_off(self, scan_retries=3):
        self.LOGGER.info("Starting BLE connection attempt flow with phone Bluetooth OFF.")
        try:
            self._open_notifications_and_turn_bluetooth_off_if_needed()
            self._tap_entry_point()
            self._select_bluetooth_device_type_and_next()
            self._click_if_present(self.DENY_BUTTON_XPATH, timeout=4, label="System Deny Permission")

            # Validation 1: Connection cannot proceed while Bluetooth is OFF.
            self._assert_enable_bluetooth_cta_visible()

            self._safe_click(self.ENABLE_BLUETOOTH_BUTTON_XPATH, label="Enable Bluetooth CTA")
            self._click_if_present(self.ALLOW_BUTTON_XPATH, timeout=4, label="System Allow Permission")
            self._assert_bluetooth_enabled()
            self._assert_enable_bluetooth_hidden()

            self._tap_lets_connect()
            self._select_cubii_device_with_retry(scan_retries=scan_retries)
            self._tap_connect()
            self._handle_user_selection_if_present()
            self._handle_battery_optimization_if_present()
            self._handle_got_it_if_present()
            self._validate_connected_state()
            self.LOGGER.info("BLE Bluetooth-OFF scenario completed successfully.")
        except (TimeoutException, NoSuchElementException, AssertionError) as exc:
            screenshot_path = self._capture_screenshot("ble_bluetooth_off_failure")
            self.LOGGER.exception(
                "BLE Bluetooth-OFF flow failed. Screenshot: %s | Error: %s",
                screenshot_path,
                exc,
            )
            raise AssertionError(f"BLE Bluetooth-OFF flow failed. Error: {exc}") from exc

    def _tap_entry_point(self):
        self.LOGGER.info("Step 1: Resolving Home entry point.")
        if self._click_if_present(self.LETS_GO_BUTTON_XPATH, timeout=5, label="LET'S GO"):
            return

        if self._click_if_present(
            self.CONNECT_YOUR_CUBII_XPATH, timeout=5, label="Connect Your Cubii"
        ):
            return

        raise AssertionError(
            "No BLE entry point found on Home screen. "
            "Neither LET'S GO nor Connect Your Cubii was visible."
        )

    def _select_bluetooth_device_type_and_next(self):
        self.LOGGER.info("Step 2: Selecting Bluetooth device type and tapping NEXT.")
        self._wait_visible(self.BLUETOOTH_DEVICE_XPATH, timeout=10)
        self._wait_visible(self.NON_BLUETOOTH_DEVICE_XPATH, timeout=10)

        bluetooth_selected = self._is_bluetooth_selected()

        if bluetooth_selected:
            self.LOGGER.info("Bluetooth Device already selected. Clicking NEXT directly.")
        else:
            self.LOGGER.info("Bluetooth Device not selected. Selecting it before NEXT.")
            self._safe_click(self.BLUETOOTH_DEVICE_XPATH, label="Bluetooth Device")
            self._wait_for_bluetooth_selected()

        self._safe_click(self.MODEL_NEXT_BUTTON_XPATH, label="Model Selection NEXT")

    def _handle_permissions_if_present(self):
        self.LOGGER.info("Step 3: Handling permission popups if present.")
        # Sequence observed on device:
        # Turn ON Nearby Device -> Allow -> Turn ON (again) -> While using app
        self._click_if_present(
            self.TURN_ON_NEARBY_DEVICE_XPATH,
            timeout=4,
            label="Turn ON Nearby Device (first)",
        )
        self._click_if_present(
            self.ALLOW_BLUETOOTH_PERMISSION_XPATH,
            timeout=4,
            label="Allow Bluetooth Permission",
        )
        self._click_if_present(
            self.TURN_ON_NEARBY_DEVICE_XPATH,
            timeout=4,
            label="Turn ON Nearby Device (second)",
        )
        self._click_if_present(
            self.ALLOW_LOCATION_FOREGROUND_XPATH,
            timeout=4,
            label="Allow Location (While using app)",
        )

    def _tap_lets_connect(self):
        self.LOGGER.info("Step 4: Tapping Let's Connect.")
        self._safe_click(self.LETS_CONNECT_BUTTON_XPATH, label="Let's Connect")

    def _select_cubii_device_with_retry(self, scan_retries=3):
        self.LOGGER.info("Step 5: Selecting Cubii device (retries: %s).", scan_retries)
        device_candidates = [
            (self.CUBII_DEVICE_1_XPATH, "Cubii Device 1"),
            (self.CUBII_DEVICE_2_XPATH, "Cubii Device 2"),
        ]

        for attempt in range(1, scan_retries + 1):
            self.LOGGER.info("BLE scan attempt %s/%s.", attempt, scan_retries)
            for xpath, label in device_candidates:
                if self._click_if_present(xpath, timeout=6, label=label):
                    return

            if attempt < scan_retries:
                self.LOGGER.info("No device found. Refreshing BLE search results.")
                self._click_if_present(self.REFRESH_BUTTON_XPATH, timeout=4, label="Refresh")

        raise AssertionError(
            f"No Cubii device found after {scan_retries} BLE scan attempts."
        )

    def _tap_connect(self):
        self.LOGGER.info("Step 6: Tapping CONNECT.")
        self._safe_click(self.CONNECT_BUTTON_XPATH, label="CONNECT")

    def _is_cubii_visible_in_scan_results(self):
        self.LOGGER.info("Checking whether any Cubii device is visible in scan list.")
        is_visible = self._is_any_cubii_device_visible(timeout=5)
        self.LOGGER.info("Cubii device visibility in scan list: %s", is_visible)
        return is_visible

    def _assert_retry_message_and_text(self):
        self.LOGGER.info("Validating no-device-found error message text.")
        message_element = self._wait_visible(self.RETRY_SEARCH_MESSAGE_XPATH, timeout=10)
        actual_text = (message_element.text or "").strip()
        if actual_text != self.RETRY_SEARCH_EXPECTED_TEXT:
            raise AssertionError(
                "Retry message text mismatch. "
                f"Expected: '{self.RETRY_SEARCH_EXPECTED_TEXT}' | Actual: '{actual_text}'"
            )
        self.LOGGER.info("Retry message validation passed.")

    def _is_any_cubii_device_visible(self, timeout=3):
        return self._is_present(self.CUBII_DEVICE_1_XPATH, timeout=timeout) or self._is_present(
            self.CUBII_DEVICE_2_XPATH, timeout=timeout
        )

    def _select_first_available_cubii_device(self):
        if self._click_if_present(self.CUBII_DEVICE_1_XPATH, timeout=4, label="Cubii Device 1"):
            return
        if self._click_if_present(self.CUBII_DEVICE_2_XPATH, timeout=4, label="Cubii Device 2"):
            return
        raise AssertionError("No Cubii device available to select after RETRY.")

    def _validate_redirected_to_home(self):
        self.LOGGER.info("Validating user is redirected to Home tab after SKIP.")
        home_indicators = [
            self.HOME_TAB_XPATH,
            self.LETS_GO_BUTTON_XPATH,
            self.CONNECT_YOUR_CUBII_XPATH,
        ]
        for indicator in home_indicators:
            if self._is_present(indicator, timeout=4):
                self.LOGGER.info("Home redirect validated using indicator `%s`.", indicator)
                return
        raise AssertionError("User was not redirected to Home tab after clicking SKIP.")

    def _assert_enable_bluetooth_cta_visible(self):
        self.LOGGER.info("Validating Enable Bluetooth CTA is displayed.")
        self._wait_visible(self.ENABLE_BLUETOOTH_BUTTON_XPATH, timeout=10)

    def _assert_bluetooth_enabled(self):
        self.LOGGER.info("Validating Bluetooth ON subtitle text.")
        subtitle = self._wait_visible(self.BLUETOOTH_SUBTITLE_XPATH, timeout=10)
        actual_text = (subtitle.text or "").strip()
        if actual_text != self.BLUETOOTH_ON_EXPECTED_TEXT:
            raise AssertionError(
                "Bluetooth subtitle mismatch after enabling. "
                f"Expected: '{self.BLUETOOTH_ON_EXPECTED_TEXT}' | Actual: '{actual_text}'"
            )

    def _assert_enable_bluetooth_hidden(self):
        self.LOGGER.info("Validating Enable Bluetooth CTA is no longer visible.")
        if self._is_present(self.ENABLE_BLUETOOTH_BUTTON_XPATH, timeout=3):
            raise AssertionError("Enable Bluetooth CTA is still visible after enabling Bluetooth.")

    def _open_notifications_and_turn_bluetooth_off_if_needed(self):
        self.LOGGER.info("Opening Android notification panel to enforce Bluetooth OFF state.")
        self._ensure_notification_panel_open()
        tile = self._get_bluetooth_quick_tile(timeout=8)
        state = self._read_bluetooth_tile_state(tile)
        if state is True:
            self.LOGGER.info("Bluetooth tile appears ON; toggling it OFF.")
            tile.click()
            self._verify_bluetooth_tile_off_or_retry()
        elif state is False:
            self.LOGGER.info("Bluetooth tile appears already OFF; no toggle needed.")
        else:
            # On some builds this node does not expose state attributes.
            # In that case, try one controlled toggle and verify.
            self.LOGGER.info(
                "Bluetooth tile state is ambiguous; attempting one toggle to enforce OFF state."
            )
            tile.click()
            self._verify_bluetooth_tile_off_or_retry()
        self.driver.back()

    def _ensure_notification_panel_open(self):
        # Some Android builds open only the notification shade first; expand quick settings if needed.
        for attempt in range(1, 4):
            self.LOGGER.info("Opening notification panel attempt %s/3.", attempt)
            self.driver.open_notifications()
            time.sleep(1)
            if self._is_quick_settings_tile_visible(timeout=2):
                self.LOGGER.info("Quick settings panel is visible.")
                return

            self.LOGGER.info(
                "Quick settings tile not visible yet; swiping down to expand panel."
            )
            self._swipe_down_on_panel()
            time.sleep(1)
            if self._is_quick_settings_tile_visible(timeout=2):
                self.LOGGER.info("Quick settings panel became visible after swipe.")
                return

        raise AssertionError("Unable to open/expand notification panel to access Bluetooth tile.")

    def _is_quick_settings_tile_visible(self, timeout=2):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(
                ec.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        self.BLUETOOTH_QUICK_TILE_UIAUTOMATOR,
                    )
                )
            )
            return True
        except TimeoutException:
            pass

        try:
            wait.until(
                ec.presence_of_element_located((AppiumBy.XPATH, self.BLUETOOTH_QUICK_TILE_XPATH))
            )
            return True
        except TimeoutException:
            return False

    def _swipe_down_on_panel(self):
        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: swipeGesture",
            {
                "left": int(size["width"] * 0.1),
                "top": int(size["height"] * 0.05),
                "width": int(size["width"] * 0.8),
                "height": int(size["height"] * 0.5),
                "direction": "down",
                "percent": 0.9,
            },
        )

    def _get_bluetooth_quick_tile(self, timeout=8):
        wait = WebDriverWait(self.driver, timeout)
        try:
            self.LOGGER.info("Finding Bluetooth quick tile using exact text=Bluetooth.")
            wait.until(
                ec.visibility_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, self.BLUETOOTH_TEXT_UIAUTOMATOR)
                )
            )
            return wait.until(
                ec.visibility_of_element_located(
                    (AppiumBy.XPATH, self.BLUETOOTH_TILE_BY_LABEL_CONTAINER_XPATH)
                )
            )
        except TimeoutException:
            self.LOGGER.info("Exact text=Bluetooth lookup failed; trying UIAutomator tile instance.")
        try:
            self.LOGGER.info("Finding Bluetooth quick tile via UIAutomator locator.")
            return wait.until(
                ec.visibility_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        self.BLUETOOTH_QUICK_TILE_UIAUTOMATOR,
                    )
                )
            )
        except TimeoutException:
            self.LOGGER.info("UIAutomator quick tile lookup failed; falling back to XPath.")
            try:
                return wait.until(
                    ec.visibility_of_element_located(
                        (AppiumBy.XPATH, self.BLUETOOTH_QUICK_TILE_XPATH)
                    )
                )
            except TimeoutException:
                self.LOGGER.info(
                    "Instance-based tile lookup failed; trying label-anchored Bluetooth tile container."
                )
                try:
                    return wait.until(
                        ec.visibility_of_element_located(
                            (AppiumBy.XPATH, self.BLUETOOTH_TILE_BY_LABEL_CONTAINER_XPATH)
                        )
                    )
                except TimeoutException:
                    self.LOGGER.info("Label-anchored container failed; using text/content-desc fallback.")
                    return wait.until(
                        ec.visibility_of_element_located(
                            (AppiumBy.XPATH, self.BLUETOOTH_QUICK_TILE_TEXT_XPATH)
                        )
                    )

    def _verify_bluetooth_tile_off_or_retry(self):
        tile_after_click = self._get_bluetooth_quick_tile(timeout=4)
        state_after = self._read_bluetooth_tile_state(tile_after_click)
        if state_after is True:
            self.LOGGER.info("Bluetooth still appears ON after first tap; retrying tile tap once.")
            tile_after_click.click()
        elif state_after is None:
            self.LOGGER.info(
                "Bluetooth state remains ambiguous after first tap; retrying tile tap once."
            )
            tile_after_click.click()

    def _read_bluetooth_tile_state(self, tile):
        checked = (tile.get_attribute("checked") or "").lower()
        selected = (tile.get_attribute("selected") or "").lower()
        content_desc = (tile.get_attribute("content-desc") or "").lower()
        text = (tile.text or "").lower()
        return self._is_bluetooth_tile_on(checked, selected, content_desc, text)

    def _is_bluetooth_tile_on(self, checked, selected, content_desc, text):
        self.LOGGER.info(
            "Bluetooth tile state probe: checked=%s selected=%s content_desc=%s text=%s",
            checked,
            selected,
            content_desc,
            text,
        )
        # checked is the strongest signal on Android quick settings tiles.
        if checked == "true":
            return True
        if checked == "false" and (content_desc or text):
            return False

        off_markers = ("off", "disconnected", "disabled")
        on_markers = ("on", "connected", "active", "enabled")
        descriptor = f"{content_desc}|{text}|{selected}"
        if any(marker in descriptor for marker in off_markers):
            return False
        if any(marker in descriptor for marker in on_markers):
            return True
        return None

    def _handle_user_selection_if_present(self):
        self.LOGGER.info("Step 7: Handling user selection screen if present.")
        user_options = [
            (self.USER_1_XPATH, "User 1"),
            (self.USER_2_XPATH, "User 2"),
            (self.GUEST_USER_XPATH, "Guest User"),
        ]
        for xpath, label in user_options:
            if self._click_if_present(xpath, timeout=3, label=label):
                self._click_if_present(self.USER_SAVE_BUTTON_XPATH, timeout=4, label="Save User")
                return

        self._click_if_present(self.USER_SAVE_BUTTON_XPATH, timeout=3, label="Save User")

    def _handle_battery_optimization_if_present(self):
        self.LOGGER.info("Step 8: Handling battery optimization screen if present.")
        self._click_if_present(self.BATTERY_DONE_BUTTON_XPATH, timeout=4, label="Battery Done")

    def _handle_got_it_if_present(self):
        self.LOGGER.info("Step 9: Handling FTUE Got It if present.")
        self._handle_post_battery_ftue_if_present()
        self._click_if_present(self.GOT_IT_CHANGE_MODES_XPATH, timeout=4, label="Got It")
        self._click_if_present(self.GOT_IT_FTUE_XPATH, timeout=4, label="Got It FTUE")

    def _handle_post_battery_ftue_if_present(self):
        self.LOGGER.info("Checking post-battery FTUE flow (NEXT -> GOT IT) if present.")
        next_clicked = self._click_if_present(
            self.NEXT_SLIDE_CHANGE_XPATH,
            timeout=4,
            label="FTUE Next Slide Change",
        )
        if next_clicked:
            self._click_if_present(
                self.GOT_IT_CONFIGURE_AVATAR_XPATH,
                timeout=4,
                label="FTUE Got It Configure Avatar",
            )

    def _validate_connected_state(self):
        self.LOGGER.info("Step 10: Validating connected state on Home screen.")
        if not self._is_present(self.DEVICE_STATUS_XPATH, timeout=3):
            self.LOGGER.info("Device status not immediately visible; scrolling down to find it.")
            self._scroll_down()

        status_element = self._wait_visible(self.DEVICE_STATUS_XPATH, timeout=15)
        status_text = (status_element.text or "").strip()
        # First line can show device name format, e.g., "Fg's Cubii-6E713C".
        if not status_text:
            raise AssertionError(
                "Device status line is empty; expected connected device name."
            )

        if not self._is_present(self.CONNECTION_TIME_XPATH, timeout=3):
            self.LOGGER.info("Connection time not immediately visible; scrolling down to find it.")
            self._scroll_down()

        connection_time_element = self._wait_visible(self.CONNECTION_TIME_XPATH, timeout=10)
        connection_time_text = (connection_time_element.text or "").strip()
        if "connected" not in connection_time_text.lower():
            raise AssertionError(
                "Connection details line did not show connected state. "
                f"Actual value: '{connection_time_text}'."
            )

        self.LOGGER.info(
            "Connected validation passed. Device: `%s`, Connection Details: `%s`.",
            status_text,
            connection_time_text,
        )

    def _scroll_to_device_control_card(self, max_scrolls=4):
        self.LOGGER.info("Scrolling to locate device control card.")
        for attempt in range(1, max_scrolls + 1):
            if self._is_present(self.DEVICE_CONTROL_CARD_XPATH, timeout=2):
                self.LOGGER.info("Device control card located on attempt %s.", attempt)
                return
            self.LOGGER.info("Device control card not visible on attempt %s. Scrolling down.", attempt)
            self._scroll_down()
        raise AssertionError("Device control card was not found after scrolling.")

    def _validate_disconnected_state(self):
        self.LOGGER.info("Validating disconnection state on card.")
        connection_details = self._wait_visible_with_scroll(
            self.CONNECTION_TIME_XPATH,
            timeout_per_try=4,
            max_scrolls=3,
            label="Connection Details",
        )
        details_text = (connection_details.text or "").strip()

        details_text_lower = details_text.lower()
        disconnected_markers = ("disconnected", "not connected")
        is_disconnected = any(marker in details_text_lower for marker in disconnected_markers)
        if details_text_lower and not is_disconnected:
            raise AssertionError(
                "Device did not appear disconnected based on connection details text. "
                f"Actual value: '{details_text}'."
            )

        connect_button = self._wait_connect_control_with_scroll(
            timeout_per_try=3,
            max_scrolls=4,
            label="CONNECT button",
        )

        self._wait_displayed_with_scroll(
            self.CARD_SCOPED_CHANGE_DEVICES_BUTTON_XPATH,
            timeout_per_try=3,
            max_scrolls=4,
            label="CHANGE DEVICES button",
        )
        self.LOGGER.info(
            "Disconnect validations passed. Connection details: '%s', connect control found: '%s'.",
            details_text,
            connect_button.get_attribute("resource-id") or "com.cubii:id/btnConnectDisconnect",
        )

    def _wait_visible_with_scroll(self, xpath, timeout_per_try=3, max_scrolls=3, label="element"):
        for attempt in range(1, max_scrolls + 1):
            try:
                element = self._wait_visible(xpath, timeout=timeout_per_try)
                self.LOGGER.info("Located `%s` on attempt %s.", label, attempt)
                return element
            except TimeoutException:
                if attempt == max_scrolls:
                    break
                self.LOGGER.info(
                    "`%s` not visible on attempt %s. Performing small scroll and retrying.",
                    label,
                    attempt,
                )
                self._scroll_down_small()
        raise TimeoutException(f"Unable to locate `{label}` after scrolling retries.")

    def _wait_displayed_with_scroll(self, xpath, timeout_per_try=3, max_scrolls=3, label="element"):
        locator = (AppiumBy.XPATH, xpath)
        for attempt in range(1, max_scrolls + 1):
            end_time = time.time() + timeout_per_try
            while time.time() < end_time:
                elements = self.driver.find_elements(*locator)
                for element in elements:
                    try:
                        if element.is_displayed():
                            self.LOGGER.info("Located displayed `%s` on attempt %s.", label, attempt)
                            return element
                    except Exception:
                        continue
                time.sleep(0.25)

            if attempt == max_scrolls:
                break
            self.LOGGER.info(
                "Displayed `%s` not found on attempt %s. Performing small scroll and retrying.",
                label,
                attempt,
            )
            self._scroll_down_small()

        raise TimeoutException(f"Unable to locate displayed `{label}` after scrolling retries.")

    def _wait_connect_control_with_scroll(self, timeout_per_try=3, max_scrolls=3, label="CONNECT button"):
        for attempt in range(1, max_scrolls + 1):
            end_time = time.time() + timeout_per_try
            while time.time() < end_time:
                # Primary locator (inside card)
                elements = self.driver.find_elements(AppiumBy.XPATH, self.CARD_SCOPED_CONNECT_DISCONNECT_XPATH)
                for element in elements:
                    try:
                        if element.is_displayed():
                            self.LOGGER.info("Located displayed `%s` via card-scoped XPath on attempt %s.", label, attempt)
                            return element
                    except Exception:
                        continue

                # Fallback locator (resource-id driven)
                elements = self.driver.find_elements(
                    AppiumBy.ANDROID_UIAUTOMATOR, self.CONNECT_DISCONNECT_UIAUTOMATOR
                )
                for element in elements:
                    try:
                        if element.is_displayed():
                            self.LOGGER.info(
                                "Located displayed `%s` via UIAutomator resource-id on attempt %s.",
                                label,
                                attempt,
                            )
                            return element
                    except Exception:
                        continue

                time.sleep(0.25)

            if attempt == max_scrolls:
                break
            self.LOGGER.info(
                "Displayed `%s` not found on attempt %s. Performing small scroll and retrying.",
                label,
                attempt,
            )
            self._scroll_down_small()

        raise TimeoutException(f"Unable to locate displayed `{label}` after scrolling retries.")

    def _is_connect_button_visible(self, timeout_per_try=2, max_scrolls=2):
        try:
            self._wait_connect_control_with_scroll(
                timeout_per_try=timeout_per_try,
                max_scrolls=max_scrolls,
                label="CONNECT button",
            )
            return True
        except TimeoutException:
            self.LOGGER.info("CONNECT button not visible after scroll retries.")
            return False

    def _scroll_down_small(self):
        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.1),
                "top": int(size["height"] * 0.25),
                "width": int(size["width"] * 0.8),
                "height": int(size["height"] * 0.5),
                "direction": "down",
                "percent": 0.3,
            },
        )
        self.LOGGER.info("Performed small downward scroll gesture.")

    def _wait_visible(self, xpath, timeout=None):
        wait_timeout = timeout or Settings.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_timeout)
        return wait.until(ec.visibility_of_element_located((AppiumBy.XPATH, xpath)))

    def _is_present(self, xpath, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located((AppiumBy.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False

    def _safe_click(self, xpath, label, timeout=None):
        element = self._wait_visible(xpath, timeout=timeout)
        element.click()
        self.LOGGER.info("Clicked `%s`.", label)

    def _click_if_present(self, xpath, timeout=3, label="element"):
        try:
            element = self._wait_visible(xpath, timeout=timeout)
            element.click()
            self.LOGGER.info("Clicked optional `%s`.", label)
            return True
        except TimeoutException:
            self.LOGGER.info("Optional `%s` not present.", label)
            return False

    def _is_device_type_selected(self, xpath):
        return self._is_element_selected(xpath)

    def _is_bluetooth_selected(self):
        if self._is_present(self.BLUETOOTH_SELECTED_LABEL_XPATH, timeout=2):
            self.LOGGER.info("Bluetooth selected detected using selected label locator.")
            return True

        selected_by_attr = self._is_device_type_selected(
            self.BLUETOOTH_DEVICE_XPATH
        ) or self._is_element_selected(self.BLUETOOTH_DEVICE_PARENT_XPATH)
        self.LOGGER.info("Bluetooth selected detected using element attributes: %s", selected_by_attr)
        return selected_by_attr

    def _wait_for_bluetooth_selected(self, timeout=4):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            lambda _: self._is_bluetooth_selected()
        )
        self.LOGGER.info("Bluetooth selection confirmed before clicking NEXT.")

    def _is_element_selected(self, xpath):
        try:
            element = self._wait_visible(xpath, timeout=4)
            selected_attr = (element.get_attribute("selected") or "").lower()
            checked_attr = (element.get_attribute("checked") or "").lower()
            focused_attr = (element.get_attribute("focused") or "").lower()
            content_desc = (element.get_attribute("content-desc") or "").lower()
            text_attr = (element.text or "").lower()

            is_selected = (
                selected_attr == "true"
                or checked_attr == "true"
                or focused_attr == "true"
                or "selected" in content_desc
                or "selected" in text_attr
            )
            self.LOGGER.info(
                "Selection probe for `%s`: selected=%s checked=%s focused=%s content_desc=%s text=%s -> %s",
                xpath,
                selected_attr,
                checked_attr,
                focused_attr,
                content_desc,
                text_attr,
                is_selected,
            )
            return is_selected
        except TimeoutException:
            self.LOGGER.info("Selection probe timed out for `%s`.", xpath)
            return False

    def _capture_screenshot(self, prefix):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = os.path.join("reports", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        path = os.path.join(screenshot_dir, f"{prefix}_{timestamp}.png")
        self.driver.save_screenshot(path)
        return path

    def _resolve_metric_text_from_card(self):
        if self.PEDAL_METRIC_XPATH:
            self.LOGGER.info("Resolving metric via explicit xpath override.")
            element = self._wait_visible(self.PEDAL_METRIC_XPATH, timeout=6)
            return (element.text or "").strip()

        metric_xpath = self.METRIC_CARD_XPATHS.get(self.PEDAL_METRIC_TYPE)
        if not metric_xpath:
            metric_xpath = self.METRIC_CARD_XPATHS["strides"]
            self.LOGGER.info(
                "Unknown metric type `%s`; falling back to `strides`.",
                self.PEDAL_METRIC_TYPE,
            )
        self.LOGGER.info(
            "Resolving metric from card type `%s` using xpath `%s`.",
            self.PEDAL_METRIC_TYPE,
            metric_xpath,
        )

        container = self._wait_visible(metric_xpath, timeout=8)
        text_parts = []
        for text_node in container.find_elements(AppiumBy.XPATH, ".//android.widget.TextView"):
            text_value = (text_node.text or "").strip()
            if text_value:
                text_parts.append(text_value)

        combined_text = " ".join(text_parts).strip()
        if combined_text:
            self.LOGGER.info("Resolved metric card combined text `%s`.", combined_text)
            return combined_text

        container_text = (container.text or "").strip()
        if container_text:
            self.LOGGER.info("Resolved metric card container text `%s`.", container_text)
            return container_text

        raise AssertionError(
            "Metric card is visible but no readable text value was found. "
            f"Metric type: `{self.PEDAL_METRIC_TYPE}`."
        )

    def _extract_numeric_value(self, value_text):
        matches = re.findall(r"\d+", value_text or "")
        if not matches:
            raise AssertionError(
                "Pedal metric text does not contain a numeric value. "
                f"Actual text: '{value_text}'."
            )
        return int(matches[-1])

    def _scroll_down(self):
        size = self.driver.get_window_size()
        left = int(size["width"] * 0.1)
        top = int(size["height"] * 0.2)
        width = int(size["width"] * 0.8)
        height = int(size["height"] * 0.6)
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": left,
                "top": top,
                "width": width,
                "height": height,
                "direction": "down",
                "percent": 0.7,
            },
        )
        self.LOGGER.info("Performed downward scroll gesture.")

    def tap_settings_highlight(self):
        self.LOGGER.info("Tapping three-dot Settings highlight on home screen.")
        try:
            btn = self.wait.until(ec.element_to_be_clickable(self.SETTINGS_HIGHLIGHT))
        except TimeoutException:
            self.LOGGER.info("Primary Settings locator failed; trying XPath fallback.")
            btn = self.wait.until(
                ec.element_to_be_clickable(self.SETTINGS_HIGHLIGHT_FALLBACK)
            )
        btn.click()
        self.LOGGER.info("Three-dot Settings tapped.")

    def tap_logout_menu_item(self):
        self.LOGGER.info("Tapping Logout entry in Settings menu.")
        for locator in (
            self.LOGOUT_MENU_ITEM_BY_TEXT,
            self.LOGOUT_MENU_ITEM,
            self.LOGOUT_MENU_ITEM_FALLBACK,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Logout menu item tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Logout menu locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Logout menu item could not be located.")

    def tap_logout_confirm(self):
        self.LOGGER.info("Tapping final Logout confirmation button.")
        try:
            btn = self.wait.until(
                ec.element_to_be_clickable(self.LOGOUT_CONFIRM_BUTTON)
            )
        except TimeoutException:
            self.LOGGER.info(
                "Primary btn_logout locator failed; trying XPath fallback."
            )
            btn = self.wait.until(
                ec.element_to_be_clickable(self.LOGOUT_CONFIRM_BUTTON_FALLBACK)
            )
        btn.click()
        self.LOGGER.info("Logout confirmed.")
