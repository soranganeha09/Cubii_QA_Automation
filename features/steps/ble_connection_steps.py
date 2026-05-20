import logging

from behave import given, then, when


LOGGER = logging.getLogger("cubii_ble_connection_steps")


@given("the user is on the Cubii home tab for BLE pairing")
def step_user_on_home_for_ble(context):
    LOGGER.info("Step: user is ready on home tab for BLE pairing.")


@given("the app is ready with a logged-in user and a connected Cubii device")
def step_app_ready_logged_in_and_connected(context):
    LOGGER.info("Step: normalizing app state (open/login/home/connected).")
    try:
        context.login_page.launch_application()
        context.ftue_page.ensure_logged_in_or_on_home()
        context.home_page.ensure_connected_on_home(scan_retries=3)
        context.ble_stability_result = False
        LOGGER.info("State normalization completed successfully.")
    except Exception as exc:
        LOGGER.exception("State normalization failed: %s", exc)
        raise AssertionError(f"Unable to normalize app state for BLE stability test. Error: {exc}") from exc


@when("the user completes the end-to-end Cubii BLE connection flow")
def step_execute_ble_connection_flow(context):
    LOGGER.info("Step: executing BLE connection flow from Home page object.")
    try:
        context.home_page.connect_ble_device_end_to_end(scan_retries=3)
        context.ble_connection_result = True
        LOGGER.info("BLE connection flow completed successfully.")
    except Exception as exc:
        context.ble_connection_result = False
        LOGGER.exception("BLE connection flow execution failed: %s", exc)
        raise AssertionError(f"BLE connection flow failed. Error: {exc}") from exc


@when("the user scans for Cubii while the device is powered off")
def step_execute_ble_powered_off_flow(context):
    LOGGER.info("Step: executing BLE powered-OFF scan workflow.")
    try:
        context.home_page.connect_ble_when_device_powered_off()
        context.ble_powered_off_result = True
        LOGGER.info("BLE powered-OFF workflow completed successfully.")
    except Exception as exc:
        context.ble_powered_off_result = False
        LOGGER.exception("BLE powered-OFF workflow failed: %s", exc)
        raise AssertionError(f"BLE powered-OFF workflow failed. Error: {exc}") from exc


@when("the user attempts BLE connection while phone Bluetooth is off")
def step_execute_ble_bluetooth_off_flow(context):
    LOGGER.info("Step: executing BLE workflow with phone Bluetooth OFF.")
    try:
        context.home_page.connect_ble_when_phone_bluetooth_off(scan_retries=3)
        context.ble_bluetooth_off_result = True
        LOGGER.info("BLE phone-Bluetooth-OFF workflow completed successfully.")
    except Exception as exc:
        context.ble_bluetooth_off_result = False
        LOGGER.exception("BLE phone-Bluetooth-OFF workflow failed: %s", exc)
        raise AssertionError(f"BLE phone-Bluetooth-OFF workflow failed. Error: {exc}") from exc


@when("the user restarts the app")
def step_restart_app(context):
    LOGGER.info("Step: restarting app and validating auto-reconnect behavior.")
    try:
        context.home_page.restart_app_and_validate_auto_reconnect(reconnect_timeout_seconds=30)
        context.ble_restart_result = True
        LOGGER.info("App restart workflow completed successfully.")
    except Exception as exc:
        context.ble_restart_result = False
        LOGGER.exception("App restart workflow failed: %s", exc)
        raise AssertionError(f"App restart workflow failed. Error: {exc}") from exc


@then("the Cubii device should be connected and connection details should be visible")
def step_validate_ble_connection_success(context):
    LOGGER.info("Step: validating BLE flow success status.")
    assert getattr(context, "ble_connection_result", False), (
        "BLE connection flow did not complete successfully."
    )


@then("the powered-off BLE scan should show retry guidance and handle retry or skip safely")
def step_validate_ble_powered_off_success(context):
    LOGGER.info("Step: validating BLE powered-OFF workflow status.")
    assert getattr(context, "ble_powered_off_result", False), (
        "BLE powered-OFF workflow did not complete successfully."
    )


@then("the Bluetooth-off flow should enforce enable, recover, and continue BLE connection")
def step_validate_ble_bluetooth_off_success(context):
    LOGGER.info("Step: validating BLE phone-Bluetooth-OFF workflow status.")
    assert getattr(context, "ble_bluetooth_off_result", False), (
        "BLE phone-Bluetooth-OFF workflow did not complete successfully."
    )


@then("the Cubii device should auto-reconnect after app relaunch")
def step_validate_restart_auto_reconnect(context):
    LOGGER.info("Step: validating restart auto-reconnect result.")
    assert getattr(context, "ble_restart_result", False), (
        "BLE restart auto-reconnect workflow did not complete successfully."
    )


@then("the connect button should not be visible on the device control card after restart")
def step_validate_connect_hidden_post_restart(context):
    LOGGER.info("Step: validating CONNECT button is hidden after restart.")
    assert getattr(context, "ble_restart_result", False), (
        "CONNECT button hidden-state after restart could not be confirmed."
    )


@when("the user pedals for {duration_seconds:d} seconds with the app in foreground")
def step_validate_foreground_pedaling(context, duration_seconds):
    LOGGER.info("Step: validating foreground pedaling sync for %s seconds.", duration_seconds)
    try:
        context.home_page.validate_foreground_pedaling_sync(
            duration_seconds=duration_seconds,
            poll_interval_seconds=5,
            min_required_increments=1,
        )
        context.ble_stability_result = True
        LOGGER.info("Foreground pedaling sync validation completed successfully.")
    except Exception as exc:
        context.ble_stability_result = False
        LOGGER.exception("Foreground pedaling sync validation failed: %s", exc)
        raise AssertionError(f"Foreground pedaling sync validation failed. Error: {exc}") from exc


@when("the user pedals while the app is in background for {duration_seconds:d} seconds")
def step_validate_background_pedaling(context, duration_seconds):
    LOGGER.info("Step: validating background pedaling sync for %s seconds.", duration_seconds)
    try:
        context.home_page.validate_background_pedaling_sync(
            background_seconds=duration_seconds,
            min_required_increments=1,
        )
        context.ble_stability_result = True
        LOGGER.info("Background pedaling sync validation completed successfully.")
    except Exception as exc:
        context.ble_stability_result = False
        LOGGER.exception("Background pedaling sync validation failed: %s", exc)
        raise AssertionError(f"Background pedaling sync validation failed. Error: {exc}") from exc


@when("the user does not pedal for {duration_seconds:d} seconds with the app in foreground")
def step_validate_foreground_no_pedaling(context, duration_seconds):
    LOGGER.info("Step: validating foreground no-pedaling stability for %s seconds.", duration_seconds)
    try:
        context.home_page.validate_foreground_no_pedaling_stability(
            duration_seconds=duration_seconds,
            poll_interval_seconds=5,
        )
        context.ble_stability_result = True
        LOGGER.info("Foreground no-pedaling stability validation completed successfully.")
    except Exception as exc:
        context.ble_stability_result = False
        LOGGER.exception("Foreground no-pedaling stability validation failed: %s", exc)
        raise AssertionError(f"Foreground no-pedaling stability validation failed. Error: {exc}") from exc


@when("the user does not pedal while the app is in background for {duration_seconds:d} seconds")
def step_validate_background_no_pedaling(context, duration_seconds):
    LOGGER.info("Step: validating background no-pedaling stability for %s seconds.", duration_seconds)
    try:
        context.home_page.validate_background_no_pedaling_stability(
            background_seconds=duration_seconds,
        )
        context.ble_stability_result = True
        LOGGER.info("Background no-pedaling stability validation completed successfully.")
    except Exception as exc:
        context.ble_stability_result = False
        LOGGER.exception("Background no-pedaling stability validation failed: %s", exc)
        raise AssertionError(f"Background no-pedaling stability validation failed. Error: {exc}") from exc


@when("the user is {activity} for {duration_seconds:d} seconds with the app in foreground")
def step_validate_foreground_by_activity(context, activity, duration_seconds):
    normalized_activity = activity.strip().lower()
    LOGGER.info(
        "Step: routing foreground activity `%s` for duration=%s seconds.",
        normalized_activity,
        duration_seconds,
    )
    if normalized_activity == "pedaling":
        step_validate_foreground_pedaling(context, duration_seconds)
    elif normalized_activity == "not pedaling":
        step_validate_foreground_no_pedaling(context, duration_seconds)
    else:
        raise AssertionError(
            f"Unsupported activity `{activity}` for foreground scenario. "
            "Use `pedaling` or `not pedaling`."
        )
    context.expected_metric_behavior = normalized_activity
    LOGGER.info(
        "Foreground activity `%s` completed with ble_stability_result=%s.",
        normalized_activity,
        getattr(context, "ble_stability_result", None),
    )


@when("the user is {activity} while the app is in background for {duration_seconds:d} seconds")
def step_validate_background_by_activity(context, activity, duration_seconds):
    normalized_activity = activity.strip().lower()
    LOGGER.info(
        "Step: routing background activity `%s` for duration=%s seconds.",
        normalized_activity,
        duration_seconds,
    )
    if normalized_activity == "pedaling":
        step_validate_background_pedaling(context, duration_seconds)
    elif normalized_activity == "not pedaling":
        step_validate_background_no_pedaling(context, duration_seconds)
    else:
        raise AssertionError(
            f"Unsupported activity `{activity}` for background scenario. "
            "Use `pedaling` or `not pedaling`."
        )
    context.expected_metric_behavior = normalized_activity
    LOGGER.info(
        "Background activity `%s` completed with ble_stability_result=%s.",
        normalized_activity,
        getattr(context, "ble_stability_result", None),
    )


@then("the BLE connection should remain active during the foreground session")
def step_assert_foreground_connection_active(context):
    LOGGER.info("Step: asserting BLE remained active in foreground session.")
    assert getattr(context, "ble_stability_result", False), (
        "Foreground BLE stability verification did not complete successfully."
    )


@then("the BLE connection should remain active after app returns to foreground")
def step_assert_background_connection_active(context):
    LOGGER.info("Step: asserting BLE remained active after background session.")
    assert getattr(context, "ble_stability_result", False), (
        "Background BLE stability verification did not complete successfully."
    )


@then("the pedal metric should increase from the baseline")
def step_assert_pedal_metric_increased_foreground(context):
    LOGGER.info("Step: pedal metric increase already verified during foreground workflow.")
    assert getattr(context, "ble_stability_result", False), (
        "Foreground pedal metric verification did not complete successfully."
    )


@then("the pedal metric should increase compared to the baseline")
def step_assert_pedal_metric_increased_background(context):
    LOGGER.info("Step: pedal metric increase already verified during background workflow.")
    assert getattr(context, "ble_stability_result", False), (
        "Background pedal metric verification did not complete successfully."
    )


@then("the pedal metric should remain unchanged from the baseline")
def step_assert_pedal_metric_unchanged(context):
    LOGGER.info("Step: pedal metric unchanged verification already validated in no-pedaling workflow.")
    assert getattr(context, "ble_stability_result", False), (
        "No-pedaling pedal metric verification did not complete successfully."
    )


@then("the pedal metric should {expected_behavior} from the baseline for {activity}")
def step_assert_metric_behavior_by_activity(context, expected_behavior, activity):
    normalized_activity = activity.strip().lower()
    normalized_behavior = expected_behavior.strip().lower()
    expected_activity = getattr(context, "expected_metric_behavior", "")
    LOGGER.info(
        "Step: validating metric behavior mapping activity=%s expected_behavior=%s tracked_activity=%s result=%s",
        normalized_activity,
        normalized_behavior,
        expected_activity,
        getattr(context, "ble_stability_result", None),
    )
    assert expected_activity == normalized_activity, (
        f"Metric behavior activity mismatch. Expected `{normalized_activity}`, got `{expected_activity}`."
    )

    valid_behavior_by_activity = {
        "pedaling": "increase",
        "not pedaling": "remain unchanged",
    }
    expected_for_activity = valid_behavior_by_activity.get(normalized_activity)
    assert expected_for_activity is not None, (
        f"Unsupported activity `{normalized_activity}` for metric behavior validation."
    )
    assert normalized_behavior == expected_for_activity, (
        "Metric behavior mismatch for activity. "
        f"Activity `{normalized_activity}` expects `{expected_for_activity}`, got `{normalized_behavior}`."
    )

    assert getattr(context, "ble_stability_result", False), (
        "Metric verification did not complete successfully for "
        f"`{normalized_activity}` with expected behavior `{normalized_behavior}`."
    )
