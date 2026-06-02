import logging
import os

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage


class PreviewProfilePage(BasePage):
    LOGGER = logging.getLogger("cubii_preview_profile_page")

    PREVIEW_PROFILE_SCREEN_TITLE = "Preview Profile"

    TOOLBAR_TITLE_ID = "com.cubii:id/toolbar_title"
    TOOLBAR_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title"]'
    )
    TOOLBAR_TITLE_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/toolbar_title")'

    USER_NAME_ID = "com.cubii:id/textView22"
    USER_NAME_XPATH = '//android.widget.TextView[@resource-id="com.cubii:id/textView22"]'
    USER_NAME_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/textView22")'

    BIO_TITLE_ID = "com.cubii:id/txtIgnoreBioTitle"
    BIO_TITLE_XPATH = '//android.widget.TextView[@resource-id="com.cubii:id/txtIgnoreBioTitle"]'
    BIO_TITLE_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtIgnoreBioTitle")'

    BIO_TEXT_ID = "com.cubii:id/txtBio"
    BIO_TEXT_XPATH = '//android.widget.TextView[@resource-id="com.cubii:id/txtBio"]'
    BIO_TEXT_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtBio")'

    FOCUS_TITLE_ID = "com.cubii:id/txtIgnoreFocusTitle"
    FOCUS_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtIgnoreFocusTitle"]'
    )
    FOCUS_TITLE_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtIgnoreFocusTitle")'

    FOCUS_TEXT_ID = "com.cubii:id/txtFocus"
    FOCUS_TEXT_XPATH = '//android.widget.TextView[@resource-id="com.cubii:id/txtFocus"]'
    FOCUS_TEXT_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtFocus")'

    INTERESTS_TITLE_ID = "com.cubii:id/txtIgnoreInterestTitle"
    INTERESTS_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtIgnoreInterestTitle"]'
    )
    INTERESTS_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtIgnoreInterestTitle")'
    )

    INTERESTS_TEXT_ID = "com.cubii:id/txtInterest"
    INTERESTS_TEXT_XPATH = '//android.widget.TextView[@resource-id="com.cubii:id/txtInterest"]'
    INTERESTS_TEXT_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtInterest")'

    BADGES_TITLE_ID = "com.cubii:id/txtIgnoreBadgesTitle"
    BADGES_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtIgnoreBadgesTitle"]'
    )
    BADGES_TITLE_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtIgnoreBadgesTitle")'

    BADGES_GRID_ID = "com.cubii:id/rvBadges"
    BADGES_GRID_XPATH = '//android.widget.GridView[@resource-id="com.cubii:id/rvBadges"]'
    BADGES_GRID_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/rvBadges")'

    NO_BADGES_TEXT_ID = "com.cubii:id/txtNoBadgesEarnedText"
    NO_BADGES_TEXT_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtNoBadgesEarnedText"]'
    )
    NO_BADGES_TEXT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtNoBadgesEarnedText")'
    )

    @staticmethod
    def _locator_triplets(resource_id: str, xpath: str, uiautomator: str) -> tuple[tuple, ...]:
        return (
            (AppiumBy.ID, resource_id),
            (AppiumBy.ANDROID_UIAUTOMATOR, uiautomator),
            (AppiumBy.XPATH, xpath),
        )

    @staticmethod
    def _is_visible_one_of(wait: WebDriverWait, locator_triplets: tuple[tuple, ...]) -> bool:
        for by, locator in locator_triplets:
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                return True
            except Exception:
                continue
        return False

    def _assert_visible_one_of(
        self, wait: WebDriverWait, locator_triplets: tuple[tuple, ...], description: str
    ) -> None:
        if not self._is_visible_one_of(wait, locator_triplets):
            raise AssertionError(f"Preview Profile: {description} not visible.")

    def _read_visible_text_one_of(self, locator_triplets: tuple[tuple, ...]) -> str | None:
        for by, locator in locator_triplets:
            try:
                for el in self.driver.find_elements(by, locator):
                    if not el.is_displayed():
                        continue
                    text = (el.text or el.get_attribute("text") or "").strip()
                    if text:
                        return text
            except Exception:
                continue
        return None

    def _verify_text_section_if_available(
        self,
        wait_opt: WebDriverWait,
        section_label: str,
        title_triplets: tuple[tuple, ...],
        value_triplets: tuple[tuple, ...],
    ) -> bool:
        title_visible = self._is_visible_one_of(wait_opt, title_triplets)
        value_visible = self._is_visible_one_of(wait_opt, value_triplets)
        if not title_visible and not value_visible:
            self.LOGGER.info("Preview Profile: %s not present; skipped.", section_label)
            return False
        if title_visible and not value_visible:
            raise AssertionError(
                f"Preview Profile: {section_label} title visible but value field missing."
            )
        if value_visible and not title_visible:
            raise AssertionError(
                f"Preview Profile: {section_label} value visible but title missing."
            )
        self._assert_visible_one_of(wait_opt, title_triplets, f"{section_label} title")
        self._assert_visible_one_of(wait_opt, value_triplets, f"{section_label} value")
        value_text = self._read_visible_text_one_of(value_triplets)
        if not value_text:
            raise AssertionError(f"Preview Profile: {section_label} value is empty.")
        self.LOGGER.info(
            "Preview Profile: %s verified (value sample=%r).",
            section_label,
            value_text[:120],
        )
        return True

    def verify_preview_profile_screen_visible(self) -> None:
        self.LOGGER.info("Verifying Preview Profile screen toolbar title.")
        title_triplets = self._locator_triplets(
            self.TOOLBAR_TITLE_ID,
            self.TOOLBAR_TITLE_XPATH,
            self.TOOLBAR_TITLE_UIAUTOMATOR,
        )
        last_err = None
        for by, locator in title_triplets:
            try:
                element = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT).until(
                    ec.visibility_of_element_located((by, locator))
                )
                title = (element.text or "").strip()
                if title and title != self.PREVIEW_PROFILE_SCREEN_TITLE:
                    raise AssertionError(
                        f"Preview Profile toolbar title mismatch: "
                        f"expected {self.PREVIEW_PROFILE_SCREEN_TITLE!r}, got {title!r}."
                    )
                if title:
                    self.LOGGER.info("Preview Profile screen verified: %r.", title)
                    return
                self.LOGGER.info("Preview Profile toolbar title element visible.")
                return
            except (TimeoutException, AssertionError) as exc:
                last_err = exc
                continue
        raise AssertionError(
            "Preview Profile screen not verified. Expected toolbar title "
            f"{self.PREVIEW_PROFILE_SCREEN_TITLE!r} (`toolbar_title`). Last error: {last_err!r}"
        )

    def verify_preview_profile_details(self) -> None:
        """Verify name and optional Bio, Focus, Interests, and Badges sections."""
        wait_sec = int(
            os.getenv("CUBII_PREVIEW_PROFILE_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )
        optional_sec = max(
            2,
            int(os.getenv("CUBII_PREVIEW_PROFILE_OPTIONAL_SECTION_WAIT_SEC", "3")),
        )
        wait = WebDriverWait(self.driver, wait_sec)
        wait_opt = WebDriverWait(self.driver, optional_sec)

        name_triplets = self._locator_triplets(
            self.USER_NAME_ID,
            self.USER_NAME_XPATH,
            self.USER_NAME_UIAUTOMATOR,
        )
        self._assert_visible_one_of(wait, name_triplets, "user name (textView22)")
        name_text = self._read_visible_text_one_of(name_triplets)
        if not name_text:
            raise AssertionError("Preview Profile: user name (`textView22`) is empty.")
        self.LOGGER.info("Preview Profile: name verified (%r).", name_text)

        verified: list[str] = ["Name"]

        if self._verify_text_section_if_available(
            wait_opt,
            "Bio",
            self._locator_triplets(
                self.BIO_TITLE_ID, self.BIO_TITLE_XPATH, self.BIO_TITLE_UIAUTOMATOR
            ),
            self._locator_triplets(
                self.BIO_TEXT_ID, self.BIO_TEXT_XPATH, self.BIO_TEXT_UIAUTOMATOR
            ),
        ):
            verified.append("Bio")

        if self._verify_text_section_if_available(
            wait_opt,
            "Focus",
            self._locator_triplets(
                self.FOCUS_TITLE_ID, self.FOCUS_TITLE_XPATH, self.FOCUS_TITLE_UIAUTOMATOR
            ),
            self._locator_triplets(
                self.FOCUS_TEXT_ID, self.FOCUS_TEXT_XPATH, self.FOCUS_TEXT_UIAUTOMATOR
            ),
        ):
            verified.append("Focus")

        if self._verify_text_section_if_available(
            wait_opt,
            "Interests",
            self._locator_triplets(
                self.INTERESTS_TITLE_ID,
                self.INTERESTS_TITLE_XPATH,
                self.INTERESTS_TITLE_UIAUTOMATOR,
            ),
            self._locator_triplets(
                self.INTERESTS_TEXT_ID,
                self.INTERESTS_TEXT_XPATH,
                self.INTERESTS_TEXT_UIAUTOMATOR,
            ),
        ):
            verified.append("Interests")

        badges_title_triplets = self._locator_triplets(
            self.BADGES_TITLE_ID,
            self.BADGES_TITLE_XPATH,
            self.BADGES_TITLE_UIAUTOMATOR,
        )
        if self._is_visible_one_of(wait_opt, badges_title_triplets):
            self._assert_visible_one_of(wait_opt, badges_title_triplets, "Badges title")
            badges_grid_triplets = self._locator_triplets(
                self.BADGES_GRID_ID,
                self.BADGES_GRID_XPATH,
                self.BADGES_GRID_UIAUTOMATOR,
            )
            no_badges_triplets = self._locator_triplets(
                self.NO_BADGES_TEXT_ID,
                self.NO_BADGES_TEXT_XPATH,
                self.NO_BADGES_TEXT_UIAUTOMATOR,
            )
            has_badges = self._is_visible_one_of(wait_opt, badges_grid_triplets)
            has_no_badges_msg = self._is_visible_one_of(wait_opt, no_badges_triplets)
            if has_badges:
                self._assert_visible_one_of(wait_opt, badges_grid_triplets, "Badges grid")
                self.LOGGER.info("Preview Profile: Badges grid verified.")
            elif has_no_badges_msg:
                no_badges_text = self._read_visible_text_one_of(no_badges_triplets)
                if not no_badges_text:
                    raise AssertionError(
                        "Preview Profile: no-badges message (`txtNoBadgesEarnedText`) is empty."
                    )
                self.LOGGER.info(
                    "Preview Profile: no badges message verified (%r).", no_badges_text
                )
            else:
                raise AssertionError(
                    "Preview Profile: Badges section visible but neither badge grid "
                    "(`rvBadges`) nor no-badges message (`txtNoBadgesEarnedText`) found."
                )
            verified.append("Badges")

        self.LOGGER.info(
            "Step Passed: Preview Profile details verified. Sections: %s.",
            ", ".join(verified),
        )
