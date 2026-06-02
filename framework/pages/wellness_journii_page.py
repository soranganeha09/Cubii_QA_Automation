import logging
import os
import re
import time
from datetime import datetime

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage
from framework.pages.non_ble_connection import NonBleConnectionPage

ANDROID_KEYCODE_BACK = 4


class WellnessJourniiPage(BasePage):
    """Wellness Journii bottom-nav tab and current-month program screen."""

    LOGGER = logging.getLogger("cubii_wellness_journii_page")

    WELLNESS_TAB_CANDIDATE_LOCATORS = (
        (AppiumBy.ACCESSIBILITY_ID, "Wellness Journii"),
        (AppiumBy.ID, "com.cubii:id/navigation_wellness"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.cubii:id/navigation_wellness")',
        ),
        (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Wellness Journii"]'),
    )

    SB_CURRENT_ID = "com.cubii:id/sbCurrent"
    SB_CURRENT_XPATH = '//android.view.View[@resource-id="com.cubii:id/sbCurrent"]'
    SB_CURRENT_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/sbCurrent")'
    SB_CURRENT_LOCATORS = (
        (AppiumBy.ID, SB_CURRENT_ID),
        (AppiumBy.XPATH, SB_CURRENT_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, SB_CURRENT_UIAUTOMATOR),
    )

    SB_PREVIOUS_ID = "com.cubii:id/sbPrevious"
    SB_PREVIOUS_XPATH = '//android.view.View[@resource-id="com.cubii:id/sbPrevious"]'
    SB_PREVIOUS_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/sbPrevious")'
    SB_PREVIOUS_LOCATORS = (
        (AppiumBy.ID, SB_PREVIOUS_ID),
        (AppiumBy.XPATH, SB_PREVIOUS_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, SB_PREVIOUS_UIAUTOMATOR),
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
        (AppiumBy.XPATH, EMPTY_LIST_TEXT_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, EMPTY_LIST_TEXT_UIAUTOMATOR),
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
        (AppiumBy.XPATH, EMPTY_LIST_NORMAL_TEXT_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, EMPTY_LIST_NORMAL_TEXT_UIAUTOMATOR),
    )

    PREVIOUS_EMPTY_TITLE_TEXT = "No Journiis"

    IV_JOURNII_IMAGE_ID = "com.cubii:id/ivJourniiImage"
    IV_JOURNII_IMAGE_XPATH = (
        '//android.widget.ImageView[@resource-id="com.cubii:id/ivJourniiImage"]'
    )
    IV_JOURNII_IMAGE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/ivJourniiImage")'
    )
    IV_JOURNII_IMAGE_LOCATORS = (
        (AppiumBy.ID, IV_JOURNII_IMAGE_ID),
        (AppiumBy.XPATH, IV_JOURNII_IMAGE_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, IV_JOURNII_IMAGE_UIAUTOMATOR),
    )

    TV_WJP_MONTH_TITLE_ID = "com.cubii:id/tvWJPMonthTitle"
    TV_WJP_MONTH_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/tvWJPMonthTitle"]'
    )
    TV_WJP_MONTH_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/tvWJPMonthTitle")'
    )
    TV_WJP_MONTH_TITLE_LOCATORS = (
        (AppiumBy.ID, TV_WJP_MONTH_TITLE_ID),
        (AppiumBy.XPATH, TV_WJP_MONTH_TITLE_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, TV_WJP_MONTH_TITLE_UIAUTOMATOR),
    )

    TV_WJP_MONTH_HIGHLIGHT_ID = "com.cubii:id/tvWJPMonthHighlight"
    TV_WJP_MONTH_HIGHLIGHT_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/tvWJPMonthHighlight"]'
    )
    TV_WJP_MONTH_HIGHLIGHT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/tvWJPMonthHighlight")'
    )
    TV_WJP_MONTH_HIGHLIGHT_LOCATORS = (
        (AppiumBy.ID, TV_WJP_MONTH_HIGHLIGHT_ID),
        (AppiumBy.XPATH, TV_WJP_MONTH_HIGHLIGHT_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, TV_WJP_MONTH_HIGHLIGHT_UIAUTOMATOR),
    )

    TOOLBAR_TITLE_ID = "com.cubii:id/toolbar_title"
    TOOLBAR_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title"]'
    )
    TOOLBAR_TITLE_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/toolbar_title")'
    TOOLBAR_TITLE_LOCATORS = (
        (AppiumBy.ID, TOOLBAR_TITLE_ID),
        (AppiumBy.XPATH, TOOLBAR_TITLE_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, TOOLBAR_TITLE_UIAUTOMATOR),
    )

    TXT_LINK_ID = "com.cubii:id/txtLink"
    TXT_LINK_XPATH = '//android.widget.TextView[@resource-id="com.cubii:id/txtLink"]'
    TXT_LINK_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtLink")'
    TXT_LINK_LOCATORS = (
        (AppiumBy.ID, TXT_LINK_ID),
        (AppiumBy.XPATH, TXT_LINK_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, TXT_LINK_UIAUTOMATOR),
    )

    TV_TITLE_DESC_ICON_ID = "com.cubii:id/tvTitleDescIcon"
    TV_TITLE_DESC_ICON_XPATH = (
        '//android.widget.ImageView[@resource-id="com.cubii:id/tvTitleDescIcon"]'
    )
    TV_TITLE_DESC_ICON_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/tvTitleDescIcon")'
    )
    TV_TITLE_DESC_ICON_LOCATORS = (
        (AppiumBy.ID, TV_TITLE_DESC_ICON_ID),
        (AppiumBy.XPATH, TV_TITLE_DESC_ICON_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, TV_TITLE_DESC_ICON_UIAUTOMATOR),
    )

    DETAIL_BACK_TEXT = "Back"
    DETAIL_TOOLBAR_BACK_XPATH = (
        '//android.view.ViewGroup[@resource-id="com.cubii:id/toolbar"]'
        "/android.widget.LinearLayout"
    )
    DETAIL_TOOLBAR_BACK_UIAUTOMATOR = (
        'new UiSelector().className("android.widget.LinearLayout").instance(2)'
    )
    DETAIL_BACK_XPATH = '//android.widget.TextView[@text="Back"]'
    DETAIL_BACK_UIAUTOMATOR = 'new UiSelector().text("Back")'
    DETAIL_BACK_LOCATORS = (
        (AppiumBy.XPATH, DETAIL_TOOLBAR_BACK_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, DETAIL_TOOLBAR_BACK_UIAUTOMATOR),
        (AppiumBy.XPATH, DETAIL_BACK_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, DETAIL_BACK_UIAUTOMATOR),
        (AppiumBy.ACCESSIBILITY_ID, DETAIL_BACK_TEXT),
    )

    CHROME_URL_BAR_LOCATORS = (
        (AppiumBy.ID, "com.android.chrome:id/url_bar"),
        (AppiumBy.ID, "com.android.chrome:id/search_box_text"),
        (AppiumBy.ID, "com.android.chrome:id/omnibox_url_bar"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.android.chrome:id/url_bar")',
        ),
    )
    CHROME_CUBII_URL_TEXT_UIAUTOMATOR = 'new UiSelector().textContains("cubii.com")'
    CHROME_PACKAGE_HINTS = (
        "com.android.chrome",
        "com.chrome.beta",
        "com.android.browser",
    )
    CUBII_URL_HOST_FRAGMENT = "cubii.com"

    BTN_VIEW_ALL_ID = "com.cubii:id/btnViewAll"
    BTN_VIEW_ALL_XPATH = '//android.widget.Button[@resource-id="com.cubii:id/btnViewAll"]'
    BTN_VIEW_ALL_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btnViewAll")'
    BTN_VIEW_ALL_LOCATORS = (
        (AppiumBy.ID, BTN_VIEW_ALL_ID),
        (AppiumBy.XPATH, BTN_VIEW_ALL_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, BTN_VIEW_ALL_UIAUTOMATOR),
    )

    CV_SHOW_FILTERS_ID = "com.cubii:id/cvShowFilters"
    CV_SHOW_FILTERS_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cvShowFilters"]'
        "/android.widget.LinearLayout"
    )
    CV_SHOW_FILTERS_FRAME_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cvShowFilters"]'
    )
    CV_SHOW_FILTERS_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/cvShowFilters")'
    CV_SHOW_FILTERS_LINEAR_LAYOUT_UIAUTOMATOR = (
        'new UiSelector().className("android.widget.LinearLayout").instance(28)'
    )
    UPCOMING_TASKS_FILTER_TEXT = "FILTERS"
    UPCOMING_TASKS_FILTER_XPATH = '//android.widget.TextView[@text="FILTERS"]'
    UPCOMING_TASKS_FILTER_UIAUTOMATOR = 'new UiSelector().text("FILTERS")'
    UPCOMING_TASKS_FILTER_LOCATORS = (
        (AppiumBy.XPATH, CV_SHOW_FILTERS_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, CV_SHOW_FILTERS_LINEAR_LAYOUT_UIAUTOMATOR),
        (AppiumBy.ANDROID_UIAUTOMATOR, CV_SHOW_FILTERS_UIAUTOMATOR),
        (AppiumBy.XPATH, CV_SHOW_FILTERS_FRAME_XPATH),
        (AppiumBy.ID, CV_SHOW_FILTERS_ID),
        (AppiumBy.XPATH, UPCOMING_TASKS_FILTER_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, UPCOMING_TASKS_FILTER_UIAUTOMATOR),
    )
    CV_SHOW_FILTERS_LOCATORS = UPCOMING_TASKS_FILTER_LOCATORS

    MCV_INCOMPLETE_ID = "com.cubii:id/mcvIncomplete"
    MCV_INCOMPLETE_XPATH = (
        '//androidx.cardview.widget.CardView[@resource-id="com.cubii:id/mcvIncomplete"]'
    )
    MCV_INCOMPLETE_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/mcvIncomplete")'
    MCV_INCOMPLETE_LOCATORS = (
        (AppiumBy.ID, MCV_INCOMPLETE_ID),
        (AppiumBy.XPATH, MCV_INCOMPLETE_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, MCV_INCOMPLETE_UIAUTOMATOR),
    )

    MCV_COMPLETED_ID = "com.cubii:id/mcvCompleted"
    MCV_COMPLETED_XPATH = (
        '//androidx.cardview.widget.CardView[@resource-id="com.cubii:id/mcvCompleted"]'
    )
    MCV_COMPLETED_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/mcvCompleted")'
    MCV_COMPLETED_LOCATORS = (
        (AppiumBy.ID, MCV_COMPLETED_ID),
        (AppiumBy.XPATH, MCV_COMPLETED_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, MCV_COMPLETED_UIAUTOMATOR),
    )

    MCV_ALL_ID = "com.cubii:id/mcvAll"
    MCV_ALL_XPATH = '//androidx.cardview.widget.CardView[@resource-id="com.cubii:id/mcvAll"]'
    MCV_ALL_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/mcvAll")'
    MCV_ALL_LOCATORS = (
        (AppiumBy.ID, MCV_ALL_ID),
        (AppiumBy.XPATH, MCV_ALL_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, MCV_ALL_UIAUTOMATOR),
    )

    BTN_SHOW_RESULTS_ID = "com.cubii:id/btnShowResults"
    BTN_SHOW_RESULTS_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnShowResults"]'
    )
    BTN_SHOW_RESULTS_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnShowResults")'
    )
    BTN_SHOW_RESULTS_LOCATORS = (
        (AppiumBy.ID, BTN_SHOW_RESULTS_ID),
        (AppiumBy.XPATH, BTN_SHOW_RESULTS_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, BTN_SHOW_RESULTS_UIAUTOMATOR),
    )

    FILTER_NO_RESULTS_FOUND_TEXT = "No results found"
    FILTER_NO_RESULTS_FOUND_XPATH = (
        '//android.widget.TextView[@text="No results found"]'
    )
    FILTER_NO_RESULTS_FOUND_UIAUTOMATOR = (
        'new UiSelector().text("No results found")'
    )
    FILTER_NO_RESULTS_FOUND_LOCATORS = (
        (AppiumBy.ANDROID_UIAUTOMATOR, FILTER_NO_RESULTS_FOUND_UIAUTOMATOR),
        (AppiumBy.XPATH, FILTER_NO_RESULTS_FOUND_XPATH),
    )

    FILTER_TRY_REMOVING_FILTERS_TEXT = "Try removing some filters"
    FILTER_TRY_REMOVING_FILTERS_XPATH = (
        '//android.widget.TextView[@text="Try removing some filters"]'
    )
    FILTER_TRY_REMOVING_FILTERS_UIAUTOMATOR = (
        'new UiSelector().text("Try removing some filters")'
    )
    FILTER_TRY_REMOVING_FILTERS_LOCATORS = (
        (AppiumBy.ANDROID_UIAUTOMATOR, FILTER_TRY_REMOVING_FILTERS_UIAUTOMATOR),
        (AppiumBy.XPATH, FILTER_TRY_REMOVING_FILTERS_XPATH),
    )

    BTN_CLEAR_FILTER_ID = "com.cubii:id/btnClearFilter"
    BTN_CLEAR_FILTER_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnClearFilter"]'
    )
    BTN_CLEAR_FILTER_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnClearFilter")'
    )
    BTN_CLEAR_FILTER_LOCATORS = (
        (AppiumBy.ID, BTN_CLEAR_FILTER_ID),
        (AppiumBy.XPATH, BTN_CLEAR_FILTER_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, BTN_CLEAR_FILTER_UIAUTOMATOR),
    )

    JOURNII_DETAIL_BASE_DESCRIPTION_SPECS = (
        ("month title", TV_WJP_MONTH_TITLE_LOCATORS),
        ("month highlight", TV_WJP_MONTH_HIGHLIGHT_LOCATORS),
    )
    JOURNII_DETAIL_JOIN_DESCRIPTION_SPECS = (
        ("link text", TXT_LINK_LOCATORS),
    )

    RV_DAYS_ID = "com.cubii:id/rvDays"
    RV_DAYS_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvDays"]'
    )
    RV_DAYS_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/rvDays")'
    RV_WELLNESS_JOURNII_ID = "com.cubii:id/rvWellnessJournii"
    RV_WELLNESS_JOURNIIS_ID = "com.cubii:id/rvWellnessJourniis"
    RV_WELLNESS_JOURNII_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView'
        '[@resource-id="com.cubii:id/rvWellnessJournii"]'
    )
    RV_WELLNESS_JOURNIIS_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView'
        '[@resource-id="com.cubii:id/rvWellnessJourniis"]'
    )
    RV_WELLNESS_JOURNII_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/rvWellnessJournii")'
    )
    RV_WELLNESS_JOURNIIS_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/rvWellnessJourniis")'
    )
    RV_PREVIOUS_JOURNII_RECYCLER_LOCATORS = (
        (AppiumBy.ID, RV_WELLNESS_JOURNIIS_ID),
        (AppiumBy.XPATH, RV_WELLNESS_JOURNIIS_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, RV_WELLNESS_JOURNIIS_UIAUTOMATOR),
        (AppiumBy.ID, RV_WELLNESS_JOURNII_ID),
        (AppiumBy.XPATH, RV_WELLNESS_JOURNII_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, RV_WELLNESS_JOURNII_UIAUTOMATOR),
    )
    PREVIOUS_JOURNII_CARD_REL_XPATH = "./android.widget.FrameLayout"
    PREVIOUS_JOURNII_CARD_ABS_XPATHS = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvWellnessJourniis"]'
        "/android.widget.FrameLayout",
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvWellnessJournii"]'
        "/android.widget.FrameLayout",
    )
    PREVIOUS_JOURNII_CARD_IMAGE_REL_XPATHS = (
        './/android.widget.ImageView[@resource-id="com.cubii:id/ivJourniiImage"]',
        ".//android.widget.ImageView",
    )
    RV_DAYS_LOCATORS = (
        (AppiumBy.ID, RV_DAYS_ID),
        (AppiumBy.XPATH, RV_DAYS_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, RV_DAYS_UIAUTOMATOR),
        (AppiumBy.ID, RV_WELLNESS_JOURNII_ID),
        (AppiumBy.XPATH, RV_WELLNESS_JOURNII_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, RV_WELLNESS_JOURNII_UIAUTOMATOR),
    )
    TV_TASK_DATE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/tvTaskDate"]'
    )
    TV_TASK_DATE_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/tvTaskDate")'

    LL_WJP_TASK_ID = "com.cubii:id/llWJPTask"
    LL_WJP_TASK_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/llWJPTask"]'
    )
    LL_WJP_TASK_FIRST_XPATH = (
        '(//android.widget.LinearLayout[@resource-id="com.cubii:id/llWJPTask"])[1]'
    )
    LL_WJP_TASK_UIAUTOMATOR_TMPL = (
        'new UiSelector().resourceId("com.cubii:id/llWJPTask").instance({idx})'
    )

    TV_TASK_DATE_ID = "com.cubii:id/tvTaskDate"
    TV_TASK_NAME_ID = "com.cubii:id/tvTaskName"
    TV_TASK_PEOPLE_JOINED_ID = "com.cubii:id/tvTaskPeopleJoined"
    LL_WJP_TASK_REL_XPATH = (
        './/android.widget.LinearLayout[@resource-id="com.cubii:id/llWJPTask"]'
    )
    TASK_FIELD_SPECS = (
        ("date", TV_TASK_DATE_ID, "task date (tvTaskDate)"),
        ("name", TV_TASK_NAME_ID, "task name (tvTaskName)"),
        ("people_joined", TV_TASK_PEOPLE_JOINED_ID, "people joined (tvTaskPeopleJoined)"),
    )

    UPCOMING_TASKS_TAB_TEXT = "Upcoming Tasks"
    UPCOMING_TASKS_TAB_XPATH = (
        f'//android.widget.TextView[@text="{UPCOMING_TASKS_TAB_TEXT}"]'
    )
    UPCOMING_TASKS_TAB_UIAUTOMATOR = (
        f'new UiSelector().text("{UPCOMING_TASKS_TAB_TEXT}")'
    )
    UPCOMING_TASKS_TAB_LOCATORS = (
        (AppiumBy.XPATH, UPCOMING_TASKS_TAB_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, UPCOMING_TASKS_TAB_UIAUTOMATOR),
    )

    TV_COMPLETED_TASKS_ID = "com.cubii:id/tvCompletedTasks"
    TV_COMPLETED_TASKS_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/tvCompletedTasks"]'
    )
    TV_COMPLETED_TASKS_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/tvCompletedTasks")'
    )
    PREVIOUS_TASKS_TAB_TEXT = "Previous Tasks"
    PREVIOUS_TASKS_TAB_TEXT_XPATH = (
        f'//android.widget.TextView[@text="{PREVIOUS_TASKS_TAB_TEXT}"]'
    )
    PREVIOUS_TASKS_TAB_LOCATORS = (
        (AppiumBy.ID, TV_COMPLETED_TASKS_ID),
        (AppiumBy.XPATH, TV_COMPLETED_TASKS_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, TV_COMPLETED_TASKS_UIAUTOMATOR),
        (AppiumBy.XPATH, PREVIOUS_TASKS_TAB_TEXT_XPATH),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{PREVIOUS_TASKS_TAB_TEXT}")',
        ),
    )

    RV_DAYS_CARD_REL_XPATH = "./android.widget.FrameLayout"
    RV_DAYS_CARD_ABS_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvDays"]'
        "/android.widget.FrameLayout"
    )
    RV_DAYS_TASK_NAME_REL_XPATH = (
        './/android.widget.TextView[@resource-id="com.cubii:id/tvTaskName"]'
    )
    RV_DAYS_TASK_NAME_ABS_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvDays"]'
        '//android.widget.TextView[@resource-id="com.cubii:id/tvTaskName"]'
    )
    TASK_PROGRESS_BAR_CLASS = "android.widget.ProgressBar"

    TASKS_SCROLL_VIEW_CLASS = "android.widget.ScrollView"
    TASKS_SCROLL_VIEW_XPATH = "//android.widget.ScrollView"
    TASKS_SCROLL_VIEW_UIAUTOMATOR = (
        'new UiSelector().className("android.widget.ScrollView")'
    )
    TASKS_SCROLL_VIEW_LOCATORS = (
        (AppiumBy.CLASS_NAME, TASKS_SCROLL_VIEW_CLASS),
        (AppiumBy.XPATH, TASKS_SCROLL_VIEW_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, TASKS_SCROLL_VIEW_UIAUTOMATOR),
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

    def _must_see(
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

    def _wait_for_visible(
        self,
        locator_triplets: tuple[tuple, ...],
        env_key: str = "CUBII_WELLNESS_JOURNII_WAIT_SEC",
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

    def _get_visible_text(
        self,
        locator_triplets: tuple[tuple, ...],
        env_key: str = "CUBII_WELLNESS_JOURNII_WAIT_SEC",
        label: str = "element",
    ) -> str:
        el = self._wait_for_visible(locator_triplets, env_key=env_key, label=label)
        return (el.text or "").strip()

    def _is_any_visible(
        self, locator_triplets: tuple[tuple, ...], *, require_text: bool = False
    ) -> bool:
        for by, locator in locator_triplets:
            try:
                for el in self.driver.find_elements(by, locator):
                    if not el.is_displayed():
                        continue
                    if require_text and not (el.text or "").strip():
                        continue
                    return True
            except Exception:
                continue
        return False

    def _tap_any_clickable(
        self,
        locator_triplets: tuple[tuple, ...],
        label: str,
        *,
        env_key: str = "CUBII_WELLNESS_JOURNII_WAIT_SEC",
        pause_env_key: str = "CUBII_AFTER_WELLNESS_TAP_SEC",
        pause_default: str = "0.8",
        required: bool = True,
    ) -> bool:
        wait_sec = self._wait_sec(env_key)
        wait = WebDriverWait(self.driver, wait_sec)
        last_exc: Exception | None = None
        for by, locator in locator_triplets:
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                self._pause_after_tap(pause_env_key, pause_default)
                self.LOGGER.info("Tapped %s using (%s, %s).", label, by, locator)
                return True
            except Exception as exc:
                last_exc = exc
                continue
        if required:
            raise AssertionError(
                f"Could not tap {label} within {wait_sec}s (last error: {last_exc})"
            )
        self.LOGGER.info("%s not clickable within %ss; continuing.", label, wait_sec)
        return False

    def _find_rv_days_element(self):
        for by, locator in self.RV_DAYS_LOCATORS:
            try:
                el = self.driver.find_element(by, locator)
                if el.is_displayed():
                    return el
            except Exception:
                continue
        return None

    def _element_is_scroll_view(self, el) -> bool:
        try:
            class_name = (el.get_attribute("className") or el.get_attribute("class") or "")
            return "ScrollView" in class_name
        except Exception:
            return False

    def _find_tasks_scroll_view_element(self):
        """
        Find the ScrollView wrapping the May Wellness Journii task list (rvDays).
        Falls back to the first visible ScrollView on screen.
        """
        recycler = self._find_rv_days_element()
        if recycler is not None:
            current = recycler
            for _ in range(15):
                try:
                    parent = current.find_element(AppiumBy.XPATH, "./..")
                except Exception:
                    break
                if self._element_is_scroll_view(parent):
                    return parent
                current = parent

        for by, locator in self.TASKS_SCROLL_VIEW_LOCATORS:
            try:
                for el in self.driver.find_elements(by, locator):
                    if el.is_displayed():
                        return el
            except Exception:
                continue
        return None

    def _scroll_element_gesture(self, element, direction: str, percent: float) -> bool:
        try:
            element_id = element.id
            if element_id:
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "elementId": element_id,
                        "direction": direction,
                        "percent": percent,
                    },
                )
                return True
        except Exception as exc:
            self.LOGGER.debug("scrollGesture on element failed: %s", exc)
        return False

    def _scroll_tasks_list(self, direction: str = "down", percent: float | None = None) -> None:
        """
        Scroll the upcoming/previous tasks list via ScrollView (primary), then rvDays, then screen.
        """
        if percent is None:
            percent = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PERCENT", "0.55"))
        scroll_view = self._find_tasks_scroll_view_element()
        if scroll_view is not None:
            if self._scroll_element_gesture(scroll_view, direction, percent):
                self.LOGGER.debug(
                    "Scrolled tasks list %s using ScrollView.", direction
                )
                return
            self.LOGGER.info(
                "Wellness Journii: ScrollView scroll failed; trying rvDays fallback."
            )

        recycler = self._find_rv_days_element()
        if recycler is not None and self._scroll_element_gesture(recycler, direction, percent):
            self.LOGGER.debug("Scrolled tasks list %s using rvDays.", direction)
            return

        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.08),
                "top": int(size["height"] * 0.28),
                "width": int(size["width"] * 0.84),
                "height": int(size["height"] * 0.55),
                "direction": direction,
                "percent": percent,
            },
        )
        self.LOGGER.debug("Scrolled tasks list %s using screen fallback.", direction)

    def _scroll_rv_days_to_top(self) -> None:
        """Scroll the task list up so the first upcoming tasks are at the top."""
        up_scrolls = int(os.getenv("CUBII_WELLNESS_UPCOMING_TASKS_SCROLL_UP_ATTEMPTS", "5"))
        pause = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4"))
        for _ in range(up_scrolls):
            self._scroll_tasks_list("up")
            time.sleep(pause)

    def _scroll_rv_days(self, direction: str = "down", percent: float | None = None) -> None:
        """Scroll the task list (ScrollView preferred for May Wellness Journii screen)."""
        self._scroll_tasks_list(direction, percent=percent)

    def _upcoming_tasks_scroll_percent(self) -> float:
        return float(os.getenv("CUBII_WELLNESS_UPCOMING_TASKS_SCROLL_PERCENT", "0.32"))

    def _scroll_upcoming_tasks_list(self, direction: str = "down") -> None:
        """Smaller scroll steps so individual days are not skipped in rvDays."""
        self._scroll_tasks_list(direction, percent=self._upcoming_tasks_scroll_percent())

    def _scroll_task_row_element(self, row, direction: str = "down") -> None:
        """Scroll within/near a task row so clipped fields (e.g. people joined) can appear."""
        percent = float(os.getenv("CUBII_WELLNESS_JOURNII_ROW_SCROLL_PERCENT", "0.35"))
        try:
            element_id = row.id
            if element_id:
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "elementId": element_id,
                        "direction": direction,
                        "percent": percent,
                    },
                )
                return
        except Exception as exc:
            self.LOGGER.debug(
                "Wellness Journii: row element scroll failed (%s); using list scroll.",
                exc,
            )
        self._scroll_rv_days(direction)

    def _scroll_task_row_into_view(self, row, *, for_upcoming: bool = False) -> None:
        """Scroll rvDays until the task row sits in the visible viewport."""
        size = self.driver.get_window_size()
        screen_h = size["height"]
        top_default = "0.12" if for_upcoming else "0.2"
        top_margin = int(
            screen_h * float(os.getenv("CUBII_WELLNESS_JOURNII_ROW_VIEWPORT_TOP", top_default))
        )
        bottom_margin = int(
            screen_h * float(os.getenv("CUBII_WELLNESS_JOURNII_ROW_VIEWPORT_BOTTOM", "0.78"))
        )
        pause = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4"))
        max_attempts = int(os.getenv("CUBII_WELLNESS_JOURNII_ROW_SCROLL_INTO_VIEW_ATTEMPTS", "3"))
        scroll_list = self._scroll_upcoming_tasks_list if for_upcoming else self._scroll_rv_days

        for attempt in range(max_attempts):
            try:
                loc = row.location or {}
                row_h = int((row.size or {}).get("height", 80))
                y = int(loc.get("y", -1))
                bottom = y + row_h
                if y >= 0 and bottom <= bottom_margin and y >= top_margin:
                    return
                if y >= 0 and bottom <= bottom_margin and y < top_margin:
                    return
                if y < 0:
                    break
                if bottom > bottom_margin:
                    self.LOGGER.debug(
                        "Wellness Journii: scrolling task row down into view "
                        "(attempt %s, y=%s).",
                        attempt + 1,
                        y,
                    )
                    scroll_list("down")
                    time.sleep(pause)
                    continue
                if y < top_margin:
                    self.LOGGER.debug(
                        "Wellness Journii: row above viewport (y=%s); list scroll only.",
                        y,
                    )
                    return
                return
            except Exception as exc:
                self.LOGGER.debug("Wellness Journii: row viewport check failed: %s", exc)
                scroll_list("down")
                time.sleep(pause)

    def _find_task_row_by_name(self, task_name: str):
        """Re-locate llWJPTask after scrolling (stale-safe) using visible task name text."""
        name = (task_name or "").strip()
        if not name:
            return None
        recycler = self._find_rv_days_element()
        roots = [recycler] if recycler is not None else [self.driver]
        for root in roots:
            for row in root.find_elements(AppiumBy.XPATH, self.LL_WJP_TASK_REL_XPATH):
                try:
                    if not row.is_displayed():
                        continue
                    for el in row.find_elements(AppiumBy.ID, self.TV_TASK_NAME_ID):
                        if (el.text or "").strip() == name:
                            return row
                except Exception:
                    continue
        return None

    @staticmethod
    def _descendant_xpath(resource_id: str) -> str:
        return f'.//*[@resource-id="{resource_id}"]'

    def _row_dedupe_key(self, row) -> str:
        try:
            loc = row.location or {}
            size = row.size or {}
            return (
                f"{loc.get('x', '')}:{loc.get('y', '')}:"
                f"{size.get('width', '')}:{size.get('height', '')}"
            )
        except Exception:
            return str(id(row))

    def _collect_visible_task_rows(self) -> list:
        """Return displayed llWJPTask rows scoped to rvDays only."""
        recycler = self._find_rv_days_element()
        if recycler is None:
            self.LOGGER.warning(
                "Wellness Journii: rvDays not found; falling back to global llWJPTask search."
            )
            search_roots = [self.driver]
        else:
            search_roots = [recycler]

        rows: list = []
        seen_keys: set[str] = set()
        for root in search_roots:
            try:
                candidates = root.find_elements(AppiumBy.XPATH, self.LL_WJP_TASK_REL_XPATH)
            except Exception:
                candidates = []
            if not candidates and root is self.driver:
                candidates = self.driver.find_elements(AppiumBy.XPATH, self.LL_WJP_TASK_XPATH)
            for el in candidates:
                try:
                    if not el.is_displayed():
                        continue
                    key = self._row_dedupe_key(el)
                    if key in seen_keys:
                        continue
                    seen_keys.add(key)
                    rows.append(el)
                except Exception:
                    continue
        return rows

    def _first_visible_descendant_text(self, root, resource_id: str) -> tuple[str, bool]:
        """Return text and whether a visible descendant with resource_id was found."""
        try:
            for el in root.find_elements(AppiumBy.XPATH, self._descendant_xpath(resource_id)):
                try:
                    if not el.is_displayed():
                        continue
                    return (el.text or "").strip(), True
                except Exception:
                    continue
        except Exception:
            pass
        return "", False

    def _first_visible_from_row_xpaths(self, row, xpaths: tuple[str, ...]) -> tuple[str, bool]:
        """Return text from the first visible element matched by relative xpaths on row."""
        for xpath in xpaths:
            try:
                for el in row.find_elements(AppiumBy.XPATH, xpath):
                    try:
                        if not el.is_displayed():
                            continue
                        return (el.text or "").strip(), True
                    except Exception:
                        continue
            except Exception:
                continue
        return "", False

    @staticmethod
    def _element_vertical_bounds(element) -> tuple[int, int]:
        try:
            loc = element.location or {}
            size = element.size or {}
            top = int(loc.get("y", -1))
            height = int(size.get("height", 0))
            if top < 0:
                return -1, -1
            return top, top + max(height, 0)
        except Exception:
            return -1, -1

    def _find_nearest_task_date_near_row(self, row) -> tuple[str, bool]:
        """
        Pick tvTaskDate for a task row in rvDays.

        Handles both layouts: date section above llWJPTask, and date badge on the
        card frame (top-left on the same card — see May 24 / May 25 in the app UI).
        """
        recycler = self._find_rv_days_element()
        if recycler is None:
            return "", False
        row_top, row_bottom = self._element_vertical_bounds(row)
        if row_top < 0:
            return "", False

        gap_px = int(os.getenv("CUBII_WELLNESS_TASK_DATE_NEAR_ROW_GAP_PX", "64"))
        best_el = None
        best_score: int | None = None

        for by, locator in (
            (AppiumBy.ID, self.TV_TASK_DATE_ID),
            (AppiumBy.XPATH, self.TV_TASK_DATE_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.TV_TASK_DATE_UIAUTOMATOR),
        ):
            try:
                candidates = recycler.find_elements(by, locator)
            except Exception:
                continue
            for el in candidates:
                try:
                    if not el.is_displayed():
                        continue
                    date_top, date_bottom = self._element_vertical_bounds(el)
                    if date_top < 0:
                        continue
                    if date_bottom < row_top - gap_px:
                        continue
                    if date_top > row_bottom + gap_px:
                        continue
                    on_card = date_top >= row_top and date_bottom <= row_bottom + gap_px
                    score = abs(date_top - row_top)
                    if on_card:
                        score -= 1000
                    elif date_bottom <= row_top:
                        score += abs(row_top - date_bottom)
                    if best_score is None or score < best_score:
                        best_score = score
                        best_el = el
                except Exception:
                    continue
        if best_el is None:
            return "", False
        return (best_el.text or "").strip(), True

    def _find_nearest_task_date_above_row(self, row) -> tuple[str, bool]:
        """Backward-compatible alias for recycler-wide date lookup near a row."""
        return self._find_nearest_task_date_near_row(row)

    def _find_task_date_for_row(self, row) -> tuple[str, bool]:
        """
        Resolve tvTaskDate for a task card.

        Date may sit on the rvDays card frame (badge) or in a section above llWJPTask.
        """
        try:
            card_frame = self._frame_layout_row_parent_of(row)
            text, found = self._first_visible_descendant_text(
                card_frame, self.TV_TASK_DATE_ID
            )
            if found and text.strip():
                return text, found
        except Exception:
            pass

        date_xpaths = (
            f'./preceding-sibling::*[@resource-id="{self.TV_TASK_DATE_ID}"]',
            f'./preceding-sibling::*//*[@resource-id="{self.TV_TASK_DATE_ID}"]',
            './preceding-sibling::*[.//*[@resource-id="com.cubii:id/tvTaskDate"]]'
            '[last()]//*[@resource-id="com.cubii:id/tvTaskDate"]',
            './preceding-sibling::*[.//*[@resource-id="com.cubii:id/tvTaskDate"]]'
            '[last()]',
            './parent::*//*[@resource-id="com.cubii:id/tvTaskDate"]',
        )
        text, found = self._first_visible_from_row_xpaths(row, date_xpaths)
        if found:
            return text, found

        text, found = self._first_visible_descendant_text(row, self.TV_TASK_DATE_ID)
        if found:
            return text, found

        current = row
        for _ in range(int(os.getenv("CUBII_WELLNESS_JOURNII_TASK_ANCESTOR_DEPTH", "5"))):
            try:
                parent = current.find_element(AppiumBy.XPATH, "./..")
            except Exception:
                break
            text, found = self._first_visible_descendant_text(parent, self.TV_TASK_DATE_ID)
            if found:
                return text, found
            current = parent

        return self._find_nearest_task_date_near_row(row)

    def _find_task_field(self, row, resource_id: str) -> tuple[str, bool]:
        """Resolve a task field on the card; date uses sibling/recycler-aware lookup."""
        if resource_id == self.TV_TASK_DATE_ID:
            return self._find_task_date_for_row(row)

        text, found = self._first_visible_descendant_text(row, resource_id)
        if found:
            return text, found

        current = row
        for _ in range(int(os.getenv("CUBII_WELLNESS_JOURNII_TASK_ANCESTOR_DEPTH", "5"))):
            try:
                parent = current.find_element(AppiumBy.XPATH, "./..")
            except Exception:
                break
            text, found = self._first_visible_descendant_text(parent, resource_id)
            if found:
                return text, found
            current = parent
        return "", False

    def _task_row_details(self, row) -> dict[str, tuple[str, bool]]:
        details: dict[str, tuple[str, bool]] = {}
        for key, resource_id, _label in self.TASK_FIELD_SPECS:
            details[key] = self._find_task_field(row, resource_id)
        return details

    def _format_task_row_details(self, details: dict[str, tuple[str, bool]]) -> str:
        parts: list[str] = []
        for key, _resource_id, label in self.TASK_FIELD_SPECS:
            text, found = details.get(key, ("", False))
            parts.append(f"{label}={text!r} (found={found})")
        return "; ".join(parts)

    def _task_row_signature(self, details: dict[str, tuple[str, bool]]) -> str:
        return "|".join(details.get(key, ("", False))[0] for key, _, _ in self.TASK_FIELD_SPECS)

    def _is_actionable_task_row(self, details: dict[str, tuple[str, bool]]) -> bool:
        """A row must expose a task name before we treat it as a Journii task card."""
        _name_text, name_found = details.get("name", ("", False))
        return name_found and bool(_name_text.strip())

    def _missing_task_field_labels(self, details: dict[str, tuple[str, bool]]) -> list[str]:
        missing: list[str] = []
        for key, _resource_id, label in self.TASK_FIELD_SPECS:
            text, found = details.get(key, ("", False))
            if not found:
                missing.append(label)
            elif not text.strip():
                missing.append(f"{label} (empty text)")
        return missing

    def _resolve_task_row_details_with_scroll(
        self, row, row_index: int
    ) -> tuple[object, dict[str, tuple[str, bool]]]:
        """
        Scroll the task row into view and re-read fields until complete or retries exhaust.
        """
        pause = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4"))
        max_retries = int(os.getenv("CUBII_WELLNESS_JOURNII_ROW_FIELD_SCROLL_RETRIES", "4"))

        self._scroll_task_row_into_view(row)
        details = self._task_row_details(row)
        name_text, _ = details.get("name", ("", False))

        for attempt in range(max_retries + 1):
            missing = self._missing_task_field_labels(details)
            if not missing:
                return row, details

            self.LOGGER.info(
                "Wellness Journii: task row %s missing %s; scrolling down (%s/%s).",
                row_index,
                ", ".join(missing),
                attempt + 1,
                max_retries + 1,
            )
            self._scroll_task_row_into_view(row)
            self._scroll_rv_days("down")
            time.sleep(pause)

            if name_text:
                relocated = self._find_task_row_by_name(name_text)
                if relocated is not None:
                    row = relocated
            details = self._task_row_details(row)

        return row, details

    def _verify_task_row_fields(self, row, row_index: int, details: dict[str, tuple[str, bool]]) -> None:
        missing: list[str] = []
        for key, _resource_id, label in self.TASK_FIELD_SPECS:
            text, found = details.get(key, ("", False))
            if not found:
                missing.append(label)
            elif not text.strip():
                missing.append(f"{label} (empty text)")
        if missing:
            self.LOGGER.error(
                "Journii task row %s failed verification. Observed: %s",
                row_index,
                self._format_task_row_details(details),
            )
            raise AssertionError(
                f"Journii task row {row_index} is missing fields: {', '.join(missing)}. "
                f"Observed: {self._format_task_row_details(details)}"
            )

    def open_wellness_journii_tab(self) -> None:
        """Open Wellness Journii from bottom navigation."""
        self.LOGGER.info("Open Wellness Journii tab.")
        self._dismiss_navigation_blockers()
        for by, locator in self.WELLNESS_TAB_CANDIDATE_LOCATORS:
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
                    self._pause_after_tap("CUBII_AFTER_WELLNESS_TAB_TAP_SEC", "1.0")
                    self.LOGGER.info(
                        "Opened Wellness Journii tab using locator=(%s, %s).", by, locator
                    )
                    return
            except Exception:
                continue
        raise AssertionError(
            "Could not open Wellness Journii tab. Tried accessibility id, resource id, "
            "UiAutomator, and content-desc xpath."
        )

    def verify_current_and_previous_tabs(self) -> None:
        """Assert Current and Previous segment controls are visible."""
        wait_sec = self._wait_sec("CUBII_WELLNESS_JOURNII_SCREEN_WAIT_SEC")
        wait = WebDriverWait(self.driver, wait_sec)
        missing: list[str] = []
        self._must_see(
            self.SB_CURRENT_LOCATORS,
            "Current tab (sbCurrent)",
            wait,
            missing,
        )
        self._must_see(
            self.SB_PREVIOUS_LOCATORS,
            "Previous tab (sbPrevious)",
            wait,
            missing,
        )
        if missing:
            raise AssertionError(
                "Wellness Journii current/previous tabs not visible: "
                + ", ".join(missing)
            )
        self.LOGGER.info("Verified Current and Previous Journii tabs.")

    def tap_current_journii_segment_tab(self) -> None:
        """Tap Current on the main Wellness Journii screen (sbCurrent)."""
        self.LOGGER.info("Tap Current Journii segment tab (sbCurrent).")
        self._tap_any_clickable(
            self.SB_CURRENT_LOCATORS,
            "Current Journii segment tab (sbCurrent)",
            env_key="CUBII_WELLNESS_SB_CURRENT_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_SB_CURRENT_TAP_SEC",
            pause_default="0.8",
        )

    def tap_previous_journii_segment_tab(self) -> None:
        """Tap Previous on the main Wellness Journii screen (sbPrevious)."""
        self.LOGGER.info("Tap Previous Journii segment tab (sbPrevious).")
        self._tap_any_clickable(
            self.SB_PREVIOUS_LOCATORS,
            "Previous Journii segment tab (sbPrevious)",
            env_key="CUBII_WELLNESS_SB_PREVIOUS_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_SB_PREVIOUS_TAP_SEC",
            pause_default="0.8",
        )

    def _get_visible_element_text(self, locator_triplets: tuple[tuple, ...]) -> str:
        for by, locator in locator_triplets:
            try:
                for el in self.driver.find_elements(by, locator):
                    if self._element_is_effectively_visible(el):
                        return (el.text or "").strip()
            except Exception:
                continue
        return ""

    def _find_previous_journii_recycler(self):
        for by, locator in self.RV_PREVIOUS_JOURNII_RECYCLER_LOCATORS:
            try:
                el = self.driver.find_element(by, locator)
                if el.is_displayed():
                    return el
            except Exception:
                continue
        return None

    def _previous_journii_card_has_image(self, card) -> bool:
        for xpath in self.PREVIOUS_JOURNII_CARD_IMAGE_REL_XPATHS:
            try:
                for el in card.find_elements(AppiumBy.XPATH, xpath):
                    if self._element_is_effectively_visible(el):
                        return True
            except Exception:
                continue
        return False

    def _previous_journii_card_key(self, card) -> str:
        title_text, title_found = self._first_visible_descendant_text(
            card, self.TV_WJP_MONTH_TITLE_ID
        )
        if title_found and title_text.strip():
            return title_text.strip()
        return self._row_dedupe_key(card)

    def _screen_has_visible_journii_program_indicators(self) -> bool:
        """True when past/current Journii hero content is on screen (not the empty list)."""
        for locator_triplets in (
            self.IV_JOURNII_IMAGE_LOCATORS,
            self.TV_WJP_MONTH_TITLE_LOCATORS,
        ):
            for by, locator in locator_triplets:
                try:
                    for el in self.driver.find_elements(by, locator):
                        if self._element_is_effectively_visible(el):
                            return True
                except Exception:
                    continue
        return False

    def _collect_previous_journii_program_cards(self) -> list:
        """
        Return displayed past Journii cards in rvWellnessJourniis / rvWellnessJournii.

        Card layout: RecyclerView/FrameLayout/.../ImageView (ivJourniiImage).
        Falls back to visible ivJourniiImage nodes when the recycler id differs on device.
        """
        cards: list = []
        seen_keys: set[str] = set()

        def _add_card(card) -> None:
            try:
                if not self._element_is_effectively_visible(card):
                    return
                if not self._previous_journii_card_has_image(card):
                    return
                key = self._previous_journii_card_key(card)
                if not key or key in seen_keys:
                    return
                seen_keys.add(key)
                cards.append(card)
            except Exception:
                pass

        recycler = self._find_previous_journii_recycler()
        candidates: list = []
        if recycler is not None:
            try:
                candidates.extend(
                    recycler.find_elements(
                        AppiumBy.XPATH, self.PREVIOUS_JOURNII_CARD_REL_XPATH
                    )
                )
            except Exception:
                pass
        if not candidates:
            for xpath in self.PREVIOUS_JOURNII_CARD_ABS_XPATHS:
                try:
                    candidates.extend(self.driver.find_elements(AppiumBy.XPATH, xpath))
                except Exception:
                    continue

        for card in candidates:
            _add_card(card)

        if cards:
            return cards

        for by, locator in self.IV_JOURNII_IMAGE_LOCATORS:
            try:
                for image_el in self.driver.find_elements(by, locator):
                    if not self._element_is_effectively_visible(image_el):
                        continue
                    card = self._frame_layout_row_parent_of(image_el)
                    _add_card(card)
            except Exception:
                continue

        return cards

    def _scroll_previous_journii_list(self, direction: str = "down") -> None:
        percent = float(os.getenv("CUBII_WELLNESS_PREVIOUS_JOURNII_SCROLL_PERCENT", "0.45"))
        recycler = self._find_previous_journii_recycler()
        if recycler is not None and self._scroll_element_gesture(recycler, direction, percent):
            self.LOGGER.debug(
                "Scrolled previous Journii list %s using rvWellnessJournii(s).", direction
            )
            return
        self._scroll_tasks_list(direction, percent=percent)

    def _previous_segment_shows_empty_list(self) -> bool:
        if self._screen_has_visible_journii_program_indicators():
            return False
        empty_title = self._get_visible_element_text(self.EMPTY_LIST_TEXT_LOCATORS)
        return self._text_looks_like_no_journiis_empty(empty_title)

    @staticmethod
    def _text_looks_like_no_journiis_empty(title: str) -> bool:
        cleaned = (title or "").strip().lower()
        if not cleaned:
            return False
        return "no journii" in cleaned or cleaned == "no journiis"

    def _verify_previous_journii_empty_copy(self) -> None:
        empty_title = self._get_visible_element_text(self.EMPTY_LIST_TEXT_LOCATORS)
        if not empty_title:
            self._wait_for_visible(
                self.EMPTY_LIST_TEXT_LOCATORS,
                env_key="CUBII_WELLNESS_PREVIOUS_EMPTY_WAIT_SEC",
                label="Previous Journii empty title (emptyListText)",
            )
            empty_title = self._get_visible_element_text(self.EMPTY_LIST_TEXT_LOCATORS)

        if not self._text_looks_like_no_journiis_empty(empty_title):
            raise AssertionError(
                "Previous Journii empty list title (emptyListText) expected "
                f"{self.PREVIOUS_EMPTY_TITLE_TEXT!r} or similar; got {empty_title!r}."
            )

        normal_text = self._get_visible_element_text(self.EMPTY_LIST_NORMAL_TEXT_LOCATORS)
        if not normal_text:
            self._wait_for_visible(
                self.EMPTY_LIST_NORMAL_TEXT_LOCATORS,
                env_key="CUBII_WELLNESS_PREVIOUS_EMPTY_WAIT_SEC",
                label="Previous Journii empty body (emptyListNormalText)",
            )
            normal_text = self._get_visible_element_text(self.EMPTY_LIST_NORMAL_TEXT_LOCATORS)

        if not normal_text.strip():
            raise AssertionError(
                "Previous Journii empty body (emptyListNormalText) is not displayed."
            )

        self.LOGGER.info(
            "Verified Previous Journii empty state: emptyListText=%r; "
            "emptyListNormalText=%r.",
            empty_title,
            normal_text,
        )

    def _wait_for_previous_journii_programs(self) -> None:
        """Wait until past Journii content appears (recycler list or ivJourniiImage)."""
        wait_sec = self._wait_sec("CUBII_WELLNESS_PREVIOUS_PROGRAMS_WAIT_SEC")
        wait = WebDriverWait(self.driver, wait_sec)
        last_exc: Exception | None = None
        locator_sets = (
            self.RV_PREVIOUS_JOURNII_RECYCLER_LOCATORS,
            self.IV_JOURNII_IMAGE_LOCATORS,
            self.TV_WJP_MONTH_TITLE_LOCATORS,
        )
        for locator_triplets in locator_sets:
            for by, locator in locator_triplets:
                try:
                    wait.until(ec.visibility_of_element_located((by, locator)))
                    self.LOGGER.info(
                        "Previous Journii program UI visible via (%s, %s).", by, locator
                    )
                    return
                except Exception as exc:
                    last_exc = exc
        raise TimeoutException(
            f"Previous Journii programs not visible within {wait_sec}s (last: {last_exc})"
        )

    def _verify_and_scroll_previous_journii_programs(self) -> None:
        """Verify each past Journii card (ImageView) and scroll the Previous segment list."""
        self._wait_for_previous_journii_programs()

        max_scrolls = int(os.getenv("CUBII_WELLNESS_PREVIOUS_JOURNII_SCROLL_ATTEMPTS", "20"))
        pause = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4"))
        empty_passes_to_stop = int(
            os.getenv("CUBII_WELLNESS_PREVIOUS_JOURNII_EMPTY_PASSES_TO_STOP", "3")
        )

        verified_keys: set[str] = set()
        seen_keys: set[str] = set()
        consecutive_no_new_seen = 0

        for scroll_attempt in range(max_scrolls + 1):
            before_seen = len(seen_keys)
            cards = self._collect_previous_journii_program_cards()
            self.LOGGER.info(
                "Previous Journii programs: scroll %s — %s card(s), %s seen, %s verified.",
                scroll_attempt,
                len(cards),
                len(seen_keys),
                len(verified_keys),
            )

            for card in cards:
                key = self._previous_journii_card_key(card)
                if not key:
                    continue
                seen_keys.add(key)
                if key in verified_keys:
                    continue
                if not self._previous_journii_card_has_image(card):
                    self.LOGGER.info(
                        "Previous Journii card %r not verified yet (no visible image); retry.",
                        key,
                    )
                    continue
                title_text, title_found = self._first_visible_descendant_text(
                    card, self.TV_WJP_MONTH_TITLE_ID
                )
                verified_keys.add(key)
                self.LOGGER.info(
                    "Verified previous Journii program %s: image=ok, title=%r (found=%s).",
                    len(verified_keys),
                    title_text,
                    title_found,
                )

            if len(seen_keys) - before_seen == 0:
                consecutive_no_new_seen += 1
            else:
                consecutive_no_new_seen = 0

            if consecutive_no_new_seen >= empty_passes_to_stop:
                break
            if scroll_attempt >= max_scrolls:
                break

            self._scroll_previous_journii_list("down")
            time.sleep(pause)

        if not verified_keys:
            raise AssertionError(
                "Previous Journii segment shows list UI but no program cards with a "
                "visible ImageView (ivJourniiImage) were verified."
            )

        unverified = seen_keys - verified_keys
        if unverified:
            raise AssertionError(
                f"Verified {len(verified_keys)} of {len(seen_keys)} seen previous Journii "
                f"program(s). Could not verify image on: {sorted(unverified)}."
            )

        self.LOGGER.info(
            "Verified %s previous Journii program(s) in rvWellnessJourniis with scroll.",
            len(verified_keys),
        )

    def verify_previous_journii_empty_state_if_no_programs(self) -> None:
        """
        On sbPrevious: if empty -> No Journiis; otherwise verify Journii cards and scroll.

        Programs may render in rvWellnessJourniis or as visible ivJourniiImage rows without
        that recycler id on all builds.
        """
        time.sleep(float(os.getenv("CUBII_WELLNESS_PREVIOUS_EMPTY_WAIT_SEC", "1.2")))

        if self._previous_segment_shows_empty_list():
            self._verify_previous_journii_empty_copy()
            return

        self.LOGGER.info(
            "Previous Journii segment is not empty; verifying program card(s) and scrolling."
        )
        self._verify_and_scroll_previous_journii_programs()

    def verify_current_month_journii_image(self) -> None:
        """Assert the current-month Journii hero image is displayed."""
        self._wait_for_visible(
            self.IV_JOURNII_IMAGE_LOCATORS,
            label="current month Journii image (ivJourniiImage)",
        )
        self.LOGGER.info("Verified current month Journii image.")

    def verify_current_month_journii_name(self) -> None:
        """Assert month title is visible and non-empty; optionally matches current month."""
        title = self._get_visible_text(
            self.TV_WJP_MONTH_TITLE_LOCATORS,
            label="current month Journii title (tvWJPMonthTitle)",
        )
        if not title:
            raise AssertionError(
                "Current month Journii title (tvWJPMonthTitle) is empty."
            )
        current_month = datetime.now().strftime("%B")
        if current_month.lower() not in title.lower():
            self.LOGGER.warning(
                "Month title %r does not contain current month %r; continuing.",
                title,
                current_month,
            )
        self.LOGGER.info("Verified current month Journii title: %r.", title)

    def verify_joined_journii_members_highlight(self) -> None:
        """Assert joined-members highlight text is visible and non-empty."""
        highlight = self._get_visible_text(
            self.TV_WJP_MONTH_HIGHLIGHT_LOCATORS,
            label="joined Journii members highlight (tvWJPMonthHighlight)",
        )
        if not highlight:
            raise AssertionError(
                "Joined Journii members highlight (tvWJPMonthHighlight) is empty."
            )
        if not re.search(r"\d", highlight):
            self.LOGGER.warning(
                "Joined members highlight %r has no digit; text still displayed.",
                highlight,
            )
        self.LOGGER.info("Verified joined Journii members highlight: %r.", highlight)

    def verify_all_journii_tasks(self) -> None:
        """Assert every task row under rvDays shows date, name, and people-joined; scroll if needed."""
        self._wait_for_visible(
            self.RV_DAYS_LOCATORS,
            label="Journii tasks list (rvDays)",
        )
        max_scrolls = int(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_ATTEMPTS", "10"))
        pause = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4"))

        verified_signatures: set[str] = set()
        row_index = 0

        for scroll_attempt in range(max_scrolls + 1):
            rows = self._collect_visible_task_rows()
            self.LOGGER.info(
                "Wellness Journii: scroll %s — %s llWJPTask row(s) visible in rvDays.",
                scroll_attempt,
                len(rows),
            )
            new_rows_found = False
            for row in rows:
                details = self._task_row_details(row)
                if not self._is_actionable_task_row(details):
                    self.LOGGER.debug(
                        "Skipping non-task llWJPTask (no visible name): %s",
                        self._format_task_row_details(details),
                    )
                    continue
                signature = self._task_row_signature(details)
                if signature in verified_signatures:
                    continue
                row_index += 1
                row, details = self._resolve_task_row_details_with_scroll(row, row_index)
                self._verify_task_row_fields(row, row_index, details)
                verified_signatures.add(self._task_row_signature(details))
                new_rows_found = True
                self.LOGGER.info(
                    "Verified Journii task %s: %s",
                    row_index,
                    self._format_task_row_details(details),
                )

            if scroll_attempt >= max_scrolls:
                break
            before_scroll = len(verified_signatures)
            self._scroll_rv_days("down")
            time.sleep(pause)
            rows_after = self._collect_visible_task_rows()
            for row in rows_after:
                details = self._task_row_details(row)
                if not self._is_actionable_task_row(details):
                    continue
                signature = self._task_row_signature(details)
                if signature not in verified_signatures:
                    new_rows_found = True
                    break
            if not new_rows_found and len(verified_signatures) == before_scroll:
                break

        if not verified_signatures:
            raise AssertionError(
                "No Journii tasks (llWJPTask) found under rvDays after scrolling."
            )
        self.LOGGER.info(
            "Verified %s Journii task row(s) with date, name, and people joined.",
            len(verified_signatures),
        )

    def tap_journii_banner_card(self) -> None:
        """Tap the hero banner (ivJourniiImage) on the Wellness Journii main screen."""
        self.LOGGER.info("Tap Journii banner card (ivJourniiImage).")
        self._dismiss_navigation_blockers()
        self._tap_any_clickable(
            self.IV_JOURNII_IMAGE_LOCATORS,
            "Journii banner card (ivJourniiImage)",
            pause_env_key="CUBII_AFTER_WELLNESS_BANNER_TAP_SEC",
            pause_default="1.0",
        )
        self._pause_after_tap("CUBII_AFTER_WELLNESS_BANNER_NAV_SEC", "0.6")

    def verify_journii_detail_screen_title(self) -> None:
        """Assert detail screen toolbar title (toolbar_title) is visible and non-empty."""
        title = self._get_visible_text(
            self.TOOLBAR_TITLE_LOCATORS,
            env_key="CUBII_WELLNESS_JOURNII_DETAIL_TITLE_WAIT_SEC",
            label="Wellness Journii detail toolbar title (toolbar_title)",
        )
        if not title:
            raise AssertionError(
                "Wellness Journii detail toolbar title (toolbar_title) is empty."
            )
        self.LOGGER.info("Verified Wellness Journii detail screen title: %r.", title)

    def is_join_button_displayed(self) -> bool:
        """Return True when Join / View All (btnViewAll) is visible on the detail screen."""
        return self._is_any_visible(self.BTN_VIEW_ALL_LOCATORS)

    def _find_view_all_button_element(self):
        for by, locator in self.BTN_VIEW_ALL_LOCATORS:
            try:
                for el in self.driver.find_elements(by, locator):
                    if self._element_is_effectively_visible(el):
                        return el
            except Exception:
                continue
        return None

    def scroll_detail_until_view_all_visible(self) -> None:
        """
        Scroll the Journii detail ScrollView down until btnViewAll (View All) is visible.
        """
        pause = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4"))
        max_scrolls = int(os.getenv("CUBII_WELLNESS_VIEW_ALL_SCROLL_ATTEMPTS", "18"))
        percent = float(os.getenv("CUBII_WELLNESS_VIEW_ALL_SCROLL_PERCENT", "0.5"))

        if self._is_any_visible(self.BTN_VIEW_ALL_LOCATORS):
            btn = self._find_view_all_button_element()
            if btn is not None:
                try:
                    self._scroll_task_row_into_view(btn)
                    time.sleep(pause * 0.5)
                except Exception:
                    pass
            self.LOGGER.info("View All button (btnViewAll) already visible on detail screen.")
            return

        for scroll_attempt in range(max_scrolls):
            self._scroll_tasks_list("down", percent=percent)
            time.sleep(pause)
            if self._is_any_visible(self.BTN_VIEW_ALL_LOCATORS):
                btn = self._find_view_all_button_element()
                if btn is not None:
                    try:
                        self._scroll_task_row_into_view(btn)
                        time.sleep(pause * 0.5)
                    except Exception:
                        pass
                self.LOGGER.info(
                    "View All button (btnViewAll) visible after %s scroll-down(s).",
                    scroll_attempt + 1,
                )
                return

        raise AssertionError(
            f"View All button (btnViewAll) not found after {max_scrolls} scroll-down "
            "gestures on the Journii detail screen."
        )

    def tap_view_all_button(self) -> None:
        """Tap View All / Join (btnViewAll) on the Journii detail screen."""
        if not self._is_any_visible(self.BTN_VIEW_ALL_LOCATORS):
            raise AssertionError(
                "View All button (btnViewAll) is not visible; scroll to it before tapping."
            )
        btn = self._find_view_all_button_element()
        if btn is not None:
            try:
                label = (btn.text or "").strip() or "View All"
            except Exception:
                label = "View All"
        else:
            label = "View All"
        self.LOGGER.info("Tap View All button (btnViewAll) label=%r.", label)
        self._tap_any_clickable(
            self.BTN_VIEW_ALL_LOCATORS,
            f"View All button (btnViewAll, {label!r})",
            env_key="CUBII_WELLNESS_VIEW_ALL_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_WELLNESS_VIEW_ALL_TAP_SEC",
            pause_default="1.0",
            required=True,
        )

    def _verify_journii_detail_description_fields(
        self,
        specs: tuple[tuple[str, tuple[tuple, ...]], ...],
        *,
        wait_sec: int,
    ) -> list[str]:
        """Verify description fields; return human-readable observed values."""
        wait = WebDriverWait(self.driver, wait_sec)
        missing: list[str] = []
        observed: list[str] = []

        for label, locator_triplets in specs:
            found_text = ""
            for by, locator in locator_triplets:
                try:
                    el = wait.until(ec.visibility_of_element_located((by, locator)))
                    found_text = (el.text or "").strip()
                    if found_text:
                        observed.append(f"{label}={found_text!r}")
                        break
                except TimeoutException:
                    continue
            else:
                missing.append(label)
                continue
            if not found_text:
                missing.append(f"{label} (empty text)")

        if missing:
            detail = "; ".join(observed) if observed else "none"
            raise AssertionError(
                "Wellness Journii detail description incomplete. Missing: "
                f"{', '.join(missing)}. Observed: {detail}."
            )
        return observed

    def verify_journii_detail_description(self) -> None:
        """
        Assert detail description based on join state.

        Always: month title + highlight.
        When join button (btnViewAll) is visible: also require link text (txtLink).
        When join button is hidden (already joined): skip link text check.
        """
        wait_sec = self._wait_sec("CUBII_WELLNESS_JOURNII_DETAIL_DESC_WAIT_SEC")
        join_visible = self.is_join_button_displayed()

        specs: list[tuple[str, tuple[tuple, ...]]] = list(
            self.JOURNII_DETAIL_BASE_DESCRIPTION_SPECS
        )
        if join_visible:
            specs.extend(self.JOURNII_DETAIL_JOIN_DESCRIPTION_SPECS)
            self.LOGGER.info(
                "Join button (btnViewAll) visible; verifying title, highlight, and link text."
            )
        else:
            self.LOGGER.info(
                "Join button (btnViewAll) not visible; verifying title and highlight only "
                "(link text skipped — user likely already joined)."
            )

        observed = self._verify_journii_detail_description_fields(
            tuple(specs),
            wait_sec=wait_sec,
        )
        self.LOGGER.info(
            "Verified Wellness Journii detail description (join_visible=%s): %s.",
            join_visible,
            "; ".join(observed),
        )

    def tap_join_button_if_displayed(self) -> bool:
        """
        Tap Join / View All (btnViewAll) when visible; skip gracefully when absent
        (e.g. user already joined).
        """
        self.LOGGER.info("Check for Journii join button (btnViewAll).")
        if not self._is_any_visible(self.BTN_VIEW_ALL_LOCATORS):
            self.LOGGER.info(
                "Join button (btnViewAll) not displayed; skipping tap (user may already be joined)."
            )
            return False
        self._tap_any_clickable(
            self.BTN_VIEW_ALL_LOCATORS,
            "Journii join button (btnViewAll)",
            env_key="CUBII_WELLNESS_JOURNII_JOIN_BTN_WAIT_SEC",
            pause_env_key="CUBII_AFTER_WELLNESS_JOIN_TAP_SEC",
            pause_default="1.0",
            required=True,
        )
        return True

    @staticmethod
    def _highlight_looks_like_month_progress(text: str) -> bool:
        """True for joined count or tasks-completed style highlight (e.g. 1/30 tasks completed)."""
        cleaned = (text or "").strip().lower()
        if not cleaned:
            return False
        if re.search(r"\d+/\d+", cleaned):
            return True
        return any(token in cleaned for token in ("task", "completed", "joined"))

    def verify_journii_banner_month_title_and_progress(self) -> None:
        """
        After opening the banner area, assert hero image, month title, and progress highlight
        (tvWJPMonthTitle / tvWJPMonthHighlight — e.g. tasks completed or joined count).
        """
        self.verify_current_month_journii_image()
        title = self._get_visible_text(
            self.TV_WJP_MONTH_TITLE_LOCATORS,
            env_key="CUBII_WELLNESS_JOURNII_BANNER_WAIT_SEC",
            label="Journii banner month title (tvWJPMonthTitle)",
        )
        if not title:
            raise AssertionError(
                "Journii banner month title (tvWJPMonthTitle) is empty."
            )
        highlight = self._get_visible_text(
            self.TV_WJP_MONTH_HIGHLIGHT_LOCATORS,
            env_key="CUBII_WELLNESS_JOURNII_BANNER_WAIT_SEC",
            label="Journii banner month highlight (tvWJPMonthHighlight)",
        )
        if not highlight:
            raise AssertionError(
                "Journii banner month highlight (tvWJPMonthHighlight) is empty."
            )
        if not self._highlight_looks_like_month_progress(highlight):
            raise AssertionError(
                "Journii banner highlight does not look like month progress "
                f"(expected tasks completed or joined text). Got: {highlight!r}"
            )
        self.LOGGER.info(
            "Verified Journii banner: image, title=%r, highlight=%r.",
            title,
            highlight,
        )

    def tap_journii_title_description_arrow(self) -> None:
        """Tap expand/collapse arrow beside month title (tvTitleDescIcon)."""
        self.LOGGER.info("Tap Wellness Journii title description arrow (tvTitleDescIcon).")
        self._tap_any_clickable(
            self.TV_TITLE_DESC_ICON_LOCATORS,
            "Wellness Journii title description arrow (tvTitleDescIcon)",
            env_key="CUBII_WELLNESS_JOURNII_ARROW_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_WELLNESS_ARROW_TAP_SEC",
            pause_default="0.8",
        )

    def verify_journii_description_link_displayed(self) -> None:
        """Assert expanded description link (txtLink) is visible and non-empty."""
        link_text = self._get_visible_text(
            self.TXT_LINK_LOCATORS,
            env_key="CUBII_WELLNESS_JOURNII_LINK_WAIT_SEC",
            label="Wellness Journii description link (txtLink)",
        )
        if not link_text:
            raise AssertionError(
                "Wellness Journii description link (txtLink) is empty. "
                "Expand the section with tvTitleDescIcon first."
            )
        self.LOGGER.info(
            "Verified Wellness Journii description link (txtLink): %r.", link_text
        )

    def tap_journii_download_pdf_link(self) -> None:
        """Tap Download PDF / description link (txtLink)."""
        self.LOGGER.info("Tap Wellness Journii Download PDF link (txtLink).")
        self._tap_any_clickable(
            self.TXT_LINK_LOCATORS,
            "Wellness Journii Download PDF link (txtLink)",
            env_key="CUBII_WELLNESS_JOURNII_PDF_LINK_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_WELLNESS_PDF_LINK_TAP_SEC",
            pause_default="1.2",
        )

    def _cubii_app_package(self) -> str:
        return (os.getenv("APP_PACKAGE") or Settings.APP_PACKAGE or "com.cubii").strip()

    def _chrome_package_hints(self) -> tuple[str, ...]:
        extra = (os.getenv("CUBII_CHROME_PACKAGE") or "").strip()
        packages = list(self.CHROME_PACKAGE_HINTS)
        if extra and extra not in packages:
            packages.insert(0, extra)
        return tuple(packages)

    def _current_package(self) -> str:
        try:
            return (self.driver.current_package or "").strip()
        except Exception:
            return ""

    def _package_looks_like_chrome(self, package_name: str) -> bool:
        pkg = (package_name or "").lower()
        return any(hint in pkg for hint in self._chrome_package_hints())

    def _wait_for_external_browser_foreground(self) -> str:
        """Wait until Chrome (or configured browser) is the foreground app."""
        wait_sec = self._wait_sec("CUBII_WELLNESS_PDF_BROWSER_OPEN_WAIT_SEC", default=15)
        pause = float(os.getenv("CUBII_WELLNESS_PDF_BROWSER_POLL_SEC", "0.5"))
        deadline = time.time() + wait_sec
        last_pkg = ""

        while time.time() < deadline:
            last_pkg = self._current_package()
            if self._package_looks_like_chrome(last_pkg):
                self.LOGGER.info(
                    "External browser in foreground (package=%s).", last_pkg
                )
                time.sleep(float(os.getenv("CUBII_WELLNESS_PDF_BROWSER_SETTLE_SEC", "1.0")))
                return last_pkg
            time.sleep(pause)

        raise AssertionError(
            f"External browser did not open within {wait_sec}s. "
            f"Last foreground package: {last_pkg!r}. "
            f"Expected one of: {self._chrome_package_hints()}."
        )

    def _read_chrome_url_text(self) -> str:
        """Read cubii.com URL from Chrome native URL bar or visible page text."""
        for by, locator in self.CHROME_URL_BAR_LOCATORS:
            try:
                for el in self.driver.find_elements(by, locator):
                    if not el.is_displayed():
                        continue
                    text = (
                        (el.text or "")
                        + " "
                        + (el.get_attribute("text") or "")
                        + " "
                        + (el.get_attribute("content-desc") or "")
                    ).strip()
                    if self.CUBII_URL_HOST_FRAGMENT in text.lower():
                        return text
            except Exception:
                continue

        try:
            for el in self.driver.find_elements(
                AppiumBy.ANDROID_UIAUTOMATOR, self.CHROME_CUBII_URL_TEXT_UIAUTOMATOR
            ):
                if not el.is_displayed():
                    continue
                text = (el.text or "").strip()
                if self.CUBII_URL_HOST_FRAGMENT in text.lower():
                    return text
        except Exception:
            pass

        return ""

    def _read_cubii_url_from_webview_context(self) -> str:
        """Optional fallback when a WEBVIEW context is exposed (Custom Tab)."""
        try:
            contexts = self.driver.contexts or []
        except Exception:
            return ""

        for ctx in contexts:
            if "WEBVIEW" not in (ctx or "").upper():
                continue
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

    def verify_pdf_link_opened_in_external_chrome(self) -> None:
        """
        Assert Download PDF opens an external browser (separate Chrome app), not an
        in-app Close-tab WebView. Verifies foreground package and cubii.com in URL.
        """
        self._wait_for_external_browser_foreground()

        url_text = self._read_chrome_url_text()
        if not url_text:
            url_text = self._read_cubii_url_from_webview_context()

        if not url_text:
            raise AssertionError(
                "Chrome opened but cubii.com URL was not found in the address bar or page. "
                "PDF link may have opened the wrong destination."
            )

        self.LOGGER.info(
            "Verified PDF link opened in external browser with URL text: %r.", url_text
        )

    def return_to_cubii_from_chrome(self) -> None:
        """Leave external Chrome and return focus to the Cubii app (no in-app Close tab)."""
        cubii_pkg = self._cubii_app_package()
        back_attempts = int(os.getenv("CUBII_WELLNESS_PDF_BROWSER_BACK_ATTEMPTS", "2"))
        pause = float(os.getenv("CUBII_WELLNESS_PDF_BROWSER_BACK_PAUSE_SEC", "0.6"))

        self.LOGGER.info("Returning to Cubii from external Chrome (package=%s).", cubii_pkg)

        for attempt in range(back_attempts):
            if self._current_package() == cubii_pkg:
                self.LOGGER.info("Back on Cubii after %s BACK press(es).", attempt)
                break
            try:
                self.driver.press_keycode(ANDROID_KEYCODE_BACK)
                self.LOGGER.info("Pressed BACK (%s/%s) to leave Chrome.", attempt + 1, back_attempts)
            except Exception as exc:
                self.LOGGER.warning("BACK key failed: %s", exc)
            time.sleep(pause)

        if self._current_package() != cubii_pkg:
            try:
                self.driver.activate_app(cubii_pkg)
                self.LOGGER.info("Activated Cubii via activate_app(%s).", cubii_pkg)
            except Exception as exc:
                raise AssertionError(
                    f"Could not return to Cubii from Chrome. "
                    f"Current package={self._current_package()!r}. Error: {exc}"
                ) from exc
            time.sleep(pause)

        try:
            self.driver.switch_to.context("NATIVE_APP")
        except Exception:
            pass

        if self._current_package() != cubii_pkg:
            raise AssertionError(
                f"Expected Cubii foreground ({cubii_pkg!r}) after leaving Chrome, "
                f"got {self._current_package()!r}."
            )
        self.LOGGER.info("Returned to Cubii app from external Chrome.")
        self._pause_after_tap("CUBII_AFTER_RETURN_FROM_CHROME_SEC", "0.8")

    def verify_upcoming_and_previous_tasks_tabs(self) -> None:
        """Assert Upcoming Tasks and Previous/Completed Tasks segment labels are visible."""
        wait_sec = self._wait_sec("CUBII_WELLNESS_TASKS_TABS_WAIT_SEC")
        wait = WebDriverWait(self.driver, wait_sec)
        missing: list[str] = []

        for by, locator in self.UPCOMING_TASKS_TAB_LOCATORS:
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Verified Upcoming Tasks tab (text=%r).", self.UPCOMING_TASKS_TAB_TEXT)
                break
            except TimeoutException:
                continue
        else:
            missing.append(f"Upcoming Tasks tab ({self.UPCOMING_TASKS_TAB_TEXT})")

        previous_found = False
        for by, locator in self.PREVIOUS_TASKS_TAB_LOCATORS:
            try:
                el = wait.until(ec.visibility_of_element_located((by, locator)))
                previous_found = True
                self.LOGGER.info(
                    "Verified Previous/Completed Tasks tab (tvCompletedTasks text=%r).",
                    (el.text or "").strip(),
                )
                break
            except TimeoutException:
                continue
        if not previous_found:
            missing.append("Previous Tasks tab (tvCompletedTasks / Previous Tasks text)")

        if missing:
            raise AssertionError(
                "Wellness Journii task segment tabs not visible: " + ", ".join(missing)
            )

    def tap_upcoming_tasks_tab(self) -> None:
        """Select Upcoming Tasks so rvDays shows upcoming task cards."""
        self.LOGGER.info("Tap Upcoming Tasks tab.")
        self._tap_any_clickable(
            self.UPCOMING_TASKS_TAB_LOCATORS,
            f"Upcoming Tasks tab ({self.UPCOMING_TASKS_TAB_TEXT})",
            env_key="CUBII_WELLNESS_UPCOMING_TAB_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_UPCOMING_TAB_TAP_SEC",
            pause_default="0.6",
        )

    def tap_previous_tasks_tab(self) -> None:
        """Select Previous Tasks (tvCompletedTasks) so rvDays shows completed task cards."""
        self.LOGGER.info("Tap Previous Tasks tab (tvCompletedTasks).")
        self._tap_any_clickable(
            self.PREVIOUS_TASKS_TAB_LOCATORS,
            f"Previous Tasks tab ({self.PREVIOUS_TASKS_TAB_TEXT})",
            env_key="CUBII_WELLNESS_PREVIOUS_TAB_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_PREVIOUS_TAB_TAP_SEC",
            pause_default="0.6",
        )

    @staticmethod
    def _element_has_layout_size(el) -> bool:
        try:
            size = el.size or {}
            return int(size.get("width", 0)) > 0 and int(size.get("height", 0)) > 0
        except Exception:
            return False

    def _element_is_effectively_visible(self, el) -> bool:
        try:
            if el.is_displayed():
                return True
        except Exception:
            pass
        return self._element_has_layout_size(el)

    def _card_has_visible_progress_bar(self, card) -> bool:
        """
        Task progress line under tvTaskName.

        Workout tasks use android.widget.ProgressBar; some categories (e.g. nutrition /
        meditation) may render the same grey line as a thin android.view.View instead.
        """
        searches = (
            (AppiumBy.CLASS_NAME, self.TASK_PROGRESS_BAR_CLASS),
            (AppiumBy.XPATH, './/*[contains(@class,"ProgressBar")]'),
            (
                AppiumBy.XPATH,
                './/*[contains(@resource-id,"progress") or contains(@resource-id,"Progress")]',
            ),
        )
        skip_resource_ids = {
            self.TV_TASK_DATE_ID,
            self.TV_TASK_NAME_ID,
            self.TV_TASK_PEOPLE_JOINED_ID,
            self.TV_WJP_MONTH_HIGHLIGHT_ID,
        }
        for by, locator in searches:
            try:
                for el in card.find_elements(by, locator):
                    rid = (el.get_attribute("resourceId") or "").strip()
                    if rid in skip_resource_ids:
                        continue
                    if self._element_is_effectively_visible(el):
                        return True
            except Exception:
                continue

        return self._llwjptask_has_horizontal_progress_line(card)

    def _llwjptask_has_horizontal_progress_line(self, card) -> bool:
        """Detect a thin horizontal bar inside llWJPTask when it is not a ProgressBar."""
        try:
            for layout in card.find_elements(AppiumBy.ID, self.LL_WJP_TASK_ID):
                if not self._element_is_effectively_visible(layout):
                    continue
                for el in layout.find_elements(AppiumBy.XPATH, ".//*"):
                    try:
                        rid = (el.get_attribute("resourceId") or "").strip()
                        if rid in (
                            self.TV_TASK_NAME_ID,
                            self.TV_TASK_PEOPLE_JOINED_ID,
                            self.LL_WJP_TASK_ID,
                        ):
                            continue
                        class_name = (el.get_attribute("className") or "").strip()
                        if "TextView" in class_name or "ImageView" in class_name:
                            continue
                        if "ProgressBar" in class_name:
                            return True
                        width = int((el.size or {}).get("width", 0))
                        height = int((el.size or {}).get("height", 0))
                        if width > 80 and 0 < height <= 30 and width > height * 3:
                            if self._element_is_effectively_visible(el):
                                return True
                    except Exception:
                        continue
        except Exception:
            pass
        return False

    def _upcoming_task_dedupe_key(self, details: dict[str, tuple[str, bool]]) -> str:
        """Stable key across scroll (position changes); prefer date + task name."""
        date_text, _ = details.get("date", ("", False))
        name_text, name_found = details.get("name", ("", False))
        if not name_found or not name_text.strip():
            return ""
        if date_text.strip():
            return f"{date_text.strip()}|{name_text.strip()}"
        return name_text.strip()

    def _canonical_upcoming_dedupe_key(
        self,
        details: dict[str, tuple[str, bool]],
        *,
        verified_keys: set[str] | None = None,
        seen_keys: set[str] | None = None,
    ) -> str:
        """
        Prefer date|name; merge name-only keys with an existing date|name for same task.
        """
        key = self._upcoming_task_dedupe_key(details)
        if not key or "|" in key:
            return key
        task_name = key
        for bucket in (verified_keys or set(), seen_keys or set()):
            for existing in bucket:
                if "|" not in existing:
                    continue
                _date, name = existing.split("|", 1)
                if name == task_name:
                    return existing
        return key

    def _upcoming_name_already_verified(self, dedupe_key: str, verified_keys: set[str]) -> bool:
        if "|" in dedupe_key or not dedupe_key:
            return dedupe_key in verified_keys
        return any(
            existing.endswith(f"|{dedupe_key}") for existing in verified_keys if "|" in existing
        )

    def _card_has_visible_task_name(self, card) -> bool:
        text, found = self._first_visible_descendant_text(card, self.TV_TASK_NAME_ID)
        return found and bool(text.strip())

    def _card_has_llwjptask(self, card) -> bool:
        try:
            for layout in card.find_elements(AppiumBy.ID, self.LL_WJP_TASK_ID):
                if self._element_is_effectively_visible(layout):
                    return True
        except Exception:
            pass
        return False

    def _frame_layout_row_parent_of(self, element):
        """Return rvDays direct child FrameLayout that wraps a task row."""
        recycler = self._find_rv_days_element()
        current = element
        best = element
        for _ in range(14):
            try:
                parent = current.find_element(AppiumBy.XPATH, "./..")
            except Exception:
                break
            current = parent
            if recycler is not None:
                try:
                    grand = parent.find_element(AppiumBy.XPATH, "./..")
                    if grand.id == recycler.id:
                        return parent
                except Exception:
                    pass
            class_name = (
                parent.get_attribute("className") or parent.get_attribute("class") or ""
            )
            if "FrameLayout" in class_name:
                best = parent
        return best

    def _collect_upcoming_task_cards(self) -> list:
        """
        Return displayed task rows: rvDays FrameLayout that contains llWJPTask + tvTaskName.

        Avoids empty/partial FrameLayout wrappers that caused silent skips at y≈265.
        """
        recycler = self._find_rv_days_element()
        search_roots = [recycler] if recycler is not None else [self.driver]
        cards: list = []
        seen_keys: set[str] = set()

        for root in search_roots:
            try:
                task_layouts = root.find_elements(AppiumBy.XPATH, self.LL_WJP_TASK_REL_XPATH)
            except Exception:
                task_layouts = []
            if not task_layouts and root is self.driver:
                task_layouts = self.driver.find_elements(
                    AppiumBy.XPATH, self.LL_WJP_TASK_XPATH
                )
            for layout in task_layouts:
                try:
                    if not self._element_is_effectively_visible(layout):
                        continue
                    card = self._frame_layout_row_parent_of(layout)
                    if not self._card_has_visible_task_name(card):
                        continue
                    if not self._card_has_llwjptask(card):
                        continue
                    details = self._upcoming_card_details(card)
                    dedupe_key = self._upcoming_task_dedupe_key(details)
                    if not dedupe_key or dedupe_key in seen_keys:
                        continue
                    seen_keys.add(dedupe_key)
                    cards.append(card)
                except Exception:
                    continue

        if cards:
            return cards

        self.LOGGER.warning(
            "Wellness Journii: no llWJPTask rows; falling back to rvDays FrameLayout scan."
        )
        if recycler is None:
            candidates = self.driver.find_elements(AppiumBy.XPATH, self.RV_DAYS_CARD_ABS_XPATH)
        else:
            try:
                candidates = recycler.find_elements(AppiumBy.XPATH, self.RV_DAYS_CARD_REL_XPATH)
            except Exception:
                candidates = []
            if not candidates:
                candidates = self.driver.find_elements(AppiumBy.XPATH, self.RV_DAYS_CARD_ABS_XPATH)
        for card in candidates:
            try:
                if not card.is_displayed():
                    continue
                if not self._card_has_visible_task_name(card) or not self._card_has_llwjptask(card):
                    continue
                dedupe_key = self._upcoming_task_dedupe_key(self._upcoming_card_details(card))
                if not dedupe_key or dedupe_key in seen_keys:
                    continue
                seen_keys.add(dedupe_key)
                cards.append(card)
            except Exception:
                continue
        return cards

    def _upcoming_card_details(self, card) -> dict[str, tuple[str, bool]]:
        date_text, date_found = self._find_task_date_for_row(card)
        name_text, name_found = self._find_task_field(card, self.TV_TASK_NAME_ID)
        people_text, people_found = self._find_task_field(card, self.TV_TASK_PEOPLE_JOINED_ID)
        progress_found = self._card_has_visible_progress_bar(card)
        return {
            "date": (date_text, date_found),
            "name": (name_text, name_found),
            "people_joined": (people_text, people_found),
            "progress": ("", progress_found),
        }

    def _format_upcoming_card_details(self, details: dict[str, tuple[str, bool]]) -> str:
        date_text, date_found = details.get("date", ("", False))
        name_text, name_found = details.get("name", ("", False))
        people_text, people_found = details.get("people_joined", ("", False))
        _progress_text, progress_found = details.get("progress", ("", False))
        return (
            f"task date (tvTaskDate)={date_text!r} (found={date_found}); "
            f"task name (tvTaskName)={name_text!r} (found={name_found}); "
            f"progress bar (found={progress_found}); "
            f"people joined (tvTaskPeopleJoined)={people_text!r} (found={people_found})"
        )

    def _missing_upcoming_card_fields(self, details: dict[str, tuple[str, bool]]) -> list[str]:
        missing: list[str] = []
        date_text, date_found = details.get("date", ("", False))
        name_text, name_found = details.get("name", ("", False))
        people_text, people_found = details.get("people_joined", ("", False))
        _progress_text, progress_found = details.get("progress", ("", False))

        if not date_found or not date_text.strip():
            missing.append("task date (tvTaskDate)")
        if not name_found or not name_text.strip():
            missing.append("task name (tvTaskName)")
        if not progress_found:
            self.LOGGER.debug(
                "Upcoming card %r: no progress bar (optional — skipped).",
                name_text.strip() if name_text.strip() else "unknown",
            )
        if not people_found:
            missing.append("people joined (tvTaskPeopleJoined)")
        elif not people_text.strip():
            self.LOGGER.debug(
                "Upcoming card people-joined label is empty (allowed): %r", people_text
            )
        return missing

    def _verify_upcoming_card_fields(
        self, card_index: int, dedupe_key: str, details: dict[str, tuple[str, bool]]
    ) -> None:
        missing = self._missing_upcoming_card_fields(details)
        if missing:
            self.LOGGER.error(
                "Upcoming task card %s (%s) failed verification. Observed: %s",
                card_index,
                dedupe_key,
                self._format_upcoming_card_details(details),
            )
            raise AssertionError(
                f"Upcoming task card {card_index} ({dedupe_key!r}) is missing fields: "
                f"{', '.join(missing)}. "
                f"Observed: {self._format_upcoming_card_details(details)}"
            )

    def _upcoming_card_details_in_view(self, card) -> dict[str, tuple[str, bool]]:
        """Read card fields after scrolling the whole FrameLayout row into view."""
        try:
            self._scroll_task_row_into_view(card, for_upcoming=True)
            time.sleep(float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4")) * 0.5)
        except Exception:
            pass
        return self._upcoming_card_details(card)

    def _scroll_upcoming_list_to_top(self) -> None:
        up_scrolls = int(os.getenv("CUBII_WELLNESS_UPCOMING_TASKS_SCROLL_UP_ATTEMPTS", "8"))
        pause = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4"))
        for _ in range(up_scrolls):
            self._scroll_upcoming_tasks_list("up")
            time.sleep(pause)

    def tap_upcoming_tasks_filter_option(self) -> None:
        """Open the filter sheet via the floating FILTERS control (cvShowFilters)."""
        self.LOGGER.info("Tap upcoming tasks filter (cvShowFilters / FILTERS).")
        self._tap_any_clickable(
            self.UPCOMING_TASKS_FILTER_LOCATORS,
            f'Upcoming tasks filter (cvShowFilters / "{self.UPCOMING_TASKS_FILTER_TEXT}")',
            env_key="CUBII_WELLNESS_FILTER_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_FILTER_OPEN_SEC",
            pause_default="0.8",
        )

    def tap_incomplete_filter_option(self) -> None:
        """Select Incomplete on the filter sheet (mcvIncomplete)."""
        self.LOGGER.info("Tap Incomplete filter option (mcvIncomplete).")
        self._tap_any_clickable(
            self.MCV_INCOMPLETE_LOCATORS,
            "Incomplete filter (mcvIncomplete)",
            env_key="CUBII_WELLNESS_INCOMPLETE_FILTER_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_INCOMPLETE_FILTER_TAP_SEC",
            pause_default="0.5",
        )

    def tap_completed_filter_option(self) -> None:
        """Select Completed on the filter sheet (mcvCompleted)."""
        self.LOGGER.info("Tap Completed filter option (mcvCompleted).")
        self._tap_any_clickable(
            self.MCV_COMPLETED_LOCATORS,
            "Completed filter (mcvCompleted)",
            env_key="CUBII_WELLNESS_COMPLETED_FILTER_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_COMPLETED_FILTER_TAP_SEC",
            pause_default="0.5",
        )

    def tap_all_filter_option(self) -> None:
        """Select All on the filter sheet (mcvAll)."""
        self.LOGGER.info("Tap All filter option (mcvAll).")
        self._tap_any_clickable(
            self.MCV_ALL_LOCATORS,
            "All filter (mcvAll)",
            env_key="CUBII_WELLNESS_ALL_FILTER_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_ALL_FILTER_TAP_SEC",
            pause_default="0.5",
        )

    def tap_filter_show_results(self) -> None:
        """Apply filter and return to the upcoming task list (btnShowResults)."""
        self.LOGGER.info("Tap Show Results (btnShowResults).")
        self._tap_any_clickable(
            self.BTN_SHOW_RESULTS_LOCATORS,
            "Show Results (btnShowResults)",
            env_key="CUBII_WELLNESS_SHOW_RESULTS_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_SHOW_RESULTS_TAP_SEC",
            pause_default="1.0",
        )
        self._wait_for_visible(
            self.RV_DAYS_LOCATORS,
            env_key="CUBII_WELLNESS_SHOW_RESULTS_WAIT_SEC",
            label="Filtered upcoming tasks list (rvDays)",
        )

    def _is_filter_no_results_visible(self, *, wait: bool = False) -> bool:
        """True when the filtered upcoming list shows the no-results empty state."""

        def _visible(_driver) -> bool:
            for by, locator in self.FILTER_NO_RESULTS_FOUND_LOCATORS:
                try:
                    el = _driver.find_element(by, locator)
                    if el.is_displayed() and (el.text or "").strip():
                        return True
                except Exception:
                    continue
            return False

        if wait:
            wait_sec = self._wait_sec("CUBII_WELLNESS_FILTER_NO_RESULTS_WAIT_SEC", default=15)
            try:
                WebDriverWait(self.driver, wait_sec).until(_visible)
                return True
            except TimeoutException:
                return False
        return self._is_any_visible(
            self.FILTER_NO_RESULTS_FOUND_LOCATORS, require_text=True
        )

    def verify_filter_no_results_empty_state(self) -> None:
        """
        Assert filtered upcoming list empty state after Show Results.

        Expects: No results found, Try removing some filters, Clear Filter button.
        """
        self.LOGGER.info("Verify filtered upcoming tasks no-results empty state.")
        debounce = float(os.getenv("CUBII_WELLNESS_FILTER_NO_RESULTS_DEBOUNCE_SEC", "1.0"))
        time.sleep(debounce)
        wait_sec = self._wait_sec("CUBII_WELLNESS_FILTER_NO_RESULTS_VERIFY_WAIT_SEC", default=20)
        missing: list[str] = []

        def _must_see(locator_triplets: tuple[tuple, ...], description: str) -> None:
            def _any_visible(_driver):
                for by, locator in locator_triplets:
                    try:
                        el = _driver.find_element(by, locator)
                        if el.is_displayed():
                            return el
                    except Exception:
                        continue
                return False

            try:
                WebDriverWait(self.driver, wait_sec).until(_any_visible)
            except TimeoutException:
                missing.append(description)

        _must_see(
            self.FILTER_NO_RESULTS_FOUND_LOCATORS,
            f'"{self.FILTER_NO_RESULTS_FOUND_TEXT}" (TextView)',
        )
        _must_see(
            self.FILTER_TRY_REMOVING_FILTERS_LOCATORS,
            f'"{self.FILTER_TRY_REMOVING_FILTERS_TEXT}" (TextView)',
        )
        _must_see(
            self.BTN_CLEAR_FILTER_LOCATORS,
            "Clear Filter (btnClearFilter)",
        )
        if missing:
            raise AssertionError(
                "Filtered upcoming no-results empty state verification failed. "
                f"Missing: {', '.join(missing)}"
            )
        self.LOGGER.info(
            "Verified no-results empty state: %r, %r, btnClearFilter visible.",
            self.FILTER_NO_RESULTS_FOUND_TEXT,
            self.FILTER_TRY_REMOVING_FILTERS_TEXT,
        )

    def _verify_filtered_upcoming_results(self, *, log_label: str, min_tasks: int) -> None:
        """
        After a filter + Show Results, verify task cards OR the no-results empty state.
        """
        self.LOGGER.info(
            "Verify %s filter results (task cards or no-results empty state, min_tasks=%s).",
            log_label,
            min_tasks,
        )
        debounce = float(os.getenv("CUBII_WELLNESS_FILTER_RESULTS_DEBOUNCE_SEC", "1.0"))
        time.sleep(debounce)

        if self._is_filter_no_results_visible(wait=True):
            self.verify_filter_no_results_empty_state()
            self.LOGGER.info("Verified %s filter: no-results empty state.", log_label)
            return

        cards = self._collect_upcoming_task_cards()
        if not cards and self._is_filter_no_results_visible(wait=True):
            self.verify_filter_no_results_empty_state()
            self.LOGGER.info("Verified %s filter: no-results empty state.", log_label)
            return

        if not cards:
            raise AssertionError(
                f"No {log_label} task cards under rvDays and no "
                f'"{self.FILTER_NO_RESULTS_FOUND_TEXT}" empty state after applying filter.'
            )

        self.verify_all_upcoming_task_cards(
            min_tasks=min_tasks,
            log_label=log_label,
            tap_upcoming_tab=False,
        )

    def verify_all_filtered_incomplete_upcoming_tasks(self) -> None:
        """
        After Incomplete filter + Show Results, verify task cards or no-results empty state.
        """
        min_tasks = int(os.getenv("CUBII_WELLNESS_FILTERED_INCOMPLETE_MIN_TASKS", "1"))
        self._verify_filtered_upcoming_results(
            log_label="filtered incomplete", min_tasks=min_tasks
        )

    def verify_all_filtered_complete_upcoming_tasks(self) -> None:
        """
        After Completed filter + Show Results, verify task cards or no-results empty state.
        """
        min_tasks = int(os.getenv("CUBII_WELLNESS_FILTERED_COMPLETE_MIN_TASKS", "1"))
        self._verify_filtered_upcoming_results(
            log_label="filtered complete", min_tasks=min_tasks
        )

    def verify_all_filtered_all_upcoming_tasks(self) -> None:
        """
        After All filter + Show Results, verify task cards or no-results empty state.
        """
        min_tasks = int(os.getenv("CUBII_WELLNESS_FILTERED_ALL_MIN_TASKS", "8"))
        self._verify_filtered_upcoming_results(log_label="filtered All", min_tasks=min_tasks)

    def verify_all_upcoming_task_cards(
        self,
        *,
        min_tasks: int | None = None,
        log_label: str = "upcoming",
        tap_upcoming_tab: bool = True,
    ) -> None:
        """
        Single pass: scroll rvDays with small steps, verify each llWJPTask row once.

        Tracks seen vs verified keys; fails if any seen task could not be verified.
        """
        self._wait_for_visible(self.RV_DAYS_LOCATORS, label="Journii tasks list (rvDays)")
        if tap_upcoming_tab:
            self.tap_upcoming_tasks_tab()

        max_scrolls = int(os.getenv("CUBII_WELLNESS_UPCOMING_TASKS_SCROLL_ATTEMPTS", "35"))
        pause = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4"))
        empty_passes_to_stop = int(
            os.getenv("CUBII_WELLNESS_UPCOMING_TASKS_EMPTY_PASSES_TO_STOP", "3")
        )
        if min_tasks is None:
            min_tasks = int(os.getenv("CUBII_WELLNESS_UPCOMING_MIN_TASKS", "8"))

        self._scroll_upcoming_list_to_top()
        time.sleep(pause)

        verified_keys: set[str] = set()
        seen_keys: set[str] = set()
        card_index = 0
        consecutive_no_new_seen = 0

        for scroll_attempt in range(max_scrolls + 1):
            before_seen = len(seen_keys)
            before_verified = len(verified_keys)
            cards = self._collect_upcoming_task_cards()
            self.LOGGER.info(
                "Wellness Journii %s: scroll %s — %s task card(s), %s seen, %s verified.",
                log_label,
                scroll_attempt,
                len(cards),
                len(seen_keys),
                len(verified_keys),
            )

            for card in cards:
                details = self._upcoming_card_details_in_view(card)
                dedupe_key = self._canonical_upcoming_dedupe_key(
                    details, verified_keys=verified_keys, seen_keys=seen_keys
                )
                if not dedupe_key:
                    self.LOGGER.warning(
                        "Skipping rvDays row without date/name on scroll %s: %s",
                        scroll_attempt,
                        self._format_upcoming_card_details(details),
                    )
                    continue

                if self._upcoming_name_already_verified(dedupe_key, verified_keys):
                    continue

                if dedupe_key not in seen_keys:
                    seen_keys.add(dedupe_key)
                    self.LOGGER.info(
                        "Seen upcoming task on scroll %s: %s",
                        scroll_attempt,
                        dedupe_key,
                    )

                if dedupe_key in verified_keys:
                    continue

                missing = self._missing_upcoming_card_fields(details)
                if missing:
                    details = self._upcoming_card_details_in_view(card)
                    missing = self._missing_upcoming_card_fields(details)
                if missing:
                    self.LOGGER.info(
                        "Task %s not verified yet (missing %s); will retry on next scroll.",
                        dedupe_key,
                        ", ".join(missing),
                    )
                    continue

                card_index += 1
                self._verify_upcoming_card_fields(card_index, dedupe_key, details)
                verified_keys.add(dedupe_key)
                self.LOGGER.info(
                    "Verified upcoming task %s (%s): %s",
                    len(verified_keys),
                    dedupe_key,
                    self._format_upcoming_card_details(details),
                )

            added_seen = len(seen_keys) - before_seen
            added_verified = len(verified_keys) - before_verified
            if added_seen == 0:
                consecutive_no_new_seen += 1
            else:
                consecutive_no_new_seen = 0

            self.LOGGER.info(
                "Wellness Journii %s: scroll %s done — +%s seen, +%s verified "
                "(totals %s seen / %s verified).",
                log_label,
                scroll_attempt,
                added_seen,
                added_verified,
                len(seen_keys),
                len(verified_keys),
            )

            if consecutive_no_new_seen >= empty_passes_to_stop:
                self.LOGGER.info(
                    "Stopping scroll: %s consecutive passes with no newly seen tasks.",
                    consecutive_no_new_seen,
                )
                break
            if scroll_attempt >= max_scrolls:
                break

            self._scroll_upcoming_tasks_list("down")
            time.sleep(pause)

        if not verified_keys:
            raise AssertionError(
                f"No {log_label} tasks found under rvDays after scrolling the full list."
            )

        unverified = seen_keys - verified_keys
        unverified = {
            key
            for key in unverified
            if not self._upcoming_name_already_verified(key, verified_keys)
        }
        if unverified:
            raise AssertionError(
                f"Verified {len(verified_keys)} of {len(seen_keys)} seen {log_label} task(s). "
                f"Could not verify: {sorted(unverified)}."
            )

        if len(verified_keys) < min_tasks:
            raise AssertionError(
                f"Only {len(verified_keys)} {log_label} task(s) verified; expected at least "
                f"{min_tasks}. Seen keys: {sorted(seen_keys)}."
            )

        self.LOGGER.info(
            "Verified all %s seen %s task(s) with date, name, and people joined "
            "(progress bar optional).",
            len(verified_keys),
            log_label,
        )

    def _journii_banner_visible_in_upper_viewport(self) -> bool:
        """True when hero image or month title is displayed in the upper part of the screen."""
        screen_h = self.driver.get_window_size().get("height", 2000)
        upper_bound = int(screen_h * float(os.getenv("CUBII_WELLNESS_BANNER_VIEWPORT_MAX_Y", "0.42")))
        locator_sets = (
            self.IV_JOURNII_IMAGE_LOCATORS,
            self.TV_WJP_MONTH_TITLE_LOCATORS,
        )
        for locator_triplets in locator_sets:
            for by, locator in locator_triplets:
                try:
                    for el in self.driver.find_elements(by, locator):
                        if not self._element_is_effectively_visible(el):
                            continue
                        y = int((el.location or {}).get("y", -1))
                        if 0 <= y <= upper_bound:
                            return True
                except Exception:
                    continue
        return False

    def scroll_up_to_journii_banner(self) -> None:
        """
        Scroll the Wellness Journii detail screen up until the month banner is visible.

        Used after scrolling through the upcoming tasks list back to ivJourniiImage /
        tvWJPMonthTitle at the top.
        """
        max_scrolls = int(os.getenv("CUBII_WELLNESS_SCROLL_TO_BANNER_UP_ATTEMPTS", "14"))
        pause = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4"))
        percent = float(os.getenv("CUBII_WELLNESS_SCROLL_TO_BANNER_PERCENT", "0.55"))

        if self._journii_banner_visible_in_upper_viewport():
            self.LOGGER.info("Journii banner already visible; no scroll needed.")
        else:
            for scroll_attempt in range(max_scrolls):
                self._scroll_tasks_list("up", percent=percent)
                time.sleep(pause)
                if self._journii_banner_visible_in_upper_viewport():
                    self.LOGGER.info(
                        "Journii banner visible after %s scroll-up(s).",
                        scroll_attempt + 1,
                    )
                    break
            else:
                raise AssertionError(
                    f"Journii banner (ivJourniiImage / tvWJPMonthTitle) not visible in the "
                    f"upper viewport after {max_scrolls} scroll-up gestures."
                )

        self.verify_current_month_journii_image()
        title = self._get_visible_text(
            self.TV_WJP_MONTH_TITLE_LOCATORS,
            env_key="CUBII_WELLNESS_JOURNII_BANNER_WAIT_SEC",
            label="Journii banner month title (tvWJPMonthTitle)",
        )
        if not title:
            raise AssertionError(
                "Journii banner month title (tvWJPMonthTitle) not visible after scrolling up."
            )
        self.LOGGER.info("Scrolled up to Journii banner; title=%r.", title)

    def _previous_card_details(self, card) -> dict[str, tuple[str, bool]]:
        """Previous task row: rvDays/FrameLayout with tvTaskDate, tvTaskName, tvTaskPeopleJoined."""
        date_text, date_found = self._find_task_date_for_row(card)
        name_text, name_found = self._find_task_field(card, self.TV_TASK_NAME_ID)
        people_text, people_found = self._find_task_field(card, self.TV_TASK_PEOPLE_JOINED_ID)
        return {
            "date": (date_text, date_found),
            "name": (name_text, name_found),
            "people_joined": (people_text, people_found),
        }

    def _format_previous_card_details(self, details: dict[str, tuple[str, bool]]) -> str:
        date_text, date_found = details.get("date", ("", False))
        name_text, name_found = details.get("name", ("", False))
        people_text, people_found = details.get("people_joined", ("", False))
        return (
            f"task date (tvTaskDate)={date_text!r} (found={date_found}); "
            f"task name (tvTaskName)={name_text!r} (found={name_found}); "
            f"people joined (tvTaskPeopleJoined)={people_text!r} (found={people_found})"
        )

    def _missing_previous_card_fields(self, details: dict[str, tuple[str, bool]]) -> list[str]:
        missing: list[str] = []
        date_text, date_found = details.get("date", ("", False))
        name_text, name_found = details.get("name", ("", False))
        people_text, people_found = details.get("people_joined", ("", False))

        if not date_found or not date_text.strip():
            missing.append("task date (tvTaskDate)")
        if not name_found or not name_text.strip():
            missing.append("task name (tvTaskName)")
        if not people_found:
            missing.append("people joined (tvTaskPeopleJoined)")
        elif not people_text.strip():
            self.LOGGER.debug(
                "Previous card people-joined label is empty (allowed): %r", people_text
            )
        return missing

    def _verify_previous_card_fields(
        self, card_index: int, dedupe_key: str, details: dict[str, tuple[str, bool]]
    ) -> None:
        missing = self._missing_previous_card_fields(details)
        if missing:
            self.LOGGER.error(
                "Previous task card %s (%s) failed verification. Observed: %s",
                card_index,
                dedupe_key,
                self._format_previous_card_details(details),
            )
            raise AssertionError(
                f"Previous task card {card_index} ({dedupe_key!r}) is missing fields: "
                f"{', '.join(missing)}. "
                f"Observed: {self._format_previous_card_details(details)}"
            )

    def _previous_card_details_in_view(self, card) -> dict[str, tuple[str, bool]]:
        try:
            self._scroll_task_row_into_view(card, for_upcoming=True)
            time.sleep(float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4")) * 0.5)
        except Exception:
            pass
        return self._previous_card_details(card)

    def _scroll_previous_list_to_top(self) -> None:
        up_scrolls = int(os.getenv("CUBII_WELLNESS_PREVIOUS_TASKS_SCROLL_UP_ATTEMPTS", "8"))
        pause = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4"))
        for _ in range(up_scrolls):
            self._scroll_upcoming_tasks_list("up")
            time.sleep(pause)

    def verify_all_previous_task_cards(self) -> None:
        """
        Scroll rvDays on Previous Tasks tab and verify each FrameLayout task card.

        Card: rvDays/android.widget.FrameLayout with tvTaskDate, tvTaskName,
        tvTaskPeopleJoined (same structure as upcoming; no progress bar required).
        """
        self._wait_for_visible(self.RV_DAYS_LOCATORS, label="Journii tasks list (rvDays)")
        self.tap_previous_tasks_tab()

        max_scrolls = int(os.getenv("CUBII_WELLNESS_PREVIOUS_TASKS_SCROLL_ATTEMPTS", "35"))
        pause = float(os.getenv("CUBII_WELLNESS_JOURNII_TASKS_SCROLL_PAUSE_SEC", "0.4"))
        empty_passes_to_stop = int(
            os.getenv("CUBII_WELLNESS_PREVIOUS_TASKS_EMPTY_PASSES_TO_STOP", "3")
        )
        min_tasks = int(os.getenv("CUBII_WELLNESS_PREVIOUS_MIN_TASKS", "1"))

        self._scroll_previous_list_to_top()
        time.sleep(pause)

        verified_keys: set[str] = set()
        seen_keys: set[str] = set()
        card_index = 0
        consecutive_no_new_seen = 0

        for scroll_attempt in range(max_scrolls + 1):
            before_seen = len(seen_keys)
            before_verified = len(verified_keys)
            cards = self._collect_upcoming_task_cards()
            self.LOGGER.info(
                "Wellness Journii previous: scroll %s — %s task card(s), "
                "%s seen, %s verified.",
                scroll_attempt,
                len(cards),
                len(seen_keys),
                len(verified_keys),
            )

            for card in cards:
                details = self._previous_card_details_in_view(card)
                dedupe_key = self._upcoming_task_dedupe_key(details)
                if not dedupe_key:
                    self.LOGGER.warning(
                        "Skipping previous rvDays row without date/name on scroll %s: %s",
                        scroll_attempt,
                        self._format_previous_card_details(details),
                    )
                    continue

                if dedupe_key not in seen_keys:
                    seen_keys.add(dedupe_key)
                    self.LOGGER.info(
                        "Seen previous task on scroll %s: %s",
                        scroll_attempt,
                        dedupe_key,
                    )

                if dedupe_key in verified_keys:
                    continue

                missing = self._missing_previous_card_fields(details)
                if missing:
                    details = self._previous_card_details_in_view(card)
                    missing = self._missing_previous_card_fields(details)
                if missing:
                    self.LOGGER.info(
                        "Previous task %s not verified yet (missing %s); retry next scroll.",
                        dedupe_key,
                        ", ".join(missing),
                    )
                    continue

                card_index += 1
                self._verify_previous_card_fields(card_index, dedupe_key, details)
                verified_keys.add(dedupe_key)
                self.LOGGER.info(
                    "Verified previous task %s (%s): %s",
                    len(verified_keys),
                    dedupe_key,
                    self._format_previous_card_details(details),
                )

            added_seen = len(seen_keys) - before_seen
            if added_seen == 0:
                consecutive_no_new_seen += 1
            else:
                consecutive_no_new_seen = 0

            self.LOGGER.info(
                "Wellness Journii previous: scroll %s done — +%s seen, +%s verified "
                "(totals %s seen / %s verified).",
                scroll_attempt,
                len(seen_keys) - before_seen,
                len(verified_keys) - before_verified,
                len(seen_keys),
                len(verified_keys),
            )

            if consecutive_no_new_seen >= empty_passes_to_stop:
                self.LOGGER.info(
                    "Stopping previous scroll: %s passes with no newly seen tasks.",
                    consecutive_no_new_seen,
                )
                break
            if scroll_attempt >= max_scrolls:
                break

            self._scroll_upcoming_tasks_list("down")
            time.sleep(pause)

        if not verified_keys:
            raise AssertionError(
                "No previous tasks found under rvDays after scrolling the Previous Tasks list."
            )

        unverified = seen_keys - verified_keys
        if unverified:
            raise AssertionError(
                f"Verified {len(verified_keys)} of {len(seen_keys)} seen previous task(s). "
                f"Could not verify: {sorted(unverified)}."
            )

        if len(verified_keys) < min_tasks:
            raise AssertionError(
                f"Only {len(verified_keys)} previous task(s) verified; expected at least "
                f"{min_tasks}. Seen keys: {sorted(seen_keys)}."
            )

        self.LOGGER.info(
            "Verified all %s seen previous task(s) with date, name, and people joined.",
            len(verified_keys),
        )

    def tap_journii_detail_back_button(self) -> None:
        """Tap Back on the Journii screen (toolbar control or Back text)."""
        self.LOGGER.info("Tap Back on Journii screen (toolbar / Back text).")
        self._tap_any_clickable(
            self.DETAIL_BACK_LOCATORS,
            f'Back button (toolbar / text="{self.DETAIL_BACK_TEXT}")',
            env_key="CUBII_WELLNESS_JOURNII_BACK_TAP_WAIT_SEC",
            pause_env_key="CUBII_AFTER_JOURNII_BACK_TAP_SEC",
            pause_default="0.6",
        )
