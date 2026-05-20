import logging  # Use module logger consistent with other step modules

from behave import given, then, when  # BDD decorators for step binding

# Keep in sync with `BOOTSTRAP_SKIP_TAGS` in features/environment.py (avoid importing environment here).
_NON_BLE_BOOTSTRAP_SKIP_TAGS = {"skip_bootstrap", "no_bootstrap", "raw_ftue"}

LOGGER = logging.getLogger("cubii_non_ble_connection_steps")  # Logger name used in behave output


@given("the app is launched and user is resolved to home for Non-BLE flow")  # Gherkin: precondition scenario line
def step_resolve_user_state_for_non_ble(context):  # Implements Given step binding
    LOGGER.info(  # Announce sub-flow start at INFO level
        "Step Started: Resolve app state (login / logged-in / FTUE) for Non-BLE flow."  # Human-readable message string
    )
    try:  # Isolate failures into assertion with traceback in logs
        scenario_tags = set(getattr(context.scenario, "effective_tags", []) or [])
        skip_bootstrap = bool(scenario_tags.intersection(_NON_BLE_BOOTSTRAP_SKIP_TAGS))
        if getattr(context, "bootstrap_completed", False) and not skip_bootstrap:
            LOGGER.info(
                "Skipping redundant launch_application(); automatic scenario bootstrap already prepared the app."
            )
        else:
            context.login_page.launch_application()  # Bring Cubii to foreground when bootstrap did not run or skip tag
        context.ftue_page.ensure_logged_in_or_on_home()  # Handle login screen vs logged-in detection

        if context.ftue_page.is_ftue_present():  # Conditional: overlays still requesting FTUE
            LOGGER.info("FTUE indicators present; completing FTUE dynamic flow.")  # Explain extra branch execution
            context.ftue_page.execute_ftue_dynamic_flow()  # Run walkthrough till Home when needed

        assert context.non_ble_connection_page.is_home_screen_ready(), (  # Must see Home before flow
            "Home screen is not ready. Expected LET'S GO card, CONNECT NEW DEVICE, imgNonBleBanner, imageView35, or device card."
        )
        LOGGER.info("Step Passed: User reached Home screen for Non-BLE entry.")  # Success marker for precondition
        context.non_ble_result = False  # Initialize outcome flag until When step succeeds
    except Exception as exc:  # Any unexpected precondition error path
        LOGGER.exception("Precondition failed for Non-BLE flow: %s", exc)  # Full traceback for troubleshooting
        raise AssertionError(f"Could not resolve app state for Non-BLE flow. Error: {exc}") from exc  # Normalize failure


@when("the user completes the end-to-end Cubii Non-BLE connection flow")  # Gherkin When action clause
def step_execute_non_ble_flow(context):  # Executes main Non-BLE automation path
    LOGGER.info("Step Started: Execute Non-BLE connection flow.")  # Log action step start timestamp via logging
    try:  # Isolate page object exceptions for consistent scenario failure text
        context.non_ble_connection_page.connect_non_ble_device_end_to_end()  # Delegate full UI flow to page
        context.non_ble_result = True  # Mark behavioral success flag for Then step
        LOGGER.info("Step Passed: Non-BLE flow completed.")  # Confirmation before assertions in Then step
    except Exception as exc:  # Covers TimeoutException and AssertionError from page layer
        context.non_ble_result = False  # Prevent Then from falsely passing silently
        LOGGER.exception("Non-BLE flow failed: %s", exc)  # Preserve stack trace in behave output
        raise AssertionError(f"Non-BLE connection flow failed. Error: {exc}") from exc  # Surface clean behave failure


@when("the user opens Add Manual Workout from Home ensuring Non-BLE connectivity")  # Add Workout probe or pair then tap
def step_open_add_manual_workout_from_home(context):  # Non-BLE manual workout entry navigation
    LOGGER.info(
        "Step Started: Open Add Manual Workout — probe Add Workout CTAs / connect Non-BLE if absent / wait for editor."
    )
    try:
        context.non_ble_connection_page.open_add_manual_workout_from_home()
        context.add_manual_workout_navigated = True
        LOGGER.info("Step Passed: Add Manual Workout navigation from Home succeeded.")
    except Exception as exc:
        LOGGER.exception("Add Manual Workout navigation failed: %s", exc)
        context.add_manual_workout_navigated = False
        raise AssertionError(
            f"Add Manual Workout flow failed opening from Home. Error: {exc}"
        ) from exc


@then("the Add Manual Workout screen should show title and manual entry fields")  # Editor title + labelled rows
def step_then_add_manual_workout_screen_valid(context):
    LOGGER.info(
        "Step Started: Validate Add Manual Workout screen elements and title text."
    )
    assert getattr(
        context,
        "add_manual_workout_navigated",
        False,
    ), "Add Manual Workout screen check skipped because navigation step did not succeed."
    try:
        context.non_ble_connection_page.verify_add_manual_workout_screen()
        LOGGER.info("Step Passed: Add Manual Workout screen validation succeeded.")
    except Exception as exc:
        LOGGER.exception("Add Manual Workout screen validation failed: %s", exc)
        raise AssertionError(
            f"Add Manual Workout screen assertion failed. Error: {exc}"
        ) from exc


@when("the user selects Start Date as current date and confirms")
def step_select_start_date_current(context):
    LOGGER.info("Step Started: Select Start Date as current date and confirm.")
    try:
        context.non_ble_connection_page.select_start_date_current_and_confirm()
        LOGGER.info("Step Passed: Start Date selected and confirmed.")
    except Exception as exc:
        LOGGER.exception("Selecting Start Date failed: %s", exc)
        raise AssertionError(f"Could not select Start Date. Error: {exc}") from exc


@when("the user selects Start Date as yesterday and confirms")
def step_select_start_date_yesterday(context):
    LOGGER.info("Step Started: Select Start Date as yesterday and confirm.")
    try:
        context.non_ble_connection_page.select_start_date_yesterday_and_confirm()
        LOGGER.info("Step Passed: Start Date selected as yesterday and confirmed.")
    except Exception as exc:
        LOGGER.exception("Selecting yesterday Start Date failed: %s", exc)
        raise AssertionError(f"Could not select yesterday Start Date. Error: {exc}") from exc


@when("the user selects Start Time as a past time and confirms")
def step_select_start_time_past(context):
    LOGGER.info("Step Started: Select Start Time as past time and confirm.")
    try:
        context.non_ble_connection_page.select_start_time_past_and_confirm()
        LOGGER.info("Step Passed: Start Time selected as past time and confirmed.")
    except Exception as exc:
        LOGGER.exception("Selecting Start Time failed: %s", exc)
        raise AssertionError(f"Could not select Start Time. Error: {exc}") from exc


@when("the user selects Start Time as a random past time and confirms")
@then("the user selects Start Time as a random past time and confirms")
def step_select_start_time_random_past(context):
    # Recovery leg: this step can be placed after future-time validation check.
    if getattr(context, "manual_workout_future_time_check_done", False):
        if not getattr(context, "manual_workout_time_error_found", False):
            LOGGER.info(
                "Skipping random past Start Time reselection because no future-time validation error was shown."
            )
            context.manual_workout_retry_time_set = False
            return
        context.manual_workout_retry_time_set = True
    LOGGER.info("Step Started: Select Start Time as random past time and confirm.")
    try:
        context.non_ble_connection_page.select_start_time_random_past_and_confirm()
        LOGGER.info("Step Passed: Start Time selected as random past time and confirmed.")
    except Exception as exc:
        LOGGER.exception("Selecting random past Start Time failed: %s", exc)
        raise AssertionError(f"Could not select random past Start Time. Error: {exc}") from exc


@when("the user selects Duration and submits")
def step_select_duration_and_submit(context):
    LOGGER.info("Step Started: Select Duration and submit.")
    try:
        context.non_ble_connection_page.select_duration_and_submit()
        LOGGER.info("Step Passed: Duration selected and submitted.")
    except Exception as exc:
        LOGGER.exception("Selecting Duration failed: %s", exc)
        raise AssertionError(f"Could not select Duration. Error: {exc}") from exc


@when("the user enters valid Strides value")
def step_enter_valid_strides(context):
    LOGGER.info("Step Started: Enter valid Strides value.")
    try:
        context.non_ble_connection_page.enter_valid_strides_value()
        LOGGER.info("Step Passed: Valid Strides entered.")
    except Exception as exc:
        LOGGER.exception("Entering Strides failed: %s", exc)
        raise AssertionError(f"Could not enter Strides. Error: {exc}") from exc


@when("the user enters strides value {stride_count:d}")
def step_enter_numeric_strides(context, stride_count):
    LOGGER.info("Step Started: Enter Strides value %s.", stride_count)
    try:
        context.non_ble_connection_page.enter_valid_strides_value(stride_count)
        LOGGER.info("Step Passed: Strides entered as %s.", stride_count)
    except Exception as exc:
        LOGGER.exception("Entering Strides failed: %s", exc)
        raise AssertionError(f"Could not enter Strides. Error: {exc}") from exc


@then('the strides validation error should be "{expected_message}"')
def step_verify_strides_validation_error(context, expected_message):
    LOGGER.info("Step Started: Verify strides validation error message.")
    try:
        context.non_ble_connection_page.verify_strides_validation_error(expected_message)
        LOGGER.info("Step Passed: Strides validation error verified.")
    except Exception as exc:
        LOGGER.exception("Strides validation error check failed: %s", exc)
        raise AssertionError(
            f"Strides validation error check failed. Error: {exc}"
        ) from exc


@when("the user enters 0 Strides value")
@then("the user enters 0 Strides value")
def step_enter_zero_strides(context):
    LOGGER.info("Step Started: Enter 0 Strides value.")
    try:
        context.non_ble_connection_page.enter_zero_strides_value()
        LOGGER.info("Step Passed: 0 Strides entered.")
    except Exception as exc:
        LOGGER.exception("Entering 0 Strides failed: %s", exc)
        raise AssertionError(f"Could not enter 0 Strides. Error: {exc}") from exc


@when("the user sets a valid Resistance level")
def step_set_valid_resistance(context):
    LOGGER.info("Step Started: Set a valid Resistance level.")
    try:
        context.non_ble_connection_page.set_valid_resistance_level()
        LOGGER.info("Step Passed: Resistance level set.")
    except Exception as exc:
        LOGGER.exception("Setting Resistance failed: %s", exc)
        raise AssertionError(f"Could not set Resistance. Error: {exc}") from exc


@when("the user taps Save on Add Manual Workout")
@then("the user taps Save on Add Manual Workout")
def step_tap_save_manual_workout(context):
    # Recovery leg: second Save should happen only when future-time error was actually displayed.
    if getattr(context, "manual_workout_future_time_check_done", False):
        if not getattr(context, "manual_workout_time_error_found", False):
            LOGGER.info(
                "Skipping Save retry because no future-time validation error was shown."
            )
            return
        if not getattr(context, "manual_workout_retry_time_set", False):
            LOGGER.info(
                "Skipping Save retry because Start Time reselection step did not run in recovery path."
            )
            return
    LOGGER.info("Step Started: Tap Save on Add Manual Workout.")
    try:
        context.non_ble_connection_page.tap_save_manual_workout()
        LOGGER.info("Step Passed: Save tapped for Add Manual Workout.")
    except Exception as exc:
        LOGGER.exception("Tapping Save failed: %s", exc)
        raise AssertionError(f"Could not tap Save. Error: {exc}") from exc


@then("the user taps Save on Add Manual Workout and save button should be in disable")
@then("the user taps Save on Add Manual Workout and save button should be disabled")
def step_tap_save_and_verify_disabled(context):
    LOGGER.info("Step Started: Verify Save button remains disabled on Add Workout screen.")
    try:
        context.non_ble_connection_page.verify_save_button_disabled_on_add_workout()
        LOGGER.info("Step Passed: Save button disabled validation succeeded.")
    except Exception as exc:
        LOGGER.exception("Save button disabled validation failed: %s", exc)
        raise AssertionError(
            f"Save button disabled validation failed. Error: {exc}"
        ) from exc


@then("the manual workout form should be saved without validation errors")
def step_validate_manual_workout_saved(context):
    LOGGER.info("Step Started: Validate no manual workout validation errors are shown.")
    try:
        context.non_ble_connection_page.verify_manual_workout_saved_without_errors()
        LOGGER.info("Step Passed: Manual workout saved without validation errors.")
    except Exception as exc:
        LOGGER.exception("Manual workout final validation failed: %s", exc)
        raise AssertionError(
            f"Manual workout save validation failed. Error: {exc}"
        ) from exc


@then('if time validation is shown it should say either "You cannot enter data for future time" or "This time is overlapping another workout entry."')
@then('if time validation is shown it should say "You cannot enter data for future time"')
def step_validate_future_time_error_if_present(context):
    LOGGER.info(
        "Step Started: If time validation appears after Save, verify retryable time error message."
    )
    try:
        max_retries = 10
        has_error = context.non_ble_connection_page.verify_future_time_error_if_present()
        retry_count = 0
        while has_error and retry_count < max_retries:
            retry_count += 1
            LOGGER.warning(
                "Retryable time validation still visible after Save. "
                "Recovery attempt %s/%s: reselection of random past Start Time + Save.",
                retry_count,
                max_retries,
            )
            context.non_ble_connection_page.select_start_time_random_past_and_confirm()
            context.non_ble_connection_page.tap_save_manual_workout()
            has_error = context.non_ble_connection_page.verify_future_time_error_if_present()
        if has_error:
            raise AssertionError(
                "Retryable time validation persisted after retries. "
                f"Attempts={max_retries}. Message should disappear after Start Time correction."
            )
        context.manual_workout_future_time_check_done = True
        context.manual_workout_time_error_found = has_error
        context.manual_workout_retry_time_set = retry_count > 0
        LOGGER.info(
            "Step Passed: Retryable time validation check complete (error_found=%s, recovery_attempts=%s).",
            has_error,
            retry_count,
        )
    except Exception as exc:
        LOGGER.exception("Retryable time validation check failed: %s", exc)
        raise AssertionError(
            f"Retryable time validation assertion failed. Error: {exc}"
        ) from exc


@then("the manual workout confirmation pop-up should display saved workout details")
def step_validate_manual_workout_confirmation_popup(context):
    LOGGER.info("Step Started: Validate manual workout confirmation pop-up details.")
    if getattr(context, "manual_workout_time_error_found", False):
        LOGGER.info(
            "Skipping confirmation pop-up validation because expected future-time validation error is displayed."
        )
        return
    try:
        context.non_ble_connection_page.verify_manual_workout_confirmation_popup_details()
        LOGGER.info("Step Passed: Manual workout confirmation pop-up details validated.")
    except Exception as exc:
        LOGGER.exception("Manual workout confirmation pop-up validation failed: %s", exc)
        raise AssertionError(
            f"Manual workout confirmation pop-up validation failed. Error: {exc}"
        ) from exc


@when("the user opens the first manual workout entry for editing")
def step_open_first_manual_workout_for_edit(context):
    LOGGER.info("Step Started: Open first manual workout for editing.")
    try:
        context.non_ble_connection_page.open_first_manual_workout_for_edit()
        LOGGER.info("Step Passed: Manual workout editor opened for edit.")
    except Exception as exc:
        LOGGER.exception("Open manual workout for edit failed: %s", exc)
        raise AssertionError(
            f"Could not open manual workout for edit. Error: {exc}"
        ) from exc


@then("the Edit Workout screen should be displayed")
def step_edit_workout_screen_displayed(context):
    LOGGER.info("Step Started: Assert Edit Workout screen.")
    try:
        context.non_ble_connection_page.verify_edit_workout_screen_displayed()
        LOGGER.info("Step Passed: Edit Workout screen is displayed.")
    except Exception as exc:
        LOGGER.exception("Edit Workout screen assertion failed: %s", exc)
        raise AssertionError(
            f"Edit Workout screen not shown as expected. Error: {exc}"
        ) from exc


@then("the edited manual workout should be visible in In Progress with expected details")
def step_verify_edited_manual_in_progress(context):
    LOGGER.info("Step Started: Verify edited manual workout on In Progress.")
    try:
        context.non_ble_connection_page.verify_edited_manual_workout_details_in_in_progress()
        LOGGER.info("Step Passed: Edited manual workout details verified.")
    except Exception as exc:
        LOGGER.exception("Edited manual workout verification failed: %s", exc)
        raise AssertionError(
            f"Edited manual workout verification failed. Error: {exc}"
        ) from exc


@when("the user clicks on the Add Manual Workout button")
@when("the user click on the Add workout button")
@then("the user clicks on the Add Manual Workout button")
@then("the user click on the Add workout button")
def step_click_add_manual_workout_from_progress(context):
    LOGGER.info("Step Started: Tap Add Manual Workout on Progress/In Progress.")
    try:
        context.non_ble_connection_page.tap_add_manual_workout_on_progress_tab()
        context.add_manual_workout_navigated = True
        LOGGER.info("Step Passed: Add Manual Workout opened from Progress tab.")
    except Exception as exc:
        LOGGER.exception("Add Manual Workout from Progress failed: %s", exc)
        context.add_manual_workout_navigated = False
        raise AssertionError(
            f"Could not tap Add Manual Workout on Progress tab. Error: {exc}"
        ) from exc


@when("the user opens In Progress tab")
@then("the user opens In Progress tab")
def step_open_in_progress_tab(context):
    LOGGER.info("Step Started: Open In Progress tab.")
    try:
        context.non_ble_connection_page.open_in_progress_tab()
        LOGGER.info("Step Passed: In Progress tab opened.")
    except Exception as exc:
        LOGGER.exception("Open In Progress tab failed: %s", exc)
        raise AssertionError(f"Could not open In Progress tab. Error: {exc}") from exc


@when("the user clicks on the Home tab")
@then("the user clicks on the Home tab")
def step_click_home_tab(context):
    LOGGER.info("Step Started: Open Home tab.")
    try:
        context.non_ble_connection_page.open_home_tab()
        LOGGER.info("Step Passed: Home tab opened.")
    except Exception as exc:
        LOGGER.exception("Open Home tab failed: %s", exc)
        raise AssertionError(f"Could not open Home tab. Error: {exc}") from exc


@then("the manually added workout should be visible in In Progress")
def step_verify_manual_workout_in_progress(context):
    LOGGER.info("Step Started: Verify manually added workout is visible in In Progress.")
    try:
        context.non_ble_connection_page.verify_manual_workout_visible_in_in_progress()
        LOGGER.info("Step Passed: Manually added workout is visible in In Progress.")
    except Exception as exc:
        LOGGER.exception("In Progress manual workout validation failed: %s", exc)
        raise AssertionError(
            f"In Progress manual workout validation failed. Error: {exc}"
        ) from exc


@when("the user refreshes the page")
@when("the user refersh the page")
@then("the user refreshes the page")
@then("the user refersh the page")
def step_refresh_page(context):
    LOGGER.info("Step Started: Refresh page (pull-to-refresh).")
    try:
        context.non_ble_connection_page.refresh_page_pull_down()
        LOGGER.info("Step Passed: Page refresh gesture completed.")
    except Exception as exc:
        LOGGER.exception("Refresh page failed: %s", exc)
        raise AssertionError(f"Could not refresh the page. Error: {exc}") from exc


@then("the Non-BLE Cubii device should be saved and visible on Home")  # Gherkin Then acceptance criteria
def step_validate_non_ble_outcome(context):  # Final validations on connected Home dashboard
    LOGGER.info("Step Started: Validate Non-BLE post-connection state.")  # Start post-condition logging block
    assert getattr(context, "non_ble_result", False), (  # Guard if When aborted without setting truthy flag
        "Non-BLE flow did not complete successfully."  # Clear reason when intermediate step failed silently
    )
    context.non_ble_connection_page.validate_non_ble_connected_state()  # Detailed UI asserts on cards and CTAs
    LOGGER.info("Step Passed: Non-BLE device visible on Home with expected controls.")  # End-to-end acceptance log line
