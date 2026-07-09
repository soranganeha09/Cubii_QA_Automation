import logging
import os

from behave import then, when

LOGGER = logging.getLogger("cubii_report_a_problem_steps")


@when("the user click on the Report a Problem")
@then("the user click on the Report a Problem")
def step_click_report_a_problem(context):
    LOGGER.info("Step: clicking Report a Problem from Settings menu.")
    try:
        context.home_page.tap_report_a_problem_menu_item()
        LOGGER.info("Step passed: Report a Problem screen opened.")
    except Exception as exc:
        LOGGER.exception("Clicking Report a Problem menu item failed: %s", exc)
        raise AssertionError(
            f"Unable to click Report a Problem menu item. Error: {exc}"
        ) from exc


@when("the user verify the fields")
@then("the user verify the fields")
def step_verify_report_a_problem_fields(context):
    LOGGER.info("Step: verifying Report a Problem form fields.")
    try:
        context.report_a_problem_page.verify_report_a_problem_fields()
        LOGGER.info("Step passed: Report a Problem fields verified.")
    except Exception as exc:
        LOGGER.exception("Report a Problem fields verification failed: %s", exc)
        raise AssertionError(
            f"Report a Problem fields verification failed. Error: {exc}"
        ) from exc


@when("the user click on the cancel button")
@then("the user click on the cancel button")
def step_click_report_a_problem_cancel_button(context):
    LOGGER.info("Step: clicking Report a Problem cancel button.")
    try:
        context.report_a_problem_page.tap_cancel_button()
        LOGGER.info("Step passed: Report a Problem cancel button clicked.")
    except Exception as exc:
        LOGGER.exception("Report a Problem cancel button click failed: %s", exc)
        raise AssertionError(
            f"Could not click Report a Problem cancel button. Error: {exc}"
        ) from exc


@when(
    "the user verify that SEND button display in disable mode "
    "without adding subject and Description"
)
@then(
    "the user verify that SEND button display in disable mode "
    "without adding subject and Description"
)
def step_verify_send_button_disabled_without_input(context):
    LOGGER.info(
        "Step: verify SEND button is disabled without subject and description."
    )
    try:
        context.report_a_problem_page.verify_send_button_disabled_without_input()
        LOGGER.info("Step passed: SEND button verified disabled without input.")
    except Exception as exc:
        LOGGER.exception("SEND button disabled verification failed: %s", exc)
        raise AssertionError(
            f"SEND button disabled verification failed. Error: {exc}"
        ) from exc


@when("the user add the subject and Description")
@then("the user add the subject and Description")
def step_add_report_a_problem_subject_and_description(context):
    LOGGER.info("Step: add subject and description on Report a Problem form.")
    subject = os.getenv(
        "CUBII_REPORT_A_PROBLEM_SUBJECT", "QA automated report subject"
    )
    description = os.getenv(
        "CUBII_REPORT_A_PROBLEM_DESCRIPTION",
        "QA automated report description for Cubii app testing.",
    )
    try:
        context.report_a_problem_page.enter_subject_and_description(
            subject, description
        )
        LOGGER.info("Step passed: subject and description added.")
    except Exception as exc:
        LOGGER.exception("Adding subject and description failed: %s", exc)
        raise AssertionError(
            f"Could not add subject and description. Error: {exc}"
        ) from exc


@when("the user click on send button")
@then("the user click on send button")
def step_click_report_a_problem_send_button(context):
    LOGGER.info("Step: click SEND button on Report a Problem form.")
    try:
        context.report_a_problem_page.tap_send_button()
        LOGGER.info("Step passed: SEND button clicked.")
    except Exception as exc:
        LOGGER.exception("SEND button click failed: %s", exc)
        raise AssertionError(
            f"Could not click SEND button. Error: {exc}"
        ) from exc


@when("the user close the application")
@then("the user close the application")
def step_close_application(context):
    LOGGER.info("Step: close the Cubii application.")
    try:
        context.home_page.close_application()
        LOGGER.info("Step passed: application closed.")
    except Exception as exc:
        LOGGER.exception("Closing application failed: %s", exc)
        raise AssertionError(
            f"Could not close the application. Error: {exc}"
        ) from exc
