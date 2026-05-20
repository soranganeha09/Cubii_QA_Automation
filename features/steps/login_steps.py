import logging

from behave import given, then, when


LOGGER = logging.getLogger("cubii_login_steps")


@given("the Cubii application is launched")
def step_launch_application(context):
    LOGGER.info("Step: launching Cubii application.")
    try:
        context.login_page.launch_application()
        LOGGER.info("Cubii application launch step completed.")
    except Exception as exc:
        LOGGER.exception("Application launch failed: %s", exc)
        raise AssertionError(f"Unable to launch Cubii application. Error: {exc}") from exc


@given("the Cubii login screen is visible")
def step_login_screen_visible(context):
    LOGGER.info("Step: validating login screen visibility.")
    try:
        context.login_page.wait_for_login_screen()
        LOGGER.info("Login screen validated.")
    except Exception as exc:
        LOGGER.exception("Login screen validation failed: %s", exc)
        raise AssertionError(f"Login screen is not visible. Error: {exc}") from exc


@when("the user enters valid email and password")
def step_enter_credentials(context):
    LOGGER.info("Step: entering valid credentials.")
    try:
        context.login_page.enter_email(context.login_page.EMAIL)
        context.login_page.enter_password(context.login_page.PASSWORD)
        LOGGER.info("Valid credentials entered.")
    except Exception as exc:
        LOGGER.exception("Entering credentials failed: %s", exc)
        raise AssertionError(f"Unable to enter credentials. Error: {exc}") from exc


@when("the user taps the SIGN IN button")
def step_tap_sign_in(context):
    LOGGER.info("Step: tapping SIGN IN.")
    try:
        context.login_page.tap_sign_in()
        LOGGER.info("SIGN IN tapped.")
    except Exception as exc:
        LOGGER.exception("Tap SIGN IN failed: %s", exc)
        raise AssertionError(f"Unable to tap SIGN IN button. Error: {exc}") from exc


@then("the user should be successfully logged in")
def step_verify_logged_in(context):
    LOGGER.info("Step: verifying successful login.")
    try:
        assert context.login_page.is_logged_in(), "Post-login element was not visible."
        LOGGER.info("Successful Login scenario passed.")
        print("SUCCESS: User logged in successfully via BDD flow.")
    except Exception as exc:
        LOGGER.exception("Login verification failed: %s", exc)
        print(f"FAILURE: User login failed in BDD flow. Error: {exc}")
        raise


@when("the user taps Continue with Google")
def step_tap_continue_with_google(context):
    LOGGER.info("Step: tapping 'Login with Google'.")
    try:
        context.login_page.tap_continue_with_google()
        LOGGER.info("'Login with Google' tapped.")
    except Exception as exc:
        LOGGER.exception("Tapping Google login failed: %s", exc)
        raise AssertionError(f"Unable to tap 'Login with Google'. Error: {exc}") from exc


@then("the Agree and Login popup is displayed")
def step_verify_agree_login_popup(context):
    LOGGER.info("Step: verifying 'Agree and Login' popup visibility.")
    assert context.login_page.is_agree_login_popup_visible(), (
        "'Agree and Login' popup did not appear after tapping 'Login with Google'."
    )


@when("the user taps Agree and Login")
def step_tap_agree_and_login(context):
    LOGGER.info("Step: tapping AGREE AND LOGIN.")
    try:
        context.login_page.tap_agree_and_login()
        LOGGER.info("AGREE AND LOGIN tapped.")
    except Exception as exc:
        LOGGER.exception("Tap AGREE AND LOGIN failed: %s", exc)
        raise AssertionError(f"Unable to tap AGREE AND LOGIN. Error: {exc}") from exc


@then("the Choose an account popup is displayed")
def step_verify_choose_account_popup(context):
    LOGGER.info("Step: verifying Google 'Choose an account' chooser visibility.")
    assert context.login_page.is_choose_account_popup_visible(), (
        "Google 'Choose an account' chooser did not appear."
    )


@when("the user selects an available Google account")
def step_select_google_account(context):
    LOGGER.info("Step: selecting Google account.")
    try:
        context.login_page.select_google_account()
        LOGGER.info("Google account selected.")
    except Exception as exc:
        LOGGER.exception("Selecting Google account failed: %s", exc)
        raise AssertionError(f"Unable to select Google account. Error: {exc}") from exc


@then("the user is redirected to the Cubii home screen")
def step_verify_redirected_home(context):
    LOGGER.info("Step: verifying redirect to Cubii home screen after Google login.")
    try:
        assert context.login_page.is_logged_in(), (
            "App did not return to home screen after Google login."
        )
        LOGGER.info("Google Login scenario passed.")
        print("SUCCESS: User logged in successfully via Google.")
    except Exception as exc:
        LOGGER.exception("Google login verification failed: %s", exc)
        print(f"FAILURE: Google login flow failed. Error: {exc}")
        raise


@when("the user taps the three dots menu")
def step_tap_three_dots_menu(context):
    LOGGER.info("Step: tapping the three-dot Settings menu on home screen.")
    try:
        context.home_page.tap_settings_highlight()
    except Exception as exc:
        LOGGER.exception("Tapping three-dot Settings failed: %s", exc)
        raise AssertionError(
            f"Unable to tap three-dot Settings menu. Error: {exc}"
        ) from exc


@when("the user taps Logout from the menu")
def step_tap_logout_menu_item(context):
    LOGGER.info("Step: tapping Logout entry in Settings menu.")
    try:
        context.home_page.tap_logout_menu_item()
    except Exception as exc:
        LOGGER.exception("Tapping Logout menu item failed: %s", exc)
        raise AssertionError(
            f"Unable to tap Logout in Settings menu. Error: {exc}"
        ) from exc


@when("the user confirms Logout")
def step_confirm_logout(context):
    LOGGER.info("Step: tapping Logout confirmation button.")
    try:
        context.home_page.tap_logout_confirm()
        context.bootstrap_completed = False
    except Exception as exc:
        LOGGER.exception("Confirming Logout failed: %s", exc)
        raise AssertionError(
            f"Unable to confirm Logout. Error: {exc}"
        ) from exc


@then("the user is signed out and the login screen is visible")
def step_verify_signed_out(context):
    LOGGER.info("Step: verifying the user has been signed out.")
    try:
        context.login_page.wait_for_login_screen()
        LOGGER.info("Login screen is visible after logout.")
        print("SUCCESS: User signed out and returned to login screen.")
    except Exception as exc:
        LOGGER.exception("Logout verification failed: %s", exc)
        print(f"FAILURE: Logout flow failed. Error: {exc}")
        raise AssertionError(
            f"Login screen was not visible after logout. Error: {exc}"
        ) from exc


@when("the user taps Continue with Facebook")
def step_tap_continue_with_facebook(context):
    LOGGER.info("Step: tapping 'Login with Facebook'.")
    try:
        context.login_page.tap_continue_with_facebook()
        LOGGER.info("'Login with Facebook' tapped.")
    except Exception as exc:
        LOGGER.exception("Tapping Facebook login failed: %s", exc)
        raise AssertionError(
            f"Unable to tap 'Login with Facebook'. Error: {exc}"
        ) from exc


@when("the user enters valid Facebook credentials")
def step_enter_facebook_credentials(context):
    LOGGER.info("Step: entering Facebook credentials.")
    try:
        context.login_page.enter_facebook_credentials()
        LOGGER.info("Facebook credentials entered.")
    except Exception as exc:
        LOGGER.exception("Entering Facebook credentials failed: %s", exc)
        raise AssertionError(
            f"Unable to enter Facebook credentials. Error: {exc}"
        ) from exc


@when("the user submits the Facebook login form")
def step_submit_facebook_login(context):
    LOGGER.info("Step: submitting Facebook login form.")
    try:
        context.login_page.submit_facebook_login()
        LOGGER.info("Facebook login submitted.")
    except Exception as exc:
        LOGGER.exception("Submitting Facebook login failed: %s", exc)
        raise AssertionError(
            f"Unable to submit Facebook login. Error: {exc}"
        ) from exc
