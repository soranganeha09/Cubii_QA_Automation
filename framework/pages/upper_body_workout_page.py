import calendar
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


class UpperBodyWorkoutPage(BasePage):
    """Upper Body workout set entry flow from Progress / In Progress."""

    LOGGER = logging.getLogger("cubii_upper_body_workout_page")

    TAB_UPPER_BODY_ID = "com.cubii:id/txtUpperBody"
    DATE_RANGE_TITLE_ID = "com.cubii:id/txtTitleDateRange"
    NO_WORKOUT_DATA_TEXT = "No workout data"

    ADD_WORKOUT_SET_BUTTON_ID = "com.cubii:id/btnAddManualWorkout"
    ADD_WORKOUT_SET_TEXTS = ("ADD WORKOUT SET", "ADD WORKOUT SETS")
    ADD_EDIT_WORKOUT_TITLE_ID = "com.cubii:id/txtAddEditWorkoutTitle"
    WORKOUT_FTUE_GOT_IT_ID = "com.cubii:id/btnGotIt"

    START_DATE_VALUE_ID = "com.cubii:id/tvStartDateWorkout"
    DATE_PICKER_XPATH = "//android.widget.DatePicker"
    ANDROID_OK_BUTTON_ID = "android:id/button1"

    TIME_VALUE_ID = "com.cubii:id/tvTime"
    TIME_PICKER_XPATH = (
        '//android.widget.TimePicker[@resource-id="android:id/timePicker"]'
        "/android.widget.LinearLayout"
    )
    TIME_PICKER_RADIAL_ID = "android:id/radial_picker"
    TIME_PICKER_AM_LABEL_ID = "android:id/am_label"
    TIME_PICKER_PM_LABEL_ID = "android:id/pm_label"
    TIME_PICKER_HOURS_CHIP_ID = "android:id/hours"
    TIME_PICKER_MINUTES_CHIP_ID = "android:id/minutes"

    EXERCISE_OPTIONS = (
        "Chest Fly",
        "Bicep Curls",
        "Front Raises",
        "Upright Row",
        "Overhead Press",
        "Back Flies",
        "Cross Body Rows",
        "Triceps",
    )

    EXERCISE_SETS_RECYCLER_ID = "com.cubii:id/rvExerciseSets"
    REPS_INPUT_ID = "com.cubii:id/etReps"
    REPS_MINUS_ID = "com.cubii:id/ivMinus"
    REPS_PLUS_ID = "com.cubii:id/ivPlus"
    SAVE_WORKOUT_BUTTON_ID = "com.cubii:id/btnSaveManualEntry"
    LL_ADD_SETS_ID = "com.cubii:id/llAddSets"

    ENTRY_POPUP_CARD_ID = "com.cubii:id/cardChiirMotivatedParent"
    ENTRY_POPUP_TITLE_ID = "com.cubii:id/txtUpwWorkoutEntryInfoTitle"
    ENTRY_POPUP_REPS_RECYCLER_ID = "com.cubii:id/rcyUpwEntryReps"
    ENTRY_POPUP_SET_ID = "com.cubii:id/txtSet"
    ENTRY_POPUP_REPS_ID = "com.cubii:id/txtReps"
    ENTRY_POPUP_GOT_IT_ID = "com.cubii:id/btnUbwEntryGotIt"

    ENTRY_CARD_ROOT_ID = "com.cubii:id/cnsLayoutActivityLogRoot"
    ENTRY_CARD_TIME_ID = "com.cubii:id/txtWorkoutDayTime"

    @staticmethod
    def _standalone_integer_in_text(value, text):
        """True if `value` appears as its own number in `text` (avoids 20 matching inside 120)."""
        return bool(re.search(rf"(?<!\d){int(value)}(?!\d)", text or ""))

    def open_upper_body_tab(self):
        self.LOGGER.info("Upper Body: open tab.")
        self._tap_by_id_or_uiautomator(self.TAB_UPPER_BODY_ID, "Upper Body tab")
        time.sleep(float(os.getenv("CUBII_UPPER_BODY_TAB_SETTLE_SEC", "0.8")))
        self._upper_body_tab_opened = True

    def open_upper_body_tab_and_record_baseline(self):
        self.open_upper_body_tab()
        return self.record_upper_body_baseline()

    def record_upper_body_baseline(self):
        self.LOGGER.info("Upper Body: record current list state.")
        self._assert_add_workout_set_visible()
        empty_visible = self._is_text_visible(self.NO_WORKOUT_DATA_TEXT, timeout=2)
        entry_count = self._count_visible_entry_cards()
        date_title = self._read_text_if_visible(AppiumBy.ID, self.DATE_RANGE_TITLE_ID, timeout=3)
        self._baseline_entry_count = entry_count
        self._baseline_empty_state = empty_visible
        self.LOGGER.info(
            "Upper Body baseline: empty=%s entry_count=%s date_title=%r",
            empty_visible,
            entry_count,
            date_title,
        )
        if empty_visible:
            assert entry_count == 0, (
                "Upper Body shows `No workout data` but visible entry cards were also detected "
                f"(count={entry_count})."
            )
        return {
            "empty": empty_visible,
            "entry_count": entry_count,
            "date_title": date_title,
        }

    def add_upper_body_workout(self, row1_reps, row2_reps, input_mode):
        if not getattr(self, "_upper_body_tab_opened", False):
            self.open_upper_body_tab()
        if not hasattr(self, "_baseline_entry_count"):
            self.record_upper_body_baseline()

        mode = (input_mode or "").strip().lower().replace("_", "-")
        self._current_expected = {
            "row1_reps": int(row1_reps),
            "row2_reps": int(row2_reps),
            "input_mode": mode,
        }

        self._tap_add_workout_set()
        self._dismiss_optional_ftue_got_it()
        self._assert_add_workout_screen_visible()
        self._select_start_date_current_and_confirm()
        selected_time = self._select_random_past_time_and_confirm()
        exercise = self._select_random_exercise()

        if mode in {"manual", "manual-entry", "manual add", "manual-add"}:
            self._set_reps_manually(0, int(row1_reps))
            self._set_reps_manually(1, int(row2_reps))
        elif mode in {"plus-minus", "plus/minus", "plusminus"}:
            self._set_reps_with_buttons(0, int(row1_reps), prefer_plus=True)
            self._set_reps_with_buttons(1, int(row2_reps), prefer_plus=False)
        else:
            raise AssertionError(
                f"Unsupported Upper Body reps input mode: {input_mode!r}. "
                "Use `plus-minus` or `manual`."
            )

        self._current_expected.update(
            {
                "exercise": exercise,
                "selected_time": selected_time,
                "total_reps": int(row1_reps) + int(row2_reps),
            }
        )
        self._tap_save_workout()
        self.LOGGER.info(
            "Upper Body workout submitted: exercise=%s time=%s reps=%s/%s mode=%s",
            exercise,
            selected_time,
            row1_reps,
            row2_reps,
            mode,
        )
        return dict(self._current_expected)

    def add_upper_body_workout_with_three_sets(self, row1_reps, row2_reps, row3_reps, input_mode):
        """Open manual Upper Body editor, fill two sets, tap + ADD SETS, fill third set, save."""
        if not getattr(self, "_upper_body_tab_opened", False):
            self.open_upper_body_tab()
        if not hasattr(self, "_baseline_entry_count"):
            self.record_upper_body_baseline()

        mode = (input_mode or "").strip().lower().replace("_", "-")
        self._current_expected = {
            "row1_reps": int(row1_reps),
            "row2_reps": int(row2_reps),
            "row3_reps": int(row3_reps),
            "input_mode": mode,
        }

        self._tap_add_workout_set()
        self._dismiss_optional_ftue_got_it()
        self._assert_add_workout_screen_visible()
        self._select_start_date_current_and_confirm()
        selected_time = self._select_random_past_time_and_confirm()
        exercise = self._select_random_exercise()

        if mode in {"manual", "manual-entry", "manual add", "manual-add"}:
            self._set_reps_manually(0, int(row1_reps))
            self._set_reps_manually(1, int(row2_reps))
        elif mode in {"plus-minus", "plus/minus", "plusminus"}:
            self._set_reps_with_buttons(0, int(row1_reps), prefer_plus=True)
            self._set_reps_with_buttons(1, int(row2_reps), prefer_plus=False)
        else:
            raise AssertionError(
                f"Unsupported Upper Body reps input mode: {input_mode!r}. "
                "Use `plus-minus` or `manual`."
            )

        self._scroll_add_workout_editor_for_add_sets_button()
        self._tap_ll_add_sets()

        if mode in {"manual", "manual-entry", "manual add", "manual-add"}:
            self._set_reps_manually(2, int(row3_reps))
        else:
            self._set_reps_with_buttons(2, int(row3_reps), prefer_plus=True)

        self._current_expected.update(
            {
                "exercise": exercise,
                "selected_time": selected_time,
                "total_reps": int(row1_reps) + int(row2_reps) + int(row3_reps),
            }
        )
        self._tap_save_workout()
        self.LOGGER.info(
            "Upper Body 3-set workout submitted: exercise=%s time=%s reps=%s/%s/%s mode=%s",
            exercise,
            selected_time,
            row1_reps,
            row2_reps,
            row3_reps,
            mode,
        )
        return dict(self._current_expected)

    @staticmethod
    def _popup_title_contains_today_date(title):
        """Allow full/short month and optional leading-zero day in popup title date."""
        now = datetime.now()
        month_full = calendar.month_name[now.month]
        month_abbr = calendar.month_abbr[now.month]
        day = now.day
        year = now.year
        patterns = (
            rf"{month_full}\s+0?{day},\s+{year}",
            rf"{month_abbr}\s+0?{day},\s+{year}",
        )
        return any(re.search(pattern, title) for pattern in patterns)

    def verify_workout_entry_popup(self, row1_reps, row2_reps):
        expected = self._require_current_expected(row1_reps, row2_reps)
        self._wait_visible(
            AppiumBy.ID,
            self.ENTRY_POPUP_CARD_ID,
            "Upper Body post-save popup card",
            timeout=15,
        )
        title = self._read_text_if_visible(
            AppiumBy.ID, self.ENTRY_POPUP_TITLE_ID, "Upper Body popup title", timeout=8
        )
        assert title, "Upper Body workout entry popup title is empty."
        assert expected["exercise"].lower() in title.lower(), (
            f"Popup title does not contain exercise {expected['exercise']!r}: {title!r}"
        )
        assert self._popup_title_contains_today_date(title), (
            "Popup title does not include today's date in accepted formats "
            "(e.g., June 2, 2026 or Jun 02, 2026). "
            f"observed {title!r}."
        )

        self._assert_popup_reps_row(1, 1, int(row1_reps))
        self._assert_popup_reps_row(2, 2, int(row2_reps))
        self.LOGGER.info(
            "Upper Body popup verified: title=%r row1=%s row2=%s",
            title,
            row1_reps,
            row2_reps,
        )

    def verify_workout_entry_popup_three_sets_with_scroll(self, row1_reps, row2_reps, row3_reps):
        """Confirm post-save popup title and each set row; scrolls `rcyUpwEntryReps` so off-screen rows are reachable."""
        expected = self._require_current_expected_three(row1_reps, row2_reps, row3_reps)
        self._wait_visible(
            AppiumBy.ID,
            self.ENTRY_POPUP_CARD_ID,
            "Upper Body post-save popup card",
            timeout=15,
        )
        title = self._read_text_if_visible(
            AppiumBy.ID, self.ENTRY_POPUP_TITLE_ID, "Upper Body popup title", timeout=8
        )
        assert title, "Upper Body workout entry popup title is empty."
        assert expected["exercise"].lower() in title.lower(), (
            f"Popup title does not contain exercise {expected['exercise']!r}: {title!r}"
        )
        assert self._popup_title_contains_today_date(title), (
            "Popup title does not include today's date in accepted formats "
            "(e.g., June 2, 2026 or Jun 02, 2026). "
            f"observed {title!r}."
        )

        # RecyclerView often opens partially scrolled; reset to top so row 1's txtReps is reachable.
        self._scroll_popup_reps_recycler_reset_top()

        for set_no, reps in (
            (1, int(row1_reps)),
            (2, int(row2_reps)),
            (3, int(row3_reps)),
        ):
            self._scroll_popup_set_row_into_view(set_no)
            self._assert_popup_reps_row(set_no, set_no, reps)

        self.LOGGER.info(
            "Upper Body 3-set popup verified with scroll: title=%r reps=%s/%s/%s",
            title,
            row1_reps,
            row2_reps,
            row3_reps,
        )

    def dismiss_workout_entry_popup(self):
        self._wait_clickable(
            AppiumBy.ID,
            self.ENTRY_POPUP_GOT_IT_ID,
            "Upper Body popup GOT IT button",
            timeout=8,
        ).click()
        self._wait_until_not_visible(
            AppiumBy.ID, self.ENTRY_POPUP_CARD_ID, "Upper Body post-save popup card", timeout=8
        )
        time.sleep(float(os.getenv("CUBII_UPPER_BODY_AFTER_POPUP_SEC", "0.8")))
        self.LOGGER.info("Upper Body popup dismissed.")

    def verify_new_entry_persisted(self, row1_reps, row2_reps):
        expected = self._require_current_expected(row1_reps, row2_reps)
        self._wait_until_text_not_visible(self.NO_WORKOUT_DATA_TEXT, timeout=5)

        baseline_count = int(getattr(self, "_baseline_entry_count", 0))
        if baseline_count == 0:
            current_count = self._wait_for_entry_count_at_least(1)
        else:
            current_count = self._wait_for_any_entry_card()
        top_blob = self._wait_for_top_entry_to_match(expected, row1_reps, row2_reps)
        expected_total = int(row1_reps) + int(row2_reps)
        assert expected["exercise"].lower() in top_blob.lower(), (
            f"Matched Upper Body activity row does not contain exercise {expected['exercise']!r}. "
            f"Text={top_blob!r}"
        )
        assert self._standalone_integer_in_text(expected_total, top_blob), (
            f"Matched Upper Body activity row does not show total reps {expected_total}. Text={top_blob!r}"
        )
        if expected.get("selected_time"):
            assert self._blob_includes_selected_time(expected["selected_time"], top_blob), (
                f"Matched Upper Body activity row does not show selected time {expected['selected_time']!r}. "
                f"Text={top_blob!r}"
            )

        self.LOGGER.info(
            "Upper Body persisted entry verified: baseline=%s current=%s matched=%r",
            baseline_count,
            current_count,
            top_blob,
        )

    def _assert_add_workout_set_visible(self):
        if self._find_visible_clickable_add_workout_set(timeout=12):
            return
        raise AssertionError("Upper Body ADD WORKOUT SET button is not visible.")

    def _tap_add_workout_set(self):
        el = self._find_visible_clickable_add_workout_set(timeout=15)
        if el is None:
            raise AssertionError("Could not find Upper Body ADD WORKOUT SET button.")
        el.click()
        time.sleep(float(os.getenv("CUBII_UPPER_BODY_AFTER_ADD_TAP_SEC", "0.8")))
        self.LOGGER.info("Upper Body ADD WORKOUT SET tapped.")

    def _find_visible_clickable_add_workout_set(self, timeout=5):
        deadline = time.monotonic() + timeout
        locators = [(AppiumBy.ID, self.ADD_WORKOUT_SET_BUTTON_ID)]
        for text in self.ADD_WORKOUT_SET_TEXTS:
            locators.extend(
                [
                    (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")'),
                    (AppiumBy.XPATH, f'//android.widget.Button[@text="{text}"]'),
                    (AppiumBy.XPATH, f'//*[contains(@text, "{text}")]'),
                ]
            )
        last_error = None
        while time.monotonic() < deadline:
            for by, locator in locators:
                try:
                    remaining = max(0.5, deadline - time.monotonic())
                    el = WebDriverWait(self.driver, min(2, remaining)).until(
                        ec.element_to_be_clickable((by, locator))
                    )
                    if el.is_displayed():
                        return el
                except Exception as exc:
                    last_error = exc
            self._scroll_upper_body_list_towards_add_button()
            time.sleep(0.2)
        self.LOGGER.info("ADD WORKOUT SET not found; last error=%r", last_error)
        return None

    def _scroll_upper_body_list_towards_add_button(self):
        try:
            size = self.driver.get_window_size()
            self.driver.execute_script(
                "mobile: swipeGesture",
                {
                    "left": int(size["width"] * 0.15),
                    "top": int(size["height"] * 0.35),
                    "width": int(size["width"] * 0.7),
                    "height": int(size["height"] * 0.45),
                    "direction": "up",
                    "percent": 0.25,
                },
            )
        except Exception:
            pass

    def _dismiss_optional_ftue_got_it(self):
        if self._click_if_present(
            AppiumBy.ID, self.WORKOUT_FTUE_GOT_IT_ID, "Upper Body editor FTUE GOT IT", timeout=3
        ):
            time.sleep(0.5)

    def _assert_add_workout_screen_visible(self):
        title = self._wait_visible(
            AppiumBy.ID,
            self.ADD_EDIT_WORKOUT_TITLE_ID,
            "Add Workout Sets title",
            timeout=12,
        )
        assert title.is_displayed(), "Add Workout Sets screen title is not visible."

    def _select_start_date_current_and_confirm(self):
        self.LOGGER.info("Upper Body: select Start Date as current date.")
        field = self._find_first_clickable(
            (
                (AppiumBy.ID, self.START_DATE_VALUE_ID, "Start Date value (id)"),
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().resourceId("{self.START_DATE_VALUE_ID}")',
                    "Start Date value (UiAutomator)",
                ),
                (
                    AppiumBy.XPATH,
                    f'//android.widget.TextView[@resource-id="{self.START_DATE_VALUE_ID}"]',
                    "Start Date value (XPath)",
                ),
            ),
            timeout=10,
        )
        field.click()
        self._wait_visible(AppiumBy.XPATH, self.DATE_PICKER_XPATH, "Date picker", timeout=10)
        self._wait_clickable(
            AppiumBy.ID, self.ANDROID_OK_BUTTON_ID, "Date picker OK button", timeout=8
        ).click()
        time.sleep(0.4)

    def _select_random_past_time_and_confirm(self):
        now_local = datetime.now()
        minutes_since_midnight = (now_local.hour * 60) + now_local.minute
        minutes_back = random.randint(1, max(1, minutes_since_midnight))
        target_past = now_local - timedelta(minutes=minutes_back)
        observed_time = ""

        for attempt in range(1, 3):
            self._wait_clickable(AppiumBy.ID, self.TIME_VALUE_ID, "Upper Body Time field").click()
            self._wait_visible(AppiumBy.ID, self.TIME_PICKER_RADIAL_ID, "Time radial picker", timeout=8)

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
            observed_time = self._read_text_if_visible(
                AppiumBy.ID, self.TIME_VALUE_ID, "Upper Body time after save", timeout=5
            )
            if observed_time and self._is_displayed_time_strictly_past(observed_time):
                self.LOGGER.info(
                    "Upper Body time selected: target=%s observed=%s attempt=%s",
                    target_past.strftime("%I:%M %p"),
                    observed_time,
                    attempt,
                )
                return observed_time
            self.LOGGER.warning(
                "Observed time %r was not past after attempt %s; retrying.",
                observed_time,
                attempt,
            )

        raise AssertionError(
            f"Could not select a past Upper Body workout time. Last observed={observed_time!r}."
        )

    def _exercise_strip_bounds(self):
        """Screen-relative rect for the horizontal exercise chip row (tunable per device)."""
        size = self.driver.get_window_size()
        w, h = int(size["width"]), int(size["height"])
        top_frac = float(os.getenv("CUBII_UPPER_BODY_EXERCISE_ROW_TOP_FRAC", "0.38"))
        height_frac = float(os.getenv("CUBII_UPPER_BODY_EXERCISE_ROW_HEIGHT_FRAC", "0.22"))
        left = int(w * 0.08)
        top = int(h * top_frac)
        width = int(w * 0.84)
        height = max(int(h * height_frac), 80)
        return {"left": left, "top": top, "width": width, "height": height}

    def _drag_exercise_strip(self, direction, center_y):
        size = self.driver.get_window_size()
        w = int(size["width"])
        margin = int(w * 0.1)
        y = int(center_y)
        if direction == "left":
            start_x, end_x = w - margin, margin
        else:
            start_x, end_x = margin, w - margin
        try:
            self.driver.execute_script(
                "mobile: dragGesture",
                {
                    "startX": start_x,
                    "startY": y,
                    "endX": end_x,
                    "endY": y,
                    "speed": int(os.getenv("CUBII_UPPER_BODY_EXERCISE_DRAG_SPEED", "2500")),
                },
            )
        except Exception as exc:
            self.LOGGER.debug("dragGesture on exercise strip failed: %s", exc)

    def _nudge_exercise_strip(self, direction="left"):
        """Move the exercise chip row horizontally using several drivers (nested scroll often eats plain swipes)."""
        area = self._exercise_strip_bounds()
        pct = float(os.getenv("CUBII_UPPER_BODY_EXERCISE_SWIPE_PERCENT", "0.65"))
        pause = float(os.getenv("CUBII_UPPER_BODY_EXERCISE_SWIPE_PAUSE_SEC", "0.45"))
        center_y = area["top"] + area["height"] // 2

        for script_name, script, payload in (
            (
                "swipeGesture",
                "mobile: swipeGesture",
                {**area, "direction": direction, "percent": pct},
            ),
            (
                "scrollGesture",
                "mobile: scrollGesture",
                {**area, "direction": direction, "percent": pct},
            ),
        ):
            try:
                self.driver.execute_script(script, payload)
            except Exception as exc:
                self.LOGGER.debug("%s on exercise strip failed: %s", script_name, exc)

        try:
            self.driver.execute_script(
                "mobile: flingGesture",
                {
                    **area,
                    "direction": direction,
                    "speed": int(os.getenv("CUBII_UPPER_BODY_EXERCISE_FLING_SPEED", "2000")),
                },
            )
        except Exception as exc:
            self.LOGGER.debug("flingGesture on exercise strip failed: %s", exc)

        self._drag_exercise_strip(direction, center_y)
        time.sleep(pause)

    def _try_uiautomator_scroll_exercise_into_view(self, exercise):
        """Use UiScrollable.scrollTextIntoView on horizontal scrollables (works when coordinate swipes do not)."""
        escaped = exercise.replace("\\", "\\\\").replace('"', '\\"')
        specs = [
            (
                "HorizontalScrollView",
                f'new UiScrollable(new UiSelector().className("android.widget.HorizontalScrollView").scrollable(true))'
                f'.setAsHorizontalList().scrollTextIntoView("{escaped}")',
            ),
        ]
        for inst in range(5):
            specs.append(
                (
                    f"scrollable.instance({inst})",
                    f'new UiScrollable(new UiSelector().scrollable(true).instance({inst}))'
                    f'.setAsHorizontalList().scrollTextIntoView("{escaped}")',
                )
            )
        for label, uia in specs:
            try:
                WebDriverWait(self.driver, 2).until(
                    lambda d, sel=uia: d.find_element(AppiumBy.ANDROID_UIAUTOMATOR, sel)
                )
                self.LOGGER.info("UiScrollable (%s) brought exercise %r into view.", label, exercise)
                time.sleep(0.35)
                return True
            except Exception:
                self.LOGGER.debug("UiScrollable %s scrollTextIntoView failed for %r.", label, exercise)
        return False

    def _select_random_exercise(self):
        target = random.choice(self.EXERCISE_OPTIONS)
        self.LOGGER.info("Upper Body: select exercise `%s`.", target)
        if self._tap_exercise_if_visible(target, timeout=2):
            return target

        self._try_uiautomator_scroll_exercise_into_view(target)
        if self._tap_exercise_if_visible(target, timeout=2):
            return target

        for direction in ("left", "right", "left", "right", "left", "right"):
            self._nudge_exercise_strip(direction=direction)
            if self._tap_exercise_if_visible(target, timeout=2):
                return target

        for fallback in self.EXERCISE_OPTIONS:
            self._try_uiautomator_scroll_exercise_into_view(fallback)
            if self._tap_exercise_if_visible(fallback, timeout=1):
                self.LOGGER.warning("Selected fallback exercise `%s`; target `%s` unavailable.", fallback, target)
                return fallback
        raise AssertionError("Could not select any Upper Body exercise option.")

    def _tap_exercise_if_visible(self, exercise, timeout=2):
        locators = (
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{exercise}")'),
            (AppiumBy.XPATH, f'//android.widget.TextView[@text="{exercise}"]'),
            (AppiumBy.XPATH, f'//*[contains(@text, "{exercise}")]'),
        )
        for by, locator in locators:
            pair = (by, locator)
            try:
                el = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(pair))
                el.click()
                self.LOGGER.info("Clicked exercise %s.", exercise)
                time.sleep(0.4)
                return True
            except TimeoutException:
                try:
                    el = WebDriverWait(self.driver, min(timeout, 2)).until(
                        ec.visibility_of_element_located(pair)
                    )
                    rect = el.rect
                    cx = int(rect["x"] + rect["width"] / 2)
                    cy = int(rect["y"] + rect["height"] / 2)
                    self.driver.execute_script("mobile: clickGesture", {"x": cx, "y": cy})
                    self.LOGGER.info("Tapped exercise %s via clickGesture at (%s,%s).", exercise, cx, cy)
                    time.sleep(0.4)
                    return True
                except Exception:
                    continue
            except Exception:
                continue
        return False

    def _swipe_exercise_carousel(self, direction="left"):
        self._nudge_exercise_strip(direction=direction)

    def _set_reps_manually(self, row_index, target_value):
        input_el = self._rep_input(row_index)
        input_el.click()
        time.sleep(0.2)
        try:
            input_el.clear()
        except Exception:
            self.LOGGER.debug("Could not clear reps input row %s before Ctrl+A fallback.", row_index + 1)
        try:
            input_el.send_keys(str(int(target_value)))
        finally:
            self._hide_keyboard_quietly()
        observed = self._read_reps_value(row_index)
        assert observed == int(target_value), (
            f"Manual reps entry failed on row {row_index + 1}: "
            f"expected {target_value}, observed {observed}."
        )

    def _set_reps_with_buttons(self, row_index, target_value, prefer_plus=True):
        target = int(target_value)
        current = self._read_reps_value(row_index)
        max_taps = int(os.getenv("CUBII_UPPER_BODY_REPS_MAX_TAPS", "60"))
        if current is None:
            raise AssertionError(f"Could not read initial reps value for row {row_index + 1}.")

        for _ in range(max_taps):
            if current == target:
                return
            if prefer_plus and current < target:
                self._rep_button(row_index, self.REPS_PLUS_ID, "plus").click()
            elif not prefer_plus and current > target:
                self._rep_button(row_index, self.REPS_MINUS_ID, "minus").click()
            elif current < target:
                self._rep_button(row_index, self.REPS_PLUS_ID, "plus fallback").click()
            else:
                self._rep_button(row_index, self.REPS_MINUS_ID, "minus fallback").click()
            time.sleep(0.12)
            current = self._read_reps_value(row_index)

        raise AssertionError(
            f"Could not set row {row_index + 1} reps to {target} with plus/minus buttons."
        )

    def _rep_input(self, row_index):
        return self._visible_instance_by_id(self.REPS_INPUT_ID, row_index, "reps input")

    def _rep_button(self, row_index, resource_id, label):
        return self._visible_instance_by_id(resource_id, row_index, f"reps {label} button")

    def _read_reps_value(self, row_index):
        el = self._rep_input(row_index)
        raw = (
            el.text
            or el.get_attribute("text")
            or el.get_attribute("value")
            or el.get_attribute("content-desc")
            or ""
        ).strip()
        match = re.search(r"\d+", raw)
        return int(match.group(0)) if match else None

    def _tap_save_workout(self):
        self._wait_clickable(
            AppiumBy.ID, self.SAVE_WORKOUT_BUTTON_ID, "Upper Body Save button", timeout=10
        ).click()

    def _scroll_add_workout_editor_for_add_sets_button(self):
        """Scroll the add-workout form so + ADD SETS (`llAddSets`) is reachable."""
        try:
            el = self.driver.find_element(AppiumBy.ID, self.EXERCISE_SETS_RECYCLER_ID)
            rect = el.rect
            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                    "left": max(0, int(rect["x"])),
                    "top": max(0, int(rect["y"])),
                    "width": max(1, int(rect["width"])),
                    "height": max(1, int(rect["height"])),
                    "direction": "down",
                    "percent": float(os.getenv("CUBII_UPPER_BODY_EDITOR_SCROLL_PERCENT", "0.5")),
                },
            )
        except Exception as exc:
            self.LOGGER.debug("Editor scrollGesture on rvExerciseSets skipped: %s", exc)
            try:
                size = self.driver.get_window_size()
                w, h = int(size["width"]), int(size["height"])
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "left": int(w * 0.1),
                        "top": int(h * 0.42),
                        "width": int(w * 0.8),
                        "height": int(h * 0.38),
                        "direction": "down",
                        "percent": 0.45,
                    },
                )
            except Exception as exc2:
                self.LOGGER.debug("Fallback editor scroll skipped: %s", exc2)
        time.sleep(0.35)

    def _tap_ll_add_sets(self):
        locators = (
            (AppiumBy.ID, self.LL_ADD_SETS_ID),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("{self.LL_ADD_SETS_ID}")',
            ),
            (
                AppiumBy.XPATH,
                f'//android.widget.LinearLayout[@resource-id="{self.LL_ADD_SETS_ID}"]',
            ),
        )
        for by, loc in locators:
            try:
                self._wait_clickable(by, loc, "+ ADD SETS (llAddSets)", timeout=6).click()
                self.LOGGER.info("Tapped + ADD SETS (%s).", self.LL_ADD_SETS_ID)
                time.sleep(float(os.getenv("CUBII_UPPER_BODY_AFTER_ADD_SETS_ROW_SEC", "0.65")))
                return
            except Exception:
                continue
        raise AssertionError("Could not tap + ADD SETS (com.cubii:id/llAddSets).")

    def _scroll_popup_reps_recycler_reset_top(self):
        """Scroll reps list toward top so set 1 header + columns align (uses swipe; scrollGesture often no-ops)."""
        rid = self.ENTRY_POPUP_REPS_RECYCLER_ID
        rounds = int(os.getenv("CUBII_UPPER_BODY_POPUP_RECYCLER_TOP_SWIPES", "6"))
        pct = float(os.getenv("CUBII_UPPER_BODY_POPUP_SCROLL_TOP_PERCENT", "0.55"))
        for _ in range(max(3, rounds)):
            self._scroll_popup_recycler_try_scroll(rid, direction="down", percent=pct)
            time.sleep(0.18)
        time.sleep(0.35)

    def _popup_first_descendant_cell(self, node, resource_id):
        """Any descendant with `resource_id`: prefer displayed, else first with text (clipped modals)."""
        best = None
        try:
            for el in node.find_elements(AppiumBy.ID, resource_id):
                if el.is_displayed():
                    return el
                t = (el.text or el.get_attribute("text") or "").strip()
                if t and best is None:
                    best = el
        except Exception:
            pass
        return best

    def _popup_reps_row_label_and_reps_ready(self, driver, sn: str) -> bool:
        """True when txtSet `sn` is shown and the row has txtReps (visible or readable text)."""
        rid = self.ENTRY_POPUP_REPS_RECYCLER_ID
        sid = self.ENTRY_POPUP_SET_ID
        reps_id = self.ENTRY_POPUP_REPS_ID
        label_xpath = (
            f'//androidx.recyclerview.widget.RecyclerView[@resource-id="{rid}"]'
            f'//*[@resource-id="{sid}" and normalize-space(@text)="{sn}"]'
        )
        try:
            set_el = driver.find_element(AppiumBy.XPATH, label_xpath)
            if not set_el.is_displayed():
                return False
        except Exception:
            return False
        node = set_el
        for _ in range(16):
            if self._popup_first_descendant_cell(node, reps_id) is not None:
                return True
            try:
                node = node.find_element(AppiumBy.XPATH, "./..")
            except Exception:
                break
        return False

    def _scroll_popup_recycler_gesture(self, rid, *, direction: str, percent: float) -> bool:
        """Drive the popup reps list; swipeGesture usually works when scrollGesture does not. Returns success."""
        try:
            rcy = self.driver.find_element(AppiumBy.ID, rid)
            rect = rcy.rect
        except Exception as exc:
            self.LOGGER.warning("popup list: RecyclerView %s not found: %s", rid, exc)
            return False
        box = {
            "left": max(0, int(rect["x"])),
            "top": max(0, int(rect["y"])),
            "width": max(1, int(rect["width"])),
            "height": max(1, int(rect["height"])),
        }
        if box["height"] < 24 or box["width"] < 24:
            self.LOGGER.debug("popup list: RecyclerView bounds too small %s; use card swipe.", box)
            return False
        engine = (os.getenv("CUBII_UPPER_BODY_POPUP_SCROLL_ENGINE") or "swipe_first").strip().lower()
        if engine in ("scroll", "scroll_only"):
            seq = ("mobile: scrollGesture",)
        elif engine in ("swipe", "swipe_only"):
            seq = ("mobile: swipeGesture",)
        else:
            seq = ("mobile: swipeGesture", "mobile: scrollGesture")
        last_exc = None
        for name in seq:
            try:
                self.driver.execute_script(
                    name,
                    {**box, "direction": direction, "percent": percent},
                )
                return True
            except Exception as exc:
                last_exc = exc
        self.LOGGER.warning(
            "popup list gesture failed rid=%s dir=%s box=%s last=%s", rid, direction, box, last_exc
        )
        return False

    def _scroll_popup_card_swipe(self, *, direction: str, percent: float) -> bool:
        """Swipe inside the post-save popup card when RecyclerView-targeted gestures do nothing."""
        try:
            card = self.driver.find_element(AppiumBy.ID, self.ENTRY_POPUP_CARD_ID)
            r = card.rect
        except Exception as exc:
            self.LOGGER.debug("popup card swipe: no card: %s", exc)
            return False
        w, h = max(1, int(r["width"])), max(1, int(r["height"]))
        box = {
            "left": max(0, int(r["x"]) + int(w * 0.12)),
            "top": max(0, int(r["y"]) + int(h * 0.28)),
            "width": max(1, int(w * 0.76)),
            "height": max(1, int(h * 0.42)),
        }
        for name in ("mobile: swipeGesture", "mobile: scrollGesture"):
            try:
                self.driver.execute_script(
                    name,
                    {**box, "direction": direction, "percent": percent},
                )
                return True
            except Exception:
                continue
        return False

    def _scroll_popup_recycler_try_scroll(self, rid, *, direction: str, percent: float) -> bool:
        """Scroll reps list; fall back to swiping the dialog card if RV gestures fail or bounds are unusable."""
        if self._scroll_popup_recycler_gesture(rid, direction=direction, percent=percent):
            return True
        if self._scroll_popup_card_swipe(direction=direction, percent=percent):
            self.LOGGER.info(
                "Popup reps scroll used card fallback (RecyclerView swipe missed or tiny bounds) dir=%s",
                direction,
            )
            return True
        return False

    def _scroll_popup_set_row_into_view(self, set_number):
        """Scroll `rcyUpwEntryReps` until the row shows both txtSet and visible txtReps for that set."""
        sn = str(int(set_number))
        nset = int(set_number)
        rid = self.ENTRY_POPUP_REPS_RECYCLER_ID
        sid = self.ENTRY_POPUP_SET_ID
        down_pct = float(os.getenv("CUBII_UPPER_BODY_POPUP_ROW_SCROLL_DOWN_PERCENT", "0.48"))
        dead_sec = float(os.getenv("CUBII_UPPER_BODY_POPUP_ROW_SCROLL_DEADLINE_SEC", "20"))

        def _ready(drv):
            return self._popup_reps_row_label_and_reps_ready(drv, sn)

        uia = (
            f'new UiScrollable(new UiSelector().resourceId("{rid}"))'
            f'.scrollIntoView(new UiSelector().resourceId("{sid}").text("{sn}"))'
        )
        for _ in range(3 if nset >= 3 else 1):
            try:
                WebDriverWait(self.driver, 5).until(
                    lambda d, sel=uia: d.find_element(AppiumBy.ANDROID_UIAUTOMATOR, sel)
                )
                time.sleep(0.3)
            except Exception as exc:
                self.LOGGER.debug("UiScrollable scrollIntoView for popup set %s: %s", sn, exc)
            if _ready(self.driver):
                time.sleep(0.2)
                return

        # Set 3+ sits lower in the list — swipe `up` in the RV reveals bottom rows (matches In Progress).
        if nset >= 3:
            lead = int(os.getenv("CUBII_UPPER_BODY_POPUP_LEAD_DOWN_SWIPES_FOR_SET3", "5"))
            for _ in range(max(3, lead)):
                if _ready(self.driver):
                    time.sleep(0.2)
                    return
                self._scroll_popup_recycler_try_scroll(rid, direction="up", percent=down_pct)
                time.sleep(0.2)

        if _ready(self.driver):
            time.sleep(0.2)
            return

        # Sets 1–2: nudge toward top (swipe `down` in RV) so header + first reps column align.
        if nset <= 2:
            for _ in range(5):
                if _ready(self.driver):
                    time.sleep(0.2)
                    return
                self._scroll_popup_recycler_try_scroll(rid, direction="down", percent=0.55)
                time.sleep(0.18)

        deadline = time.monotonic() + dead_sec
        # One direction only — alternating up/down undoes progress (e.g. reveals set 3 then hides it).
        primary = "up" if nset >= 3 else "down"
        while time.monotonic() < deadline:
            if _ready(self.driver):
                time.sleep(0.2)
                return
            self._scroll_popup_recycler_try_scroll(rid, direction=primary, percent=down_pct)
            time.sleep(0.22)

        # Last-chance pulses for lower rows (still single direction).
        if nset >= 3:
            extra = int(os.getenv("CUBII_UPPER_BODY_POPUP_SET3_FINAL_UP_PULSES", "14"))
            for _ in range(max(0, extra)):
                if _ready(self.driver):
                    time.sleep(0.15)
                    return
                self._scroll_popup_recycler_try_scroll(rid, direction="up", percent=down_pct)
                time.sleep(0.18)

    def _popup_row_field_text(self, row, resource_id):
        el = self._popup_first_descendant_cell(row, resource_id)
        if el is None:
            raise AssertionError(f"No `{resource_id}` under popup row (displayed or with text).")
        return (el.text or el.get_attribute("text") or "").strip()

    def _popup_reps_row_root_for_set_label(self, expected_set):
        """Row under `rcyUpwEntryReps` for a data set; avoids header row where txtSet shows e.g. 'Sets'."""
        label = str(int(expected_set))
        rid = self.ENTRY_POPUP_REPS_RECYCLER_ID
        sid = self.ENTRY_POPUP_SET_ID
        reps_id = self.ENTRY_POPUP_REPS_ID
        set_xpath = (
            f'//androidx.recyclerview.widget.RecyclerView[@resource-id="{rid}"]'
            f'//*[@resource-id="{sid}" and normalize-space(@text)="{label}"]'
        )
        self._scroll_popup_set_row_into_view(expected_set)
        # Closest ancestor of the set label that also contains txtReps (handles non-uniform row depth).
        row_xpath = (
            f'//androidx.recyclerview.widget.RecyclerView[@resource-id="{rid}"]'
            f'//*[@resource-id="{sid}" and normalize-space(@text)="{label}"]'
            f'/ancestor::*[.//*[@resource-id="{reps_id}"]][1]'
        )
        try:
            row = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((AppiumBy.XPATH, row_xpath))
            )
            if self._popup_first_descendant_cell(row, reps_id) is not None:
                return row
        except Exception as exc:
            self.LOGGER.debug("popup row xpath for set %s: %s", label, exc)

        try:
            set_el = WebDriverWait(self.driver, 8).until(
                ec.presence_of_element_located((AppiumBy.XPATH, set_xpath))
            )
        except Exception as exc:
            raise AssertionError(
                f"Popup set label {label} not found under {rid} after scroll. {exc}"
            ) from exc
        node = set_el
        for _ in range(16):
            if self._popup_first_descendant_cell(node, reps_id) is not None:
                return node
            try:
                node = node.find_element(AppiumBy.XPATH, "./..")
            except Exception:
                break
        raise AssertionError(
            f"Popup row container for set {expected_set}: no {reps_id} under ancestors."
        )

    def _assert_popup_reps_row(self, _set_no, expected_set, expected_reps):
        # Locate by txtSet numeric label — RecyclerView child [1] is often a header ("Sets"), not set 1.
        row = self._popup_reps_row_root_for_set_label(expected_set)
        set_text = self._popup_row_field_text(row, self.ENTRY_POPUP_SET_ID)
        reps_text = self._popup_row_field_text(row, self.ENTRY_POPUP_REPS_ID)
        assert str(expected_set) == set_text, (
            f"Popup row set mismatch: expected {expected_set}, observed {set_text!r}."
        )
        assert str(expected_reps) == reps_text, (
            f"Popup row reps mismatch for set {expected_set}: expected {expected_reps}, "
            f"observed {reps_text!r}."
        )

    def _first_child_text(self, parent, resource_id):
        for el in parent.find_elements(AppiumBy.ID, resource_id):
            if el.is_displayed():
                return (el.text or el.get_attribute("text") or "").strip()
        raise AssertionError(f"Child `{resource_id}` not visible under popup row.")

    def _wait_for_entry_count_at_least(self, expected_min):
        deadline = time.monotonic() + max(10, Settings.EXPLICIT_WAIT)
        last_count = 0
        while time.monotonic() < deadline:
            last_count = self._count_visible_entry_cards()
            if last_count >= expected_min:
                return last_count
            time.sleep(0.5)
        raise AssertionError(
            f"Expected at least {expected_min} Upper Body entries after save; observed {last_count}."
        )

    def _wait_for_any_entry_card(self):
        deadline = time.monotonic() + max(8, Settings.EXPLICIT_WAIT)
        last_count = 0
        while time.monotonic() < deadline:
            last_count = self._count_visible_entry_cards()
            if last_count >= 1:
                return last_count
            time.sleep(0.5)
        raise AssertionError("Expected at least one Upper Body entry after save; none visible.")

    def _activity_card_blob(self, row):
        """Text for one activity log card, always merging `txtWorkoutDayTime` when present under the row."""
        time_parts = []
        try:
            for tel in row.find_elements(AppiumBy.ID, self.ENTRY_CARD_TIME_ID):
                if not tel.is_displayed():
                    continue
                t = (tel.text or tel.get_attribute("text") or tel.get_attribute("content-desc") or "").strip()
                if t:
                    time_parts.append(t)
        except Exception:
            pass
        body = (self._collect_descendant_text(row) or "").strip()
        return " ".join(time_parts + ([body] if body else [])).strip()

    def _blob_includes_selected_time(self, selected_time, blob):
        if not selected_time:
            return True
        if not blob:
            return False
        compact_time = selected_time.replace(" ", "").lower()
        compact_blob = blob.replace(" ", "").lower()
        if compact_time in compact_blob:
            return True
        alt = re.sub(r"^0(\d:\d{2})", r"\1", compact_time)
        if alt != compact_time and alt in compact_blob:
            return True
        return self._time_texts_are_close(selected_time, blob)

    def _visible_activity_entry_blobs(self):
        """Text blobs for each visible activity log card (order is not guaranteed to be newest-first)."""
        blobs = []
        try:
            rows = [
                row
                for row in self.driver.find_elements(AppiumBy.ID, self.ENTRY_CARD_ROOT_ID)
                if row.is_displayed()
            ]
        except Exception:
            return blobs
        for row in rows:
            blob = self._activity_card_blob(row)
            if blob:
                blobs.append(blob)
        return blobs

    def _first_activity_entry_blob_matching_submitted(self, expected, row1_reps, row2_reps):
        """Find a visible activity row that matches the exercise and total reps we just saved."""
        expected_total = int(row1_reps) + int(row2_reps)
        ex = (expected.get("exercise") or "").lower()
        if not ex:
            return ""
        for blob in self._visible_activity_entry_blobs():
            if ex in blob.lower() and self._standalone_integer_in_text(expected_total, blob):
                return blob
        return ""

    def _wait_for_top_entry_to_match(self, expected, row1_reps, row2_reps):
        deadline = time.monotonic() + max(10, Settings.EXPLICIT_WAIT)
        expected_total = int(row1_reps) + int(row2_reps)
        last_fallback = ""
        while time.monotonic() < deadline:
            match = self._first_activity_entry_blob_matching_submitted(expected, row1_reps, row2_reps)
            if match:
                return match
            last_fallback = self._top_entry_card_text()
            time.sleep(0.5)
        visible = self._visible_activity_entry_blobs()
        raise AssertionError(
            f"No visible Upper Body activity row matched the submitted workout. "
            f"Expected exercise={expected['exercise']!r} total_reps={expected_total}; "
            f"legacy_top_blob={last_fallback!r}; visible_activity_rows={visible!r}."
        )

    def _count_visible_entry_cards(self):
        try:
            rows = self.driver.find_elements(AppiumBy.ID, self.ENTRY_CARD_ROOT_ID)
            visible = [row for row in rows if row.is_displayed()]
            if visible:
                return len(visible)
        except Exception:
            pass
        count = 0
        for exercise in self.EXERCISE_OPTIONS:
            try:
                count += sum(
                    1
                    for el in self.driver.find_elements(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiSelector().text("{exercise}")',
                    )
                    if el.is_displayed()
                )
            except Exception:
                continue
        return count

    def _top_entry_card_text(self):
        rows = []
        try:
            rows = [row for row in self.driver.find_elements(AppiumBy.ID, self.ENTRY_CARD_ROOT_ID) if row.is_displayed()]
        except Exception:
            rows = []
        if rows:
            rows.sort(key=lambda row: row.rect.get("y", 0))
            blob = self._activity_card_blob(rows[0])
            if blob:
                return blob

        parts = []
        for rid in (self.ENTRY_CARD_TIME_ID,):
            text = self._read_text_if_visible(AppiumBy.ID, rid, timeout=1)
            if text:
                parts.append(text)
        for exercise in self.EXERCISE_OPTIONS:
            if self._is_text_visible(exercise, timeout=1):
                parts.append(exercise)
                break
        page_text = " ".join(parts + [self._collect_visible_page_text()]).strip()
        return page_text

    def _collect_descendant_text(self, root):
        parts = []
        text = (root.text or "").strip()
        if text:
            parts.append(text)
        try:
            for child in root.find_elements(AppiumBy.XPATH, ".//*"):
                child_text = (child.text or child.get_attribute("text") or "").strip()
                if child_text:
                    parts.append(child_text)
        except Exception:
            pass
        return " ".join(parts)

    def _collect_visible_page_text(self):
        parts = []
        try:
            for el in self.driver.find_elements(AppiumBy.XPATH, "//*[@text]"):
                if el.is_displayed():
                    text = (el.text or el.get_attribute("text") or "").strip()
                    if text:
                        parts.append(text)
        except Exception:
            pass
        return " ".join(parts)

    def _visible_instance_by_id(self, resource_id, zero_based_index, label):
        deadline = time.monotonic() + Settings.EXPLICIT_WAIT
        last_count = 0
        while time.monotonic() < deadline:
            els = self.driver.find_elements(AppiumBy.ID, resource_id)
            visible = [el for el in els if el.is_displayed()]
            last_count = len(visible)
            if zero_based_index < len(visible):
                return visible[zero_based_index]
            time.sleep(0.25)
        raise AssertionError(
            f"Could not find {label} instance {zero_based_index}; visible count={last_count}."
        )

    def _find_first_clickable(self, locator_specs, timeout=8):
        deadline = time.monotonic() + timeout
        last_error = None
        while time.monotonic() < deadline:
            for by, locator, label in locator_specs:
                try:
                    remaining = max(0.5, deadline - time.monotonic())
                    el = WebDriverWait(self.driver, min(2, remaining)).until(
                        ec.element_to_be_clickable((by, locator))
                    )
                    self.LOGGER.info("Found clickable %s via %s.", label, by)
                    return el
                except Exception as exc:
                    last_error = exc
        raise AssertionError(f"No clickable locator found. Last error: {last_error!r}")

    def _tap_by_id_or_uiautomator(self, resource_id, label):
        locators = (
            (AppiumBy.ID, resource_id),
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("{resource_id}")'),
        )
        last_error = None
        for by, locator in locators:
            try:
                el = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT).until(
                    ec.element_to_be_clickable((by, locator))
                )
                el.click()
                self.LOGGER.info("Tapped %s via %s.", label, by)
                return
            except Exception as exc:
                last_error = exc
        raise AssertionError(f"Could not tap {label} ({resource_id}). Last error: {last_error!r}")

    def _wait_visible(self, by, value, label, timeout=None):
        wait_sec = timeout or Settings.EXPLICIT_WAIT
        try:
            el = WebDriverWait(self.driver, wait_sec).until(
                ec.visibility_of_element_located((by, value))
            )
            self.LOGGER.info("Element visible: %s.", label)
            return el
        except TimeoutException:
            self.LOGGER.exception("Timed out waiting visible: %s (%s, %s)", label, by, value)
            raise

    def _wait_clickable(self, by, value, label, timeout=None):
        wait_sec = timeout or Settings.EXPLICIT_WAIT
        try:
            el = WebDriverWait(self.driver, wait_sec).until(
                ec.element_to_be_clickable((by, value))
            )
            self.LOGGER.info("Element clickable: %s.", label)
            return el
        except TimeoutException:
            self.LOGGER.exception("Timed out waiting clickable: %s (%s, %s)", label, by, value)
            raise

    def _wait_until_not_visible(self, by, value, label, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.invisibility_of_element_located((by, value))
            )
        except TimeoutException:
            self.LOGGER.warning("%s still visible after %ss.", label, timeout)

    def _click_if_present(self, by, value, label, timeout=2):
        try:
            el = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((by, value)))
            el.click()
            self.LOGGER.info("Clicked optional %s.", label)
            return True
        except Exception:
            return False

    def _is_text_visible(self, text, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')
                )
            )
            return True
        except Exception:
            return False

    def _wait_until_text_not_visible(self, text, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until_not(
                ec.visibility_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')
                )
            )
        except Exception:
            if self._is_text_visible(text, timeout=1):
                raise AssertionError(f"Unexpected text still visible: {text!r}")

    def _read_text_if_visible(self, by, value, label=None, timeout=2):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located((by, value))
            )
            return (el.text or el.get_attribute("text") or el.get_attribute("content-desc") or "").strip()
        except Exception:
            if label:
                self.LOGGER.debug("Could not read optional text for %s.", label)
            return ""

    def _try_set_picker_text(self, resource_id, value):
        try:
            picker_input = WebDriverWait(self.driver, 2).until(
                ec.presence_of_element_located((AppiumBy.ID, resource_id))
            )
            picker_input.click()
            try:
                picker_input.clear()
            except Exception:
                pass
            picker_input.send_keys(value)
            observed = (
                picker_input.text
                or picker_input.get_attribute("text")
                or picker_input.get_attribute("content-desc")
                or ""
            ).strip()
            return "".join(ch for ch in observed if ch.isdigit()).endswith(
                "".join(ch for ch in str(value) if ch.isdigit())
            )
        except Exception:
            return False

    def _set_time_using_radial_picker(self, target_dt):
        radial = self._wait_visible(AppiumBy.ID, self.TIME_PICKER_RADIAL_ID, "Time radial picker", timeout=4)
        hour_12 = int(target_dt.strftime("%I"))
        minute_rounded = int(round(int(target_dt.strftime("%M")) / 5.0) * 5) % 60
        self._tap_if_present_quiet(AppiumBy.ID, self.TIME_PICKER_HOURS_CHIP_ID)
        self._tap_radial_clock_value(radial, hour_12, is_minute=False)
        self._tap_if_present_quiet(AppiumBy.ID, self.TIME_PICKER_MINUTES_CHIP_ID)
        self._tap_radial_clock_value(radial, minute_rounded, is_minute=True)

    def _tap_radial_clock_value(self, radial_element, value, is_minute=False):
        rect = radial_element.rect
        center_x = rect["x"] + (rect["width"] / 2.0)
        center_y = rect["y"] + (rect["height"] / 2.0)
        radius = min(rect["width"], rect["height"]) * (0.34 if is_minute else 0.36)
        if is_minute:
            angle = (int(value) / 60.0) * 2.0 * math.pi - (math.pi / 2.0)
        else:
            hour = int(value) % 12
            angle = (hour / 12.0) * 2.0 * math.pi - (math.pi / 2.0)
        x = int(center_x + radius * math.cos(angle))
        y = int(center_y + radius * math.sin(angle))
        try:
            self.driver.execute_script("mobile: clickGesture", {"x": x, "y": y})
            return True
        except Exception:
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
        target_id = self.TIME_PICKER_AM_LABEL_ID if label == "AM" else self.TIME_PICKER_PM_LABEL_ID
        return self._click_if_present(AppiumBy.ID, target_id, f"time picker {label}", timeout=2)

    def _is_displayed_time_strictly_past(self, observed_time_text):
        parsed = self._parse_time_from_text(observed_time_text)
        if parsed is None:
            return False
        now_local = datetime.now()
        candidate = now_local.replace(hour=parsed.hour, minute=parsed.minute, second=0, microsecond=0)
        return candidate < now_local.replace(second=0, microsecond=0)

    def _parse_time_from_text(self, text_value):
        match = re.search(r"(\d{1,2}):(\d{2})\s*([AP]M)", text_value or "", re.I)
        if not match:
            return None
        hour = int(match.group(1))
        minute = int(match.group(2))
        meridiem = match.group(3).upper()
        if meridiem == "PM" and hour != 12:
            hour += 12
        if meridiem == "AM" and hour == 12:
            hour = 0
        return datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)

    def _time_texts_are_close(self, selected_time, card_text):
        selected = self._parse_time_from_text(selected_time)
        if selected is None:
            return False
        candidates = re.findall(r"\d{1,2}:\d{2}\s*[AP]M", card_text or "", re.I)
        for candidate_text in candidates:
            candidate = self._parse_time_from_text(candidate_text)
            if candidate and abs((candidate - selected).total_seconds()) <= 5 * 60:
                return True
        return False

    def _hide_keyboard_quietly(self):
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass

    def _require_current_expected(self, row1_reps, row2_reps):
        expected = getattr(self, "_current_expected", None)
        if not expected:
            raise AssertionError("No Upper Body workout submission details were recorded.")
        assert expected["row1_reps"] == int(row1_reps), "Stored row 1 reps do not match step input."
        assert expected["row2_reps"] == int(row2_reps), "Stored row 2 reps do not match step input."
        return expected

    def _require_current_expected_three(self, row1_reps, row2_reps, row3_reps):
        expected = getattr(self, "_current_expected", None)
        if not expected:
            raise AssertionError("No Upper Body workout submission details were recorded.")
        assert expected["row1_reps"] == int(row1_reps), "Stored row 1 reps do not match step input."
        assert expected["row2_reps"] == int(row2_reps), "Stored row 2 reps do not match step input."
        assert int(expected.get("row3_reps", -1)) == int(row3_reps), (
            "Stored row 3 reps do not match step input "
            f"(expected {row3_reps}, got {expected.get('row3_reps')})."
        )
        return expected
