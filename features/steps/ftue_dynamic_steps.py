import logging

from behave import given, then, when


LOGGER = logging.getLogger("cubii_ftue_dynamic_steps")


@given("the user starts the Cubii FTUE flow")
def step_start_ftue(context):
    LOGGER.info("Step: starting Cubii FTUE dynamic workflow.")
    context.ftue_result = False


@when("the user completes login and FTUE steps with dynamic checks")
def step_execute_ftue(context):
    LOGGER.info("Step: executing FTUE workflow with dynamic Wellness Journii handling.")
    try:
        context.ftue_page.execute_ftue_dynamic_flow()
        context.ftue_result = True
        LOGGER.info("FTUE dynamic workflow execution completed.")
    except Exception as exc:
        LOGGER.exception("FTUE dynamic workflow failed: %s", exc)
        context.ftue_result = False
        raise AssertionError(f"FTUE workflow failed with error: {exc}") from exc


@then("the FTUE flow should complete without failing on optional screens")
def step_verify_ftue_completion(context):
    LOGGER.info("Step: verifying FTUE completion status.")
    assert context.ftue_result, "FTUE dynamic workflow did not complete successfully."
    LOGGER.info("SUCCESS: FTUE flow completed with optional screen resilience.")
    print("SUCCESS: Cubii FTUE dynamic flow completed.")


@given("the user has a connected Cubii device on the home page")
def step_connected_device_precondition(context):
    LOGGER.info("Step: ensuring connected-device precondition on Home.")
    try:
        context.home_page.connect_ble_device_end_to_end(scan_retries=3)
        context.manual_disconnect_result = False
        LOGGER.info("Connected-device precondition satisfied.")
    except Exception as exc:
        LOGGER.exception("Failed to satisfy connected-device precondition: %s", exc)
        raise AssertionError(f"Connected-device precondition failed. Error: {exc}") from exc


@when("the user manually disconnects the Cubii device from the control card")
def step_manual_disconnect(context):
    LOGGER.info("Step: executing manual disconnect workflow.")
    try:
        context.home_page.manually_disconnect_connected_device()
        context.manual_disconnect_result = True
        LOGGER.info("Manual disconnect workflow execution completed.")
    except Exception as exc:
        context.manual_disconnect_result = False
        LOGGER.exception("Manual disconnect workflow failed: %s", exc)
        raise AssertionError(f"Manual disconnect workflow failed. Error: {exc}") from exc


@then("the Cubii device should show disconnected state with connect and change devices actions")
def step_verify_manual_disconnect(context):
    LOGGER.info("Step: verifying manual disconnect workflow status.")
    assert getattr(context, "manual_disconnect_result", False), (
        "Manual disconnect workflow did not complete successfully."
    )
    LOGGER.info("SUCCESS: Manual disconnect scenario completed.")

