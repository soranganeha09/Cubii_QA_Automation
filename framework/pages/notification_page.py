import logging
import os
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage
from framework.pages.non_ble_connection import NonBleConnectionPage


class NotificationPage(BasePage):
    """In-app notifications bell icon and notifications list screen."""

    LOGGER = logging.getLogger("cubii_notification_page")

    NOTIFICATION_ICON_ACCESSIBILITY_ID = "Notifications"
    NOTIFICATION_ICON_ID = "com.cubii:id/notificationIcon"
    NOTIFICATION_ICON_XPATH = (
        '//android.widget.ImageView[@content-desc="Notifications"]'
    )
    NOTIFICATION_ICON_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/notificationIcon")'
    )
    NOTIFICATION_ICON_LOCATORS = (
        (AppiumBy.ACCESSIBILITY_ID, NOTIFICATION_ICON_ACCESSIBILITY_ID),
        (AppiumBy.ID, NOTIFICATION_ICON_ID),
        (AppiumBy.ANDROID_UIAUTOMATOR, NOTIFICATION_ICON_UIAUTOMATOR),
        (AppiumBy.XPATH, NOTIFICATION_ICON_XPATH),
    )

    NOTIFICATIONS_TITLE_TEXT = "Notifications"
    TOOLBAR_TITLE_ID = "com.cubii:id/toolbar_title"
    TOOLBAR_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title"]'
    )
    TOOLBAR_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/toolbar_title")'
    )
    TOOLBAR_TITLE_LOCATORS = (
        (AppiumBy.ID, TOOLBAR_TITLE_ID),
        (AppiumBy.ANDROID_UIAUTOMATOR, TOOLBAR_TITLE_UIAUTOMATOR),
        (AppiumBy.XPATH, TOOLBAR_TITLE_XPATH),
    )

    CLEAR_ALL_NOTIFICATION_ID = "com.cubii:id/txtClearAllNotification"
    CLEAR_ALL_NOTIFICATION_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtClearAllNotification"]'
    )
    CLEAR_ALL_NOTIFICATION_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtClearAllNotification")'
    )
    CLEAR_ALL_NOTIFICATION_LOCATORS = (
        (AppiumBy.ID, CLEAR_ALL_NOTIFICATION_ID),
        (AppiumBy.ANDROID_UIAUTOMATOR, CLEAR_ALL_NOTIFICATION_UIAUTOMATOR),
        (AppiumBy.XPATH, CLEAR_ALL_NOTIFICATION_XPATH),
    )

    CLEAR_ALL_POPUP_QUESTION_ID = "com.cubii:id/txtClearAllNotificationQue"
    CLEAR_ALL_POPUP_QUESTION_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtClearAllNotificationQue"]'
    )
    CLEAR_ALL_POPUP_QUESTION_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtClearAllNotificationQue")'
    )
    CLEAR_ALL_POPUP_QUESTION_LOCATORS = (
        (AppiumBy.ID, CLEAR_ALL_POPUP_QUESTION_ID),
        (AppiumBy.ANDROID_UIAUTOMATOR, CLEAR_ALL_POPUP_QUESTION_UIAUTOMATOR),
        (AppiumBy.XPATH, CLEAR_ALL_POPUP_QUESTION_XPATH),
    )

    POPUP_GO_BACK_TEXT = "GO BACK"
    POPUP_GO_BACK_BTN_ID = "com.cubii:id/btnNo"
    POPUP_GO_BACK_BTN_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnNo"]'
    )
    POPUP_GO_BACK_BTN_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btnNo")'
    POPUP_GO_BACK_BTN_LOCATORS = (
        (AppiumBy.ID, POPUP_GO_BACK_BTN_ID),
        (AppiumBy.ANDROID_UIAUTOMATOR, POPUP_GO_BACK_BTN_UIAUTOMATOR),
        (AppiumBy.XPATH, POPUP_GO_BACK_BTN_XPATH),
    )

    POPUP_CLEAR_ALL_CONFIRM_BTN_ID = "com.cubii:id/btnYes"
    POPUP_CLEAR_ALL_CONFIRM_BTN_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnYes"]'
    )
    POPUP_CLEAR_ALL_CONFIRM_BTN_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnYes")'
    )
    POPUP_CLEAR_ALL_CONFIRM_BTN_LOCATORS = (
        (AppiumBy.ID, POPUP_CLEAR_ALL_CONFIRM_BTN_ID),
        (AppiumBy.ANDROID_UIAUTOMATOR, POPUP_CLEAR_ALL_CONFIRM_BTN_UIAUTOMATOR),
        (AppiumBy.XPATH, POPUP_CLEAR_ALL_CONFIRM_BTN_XPATH),
    )

    EMPTY_STATE_TITLE_TEXT = "It's empty here!"

    GROUP_INVITE_TEXT_ID = "com.cubii:id/txtGroupInvite"
    GROUP_INVITE_TEXT_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtGroupInvite"]'
    )
    GROUP_INVITE_TEXT_IN_LIST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_notification"]'
        '//android.widget.TextView[@resource-id="com.cubii:id/txtGroupInvite"]'
    )
    GROUP_INVITE_TEXT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtGroupInvite")'
    )
    GROUP_INVITE_TEXT_LOCATORS = (
        (AppiumBy.ID, GROUP_INVITE_TEXT_ID),
        (AppiumBy.XPATH, GROUP_INVITE_TEXT_XPATH),
        (AppiumBy.XPATH, GROUP_INVITE_TEXT_IN_LIST_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, GROUP_INVITE_TEXT_UIAUTOMATOR),
    )

    FRIEND_REQUEST_DECLINE_BTN_ID = "com.cubii:id/imageView15"
    FRIEND_REQUEST_DECLINE_BTN_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/imageView15"]'
    )
    FRIEND_REQUEST_DECLINE_BTN_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/imageView15")'
    )
    FRIEND_REQUEST_DECLINE_BTN_LOCATORS = (
        (AppiumBy.ID, FRIEND_REQUEST_DECLINE_BTN_ID),
        (AppiumBy.XPATH, FRIEND_REQUEST_DECLINE_BTN_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, FRIEND_REQUEST_DECLINE_BTN_UIAUTOMATOR),
    )

    FRIEND_REQUEST_ACCEPT_BTN_ID = "com.cubii:id/imageView17"
    FRIEND_REQUEST_ACCEPT_BTN_TEXT = "ACCEPT"
    FRIEND_REQUEST_ACCEPT_BTN_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/imageView17"]'
    )
    FRIEND_REQUEST_ACCEPT_BTN_XPATH_TEXT = (
        '//android.widget.Button[@resource-id="com.cubii:id/imageView17" and @text="ACCEPT"]'
    )
    FRIEND_REQUEST_ACCEPT_BTN_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/imageView17")'
    )
    FRIEND_REQUEST_ACCEPT_BTN_LOCATORS = (
        (AppiumBy.ID, FRIEND_REQUEST_ACCEPT_BTN_ID),
        (AppiumBy.XPATH, FRIEND_REQUEST_ACCEPT_BTN_XPATH),
        (AppiumBy.XPATH, FRIEND_REQUEST_ACCEPT_BTN_XPATH_TEXT),
        (AppiumBy.ANDROID_UIAUTOMATOR, FRIEND_REQUEST_ACCEPT_BTN_UIAUTOMATOR),
    )

    FRIEND_REQUEST_ARROW_ID = "com.cubii:id/imgNotificationArrowGroupInvite"
    FRIEND_REQUEST_ARROW_CONTENT_DESC_SUFFIX = "sent you a friend request"
    FRIEND_REQUEST_ARROW_XPATH = (
        '//android.widget.ImageView[@resource-id="com.cubii:id/imgNotificationArrowGroupInvite"]'
    )
    FRIEND_REQUEST_ARROW_XPATH_CONTENT_DESC = (
        '//android.widget.ImageView[contains(@content-desc, "sent you a friend request")]'
    )
    FRIEND_REQUEST_ARROW_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/imgNotificationArrowGroupInvite")'
    )
    FRIEND_REQUEST_ARROW_LOCATORS = (
        (AppiumBy.ID, FRIEND_REQUEST_ARROW_ID),
        (AppiumBy.XPATH, FRIEND_REQUEST_ARROW_XPATH),
        (AppiumBy.XPATH, FRIEND_REQUEST_ARROW_XPATH_CONTENT_DESC),
        (AppiumBy.ANDROID_UIAUTOMATOR, FRIEND_REQUEST_ARROW_UIAUTOMATOR),
    )

    NAVIGATE_UP_ACCESSIBILITY_ID = "Navigate up"
    NAVIGATE_UP_CLASS = "android.widget.ImageButton"
    NAVIGATE_UP_XPATH = '//android.widget.ImageButton[@content-desc="Navigate up"]'
    NAVIGATE_UP_UIAUTOMATOR = 'new UiSelector().description("Navigate up")'
    NAVIGATE_UP_LOCATORS = (
        (AppiumBy.ACCESSIBILITY_ID, NAVIGATE_UP_ACCESSIBILITY_ID),
        (AppiumBy.XPATH, NAVIGATE_UP_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, NAVIGATE_UP_UIAUTOMATOR),
    )

    RV_NOTIFICATION_ID = "com.cubii:id/rv_notification"
    RV_NOTIFICATION_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView'
        '[@resource-id="com.cubii:id/rv_notification"]'
    )
    RV_NOTIFICATION_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/rv_notification")'
    )
    RV_NOTIFICATION_LOCATORS = (
        (AppiumBy.ID, RV_NOTIFICATION_ID),
        (AppiumBy.XPATH, RV_NOTIFICATION_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, RV_NOTIFICATION_UIAUTOMATOR),
    )

    NOTIFICATION_ROW_REL_XPATH = "./android.view.ViewGroup"
    NOTIFICATION_ROW_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView'
        '[@resource-id="com.cubii:id/rv_notification"]/android.view.ViewGroup'
    )
    NOTIFICATION_ROW_FIRST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView'
        '[@resource-id="com.cubii:id/rv_notification"]/android.view.ViewGroup[1]'
    )
    NOTIFICATION_ROW_FALLBACK_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(3)'
    )
    NOTIFICATION_CARD_LOCATORS = (
        (AppiumBy.XPATH, NOTIFICATION_ROW_XPATH),
        (AppiumBy.XPATH, NOTIFICATION_ROW_FIRST_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, NOTIFICATION_ROW_FALLBACK_UIAUTOMATOR),
    )

    NOTIFICATION_DATE_ID = "com.cubii:id/textView117"
    NOTIFICATION_DATE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView117"]'
    )
    NOTIFICATION_DATE_IN_LIST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_notification"]'
        '//android.widget.TextView[@resource-id="com.cubii:id/textView117"]'
    )
    NOTIFICATION_DATE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/textView117")'
    )
    NOTIFICATION_DATE_LOCATORS = (
        (AppiumBy.ID, NOTIFICATION_DATE_ID),
        (AppiumBy.XPATH, NOTIFICATION_DATE_XPATH),
        (AppiumBy.XPATH, NOTIFICATION_DATE_IN_LIST_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, NOTIFICATION_DATE_UIAUTOMATOR),
    )

    NOTIFICATION_DESCRIPTION_ID = "com.cubii:id/textView118"
    NOTIFICATION_DESCRIPTION_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView118"]'
    )
    NOTIFICATION_DESCRIPTION_IN_LIST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_notification"]'
        '//android.widget.TextView[@resource-id="com.cubii:id/textView118"]'
    )
    NOTIFICATION_DESCRIPTION_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/textView118")'
    )
    NOTIFICATION_DESCRIPTION_LOCATORS = (
        (AppiumBy.ID, NOTIFICATION_DESCRIPTION_ID),
        (AppiumBy.XPATH, NOTIFICATION_DESCRIPTION_XPATH),
        (AppiumBy.XPATH, NOTIFICATION_DESCRIPTION_IN_LIST_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, NOTIFICATION_DESCRIPTION_UIAUTOMATOR),
    )

    EMPTY_LIST_TEXT_ID = "com.cubii:id/emptyListText"
    EMPTY_LIST_TEXT_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/emptyListText"]'
    )
    EMPTY_LIST_TEXT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/emptyListText")'
    )
    EMPTY_LIST_TEXT_LOCATORS = (
        (AppiumBy.ID, EMPTY_LIST_TEXT_ID),
        (AppiumBy.ANDROID_UIAUTOMATOR, EMPTY_LIST_TEXT_UIAUTOMATOR),
        (AppiumBy.XPATH, EMPTY_LIST_TEXT_XPATH),
    )

    EMPTY_LIST_NORMAL_TEXT_ID = "com.cubii:id/emptyListNormalText"
    EMPTY_LIST_NORMAL_TEXT_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/emptyListNormalText"]'
    )
    EMPTY_LIST_NORMAL_TEXT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/emptyListNormalText")'
    )
    EMPTY_LIST_NORMAL_TEXT_LOCATORS = (
        (AppiumBy.ID, EMPTY_LIST_NORMAL_TEXT_ID),
        (AppiumBy.ANDROID_UIAUTOMATOR, EMPTY_LIST_NORMAL_TEXT_UIAUTOMATOR),
        (AppiumBy.XPATH, EMPTY_LIST_NORMAL_TEXT_XPATH),
    )

    def __init__(self, driver, non_ble_page: NonBleConnectionPage | None = None):
        super().__init__(driver)
        self._non_ble = non_ble_page

    def _wait_sec(self, env_key: str, default: int | None = None) -> int:
        default = default if default is not None else Settings.EXPLICIT_WAIT
        return int(os.getenv(env_key, str(default)))

    def _pause_after_tap(self, env_key: str, default: str = "0.8") -> None:
        time.sleep(float(os.getenv(env_key, default)))

    def _dismiss_navigation_blockers(self) -> None:
        if self._non_ble is None:
            return
        self._non_ble._leave_manual_workout_editor_if_blocking_navigation()
        self._non_ble._dismiss_in_progress_ftue_overlays_if_present()

    def _wait_for_visible(
        self,
        locator_triplets: tuple[tuple, ...],
        env_key: str = "CUBII_NOTIFICATION_WAIT_SEC",
        label: str = "element",
    ):
        wait_sec = self._wait_sec(env_key)
        wait = WebDriverWait(self.driver, wait_sec)
        last_exc: Exception | None = None
        for by, locator in locator_triplets:
            try:
                return wait.until(ec.visibility_of_element_located((by, locator)))
            except Exception as exc:
                last_exc = exc
                continue
        raise TimeoutException(
            f"{label} not visible within {wait_sec}s (last error: {last_exc})"
        )

    def _is_any_visible(self, locator_triplets: tuple[tuple, ...]) -> bool:
        for by, locator in locator_triplets:
            try:
                for el in self.driver.find_elements(by, locator):
                    if el.is_displayed():
                        return True
            except Exception:
                continue
        return False

    def _must_see_either(
        self,
        locator_triplets: tuple[tuple, ...],
        description: str,
        wait: WebDriverWait,
        missing: list[str],
    ) -> None:
        for by, locator in locator_triplets:
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                return
            except TimeoutException:
                continue
        missing.append(description)

    def _tap_any_clickable(
        self,
        locator_triplets: tuple[tuple, ...],
        label: str,
        *,
        env_key: str = "CUBII_NOTIFICATION_WAIT_SEC",
        pause_env_key: str = "CUBII_AFTER_NOTIFICATION_TAP_SEC",
        pause_default: str = "0.8",
    ) -> None:
        wait_sec = self._wait_sec(env_key)
        wait = WebDriverWait(self.driver, wait_sec)
        last_exc: Exception | None = None
        for by, locator in locator_triplets:
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                self._pause_after_tap(pause_env_key, pause_default)
                self.LOGGER.info("Tapped %s using (%s, %s).", label, by, locator)
                return
            except Exception as exc:
                last_exc = exc
                continue
        raise AssertionError(
            f"Could not tap {label} within {wait_sec}s (last error: {last_exc})"
        )

    def verify_notification_icon_visible(self) -> None:
        """Assert the notifications bell icon is visible on the current screen."""
        self.LOGGER.info("Notification: verify bell icon is visible.")
        self._dismiss_navigation_blockers()
        if not self._is_any_visible(self.NOTIFICATION_ICON_LOCATORS):
            raise AssertionError(
                "Notification icon (notificationIcon / content-desc Notifications) "
                "is not visible on the current screen."
            )
        self.LOGGER.info("Notification: bell icon is visible.")

    def tap_notification_icon(self) -> None:
        """Tap the notifications bell icon from the current tab."""
        self.LOGGER.info("Notification: tap bell icon.")
        self._dismiss_navigation_blockers()
        self._tap_any_clickable(
            self.NOTIFICATION_ICON_LOCATORS,
            "notification icon (notificationIcon)",
        )

    def _get_toolbar_title_text(self) -> str:
        el = self._wait_for_visible(
            self.TOOLBAR_TITLE_LOCATORS,
            env_key="CUBII_NOTIFICATION_SCREEN_WAIT_SEC",
            label="Notifications toolbar title (toolbar_title)",
        )
        return self._element_text(el)

    def is_on_notifications_screen(self) -> bool:
        """Return True when toolbar_title shows the in-app Notifications screen."""
        self._dismiss_navigation_blockers()
        wait_sec = self._wait_sec("CUBII_NOTIFICATION_SCREEN_DETECT_WAIT_SEC", default=3)
        poll = float(os.getenv("CUBII_NOTIFICATION_SCREEN_DETECT_POLL_SEC", "0.4"))
        deadline = time.time() + wait_sec
        while time.time() < deadline:
            title = self._get_visible_element_text(self.TOOLBAR_TITLE_LOCATORS)
            if title == self.NOTIFICATIONS_TITLE_TEXT:
                return True
            time.sleep(poll)
        return False

    def open_notifications_from_any_tab(self, studio_page) -> None:
        """
        Open notifications from a bottom-nav tab, or continue if already on the screen.

        Later scenarios in the same Behave run can reuse the notifications screen
        without tapping back or re-opening Studio.
        """
        if self.is_on_notifications_screen():
            self.LOGGER.info(
                "Notification: already on notifications screen; "
                "skipping Studio tab and bell icon tap."
            )
            return
        self.LOGGER.info(
            "Notification: opening from Cubii Studio tab via notification bell."
        )
        studio_page.open_cubii_studio_tab()
        self.verify_notification_icon_visible()
        self.tap_notification_icon()

    def _try_find_field_in_row(self, row, resource_id: str) -> str:
        try:
            el = row.find_element(AppiumBy.ID, resource_id)
            if el.is_displayed():
                text = self._element_text(el)
                if text:
                    return text
        except Exception:
            pass
        rel_xpath = f".//*[@resource-id='{resource_id}']"
        try:
            for el in row.find_elements(AppiumBy.XPATH, rel_xpath):
                if not el.is_displayed():
                    continue
                text = self._element_text(el)
                if text:
                    return text
        except Exception:
            pass
        return ""

    def _find_field_in_row(self, row, resource_id: str, label: str) -> str:
        text = self._try_find_field_in_row(row, resource_id)
        if text:
            return text
        raise AssertionError(
            f"Notification card is missing visible {label} ({resource_id})."
        )

    def _row_has_resource(self, row, resource_id: str) -> bool:
        return bool(self._try_find_field_in_row(row, resource_id))

    @staticmethod
    def _sender_name_from_friend_invite_text(invite_text: str) -> str:
        suffix = " sent you a friend request"
        normalized = (invite_text or "").strip()
        if suffix.lower() in normalized.lower():
            idx = normalized.lower().index(suffix.lower())
            return normalized[:idx].strip()
        return normalized

    def _friend_request_arrow_locators_for_sender(
        self, sender_name: str
    ) -> tuple[tuple, ...]:
        if not sender_name:
            return ()
        content_desc = f"{sender_name} sent you a friend request"
        return (
            (AppiumBy.ACCESSIBILITY_ID, content_desc),
            (
                AppiumBy.XPATH,
                f'//android.widget.ImageView[@content-desc="{content_desc}"]',
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().description("{content_desc}")',
            ),
        )

    def _detect_notification_card_type(self, row) -> str:
        if self._row_has_resource(row, self.GROUP_INVITE_TEXT_ID):
            return "friend_invite"
        if (
            self._row_has_resource(row, self.NOTIFICATION_DATE_ID)
            and self._row_has_resource(row, self.NOTIFICATION_DESCRIPTION_ID)
        ):
            return "standard"
        return "unknown"

    def _verify_visible_notification_card_content(self) -> None:
        """
        Assert at least one visible notification card has recognizable content.

        Supports standard cards (textView117 + textView118) and friend-invite cards
        (txtGroupInvite), using dynamic per-row detection instead of a single layout.
        """
        self._wait_for_visible(
            self.NOTIFICATION_CARD_LOCATORS,
            env_key="CUBII_NOTIFICATION_SCREEN_WAIT_SEC",
            label="notification card (ViewGroup in rv_notification)",
        )
        rows = self._collect_visible_notification_cards()
        if not rows:
            raise AssertionError(
                "No notification card (ViewGroup) found under rv_notification."
            )

        for index, row in enumerate(rows, start=1):
            card_type = self._detect_notification_card_type(row)
            if card_type == "friend_invite":
                invite_text = self._try_find_field_in_row(row, self.GROUP_INVITE_TEXT_ID)
                if invite_text:
                    self.LOGGER.info(
                        "Notification: card %s verified (friend_invite) — txtGroupInvite=%r.",
                        index,
                        invite_text[:120] if len(invite_text) > 120 else invite_text,
                    )
                    return
            if card_type == "standard":
                date = self._try_find_field_in_row(row, self.NOTIFICATION_DATE_ID)
                description = self._try_find_field_in_row(
                    row, self.NOTIFICATION_DESCRIPTION_ID
                )
                if date and description:
                    self.LOGGER.info(
                        "Notification: card %s verified (standard) — date=%r, description=%r.",
                        index,
                        date,
                        description[:120] if len(description) > 120 else description,
                    )
                    return

        invite_text = self._get_visible_friend_invite_text()
        if invite_text:
            self.LOGGER.info(
                "Notification: list content verified (friend_invite fallback) — "
                "txtGroupInvite=%r.",
                invite_text[:120] if len(invite_text) > 120 else invite_text,
            )
            return

        date = self._get_visible_element_text(self.NOTIFICATION_DATE_LOCATORS)
        description = self._get_visible_element_text(self.NOTIFICATION_DESCRIPTION_LOCATORS)
        if date and description:
            self.LOGGER.info(
                "Notification: list content verified (standard fallback) — "
                "date=%r, description=%r.",
                date,
                description[:120] if len(description) > 120 else description,
            )
            return

        raise AssertionError(
            "No recognizable notification card content found. Expected either "
            "friend invite (txtGroupInvite) or standard date/description "
            "(textView117 + textView118)."
        )

    def _get_row_date_and_description(self, row) -> tuple[str, str]:
        date = self._find_field_in_row(row, self.NOTIFICATION_DATE_ID, "date (textView117)")
        description = self._find_field_in_row(
            row, self.NOTIFICATION_DESCRIPTION_ID, "description (textView118)"
        )
        return date, description

    def _verify_first_notification_card(self) -> None:
        """Assert visible notification list content (standard or friend-invite card)."""
        self._verify_visible_notification_card_content()

    def verify_notifications_screen(self) -> None:
        """Assert toolbar_title, rv_notification, and dynamic list card content."""
        self.LOGGER.info("Notification: verify notifications screen.")
        wait_key = "CUBII_NOTIFICATION_SCREEN_WAIT_SEC"
        title = self._get_toolbar_title_text()
        if title != self.NOTIFICATIONS_TITLE_TEXT:
            raise AssertionError(
                f'Notifications toolbar title (toolbar_title) expected '
                f'"{self.NOTIFICATIONS_TITLE_TEXT}", got "{title}".'
            )
        self._wait_for_visible(
            self.RV_NOTIFICATION_LOCATORS,
            env_key=wait_key,
            label="Notifications list (rv_notification)",
        )
        self._verify_first_notification_card()
        self.LOGGER.info(
            "Notification: notifications screen verified "
            "(toolbar_title=%r, rv_notification, dynamic card content).",
            title,
        )

    def _find_notification_recycler(self):
        for by, locator in self.RV_NOTIFICATION_LOCATORS:
            try:
                el = self.driver.find_element(by, locator)
                if el.is_displayed():
                    return el
            except Exception:
                continue
        return None

    def _get_visible_element_text(
        self,
        locator_triplets: tuple[tuple, ...],
    ) -> str:
        for by, locator in locator_triplets:
            try:
                for el in self.driver.find_elements(by, locator):
                    if not el.is_displayed():
                        continue
                    text = self._element_text(el)
                    if text:
                        return text
            except Exception:
                continue
        return ""

    def _has_notification_cards_with_content(self) -> bool:
        for card in self._collect_visible_notification_cards():
            card_type = self._detect_notification_card_type(card)
            if card_type == "friend_invite":
                if self._try_find_field_in_row(card, self.GROUP_INVITE_TEXT_ID):
                    return True
            if card_type == "standard":
                date = self._try_find_field_in_row(card, self.NOTIFICATION_DATE_ID)
                description = self._try_find_field_in_row(
                    card, self.NOTIFICATION_DESCRIPTION_ID
                )
                if date and description:
                    return True
        if self._get_visible_friend_invite_text():
            return True
        date = self._get_visible_element_text(self.NOTIFICATION_DATE_LOCATORS)
        description = self._get_visible_element_text(self.NOTIFICATION_DESCRIPTION_LOCATORS)
        return bool(date and description)

    def _is_empty_state_visible(self) -> bool:
        """Return True when emptyListText (and ideally no notification cards) is on screen."""
        if self._has_notification_cards_with_content():
            return False
        empty_title = self._get_visible_element_text(self.EMPTY_LIST_TEXT_LOCATORS)
        if empty_title:
            return True
        return self._is_any_visible(self.EMPTY_LIST_TEXT_LOCATORS)

    def _detect_notifications_empty_state_available(self) -> bool:
        """
        Poll briefly: empty state is available when emptyListText is shown and
        there are no notification cards.
        """
        wait_sec = self._wait_sec("CUBII_NOTIFICATION_EMPTY_DETECT_WAIT_SEC", default=5)
        poll = float(os.getenv("CUBII_NOTIFICATION_EMPTY_DETECT_POLL_SEC", "0.5"))
        deadline = time.time() + wait_sec

        while time.time() < deadline:
            if self._has_notification_cards_with_content():
                self.LOGGER.info(
                    "Notification: notification cards found; empty state not available."
                )
                return False
            if self._is_empty_state_visible():
                self.LOGGER.info("Notification: empty state detected on screen.")
                return True
            time.sleep(poll)

        if self._has_notification_cards_with_content():
            return False
        return self._is_empty_state_visible()

    def verify_no_notifications_available(self) -> str:
        """
        Verify empty state when available.

        Returns:
            ``"verified"`` when emptyListText / emptyListNormalText are shown.
            ``"skipped"`` when the account has notifications (empty state not shown).
        """
        self.LOGGER.info("Notification: verify no notifications available (empty state).")
        title = self._get_toolbar_title_text()
        if title != self.NOTIFICATIONS_TITLE_TEXT:
            raise AssertionError(
                f'Notifications toolbar title (toolbar_title) expected '
                f'"{self.NOTIFICATIONS_TITLE_TEXT}", got "{title}".'
            )

        if not self._detect_notifications_empty_state_available():
            self.LOGGER.info(
                "Notification: skipping empty-state verification — "
                "notifications list is present or emptyListText is not shown."
            )
            return "skipped"

        wait_key = "CUBII_NOTIFICATION_EMPTY_WAIT_SEC"
        empty_title = self._get_visible_element_text(self.EMPTY_LIST_TEXT_LOCATORS)
        if not empty_title:
            self._wait_for_visible(
                self.EMPTY_LIST_TEXT_LOCATORS,
                env_key=wait_key,
                label="Notifications empty title (emptyListText)",
            )
            empty_title = self._get_visible_element_text(self.EMPTY_LIST_TEXT_LOCATORS)
        if not empty_title:
            raise AssertionError(
                "Notifications empty title (emptyListText) is not displayed."
            )

        empty_body = self._get_visible_element_text(self.EMPTY_LIST_NORMAL_TEXT_LOCATORS)
        if not empty_body:
            self._wait_for_visible(
                self.EMPTY_LIST_NORMAL_TEXT_LOCATORS,
                env_key=wait_key,
                label="Notifications empty body (emptyListNormalText)",
            )
            empty_body = self._get_visible_element_text(self.EMPTY_LIST_NORMAL_TEXT_LOCATORS)
        if not empty_body:
            raise AssertionError(
                "Notifications empty body (emptyListNormalText) is not displayed."
            )

        if self._has_notification_cards_with_content():
            raise AssertionError(
                "Expected no notifications, but notification cards with list content "
                "(standard or friend-invite) were found on the screen."
            )

        self.LOGGER.info(
            "Notification: empty state verified — emptyListText=%r; "
            "emptyListNormalText=%r.",
            empty_title,
            empty_body,
        )
        return "verified"

    @staticmethod
    def _element_text(el) -> str:
        try:
            text = (el.text or "").strip()
            if text:
                return text
        except Exception:
            pass
        try:
            return (el.get_attribute("text") or "").strip()
        except Exception:
            return ""

    def _notification_card_signature(self, date: str, description: str) -> str:
        return f"{date}|{description}"

    def _collect_visible_notification_cards(self) -> list:
        recycler = self._find_notification_recycler()
        if recycler is not None:
            try:
                cards = recycler.find_elements(AppiumBy.XPATH, self.NOTIFICATION_ROW_REL_XPATH)
                visible = [card for card in cards if card.is_displayed()]
                if visible:
                    return visible
            except Exception:
                pass

        cards: list = []
        for by, locator in self.NOTIFICATION_CARD_LOCATORS:
            try:
                for el in self.driver.find_elements(by, locator):
                    if el.is_displayed() and el not in cards:
                        cards.append(el)
            except Exception:
                continue
        return cards

    def _verify_notification_card(self, row, index: int) -> tuple[str, str]:
        if not row.is_displayed():
            raise AssertionError(f"Notification card {index} is not displayed.")
        date, description = self._get_row_date_and_description(row)
        self.LOGGER.info(
            "Verified notification card %s: date=%r, description=%r.",
            index,
            date,
            description[:120] if len(description) > 120 else description,
        )
        return date, description

    def _scroll_notifications_list(self, direction: str = "down") -> None:
        recycler = self._find_notification_recycler()
        if recycler is not None:
            try:
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "elementId": recycler.id,
                        "direction": direction,
                        "percent": float(
                            os.getenv("CUBII_NOTIFICATION_LIST_SCROLL_PERCENT", "0.75")
                        ),
                    },
                )
                return
            except Exception as exc:
                self.LOGGER.info(
                    "Notification: element scroll on rv_notification failed (%s); "
                    "using screen scroll.",
                    exc,
                )

        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.1),
                "top": int(size["height"] * 0.3),
                "width": int(size["width"] * 0.8),
                "height": int(size["height"] * 0.5),
                "direction": direction,
                "percent": float(os.getenv("CUBII_NOTIFICATION_LIST_SCROLL_PERCENT", "0.75")),
            },
        )

    def verify_all_notifications(self) -> None:
        """
        Scroll rv_notification and verify every notification card has
        date (textView117) and description (textView118).
        """
        self.LOGGER.info("Notification: verify all notifications with scroll.")
        self._wait_for_visible(
            self.RV_NOTIFICATION_LOCATORS,
            env_key="CUBII_NOTIFICATION_LIST_WAIT_SEC",
            label="Notifications list (rv_notification)",
        )

        max_scrolls = int(os.getenv("CUBII_NOTIFICATION_LIST_SCROLL_ATTEMPTS", "12"))
        pause = float(os.getenv("CUBII_NOTIFICATION_LIST_SCROLL_PAUSE_SEC", "0.5"))
        verified_signatures: set[str] = set()
        card_index = 0

        for scroll_attempt in range(max_scrolls + 1):
            cards = self._collect_visible_notification_cards()
            self.LOGGER.info(
                "Notification: scroll %s — %s card(s) visible in rv_notification.",
                scroll_attempt,
                len(cards),
            )
            new_cards_found = False
            for card in cards:
                try:
                    date, description = self._get_row_date_and_description(card)
                except AssertionError:
                    continue
                signature = self._notification_card_signature(date, description)
                if signature in verified_signatures:
                    continue
                card_index += 1
                self._verify_notification_card(card, card_index)
                verified_signatures.add(signature)
                new_cards_found = True

            if scroll_attempt >= max_scrolls:
                break

            before_scroll = len(verified_signatures)
            self._scroll_notifications_list("down")
            time.sleep(pause)

            cards_after = self._collect_visible_notification_cards()
            for card in cards_after:
                try:
                    date, description = self._get_row_date_and_description(card)
                except AssertionError:
                    continue
                signature = self._notification_card_signature(date, description)
                if signature not in verified_signatures:
                    new_cards_found = True
                    break

            if not new_cards_found and len(verified_signatures) == before_scroll:
                break

        if not verified_signatures:
            raise AssertionError(
                "No notification cards with date (textView117) and description "
                "(textView118) found under rv_notification after scrolling."
            )

        self.LOGGER.info(
            "Verified %s notification card(s) (textView117 + textView118) after scrolling.",
            len(verified_signatures),
        )

    def verify_notifications_header_clear_all_and_back(self) -> None:
        """Assert Clear All (txtClearAllNotification) and back (Navigate up) are visible in header."""
        self.LOGGER.info(
            "Notification: verify header Clear All and Navigate up back button."
        )
        wait_key = "CUBII_NOTIFICATION_HEADER_WAIT_SEC"
        clear_all = self._get_visible_element_text(self.CLEAR_ALL_NOTIFICATION_LOCATORS)
        if not clear_all:
            clear_el = self._wait_for_visible(
                self.CLEAR_ALL_NOTIFICATION_LOCATORS,
                env_key=wait_key,
                label="Clear All (txtClearAllNotification)",
            )
            clear_all = self._element_text(clear_el)
        if not clear_all:
            raise AssertionError(
                "Clear All (txtClearAllNotification) is not displayed in the notifications header."
            )

        self._wait_for_visible(
            self.NAVIGATE_UP_LOCATORS,
            env_key=wait_key,
            label="Navigate up (back button)",
        )

        self.LOGGER.info(
            "Notification: header verified — Clear All=%r; Navigate up back button visible.",
            clear_all,
        )

    def tap_clear_all_notification(self) -> None:
        """Tap Clear All (txtClearAllNotification) in the notifications header."""
        self.LOGGER.info("Notification: tap Clear All (txtClearAllNotification).")
        self._tap_any_clickable(
            self.CLEAR_ALL_NOTIFICATION_LOCATORS,
            "Clear All (txtClearAllNotification)",
            pause_env_key="CUBII_AFTER_CLEAR_ALL_TAP_SEC",
            pause_default="0.6",
        )

    def verify_clear_all_notification_popup_open(self) -> None:
        """Assert the clear-all confirmation dialog question is visible."""
        self.LOGGER.info("Notification: verify clear-all popup (txtClearAllNotificationQue).")
        popup_text = self._get_visible_element_text(self.CLEAR_ALL_POPUP_QUESTION_LOCATORS)
        if not popup_text:
            popup_el = self._wait_for_visible(
                self.CLEAR_ALL_POPUP_QUESTION_LOCATORS,
                env_key="CUBII_NOTIFICATION_CLEAR_ALL_POPUP_WAIT_SEC",
                label="Clear all popup question (txtClearAllNotificationQue)",
            )
            popup_text = self._element_text(popup_el)
        if not popup_text:
            raise AssertionError(
                "Clear all notification popup (txtClearAllNotificationQue) is not displayed."
            )
        self.LOGGER.info(
            "Notification: clear-all popup open — question=%r.",
            popup_text[:120] if len(popup_text) > 120 else popup_text,
        )

    def tap_popup_go_back(self) -> None:
        """Tap GO BACK (btnNo) on the clear-all confirmation popup."""
        self.LOGGER.info("Notification: tap GO BACK (btnNo) on clear-all popup.")
        self._tap_any_clickable(
            self.POPUP_GO_BACK_BTN_LOCATORS,
            "GO BACK (btnNo)",
            env_key="CUBII_NOTIFICATION_POPUP_BTN_WAIT_SEC",
            pause_env_key="CUBII_AFTER_POPUP_GO_BACK_TAP_SEC",
            pause_default="0.6",
        )

    def tap_popup_clear_all_confirm(self) -> None:
        """Tap confirm Clear All (btnYes) on the clear-all confirmation popup."""
        self.LOGGER.info("Notification: tap confirm Clear All (btnYes) on popup.")
        self._tap_any_clickable(
            self.POPUP_CLEAR_ALL_CONFIRM_BTN_LOCATORS,
            "Clear All confirm (btnYes)",
            env_key="CUBII_NOTIFICATION_POPUP_BTN_WAIT_SEC",
            pause_env_key="CUBII_AFTER_POPUP_CLEAR_ALL_CONFIRM_TAP_SEC",
            pause_default="1.0",
        )

    def verify_empty_state_displayed(self) -> None:
        """Assert empty state after clear all: emptyListText shows It's empty here!"""
        self.LOGGER.info("Notification: verify empty state displayed after clear all.")
        wait_key = "CUBII_NOTIFICATION_EMPTY_WAIT_SEC"
        poll = float(os.getenv("CUBII_NOTIFICATION_EMPTY_AFTER_CLEAR_POLL_SEC", "0.5"))
        wait_sec = self._wait_sec(wait_key)
        deadline = time.time() + wait_sec

        empty_title = ""
        while time.time() < deadline:
            empty_title = self._get_visible_element_text(self.EMPTY_LIST_TEXT_LOCATORS)
            if empty_title == self.EMPTY_STATE_TITLE_TEXT and not self._has_notification_cards_with_content():
                break
            time.sleep(poll)
        else:
            raise AssertionError(
                f'Empty state title (emptyListText) expected {self.EMPTY_STATE_TITLE_TEXT!r}; '
                f"got {empty_title!r} within {wait_sec}s."
            )

        empty_body = self._get_visible_element_text(self.EMPTY_LIST_NORMAL_TEXT_LOCATORS)
        if not empty_body:
            self._wait_for_visible(
                self.EMPTY_LIST_NORMAL_TEXT_LOCATORS,
                env_key=wait_key,
                label="Notifications empty body (emptyListNormalText)",
            )
            empty_body = self._get_visible_element_text(self.EMPTY_LIST_NORMAL_TEXT_LOCATORS)
        if not empty_body:
            raise AssertionError(
                "Notifications empty body (emptyListNormalText) is not displayed."
            )

        if self._has_notification_cards_with_content():
            raise AssertionError(
                "Expected empty state after clear all, but notification cards remain visible."
            )

        self.LOGGER.info(
            "Notification: empty state displayed — emptyListText=%r; emptyListNormalText=%r.",
            empty_title,
            empty_body,
        )

    def _get_visible_friend_invite_text(self) -> str:
        for by, locator in self.GROUP_INVITE_TEXT_LOCATORS:
            try:
                for el in self.driver.find_elements(by, locator):
                    if not el.is_displayed():
                        continue
                    text = self._element_text(el)
                    if text:
                        return text
            except Exception:
                continue
        return ""

    def _scroll_friend_invite_into_view(self) -> str:
        """Scroll rv_notification until txtGroupInvite invitation text is visible."""
        max_scrolls = int(
            os.getenv("CUBII_NOTIFICATION_FRIEND_INVITE_SCROLL_ATTEMPTS", "10")
        )
        pause = float(os.getenv("CUBII_NOTIFICATION_FRIEND_INVITE_SCROLL_PAUSE_SEC", "0.5"))

        for attempt in range(max_scrolls + 1):
            invite_text = self._get_visible_friend_invite_text()
            if invite_text:
                self.LOGGER.info(
                    "Notification: friend invite visible after scroll %s — %r.",
                    attempt,
                    invite_text[:120] if len(invite_text) > 120 else invite_text,
                )
                return invite_text

            if attempt < max_scrolls:
                self._scroll_notifications_list("down")
                time.sleep(pause)

        raise AssertionError(
            "Friend notification invitation (txtGroupInvite) not found in rv_notification "
            "after scrolling."
        )

    def verify_friend_notification_invitation(self) -> None:
        """Assert friend invite invitation (txtGroupInvite) with ACCEPT and DECLINE actions."""
        self.LOGGER.info("Notification: verify friend notification invitation.")
        self._dismiss_navigation_blockers()
        invite_text = self._scroll_friend_invite_into_view()
        if not invite_text:
            raise AssertionError(
                "Friend notification invitation (txtGroupInvite) has no visible text."
            )

        self._wait_for_visible(
            self.FRIEND_REQUEST_ACCEPT_BTN_LOCATORS,
            env_key="CUBII_NOTIFICATION_FRIEND_INVITE_WAIT_SEC",
            label="ACCEPT (imageView17)",
        )
        self._wait_for_visible(
            self.FRIEND_REQUEST_DECLINE_BTN_LOCATORS,
            env_key="CUBII_NOTIFICATION_FRIEND_INVITE_WAIT_SEC",
            label="DECLINE (imageView15)",
        )

        self.LOGGER.info(
            "Notification: friend invitation verified — txtGroupInvite=%r; "
            "ACCEPT and DECLINE visible.",
            invite_text[:120] if len(invite_text) > 120 else invite_text,
        )

    def tap_accept_friend_request(self) -> None:
        """Tap ACCEPT (imageView17) on the friend request notification."""
        self.LOGGER.info("Notification: tap ACCEPT on friend request (imageView17).")
        self._dismiss_navigation_blockers()
        self._scroll_friend_invite_into_view()
        self._tap_any_clickable(
            self.FRIEND_REQUEST_ACCEPT_BTN_LOCATORS,
            "ACCEPT (imageView17)",
            env_key="CUBII_NOTIFICATION_FRIEND_INVITE_WAIT_SEC",
            pause_env_key="CUBII_AFTER_FRIEND_ACCEPT_TAP_SEC",
            pause_default="1.0",
        )

    def tap_friend_request_arrow_button(self) -> None:
        """Tap the friend request arrow (dynamic content-desc or resource id)."""
        self.LOGGER.info(
            "Notification: tap friend request arrow (imgNotificationArrowGroupInvite)."
        )
        self._dismiss_navigation_blockers()
        invite_text = self._scroll_friend_invite_into_view()
        sender_name = self._sender_name_from_friend_invite_text(invite_text)
        dynamic_arrow_locators = self._friend_request_arrow_locators_for_sender(sender_name)
        arrow_locators = dynamic_arrow_locators + self.FRIEND_REQUEST_ARROW_LOCATORS

        arrow_el = None
        wait_sec = self._wait_sec("CUBII_NOTIFICATION_FRIEND_INVITE_WAIT_SEC")
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator in arrow_locators:
            try:
                arrow_el = wait.until(ec.element_to_be_clickable((by, locator)))
                break
            except Exception:
                continue
        if arrow_el is None:
            raise AssertionError(
                "Friend request arrow (imgNotificationArrowGroupInvite) is not clickable. "
                f"Tried dynamic content-desc for sender={sender_name!r} and static locators."
            )

        content_desc = ""
        try:
            content_desc = (arrow_el.get_attribute("contentDescription") or "").strip()
        except Exception:
            pass

        arrow_el.click()
        self._pause_after_tap("CUBII_AFTER_FRIEND_ARROW_TAP_SEC", "1.0")
        self.LOGGER.info(
            "Notification: tapped friend request arrow — sender=%r; content-desc=%r.",
            sender_name,
            content_desc[:120] if len(content_desc) > 120 else content_desc,
        )

    def verify_friend_request_redirection(self) -> None:
        """
        Assert redirection after tapping the friend request arrow
        (detail/sub-screen opens with Navigate up or invite UI still reachable).
        """
        self.LOGGER.info("Notification: verify friend request redirection.")
        wait_sec = self._wait_sec("CUBII_NOTIFICATION_FRIEND_REDIRECT_WAIT_SEC", default=15)
        poll = float(os.getenv("CUBII_NOTIFICATION_FRIEND_REDIRECT_POLL_SEC", "0.5"))
        deadline = time.time() + wait_sec

        while time.time() < deadline:
            if self._is_any_visible(self.NAVIGATE_UP_LOCATORS):
                self.LOGGER.info(
                    "Notification: friend request redirection verified — "
                    "Navigate up visible on redirected screen."
                )
                return
            if self._get_visible_friend_invite_text():
                self.LOGGER.info(
                    "Notification: friend request redirection verified — "
                    "friend invite (txtGroupInvite) still visible after arrow tap."
                )
                return
            if self._is_any_visible(self.FRIEND_REQUEST_ARROW_LOCATORS):
                self.LOGGER.info(
                    "Notification: friend request redirection verified — "
                    "friend request arrow still visible after tap."
                )
                return
            time.sleep(poll)

        raise AssertionError(
            f"Friend request redirection not confirmed within {wait_sec}s after arrow tap."
        )
