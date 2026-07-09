import logging
import os
import random
import re
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage


class GoalsPage(BasePage):
    """Home screen Today's Goals section and goal introduction (FTUE) flow."""

    LOGGER = logging.getLogger("cubii_goals_page")

    TODAYS_GOALS_LABEL = "Today's Goals"

    TODAYS_GOALS_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().text("{TODAYS_GOALS_LABEL}")',
    )
    TODAYS_GOALS_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@text="{TODAYS_GOALS_LABEL}"]',
    )

    ADD_GOAL_BUTTON_ID = "com.cubii:id/btnAdd"
    ADD_GOAL_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{ADD_GOAL_BUTTON_ID}")',
    )
    ADD_GOAL_BUTTON_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.LinearLayout[@resource-id="{ADD_GOAL_BUTTON_ID}"]',
    )

    EDIT_GOAL_BUTTON_ID = "com.cubii:id/btn_edit"
    EDIT_GOAL_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{EDIT_GOAL_BUTTON_ID}")',
    )
    EDIT_GOAL_BUTTON_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.LinearLayout[@resource-id="{EDIT_GOAL_BUTTON_ID}"]',
    )
    EDIT_GOAL_BUTTON_TEXT_XPATH = (
        AppiumBy.XPATH,
        (
            '//android.widget.TextView['
            'contains(translate(@text, "editgoals", "EDITGOALS"), "EDIT GOAL")]'
        ),
    )
    EDIT_GOALS_BUTTON_TEXT = "EDIT GOALS"
    EDIT_GOALS_BUTTON_TEXT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().text("{EDIT_GOALS_BUTTON_TEXT}")',
    )
    EDIT_GOALS_BUTTON_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@text="{EDIT_GOALS_BUTTON_TEXT}"]',
    )

    GOAL_FTUE_NEXT_BUTTON_ID = "com.cubii:id/btnNext"
    GOAL_FTUE_NEXT_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{GOAL_FTUE_NEXT_BUTTON_ID}")',
    )
    GOAL_FTUE_NEXT_BUTTON_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.Button[@resource-id="{GOAL_FTUE_NEXT_BUTTON_ID}"]',
    )

    GOAL_FTUE_GOT_IT_BUTTON_ID = "com.cubii:id/btnGotIt1"
    GOAL_FTUE_GOT_IT_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{GOAL_FTUE_GOT_IT_BUTTON_ID}")',
    )
    GOAL_FTUE_GOT_IT_BUTTON_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.Button[@resource-id="{GOAL_FTUE_GOT_IT_BUTTON_ID}"]',
    )

    HOME_TAB_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@content-desc="Home"]',
    )
    HOME_TAB_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Home")',
    )

    TODAYS_GOALS_LOCATORS = (
        TODAYS_GOALS_UIAUTOMATOR,
        TODAYS_GOALS_XPATH,
    )
    ADD_GOAL_BUTTON_LOCATORS = (
        (AppiumBy.ID, ADD_GOAL_BUTTON_ID),
        ADD_GOAL_BUTTON_UIAUTOMATOR,
        ADD_GOAL_BUTTON_XPATH,
    )
    EDIT_GOAL_BUTTON_LOCATORS = (
        (AppiumBy.ID, EDIT_GOAL_BUTTON_ID),
        EDIT_GOAL_BUTTON_UIAUTOMATOR,
        EDIT_GOAL_BUTTON_XPATH,
        EDIT_GOALS_BUTTON_TEXT_UIAUTOMATOR,
        EDIT_GOALS_BUTTON_TEXT_XPATH,
        EDIT_GOAL_BUTTON_TEXT_XPATH,
    )
    GOAL_FTUE_NEXT_LOCATORS = (
        (AppiumBy.ID, GOAL_FTUE_NEXT_BUTTON_ID),
        GOAL_FTUE_NEXT_BUTTON_UIAUTOMATOR,
        GOAL_FTUE_NEXT_BUTTON_XPATH,
    )
    GOAL_FTUE_GOT_IT_LOCATORS = (
        (AppiumBy.ID, GOAL_FTUE_GOT_IT_BUTTON_ID),
        GOAL_FTUE_GOT_IT_BUTTON_UIAUTOMATOR,
        GOAL_FTUE_GOT_IT_BUTTON_XPATH,
    )

    GOAL_TYPE_CARD_LAYOUT_ID = "com.cubii:id/goalTypeCardLayout"
    STRIDES_GOAL_CARD_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.LinearLayout").instance(3)',
    )
    STRIDES_GOAL_CARD_XPATH = (
        AppiumBy.XPATH,
        f'(//android.widget.FrameLayout[@resource-id="{GOAL_TYPE_CARD_LAYOUT_ID}"])[1]'
        "/android.widget.LinearLayout",
    )
    STRIDES_GOAL_METRIC_LABEL = "Strides"
    CALORIES_GOAL_METRIC_LABEL = "Calories"
    MILES_GOAL_METRIC_LABEL = "Miles"
    KMS_GOAL_METRIC_LABEL = "Kms"
    TIME_GOAL_METRIC_LABEL = "Time"
    GOAL_METRIC_LABELS = (
        STRIDES_GOAL_METRIC_LABEL,
        CALORIES_GOAL_METRIC_LABEL,
        MILES_GOAL_METRIC_LABEL,
        TIME_GOAL_METRIC_LABEL,
    )

    STRIDES_GOAL_CARD_LOCATORS = (
        STRIDES_GOAL_CARD_XPATH,
        STRIDES_GOAL_CARD_UIAUTOMATOR,
    )

    GOAL_RECYCLER_VIEW_ID = "com.cubii:id/goalRecyclerView"
    STRIDES_GOAL_DETAIL_CARD_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").instance(13)',
    )
    STRIDES_GOAL_DETAIL_CARD_XPATH = (
        AppiumBy.XPATH,
        f'//androidx.recyclerview.widget.RecyclerView[@resource-id="{GOAL_RECYCLER_VIEW_ID}"]'
        "/android.widget.FrameLayout/android.view.ViewGroup",
    )
    STRIDES_GOAL_DETAIL_CARD_LOCATORS = (
        STRIDES_GOAL_DETAIL_CARD_XPATH,
        STRIDES_GOAL_DETAIL_CARD_UIAUTOMATOR,
    )

    GOAL_TITLE_ID = "com.cubii:id/goalTitle"
    GOAL_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{GOAL_TITLE_ID}")',
    )
    GOAL_TITLE_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{GOAL_TITLE_ID}"]',
    )
    GOAL_TITLE_LOCATORS = (
        (AppiumBy.ID, GOAL_TITLE_ID),
        GOAL_TITLE_UIAUTOMATOR,
        GOAL_TITLE_XPATH,
    )

    @classmethod
    def _goal_metric_title_locators(
        cls,
        metric_label: str,
        *,
        instance: int | None = None,
    ) -> tuple[tuple, ...]:
        locators: list[tuple] = []
        for label in cls._goal_metric_title_labels(metric_label):
            locators.extend(
                (
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        (
                            f'new UiSelector().resourceId("{cls.GOAL_TITLE_ID}")'
                            f'.text("{label}")'
                        ),
                    ),
                    (
                        AppiumBy.XPATH,
                        (
                            f'//android.widget.TextView[@resource-id="{cls.GOAL_TITLE_ID}" '
                            f'and @text="{label}"]'
                        ),
                    ),
                )
            )
        if instance is not None:
            locators.append(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().resourceId("{cls.GOAL_TITLE_ID}").instance({instance})',
                )
            )
        locators.extend(cls.GOAL_TITLE_LOCATORS)
        return tuple(locators)

    @classmethod
    def _strides_goal_title_locators(cls) -> tuple[tuple, ...]:
        return cls._goal_metric_title_locators(
            cls.STRIDES_GOAL_METRIC_LABEL,
            instance=0,
        )

    @classmethod
    def _goal_metric_card_value_locators(
        cls,
        metric_label: str,
        current_value: str | None = None,
    ) -> tuple[tuple, ...]:
        """Locate `goalValue` inside the RecyclerView card for a specific metric."""
        locators: list[tuple] = []
        for label in cls._goal_metric_title_labels(metric_label):
            card_value_xpath = (
                f'//androidx.recyclerview.widget.RecyclerView'
                f'[@resource-id="{cls.GOAL_RECYCLER_VIEW_ID}"]'
                f"/android.widget.FrameLayout["
                f'.//android.widget.TextView[@resource-id="{cls.GOAL_TITLE_ID}" '
                f'and @text="{label}"]'
                f']//android.widget.EditText[@resource-id="{cls.GOAL_VALUE_ID}"]'
            )
            if current_value:
                locators.append(
                    (
                        AppiumBy.XPATH,
                        f'{card_value_xpath}[@text="{current_value}"]',
                    )
                )
            locators.append((AppiumBy.XPATH, card_value_xpath))
            locators.append(
                (
                    AppiumBy.XPATH,
                    (
                        f'//android.widget.TextView[@resource-id="{cls.GOAL_TITLE_ID}" '
                        f'and @text="{label}"]'
                        f"/ancestor::android.widget.FrameLayout[1]"
                        f'//android.widget.EditText[@resource-id="{cls.GOAL_VALUE_ID}"]'
                    ),
                )
            )
            locators.append(
                (
                    AppiumBy.XPATH,
                    (
                        f'//android.widget.TextView[@resource-id="{cls.GOAL_TITLE_ID}" '
                        f'and @text="{label}"]'
                        f"/ancestor::android.view.ViewGroup[1]"
                        f'//android.widget.EditText[@resource-id="{cls.GOAL_VALUE_ID}"]'
                    ),
                )
            )
        return tuple(locators)

    @classmethod
    def _goal_metric_value_locators(
        cls,
        metric_label: str,
        current_value: str | None = None,
    ) -> tuple[tuple, ...]:
        return cls._goal_metric_card_value_locators(metric_label, current_value)

    GOAL_VALUE_ID = "com.cubii:id/goalValue"
    GOAL_VALUE_CLASS = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    GOAL_VALUE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{GOAL_VALUE_ID}")',
    )
    GOAL_VALUE_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.EditText[@resource-id="{GOAL_VALUE_ID}"]',
    )
    GOAL_VALUE_LOCATORS = (
        (AppiumBy.ID, GOAL_VALUE_ID),
        GOAL_VALUE_UIAUTOMATOR,
        GOAL_VALUE_XPATH,
        GOAL_VALUE_CLASS,
    )

    GOAL_DAYS_TITLE_ID = "com.cubii:id/goal_days_title"
    GOAL_DAYS_TITLE_TEXT = "On every day"
    GOAL_DAYS_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{GOAL_DAYS_TITLE_ID}")',
    )
    GOAL_DAYS_TITLE_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{GOAL_DAYS_TITLE_ID}"]',
    )
    GOAL_DAYS_TITLE_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{GOAL_DAYS_TITLE_ID}" '
        f'and @text="{GOAL_DAYS_TITLE_TEXT}"]',
    )
    GOAL_DAYS_TITLE_LOCATORS = (
        GOAL_DAYS_TITLE_TEXT_XPATH,
        (AppiumBy.ID, GOAL_DAYS_TITLE_ID),
        GOAL_DAYS_TITLE_UIAUTOMATOR,
        GOAL_DAYS_TITLE_XPATH,
    )

    SAVE_GOALS_BUTTON_ID = "com.cubii:id/btnSave"
    SAVE_GOALS_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{SAVE_GOALS_BUTTON_ID}")',
    )
    SAVE_GOALS_BUTTON_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.Button[@resource-id="{SAVE_GOALS_BUTTON_ID}"]',
    )
    SAVE_GOALS_BUTTON_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@text="SAVE GOALS"]',
    )
    SAVE_GOALS_BUTTON_LOCATORS = (
        (AppiumBy.ID, SAVE_GOALS_BUTTON_ID),
        SAVE_GOALS_BUTTON_UIAUTOMATOR,
        SAVE_GOALS_BUTTON_XPATH,
        SAVE_GOALS_BUTTON_TEXT_XPATH,
    )

    DONE_BUTTON_ID = "com.cubii:id/btnDone"
    DONE_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{DONE_BUTTON_ID}")',
    )
    DONE_BUTTON_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.Button[@resource-id="{DONE_BUTTON_ID}"]',
    )
    DONE_BUTTON_LOCATORS = (
        (AppiumBy.ID, DONE_BUTTON_ID),
        DONE_BUTTON_UIAUTOMATOR,
        DONE_BUTTON_XPATH,
    )

    HOME_GOAL_CARD_LAYOUT_ID = "com.cubii:id/constraintLayout3"
    HOME_GOAL_TEXT_ID = "com.cubii:id/goalText"
    HOME_GOAL_CARD_METRICS = (
        (STRIDES_GOAL_METRIC_LABEL, 0),
        (CALORIES_GOAL_METRIC_LABEL, 1),
        (KMS_GOAL_METRIC_LABEL, 2),
        (TIME_GOAL_METRIC_LABEL, 3),
    )

    GOAL_VALUE_ERROR_TEXT_ID = "com.cubii:id/txtTimeErrorText"
    GOAL_VALUE_VALIDATION_MESSAGE = "Value should be more than zero"
    GOAL_VALUE_ERROR_TEXT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{GOAL_VALUE_ERROR_TEXT_ID}")',
    )
    GOAL_VALUE_ERROR_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{GOAL_VALUE_ERROR_TEXT_ID}"]',
    )
    GOAL_VALUE_ERROR_TEXT_MESSAGE_XPATH = (
        AppiumBy.XPATH,
        (
            f'//android.widget.TextView[@resource-id="{GOAL_VALUE_ERROR_TEXT_ID}"'
            f' and @text="{GOAL_VALUE_VALIDATION_MESSAGE}"]'
        ),
    )
    GOAL_VALUE_ERROR_TEXT_LOCATORS = (
        (AppiumBy.ID, GOAL_VALUE_ERROR_TEXT_ID),
        GOAL_VALUE_ERROR_TEXT_UIAUTOMATOR,
        GOAL_VALUE_ERROR_TEXT_XPATH,
        GOAL_VALUE_ERROR_TEXT_MESSAGE_XPATH,
    )

    DELETE_ALL_GOALS_BUTTON_ID = "com.cubii:id/btnDeleteAll"
    DELETE_ALL_GOALS_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{DELETE_ALL_GOALS_BUTTON_ID}")',
    )
    DELETE_ALL_GOALS_BUTTON_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.Button[@resource-id="{DELETE_ALL_GOALS_BUTTON_ID}"]',
    )
    DELETE_ALL_GOALS_BUTTON_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@text="DELETE ALL GOALS"]',
    )
    DELETE_ALL_GOALS_BUTTON_LOCATORS = (
        (AppiumBy.ID, DELETE_ALL_GOALS_BUTTON_ID),
        DELETE_ALL_GOALS_BUTTON_UIAUTOMATOR,
        DELETE_ALL_GOALS_BUTTON_XPATH,
        DELETE_ALL_GOALS_BUTTON_TEXT_XPATH,
    )

    ADD_GOAL_SCREEN_TITLE = "Add Goal"
    EDIT_GOAL_SCREEN_TITLE = "Edit Goal"
    ADD_GOAL_SCREEN_TITLE_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@text="{ADD_GOAL_SCREEN_TITLE}"]',
    )
    EDIT_GOAL_SCREEN_TITLE_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@text="{EDIT_GOAL_SCREEN_TITLE}"]',
    )
    ADD_GOAL_SCREEN_TITLE_LOCATORS = (ADD_GOAL_SCREEN_TITLE_XPATH,)
    EDIT_GOAL_SCREEN_TITLE_LOCATORS = (EDIT_GOAL_SCREEN_TITLE_XPATH,)
    GOAL_EDIT_OR_ADD_SCREEN_TITLE_LOCATORS = (
        EDIT_GOAL_SCREEN_TITLE_XPATH,
        ADD_GOAL_SCREEN_TITLE_XPATH,
    )
    GOAL_RECYCLER_VIEW_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{GOAL_RECYCLER_VIEW_ID}")',
    )
    GOAL_RECYCLER_VIEW_XPATH = (
        AppiumBy.XPATH,
        f'//androidx.recyclerview.widget.RecyclerView[@resource-id="{GOAL_RECYCLER_VIEW_ID}"]',
    )
    GOAL_RECYCLER_VIEW_LOCATORS = (
        (AppiumBy.ID, GOAL_RECYCLER_VIEW_ID),
        GOAL_RECYCLER_VIEW_UIAUTOMATOR,
        GOAL_RECYCLER_VIEW_XPATH,
    )

    GOAL_CANCEL_CLOSE_BUTTON_ID = "com.cubii:id/close"

    GOALS_BACK_BUTTON_ACCESSIBILITY = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    GOALS_BACK_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Navigate up")',
    )
    GOALS_BACK_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Navigate up"]',
    )
    GOALS_BACK_BUTTON_LOCATORS = (
        GOALS_BACK_BUTTON_ACCESSIBILITY,
        GOALS_BACK_BUTTON_UIAUTOMATOR,
        GOALS_BACK_BUTTON_XPATH,
        (AppiumBy.CLASS_NAME, "android.widget.ImageButton"),
    )

    SAVE_CHANGES_POPUP_TITLE_ID = "com.cubii:id/textView68"
    SAVE_CHANGES_POPUP_TITLE_TEXT = "Save Changes?"
    SAVE_CHANGES_POPUP_MESSAGE_ID = "com.cubii:id/textView69"
    SAVE_CHANGES_POPUP_MESSAGE_TEXT = "Are you sure you want to save all your changes?"
    SAVE_CHANGES_POPUP_NO_BUTTON_ID = "com.cubii:id/btnNo"
    SAVE_CHANGES_POPUP_YES_BUTTON_ID = "com.cubii:id/btnYes"

    SAVE_CHANGES_POPUP_TITLE_LOCATORS = (
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            (
                f'new UiSelector().resourceId("{SAVE_CHANGES_POPUP_TITLE_ID}")'
                f'.text("{SAVE_CHANGES_POPUP_TITLE_TEXT}")'
            ),
        ),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{SAVE_CHANGES_POPUP_TITLE_TEXT}")',
        ),
        (AppiumBy.ID, SAVE_CHANGES_POPUP_TITLE_ID),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().resourceId("{SAVE_CHANGES_POPUP_TITLE_ID}")',
        ),
        (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@resource-id="{SAVE_CHANGES_POPUP_TITLE_ID}"]',
        ),
        (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@text="{SAVE_CHANGES_POPUP_TITLE_TEXT}"]',
        ),
    )
    SAVE_CHANGES_POPUP_MESSAGE_LOCATORS = (
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            (
                f'new UiSelector().resourceId("{SAVE_CHANGES_POPUP_MESSAGE_ID}")'
                f'.text("{SAVE_CHANGES_POPUP_MESSAGE_TEXT}")'
            ),
        ),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{SAVE_CHANGES_POPUP_MESSAGE_TEXT}")',
        ),
        (AppiumBy.ID, SAVE_CHANGES_POPUP_MESSAGE_ID),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().resourceId("{SAVE_CHANGES_POPUP_MESSAGE_ID}")',
        ),
        (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@resource-id="{SAVE_CHANGES_POPUP_MESSAGE_ID}"]',
        ),
        (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@text="{SAVE_CHANGES_POPUP_MESSAGE_TEXT}"]',
        ),
    )
    SAVE_CHANGES_POPUP_NO_BUTTON_LOCATORS = (
        (AppiumBy.ID, SAVE_CHANGES_POPUP_NO_BUTTON_ID),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().resourceId("{SAVE_CHANGES_POPUP_NO_BUTTON_ID}")',
        ),
        (
            AppiumBy.XPATH,
            f'//android.widget.Button[@resource-id="{SAVE_CHANGES_POPUP_NO_BUTTON_ID}"]',
        ),
    )
    SAVE_CHANGES_POPUP_YES_BUTTON_LOCATORS = (
        (AppiumBy.ID, SAVE_CHANGES_POPUP_YES_BUTTON_ID),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().resourceId("{SAVE_CHANGES_POPUP_YES_BUTTON_ID}")',
        ),
        (
            AppiumBy.XPATH,
            f'//android.widget.Button[@resource-id="{SAVE_CHANGES_POPUP_YES_BUTTON_ID}"]',
        ),
    )

    @classmethod
    def _goal_metric_text_locators(cls, label: str) -> tuple[tuple, ...]:
        return (
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{label}")',
            ),
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@text="{label}"]',
            ),
        )

    @classmethod
    def _miles_or_kms_goal_metric_locators(cls) -> tuple[tuple, ...]:
        """Miles and Kms are the same metric with region-specific labels."""
        locators: list[tuple] = []
        for label in (cls.MILES_GOAL_METRIC_LABEL, cls.KMS_GOAL_METRIC_LABEL):
            locators.extend(cls._goal_metric_text_locators(label))
        return tuple(locators)

    def _short_wait(self, timeout: int | None = None) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout or Settings.EXPLICIT_WAIT)

    def _is_visible(self, locators: tuple[tuple, ...], timeout: int = 3) -> bool:
        for locator in locators:
            try:
                WebDriverWait(self.driver, timeout).until(
                    ec.visibility_of_element_located(locator)
                )
                return True
            except TimeoutException:
                continue
        return False

    def _viewport_bounds(self) -> tuple[int, int]:
        screen_h = self.driver.get_window_size()["height"]
        top = int(screen_h * float(os.getenv("CUBII_GOALS_VIEWPORT_TOP", "0.10")))
        bottom = int(screen_h * float(os.getenv("CUBII_GOALS_VIEWPORT_BOTTOM", "0.90")))
        return top, bottom

    def _element_center_in_viewport(self, element) -> bool:
        """True when the element center sits inside the usable home viewport."""
        try:
            if not element.is_displayed():
                return False
            top, bottom = self._viewport_bounds()
            location = element.location
            size = element.size
            center_y = location["y"] + (size["height"] // 2)
            in_view = top <= center_y <= bottom
            if not in_view:
                self.LOGGER.debug(
                    "Element center_y=%s outside viewport [%s, %s].",
                    center_y,
                    top,
                    bottom,
                )
            return in_view
        except Exception as exc:
            self.LOGGER.debug("Viewport check failed: %s", exc)
            return False

    def _find_elements_safe(self, locator: tuple) -> list:
        try:
            return self.driver.find_elements(*locator)
        except WebDriverException as exc:
            self.LOGGER.debug("find_elements failed for `%s`: %s", locator[1], exc)
            return []

    def _find_first_in_viewport(self, locators: tuple[tuple, ...]):
        for locator in locators:
            for element in self._find_elements_safe(locator):
                if self._element_center_in_viewport(element):
                    return element
        return None

    def _find_goal_button_near_todays_goals(self, locators: tuple[tuple, ...], *, label: str):
        """
        Pick the goal action control closest below Today's Goals in the viewport.

        Avoids XPath2 `following::` / `ancestor::` axes that crash UiAutomator2.
        """
        todays_goals = self._find_first_in_viewport(self.TODAYS_GOALS_LOCATORS)
        if todays_goals is None:
            return None

        goals_y = todays_goals.location["y"]
        candidates = []
        for locator in locators:
            for element in self._find_elements_safe(locator):
                try:
                    if not self._element_center_in_viewport(element):
                        continue
                    button_y = element.location["y"]
                    candidates.append((button_y - goals_y, element))
                except WebDriverException:
                    continue

        if not candidates:
            return None

        below = [item for item in candidates if item[0] >= 0]
        _, chosen = min(below or candidates, key=lambda item: abs(item[0]))
        self.LOGGER.info("Resolved %s nearest Today's Goals in viewport.", label)
        return chosen

    def _click_first_clickable(
        self,
        locators: tuple[tuple, ...],
        *,
        label: str,
        timeout: int | None = None,
    ) -> None:
        wait_sec = timeout or Settings.EXPLICIT_WAIT
        for locator in locators:
            try:
                element = WebDriverWait(self.driver, wait_sec).until(
                    ec.element_to_be_clickable(locator)
                )
                element.click()
                self.LOGGER.info("Tapped `%s` via `%s`.", label, locator[1])
                return
            except (TimeoutException, WebDriverException) as exc:
                self.LOGGER.debug(
                    "Locator `%s` not clickable for `%s` (%s); trying next.",
                    locator[1],
                    label,
                    exc,
                )
        raise AssertionError(f"Could not tap `{label}` — no locator became clickable.")

    def ensure_home_tab_selected(self) -> None:
        """Open the Home bottom-nav tab when another tab is active."""
        for locator in (self.HOME_TAB_XPATH, self.HOME_TAB_UIAUTOMATOR):
            try:
                element = WebDriverWait(self.driver, 6).until(
                    ec.element_to_be_clickable(locator)
                )
                element.click()
                time.sleep(float(os.getenv("CUBII_AFTER_HOME_TAB_TAP_SEC", "0.8")))
                self.LOGGER.info("Home tab selected via `%s`.", locator[1])
                return
            except TimeoutException:
                continue

        self.LOGGER.info("Home tab locator not found; continuing on current screen.")

    def _scroll_home(self, *, direction: str, percent: float = 0.7) -> None:
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
                "direction": direction,
                "percent": percent,
            },
        )
        self.LOGGER.info(
            "Performed home screen scroll-%s gesture (percent=%s).",
            direction,
            percent,
        )

    def _scroll_home_down(self, percent: float = 0.7) -> None:
        self._scroll_home(direction="down", percent=percent)

    def _todays_goals_on_screen(self) -> bool:
        """True when Today's Goals label is visible on the home screen."""
        if self._find_first_in_viewport(self.TODAYS_GOALS_LOCATORS) is not None:
            return True
        return self._is_visible(self.TODAYS_GOALS_LOCATORS, timeout=1)

    def scroll_to_todays_goals_section(self) -> None:
        """Scroll the home screen down until Today's Goals is on screen."""
        self.LOGGER.info("Scrolling home screen down to Today's Goals section.")
        self.ensure_home_tab_selected()

        if self._todays_goals_on_screen():
            self.LOGGER.info("Today's Goals already on screen; no scroll needed.")
            return

        pause = float(os.getenv("CUBII_GOALS_SCROLL_PAUSE_SEC", "0.5"))
        percent = float(os.getenv("CUBII_GOALS_HOME_SCROLL_PERCENT", "0.65"))
        max_scrolls = int(os.getenv("CUBII_GOALS_HOME_SCROLL_ATTEMPTS", "12"))

        for attempt in range(1, max_scrolls + 1):
            self.LOGGER.info(
                "Today's Goals not on screen yet; scrolling down (%s/%s).",
                attempt,
                max_scrolls,
            )
            self._scroll_home_down(percent=percent)
            time.sleep(pause)

            if self._todays_goals_on_screen():
                self.LOGGER.info(
                    "Today's Goals found on screen after %s scroll-down gesture(s).",
                    attempt,
                )
                return

        raise AssertionError(
            f"Today's Goals section ({self.TODAYS_GOALS_LABEL!r}) was not found "
            f"after {max_scrolls} scroll-down gestures on the home screen."
        )

    def verify_todays_goals_section_visible(self) -> None:
        """Assert Today's Goals is on screen."""
        if not self._todays_goals_on_screen():
            self.scroll_to_todays_goals_section()
        if not self._todays_goals_on_screen():
            raise AssertionError(
                f"Today's Goals label ({self.TODAYS_GOALS_LABEL!r}) is not visible "
                "on the home screen."
            )
        self.LOGGER.info("Verified Today's Goals section is visible on home screen.")

    def tap_add_goal_button(self) -> None:
        """Scroll down in Today's Goals and tap Add goal (`btnAdd`)."""
        self.LOGGER.info(
            "Scrolling down to Add goal (`btnAdd`) in Today's Goals section."
        )
        if not self._todays_goals_on_screen():
            self.scroll_to_todays_goals_section()

        pause = float(os.getenv("CUBII_GOALS_SCROLL_PAUSE_SEC", "0.5"))
        percent = float(os.getenv("CUBII_GOALS_HOME_SCROLL_PERCENT", "0.65"))
        max_scrolls = int(os.getenv("CUBII_GOALS_ADD_BUTTON_SCROLL_ATTEMPTS", "8"))

        for attempt in range(max_scrolls + 1):
            button = self._find_goal_button_near_todays_goals(
                self.ADD_GOAL_BUTTON_LOCATORS,
                label="Add goal (`btnAdd`)",
            )
            if button is None:
                button = self._find_first_in_viewport(self.ADD_GOAL_BUTTON_LOCATORS)

            if button is not None:
                try:
                    button.click()
                    self.LOGGER.info(
                        "Tapped Add goal (`btnAdd`) after %s scroll-down gesture(s).",
                        attempt,
                    )
                    time.sleep(float(os.getenv("CUBII_AFTER_ADD_GOAL_TAP_SEC", "0.8")))
                    return
                except WebDriverException as exc:
                    self.LOGGER.info(
                        "Add goal (`btnAdd`) not tappable on attempt %s: %s",
                        attempt + 1,
                        exc,
                    )

            if attempt >= max_scrolls:
                break

            self.LOGGER.info(
                "Add goal (`btnAdd`) not on screen yet; scrolling down (%s/%s).",
                attempt + 1,
                max_scrolls,
            )
            self._scroll_home_down(percent=percent)
            time.sleep(pause)

        raise AssertionError(
            "Could not tap Add goal (`btnAdd`) after scrolling down in "
            "Today's Goals section."
        )

    def tap_edit_goal_button(self) -> None:
        """Scroll down in Today's Goals and tap Edit goal (`btn_edit`)."""
        self.LOGGER.info(
            "Scrolling down to Edit goal (`btn_edit`) in Today's Goals section."
        )
        if not self._todays_goals_on_screen():
            self.scroll_to_todays_goals_section()

        pause = float(os.getenv("CUBII_GOALS_SCROLL_PAUSE_SEC", "0.5"))
        percent = float(os.getenv("CUBII_GOALS_HOME_SCROLL_PERCENT", "0.65"))
        max_scrolls = int(os.getenv("CUBII_GOALS_EDIT_BUTTON_SCROLL_ATTEMPTS", "8"))

        for attempt in range(max_scrolls + 1):
            button = self._find_goal_button_near_todays_goals(
                self.EDIT_GOAL_BUTTON_LOCATORS,
                label="Edit goal (`btn_edit`)",
            )
            if button is None:
                button = self._find_first_in_viewport(self.EDIT_GOAL_BUTTON_LOCATORS)

            if button is not None:
                try:
                    button.click()
                    self.LOGGER.info(
                        "Tapped Edit goal (`btn_edit`) after %s scroll-down gesture(s).",
                        attempt,
                    )
                    time.sleep(float(os.getenv("CUBII_AFTER_ADD_GOAL_TAP_SEC", "0.8")))
                    return
                except WebDriverException as exc:
                    self.LOGGER.info(
                        "Edit goal (`btn_edit`) not tappable on attempt %s: %s",
                        attempt + 1,
                        exc,
                    )

            if attempt >= max_scrolls:
                break

            self.LOGGER.info(
                "Edit goal (`btn_edit`) not on screen yet; scrolling down (%s/%s).",
                attempt + 1,
                max_scrolls,
            )
            self._scroll_home_down(percent=percent)
            time.sleep(pause)

        raise AssertionError(
            "Could not tap Edit goal (`btn_edit`) after scrolling down in "
            "Today's Goals section."
        )

    def _is_on_add_or_edit_goal_screen(self) -> bool:
        return self._is_visible(self.GOAL_EDIT_OR_ADD_SCREEN_TITLE_LOCATORS, timeout=2)

    def _return_to_home_from_goal_screen_if_needed(self) -> None:
        """Leave Add/Edit Goal so EDIT GOALS on home can be tapped."""
        if not self._is_on_add_or_edit_goal_screen():
            return
        self.LOGGER.info("Add/Edit Goal screen open; navigating back to home.")
        self.tap_goals_back_button()
        time.sleep(float(os.getenv("CUBII_AFTER_RETURN_HOME_FROM_GOALS_SEC", "0.8")))
        self.ensure_home_tab_selected()

    def tap_edit_goals_option(self) -> None:
        """Scroll down on home and tap EDIT GOALS (`btn_edit`)."""
        self.LOGGER.info("Scrolling down to tap EDIT GOALS (`btn_edit`).")
        self._return_to_home_from_goal_screen_if_needed()
        self.tap_edit_goal_button()

    def _minimum_goal_value_for_metric(self, metric_label: str) -> float:
        if metric_label in (
            self.CALORIES_GOAL_METRIC_LABEL,
            self.KMS_GOAL_METRIC_LABEL,
            self.MILES_GOAL_METRIC_LABEL,
        ):
            return 0.1
        return 1.0

    def _reject_disallowed_goal_value(self, value: str, metric_label: str) -> str:
        """Reject empty, zero, or below-minimum goal values."""
        cleaned = value.strip()
        if not cleaned:
            raise AssertionError(f"{metric_label} goal value must not be empty.")
        try:
            numeric = float(cleaned)
        except ValueError as exc:
            raise AssertionError(
                f"{metric_label} goal value {cleaned!r} is not numeric."
            ) from exc
        minimum = self._minimum_goal_value_for_metric(metric_label)
        if numeric < minimum:
            raise AssertionError(
                f"{metric_label} goal value {cleaned!r} is not allowed "
                f"(minimum {minimum:g})."
            )
        return cleaned

    def _resolve_random_int_goal_value(
        self,
        *,
        metric_label: str,
        env_key: str,
        default_min: int,
        default_max: int,
        value: str | None = None,
        min_env_key: str,
        max_env_key: str,
        enforce_min: int | None = None,
    ) -> str:
        if value is not None:
            return self._reject_disallowed_goal_value(value, metric_label)
        env_value = os.getenv(env_key, "").strip()
        if env_value and env_value.lower() not in {"random", "rand"}:
            return self._reject_disallowed_goal_value(env_value, metric_label)
        min_value = int(os.getenv(min_env_key, str(default_min)))
        max_value = int(os.getenv(max_env_key, str(default_max)))
        if enforce_min is not None:
            min_value = max(min_value, enforce_min)
        if min_value > max_value:
            min_value, max_value = max_value, min_value
        chosen = str(random.randint(min_value, max_value))
        self.LOGGER.info(
            "Selected random %s goal value %s (range %s–%s).",
            metric_label,
            chosen,
            min_value,
            max_value,
        )
        return self._reject_disallowed_goal_value(chosen, metric_label)

    def _resolve_random_decimal_goal_value(
        self,
        *,
        metric_label: str,
        env_key: str,
        default_min: float,
        default_max: float,
        value: str | None = None,
        min_env_key: str,
        max_env_key: str,
    ) -> str:
        if value is not None:
            return self._reject_disallowed_goal_value(value, metric_label)
        env_value = os.getenv(env_key, "").strip()
        if env_value and env_value.lower() not in {"random", "rand"}:
            return self._reject_disallowed_goal_value(env_value, metric_label)
        min_value = float(os.getenv(min_env_key, str(default_min)))
        max_value = float(os.getenv(max_env_key, str(default_max)))
        min_value = max(min_value, self._minimum_goal_value_for_metric(metric_label))
        if min_value > max_value:
            min_value, max_value = max_value, min_value
        chosen_value = round(random.uniform(min_value, max_value), 1)
        chosen = f"{chosen_value:.1f}".rstrip("0").rstrip(".")
        if not chosen:
            chosen = str(min_value)
        self.LOGGER.info(
            "Selected random %s goal value %s (range %s–%s).",
            metric_label,
            chosen,
            min_value,
            max_value,
        )
        return self._reject_disallowed_goal_value(chosen, metric_label)

    def _resolve_edit_strides_goal_value(self, value: str | None = None) -> str:
        """Pick strides goal value: explicit arg, env override, or random 1–200."""
        return self._resolve_random_int_goal_value(
            metric_label=self.STRIDES_GOAL_METRIC_LABEL,
            env_key="CUBII_EDIT_STRIDES_GOAL_VALUE",
            default_min=1,
            default_max=200,
            value=value,
            min_env_key="CUBII_EDIT_STRIDES_GOAL_RANDOM_MIN",
            max_env_key="CUBII_EDIT_STRIDES_GOAL_RANDOM_MAX",
            enforce_min=1,
        )

    def _resolve_edit_calories_goal_value(self, value: str | None = None) -> str:
        return self._resolve_random_decimal_goal_value(
            metric_label=self.CALORIES_GOAL_METRIC_LABEL,
            env_key="CUBII_EDIT_CALORIES_GOAL_VALUE",
            default_min=0.1,
            default_max=10.0,
            value=value,
            min_env_key="CUBII_EDIT_CALORIES_GOAL_RANDOM_MIN",
            max_env_key="CUBII_EDIT_CALORIES_GOAL_RANDOM_MAX",
        )

    def _resolve_edit_kms_goal_value(self, value: str | None = None) -> str:
        return self._resolve_random_decimal_goal_value(
            metric_label=f"{self.KMS_GOAL_METRIC_LABEL}/{self.MILES_GOAL_METRIC_LABEL}",
            env_key="CUBII_EDIT_KMS_GOAL_VALUE",
            default_min=0.1,
            default_max=10.0,
            value=value,
            min_env_key="CUBII_EDIT_KMS_GOAL_RANDOM_MIN",
            max_env_key="CUBII_EDIT_KMS_GOAL_RANDOM_MAX",
        )

    def _resolve_edit_time_goal_value(self, value: str | None = None) -> str:
        return self._resolve_random_int_goal_value(
            metric_label=self.TIME_GOAL_METRIC_LABEL,
            env_key="CUBII_EDIT_TIME_GOAL_VALUE",
            default_min=1,
            default_max=120,
            value=value,
            min_env_key="CUBII_EDIT_TIME_GOAL_RANDOM_MIN",
            max_env_key="CUBII_EDIT_TIME_GOAL_RANDOM_MAX",
            enforce_min=1,
        )

    def _set_field_text(self, element, value: str) -> None:
        """Set text on an Android field without leaving a stale zero behind."""
        element.click()
        try:
            element.clear()
        except Exception:
            pass
        try:
            element.set_value(value)
            return
        except Exception:
            pass
        try:
            self.driver.execute_script(
                "mobile: setText",
                {"elementId": element.id, "text": value},
            )
            return
        except Exception:
            pass
        try:
            self.driver.execute_script(
                "mobile: replaceText",
                {"elementId": element.id, "text": value},
            )
            return
        except Exception:
            pass
        element.send_keys(value)

    def _set_goal_value_on_field(self, field, value: str, *, metric_label: str) -> str:
        """Enter a goal value without leaving zero in the field."""
        goal_value = self._reject_disallowed_goal_value(value, metric_label)
        time.sleep(float(os.getenv("CUBII_BEFORE_GOAL_VALUE_ENTRY_SEC", "0.2")))
        self._set_field_text(field, goal_value)
        self._hide_keyboard_after_goal_value_entry()

        observed = (field.text or field.get_attribute("text") or "").strip()
        if not self._goal_values_match(goal_value, observed):
            self._set_field_text(field, goal_value)
            self._hide_keyboard_after_goal_value_entry()
            observed = (field.text or field.get_attribute("text") or "").strip()

        if not self._goal_values_match(goal_value, observed):
            raise AssertionError(
                f"{metric_label} goal value was not set correctly in `goalValue`. "
                f"Expected {goal_value!r}, observed {observed!r}."
            )
        return self._reject_disallowed_goal_value(observed, metric_label)

    def _is_goal_metric_title_visible(self, metric_label: str) -> bool:
        return (
            self._find_visible_element(
                self._goal_metric_title_locators(metric_label),
            )
            is not None
        )

    def _scroll_edit_goal_metric_into_view(self, metric_label: str) -> None:
        """Scroll Edit Goal screen until the metric goal card title is visible."""
        pause = float(os.getenv("CUBII_GOALS_SCROLL_PAUSE_SEC", "0.5"))
        percent = float(os.getenv("CUBII_GOALS_EDIT_SCREEN_SCROLL_PERCENT", "0.7"))
        max_scrolls = int(os.getenv("CUBII_GOAL_EDIT_SCROLL_ATTEMPTS", "12"))

        self.LOGGER.info(
            "Scrolling down to bring %s goal card into view for editing.",
            metric_label,
        )
        self._scroll_goal_metric_card_into_view(metric_label)
        time.sleep(pause)

        for attempt in range(max_scrolls + 1):
            if self._is_goal_metric_title_visible(metric_label):
                self.LOGGER.info(
                    "%s goal title visible after %s scroll(s).",
                    metric_label,
                    attempt,
                )
                return

            if attempt >= max_scrolls:
                break

            self.LOGGER.info(
                "%s goal card not visible yet; scrolling down (%s/%s).",
                metric_label,
                attempt + 1,
                max_scrolls,
            )
            if not self._scroll_goal_metric_card_into_view(metric_label):
                self._scroll_add_goal_screen_down(percent=percent)
            time.sleep(pause)

        raise AssertionError(
            f"Could not scroll {metric_label} goal card into view on the Edit Goal "
            f"screen after {max_scrolls} scroll attempt(s)."
        )

    def _find_goal_metric_card_title_element(self, metric_label: str):
        """Return the visible `goalTitle` element for a metric card."""
        candidates = self._goal_metric_title_candidates(metric_label)
        if candidates:
            return candidates[0]
        return self._find_visible_element(
            self._goal_metric_title_locators(metric_label),
        )

    def _find_goal_value_field_for_metric_card(
        self,
        metric_label: str,
        current_value: str | None = None,
    ):
        """Find the `goalValue` EditText inside the metric's own goal card."""
        locators = self._goal_metric_card_value_locators(metric_label, current_value)
        for locator in locators:
            try:
                field = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT).until(
                    ec.element_to_be_clickable(locator)
                )
                if field.is_displayed():
                    self.LOGGER.info(
                        "%s goal value field located in metric card via `%s`.",
                        metric_label,
                        locator[1],
                    )
                    return field
            except TimeoutException:
                continue

        title_element = self._find_goal_metric_card_title_element(metric_label)
        if title_element is not None:
            for ancestor_xpath in (
                "./ancestor::android.widget.FrameLayout[1]",
                "./ancestor::android.view.ViewGroup[1]",
            ):
                try:
                    card = title_element.find_element(AppiumBy.XPATH, ancestor_xpath)
                    field = card.find_element(AppiumBy.ID, self.GOAL_VALUE_ID)
                    if field.is_displayed():
                        self.LOGGER.info(
                            "%s goal value field located relative to `goalTitle`.",
                            metric_label,
                        )
                        return field
                except WebDriverException:
                    continue
        return None

    def _find_editable_goal_value_field(
        self,
        metric_label: str,
        current_value: str | None = None,
    ):
        """Scroll and locate the metric-scoped `goalValue` field."""
        pause = float(os.getenv("CUBII_GOALS_SCROLL_PAUSE_SEC", "0.5"))
        percent = float(os.getenv("CUBII_GOALS_EDIT_SCREEN_SCROLL_PERCENT", "0.7"))
        max_scrolls = int(os.getenv("CUBII_GOAL_EDIT_SCROLL_ATTEMPTS", "12"))

        for attempt in range(max_scrolls + 1):
            field = self._find_goal_value_field_for_metric_card(
                metric_label,
                current_value,
            )
            if field is not None:
                self.LOGGER.info(
                    "%s goal value field found after %s scroll(s).",
                    metric_label,
                    attempt,
                )
                return field

            if attempt >= max_scrolls:
                break

            self.LOGGER.info(
                "%s goal value field not visible yet; scrolling down (%s/%s).",
                metric_label,
                attempt + 1,
                max_scrolls,
            )
            if not self._scroll_goal_metric_card_into_view(metric_label):
                self._scroll_add_goal_screen_down(percent=percent)
            time.sleep(pause)

        return None

    def _edit_goal_metric(
        self,
        metric_label: str,
        new_value: str,
        *,
        current_value: str | None = None,
    ) -> str:
        """Tap a goal card title and update its scoped `goalValue`."""
        self.LOGGER.info(
            "Editing %s goal to %r on Edit Goal screen.",
            metric_label,
            new_value,
        )
        self._scroll_edit_goal_metric_into_view(metric_label)

        title_element = self._find_goal_metric_card_title_element(metric_label)
        if title_element is not None:
            title_element.click()
            self.LOGGER.info("Tapped %s goal title (`goalTitle`) in metric card.", metric_label)
        else:
            self._click_first_clickable(
                self._goal_metric_title_locators(metric_label),
                label=f"{metric_label} goal title (`goalTitle`)",
            )
        time.sleep(float(os.getenv("CUBII_AFTER_GOAL_TITLE_TAP_SEC", "0.4")))

        field = self._find_goal_value_field_for_metric_card(
            metric_label,
            current_value,
        )

        if field is None:
            raise AssertionError(
                f"{metric_label} goal value input (`goalValue`) was not found for editing."
            )

        observed = self._set_goal_value_on_field(
            field,
            new_value,
            metric_label=metric_label,
        )
        self.LOGGER.info(
            "%s goal updated to %r (`goalValue`).",
            metric_label,
            observed,
        )
        return observed

    def edit_strides_goal(self, value: str | None = None) -> str:
        """Open the Strides goal card and update its `goalValue`."""
        new_value = self._resolve_edit_strides_goal_value(value)
        current_value = os.getenv("CUBII_STRIDES_GOAL_CURRENT_VALUE", "").strip() or None
        return self._edit_goal_metric(
            self.STRIDES_GOAL_METRIC_LABEL,
            new_value,
            current_value=current_value,
        )

    def edit_calories_goal(self, value: str | None = None) -> str:
        """Open the Calories goal card and update its `goalValue`."""
        new_value = self._resolve_edit_calories_goal_value(value)
        current_value = os.getenv("CUBII_CALORIES_GOAL_CURRENT_VALUE", "").strip() or None
        return self._edit_goal_metric(
            self.CALORIES_GOAL_METRIC_LABEL,
            new_value,
            current_value=current_value,
        )

    def edit_kms_goal(self, value: str | None = None) -> str:
        """Open the Kms/Miles goal card and update its `goalValue`."""
        new_value = self._resolve_edit_kms_goal_value(value)
        current_value = os.getenv("CUBII_KMS_GOAL_CURRENT_VALUE", "").strip() or None
        return self._edit_goal_metric(
            self.KMS_GOAL_METRIC_LABEL,
            new_value,
            current_value=current_value,
        )

    def edit_time_goal(self, value: str | None = None) -> str:
        """Open the Time goal card and update its `goalValue`."""
        new_value = self._resolve_edit_time_goal_value(value)
        current_value = os.getenv("CUBII_TIME_GOAL_CURRENT_VALUE", "").strip() or None
        return self._edit_goal_metric(
            self.TIME_GOAL_METRIC_LABEL,
            new_value,
            current_value=current_value,
        )

    def _click_if_present(
        self,
        locators: tuple[tuple, ...],
        *,
        label: str,
        timeout: int = 4,
    ) -> bool:
        for locator in locators:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    ec.element_to_be_clickable(locator)
                )
                element.click()
                self.LOGGER.info("Clicked `%s` via `%s`.", label, locator[1])
                return True
            except (TimeoutException, WebDriverException):
                continue
        self.LOGGER.info("`%s` not present; continuing.", label)
        return False

    def tap_goal_ftue_next_button(self) -> None:
        """Tap Next on the goal introduction overlay (`btnNext`)."""
        self.LOGGER.info("Tapping goal FTUE Next button (`btnNext`).")
        self._click_first_clickable(
            self.GOAL_FTUE_NEXT_LOCATORS,
            label="Goal FTUE Next (`btnNext`)",
        )
        time.sleep(float(os.getenv("CUBII_AFTER_GOAL_FTUE_NEXT_SEC", "0.6")))

    def tap_goal_ftue_next_button_if_present(self) -> bool:
        """Tap Next only when goal FTUE `btnNext` is visible; otherwise skip."""
        self.LOGGER.info("Checking goal FTUE Next (`btnNext`) before tap.")
        wait_sec = int(os.getenv("CUBII_GOAL_FTUE_NEXT_WAIT_SEC", "3"))
        if not self.is_goal_ftue_next_present(timeout=wait_sec):
            self.LOGGER.info("Goal FTUE Next (`btnNext`) not present; skipping tap.")
            return False

        tapped = self._click_if_present(
            self.GOAL_FTUE_NEXT_LOCATORS,
            label="Goal FTUE Next (`btnNext`)",
            timeout=wait_sec,
        )
        if tapped:
            time.sleep(float(os.getenv("CUBII_AFTER_GOAL_FTUE_NEXT_SEC", "0.6")))
        return tapped

    def tap_goal_ftue_got_it_button(self) -> None:
        """Tap Got it on the goal introduction overlay (`btnGotIt1`)."""
        self.LOGGER.info("Tapping goal FTUE Got it button (`btnGotIt1`).")
        self._click_first_clickable(
            self.GOAL_FTUE_GOT_IT_LOCATORS,
            label="Goal FTUE Got it (`btnGotIt1`)",
        )
        time.sleep(float(os.getenv("CUBII_AFTER_GOAL_FTUE_GOT_IT_SEC", "0.6")))

    def is_goal_ftue_got_it_present(self, timeout: int = 2) -> bool:
        """True when the goal FTUE Got it control (`btnGotIt1`) is on screen."""
        return self._is_visible(self.GOAL_FTUE_GOT_IT_LOCATORS, timeout=timeout)

    def is_goal_ftue_next_present(self, timeout: int = 2) -> bool:
        """True when the goal FTUE Next control (`btnNext`) is on screen."""
        return self._is_visible(self.GOAL_FTUE_NEXT_LOCATORS, timeout=timeout)

    def tap_goal_ftue_got_it_button_if_present(self) -> bool:
        """Tap Got it only when `btnGotIt1` is visible; otherwise skip."""
        self.LOGGER.info("Checking goal FTUE Got it (`btnGotIt1`) before tap.")
        wait_sec = int(os.getenv("CUBII_GOAL_FTUE_GOT_IT_WAIT_SEC", "3"))
        if not self.is_goal_ftue_got_it_present(timeout=wait_sec):
            self.LOGGER.info("Goal FTUE Got it (`btnGotIt1`) not present; skipping tap.")
            return False

        tapped = self._click_if_present(
            self.GOAL_FTUE_GOT_IT_LOCATORS,
            label="Goal FTUE Got it (`btnGotIt1`)",
            timeout=wait_sec,
        )
        if tapped:
            time.sleep(float(os.getenv("CUBII_AFTER_GOAL_FTUE_GOT_IT_SEC", "0.6")))
        return tapped

    def verify_goal_introduction_dismissed(self) -> None:
        """Assert the goal FTUE Got it overlay (`btnGotIt1`) is no longer shown."""
        if self.is_goal_ftue_got_it_present(timeout=2):
            raise AssertionError(
                "Goal introduction is still visible — "
                "`btnGotIt1` should be dismissed after tapping Got it."
            )
        self.LOGGER.info("Verified goal introduction overlay is dismissed.")

    def verify_goal_introduction_dismissed_if_present(self) -> bool:
        """
        Fail only when `btnGotIt1` is still on screen after the optional Got it tap.

        Skips when the introduction was never shown or was already dismissed.
        """
        if not self.is_goal_ftue_got_it_present(timeout=2):
            self.LOGGER.info(
                "Goal introduction (`btnGotIt1`) not present; skipping dismissal check."
            )
            return False

        raise AssertionError(
            "Goal introduction is still visible — "
            "`btnGotIt1` should be dismissed after tapping Got it."
        )

    def _assert_goal_metric_visible(self, label: str, locators: tuple[tuple, ...]) -> None:
        if self._is_visible(locators, timeout=Settings.EXPLICIT_WAIT):
            self.LOGGER.info("Goal metric %r is visible.", label)
            return
        raise AssertionError(
            f"Goal metric {label!r} is not visible on the add goal screen."
        )

    def verify_goal_metrics(self) -> None:
        """Assert Strides, Calories, Miles, and Time are shown on the add goal screen."""
        self.LOGGER.info(
            "Verifying goal metrics: %s.",
            ", ".join(self.GOAL_METRIC_LABELS),
        )

        strides_locators = (
            *self.STRIDES_GOAL_CARD_LOCATORS,
            *self._goal_metric_text_locators(self.STRIDES_GOAL_METRIC_LABEL),
        )
        self._assert_goal_metric_visible(self.STRIDES_GOAL_METRIC_LABEL, strides_locators)
        self._assert_goal_metric_visible(
            self.CALORIES_GOAL_METRIC_LABEL,
            self._goal_metric_text_locators(self.CALORIES_GOAL_METRIC_LABEL),
        )
        self._assert_goal_metric_visible(
            f"{self.MILES_GOAL_METRIC_LABEL}/{self.KMS_GOAL_METRIC_LABEL}",
            self._miles_or_kms_goal_metric_locators(),
        )
        self._assert_goal_metric_visible(
            self.TIME_GOAL_METRIC_LABEL,
            self._goal_metric_text_locators(self.TIME_GOAL_METRIC_LABEL),
        )
        self.LOGGER.info("All goal metrics verified: Strides, Calories, Miles, Time.")

    @classmethod
    def _goal_cancel_close_locators(cls, index: int = 0) -> tuple[tuple, ...]:
        """Build locators for a goal card cancel/close (X) control by list index."""
        if index < 0:
            raise ValueError(f"Goal cancel close index must be >= 0, got {index}.")
        xpath_index = index + 1
        locators: list[tuple] = [
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                (
                    f'new UiSelector().resourceId("{cls.GOAL_CANCEL_CLOSE_BUTTON_ID}")'
                    f".instance({index})"
                ),
            ),
            (
                AppiumBy.XPATH,
                (
                    f'(//android.widget.ImageView[@resource-id="'
                    f'{cls.GOAL_CANCEL_CLOSE_BUTTON_ID}"])[{xpath_index}]'
                ),
            ),
        ]
        if index == 0:
            locators.append((AppiumBy.ID, cls.GOAL_CANCEL_CLOSE_BUTTON_ID))
        return tuple(locators)

    def tap_goal_cancel_option(self, index: int = 0) -> None:
        """Tap cancel/close (X) on a goal card (`close`) at the given index."""
        self.LOGGER.info(
            "Tapping goal cancel option (`close`) at index %s on add goal screen.",
            index,
        )
        locators = self._goal_cancel_close_locators(index)
        self._click_first_clickable(
            locators,
            label=f"Goal cancel close (`close`) index {index}",
        )
        time.sleep(float(os.getenv("CUBII_AFTER_GOAL_CANCEL_TAP_SEC", "0.6")))

    def tap_goal_metric(self, label: str, *, extra_locators: tuple[tuple, ...] = ()) -> None:
        """Tap a goal metric option on the add goal screen (e.g. Calories, Miles)."""
        self.LOGGER.info("Tapping %r goal metric on add goal screen.", label)
        locators = (*extra_locators, *self._goal_metric_text_locators(label))
        self._click_first_clickable(
            locators,
            label=f"{label} goal metric",
        )
        time.sleep(float(os.getenv("CUBII_AFTER_GOAL_METRIC_TAP_SEC", "0.6")))

    def tap_strides_goal_metric(self) -> None:
        """Tap the Strides goal type card on the add goal screen."""
        self.tap_goal_metric(
            self.STRIDES_GOAL_METRIC_LABEL,
            extra_locators=self.STRIDES_GOAL_CARD_LOCATORS,
        )

    def tap_calories_goal_metric(self) -> None:
        """Tap the Calories goal metric on the add goal screen."""
        self.tap_goal_metric(self.CALORIES_GOAL_METRIC_LABEL)

    def tap_miles_goal_metric(self) -> None:
        """Tap the Miles/Kms goal metric on the add goal screen."""
        self.LOGGER.info("Tapping Miles/Kms goal metric on add goal screen.")
        self._click_first_clickable(
            self._miles_or_kms_goal_metric_locators(),
            label="Miles/Kms goal metric",
        )
        time.sleep(float(os.getenv("CUBII_AFTER_GOAL_METRIC_TAP_SEC", "0.6")))

    def tap_time_goal_metric(self) -> None:
        """Tap the Time goal metric on the add goal screen."""
        self.tap_goal_metric(self.TIME_GOAL_METRIC_LABEL)

    def _read_visible_text(self, locators: tuple[tuple, ...]) -> str:
        for locator in locators:
            for element in self._find_elements_safe(locator):
                try:
                    if not element.is_displayed():
                        continue
                    text = (element.text or element.get_attribute("text") or "").strip()
                    if text:
                        return text
                except WebDriverException:
                    continue
        return ""

    def _find_visible_element(self, locators: tuple[tuple, ...]):
        for locator in locators:
            for element in self._find_elements_safe(locator):
                try:
                    if element.is_displayed():
                        return element
                except WebDriverException:
                    continue
        return None

    def _wait_for_save_changes_popup_text(
        self,
        locators: tuple[tuple, ...],
        *,
        label: str,
        expected_text: str,
        timeout: int | None = None,
    ) -> str:
        """Wait for a Save Changes popup text field by resource id and/or text."""
        wait_sec = timeout or int(
            os.getenv("CUBII_SAVE_CHANGES_POPUP_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )
        pause = float(os.getenv("CUBII_SAVE_CHANGES_POPUP_POLL_SEC", "0.4"))
        deadline = time.time() + wait_sec
        last_seen = ""

        while time.time() < deadline:
            for locator in locators:
                for element in self._find_elements_safe(locator):
                    try:
                        text = (element.text or element.get_attribute("text") or "").strip()
                        if text:
                            last_seen = text
                        if text and expected_text in text:
                            if element.is_displayed() or text == expected_text:
                                self.LOGGER.info(
                                    "Save Changes popup field %s matched %r via `%s`.",
                                    label,
                                    text,
                                    locator[1],
                                )
                                return text
                    except WebDriverException:
                        continue
            time.sleep(pause)

        raise AssertionError(
            f"{label} is not visible on the Save Changes popup. "
            f"Expected text containing {expected_text!r}"
            + (f", last seen {last_seen!r}" if last_seen else ".")
        )

    def _wait_for_save_changes_popup_control(
        self,
        locators: tuple[tuple, ...],
        *,
        label: str,
        timeout: int | None = None,
    ) -> None:
        """Wait for a Save Changes popup button/control to become interactable."""
        wait_sec = timeout or int(
            os.getenv("CUBII_SAVE_CHANGES_POPUP_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )
        pause = float(os.getenv("CUBII_SAVE_CHANGES_POPUP_POLL_SEC", "0.4"))
        deadline = time.time() + wait_sec

        while time.time() < deadline:
            element = self._find_visible_element(locators)
            if element is not None:
                self.LOGGER.info("Save Changes popup control visible: %s.", label)
                return
            for locator in locators:
                try:
                    WebDriverWait(self.driver, 1).until(
                        ec.presence_of_element_located(locator)
                    )
                    self.LOGGER.info(
                        "Save Changes popup control present in hierarchy: %s via `%s`.",
                        label,
                        locator[1],
                    )
                    return
                except TimeoutException:
                    continue
            time.sleep(pause)

        raise AssertionError(f"{label} is not visible on the Save Changes popup.")

    def verify_strides_goal_details(self) -> None:
        """Assert the Strides goal detail card, title, value, and days label."""
        self.LOGGER.info("Verifying Strides goal details on the add goal screen.")

        if not self._is_visible(self.STRIDES_GOAL_DETAIL_CARD_LOCATORS, timeout=Settings.EXPLICIT_WAIT):
            raise AssertionError(
                "Strides goal detail card was not visible in `goalRecyclerView`."
            )
        self.LOGGER.info("Strides goal detail card is visible.")

        title_text = self._read_visible_text(self.GOAL_TITLE_LOCATORS)
        if title_text != self.STRIDES_GOAL_METRIC_LABEL:
            raise AssertionError(
                f"Strides goal title expected {self.STRIDES_GOAL_METRIC_LABEL!r}, "
                f"got {title_text!r} (`goalTitle`)."
            )
        self.LOGGER.info("Strides goal title verified (`goalTitle`).")

        value_element = self._find_visible_element(self.GOAL_VALUE_LOCATORS)
        if value_element is None:
            raise AssertionError(
                "Strides goal value input (`goalValue`) is not visible."
            )
        value_text = (value_element.text or value_element.get_attribute("text") or "").strip()
        if not value_text:
            raise AssertionError("Strides goal value input (`goalValue`) is empty.")
        if not re.search(r"\d", value_text):
            raise AssertionError(
                f"Strides goal value (`goalValue`) should contain a number; got {value_text!r}."
            )
        self.LOGGER.info("Strides goal value verified (`goalValue`=%r).", value_text)

        days_text = self._read_visible_text(self.GOAL_DAYS_TITLE_LOCATORS)
        expected_days_text = os.getenv(
            "CUBII_STRIDES_GOAL_DAYS_TITLE_TEXT",
            self.GOAL_DAYS_TITLE_TEXT,
        ).strip()
        if days_text != expected_days_text:
            raise AssertionError(
                f"Strides goal days label expected {expected_days_text!r}, "
                f"got {days_text!r} (`goal_days_title`)."
            )
        self.LOGGER.info(
            "Strides goal days label verified (`goal_days_title`=%r).",
            days_text,
        )
        self.LOGGER.info("Strides goal details verification passed.")

    def _hide_keyboard_after_goal_value_entry(self) -> None:
        try:
            self.driver.hide_keyboard()
            time.sleep(float(os.getenv("CUBII_AFTER_HIDE_KEYBOARD_SEC", "0.4")))
            self.LOGGER.info("Soft keyboard hidden after goal value entry.")
        except Exception as exc:
            self.LOGGER.debug("hide_keyboard failed after goal value entry: %s", exc)

    @staticmethod
    def _goal_values_match(expected: str, observed: str) -> bool:
        if observed == expected:
            return True
        try:
            return abs(float(observed) - float(expected)) < 1e-6
        except ValueError:
            return False

    def _enter_goal_value(self, value: str, *, metric_label: str) -> None:
        """Enter a goal value in `goalValue` for the selected metric."""
        goal_value = value.strip()
        if not goal_value:
            raise AssertionError(f"{metric_label} goal value to enter must not be empty.")

        self.LOGGER.info(
            "Entering %s goal value %r in `goalValue`.",
            metric_label,
            goal_value,
        )
        field = self._find_goal_value_field_for_metric_card(metric_label)
        if field is None:
            for locator in self.GOAL_VALUE_LOCATORS:
                try:
                    field = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT).until(
                        ec.element_to_be_clickable(locator)
                    )
                    self.LOGGER.info("Goal value field located via `%s`.", locator[1])
                    break
                except TimeoutException:
                    continue

        if field is None:
            raise AssertionError(
                f"{metric_label} goal value input (`goalValue`) not found."
            )

        observed = self._set_goal_value_on_field(
            field,
            goal_value,
            metric_label=metric_label,
        )
        self.LOGGER.info(
            "%s goal value set to %r (`goalValue`).",
            metric_label,
            observed,
        )

    def enter_strides_goal_value(self, value: str | None = None) -> None:
        """Enter a Strides goal in `goalValue` (default 100)."""
        goal_value = (value or os.getenv("CUBII_STRIDES_GOAL_VALUE", "100")).strip()
        self._enter_goal_value(goal_value, metric_label=self.STRIDES_GOAL_METRIC_LABEL)

    def enter_calories_goal_value(self, value: str | None = None) -> None:
        """Enter a Calories goal in `goalValue` (default 0.1)."""
        goal_value = (value or os.getenv("CUBII_CALORIES_GOAL_VALUE", "0.1")).strip()
        self._enter_goal_value(goal_value, metric_label=self.CALORIES_GOAL_METRIC_LABEL)

    def enter_miles_goal_value(self, value: str | None = None) -> None:
        """Enter a Miles goal in `goalValue` (default 0.1)."""
        goal_value = (value or os.getenv("CUBII_MILES_GOAL_VALUE", "0.1")).strip()
        self._enter_goal_value(goal_value, metric_label=self.MILES_GOAL_METRIC_LABEL)

    def enter_time_goal_value(self, value: str | None = None) -> None:
        """Enter a Time goal in `goalValue` (default 1)."""
        goal_value = (value or os.getenv("CUBII_TIME_GOAL_VALUE", "1")).strip()
        self._enter_goal_value(goal_value, metric_label=self.TIME_GOAL_METRIC_LABEL)

    def tap_save_goals_button(self) -> None:
        """Tap SAVE GOALS (`btnSave`) on the add goal screen."""
        self.LOGGER.info("Tapping SAVE GOALS button (`btnSave`).")
        self._click_first_clickable(
            self.SAVE_GOALS_BUTTON_LOCATORS,
            label="SAVE GOALS (`btnSave`)",
        )
        time.sleep(float(os.getenv("CUBII_AFTER_SAVE_GOALS_TAP_SEC", "0.8")))

    def _done_button_on_screen(self) -> bool:
        if self._find_first_in_viewport(self.DONE_BUTTON_LOCATORS) is not None:
            return True
        return self._is_visible(self.DONE_BUTTON_LOCATORS, timeout=1)

    def _scroll_to_done_button(self) -> None:
        """Scroll down on the Edit/Add Goal screen until Done (`btnDone`) is visible."""
        if self._done_button_on_screen():
            self.LOGGER.info("Done button (`btnDone`) already on screen.")
            return

        pause = float(os.getenv("CUBII_GOALS_SCROLL_PAUSE_SEC", "0.5"))
        percent = float(os.getenv("CUBII_GOALS_EDIT_SCREEN_SCROLL_PERCENT", "0.7"))
        max_scrolls = int(os.getenv("CUBII_GOALS_DONE_SCROLL_ATTEMPTS", "8"))

        for attempt in range(1, max_scrolls + 1):
            self.LOGGER.info(
                "Done button not visible; scrolling Edit Goal screen down (%s/%s).",
                attempt,
                max_scrolls,
            )
            self._scroll_add_goal_screen_down(percent=percent)
            time.sleep(pause)
            if self._done_button_on_screen():
                self.LOGGER.info(
                    "Done button visible after %s scroll-down gesture(s).",
                    attempt,
                )
                return

        raise AssertionError(
            "Done button (`btnDone`) was not found after scrolling down on the "
            "Edit Goal screen."
        )

    def _wait_after_done_for_home(self) -> None:
        """Pause after Done so the home screen can refresh saved goals."""
        wait_sec = float(os.getenv("CUBII_AFTER_DONE_BUTTON_TAP_SEC", "3.0"))
        self.LOGGER.info(
            "Waiting %ss after Done (`btnDone`) for home screen to update.",
            wait_sec,
        )
        time.sleep(wait_sec)
        self.ensure_home_tab_selected()

        ready_timeout = int(os.getenv("CUBII_AFTER_DONE_HOME_READY_SEC", "10"))
        deadline = time.time() + ready_timeout
        while time.time() < deadline:
            if self._todays_goals_on_screen():
                self.LOGGER.info(
                    "Today's Goals is visible on home after Done (within %ss).",
                    ready_timeout,
                )
                return
            time.sleep(0.5)

        self.LOGGER.info(
            "Today's Goals not visible within %ss after Done; continuing.",
            ready_timeout,
        )

    def tap_done_button(self) -> None:
        """Scroll to and tap Done (`btnDone`) on the Edit Goal screen."""
        self.LOGGER.info("Tapping Done button (`btnDone`) on Edit Goal screen.")
        self._scroll_to_done_button()
        self._click_first_clickable(
            self.DONE_BUTTON_LOCATORS,
            label="Done (`btnDone`)",
        )
        self._wait_after_done_for_home()

    @classmethod
    def _home_goal_card_locators(cls, card_index: int) -> tuple[tuple, ...]:
        xpath_index = card_index + 1
        return (
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                (
                    f'new UiSelector().resourceId("{cls.HOME_GOAL_CARD_LAYOUT_ID}")'
                    f".instance({card_index})"
                ),
            ),
            (
                AppiumBy.XPATH,
                (
                    f'(//android.view.ViewGroup[@resource-id="'
                    f'{cls.HOME_GOAL_CARD_LAYOUT_ID}"])[{xpath_index}]'
                ),
            ),
        )

    @classmethod
    def _home_goal_text_locators(cls, card_index: int) -> tuple[tuple, ...]:
        xpath_index = card_index + 1
        return (
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                (
                    f'new UiSelector().resourceId("{cls.HOME_GOAL_TEXT_ID}")'
                    f".instance({card_index})"
                ),
            ),
            (
                AppiumBy.XPATH,
                (
                    f'(//android.view.ViewGroup[@resource-id="'
                    f'{cls.HOME_GOAL_CARD_LAYOUT_ID}"])[{xpath_index}]'
                    f'//*[@resource-id="{cls.HOME_GOAL_TEXT_ID}"]'
                ),
            ),
            (AppiumBy.ID, cls.HOME_GOAL_TEXT_ID),
        )

    def _parse_home_goal_display_value(
        self,
        metric_label: str,
        texts: list[str],
    ) -> str | None:
        """Extract the goal target from home Today's Goals card copy."""
        combined = " ".join(texts)
        pattern_groups: dict[str, tuple[str, ...]] = {
            self.STRIDES_GOAL_METRIC_LABEL: (
                r"Pedal\s+(\d+\.?\d*)\s+Strides",
                r"(\d+\.?\d*)\s+Strides",
            ),
            self.CALORIES_GOAL_METRIC_LABEL: (
                r"Burn\s+(\d+\.?\d*)\s+Calories",
                r"(\d+\.?\d*)\s+Calories",
            ),
            self.KMS_GOAL_METRIC_LABEL: (
                r"Reach\s+(\d+\.?\d*)\s+Kms",
                r"Reach\s+(\d+\.?\d*)\s+Miles",
                r"(\d+\.?\d*)\s+Kms",
                r"(\d+\.?\d*)\s+Miles",
            ),
            self.MILES_GOAL_METRIC_LABEL: (
                r"Reach\s+(\d+\.?\d*)\s+Miles",
                r"Reach\s+(\d+\.?\d*)\s+Kms",
                r"(\d+\.?\d*)\s+Miles",
                r"(\d+\.?\d*)\s+Kms",
            ),
            self.TIME_GOAL_METRIC_LABEL: (
                r"Workout for\s+(\d+\.?\d*)\s+Minute",
                r"Workout for\s+(\d+\.?\d*)\s+Minutes",
                r"(\d+\.?\d*)\s+Minute",
                r"(\d+\.?\d*)\s+Minutes",
            ),
        }
        patterns = pattern_groups.get(metric_label, ())
        for pattern in patterns:
            match = re.search(pattern, combined, re.IGNORECASE)
            if match:
                return match.group(1)
        return None

    def _home_goal_display_matches_expected(
        self,
        metric_label: str,
        expected: str,
        texts: list[str],
    ) -> bool:
        parsed_value = self._parse_home_goal_display_value(metric_label, texts)
        if parsed_value and self._goal_values_match(expected, parsed_value):
            self.LOGGER.info(
                "%s home goal parsed as %r from texts=%r.",
                metric_label,
                parsed_value,
                texts,
            )
            return True
        return self._home_goal_value_present(expected, texts)

    def _home_goal_card_has_metric_label(self, metric_label: str, texts: list[str]) -> bool:
        combined = " ".join(texts).lower()
        if metric_label == self.TIME_GOAL_METRIC_LABEL:
            return (
                "minute" in combined
                or "workout for" in combined
                or "time" in combined
            )
        for label in self._goal_metric_title_labels(metric_label):
            if label.lower() in combined:
                return True
        return False

    def _home_goal_value_present(self, expected: str, texts: list[str]) -> bool:
        expected = expected.strip()
        if not expected or not texts:
            return False

        candidates = list(texts)
        candidates.append(" ".join(texts))
        for observed in candidates:
            observed = observed.strip()
            if not observed:
                continue
            if self._goal_values_match(expected, observed):
                return True
            if expected in observed:
                return True
            for token in re.findall(r"\d+\.?\d*", observed):
                if self._goal_values_match(expected, token):
                    return True
            slash_match = re.search(r"(\d+\.?\d*)\s*/\s*(\d+\.?\d*)", observed)
            if slash_match:
                for group in slash_match.groups():
                    if self._goal_values_match(expected, group):
                        return True
        return False

    def _visible_home_goal_card_indexes(self) -> list[int]:
        visible_count = 0
        for element in self._find_elements_safe(
            (AppiumBy.ID, self.HOME_GOAL_CARD_LAYOUT_ID)
        ):
            try:
                if element.is_displayed():
                    visible_count += 1
            except WebDriverException:
                continue
        if visible_count <= 0:
            return [index for _, index in self.HOME_GOAL_CARD_METRICS]
        return list(range(visible_count))

    def _read_home_goal_card_texts(self, card_index: int) -> list[str]:
        """Read all visible TextView strings inside a Today's Goals home card."""
        texts: list[str] = []
        seen: set[str] = set()
        xpath_index = card_index + 1
        card_locators = (
            (
                AppiumBy.XPATH,
                (
                    f'(//android.view.ViewGroup[@resource-id="'
                    f'{self.HOME_GOAL_CARD_LAYOUT_ID}"])[{xpath_index}]'
                ),
            ),
            *self._home_goal_card_locators(card_index),
        )

        for locator in card_locators:
            for card in self._find_elements_safe(locator):
                try:
                    if not card.is_displayed():
                        continue
                    nodes = card.find_elements(
                        AppiumBy.XPATH,
                        ".//android.widget.TextView",
                    )
                    for node in nodes:
                        text = (node.text or node.get_attribute("text") or "").strip()
                        if text and text not in seen:
                            seen.add(text)
                            texts.append(text)
                except WebDriverException:
                    continue
            if texts:
                break

        if not texts:
            goal_text = self._read_visible_text(self._home_goal_text_locators(card_index))
            if goal_text:
                texts.append(goal_text)

        return texts

    def _read_home_goal_card_text(self, card_index: int) -> str:
        texts = self._read_home_goal_card_texts(card_index)
        return " | ".join(texts)

    def _scroll_home_to_goal_card(self, card_index: int) -> bool:
        """Scroll home screen down until a Today's Goals card is present."""
        metric_label = next(
            (label for label, index in self.HOME_GOAL_CARD_METRICS if index == card_index),
            f"index {card_index}",
        )
        escaped_layout_id = self.HOME_GOAL_CARD_LAYOUT_ID
        scroll_locators = (
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                (
                    "new UiScrollable(new UiSelector().scrollable(true))"
                    f'.scrollIntoView(new UiSelector().resourceId("{escaped_layout_id}")'
                    f".instance({card_index}))"
                ),
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                (
                    f'new UiScrollable(new UiSelector().resourceId("{escaped_layout_id}"))'
                    f'.scrollIntoView(new UiSelector().resourceId("{self.HOME_GOAL_TEXT_ID}")'
                    f".instance({card_index}))"
                ),
            ),
        )
        for locator in scroll_locators:
            try:
                WebDriverWait(self.driver, 5).until(
                    ec.presence_of_element_located(locator)
                )
                self.LOGGER.info(
                    "Scrolled home Today's Goals card for %r into view.",
                    metric_label,
                )
                return True
            except TimeoutException:
                continue
        return False

    def _find_home_goal_card_texts_for_metric(self, metric_label: str) -> list[str]:
        """Read a Today's Goals home card for a metric without scrolling."""
        preferred_index = next(
            (index for label, index in self.HOME_GOAL_CARD_METRICS if label == metric_label),
            None,
        )
        card_indexes: list[int] = []
        if preferred_index is not None:
            card_indexes.append(preferred_index)
        card_indexes.extend(
            index
            for index in self._visible_home_goal_card_indexes()
            if index not in card_indexes
        )

        for card_index in card_indexes:
            texts = self._read_home_goal_card_texts(card_index)
            if not texts:
                continue
            if (
                self._home_goal_card_has_metric_label(metric_label, texts)
                or self._parse_home_goal_display_value(metric_label, texts)
            ):
                self.LOGGER.info(
                    "Resolved %s home goal card at index %s with texts=%r.",
                    metric_label,
                    card_index,
                    texts,
                )
                return texts

        return []

    def verify_updated_goals_on_home(self, expected_values: dict[str, str]) -> None:
        """Assert Today's Goals on home show the values saved from the edit flow."""
        key_by_metric = {
            self.STRIDES_GOAL_METRIC_LABEL: "strides",
            self.CALORIES_GOAL_METRIC_LABEL: "calories",
            self.KMS_GOAL_METRIC_LABEL: "kms",
            self.MILES_GOAL_METRIC_LABEL: "kms",
            self.TIME_GOAL_METRIC_LABEL: "time",
        }

        self.LOGGER.info(
            "Verifying updated goals on home screen (`goalText`) after Done — wait only, no scroll."
        )
        time.sleep(float(os.getenv("CUBII_AFTER_DONE_HOME_GOAL_REFRESH_SEC", "3.0")))

        if not self._todays_goals_on_screen():
            raise AssertionError(
                "Today's Goals section is not visible on the home screen after Done."
            )
        self.LOGGER.info("Today's Goals section is visible on home screen.")

        for metric_label, card_index in self.HOME_GOAL_CARD_METRICS:
            value_key = key_by_metric[metric_label]
            expected = (expected_values.get(value_key) or "").strip()
            if not expected:
                raise AssertionError(
                    f"Missing expected {metric_label} goal value from edit steps "
                    f"(context key {value_key!r})."
                )

            observed_texts = self._find_home_goal_card_texts_for_metric(metric_label)
            if not observed_texts:
                raise AssertionError(
                    f"{metric_label} goal text (`goalText`) was not visible on the home "
                    f"screen at card index {card_index}."
                )
            if not self._home_goal_card_has_metric_label(metric_label, observed_texts):
                raise AssertionError(
                    f"{metric_label} goal card at index {card_index} does not contain the "
                    f"expected metric label. Observed texts: {observed_texts!r}."
                )
            if not self._home_goal_display_matches_expected(
                metric_label,
                expected,
                observed_texts,
            ):
                raise AssertionError(
                    f"{metric_label} goal on home does not match edited value. "
                    f"Expected {expected!r}, observed home texts {observed_texts!r} "
                    f"(`goalText` on Today's Goals)."
                )
            self.LOGGER.info(
                "%s goal verified on home (texts=%r).",
                metric_label,
                observed_texts,
            )

        self.LOGGER.info("All updated goals verified on home screen.")

    @classmethod
    def _goal_metric_title_labels(cls, metric_label: str) -> tuple[str, ...]:
        if metric_label in (cls.MILES_GOAL_METRIC_LABEL, cls.KMS_GOAL_METRIC_LABEL):
            return (cls.MILES_GOAL_METRIC_LABEL, cls.KMS_GOAL_METRIC_LABEL)
        return (metric_label,)

    def _goal_metric_title_candidates(self, metric_label: str) -> list:
        """Goal detail card titles (`goalTitle`) for a metric — not top metric tiles."""
        candidates = []
        seen_ids: set[str] = set()
        for label in self._goal_metric_title_labels(metric_label):
            for element in self._find_elements_safe((AppiumBy.ID, self.GOAL_TITLE_ID)):
                try:
                    element_id = element.id
                    if element_id in seen_ids:
                        continue
                    if not element.is_displayed():
                        continue
                    text = (element.text or element.get_attribute("text") or "").strip()
                    if text != label:
                        continue
                    seen_ids.add(element_id)
                    candidates.append(element)
                except WebDriverException:
                    continue
        return candidates

    def _scroll_goal_metric_card_into_view(self, metric_label: str) -> bool:
        """Scroll `goalRecyclerView` until the metric goal card title is present."""
        escaped_labels = [
            label.replace('"', '\\"')
            for label in self._goal_metric_title_labels(metric_label)
        ]
        scroll_locators = []
        for escaped in escaped_labels:
            scroll_locators.extend(
                (
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        (
                            f'new UiScrollable(new UiSelector().resourceId("{self.GOAL_RECYCLER_VIEW_ID}"))'
                            f'.scrollIntoView(new UiSelector().resourceId("{self.GOAL_TITLE_ID}")'
                            f'.text("{escaped}"))'
                        ),
                    ),
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        (
                            'new UiScrollable(new UiSelector().scrollable(true))'
                            f'.scrollIntoView(new UiSelector().resourceId("{self.GOAL_TITLE_ID}")'
                            f'.text("{escaped}"))'
                        ),
                    ),
                )
            )

        for locator in scroll_locators:
            try:
                WebDriverWait(self.driver, 5).until(
                    ec.presence_of_element_located(locator)
                )
                self.LOGGER.info(
                    "Scrolled %r goal card into view via UiScrollable.",
                    metric_label,
                )
                return True
            except TimeoutException:
                continue
        return False

    def _read_goal_metric_validation_error(self, metric_label: str) -> str | None:
        """Return validation text near a visible goal card title, if present."""
        expected_message = os.getenv(
            "CUBII_GOAL_VALUE_VALIDATION_MESSAGE",
            self.GOAL_VALUE_VALIDATION_MESSAGE,
        ).strip()
        max_distance = int(os.getenv("CUBII_GOAL_VALIDATION_ERROR_MAX_Y_OFFSET", "600"))

        for title in self._goal_metric_title_candidates(metric_label):
            try:
                title_y = title.location["y"]
                title_bottom = title_y + title.size["height"]
            except WebDriverException:
                continue

            for element in self._find_elements_safe(
                (AppiumBy.ID, self.GOAL_VALUE_ERROR_TEXT_ID)
            ):
                try:
                    if not element.is_displayed():
                        continue
                    error_y = element.location["y"]
                    if error_y < title_bottom or error_y - title_y > max_distance:
                        continue
                    text = (element.text or element.get_attribute("text") or "").strip()
                    if expected_message in text:
                        return text
                except WebDriverException:
                    continue

        for element in self._find_elements_safe(self.GOAL_VALUE_ERROR_TEXT_LOCATORS):
            try:
                if not element.is_displayed():
                    continue
                if not self._element_center_in_viewport(element):
                    continue
                text = (element.text or element.get_attribute("text") or "").strip()
                if expected_message in text:
                    return text
            except WebDriverException:
                continue
        return None

    def _scroll_add_goal_screen_down(self, percent: float = 0.7) -> None:
        """Scroll down on the Add/Edit Goal screen."""
        self._scroll_home_down(percent=percent)
        self.LOGGER.info(
            "Performed Add/Edit Goal screen scroll-down gesture (percent=%s).",
            percent,
        )

    def verify_goal_metric_validation(self, metric_label: str) -> None:
        """Scroll down and assert the goal metric card shows `txtTimeErrorText`."""
        expected_message = os.getenv(
            "CUBII_GOAL_VALUE_VALIDATION_MESSAGE",
            self.GOAL_VALUE_VALIDATION_MESSAGE,
        ).strip()
        self.LOGGER.info(
            "Scrolling down to verify %s validation error (`txtTimeErrorText`=%r).",
            metric_label,
            expected_message,
        )

        pause = float(os.getenv("CUBII_GOALS_SCROLL_PAUSE_SEC", "0.5"))
        percent = float(os.getenv("CUBII_GOALS_EDIT_SCREEN_SCROLL_PERCENT", "0.7"))
        max_scrolls = int(os.getenv("CUBII_GOAL_VALIDATION_SCROLL_ATTEMPTS", "12"))

        self._scroll_goal_metric_card_into_view(metric_label)
        time.sleep(pause)

        for attempt in range(max_scrolls + 1):
            matched_text = self._read_goal_metric_validation_error(metric_label)
            if matched_text is not None:
                self.LOGGER.info(
                    "%s validation error verified (`txtTimeErrorText`=%r) after %s scroll(s).",
                    metric_label,
                    matched_text,
                    attempt,
                )
                return

            if attempt >= max_scrolls:
                break

            self.LOGGER.info(
                "%s validation not visible yet; scrolling to find error (%s/%s).",
                metric_label,
                attempt + 1,
                max_scrolls,
            )
            if not self._scroll_goal_metric_card_into_view(metric_label):
                self._scroll_add_goal_screen_down(percent=percent)
            time.sleep(pause)

        raise AssertionError(
            f"{metric_label} validation error (`txtTimeErrorText`) was not found after "
            f"scrolling down on the Add Goal screen. Expected message containing "
            f"{expected_message!r}."
        )

    def verify_strides_goal_validation(self) -> None:
        """Assert strides goal value validation error is shown after SAVE GOALS."""
        self.verify_goal_metric_validation(self.STRIDES_GOAL_METRIC_LABEL)

    def verify_calories_goal_validation(self) -> None:
        """Assert calories goal value validation error is shown after SAVE GOALS."""
        self.verify_goal_metric_validation(self.CALORIES_GOAL_METRIC_LABEL)

    def verify_kms_goal_validation(self) -> None:
        """Assert Kms/Miles goal value validation error is shown after SAVE GOALS."""
        self.verify_goal_metric_validation(self.KMS_GOAL_METRIC_LABEL)

    def verify_time_goal_validation(self) -> None:
        """Assert time goal value validation error is shown after SAVE GOALS."""
        self.verify_goal_metric_validation(self.TIME_GOAL_METRIC_LABEL)

    def tap_goals_back_button(self) -> None:
        """Tap the Add/Edit Goal toolbar back button (`Navigate up`)."""
        self.LOGGER.info("Tapping goals screen back button (`Navigate up`).")
        scroll_up_attempts = int(os.getenv("CUBII_GOALS_BACK_SCROLL_UP_ATTEMPTS", "2"))
        for _ in range(scroll_up_attempts):
            self._scroll_home(direction="up", percent=0.5)
            time.sleep(0.3)
        self._click_first_clickable(
            self.GOALS_BACK_BUTTON_LOCATORS,
            label="Goals back (`Navigate up`)",
        )
        time.sleep(float(os.getenv("CUBII_AFTER_GOALS_BACK_TAP_SEC", "1.2")))

    def verify_save_changes_popup_visible(self) -> None:
        """Assert the Save Changes confirmation popup is shown."""
        self.LOGGER.info("Verifying Save Changes popup on the Add Goal screen.")
        wait_sec = int(
            os.getenv("CUBII_SAVE_CHANGES_POPUP_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )

        title_text = self._wait_for_save_changes_popup_text(
            self.SAVE_CHANGES_POPUP_TITLE_LOCATORS,
            label="Save Changes title (`textView68`)",
            expected_text=self.SAVE_CHANGES_POPUP_TITLE_TEXT,
            timeout=wait_sec,
        )
        message_text = self._wait_for_save_changes_popup_text(
            self.SAVE_CHANGES_POPUP_MESSAGE_LOCATORS,
            label="Save Changes message (`textView69`)",
            expected_text=self.SAVE_CHANGES_POPUP_MESSAGE_TEXT,
            timeout=wait_sec,
        )
        self._wait_for_save_changes_popup_control(
            self.SAVE_CHANGES_POPUP_NO_BUTTON_LOCATORS,
            label="Save Changes NO (`btnNo`)",
            timeout=wait_sec,
        )
        self._wait_for_save_changes_popup_control(
            self.SAVE_CHANGES_POPUP_YES_BUTTON_LOCATORS,
            label="Save Changes YES (`btnYes`)",
            timeout=wait_sec,
        )

        if self.SAVE_CHANGES_POPUP_TITLE_TEXT not in title_text:
            raise AssertionError(
                f"Save Changes popup title mismatch. Expected "
                f"{self.SAVE_CHANGES_POPUP_TITLE_TEXT!r}, got {title_text!r}."
            )
        if self.SAVE_CHANGES_POPUP_MESSAGE_TEXT not in message_text:
            raise AssertionError(
                f"Save Changes popup message mismatch. Expected "
                f"{self.SAVE_CHANGES_POPUP_MESSAGE_TEXT!r}, got {message_text!r}."
            )

        self.LOGGER.info(
            "Save Changes popup verified (title=%r, message=%r, NO, YES).",
            title_text,
            message_text[:80],
        )

    def tap_save_changes_popup_no_button(self) -> None:
        """Tap NO (`btnNo`) on the Save Changes confirmation popup."""
        self.LOGGER.info("Tapping NO on Save Changes popup (`btnNo`).")
        self._click_first_clickable(
            self.SAVE_CHANGES_POPUP_NO_BUTTON_LOCATORS,
            label="Save Changes NO (`btnNo`)",
        )
        time.sleep(float(os.getenv("CUBII_AFTER_SAVE_CHANGES_NO_TAP_SEC", "0.8")))

    def open_add_goal_screen(self) -> None:
        """Navigate from Home to the Add Goal screen via Today's Goals."""
        self.scroll_to_todays_goals_section()
        self.verify_todays_goals_section_visible()
        self.tap_add_goal_button()
        self.tap_goal_ftue_next_button_if_present()
        self.tap_goal_ftue_got_it_button_if_present()

    def _count_visible_goal_titles(self) -> int:
        count = 0
        for element in self._find_elements_safe((AppiumBy.ID, self.GOAL_TITLE_ID)):
            try:
                if element.is_displayed():
                    count += 1
            except WebDriverException:
                continue
        return count

    def _delete_all_goals_on_screen(self) -> bool:
        """True when DELETE ALL GOALS (`btnDeleteAll`) is visible on screen."""
        if self._find_first_in_viewport(self.DELETE_ALL_GOALS_BUTTON_LOCATORS) is not None:
            return True
        return self._is_visible(self.DELETE_ALL_GOALS_BUTTON_LOCATORS, timeout=1)

    def _scroll_to_delete_all_goals_button(self) -> None:
        """Scroll down on the Edit/Add Goal screen until DELETE ALL GOALS is visible."""
        if self._delete_all_goals_on_screen():
            self.LOGGER.info("DELETE ALL GOALS (`btnDeleteAll`) already on screen.")
            return

        pause = float(os.getenv("CUBII_GOALS_SCROLL_PAUSE_SEC", "0.5"))
        percent = float(os.getenv("CUBII_GOALS_EDIT_SCREEN_SCROLL_PERCENT", "0.7"))
        max_scrolls = int(os.getenv("CUBII_GOALS_DELETE_ALL_SCROLL_ATTEMPTS", "8"))

        for attempt in range(1, max_scrolls + 1):
            self.LOGGER.info(
                "DELETE ALL GOALS not visible; scrolling Edit Goal screen down (%s/%s).",
                attempt,
                max_scrolls,
            )
            self._scroll_home_down(percent=percent)
            time.sleep(pause)
            if self._delete_all_goals_on_screen():
                self.LOGGER.info(
                    "DELETE ALL GOALS visible after %s scroll-down gesture(s).",
                    attempt,
                )
                return

        raise AssertionError(
            "DELETE ALL GOALS button (`btnDeleteAll`) was not found after scrolling "
            "down on the Edit Goal screen."
        )

    def verify_goals_added_and_present(self) -> None:
        """
        Assert saved goals are shown on the Edit/Add Goal screen before deletion.

        Checks screen title, `goalRecyclerView`, saved goals, and `btnDeleteAll`.
        """
        self.LOGGER.info("Verifying saved goals are present on the Edit/Add Goal screen.")

        if not self._is_visible(
            self.GOAL_EDIT_OR_ADD_SCREEN_TITLE_LOCATORS, timeout=Settings.EXPLICIT_WAIT
        ):
            raise AssertionError(
                "Edit Goal / Add Goal screen title was not found — "
                "expected toolbar text 'Edit Goal' or 'Add Goal'."
            )

        if not self._is_visible(self.GOAL_RECYCLER_VIEW_LOCATORS, timeout=Settings.EXPLICIT_WAIT):
            raise AssertionError(
                "Goals list (`goalRecyclerView`) is not visible on the Edit Goal screen."
            )

        goal_count = self._count_visible_goal_titles()
        min_goals = int(os.getenv("CUBII_MIN_SAVED_GOALS_COUNT", "1"))
        if goal_count < min_goals:
            raise AssertionError(
                f"Expected at least {min_goals} saved goal(s) in `goalRecyclerView`, "
                f"found {goal_count} visible `goalTitle` element(s)."
            )

        self._scroll_to_delete_all_goals_button()

        if not self._delete_all_goals_on_screen():
            raise AssertionError(
                "DELETE ALL GOALS button (`btnDeleteAll`) is not visible at the bottom "
                "of the Edit Goal screen."
            )

        self.LOGGER.info(
            "Verified %s saved goal(s) present and DELETE ALL GOALS is available.",
            goal_count,
        )

    def tap_delete_all_goals_button(self) -> None:
        """Scroll down and tap DELETE ALL GOALS (`btnDeleteAll`) on the Edit Goal screen."""
        self.LOGGER.info(
            "Scrolling down to tap DELETE ALL GOALS (`btnDeleteAll`) on Edit Goal screen."
        )
        if not self._is_visible(
            self.GOAL_EDIT_OR_ADD_SCREEN_TITLE_LOCATORS, timeout=Settings.EXPLICIT_WAIT
        ):
            raise AssertionError(
                "Edit Goal screen was not open before tapping DELETE ALL GOALS."
            )

        self._scroll_to_delete_all_goals_button()
        self._click_first_clickable(
            self.DELETE_ALL_GOALS_BUTTON_LOCATORS,
            label="DELETE ALL GOALS (`btnDeleteAll`)",
        )
        time.sleep(float(os.getenv("CUBII_AFTER_DELETE_ALL_GOALS_TAP_SEC", "0.8")))
        self._confirm_delete_all_goals_if_present()

    def _confirm_delete_all_goals_if_present(self) -> bool:
        """Dismiss a delete confirmation dialog when the app shows one."""
        confirm_locators = (
            (AppiumBy.ID, "com.cubii:id/btnYes"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.cubii:id/btnYes")',
            ),
            (
                AppiumBy.XPATH,
                '//android.widget.Button[@resource-id="com.cubii:id/btnYes"]',
            ),
            (AppiumBy.ID, "android:id/button1"),
            (
                AppiumBy.XPATH,
                '//android.widget.Button[@resource-id="android:id/button1"]',
            ),
        )
        confirmed = self._click_if_present(
            confirm_locators,
            label="Delete all goals confirmation",
            timeout=int(os.getenv("CUBII_DELETE_ALL_GOALS_CONFIRM_WAIT_SEC", "3")),
        )
        if confirmed:
            time.sleep(float(os.getenv("CUBII_AFTER_DELETE_ALL_GOALS_CONFIRM_SEC", "0.8")))
        return confirmed
