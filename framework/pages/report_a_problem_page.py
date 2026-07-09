import logging
import os
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage


class ReportAProblemPage(BasePage):
    LOGGER = logging.getLogger("cubii_report_a_problem_page")

    SCREEN_HEADER_ID = "com.cubii:id/textView48"
    SCREEN_HEADER = (AppiumBy.ID, SCREEN_HEADER_ID)
    SCREEN_HEADER_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/textView48")',
    )
    SCREEN_HEADER_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/textView48"]',
    )

    SUBJECT_FIELD_ID = "com.cubii:id/et_subject"
    SUBJECT_FIELD = (AppiumBy.ID, SUBJECT_FIELD_ID)
    SUBJECT_FIELD_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/et_subject")',
    )
    SUBJECT_FIELD_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/et_subject"]',
    )
    SUBJECT_FIELD_HINT = "Subject"
    DESCRIPTION_FIELD_HINT = "Description"

    DESCRIPTION_FIELD_ID = "com.cubii:id/et_description"
    DESCRIPTION_FIELD = (AppiumBy.ID, DESCRIPTION_FIELD_ID)
    DESCRIPTION_FIELD_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/et_description")',
    )
    DESCRIPTION_FIELD_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/et_description"]',
    )

    DESCRIPTION_LABEL_ID = "com.cubii:id/textView49"
    DESCRIPTION_LABEL = (AppiumBy.ID, DESCRIPTION_LABEL_ID)
    DESCRIPTION_LABEL_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/textView49")',
    )
    DESCRIPTION_LABEL_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/textView49"]',
    )

    SEND_BUTTON_ID = "com.cubii:id/btn_send"
    SEND_BUTTON = (AppiumBy.ID, SEND_BUTTON_ID)
    SEND_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/btn_send")',
    )
    SEND_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btn_send"]',
    )
    SEND_BUTTON_TEXT = "SEND"

    CANCEL_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Cubii").instance(1)',
    )
    CANCEL_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '(//android.widget.ImageView[@content-desc="Cubii"])[2]',
    )

    def _assert_visible_one_of(
        self, locators: tuple[tuple, ...], description: str
    ) -> None:
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator in locators:
            try:
                wait.until(ec.visibility_of_element_located(locator))
                self.LOGGER.info("%s verified via `%s`.", description, locator[1])
                return
            except TimeoutException:
                continue
        raise AssertionError(f"Report a Problem screen: {description} not visible.")

    def _edit_text_has_user_input(
        self, element, placeholder_hints: tuple[str, ...]
    ) -> bool:
        """True when the field has real input, not just hint/label placeholder text."""
        text = (element.text or "").strip()
        hint = (element.get_attribute("hint") or "").strip()
        placeholders = {h.lower() for h in placeholder_hints if h}
        if hint:
            placeholders.add(hint.lower())
        if not text:
            return False
        return text.lower() not in placeholders

    def _visible_text_one_of(self, locators: tuple[tuple, ...], description: str) -> str:
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator in locators:
            try:
                element = wait.until(ec.visibility_of_element_located(locator))
                return (element.text or "").strip()
            except TimeoutException:
                continue
        raise AssertionError(f"Report a Problem screen: {description} not visible.")

    def _verify_subject_field_hint(self) -> None:
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator in (
            self.SUBJECT_FIELD,
            self.SUBJECT_FIELD_UIAUTOMATOR,
            self.SUBJECT_FIELD_XPATH,
        ):
            try:
                element = wait.until(ec.visibility_of_element_located(locator))
                hint = (element.get_attribute("hint") or "").strip()
                text = (element.text or "").strip()
                content_desc = (element.get_attribute("contentDescription") or "").strip()
                observed = hint or text or content_desc
                if self.SUBJECT_FIELD_HINT.lower() not in observed.lower():
                    raise AssertionError(
                        "Subject field (`et_subject`) should show "
                        f"{self.SUBJECT_FIELD_HINT!r}; got hint={hint!r}, text={text!r}, "
                        f"content-desc={content_desc!r}."
                    )
                self.LOGGER.info(
                    "Subject field verified via `%s` (observed=%r).", locator[1], observed
                )
                return
            except TimeoutException:
                continue
            except AssertionError:
                raise
        raise AssertionError(
            "Subject field (`com.cubii:id/et_subject`) not found on Report a Problem screen."
        )

    def verify_report_a_problem_fields(self) -> None:
        """Verify header, subject, description, description label, and SEND button."""
        self.LOGGER.info("Verifying Report a Problem form fields.")
        self._assert_visible_one_of(
            (self.SCREEN_HEADER, self.SCREEN_HEADER_UIAUTOMATOR, self.SCREEN_HEADER_XPATH),
            "screen header (`textView48`)",
        )
        self._verify_subject_field_hint()
        self._assert_visible_one_of(
            (
                self.DESCRIPTION_FIELD,
                self.DESCRIPTION_FIELD_UIAUTOMATOR,
                self.DESCRIPTION_FIELD_XPATH,
            ),
            "description field (`et_description`)",
        )
        self._assert_visible_one_of(
            (
                self.DESCRIPTION_LABEL,
                self.DESCRIPTION_LABEL_UIAUTOMATOR,
                self.DESCRIPTION_LABEL_XPATH,
            ),
            "description label (`textView49`)",
        )
        self._assert_visible_one_of(
            (self.SEND_BUTTON, self.SEND_BUTTON_UIAUTOMATOR, self.SEND_BUTTON_XPATH),
            "SEND button (`btn_send`)",
        )
        send_text = self._visible_text_one_of(
            (self.SEND_BUTTON, self.SEND_BUTTON_UIAUTOMATOR, self.SEND_BUTTON_XPATH),
            "SEND button (`btn_send`)",
        )
        if send_text.upper() != self.SEND_BUTTON_TEXT:
            raise AssertionError(
                f"SEND button text mismatch. Expected {self.SEND_BUTTON_TEXT!r}, got {send_text!r}."
            )
        self.LOGGER.info("Report a Problem form fields verified.")

    def tap_cancel_button(self) -> None:
        """Tap the Report a Problem screen cancel control (Cubii ImageView, 2nd instance)."""
        self.LOGGER.info("Tapping Report a Problem cancel button.")
        for locator in (self.CANCEL_BUTTON_UIAUTOMATOR, self.CANCEL_BUTTON_XPATH):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Report a Problem cancel tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Report a Problem cancel locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException(
            "Report a Problem cancel button could not be located "
            "(content-desc Cubii, instance 1 / xpath index 2)."
        )

    def verify_send_button_disabled_without_input(self) -> None:
        """Assert SEND is visible and disabled when subject and description are empty."""
        self.LOGGER.info(
            "Verifying SEND button is disabled without subject and description."
        )
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        el = None
        last_err: Exception | None = None
        for locator in (
            self.SEND_BUTTON,
            self.SEND_BUTTON_UIAUTOMATOR,
            self.SEND_BUTTON_XPATH,
        ):
            try:
                el = wait.until(ec.visibility_of_element_located(locator))
                self.LOGGER.info("SEND button located for disabled check via `%s`.", locator[1])
                break
            except Exception as exc:
                last_err = exc
                continue
        if el is None:
            raise AssertionError(
                "SEND button (`btn_send`) not visible on Report a Problem screen. "
                f"Last error: {last_err!r}"
            )

        subject_el = None
        for field_locator in (
            self.SUBJECT_FIELD,
            self.SUBJECT_FIELD_UIAUTOMATOR,
            self.SUBJECT_FIELD_XPATH,
        ):
            try:
                subject_el = wait.until(ec.visibility_of_element_located(field_locator))
                break
            except TimeoutException:
                continue
        if subject_el is None:
            raise AssertionError(
                "Subject field (`et_subject`) not found while checking empty inputs."
            )
        if self._edit_text_has_user_input(subject_el, (self.SUBJECT_FIELD_HINT,)):
            subject_text = (subject_el.text or "").strip()
            subject_hint = (subject_el.get_attribute("hint") or "").strip()
            raise AssertionError(
                "Subject field should have no user input for disabled SEND check; "
                f"text={subject_text!r}, hint={subject_hint!r}."
            )

        description_el = None
        for field_locator in (
            self.DESCRIPTION_FIELD,
            self.DESCRIPTION_FIELD_UIAUTOMATOR,
            self.DESCRIPTION_FIELD_XPATH,
        ):
            try:
                description_el = wait.until(
                    ec.visibility_of_element_located(field_locator)
                )
                break
            except TimeoutException:
                continue
        if description_el is None:
            raise AssertionError(
                "Description field (`et_description`) not found while checking empty inputs."
            )
        if self._edit_text_has_user_input(
            description_el, (self.DESCRIPTION_FIELD_HINT,)
        ):
            description_text = (description_el.text or "").strip()
            description_hint = (description_el.get_attribute("hint") or "").strip()
            raise AssertionError(
                "Description field should have no user input for disabled SEND check; "
                f"text={description_text!r}, hint={description_hint!r}."
            )

        try:
            live_enabled = el.is_enabled()
        except Exception as exc:
            raise AssertionError(
                f"Could not read SEND button enabled state: {exc}"
            ) from exc

        en_attr = None
        try:
            en_attr = el.get_attribute("enabled")
        except Exception:
            pass

        is_disabled = live_enabled is False or (
            en_attr is not None and str(en_attr).lower() == "false"
        )
        if not is_disabled:
            raise AssertionError(
                "SEND button (`btn_send`) should be disabled when subject and description "
                f"are empty; is_enabled={live_enabled!r}, enabled attribute={en_attr!r}."
            )
        self.LOGGER.info(
            "SEND button is disabled as expected without subject and description."
        )

    def _tap_edittext_one_of(
        self,
        locators: tuple[tuple, ...],
        description: str,
    ):
        for locator in locators:
            try:
                element = self.wait.until(ec.element_to_be_clickable(locator))
                self.LOGGER.info("%s located via `%s`.", description, locator[1])
                return element
            except TimeoutException:
                continue
        raise AssertionError(f"Report a Problem screen: {description} not found or not tappable.")

    def enter_subject_and_description(
        self, subject: str, description: str
    ) -> None:
        """Fill subject and description on the Report a Problem form."""
        self.LOGGER.info("Entering subject and description on Report a Problem form.")
        subject_el = self._tap_edittext_one_of(
            (
                self.SUBJECT_FIELD,
                self.SUBJECT_FIELD_UIAUTOMATOR,
                self.SUBJECT_FIELD_XPATH,
            ),
            "subject field (`et_subject`)",
        )
        try:
            subject_el.click()
        except Exception:
            pass
        try:
            subject_el.clear()
        except Exception:
            pass
        subject_el.send_keys(subject)
        time.sleep(float(os.getenv("CUBII_AFTER_REPORT_PROBLEM_SUBJECT_KEYS_SEC", "0.25")))

        description_el = self._tap_edittext_one_of(
            (
                self.DESCRIPTION_FIELD,
                self.DESCRIPTION_FIELD_UIAUTOMATOR,
                self.DESCRIPTION_FIELD_XPATH,
            ),
            "description field (`et_description`)",
        )
        try:
            description_el.click()
        except Exception:
            pass
        try:
            description_el.clear()
        except Exception:
            pass
        description_el.send_keys(description)
        time.sleep(float(os.getenv("CUBII_AFTER_REPORT_PROBLEM_DESCRIPTION_KEYS_SEC", "0.25")))

        if not self._edit_text_has_user_input(subject_el, (self.SUBJECT_FIELD_HINT,)):
            raise AssertionError(
                f"Subject field did not retain entered text. Expected {subject!r}."
            )
        if not self._edit_text_has_user_input(
            description_el, (self.DESCRIPTION_FIELD_HINT,)
        ):
            raise AssertionError(
                f"Description field did not retain entered text. Expected {description!r}."
            )
        self.LOGGER.info("Subject and description entered on Report a Problem form.")

    def tap_send_button(self) -> None:
        """Tap the SEND button on the Report a Problem form."""
        self.LOGGER.info("Tapping SEND button on Report a Problem form.")
        for locator in (
            self.SEND_BUTTON,
            self.SEND_BUTTON_UIAUTOMATOR,
            self.SEND_BUTTON_XPATH,
        ):
            try:
                el = self.wait.until(ec.element_to_be_clickable(locator))
                el.click()
                self.LOGGER.info("SEND button tapped via `%s`.", locator[1])
                time.sleep(float(os.getenv("CUBII_AFTER_REPORT_PROBLEM_SEND_SEC", "0.8")))
                return
            except TimeoutException:
                self.LOGGER.info(
                    "SEND button locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("SEND button (`com.cubii:id/btn_send`) could not be tapped.")
