import logging

from behave import given, then, when


LOGGER = logging.getLogger("cubii_signup_steps")


@given("the user opens the Cubii application for sign up")
def step_open_cubii_for_signup(context):
    LOGGER.info("Step: launching Cubii app for sign-up flow.")
    try:
        context.signup_page.launch_application()
    except Exception as exc:
        LOGGER.exception("Unable to launch app for sign-up: %s", exc)
        raise AssertionError(f"Unable to open Cubii application for sign-up. Error: {exc}") from exc


@when("the user taps Sign up with email")
def step_tap_signup_with_email(context):
    LOGGER.info("Step: tapping Sign up with email card.")
    try:
        context.signup_page.open_signup_with_email()
    except Exception as exc:
        LOGGER.exception("Unable to open sign-up with email screen: %s", exc)
        raise AssertionError(
            f"Unable to tap Sign up with email. Error: {exc}"
        ) from exc


@when("the user enters random sign up details")
def step_enter_random_signup_details(context):
    LOGGER.info("Step: entering random user details into sign-up form.")
    try:
        context.signup_payload = context.signup_page.generate_signup_data()
        context.signup_page.fill_signup_form(context.signup_payload)
        LOGGER.info(
            "Sign-up data entered (email=%s).",
            context.signup_payload["email"],
        )
    except Exception as exc:
        LOGGER.exception("Entering random sign-up details failed: %s", exc)
        raise AssertionError(
            f"Unable to enter random sign-up details. Error: {exc}"
        ) from exc


@when("the user selects a random birthdate and confirms it")
def step_select_random_birthdate(context):
    LOGGER.info("Step: selecting random birthdate from picker and confirming.")
    try:
        context.signup_page.select_random_birthdate_and_confirm()
    except Exception as exc:
        LOGGER.exception("Selecting random birthdate failed: %s", exc)
        raise AssertionError(
            f"Unable to select random birthdate. Error: {exc}"
        ) from exc


@when("the user accepts terms and conditions")
@then("the user accepts terms and conditions")
def step_accept_terms(context):
    LOGGER.info("Step: accepting terms and conditions.")
    try:
        context.signup_page.accept_terms_only()
    except Exception as exc:
        LOGGER.exception("Accepting terms failed: %s", exc)
        raise AssertionError(
            f"Unable to accept terms and conditions. Error: {exc}"
        ) from exc


@when("the user clicks on the sign up button")
@then("the user clicks on the sign up button")
def step_click_sign_up_button(context):
    LOGGER.info("Step: clicking SIGN UP button.")
    try:
        context.signup_page.tap_sign_up_button()
        LOGGER.info("Step passed: SIGN UP button clicked.")
    except Exception as exc:
        LOGGER.exception("Clicking SIGN UP button failed: %s", exc)
        raise AssertionError(
            f"Unable to click SIGN UP button. Error: {exc}"
        ) from exc


@then("the sign up request is submitted")
def step_verify_signup_submitted(context):
    LOGGER.info("Step: confirming sign-up submit action completed.")
    payload = getattr(context, "signup_payload", {})
    assert payload.get("email"), "Sign-up payload was not generated."
    LOGGER.info("Sign-up request submitted with generated email: %s", payload["email"])


@then("the sign up button should be disabled")
def step_verify_signup_button_disabled(context):
    LOGGER.info("Step: verifying SIGN UP button is disabled on empty form.")
    try:
        context.signup_page.verify_sign_up_button_disabled()
        LOGGER.info("Step passed: SIGN UP button is disabled when no data is entered.")
    except Exception as exc:
        LOGGER.exception("SIGN UP disabled-state verification failed: %s", exc)
        raise AssertionError(
            f"SIGN UP button should be disabled when no sign-up data is entered. Error: {exc}"
        ) from exc


def _verify_signup_field_error(context, field_key):
    expected = context.signup_page.SIGNUP_FIELD_ERROR_MESSAGES.get(field_key)
    if not expected:
        raise AssertionError(
            f"Unknown sign-up field for error validation: {field_key!r}. "
            f"Supported fields: {sorted(context.signup_page.SIGNUP_FIELD_ERROR_MESSAGES)}"
        )
    LOGGER.info("Step: verifying sign-up error message for %s.", field_key)
    try:
        context.signup_page.verify_signup_field_error_message(field_key, expected)
        LOGGER.info("Step passed: %s error message verified.", field_key)
    except Exception as exc:
        LOGGER.exception("Sign-up %s error verification failed: %s", field_key, exc)
        raise AssertionError(
            f"Sign-up {field_key} error message verification failed. Error: {exc}"
        ) from exc


@then("the user verifies the error message of the first name")
def step_verify_first_name_error(context):
    _verify_signup_field_error(context, "first name")


@then("the user verifies the error message of the last name")
def step_verify_last_name_error(context):
    _verify_signup_field_error(context, "last name")


@then("the user verifies the error message of the email")
def step_verify_email_error(context):
    _verify_signup_field_error(context, "email")


@then("the user verifies the error message of the password")
def step_verify_password_error(context):
    _verify_signup_field_error(context, "password")


@then("the user verifies the error message of the repeat password")
def step_verify_repeat_password_error(context):
    _verify_signup_field_error(context, "repeat password")


@then("the user verifies the error message of the birthday")
def step_verify_birthday_error(context):
    _verify_signup_field_error(context, "birthday")

