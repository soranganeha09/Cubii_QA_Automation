import logging
import os
import re
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage

ANDROID_KEYCODE_BACK = 4
ANDROID_KEYCODE_APP_SWITCH = 187


class ShareCubiiPage(BasePage):
    LOGGER = logging.getLogger("cubii_share_cubii_page")

    # Android share sheet — Chrome target by visible label.
    SHARE_CHROME_BY_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Chrome")',
    )
    SHARE_CHROME_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="android:id/text1" and @text="Chrome"]',
    )

    # Android share sheet — Gmail target.
    SHARE_GMAIL_BY_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Gmail")',
    )
    SHARE_GMAIL_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="android:id/text1" and @text="Gmail"]',
    )

    GMAIL_PACKAGE_HINTS = ("com.google.android.gm",)

    GMAIL_ACCOUNT_TITLE_DEFAULT = "Neha Soranga"
    GMAIL_ACCOUNT_SUBTITLE_DEFAULT = "neha.s@aubergine.co"
    GMAIL_SEARCH_NAME_DEFAULT = "Neha"

    GMAIL_SEARCH_FIELD = (
        AppiumBy.ID,
        "com.google.android.gm:id/group_picker_searchbar_edit_text",
    )
    GMAIL_SEARCH_FIELD_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.google.android.gm:id/group_picker_searchbar_edit_text")',
    )
    GMAIL_SEARCH_FIELD_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.google.android.gm:id/group_picker_searchbar_edit_text"]',
    )
    GMAIL_SEARCH_FIELD_CLASS = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    GMAIL_SEARCH_FIELD_LOCATORS = (
        GMAIL_SEARCH_FIELD,
        GMAIL_SEARCH_FIELD_UIAUTOMATOR,
        GMAIL_SEARCH_FIELD_XPATH,
        GMAIL_SEARCH_FIELD_CLASS,
    )

    GMAIL_POST_MESSAGE_ACCESSIBILITY = (AppiumBy.ACCESSIBILITY_ID, "Post message")
    GMAIL_POST_MESSAGE_BUTTON = (
        AppiumBy.ID,
        "com.google.android.gm:id/post_message_button",
    )
    GMAIL_POST_MESSAGE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.google.android.gm:id/post_message_button")',
    )
    GMAIL_POST_MESSAGE_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Post message"]',
    )
    GMAIL_POST_MESSAGE_LOCATORS = (
        GMAIL_POST_MESSAGE_ACCESSIBILITY,
        GMAIL_POST_MESSAGE_BUTTON,
        GMAIL_POST_MESSAGE_UIAUTOMATOR,
        GMAIL_POST_MESSAGE_XPATH,
    )

    # Android share sheet — Google Drive target.
    SHARE_DRIVE_BY_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Drive")',
    )
    SHARE_DRIVE_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="android:id/text1" and @text="Drive"]',
    )

    DRIVE_PACKAGE_HINTS = ("com.google.android.apps.docs",)

    DRIVE_UPLOAD_FILE_NAME_DEFAULT = "Cubii: Workout While You Work"
    DRIVE_UPLOAD_LOCATION_DEFAULT = "My Drive"
    DRIVE_UPLOAD_ACCOUNT_DEFAULT = "neha.s@aubergine.co"

    DRIVE_UPLOAD_TITLE_FIELD = (
        AppiumBy.ID,
        "com.google.android.apps.docs:id/upload_title_edittext",
    )
    DRIVE_UPLOAD_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.google.android.apps.docs:id/upload_title_edittext")',
    )
    DRIVE_UPLOAD_TITLE_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.google.android.apps.docs:id/upload_title_edittext"]',
    )
    DRIVE_UPLOAD_TITLE_CLASS = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    DRIVE_UPLOAD_TITLE_LOCATORS = (
        DRIVE_UPLOAD_TITLE_FIELD,
        DRIVE_UPLOAD_TITLE_UIAUTOMATOR,
        DRIVE_UPLOAD_TITLE_XPATH,
        DRIVE_UPLOAD_TITLE_CLASS,
    )

    DRIVE_UPLOAD_FOLDER_ACCESSIBILITY = (
        AppiumBy.ACCESSIBILITY_ID,
        "My Drive. Click to change.",
    )
    DRIVE_UPLOAD_FOLDER_FIELD = (
        AppiumBy.ID,
        "com.google.android.apps.docs:id/upload_folder_autocomplete",
    )
    DRIVE_UPLOAD_FOLDER_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.google.android.apps.docs:id/upload_folder_autocomplete")',
    )
    DRIVE_UPLOAD_FOLDER_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Spinner[@content-desc="My Drive. Click to change."]',
    )
    DRIVE_UPLOAD_FOLDER_LOCATORS = (
        DRIVE_UPLOAD_FOLDER_ACCESSIBILITY,
        DRIVE_UPLOAD_FOLDER_FIELD,
        DRIVE_UPLOAD_FOLDER_UIAUTOMATOR,
        DRIVE_UPLOAD_FOLDER_XPATH,
    )

    DRIVE_UPLOAD_ACCOUNT_FIELD = (
        AppiumBy.ID,
        "com.google.android.apps.docs:id/upload_account_autocomplete",
    )
    DRIVE_UPLOAD_ACCOUNT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.google.android.apps.docs:id/upload_account_autocomplete")',
    )
    DRIVE_UPLOAD_ACCOUNT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Spinner[@resource-id="com.google.android.apps.docs:id/upload_account_autocomplete"]',
    )
    DRIVE_UPLOAD_ACCOUNT_LOCATORS = (
        DRIVE_UPLOAD_ACCOUNT_FIELD,
        DRIVE_UPLOAD_ACCOUNT_UIAUTOMATOR,
        DRIVE_UPLOAD_ACCOUNT_XPATH,
    )

    DRIVE_UPLOAD_BUTTON = (
        AppiumBy.ID,
        "com.google.android.apps.docs:id/save_button",
    )
    DRIVE_UPLOAD_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.google.android.apps.docs:id/save_button")',
    )
    DRIVE_UPLOAD_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.google.android.apps.docs:id/save_button"]',
    )
    DRIVE_UPLOAD_BUTTON_CLASS = (AppiumBy.CLASS_NAME, "android.widget.Button")
    DRIVE_UPLOAD_BUTTON_LOCATORS = (
        DRIVE_UPLOAD_BUTTON,
        DRIVE_UPLOAD_BUTTON_UIAUTOMATOR,
        DRIVE_UPLOAD_BUTTON_XPATH,
        DRIVE_UPLOAD_BUTTON_CLASS,
    )

    # External Chrome — cubii.com page WebView container.
    CHROME_WEB_VIEW_ACCESSIBILITY_ID = (AppiumBy.ACCESSIBILITY_ID, "Web View")
    CHROME_WEB_VIEW_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Web View")',
    )
    CHROME_WEB_VIEW_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@content-desc="Web View"]',
    )
    CHROME_WEB_VIEW_PACKAGE_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@package="com.android.chrome" and @content-desc="Web View"]',
    )
    CHROME_WEB_VIEW_PACKAGE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().packageName("com.android.chrome").description("Web View")',
    )
    CHROME_WEB_VIEW_LOCATORS = (
        CHROME_WEB_VIEW_PACKAGE_UIAUTOMATOR,
        CHROME_WEB_VIEW_PACKAGE_XPATH,
        CHROME_WEB_VIEW_ACCESSIBILITY_ID,
        CHROME_WEB_VIEW_UIAUTOMATOR,
        CHROME_WEB_VIEW_XPATH,
    )
    CHROME_WEB_VIEW_BOUNDS_PATTERN = re.compile(
        r'content-desc="Web View"[^>]*bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"'
    )

    CHROME_URL_BAR_LOCATORS = (
        (AppiumBy.ID, "com.android.chrome:id/url_bar"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.android.chrome:id/url_bar")',
        ),
    )
    CHROME_PACKAGE_HINTS = (
        "com.android.chrome",
        "com.chrome.beta",
        "com.android.browser",
    )
    CUBII_URL_HOST_FRAGMENT = "cubii.com"
    CHROME_CUBII_PAGE_FRAGMENTS = (
        "Transform your day",
        "Cubii Total Body",
        "Under Desk Ellipticals",
    )

    # Only button labels indicate the modal is open (page text can still mention cookies).
    CHROME_COOKIE_OVERLAY_FRAGMENTS = (
        "ACCEPT COOKIES",
        "ALLOW ALL COOKIES",
    )

    # cubii.com cookie settings sheet — X close control inside Chrome WEBVIEW.
    CHROME_COOKIE_CLOSE_MODAL_XPATH = '//*[@id="close-modal"]'
    CHROME_COOKIE_CLOSE_MODAL_LOCATORS = (
        (AppiumBy.XPATH, CHROME_COOKIE_CLOSE_MODAL_XPATH),
        (AppiumBy.ID, "close-modal"),
        (AppiumBy.CSS_SELECTOR, "#close-modal"),
    )

    def tap_chrome_browser_from_share_sheet(self) -> None:
        """Select Chrome from the Android share / intent resolver sheet."""
        self.LOGGER.info("Selecting Chrome from share sheet.")
        for locator in (
            self.SHARE_CHROME_BY_TEXT,
            self.SHARE_CHROME_TEXT_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Chrome share target tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Chrome share target locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException(
            "Chrome browser could not be selected from the share sheet."
        )

    def _gmail_account_title(self) -> str:
        return (
            os.getenv("CUBII_SHARE_GMAIL_ACCOUNT_TITLE")
            or self.GMAIL_ACCOUNT_TITLE_DEFAULT
        ).strip()

    def _gmail_account_subtitle(self) -> str:
        return (
            os.getenv("CUBII_SHARE_GMAIL_ACCOUNT_SUBTITLE")
            or self.GMAIL_ACCOUNT_SUBTITLE_DEFAULT
        ).strip()

    def _gmail_search_name(self) -> str:
        return (
            os.getenv("CUBII_SHARE_GMAIL_SEARCH_NAME")
            or self.GMAIL_SEARCH_NAME_DEFAULT
        ).strip()

    def _tap_first_clickable(self, locators: tuple, description: str) -> None:
        for locator in locators:
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("%s tapped via `%s`.", description, locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "%s locator `%s` failed; trying next.", description, locator[1]
                )
        raise TimeoutException(f"{description} could not be tapped.")

    def tap_gmail_from_share_sheet(self) -> None:
        """Select Gmail from the Android share / intent resolver sheet."""
        self.LOGGER.info("Selecting Gmail from share sheet.")
        for locator in (self.SHARE_GMAIL_BY_TEXT, self.SHARE_GMAIL_TEXT_XPATH):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Gmail share target tapped via `%s`.", locator[1])
                time.sleep(float(os.getenv("CUBII_SHARE_GMAIL_OPEN_SEC", "1.5")))
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Gmail share target locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Gmail could not be selected from the share sheet.")

    def _gmail_account_locators(self) -> tuple:
        title = self._gmail_account_title()
        subtitle = self._gmail_account_subtitle()
        return (
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("com.google.android.gm:id/account_view_title")'
                f'.text("{title}")',
            ),
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{title}")'),
            (
                AppiumBy.XPATH,
                '//android.widget.TextView[@resource-id="com.google.android.gm:id/account_view_title"'
                f' and @text="{title}"]',
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("com.google.android.gm:id/account_view_subtitle")'
                f'.text("{subtitle}")',
            ),
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{subtitle}")'),
            (
                AppiumBy.XPATH,
                '//android.widget.TextView[@resource-id="com.google.android.gm:id/account_view_subtitle"'
                f' and @text="{subtitle}"]',
            ),
        )

    def select_aubergine_gmail_account(self) -> None:
        """Choose the configured Aubergine Gmail account on the account picker."""
        self.LOGGER.info(
            "Selecting Gmail account (title=%r, subtitle=%r).",
            self._gmail_account_title(),
            self._gmail_account_subtitle(),
        )
        self._tap_first_clickable(
            self._gmail_account_locators(),
            "Gmail Aubergine account",
        )
        time.sleep(float(os.getenv("CUBII_SHARE_GMAIL_ACCOUNT_SETTLE_SEC", "1.5")))

    def _gmail_recipient_locators(self, name: str) -> tuple:
        return (
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{name}")',
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().textContains("{name}")',
            ),
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[contains(@text,"{name}")]',
            ),
        )

    def search_and_select_gmail_recipient(self) -> None:
        """Open Gmail recipient search, type the name, and select the matching contact."""
        search_name = self._gmail_search_name()
        self.LOGGER.info("Searching Gmail recipient: %r.", search_name)

        search_field = None
        for locator in self.GMAIL_SEARCH_FIELD_LOCATORS:
            try:
                search_field = self.wait.until(
                    ec.element_to_be_clickable(locator)
                )
                self.LOGGER.info("Gmail search field found via `%s`.", locator[1])
                break
            except TimeoutException:
                continue
        if search_field is None:
            raise TimeoutException("Gmail group picker search field could not be located.")

        search_field.click()
        time.sleep(0.3)
        try:
            search_field.clear()
        except Exception:
            pass
        search_field.send_keys(search_name)
        time.sleep(float(os.getenv("CUBII_SHARE_GMAIL_SEARCH_DEBOUNCE_SEC", "1.0")))

        full_name = self._gmail_account_title()
        for label, locators in (
            (full_name, self._gmail_recipient_locators(full_name)),
            (search_name, self._gmail_recipient_locators(search_name)),
        ):
            try:
                self._tap_first_clickable(locators, f"Gmail recipient ({label})")
                time.sleep(float(os.getenv("CUBII_SHARE_GMAIL_RECIPIENT_SETTLE_SEC", "0.8")))
                return
            except TimeoutException:
                continue

        raise TimeoutException(
            f"Gmail recipient matching {search_name!r} could not be selected."
        )

    def tap_gmail_post_message_send(self) -> None:
        """Tap Gmail Post message (send) in the share compose flow."""
        self.LOGGER.info("Tapping Gmail Post message (send) button.")
        self._tap_first_clickable(
            self.GMAIL_POST_MESSAGE_LOCATORS,
            "Gmail Post message",
        )
        time.sleep(float(os.getenv("CUBII_SHARE_GMAIL_AFTER_SEND_SEC", "1.0")))

    def _drive_upload_file_name(self) -> str:
        return (
            os.getenv("CUBII_SHARE_DRIVE_FILE_NAME")
            or self.DRIVE_UPLOAD_FILE_NAME_DEFAULT
        ).strip()

    def _drive_upload_location(self) -> str:
        return (
            os.getenv("CUBII_SHARE_DRIVE_LOCATION")
            or self.DRIVE_UPLOAD_LOCATION_DEFAULT
        ).strip()

    def _drive_upload_account(self) -> str:
        return (
            os.getenv("CUBII_SHARE_DRIVE_ACCOUNT")
            or os.getenv("CUBII_SHARE_GMAIL_ACCOUNT_SUBTITLE")
            or self.DRIVE_UPLOAD_ACCOUNT_DEFAULT
        ).strip()

    def _find_visible_element(self, locators: tuple, description: str):
        for locator in locators:
            try:
                element = self.wait.until(ec.visibility_of_element_located(locator))
                if element.is_displayed():
                    self.LOGGER.info("%s found via `%s`.", description, locator[1])
                    return element
            except TimeoutException:
                self.LOGGER.info(
                    "%s locator `%s` failed; trying next.", description, locator[1]
                )
        raise TimeoutException(f"{description} could not be located.")

    @staticmethod
    def _element_display_text(element) -> str:
        parts = [
            element.text or "",
            element.get_attribute("text") or "",
            element.get_attribute("content-desc") or "",
            element.get_attribute("name") or "",
        ]
        return " ".join(part.strip() for part in parts if part and part.strip())

    def _assert_field_contains(
        self,
        locators: tuple,
        expected_fragment: str,
        field_name: str,
    ) -> str:
        element = self._find_visible_element(locators, field_name)
        actual = self._element_display_text(element)
        normalized_actual = self._normalize_visible_text(actual)
        normalized_expected = self._normalize_visible_text(expected_fragment)
        if normalized_expected not in normalized_actual:
            raise AssertionError(
                f"Drive upload {field_name}: expected {expected_fragment!r}, "
                f"got {actual!r}."
            )
        self.LOGGER.info(
            "Drive upload %s verified: %r.", field_name, expected_fragment
        )
        return actual

    def tap_drive_from_share_sheet(self) -> None:
        """Select Google Drive from the Android share / intent resolver sheet."""
        self.LOGGER.info("Selecting Drive from share sheet.")
        for locator in (self.SHARE_DRIVE_BY_TEXT, self.SHARE_DRIVE_TEXT_XPATH):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Drive share target tapped via `%s`.", locator[1])
                time.sleep(float(os.getenv("CUBII_SHARE_DRIVE_OPEN_SEC", "2.0")))
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Drive share target locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Drive could not be selected from the share sheet.")

    def verify_drive_upload_details(self) -> None:
        """Verify file name, Drive location, and account on Upload to Drive screen."""
        self.LOGGER.info("Verifying Google Drive upload details.")
        time.sleep(float(os.getenv("CUBII_SHARE_DRIVE_SCREEN_SETTLE_SEC", "1.0")))

        file_name = self._drive_upload_file_name()
        location = self._drive_upload_location()
        account = self._drive_upload_account()

        self._assert_field_contains(
            self.DRIVE_UPLOAD_TITLE_LOCATORS,
            file_name,
            "file name",
        )
        self._assert_field_contains(
            self.DRIVE_UPLOAD_FOLDER_LOCATORS,
            location,
            "drive location",
        )
        self._assert_field_contains(
            self.DRIVE_UPLOAD_ACCOUNT_LOCATORS,
            account,
            "account email",
        )

        self.LOGGER.info(
            "Drive upload details verified (file=%r, location=%r, account=%r).",
            file_name,
            location,
            account,
        )

    def tap_drive_upload_button(self) -> None:
        """Tap Upload on the Google Drive upload confirmation screen."""
        self.LOGGER.info("Tapping Drive Upload button.")
        self._tap_first_clickable(
            self.DRIVE_UPLOAD_BUTTON_LOCATORS,
            "Drive Upload",
        )
        time.sleep(float(os.getenv("CUBII_SHARE_DRIVE_AFTER_UPLOAD_SEC", "2.0")))

    @staticmethod
    def _normalize_visible_text(value: str) -> str:
        return re.sub(r"\s+", " ", (value or "").strip()).casefold()

    def _current_package(self) -> str:
        try:
            return (self.driver.current_package or "").strip()
        except Exception:
            return ""

    def _package_looks_like_chrome(self, package_name: str) -> bool:
        pkg = (package_name or "").lower()
        return any(hint in pkg for hint in self.CHROME_PACKAGE_HINTS)

    def _wait_for_chrome_foreground(self) -> str:
        wait_sec = int(os.getenv("CUBII_SHARE_CHROME_OPEN_WAIT_SEC", "25"))
        pause = float(os.getenv("CUBII_SHARE_CHROME_POLL_SEC", "0.5"))
        deadline = time.time() + wait_sec
        last_pkg = ""

        while time.time() < deadline:
            last_pkg = self._current_package()
            if self._package_looks_like_chrome(last_pkg):
                self.LOGGER.info("Chrome in foreground (package=%s).", last_pkg)
                time.sleep(float(os.getenv("CUBII_SHARE_CHROME_SETTLE_SEC", "1.5")))
                return last_pkg
            time.sleep(pause)

        raise TimeoutException(
            f"Chrome did not open within {wait_sec}s. Last package: {last_pkg!r}."
        )

    def _read_chrome_url_text(self) -> str:
        for by, locator in self.CHROME_URL_BAR_LOCATORS:
            try:
                for element in self.driver.find_elements(by, locator):
                    if not element.is_displayed():
                        continue
                    text = (
                        (element.text or "")
                        + " "
                        + (element.get_attribute("text") or "")
                    ).strip()
                    if self.CUBII_URL_HOST_FRAGMENT in text.lower():
                        return text
            except Exception:
                continue
        return ""

    def _wait_for_chrome_cubii_url(self) -> None:
        wait_sec = int(os.getenv("CUBII_SHARE_CHROME_URL_WAIT_SEC", "20"))
        pause = float(os.getenv("CUBII_SHARE_CHROME_URL_POLL_SEC", "0.5"))
        deadline = time.time() + wait_sec

        while time.time() < deadline:
            if self._read_chrome_url_text():
                self.LOGGER.info("Chrome URL bar shows cubii.com.")
                return
            time.sleep(pause)

        raise TimeoutException(
            f"cubii.com was not found in Chrome URL bar within {wait_sec}s."
        )

    def _read_cubii_url_from_webview_context(self) -> str:
        """Read cubii.com URL from Chrome WEBVIEW when the native URL bar is empty."""
        for ctx in self._list_chrome_webview_contexts():
            try:
                self.driver.switch_to.context(ctx)
                url = (getattr(self.driver, "current_url", None) or "") or ""
                if self.CUBII_URL_HOST_FRAGMENT in url.lower():
                    self.LOGGER.info("Found cubii.com in WEBVIEW context %r: %s", ctx, url)
                    return url
            except Exception as exc:
                self.LOGGER.debug("WEBVIEW URL read failed for %r: %s", ctx, exc)
            finally:
                try:
                    self.driver.switch_to.context("NATIVE_APP")
                except Exception:
                    pass
        return ""

    def _collect_chrome_webview_page_text(self) -> str:
        parts: list[str] = []
        for ctx in self._list_chrome_webview_contexts():
            try:
                self.driver.switch_to.context(ctx)
                parts.append(self.driver.page_source or "")
            except Exception as exc:
                self.LOGGER.debug("WEBVIEW page text read failed for %r: %s", ctx, exc)
            finally:
                try:
                    self.driver.switch_to.context("NATIVE_APP")
                except Exception:
                    pass
        return self._normalize_visible_text(" ".join(parts))

    def _is_cubii_homepage_content_visible(self) -> bool:
        combined = self._collect_chrome_webview_page_text()
        if not combined:
            try:
                combined = self._normalize_visible_text(self.driver.page_source or "")
            except Exception:
                combined = ""
        if not combined:
            return False
        matches = sum(
            1
            for fragment in self.CHROME_CUBII_PAGE_FRAGMENTS
            if self._normalize_visible_text(fragment) in combined
        )
        return matches >= 1

    def verify_link_opened_in_chrome_browser(self) -> None:
        """
        Assert Share Cubii opened cubii.com in external Chrome after cookie dismiss.
        Primary check: Chrome foreground + cubii.com in the URL bar (or WEBVIEW URL).
        """
        self.LOGGER.info("Verifying Share Cubii link opened in Chrome browser.")
        package = self._wait_for_chrome_foreground()

        wait_sec = int(os.getenv("CUBII_SHARE_VERIFY_URL_WAIT_SEC", "20"))
        pause = float(os.getenv("CUBII_SHARE_VERIFY_URL_POLL_SEC", "0.5"))
        deadline = time.time() + wait_sec
        url_text = ""

        while time.time() < deadline:
            url_text = self._read_chrome_url_text()
            if not url_text:
                url_text = self._read_cubii_url_from_webview_context()
            if url_text:
                break
            time.sleep(pause)

        if not url_text:
            raise AssertionError(
                f"Chrome is open (package={package!r}) but cubii.com was not found "
                f"in the address bar or WEBVIEW within {wait_sec}s."
            )

        if self._is_chrome_cookie_overlay_visible():
            raise AssertionError(
                "Chrome shows cubii.com but the cookie consent overlay is still visible."
            )

        web_rect = self._get_chrome_web_view_rect()
        if web_rect is None:
            self.LOGGER.info(
                "Chrome Web View container not exposed in native tree; "
                "cubii.com URL verification is sufficient."
            )

        if os.getenv("CUBII_SHARE_VERIFY_HOMEPAGE_CONTENT", "0") == "1":
            if not self._is_cubii_homepage_content_visible():
                raise AssertionError(
                    "Chrome opened cubii.com but expected homepage content was not found. "
                    f"Expected one of: {self.CHROME_CUBII_PAGE_FRAGMENTS!r}."
                )

        self.LOGGER.info(
            "Verified cubii.com opened in Chrome (package=%s, url=%r, web_view=%s).",
            package,
            url_text,
            web_rect,
        )

    def _get_chrome_web_view_rect(self) -> dict | None:
        """Resolve Chrome Web View bounds quickly (no long explicit waits)."""
        short_wait = int(os.getenv("CUBII_SHARE_WEBVIEW_FIND_SEC", "3"))
        for locator in self.CHROME_WEB_VIEW_LOCATORS:
            try:
                for element in self.driver.find_elements(*locator):
                    if element.is_displayed():
                        rect = element.rect
                        self.LOGGER.info(
                            "Chrome Web View rect via `%s`: %s.", locator[1], rect
                        )
                        return rect
            except Exception as exc:
                self.LOGGER.debug("Chrome Web View find `%s` failed: %s", locator[1], exc)

        try:
            WebDriverWait(self.driver, short_wait).until(
                ec.presence_of_element_located(self.CHROME_WEB_VIEW_PACKAGE_UIAUTOMATOR)
            )
            element = self.driver.find_element(*self.CHROME_WEB_VIEW_PACKAGE_UIAUTOMATOR)
            if element.is_displayed():
                rect = element.rect
                self.LOGGER.info("Chrome Web View rect via short wait: %s.", rect)
                return rect
        except TimeoutException:
            pass

        try:
            match = self.CHROME_WEB_VIEW_BOUNDS_PATTERN.search(
                self.driver.page_source or ""
            )
            if match:
                x1, y1, x2, y2 = (int(g) for g in match.groups())
                rect = {"x": x1, "y": y1, "width": x2 - x1, "height": y2 - y1}
                self.LOGGER.info("Chrome Web View rect from page_source: %s.", rect)
                return rect
        except Exception as exc:
            self.LOGGER.debug("Chrome Web View bounds parse failed: %s", exc)

        return None

    def _webview_contains_cookie_overlay_text(self) -> bool:
        try:
            contexts = self.driver.contexts or []
        except Exception:
            return False

        normalized_fragments = [
            self._normalize_visible_text(fragment)
            for fragment in self.CHROME_COOKIE_OVERLAY_FRAGMENTS
        ]

        for ctx in contexts:
            if "WEBVIEW" not in (ctx or "").upper():
                continue
            try:
                self.driver.switch_to.context(ctx)
                source = self._normalize_visible_text(self.driver.page_source or "")
                if any(fragment in source for fragment in normalized_fragments):
                    return True
            except Exception as exc:
                self.LOGGER.debug("Chrome WEBVIEW overlay read failed for %r: %s", ctx, exc)
            finally:
                try:
                    self.driver.switch_to.context("NATIVE_APP")
                except Exception:
                    pass
        return False

    def _is_chrome_cookie_overlay_visible(self) -> bool:
        for fragment in self.CHROME_COOKIE_OVERLAY_FRAGMENTS:
            try:
                ui = (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().textContains("{fragment}")',
                )
                for element in self.driver.find_elements(*ui):
                    if element.is_displayed():
                        return True
            except Exception:
                continue

        try:
            native_source = self._normalize_visible_text(self.driver.page_source or "")
            if any(
                self._normalize_visible_text(fragment) in native_source
                for fragment in self.CHROME_COOKIE_OVERLAY_FRAGMENTS
            ):
                return True
        except Exception:
            pass

        return self._webview_contains_cookie_overlay_text()

    def _cookie_overlay_dismissed_after_action(self) -> bool:
        time.sleep(float(os.getenv("CUBII_SHARE_OVERLAY_DISMISS_POLL_SEC", "0.5")))
        return not self._is_chrome_cookie_overlay_visible()

    def _chrome_cookie_cancel_tap_points(
        self, width: int, height: int, web_rect: dict | None
    ) -> list[tuple[int, int, str]]:
        """X icon sits top-right of the cookie sheet (just below Chrome toolbar)."""
        tap_points: list[tuple[int, int, str]] = []
        if web_rect:
            wx, wy, ww, wh = (
                int(web_rect["x"]),
                int(web_rect["y"]),
                int(web_rect["width"]),
                int(web_rect["height"]),
            )
            for frac_y, label in (
                (0.08, "webview-x-8"),
                (0.10, "webview-x-10"),
                (0.12, "webview-x-12"),
                (0.15, "webview-x-15"),
            ):
                tap_points.append(
                    (int(wx + ww * 0.93), int(wy + wh * frac_y), label)
                )

        toolbar_bottom = int(height * 0.11)
        for y_offset, label in (
            (24, "below-toolbar-24"),
            (56, "below-toolbar-56"),
            (88, "below-toolbar-88"),
            (120, "below-toolbar-120"),
        ):
            tap_points.append(
                (int(width * 0.93), toolbar_bottom + y_offset, label)
            )

        tap_points.extend(
            (
                (int(width * 0.93), int(height * 0.17), "screen-17pct"),
                (int(width * 0.90), int(height * 0.19), "screen-19pct"),
                (int(width * 0.88), int(height * 0.21), "screen-21pct"),
            )
        )
        return tap_points

    def _tap_chrome_cookie_cancel_coordinate_grid(self) -> bool:
        """Tap the cookie-sheet X (top-right of Chrome Web View / screen)."""
        pause = float(os.getenv("CUBII_SHARE_AFTER_CANCEL_SEC", "1.0"))
        window = self.driver.get_window_size()
        width = int(window["width"])
        height = int(window["height"])
        web_rect = self._get_chrome_web_view_rect()

        for x, y, label in self._chrome_cookie_cancel_tap_points(
            width, height, web_rect
        ):
            try:
                self.driver.execute_script("mobile: clickGesture", {"x": x, "y": y})
                self.LOGGER.info(
                    "Chrome cookie cancel coordinate tap (%s) at (%s, %s).",
                    label,
                    x,
                    y,
                )
                time.sleep(pause)
                if self._cookie_overlay_dismissed_after_action():
                    self.LOGGER.info("Cookie overlay dismissed after %s tap.", label)
                    return True
            except Exception as exc:
                self.LOGGER.debug("Chrome cancel tap %s failed: %s", label, exc)
        return False

    def _list_chrome_webview_contexts(self) -> list[str]:
        try:
            return [
                ctx
                for ctx in (self.driver.contexts or [])
                if "WEBVIEW" in (ctx or "").upper()
            ]
        except Exception as exc:
            self.LOGGER.debug("Could not list WEBVIEW contexts: %s", exc)
            return []

    def _tap_close_modal_in_webview_context(self, ctx: str, pause: float) -> bool:
        """Tap ``#close-modal`` in a single Chrome WEBVIEW context."""
        element_wait = int(os.getenv("CUBII_SHARE_CLOSE_MODAL_WAIT_SEC", "5"))
        try:
            self.driver.switch_to.context(ctx)
            for locator in self.CHROME_COOKIE_CLOSE_MODAL_LOCATORS:
                try:
                    element = WebDriverWait(self.driver, element_wait).until(
                        ec.element_to_be_clickable(locator)
                    )
                    element.click()
                    self.LOGGER.info(
                        "Chrome cookie cancel tapped `#close-modal` via `%s` in %r.",
                        locator[1],
                        ctx,
                    )
                    time.sleep(pause)
                    return self._cookie_overlay_dismissed_after_action()
                except TimeoutException:
                    self.LOGGER.debug(
                        "close-modal locator `%s` not ready in %r.", locator[1], ctx
                    )
                except Exception as exc:
                    self.LOGGER.debug(
                        "close-modal click via `%s` in %r failed: %s",
                        locator[1],
                        ctx,
                        exc,
                    )
        except Exception as exc:
            self.LOGGER.debug("WEBVIEW context %r switch failed: %s", ctx, exc)
        finally:
            try:
                self.driver.switch_to.context("NATIVE_APP")
            except Exception:
                pass
        return False

    def _tap_chrome_cookie_close_modal(self) -> bool:
        """Tap cubii.com cookie sheet X (`#close-modal`) inside Chrome WEBVIEW."""
        pause = float(os.getenv("CUBII_SHARE_AFTER_CANCEL_SEC", "1.0"))
        webview_wait = int(os.getenv("CUBII_SHARE_WEBVIEW_CONTEXT_WAIT_SEC", "20"))
        poll = float(os.getenv("CUBII_SHARE_WEBVIEW_CONTEXT_POLL_SEC", "0.5"))
        deadline = time.time() + webview_wait

        while time.time() < deadline:
            contexts = self._list_chrome_webview_contexts()
            if contexts:
                self.LOGGER.info("Chrome WEBVIEW contexts: %s", contexts)
            for ctx in contexts:
                if self._tap_close_modal_in_webview_context(ctx, pause):
                    return True
            time.sleep(poll)

        self.LOGGER.info(
            "No clickable `#close-modal` in WEBVIEW within %ss.", webview_wait
        )
        return False

    def _tap_chrome_cookie_cancel_in_webview_context(self) -> bool:
        pause = float(os.getenv("CUBII_SHARE_AFTER_CANCEL_SEC", "1.0"))
        webview_wait = int(os.getenv("CUBII_SHARE_WEBVIEW_CONTEXT_WAIT_SEC", "20"))
        deadline = time.time() + webview_wait

        xpaths = (
            self.CHROME_COOKIE_CLOSE_MODAL_XPATH,
            '//*[contains(@class,"close") or contains(@id,"close") or contains(@class,"Close")]',
            '//*[@aria-label="Close" or @aria-label="close" or contains(@aria-label,"Close")]',
            '//*[contains(@class,"dismiss") or contains(@id,"dismiss")]',
            "//button[contains(.,'×') or contains(.,'✕')]",
            "//*[contains(@onclick,'close') or contains(@class,'modal-close')]",
        )

        while time.time() < deadline:
            for ctx in self._list_chrome_webview_contexts():
                try:
                    self.driver.switch_to.context(ctx)
                    for xpath in xpaths:
                        for element in self.driver.find_elements(
                            AppiumBy.XPATH, xpath
                        ):
                            try:
                                if element.is_displayed():
                                    element.click()
                                    self.LOGGER.info(
                                        "Chrome cookie cancel via WEBVIEW %r (%s).",
                                        xpath,
                                        ctx,
                                    )
                                    time.sleep(pause)
                                    if self._cookie_overlay_dismissed_after_action():
                                        return True
                            except Exception:
                                continue
                except Exception as exc:
                    self.LOGGER.debug("WEBVIEW context %r cancel failed: %s", ctx, exc)
                finally:
                    try:
                        self.driver.switch_to.context("NATIVE_APP")
                    except Exception:
                        pass

            time.sleep(0.5)

        try:
            self.driver.switch_to.context("NATIVE_APP")
        except Exception:
            pass
        return False

    def tap_chrome_cookie_cancel_option(self) -> None:
        """Dismiss cubii.com cookie consent X in external Chrome."""
        self.LOGGER.info("Tapping cookie cancel (X) on Chrome cubii.com page.")
        self._wait_for_chrome_foreground()
        self._wait_for_chrome_cubii_url()
        time.sleep(float(os.getenv("CUBII_SHARE_CHROME_PAGE_LOAD_SEC", "2.0")))

        if not self._is_chrome_cookie_overlay_visible():
            self.LOGGER.info("Cookie overlay not detected; skipping cancel tap.")
            return

        # Primary: cubii.com cookie sheet close X in Chrome WEBVIEW (`#close-modal`).
        if self._tap_chrome_cookie_close_modal():
            return
        if self._tap_chrome_cookie_cancel_in_webview_context():
            return
        if self._tap_chrome_cookie_cancel_coordinate_grid():
            return

        if os.getenv("CUBII_SHARE_ALLOW_ACCEPT_COOKIES_FALLBACK", "1") == "1":
            if self._tap_accept_cookies_fallback():
                return

        raise TimeoutException(
            "Chrome cookie cancel (X) could not be tapped; overlay still visible."
        )

    def _tap_accept_cookies_fallback(self) -> bool:
        """Fallback when X is not reachable — tap ACCEPT COOKIES in WEBVIEW or by coordinate."""
        pause = float(os.getenv("CUBII_SHARE_AFTER_CANCEL_SEC", "1.0"))
        window = self.driver.get_window_size()
        x = int(window["width"] * 0.5)
        y = int(window["height"] * 0.82)

        for xpath in (
            '//*[contains(text(),"ACCEPT COOKIES") or contains(., "ACCEPT COOKIES")]',
            "//button[contains(translate(., 'accept', 'ACCEPT'), 'ACCEPT')]",
        ):
            try:
                for ctx in self.driver.contexts or []:
                    if "WEBVIEW" not in (ctx or "").upper():
                        continue
                    try:
                        self.driver.switch_to.context(ctx)
                        for element in self.driver.find_elements(
                            AppiumBy.XPATH, xpath
                        ):
                            if element.is_displayed():
                                element.click()
                                self.LOGGER.info(
                                    "Chrome cookie overlay dismissed via ACCEPT COOKIES (%s).",
                                    ctx,
                                )
                                time.sleep(pause)
                                if self._cookie_overlay_dismissed_after_action():
                                    return True
                    except Exception:
                        continue
                    finally:
                        try:
                            self.driver.switch_to.context("NATIVE_APP")
                        except Exception:
                            pass
            except Exception:
                continue

        try:
            self.driver.switch_to.context("NATIVE_APP")
        except Exception:
            pass

        try:
            self.driver.execute_script("mobile: clickGesture", {"x": x, "y": y})
            self.LOGGER.info("Chrome ACCEPT COOKIES coordinate tap at (%s, %s).", x, y)
            time.sleep(pause)
            return self._cookie_overlay_dismissed_after_action()
        except Exception as exc:
            self.LOGGER.debug("ACCEPT COOKIES coordinate tap failed: %s", exc)
            return False

    def _cubii_app_package(self) -> str:
        return (os.getenv("APP_PACKAGE") or Settings.APP_PACKAGE or "com.cubii").strip()

    def _open_recent_apps_switcher(self) -> None:
        """Open Android Recents / app switcher (Chrome card + Cubii card)."""
        self.LOGGER.info("Opening recent apps switcher.")
        try:
            self.driver.press_keycode(ANDROID_KEYCODE_APP_SWITCH)
        except Exception as exc:
            self.LOGGER.warning("APP_SWITCH key failed: %s", exc)
        time.sleep(float(os.getenv("CUBII_SHARE_RECENTS_SETTLE_SEC", "1.2")))

    def _cubii_recents_card_locators(self, cubii_pkg: str) -> tuple:
        return (
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().packageName("{cubii_pkg}")',
            ),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cubii")'),
            (AppiumBy.XPATH, '//android.widget.TextView[@text="Cubii"]'),
            (
                AppiumBy.XPATH,
                f'//*[contains(@package,"{cubii_pkg}") and @clickable="true"]',
            ),
            (
                AppiumBy.XPATH,
                f'//android.widget.FrameLayout[contains(@package,"{cubii_pkg}")]',
            ),
        )

    def _tap_cubii_card_in_recent_apps(self, cubii_pkg: str) -> bool:
        """
        Select the Cubii app card from Recents (left card in split overview).
        Falls back to a coordinate tap on the left preview pane.
        """
        pause = float(os.getenv("CUBII_SHARE_RECENTS_AFTER_TAP_SEC", "0.8"))

        for locator in self._cubii_recents_card_locators(cubii_pkg):
            try:
                for element in self.driver.find_elements(*locator):
                    if not element.is_displayed():
                        continue
                    element.click()
                    self.LOGGER.info(
                        "Tapped Cubii card in Recents via `%s`.", locator[1]
                    )
                    time.sleep(pause)
                    if self._current_package() == cubii_pkg:
                        return True
            except Exception as exc:
                self.LOGGER.debug(
                    "Recents Cubii locator `%s` failed: %s", locator[1], exc
                )

        window = self.driver.get_window_size()
        width = int(window["width"])
        height = int(window["height"])
        x = int(width * float(os.getenv("CUBII_SHARE_RECENTS_TAP_X_FRAC", "0.28")))
        y = int(height * float(os.getenv("CUBII_SHARE_RECENTS_TAP_Y_FRAC", "0.42")))
        try:
            self.driver.execute_script("mobile: clickGesture", {"x": x, "y": y})
            self.LOGGER.info(
                "Tapped Cubii Recents card by coordinate at (%s, %s).", x, y
            )
            time.sleep(pause)
            return self._current_package() == cubii_pkg
        except Exception as exc:
            self.LOGGER.debug("Recents coordinate tap failed: %s", exc)
            return False

    def _return_to_application_via_back_or_activate(self, cubii_pkg: str) -> None:
        """Fallback when Recents switcher does not restore Cubii."""
        back_attempts = int(os.getenv("CUBII_SHARE_BROWSER_BACK_ATTEMPTS", "2"))
        pause = float(os.getenv("CUBII_SHARE_BROWSER_BACK_PAUSE_SEC", "0.6"))

        for attempt in range(back_attempts):
            if self._current_package() == cubii_pkg:
                return
            try:
                self.driver.press_keycode(ANDROID_KEYCODE_BACK)
                self.LOGGER.info(
                    "Pressed BACK (%s/%s) to leave Chrome.", attempt + 1, back_attempts
                )
            except Exception as exc:
                self.LOGGER.warning("BACK key failed: %s", exc)
            time.sleep(pause)

        if self._current_package() != cubii_pkg:
            self.driver.activate_app(cubii_pkg)
            self.LOGGER.info("Activated Cubii via activate_app(%s).", cubii_pkg)
            time.sleep(pause)

    def return_to_application(self) -> None:
        """Return to Cubii via Recents app switcher (tap Cubii card), then verify."""
        cubii_pkg = self._cubii_app_package()
        self.LOGGER.info("Returning to Cubii app from Chrome (package=%s).", cubii_pkg)

        if self._current_package() == cubii_pkg:
            self.LOGGER.info("Already on Cubii; skip return navigation.")
            return

        self._open_recent_apps_switcher()
        if self._tap_cubii_card_in_recent_apps(cubii_pkg):
            self.LOGGER.info("Returned to Cubii via recent apps switcher.")
        else:
            self.LOGGER.info(
                "Recents card tap did not foreground Cubii; trying BACK / activate_app."
            )
            self._return_to_application_via_back_or_activate(cubii_pkg)

        try:
            self.driver.switch_to.context("NATIVE_APP")
        except Exception:
            pass

        if self._current_package() != cubii_pkg:
            raise AssertionError(
                f"Expected Cubii foreground ({cubii_pkg!r}) after leaving Chrome, "
                f"got {self._current_package()!r}."
            )

        time.sleep(float(os.getenv("CUBII_SHARE_AFTER_RETURN_SEC", "0.8")))
        self.LOGGER.info("Returned to Cubii application from Chrome.")
