import logging

from behave import given, then, when

LOGGER = logging.getLogger("cubii_in_progress_steps")


@when("the user opens the application and completes login and FTUE as required")
def step_open_app_login_ftue_to_home(context):
    """
    Delegates to FTUEPage.execute_ftue_dynamic_flow(): launch, login if needed,
    FTUE when indicators are present, optional Wellness/webview handling, Home.
    """
    LOGGER.info("Step: open app - login / Home / FTUE handled dynamically.")
    try:
        context.ftue_page.execute_ftue_dynamic_flow()
        LOGGER.info("Step passed: dynamic login and FTUE flow completed.")
    except Exception as exc:
        LOGGER.exception("Dynamic login/FTUE flow failed: %s", exc)
        raise AssertionError(f"Application could not reach a stable post-FTUE state. Error: {exc}") from exc


@given("the user has reached the Home screen with login and FTUE resolved")
def step_given_home_with_login_ftue(context):
    """Same resolution path as the opening When step — supports running Scenario 2 independently."""
    LOGGER.info("Step: precondition — Home via login/FTUE resolution.")
    try:
        context.ftue_page.execute_ftue_dynamic_flow()
        LOGGER.info("Step passed: user on Home (login/FTUE resolved).")
    except Exception as exc:
        LOGGER.exception("Precondition failed (Home / login / FTUE): %s", exc)
        raise AssertionError(f"Could not reach Home with login and FTUE resolved. Error: {exc}") from exc


@when("the user opens the In Progress tab")
def step_when_open_in_progress_with_article(context):
    """Opens Progress / In Progress from bottom nav (same flow as Non-BLE steps; wording includes 'the')."""
    LOGGER.info("Step: open In Progress tab.")
    try:
        context.non_ble_connection_page.open_in_progress_tab()
        LOGGER.info("Step passed: In Progress tab opened.")
    except Exception as exc:
        LOGGER.exception("Open In Progress tab failed: %s", exc)
        raise AssertionError(f"Could not open In Progress tab. Error: {exc}") from exc


@then("the Home screen should be displayed")
def step_then_home_screen_displayed(context):
    LOGGER.info("Step: assert Cubii Home logo visible (app bar iv_logo / content-desc Cubii).")
    try:
        context.home_page.verify_cubii_home_logo_visible()
        LOGGER.info("Step passed: Home Cubii logo visible.")
    except AssertionError:
        raise
    except Exception as exc:
        LOGGER.exception("Home screen check failed: %s", exc)
        raise AssertionError(f"Home screen validation failed. Error: {exc}") from exc


@then("the user should see the complete In Progress primary layout")
def step_then_in_progress_primary_ui(context):
    LOGGER.info("Step: validate In Progress tabs, summaries, and chart.")
    try:
        context.in_progress_page.verify_in_progress_primary_layout()
        LOGGER.info("Step passed: In Progress primary UI validated.")
    except Exception as exc:
        LOGGER.exception("In Progress UI validation failed: %s", exc)
        raise AssertionError(f"In Progress screen validation failed. Error: {exc}") from exc


@when("the user navigates each Progress period tab and verifies data for Day Week Month and Year")
def step_navigate_period_tabs_verify_data(context):
    LOGGER.info("Step: Day Week Month Year taps + date range + summary metrics.")
    try:
        context.in_progress_page.navigate_period_tabs_day_week_month_year_and_verify_data()
        LOGGER.info("Step passed: Progress period tab data checks.")
    except Exception as exc:
        LOGGER.exception("Progress period tabs failed: %s", exc)
        raise AssertionError(f"Progress period tab validation failed. Error: {exc}") from exc


@then("the Cubii Progress Next date control should be disabled at the latest period")
def step_then_progress_next_disabled(context):
    """Next (imgNext) disabled when viewing the newest interval for Day/Week/Month/Year."""
    LOGGER.info("Step: Progress Next arrow should be inactive.")
    try:
        context.in_progress_page.assert_progress_next_navigation_disabled()
        LOGGER.info("Step passed: Next control disabled.")
    except Exception as exc:
        LOGGER.exception("Progress Next disabled check failed: %s", exc)
        raise AssertionError(f"Progress Next navigation state failed. Error: {exc}") from exc


@when("the user opens the prior Progress period with the date arrow and validates metrics")
def step_when_progress_previous_nav_validates(context):
    """Previous (imgPrevious): date title changes; summary rows still show valid data."""
    sc = getattr(context, "scenario", None)
    scenario_name = getattr(sc, "name", "<unknown>")
    tags = getattr(sc, "effective_tags", []) or []
    LOGGER.info(
        "BDD | STEP START | scenario=%r | tags=%s",
        scenario_name,
        sorted(set(tags)),
    )
    LOGGER.info(
        "BDD | INTENT | Navigate one period BACK via `%s` (content-desc Previous Button); "
        "expect `txtTitleDateRange` to change; then re-verify Strides Calories Miles Time strips.",
        "com.cubii:id/imgPrevious",
    )
    LOGGER.info(
        "BDD | DELEGATING → InProgressPage.verify_progress_previous_date_navigation_and_summaries()"
    )
    try:
        context.in_progress_page.verify_progress_previous_date_navigation_and_summaries()
        LOGGER.info(
            "BDD | STEP PASSED | prior Progress period opened + summaries OK | scenario=%r",
            scenario_name,
        )
    except Exception as exc:
        LOGGER.exception(
            "BDD | STEP FAILED | prior Progress period | scenario=%r | error=%s",
            scenario_name,
            exc,
        )
        raise AssertionError(f"Progress Previous date navigation failed. Error: {exc}") from exc


@when("the user verifies Progress activity log drill-down stride parity across Week Month and Year")
def step_activity_log_drill_stride_parity(context):
    """First activity row under Week/Month/Year drills to Day/Week/Month; strides match txtMetricsValue1."""
    LOGGER.info("Step: activity log drill-down chain.")
    try:
        context.in_progress_page.verify_week_month_year_activity_log_drill_downs_match_strides()
        LOGGER.info("Step passed: activity log drill-down strides.")
    except Exception as exc:
        LOGGER.exception("Activity log drill-down failed: %s", exc)
        raise AssertionError(f"Activity log drill-down validation failed. Error: {exc}") from exc
