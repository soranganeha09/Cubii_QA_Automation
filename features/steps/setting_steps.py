import logging

from behave import then, when

LOGGER = logging.getLogger("setting_steps")


@when("the user click on the Setting")
@then("the user click on the Setting")
def step_click_setting(context):
    LOGGER.info("Step: clicking Settings from Settings menu.")
    try:
        context.home_page.tap_settings_menu_item()
        LOGGER.info("Step passed: Settings menu item tapped.")
    except Exception as exc:
        LOGGER.exception("Clicking Settings menu item failed: %s", exc)
        raise AssertionError(
            f"Unable to click Settings menu item. Error: {exc}"
        ) from exc


@when("the user click on the dark mode")
@then("the user click on the dark mode")
def step_click_dark_mode(context):
    LOGGER.info("Step: tapping DARK theme on Settings screen.")
    try:
        context.settings_page.tap_dark_mode()
        LOGGER.info("Step passed: DARK theme option tapped.")
    except Exception as exc:
        LOGGER.exception("Tapping DARK theme option failed: %s", exc)
        raise AssertionError(
            f"Unable to tap DARK theme option on Settings. Error: {exc}"
        ) from exc


@when("the user click on the back button")
@then("the user click on the back button")
def step_click_back_button(context):
    LOGGER.info("Step: tapping back button (Navigate up).")
    try:
        context.settings_page.tap_back_button()
        LOGGER.info("Step passed: back button (Navigate up) tapped.")
    except Exception as exc:
        LOGGER.exception("Back button (Navigate up) tap failed: %s", exc)
        raise AssertionError(
            f"Unable to tap back button (Navigate up). Error: {exc}"
        ) from exc


@when("the user click on the more screen back button")
@then("the user click on the more screen back button")
def step_click_more_screen_back_button(context):
    LOGGER.info("Step: tapping More screen back button (`iv_back`).")
    try:
        context.home_page.tap_back_button()
        LOGGER.info("Step passed: More screen back button tapped.")
    except Exception as exc:
        LOGGER.exception("More screen back button tap failed: %s", exc)
        raise AssertionError(
            f"Unable to tap More screen back button. Error: {exc}"
        ) from exc


@when("the user switch to light mode")
@then("the user switch to light mode")
def step_switch_to_light_mode(context):
    LOGGER.info("Step: tapping LIGHT theme on Settings screen.")
    try:
        context.settings_page.tap_light_mode()
        LOGGER.info("Step passed: LIGHT theme option tapped.")
    except Exception as exc:
        LOGGER.exception("Tapping LIGHT theme option failed: %s", exc)
        raise AssertionError(
            f"Unable to switch to LIGHT theme on Settings. Error: {exc}"
        ) from exc


@when("the user verify that My Account screen is in light mode")
@then("the user verify that My Account screen is in light mode")
def step_verify_my_account_screen_light_mode(context):
    LOGGER.info("Step: verify My Account screen is in light mode.")
    try:
        context.settings_page.verify_my_account_screen_light_mode(context.home_page)
        LOGGER.info("Step passed: My Account light mode verified.")
    except Exception as exc:
        LOGGER.exception("My Account light mode verification failed: %s", exc)
        raise AssertionError(
            f"My Account screen was not verified in light mode. Error: {exc}"
        ) from exc


@when("the user verify the Settings screen is in light mode")
@then("the user verify the Settings screen is in light mode")
def step_verify_settings_screen_light_mode(context):
    LOGGER.info("Step: verify Settings screen is in light mode.")
    try:
        context.settings_page.verify_settings_screen_light_mode()
        LOGGER.info("Step passed: Settings light mode verified.")
    except Exception as exc:
        LOGGER.exception("Settings light mode verification failed: %s", exc)
        raise AssertionError(
            f"Settings screen was not verified in light mode. Error: {exc}"
        ) from exc


@when("the user verify the More screen is in dark mode")
@then("the user verify the More screen is in dark mode")
def step_verify_more_screen_dark_mode(context):
    LOGGER.info("Step: verify More menu screen is in dark mode.")
    try:
        context.settings_page.verify_more_screen_dark_mode()
        LOGGER.info("Step passed: More menu dark mode verified.")
    except Exception as exc:
        LOGGER.exception("More menu dark mode verification failed: %s", exc)
        raise AssertionError(
            f"More menu screen was not verified in dark mode. Error: {exc}"
        ) from exc


@when("the user verify the My Account screen is in dark mode")
@then("the user verify the My Account screen is in dark mode")
def step_verify_my_account_screen_dark_mode(context):
    LOGGER.info("Step: verify My Account screen is in dark mode.")
    try:
        context.settings_page.verify_my_account_screen_dark_mode(context.home_page)
        LOGGER.info("Step passed: My Account dark mode verified.")
    except Exception as exc:
        LOGGER.exception("My Account dark mode verification failed: %s", exc)
        raise AssertionError(
            f"My Account screen was not verified in dark mode. Error: {exc}"
        ) from exc


@when("the user verify the Settings screen is in dark mode")
@then("the user verify the Settings screen is in dark mode")
def step_verify_settings_screen_dark_mode(context):
    LOGGER.info("Step: verify Settings screen is in dark mode.")
    try:
        context.settings_page.verify_settings_screen_dark_mode()
        LOGGER.info("Step passed: Settings dark mode verified.")
    except Exception as exc:
        LOGGER.exception("Settings dark mode verification failed: %s", exc)
        raise AssertionError(
            f"Settings screen was not verified in dark mode. Error: {exc}"
        ) from exc


@when("the user verify that theme change to dark mode on all the tabs")
@then("the user verify that theme change to dark mode on all the tabs")
def step_verify_dark_mode_on_all_tabs(context):
    LOGGER.info("Step: verify dark theme on all bottom-nav tabs.")
    try:
        context.settings_page.verify_dark_mode_on_all_tabs(
            communitii_page=context.communitii_page,
            wellness_journii_page=context.wellness_journii_page,
            cubii_studio_page=context.cubii_studio_page,
            ftue_page=getattr(context, "ftue_page", None),
        )
        LOGGER.info("Step passed: dark theme verified on all tabs.")
    except Exception as exc:
        LOGGER.exception("Dark theme verification on all tabs failed: %s", exc)
        raise AssertionError(
            f"Dark theme was not verified on all tabs. Error: {exc}"
        ) from exc


@when("the user click on the KMS")
@then("the user click on the KMS")
def step_click_kms(context):
    LOGGER.info("Step: tapping KMS distance unit on Settings screen.")
    try:
        context.settings_page.tap_kms()
        LOGGER.info("Step passed: KMS distance unit option tapped.")
    except Exception as exc:
        LOGGER.exception("Tapping KMS distance unit option failed: %s", exc)
        raise AssertionError(
            f"Unable to tap KMS distance unit option on Settings. Error: {exc}"
        ) from exc


@when("the user verify the pop-up Miles -> KM")
@then("the user verify the pop-up Miles -> KM")
def step_verify_distance_unit_popup_miles_to_km(context):
    LOGGER.info("Step: verify distance unit popup title is Miles -> KM.")
    try:
        context.settings_page.verify_distance_unit_popup_miles_to_km()
        LOGGER.info("Step passed: distance unit popup Miles -> KM verified.")
    except Exception as exc:
        LOGGER.exception("Distance unit popup verification failed: %s", exc)
        raise AssertionError(
            f"Distance unit popup was not verified as Miles -> KM. Error: {exc}"
        ) from exc


@when("the user click on the OK option of the pop-up")
@then("the user click on the OK option of the pop-up")
def step_click_metric_changed_done_ok(context):
    LOGGER.info("Step: tapping OK on distance unit confirmation popup.")
    try:
        context.settings_page.tap_metric_changed_done_ok()
        LOGGER.info("Step passed: distance unit popup OK tapped.")
    except Exception as exc:
        LOGGER.exception("Tapping distance unit popup OK failed: %s", exc)
        raise AssertionError(
            f"Unable to tap OK on distance unit popup. Error: {exc}"
        ) from exc


@when("the user click on the setting back button")
@then("the user click on the setting back button")
def step_click_setting_back_button(context):
    LOGGER.info("Step: tapping Settings screen back button (Navigate up).")
    try:
        context.settings_page.tap_back_button()
        LOGGER.info("Step passed: Settings back button tapped.")
    except Exception as exc:
        LOGGER.exception("Settings back button tap failed: %s", exc)
        raise AssertionError(
            f"Unable to tap Settings back button. Error: {exc}"
        ) from exc


@when("the user click on the more option back button")
@then("the user click on the more option back button")
def step_click_more_option_back_button(context):
    LOGGER.info("Step: tapping More screen back button (`iv_back`).")
    try:
        context.home_page.tap_back_button()
        LOGGER.info("Step passed: More option back button tapped.")
    except Exception as exc:
        LOGGER.exception("More option back button tap failed: %s", exc)
        raise AssertionError(
            f"Unable to tap More option back button. Error: {exc}"
        ) from exc


@when("the user verify that KMS display on the home screen")
@then("the user verify that KMS display on the home screen")
def step_verify_kms_display_on_home_screen(context):
    LOGGER.info("Step: verify KMS distance unit on home screen.")
    try:
        context.home_page.verify_kms_display_on_home_screen()
        LOGGER.info("Step passed: KMS distance unit verified on home screen.")
    except Exception as exc:
        LOGGER.exception("Home screen KMS verification failed: %s", exc)
        raise AssertionError(
            f"KMS was not verified on the home screen. Error: {exc}"
        ) from exc


@when("the user click on the Miles")
@then("the user click on the Miles")
def step_click_miles(context):
    LOGGER.info("Step: tapping Miles distance unit on Settings screen.")
    try:
        context.settings_page.tap_miles()
        LOGGER.info("Step passed: Miles distance unit option tapped.")
    except Exception as exc:
        LOGGER.exception("Tapping Miles distance unit option failed: %s", exc)
        raise AssertionError(
            f"Unable to tap Miles distance unit option on Settings. Error: {exc}"
        ) from exc


@when("the user verify the pop-up KM -> Miles")
@then("the user verify the pop-up KM -> Miles")
def step_verify_distance_unit_popup_km_to_miles(context):
    LOGGER.info("Step: verify distance unit popup title is KM -> Miles.")
    try:
        context.settings_page.verify_distance_unit_popup_km_to_miles()
        LOGGER.info("Step passed: distance unit popup KM -> Miles verified.")
    except Exception as exc:
        LOGGER.exception("Distance unit popup KM -> Miles verification failed: %s", exc)
        raise AssertionError(
            f"Distance unit popup was not verified as KM -> Miles. Error: {exc}"
        ) from exc


@when("the user verify that Miles display on the home screen")
@then("the user verify that Miles display on the home screen")
def step_verify_miles_display_on_home_screen(context):
    LOGGER.info("Step: verify Miles distance unit on home screen.")
    try:
        context.home_page.verify_miles_display_on_home_screen()
        LOGGER.info("Step passed: Miles distance unit verified on home screen.")
    except Exception as exc:
        LOGGER.exception("Home screen Miles verification failed: %s", exc)
        raise AssertionError(
            f"Miles was not verified on the home screen. Error: {exc}"
        ) from exc
