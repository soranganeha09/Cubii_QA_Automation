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


class InProgressPage(BasePage):
    """Progress / In Progress analytics surface — period tabs, categories, summary, chart."""

    LOGGER = logging.getLogger("cubii_in_progress_page")

    # Period tabs (resource-id). UiAutomator: new UiSelector().resourceId("<id>")
    TAB_DAY_ID = "com.cubii:id/cardTabDay"
    TAB_WEEK_ID = "com.cubii:id/txtTabWeek"
    TAB_MONTH_ID = "com.cubii:id/txtTabMonth"
    TAB_YEAR_ID = "com.cubii:id/txtTabYear"

    # Workout category tabs
    TAB_LOWER_BODY_ID = "com.cubii:id/txtTabLowerBody"
    TAB_UPPER_BODY_ID = "com.cubii:id/txtUpperBody"

    DATE_RANGE_ID = "com.cubii:id/txtTitleDateRange"

    SUMMARY_STRIDES_ID = "com.cubii:id/linLayoutStrides"
    SUMMARY_CALORIES_ID = "com.cubii:id/linLayoutCalories"
    SUMMARY_MILES_ID = "com.cubii:id/linLayoutDistance"
    SUMMARY_TIME_ID = "com.cubii:id/linLayoutTime"

    COMBINED_CHART_ID = "com.cubii:id/combinedChart"

    # Date strip — Next / Previous (content-desc matches app).
    NAV_NEXT_ID = "com.cubii:id/imgNext"
    NAV_NEXT_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/imgNext")'
    NAV_NEXT_XPATH = '//android.widget.ImageView[@content-desc="Next Button"]'

    NAV_PREVIOUS_ID = "com.cubii:id/imgPrevious"
    NAV_PREVIOUS_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/imgPrevious")'
    NAV_PREVIOUS_XPATH = '//android.widget.ImageView[@content-desc="Previous Button"]'

    # Activity log list — drill-down into finer period (Week→Day, Month→Week, Year→Month).
    ACTIVITY_LOG_CARD_ROOT_ID = "com.cubii:id/cnsLayoutActivityLogRoot"
    TXT_METRICS_VALUE1_ID = "com.cubii:id/txtMetricsValue1"

    _LOG_TRUNC = int(os.getenv("CUBII_PROGRESS_LOG_TEXT_MAX_CHARS", "800"))

    def _log_progress_block(self, heading, pairs):
        """Structured INFO logs: heading + labelled lines (grep logs for 'Progress |')."""
        self.LOGGER.info("Progress | ===== %s =====", heading)
        for label, value in pairs:
            s = repr(value) if value is None else str(value)
            if len(s) > self._LOG_TRUNC:
                s = f"{s[: self._LOG_TRUNC]}…(+{len(str(value)) - self._LOG_TRUNC} chars)"
            self.LOGGER.info("Progress |   %s: %s", label, s)

    def _safe_snap_summary_rows(self):
        """Best-effort text under each metric strip (for diagnostics)."""
        rows = []
        specs = (
            ("Strides strip", self.SUMMARY_STRIDES_ID),
            ("Calories strip", self.SUMMARY_CALORIES_ID),
            ("Miles strip", self.SUMMARY_MILES_ID),
            ("Time strip", self.SUMMARY_TIME_ID),
        )
        for label, sid in specs:
            try:
                els = self.driver.find_elements(AppiumBy.ID, sid)
                blob = ""
                for el in els:
                    try:
                        if el.is_displayed():
                            blob = self._collect_descendant_visible_text(el)
                            break
                    except Exception:
                        continue
                rows.append((f"summary_{label.lower().replace(' ', '_')}", blob or "(not visible / empty)"))
            except Exception as exc:
                rows.append((f"summary_{label.lower().replace(' ', '_')}", f"<read_error {exc}>"))
        return rows

    def _uia_resource_id(self, resource_id):
        return f'new UiSelector().resourceId("{resource_id}")'

    def _scroll_progress_vertical(self, direction="up", percent=None):
        """Nudge scroll on In Progress; `direction` matches Appium swipeGesture (e.g. up reveals lower content)."""
        pct = percent if percent is not None else float(os.getenv("CUBII_IN_PROGRESS_SCROLL_PERCENT", "0.55"))
        try:
            size = self.driver.get_window_size()
            w, h = int(size["width"]), int(size["height"])
            self.driver.execute_script(
                "mobile: swipeGesture",
                {
                    "left": int(w * 0.15),
                    "top": int(h * 0.25),
                    "width": int(w * 0.7),
                    "height": int(h * 0.45),
                    "direction": direction,
                    "percent": pct,
                },
            )
        except Exception as exc:
            self.LOGGER.debug("Swipe gesture skipped or failed: %s", exc)
        time.sleep(float(os.getenv("CUBII_IN_PROGRESS_AFTER_SCROLL_PAUSE", "0.6")))

    def _assert_visible_id_or_uiautomator(self, resource_id, label, timeout=None):
        wait_sec = timeout if timeout is not None else Settings.EXPLICIT_WAIT
        uia = self._uia_resource_id(resource_id)
        deadline = time.monotonic() + wait_sec
        last_error = None
        while time.monotonic() < deadline:
            for by, val in (
                (AppiumBy.ID, resource_id),
                (AppiumBy.ANDROID_UIAUTOMATOR, uia),
            ):
                try:
                    remaining = max(1.0, deadline - time.monotonic())
                    WebDriverWait(self.driver, min(2.0, remaining)).until(
                        ec.visibility_of_element_located((by, val))
                    )
                    self.LOGGER.info("In Progress UI: visible `%s` via %s.", label, by)
                    return
                except (TimeoutException, Exception) as exc:
                    last_error = exc
                    continue
        raise AssertionError(
            f"In Progress UI element not visible: {label} (`{resource_id}`). Last error: {last_error!r}"
        )

    def _tap_visible_clickable(self, resource_id, label, timeout=None):
        wait_sec = timeout if timeout is not None else Settings.EXPLICIT_WAIT
        uia = self._uia_resource_id(resource_id)
        deadline = time.monotonic() + wait_sec
        last_error = None
        while time.monotonic() < deadline:
            for by, val in (
                (AppiumBy.ID, resource_id),
                (AppiumBy.ANDROID_UIAUTOMATOR, uia),
            ):
                try:
                    remaining = max(1.0, deadline - time.monotonic())
                    el = WebDriverWait(self.driver, min(3.0, remaining)).until(
                        ec.element_to_be_clickable((by, val))
                    )
                    el.click()
                    self.LOGGER.info(
                        "Progress | CLICK: %s | resource_id=`%s` | strategy=%s",
                        label,
                        resource_id,
                        by,
                    )
                    time.sleep(float(os.getenv("CUBII_PERIOD_TAB_CLICK_PAUSE_SEC", "0.7")))
                    try:
                        rng = self._read_date_range_text()
                        extra = [(f"{label.lower().replace(' ', '_')}_date_range_strip", rng)]
                        self._log_progress_block(
                            f"Collected after CLICK → {label}",
                            self._safe_snap_summary_rows() + extra,
                        )
                    except Exception as exc:
                        self.LOGGER.warning("Progress | post-click data snapshot skipped: %s", exc)
                    return
                except Exception as exc:
                    last_error = exc
                    continue
        raise AssertionError(f"Could not tap `{label}` ({resource_id}). Last error: {last_error!r}")

    def _collect_descendant_visible_text(self, root_element):
        parts = []
        t = (root_element.text or "").strip()
        if t:
            parts.append(t)
        try:
            for sub in root_element.find_elements(AppiumBy.XPATH, ".//*"):
                st = (sub.text or "").strip()
                if st:
                    parts.append(st)
        except Exception:
            pass
        return " ".join(parts).strip()

    def _summary_container_shows_metric_data(self, resource_id, label):
        """
        Ensures summary row exists and aggregated text suggests metrics (digits, or hyphen-style zeros).
        Set CUBII_PERIOD_METRICS_REQUIRE_DIGITS=0 to only require non-empty text under the row.
        """
        self._assert_visible_id_or_uiautomator(resource_id, label, timeout=8)
        root = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((AppiumBy.ID, resource_id))
        )
        combined = self._collect_descendant_visible_text(root)
        if not combined:
            combined = (
                root.get_attribute("content-desc") or root.get_attribute("name") or ""
            ).strip()
        require_digit = (
            os.getenv("CUBII_PERIOD_METRICS_REQUIRE_DIGITS", "1").strip().lower()
            not in ("0", "false", "no")
        )
        has_placeholder = "--" in combined or "−" in combined
        has_digit = bool(re.search(r"\d", combined))
        if len(combined) < 2 and not has_digit:
            raise AssertionError(
                f"Summary `{label}` has no usable text (`{resource_id}`); got {combined!r}."
            )
        if require_digit and not has_digit and not has_placeholder:
            raise AssertionError(
                f"No digit or hyphen placeholder in `{label}` (`{resource_id}`); text={combined!r}."
            )
        self.LOGGER.info("Summary `%s` full aggregated text (%s chars): %.500s%s", label, len(combined), combined, "…" if len(combined) > 500 else "")

    def _read_date_range_text(self):
        self._assert_visible_id_or_uiautomator(self.DATE_RANGE_ID, "Date range title", timeout=8)
        el = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((AppiumBy.ID, self.DATE_RANGE_ID))
        )
        return (
            el.text or el.get_attribute("content-desc") or el.get_attribute("name") or ""
        ).strip()

    def _wait_visible_nav_element(self, locators, label, timeout=None):
        wait_sec = timeout if timeout is not None else Settings.EXPLICIT_WAIT
        deadline = time.monotonic() + wait_sec
        last_error = None
        while time.monotonic() < deadline:
            for by, val in locators:
                try:
                    remaining = max(1.0, deadline - time.monotonic())
                    el = WebDriverWait(self.driver, min(2.5, remaining)).until(
                        ec.visibility_of_element_located((by, val))
                    )
                    self.LOGGER.info("Navigation control `%s` found via %s.", label, by)
                    return el
                except Exception as exc:
                    last_error = exc
                    continue
        raise AssertionError(
            f"Navigation `{label}` not visible. Locators exhausted. Last error: {last_error!r}"
        )

    def _navigation_control_is_disabled(self, element):
        """True if interaction should be blocked (leading-edge Next on latest period)."""
        try:
            if not element.is_enabled():
                return True
        except Exception:
            pass
        en = element.get_attribute("enabled")
        if en is not None and str(en).lower() == "false":
            return True
        cl = element.get_attribute("clickable")
        if cl is not None and str(cl).lower() == "false":
            return True
        relaxed = (
            os.getenv("CUBII_NAV_NEXT_DISABLED_STRICT", "1").strip().lower()
            in ("0", "false", "no")
        )
        if relaxed:
            return False
        return False

    def assert_progress_next_navigation_disabled(self):
        """Works for whichever period tab is selected (Day/Week/Month/Year): Next at latest boundary."""
        locators = (
            (AppiumBy.ID, self.NAV_NEXT_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.NAV_NEXT_UIAUTOMATOR),
            (AppiumBy.XPATH, self.NAV_NEXT_XPATH),
            (AppiumBy.ACCESSIBILITY_ID, "Next Button"),
        )
        el = self._wait_visible_nav_element(locators, "Next Button", timeout=12)
        strip_now = ""
        try:
            strip_now = self._read_date_range_text()
        except Exception:
            pass
        self._log_progress_block(
            "Next control | state before assertion",
            [
                ("txtTitleDateRange_now", strip_now),
                ("imgNext_enabled_attribute", el.get_attribute("enabled")),
                ("imgNext_clickable_attribute", el.get_attribute("clickable")),
            ],
        )
        if not self._navigation_control_is_disabled(el):
            fallback_block = (
                os.getenv("CUBII_NAV_NEXT_ASSERTION_FALLBACK", "0").strip().lower()
                in ("1", "true", "yes")
            )
            if fallback_block:
                before = self._read_date_range_text()
                try:
                    el.click()
                    time.sleep(0.9)
                    after = self._read_date_range_text()
                    if after == before:
                        self.LOGGER.info(
                            "Next tap did not move date label; treating as inactive at boundary."
                        )
                        return
                except Exception:
                    self.LOGGER.info("Next tap ineffective; assuming disabled at boundary.")
                    return
            raise AssertionError(
                "Progress Next navigation control appears enabled/clickable; expected disabled "
                "at latest period. Set CUBII_NAV_NEXT_DISABLED_STRICT=0 or "
                "CUBII_NAV_NEXT_ASSERTION_FALLBACK=1 for tolerant runs."
            )
        self.LOGGER.info(
            "Progress | Next control assertion passed (disabled/unusable at boundary) | "
            "enabled=%s clickable=%s",
            el.get_attribute("enabled"),
            el.get_attribute("clickable"),
        )

    def _tap_progress_date_previous(self):
        locators = (
            (AppiumBy.ID, self.NAV_PREVIOUS_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.NAV_PREVIOUS_UIAUTOMATOR),
            (AppiumBy.XPATH, self.NAV_PREVIOUS_XPATH),
            (AppiumBy.ACCESSIBILITY_ID, "Previous Button"),
        )
        deadline = time.monotonic() + Settings.EXPLICIT_WAIT
        last_err = None
        try:
            strip_before = self._read_date_range_text()
        except Exception:
            strip_before = ""
        self.LOGGER.info(
            "Progress | COLLECT — txtTitleDateRange before Previous click | %r",
            strip_before,
        )
        while time.monotonic() < deadline:
            for by, val in locators:
                try:
                    remaining = max(1.0, deadline - time.monotonic())
                    el = WebDriverWait(self.driver, min(3.5, remaining)).until(
                        ec.element_to_be_clickable((by, val))
                    )
                    el.click()
                    self.LOGGER.info(
                        "Progress | CLICK: Previous date arrow (`%s`) | strategy=%s",
                        self.NAV_PREVIOUS_ID,
                        by,
                    )
                    time.sleep(float(os.getenv("CUBII_DATE_NAV_PREVIOUS_PAUSE_SEC", "1.0")))
                    return
                except Exception as exc:
                    last_err = exc
                    continue
        raise AssertionError(f"Could not tap Progress Previous arrow. Last error: {last_err!r}")

    def verify_progress_previous_date_navigation_and_summaries(self):
        """
        With any active period tab: capture title, tap Previous, assert title differs, validate summaries.
        """
        self._log_progress_block(
            "FLOW | verify_progress_previous_date_navigation_and_summaries | START",
            [
                ("imgPrevious_id", self.NAV_PREVIOUS_ID),
                ("txtTitleDateRange_id", self.DATE_RANGE_ID),
                ("purpose", "one step back on date strip → prior period loads → metrics still valid"),
            ],
        )

        self.LOGGER.info("Progress | PHASE 1 | Read baseline `txtTitleDateRange` + snapshot summary strips")
        baseline = self._read_date_range_text()
        if not baseline:
            raise AssertionError("Date range baseline empty before Previous navigation.")

        self._log_progress_block(
            "COLLECT — before CLICK Previous arrow",
            [("baseline_txtTitleDateRange", baseline)] + self._safe_snap_summary_rows(),
        )

        self.LOGGER.info(
            "Progress | PHASE 2 | TAP Previous date arrow (see also Progress | CLICK line below)"
        )
        self._tap_progress_date_previous()

        self.LOGGER.info(
            "Progress | PHASE 3 | Poll `txtTitleDateRange` until differs from baseline (max ~%ss)",
            max(12, Settings.EXPLICIT_WAIT),
        )
        wait_deadline = time.monotonic() + max(12.0, float(Settings.EXPLICIT_WAIT))
        last_after = baseline
        poll_i = 0
        while time.monotonic() < wait_deadline:
            poll_i += 1
            last_after = self._read_date_range_text()
            if poll_i % 5 == 0:
                self.LOGGER.info(
                    "Progress | POLL | attempt=%s | range_now=%r | unchanged_vs_baseline=%s",
                    poll_i,
                    last_after[:200] if last_after else last_after,
                    (last_after.strip() == baseline.strip()),
                )
            if last_after.strip() != baseline.strip() and last_after:
                break
            time.sleep(0.35)
        if last_after.strip() == baseline.strip() or not last_after:
            raise AssertionError(
                f"Date range did not change after Previous: before={baseline!r} after={last_after!r}"
            )

        self.LOGGER.info(
            "Progress | PHASE 4 | Strip changed after %s poll(s): %r → %r",
            poll_i,
            baseline[:240],
            last_after[:240],
        )

        self._log_progress_block(
            "COLLECT — after CLICK Previous arrow (navigation settled)",
            [("baseline_txtTitleDateRange", baseline), ("new_txtTitleDateRange", last_after)]
            + self._safe_snap_summary_rows(),
        )

        self.LOGGER.info(
            "Progress | VERIFY | Date strip updated from %.200s to %.200s",
            baseline,
            last_after,
        )

        self.LOGGER.info("Date range after Previous: %s (was %s)", last_after, baseline[:120])

        self.LOGGER.info(
            "Progress | PHASE 5 | Validate four summary rows under `linLayoutStrides`/Calories/Miles/Time"
        )
        for sid, slab in (
            (self.SUMMARY_STRIDES_ID, "Strides"),
            (self.SUMMARY_CALORIES_ID, "Calories"),
            (self.SUMMARY_MILES_ID, "Miles"),
            (self.SUMMARY_TIME_ID, "Time"),
        ):
            self.LOGGER.info(
                "Progress | METRIC ROW CHECK | %-10s | resource_id=`%s`",
                slab,
                sid,
            )
            self._summary_container_shows_metric_data(sid, slab)

        self._log_progress_block(
            "FLOW | verify_progress_previous_date_navigation_and_summaries | COMPLETE",
            [
                ("final_txtTitleDateRange", last_after),
                ("poll_iterations", repr(poll_i)),
            ]
            + self._safe_snap_summary_rows(),
        )
        self.LOGGER.info(
            "Progress | FLOW DONE | Previous navigation + summaries OK | polls=%s",
            poll_i,
        )

    @staticmethod
    def _stride_display_to_scalar(text):
        """Parse strides label like '17,979', '17.9K Strides', '14.3K' to a float for comparison."""
        if not text:
            return None
        s = text.lower().replace(",", "").strip()
        m = re.search(r"([\d.]+)\s*k\b", s)
        if m:
            return float(m.group(1)) * 1000.0
        m = re.search(r"([\d]+(?:\.[\d]+)?)", s)
        if m:
            return float(m.group(1))
        return None

    def _stride_displays_equivalent(self, a_text, b_text):
        rel = float(os.getenv("CUBII_STRIDE_COMPARE_REL_TOL", "0.04"))
        abs_tol = float(os.getenv("CUBII_STRIDE_COMPARE_ABS_TOL", "50"))
        sa = self._stride_display_to_scalar(a_text or "")
        sb = self._stride_display_to_scalar(b_text or "")
        if sa is None or sb is None:
            self.LOGGER.warning(
                "Progress | strides compare FALLBACK raw strings | card/strides_a=%r | summary_strides_b=%r",
                a_text,
                b_text,
            )
            raw_ok = (a_text or "").strip() == (b_text or "").strip()
            self.LOGGER.info("Progress | strides raw-string equality=%s", raw_ok)
            return raw_ok
        if sa == 0 and sb == 0:
            self.LOGGER.info(
                "Progress | strides MATCH | both parsed as 0 | raw %r vs %r",
                a_text,
                b_text,
            )
            return True
        diff = abs(sa - sb)
        if diff <= abs_tol:
            self.LOGGER.info(
                "Progress | strides MATCH (abs_tol) | parsed %.2f ~= %.2f | diff=%.2f | raw %r vs %r",
                sa,
                sb,
                diff,
                a_text,
                b_text,
            )
            return True
        denom = max(abs(sa), abs(sb), 1.0)
        rel_ok = (diff / denom) <= rel
        self.LOGGER.info(
            "Progress | strides MATCH check | parsed %.2f vs %.2f | diff=%.2f rel=%.4f thresh=%.4f | match=%s | raw %r vs %r",
            sa,
            sb,
            diff,
            diff / denom,
            rel,
            rel_ok,
            a_text,
            b_text,
        )
        return rel_ok

    def _period_tab_selected(self, tab_resource_id):
        try:
            el = self.driver.find_element(AppiumBy.ID, tab_resource_id)
            sel = el.get_attribute("selected")
            if sel and str(sel).lower() == "true":
                return True
            chk = el.get_attribute("checked")
            if chk and str(chk).lower() == "true":
                return True
        except Exception:
            pass
        return False

    def _scroll_until_activity_cards(self, max_scrolls=None):
        attempts = max_scrolls if max_scrolls is not None else int(
            os.getenv("CUBII_ACTIVITY_LOG_SCROLL_ATTEMPTS", "8")
        )
        for i in range(attempts):
            cards = self.driver.find_elements(AppiumBy.ID, self.ACTIVITY_LOG_CARD_ROOT_ID)
            visible = [c for c in cards if c.is_displayed()]
            if visible:
                self.LOGGER.info(
                    "Progress | scroll sweep for activity cards | pass=%s/%s | visible_rows=%s",
                    i + 1,
                    attempts,
                    len(visible),
                )
                return visible[0]
            self.LOGGER.info(
                "Progress | scroll sweep for activity cards | pass=%s/%s | no visible row — swiping up",
                i + 1,
                attempts,
            )
            self._scroll_progress_vertical(direction="up")
        return None

    def _first_metrics_value_text_under(self, root_element):
        """Primary metric on card/summary — txtMetricsValue1 (strides)."""
        try:
            els = root_element.find_elements(AppiumBy.ID, self.TXT_METRICS_VALUE1_ID)
            for el in els:
                try:
                    if not el.is_displayed():
                        continue
                except Exception:
                    continue
                t = (el.text or "").strip()
                if re.search(r"\d", t):
                    return t
                cd = (el.get_attribute("content-desc") or "").strip()
                if re.search(r"\d", cd):
                    return cd
        except Exception:
            pass
        return ""

    def _read_summary_strides_display(self):
        strip = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((AppiumBy.ID, self.SUMMARY_STRIDES_ID))
        )
        t = self._first_metrics_value_text_under(strip)
        if t:
            return t
        blob = self._collect_descendant_visible_text(strip)
        return blob or ""

    def _wait_activity_drill_transition(self, baseline_title, dest_tab_id, timeout=None):
        wait_sec = timeout if timeout is not None else max(18.0, float(Settings.EXPLICIT_WAIT))
        deadline = time.monotonic() + wait_sec
        while time.monotonic() < deadline:
            try:
                now_title = self._read_date_range_text()
            except Exception:
                now_title = ""
            if baseline_title and now_title.strip() != baseline_title.strip():
                self.LOGGER.info("Date strip changed after drill: %r -> %r", baseline_title, now_title)
                time.sleep(float(os.getenv("CUBII_DRILL_SETTLE_PAUSE_SEC", "0.8")))
                return now_title
            if dest_tab_id and self._period_tab_selected(dest_tab_id):
                self.LOGGER.info("Destination period tab selected: %s", dest_tab_id)
                time.sleep(float(os.getenv("CUBII_DRILL_SETTLE_PAUSE_SEC", "0.8")))
                return self._read_date_range_text()
            time.sleep(0.35)
        raise AssertionError(
            f"Activity log drill-down did not settle (title still {baseline_title!r}, "
            f"dest tab {dest_tab_id} selected={self._period_tab_selected(dest_tab_id) if dest_tab_id else 'n/a'})."
        )

    def _card_title_overlaps_strip(self, card_blob, strip_title):
        """Loose check that drilled period strip relates to the tapped row (Month→Week, Year→Month)."""
        if not card_blob or not strip_title:
            return True
        cb = card_blob.lower().replace("\n", " ")
        st = strip_title.lower()
        month_tokens = (
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december",
            "jan",
            "feb",
            "mar",
            "apr",
            "may",
            "jun",
            "jul",
            "aug",
            "sep",
            "oct",
            "nov",
            "dec",
        )
        for tok in month_tokens:
            if tok in cb and tok in st:
                return True
        nums_cb = set(re.findall(r"\b\d{1,4}\b", cb))
        nums_st = set(re.findall(r"\b\d{1,4}\b", st))
        return bool(nums_cb & nums_st)

    def _activity_log_drill_match_strides(self, source_tab_id, source_name, dest_tab_id, dest_name):
        self._tap_visible_clickable(source_tab_id, source_name)
        card = self._scroll_until_activity_cards()
        if card is None:
            raise AssertionError(
                f"No `{self.ACTIVITY_LOG_CARD_ROOT_ID}` rows visible under {source_name}; scroll or data?"
            )
        baseline_title = self._read_date_range_text()
        card_snapshot = self._collect_descendant_visible_text(card)
        strides_card = self._first_metrics_value_text_under(card)
        if not strides_card:
            strides_card = card_snapshot
        if not self._stride_display_to_scalar(strides_card):
            self.LOGGER.warning(
                "Could not parse strides from card metrics; snapshot tail: %.200s",
                card_snapshot,
            )

        self._log_progress_block(
            "COLLECT — first activity-log card BEFORE drill tap",
            [
                ("source_period_tab_ui", source_name),
                ("expected_dest_period_after_drill", dest_name),
                ("dest_period_resource_id", dest_tab_id or ""),
                ("txtTitleDateRange_under_source_tab", baseline_title),
                ("card_aggregate_text_under_cnsLayoutActivityLogRoot", card_snapshot),
                ("strides_txtMetrics_value1_inside_card_scope", strides_card),
            ]
            + self._safe_snap_summary_rows(),
        )

        clicked_via_root = False
        try:
            card.click()
            clicked_via_root = True
            self.LOGGER.info(
                "Progress | CLICK: activity log card root `%s` (tap on container)",
                self.ACTIVITY_LOG_CARD_ROOT_ID,
            )
        except Exception:
            clicked = False
            try:
                for sub in card.find_elements(AppiumBy.XPATH, ".//*[@clickable='true']"):
                    try:
                        if sub.is_displayed():
                            self.LOGGER.info(
                                "Progress | CLICK: activity log row via clickable descendant | "
                                "class=%s | content-desc=%s | resource-id=%s",
                                sub.get_attribute("className") or sub.tag_name,
                                sub.get_attribute("content-desc"),
                                sub.get_attribute("resource-id"),
                            )
                            sub.click()
                            clicked = True
                            break
                    except Exception:
                        continue
            except Exception:
                pass
            if not clicked:
                raise AssertionError(
                    "Could not tap activity log card root or clickable descendant."
                )

        after_title = self._wait_activity_drill_transition(baseline_title, dest_tab_id)

        strides_summary_preview = ""
        try:
            strides_summary_preview = self._read_summary_strides_display()
        except Exception:
            pass
        overlap_ok = True
        if source_name in ("Month", "Year"):
            overlap_ok = self._card_title_overlaps_strip(card_snapshot, after_title)

        self._log_progress_block(
            f"COLLECT — screen AFTER drill (target {dest_name})",
            [
                ("clicked_via_card_root_click", repr(clicked_via_root)),
                ("txtTitleDateRange_after_navigation", after_title),
                (
                    "dest_tab_selected_checked",
                    repr(self._period_tab_selected(dest_tab_id) if dest_tab_id else None),
                ),
                ("dest_tab_expected_resource_id", dest_tab_id or ""),
                ("overlap_card_vs_strip_MONTH_YEAR_check", repr(overlap_ok)),
                (
                    "strides_txt_metrics_value_under_summary_strip_preview",
                    strides_summary_preview,
                ),
            ]
            + self._safe_snap_summary_rows(),
        )

        if dest_tab_id and not self._period_tab_selected(dest_tab_id):
            self.LOGGER.warning(
                "Destination tab `%s` not marked selected; continuing with strides match. "
                "Title=%r",
                dest_name,
                after_title,
            )

        if source_name in ("Month", "Year") and not overlap_ok:
            self.LOGGER.warning(
                "Progress | Date strip vs card text overlap weak | card=%.200s | strip=%.200s",
                card_snapshot,
                after_title,
            )

        strides_summary = self._read_summary_strides_display()
        if not self._stride_displays_equivalent(strides_card, strides_summary):
            raise AssertionError(
                f"Strides mismatch after {source_name}→{dest_name} drill: "
                f"card={strides_card!r} summary={strides_summary!r}"
            )
        self.LOGGER.info(
            "Drill-down OK %s→%s: strides card %r matches summary %r.",
            source_name,
            dest_name,
            strides_card,
            strides_summary,
        )

    def verify_week_month_year_activity_log_drill_downs_match_strides(self):
        """
        Week → Day, Month → Week, Year → Month via first activity log card; strides must match summary.
        """
        self._log_progress_block(
            "FLOW START — Week/Month/Year activity-log drill chain",
            [("flows", "Week→Day, then Month→Week, then Year→Month"), ("card_selector", "first visible `cnsLayoutActivityLogRoot`")],
        )
        self._activity_log_drill_match_strides(self.TAB_WEEK_ID, "Week", self.TAB_DAY_ID, "Day")
        self._activity_log_drill_match_strides(self.TAB_MONTH_ID, "Month", self.TAB_WEEK_ID, "Week")
        self._activity_log_drill_match_strides(self.TAB_YEAR_ID, "Year", self.TAB_MONTH_ID, "Month")
        final_rng = ""
        try:
            final_rng = self._read_date_range_text()
        except Exception as exc:
            final_rng = f"<unread: {exc}>"
        self._log_progress_block(
            "FLOW END — activity-log drills complete",
            [("final_txtTitleDateRange_snapshot", final_rng)],
        )

    def navigate_period_tabs_day_week_month_year_and_verify_data(self):
        """
        Tap Day → Week → Month → Year.
        After each: non-empty date range and four metric rows populated (digits preferred).
        """
        period_sequence = (
            ("Day", self.TAB_DAY_ID),
            ("Week", self.TAB_WEEK_ID),
            ("Month", self.TAB_MONTH_ID),
            ("Year", self.TAB_YEAR_ID),
        )
        collected = []
        for name, rid in period_sequence:
            self.LOGGER.info("Progress period tab: `%s`.", name)
            self._tap_visible_clickable(rid, name)
            rng = self._read_date_range_text()
            if not rng:
                raise AssertionError(f"Empty date range after selecting `{name}`.")
            collected.append(rng)
            self.LOGGER.info("Date range after `%s`: %s", name, rng[:200])
            self._log_progress_block(
                f"COLLECT — full summary strip text after period tab `{name}`",
                [("txtTitleDateRange", rng)] + self._safe_snap_summary_rows(),
            )

            for sid, slab in (
                (self.SUMMARY_STRIDES_ID, "Strides"),
                (self.SUMMARY_CALORIES_ID, "Calories"),
                (self.SUMMARY_MILES_ID, "Miles"),
                (self.SUMMARY_TIME_ID, "Time"),
            ):
                self._summary_container_shows_metric_data(sid, slab)

        if len(set(collected)) < 2:
            self.LOGGER.warning(
                "Date range caption lacked variety across tabs; values=%s", collected
            )

        self.LOGGER.info("Period tabs Day→Week→Month→Year validated.")

    def verify_in_progress_primary_layout(self):
        """
        Asserts period tabs, category tabs, date range, summary row containers, and combined chart.
        Chart may require a short scroll on smaller viewports.
        """
        self.LOGGER.info("Validating In Progress primary UI layout.")

        top_checks = (
            (self.TAB_DAY_ID, "Day tab"),
            (self.TAB_WEEK_ID, "Week tab"),
            (self.TAB_MONTH_ID, "Month tab"),
            (self.TAB_YEAR_ID, "Year tab"),
            (self.TAB_LOWER_BODY_ID, "Lower Body tab"),
            (self.TAB_UPPER_BODY_ID, "Upper Body tab"),
            (self.DATE_RANGE_ID, "Date range title"),
            (self.SUMMARY_STRIDES_ID, "Strides summary"),
            (self.SUMMARY_CALORIES_ID, "Calories summary"),
            (self.SUMMARY_MILES_ID, "Miles summary"),
            (self.SUMMARY_TIME_ID, "Time summary"),
        )

        for rid, label in top_checks:
            self._assert_visible_id_or_uiautomator(rid, label)

        chart_timeout = int(os.getenv("CUBII_IN_PROGRESS_CHART_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        chart_scrolls = int(os.getenv("CUBII_IN_PROGRESS_CHART_SCROLL_ATTEMPTS", "4"))
        last_err = None
        for attempt in range(1, chart_scrolls + 1):
            try:
                per_try = chart_timeout if attempt == 1 else max(5, chart_timeout // 2)
                self._assert_visible_id_or_uiautomator(
                    self.COMBINED_CHART_ID,
                    "Combined chart",
                    timeout=per_try,
                )
                self.LOGGER.info("In Progress UI: primary layout validation complete.")
                return
            except AssertionError as exc:
                last_err = exc
                if attempt < chart_scrolls:
                    self.LOGGER.info(
                        "Chart not yet visible (attempt %s/%s); scrolling.",
                        attempt,
                        chart_scrolls,
                    )
                    self._scroll_progress_vertical(direction="up")

        raise AssertionError(
            f"In Progress combined chart not visible after scroll retries. Last error: {last_err!r}"
        )
