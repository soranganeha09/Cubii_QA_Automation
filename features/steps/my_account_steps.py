import logging

from behave import then, when

from features.environment import _mark_bootstrap_completed, reset_bootstrap_state


LOGGER = logging.getLogger("cubii_my_account_steps")


@then("the user verifies the More menu profile name")
def step_verify_more_menu_profile_name(context):
    LOGGER.info("Step: verifying More menu profile name (`textView22`).")
    try:
        context.home_page.verify_more_menu_profile_name()
        LOGGER.info("Step passed: More menu profile name verified.")
    except Exception as exc:
        LOGGER.exception("More menu profile name verification failed: %s", exc)
        raise AssertionError(
            f"More menu profile name verification failed. Error: {exc}"
        ) from exc


@then("the user verifies all the More menu options")
def step_verify_more_menu_options(context):
    LOGGER.info("Step: verifying all listed More menu options.")
    try:
        context.home_page.verify_more_menu_options()
        LOGGER.info("Step passed: all More menu options verified.")
    except Exception as exc:
        LOGGER.exception("More menu options verification failed: %s", exc)
        raise AssertionError(
            f"More menu options verification failed. Error: {exc}"
        ) from exc


@when("the user clicks on the three dot")
@then("the user clicks on the three dot")
def step_click_three_dot_menu(context):
    LOGGER.info("Step: clicking three-dot Settings menu on home screen.")
    try:
        context.home_page.tap_settings_highlight()
        LOGGER.info("Step passed: three-dot Settings menu opened.")
    except Exception as exc:
        LOGGER.exception("Clicking three-dot Settings menu failed: %s", exc)
        raise AssertionError(
            f"Unable to click three-dot Settings menu. Error: {exc}"
        ) from exc


@when("the user clicks on the my account")
@then("the user clicks on the my account")
def step_click_my_account(context):
    LOGGER.info("Step: clicking My Account from Settings menu.")
    try:
        context.home_page.tap_my_account_menu_item()
        LOGGER.info("Step passed: My Account screen opened.")
    except Exception as exc:
        LOGGER.exception("Clicking My Account menu item failed: %s", exc)
        raise AssertionError(
            f"Unable to click My Account menu item. Error: {exc}"
        ) from exc


@when("the user clicks on the Workout Reminder")
@then("the user clicks on the Workout Reminder")
def step_click_workout_reminder(context):
    LOGGER.info("Step: clicking Workout Reminder from Settings menu.")
    try:
        context.home_page.tap_workout_reminder_menu_item()
        LOGGER.info("Step passed: Workout Reminder screen opened.")
    except Exception as exc:
        LOGGER.exception("Clicking Workout Reminder menu item failed: %s", exc)
        raise AssertionError(
            f"Unable to click Workout Reminder menu item. Error: {exc}"
        ) from exc


@then("the user verifies the Workout Reminder screen")
def step_verify_workout_reminder_screen(context):
    LOGGER.info("Step: verifying Workout Reminder screen toolbar title.")
    try:
        context.workout_reminder_page.verify_workout_reminder_screen_visible()
        LOGGER.info("Step passed: Workout Reminder screen verified.")
    except Exception as exc:
        LOGGER.exception("Workout Reminder screen verification failed: %s", exc)
        raise AssertionError(
            f"Workout Reminder screen verification failed. Error: {exc}"
        ) from exc


@then("the user verifies the No Workout Reminder empty state if no reminder is set")
def step_verify_no_workout_reminder_empty_state_if_present(context):
    LOGGER.info(
        "Step: verify No Workout Reminders empty state if no reminder is configured."
    )
    try:
        context.workout_reminder_page.verify_no_workout_reminder_empty_state_if_present()
        LOGGER.info("Step passed: no-reminder empty state check completed.")
    except Exception as exc:
        LOGGER.exception("No Workout Reminder empty state verification failed: %s", exc)
        raise AssertionError(
            f"No Workout Reminder empty state verification failed. Error: {exc}"
        ) from exc


@when("the user click on the ADD REMINDER button")
@then("the user click on the ADD REMINDER button")
def step_click_add_reminder_button(context):
    LOGGER.info("Step: clicking ADD REMINDER button.")
    try:
        context.workout_reminder_page.tap_add_reminder_button()
        LOGGER.info("Step passed: ADD REMINDER button clicked.")
    except Exception as exc:
        LOGGER.exception("ADD REMINDER button click failed: %s", exc)
        raise AssertionError(
            f"Could not click ADD REMINDER button. Error: {exc}"
        ) from exc


@when("the user verify the Add Reminder screen")
@then("the user verify the Add Reminder screen")
def step_verify_add_reminder_screen(context):
    LOGGER.info("Step: verifying Add Reminder screen.")
    try:
        context.workout_reminder_page.verify_add_reminder_screen_visible()
        LOGGER.info("Step passed: Add Reminder screen verified.")
    except Exception as exc:
        LOGGER.exception("Add Reminder screen verification failed: %s", exc)
        raise AssertionError(
            f"Add Reminder screen verification failed. Error: {exc}"
        ) from exc


@when("the user set the reminder time for the workout")
@then("the user set the reminder time for the workout")
def step_set_workout_reminder_time(context):
    LOGGER.info("Step: set workout reminder time.")
    try:
        context.workout_reminder_page.set_workout_reminder_time()
        LOGGER.info("Step passed: workout reminder time controls verified.")
    except Exception as exc:
        LOGGER.exception("Workout reminder time setup failed: %s", exc)
        raise AssertionError(
            f"Workout reminder time setup failed. Error: {exc}"
        ) from exc


@when("the user set the reminder name")
@then("the user set the reminder name")
def step_set_workout_reminder_name(context):
    LOGGER.info("Step: set workout reminder name.")
    try:
        context.workout_reminder_page.set_workout_reminder_name()
        LOGGER.info("Step passed: workout reminder name set.")
    except Exception as exc:
        LOGGER.exception("Workout reminder name setup failed: %s", exc)
        raise AssertionError(
            f"Workout reminder name setup failed. Error: {exc}"
        ) from exc


@when("the user click on the reminder")
@then("the user click on the reminder")
def step_click_first_workout_reminder(context):
    LOGGER.info("Step: click first saved Workout Reminder.")
    try:
        context.workout_reminder_page.tap_first_workout_reminder()
        LOGGER.info("Step passed: first saved Workout Reminder opened.")
    except Exception as exc:
        LOGGER.exception("Opening first saved Workout Reminder failed: %s", exc)
        raise AssertionError(
            f"Opening first saved Workout Reminder failed. Error: {exc}"
        ) from exc


@when("the user edit the reminder time and select all the days and add the name")
@then("the user edit the reminder time and select all the days and add the name")
def step_edit_workout_reminder_time_days_name(context):
    LOGGER.info("Step: edit Workout Reminder time, all days, and name.")
    try:
        context.workout_reminder_page.edit_workout_reminder_time_days_and_name()
        LOGGER.info("Step passed: Workout Reminder edited.")
    except Exception as exc:
        LOGGER.exception("Editing Workout Reminder failed: %s", exc)
        raise AssertionError(
            f"Editing Workout Reminder failed. Error: {exc}"
        ) from exc


@when("the user sets the reminder for 1 minute ahead of the current time")
@then("the user sets the reminder for 1 minute ahead of the current time")
def step_set_workout_reminder_for_next_minute(context):
    LOGGER.info("Step: set workout reminder for 1 minute ahead.")
    try:
        context.workout_reminder_page.set_workout_reminder_for_next_minute()
        LOGGER.info("Step passed: workout reminder scheduled for upcoming minute.")
    except Exception as exc:
        LOGGER.exception("Workout reminder next-minute setup failed: %s", exc)
        raise AssertionError(
            f"Workout reminder next-minute setup failed. Error: {exc}"
        ) from exc


@when("the user click on the SAVE button")
@then("the user click on the SAVE button")
def step_click_save_reminder_button(context):
    LOGGER.info("Step: clicking SAVE reminder button.")
    try:
        context.workout_reminder_page.tap_save_reminder_button()
        LOGGER.info("Step passed: SAVE reminder button clicked.")
    except Exception as exc:
        LOGGER.exception("SAVE reminder button click failed: %s", exc)
        raise AssertionError(
            f"Could not click SAVE reminder button. Error: {exc}"
        ) from exc


@when("the user verify the reminder")
@then("the user verify the reminder")
def step_verify_saved_workout_reminder(context):
    LOGGER.info("Step: verifying saved Workout Reminder.")
    try:
        context.workout_reminder_page.verify_saved_workout_reminder()
        LOGGER.info("Step passed: saved Workout Reminder verified.")
    except Exception as exc:
        LOGGER.exception("Saved Workout Reminder verification failed: %s", exc)
        raise AssertionError(
            f"Saved Workout Reminder verification failed. Error: {exc}"
        ) from exc


@when("the user waits for the scheduled workout reminder notification")
@then("the user waits for the scheduled workout reminder notification")
def step_wait_for_scheduled_workout_reminder_notification(context):
    LOGGER.info("Step: wait for scheduled workout reminder notification.")
    try:
        context.workout_reminder_page.wait_for_scheduled_reminder_notification()
        LOGGER.info("Step passed: waited and opened notification shade.")
    except Exception as exc:
        LOGGER.exception("Waiting for workout reminder notification failed: %s", exc)
        raise AssertionError(
            f"Waiting for workout reminder notification failed. Error: {exc}"
        ) from exc


@when("the user verifies the workout reminder notification is displayed")
@then("the user verifies the workout reminder notification is displayed")
def step_verify_workout_reminder_notification_displayed(context):
    LOGGER.info("Step: verify workout reminder notification is displayed.")
    try:
        context.workout_reminder_page.verify_workout_reminder_notification_displayed()
        LOGGER.info("Step passed: workout reminder notification displayed.")
    except Exception as exc:
        LOGGER.exception("Workout reminder notification verification failed: %s", exc)
        raise AssertionError(
            f"Workout reminder notification verification failed. Error: {exc}"
        ) from exc


@when("the user close the notification panel")
@then("the user close the notification panel")
@when("the user close the notification paneel")
@then("the user close the notification paneel")
def step_close_notification_panel(context):
    LOGGER.info("Step: close Android notification panel.")
    try:
        context.workout_reminder_page.close_notification_panel()
        LOGGER.info("Step passed: Android notification panel closed.")
    except Exception as exc:
        LOGGER.exception("Closing Android notification panel failed: %s", exc)
        raise AssertionError(
            f"Closing Android notification panel failed. Error: {exc}"
        ) from exc


@when("the user click on the notification")
@then("the user click on the notification")
def step_click_workout_reminder_notification(context):
    LOGGER.info("Step: click workout reminder notification.")
    try:
        context.workout_reminder_page.tap_workout_reminder_notification()
        LOGGER.info("Step passed: workout reminder notification clicked.")
    except Exception as exc:
        LOGGER.exception("Clicking workout reminder notification failed: %s", exc)
        raise AssertionError(
            f"Clicking workout reminder notification failed. Error: {exc}"
        ) from exc


@when("the user toggle off the reminder")
@then("the user toggle off the reminder")
def step_toggle_off_workout_reminder(context):
    LOGGER.info("Step: toggle off Workout Reminder switch.")
    try:
        context.workout_reminder_page.toggle_workout_reminder_off()
        LOGGER.info("Step passed: Workout Reminder switch toggled off (or already off).")
    except Exception as exc:
        LOGGER.exception("Workout Reminder toggle-off failed: %s", exc)
        raise AssertionError(
            f"Workout Reminder toggle-off failed. Error: {exc}"
        ) from exc


@when("the user click on remove option")
@then("the user click on remove option")
def step_click_remove_reminder_option(context):
    LOGGER.info("Step: click REMOVE option on Workout Reminder.")
    try:
        context.workout_reminder_page.tap_remove_reminder_option()
        LOGGER.info("Step passed: REMOVE option clicked.")
    except Exception as exc:
        LOGGER.exception("REMOVE option click failed: %s", exc)
        raise AssertionError(
            f"Could not click REMOVE option. Error: {exc}"
        ) from exc


@when("the user select the reminder")
@then("the user select the reminder")
def step_select_reminder_for_removal(context):
    LOGGER.info("Step: selecting reminder for removal.")
    try:
        context.workout_reminder_page.select_reminder_for_removal()
        LOGGER.info("Step passed: reminder selected for removal.")
    except Exception as exc:
        LOGGER.exception("Selecting reminder for removal failed: %s", exc)
        raise AssertionError(
            f"Could not select reminder for removal. Error: {exc}"
        ) from exc


@when("click on the remove option")
@then("click on the remove option")
def step_click_remove_action_button(context):
    LOGGER.info("Step: clicking remove action button.")
    try:
        context.workout_reminder_page.click_remove_selected_reminder_button()
        LOGGER.info("Step passed: remove action button clicked.")
    except Exception as exc:
        LOGGER.exception("Remove action button click failed: %s", exc)
        raise AssertionError(
            f"Could not click remove action button. Error: {exc}"
        ) from exc


@when("the user click on the Workout Reminder cancel button")
@then("the user click on the Workout Reminder cancel button")
def step_click_workout_reminder_cancel_button(context):
    LOGGER.info("Step: click Workout Reminder cancel button.")
    try:
        context.workout_reminder_page.tap_workout_reminder_cancel_button()
        LOGGER.info("Step passed: Workout Reminder cancel button clicked.")
    except Exception as exc:
        LOGGER.exception("Workout Reminder cancel button click failed: %s", exc)
        raise AssertionError(
            f"Could not click Workout Reminder cancel button. Error: {exc}"
        ) from exc


@when("the user click on the back option")
@then("the user click on the back option")
def step_click_workout_reminder_back_option(context):
    LOGGER.info("Step: click Workout Reminder back option (Navigate up).")
    try:
        context.workout_reminder_page.tap_workout_reminder_cancel_button()
        LOGGER.info("Step passed: Workout Reminder back option clicked.")
    except Exception as exc:
        LOGGER.exception("Workout Reminder back option click failed: %s", exc)
        raise AssertionError(
            f"Could not click Workout Reminder back option. Error: {exc}"
        ) from exc


@when("the user click on the more back option")
@then("the user click on the more back option")
def step_click_more_back_option(context):
    LOGGER.info("Step: click More back option (`iv_back`).")
    try:
        context.workout_reminder_page.tap_more_back_option()
        LOGGER.info("Step passed: More back option clicked.")
    except Exception as exc:
        LOGGER.exception("More back option click failed: %s", exc)
        raise AssertionError(
            f"Could not click More back option. Error: {exc}"
        ) from exc


@then("the user handles the Set Reminder Permission pop-up if present")
def step_handle_set_reminder_permission_popup_if_present(context):
    LOGGER.info(
        "Step: handle Set Reminder Permission pop-up if present "
        "(TURN ON, Cubii app, alarms and reminders toggle, both back buttons)."
    )
    try:
        handled = context.workout_reminder_page.handle_set_reminder_permission_popup_if_present()
        if handled:
            LOGGER.info("Step passed: full Set Reminder Permission flow completed.")
        else:
            LOGGER.info("Step passed: Set Reminder Permission pop-up was not shown.")
    except Exception as exc:
        LOGGER.exception("Set Reminder Permission pop-up handling failed: %s", exc)
        raise AssertionError(
            f"Set Reminder Permission pop-up handling failed. Error: {exc}"
        ) from exc


@when("the user clicks on the preview")
@then("the user clicks on the preview")
def step_click_preview_profile(context):
    LOGGER.info("Step: clicking PREVIEW on My Account screen.")
    try:
        context.home_page.tap_preview_profile_button()
        LOGGER.info("Step passed: PREVIEW button clicked.")
    except Exception as exc:
        LOGGER.exception("Clicking PREVIEW button failed: %s", exc)
        raise AssertionError(
            f"Unable to click PREVIEW button on My Account screen. Error: {exc}"
        ) from exc


@then("the user verifies the Preview profile screen")
def step_verify_preview_profile_screen(context):
    LOGGER.info("Step: verifying Preview Profile screen toolbar title.")
    try:
        context.preview_profile_page.verify_preview_profile_screen_visible()
        LOGGER.info("Step passed: Preview Profile screen verified.")
    except Exception as exc:
        LOGGER.exception("Preview Profile screen verification failed: %s", exc)
        raise AssertionError(
            f"Preview Profile screen verification failed. Error: {exc}"
        ) from exc


@then("the user verifies all the preview profile details")
def step_verify_preview_profile_details(context):
    LOGGER.info(
        "Step: verifying Preview Profile details (name, Bio, Focus, Interests, Badges if present)."
    )
    try:
        context.preview_profile_page.verify_preview_profile_details()
        LOGGER.info("Step passed: Preview Profile details verified.")
    except Exception as exc:
        LOGGER.exception("Preview Profile details verification failed: %s", exc)
        raise AssertionError(
            f"Preview Profile details verification failed. Error: {exc}"
        ) from exc


def _tap_iv_back(context, screen_label: str) -> None:
    LOGGER.info("Step: tapping back (`iv_back`) on %s.", screen_label)
    try:
        context.home_page.tap_back_button()
        LOGGER.info("Step passed: back tapped on %s.", screen_label)
    except Exception as exc:
        LOGGER.exception("Back tap on %s failed: %s", screen_label, exc)
        raise AssertionError(
            f"Unable to tap back button on {screen_label}. Error: {exc}"
        ) from exc


@when("the user clicks on the back option on preview profile")
@then("the user clicks on the back option on preview profile")
def step_click_back_on_preview_profile(context):
    _tap_iv_back(context, "Preview Profile screen")


@when("the user clicks on the back button of my account")
@then("the user clicks on the back button of my account")
def step_click_back_on_my_account(context):
    _tap_iv_back(context, "My Account screen")


@when("the user clicks on the back button of the more screen")
@then("the user clicks on the back button of the more screen")
def step_click_back_on_more_screen(context):
    _tap_iv_back(context, "More screen")


@when("the user clicks on the EDIT PROFILE")
@then("the user clicks on the EDIT PROFILE")
def step_click_edit_profile(context):
    LOGGER.info("Step: clicking EDIT PROFILE from Settings menu.")
    try:
        context.home_page.tap_edit_profile_menu_item()
        LOGGER.info("Step passed: EDIT PROFILE button clicked.")
    except Exception as exc:
        LOGGER.exception("Clicking EDIT PROFILE menu item failed: %s", exc)
        raise AssertionError(
            f"Unable to click EDIT PROFILE menu item. Error: {exc}"
        ) from exc


@then("the user verify the Edit profile screen")
@then("the user verifies the Edit profile screen")
def step_verify_edit_profile_screen(context):
    LOGGER.info("Step: verifying Edit Profile screen toolbar title.")
    try:
        context.home_page.verify_edit_profile_screen_visible()
        LOGGER.info("Step passed: Edit Profile screen verified.")
    except Exception as exc:
        LOGGER.exception("Edit Profile screen verification failed: %s", exc)
        raise AssertionError(
            f"Edit Profile screen verification failed. Error: {exc}"
        ) from exc


def _edit_profile_payload(context):
    payload = getattr(context, "edit_profile_payload", None)
    if payload is None:
        payload = context.edit_profile_page.generate_edit_profile_data()
        context.edit_profile_payload = payload
    return payload


def _verify_edit_profile_field_error(context, field_key):
    LOGGER.info("Step: verifying Edit Profile error message for %s.", field_key)
    try:
        context.edit_profile_page.verify_field_error_message(field_key)
        LOGGER.info("Step passed: %s error message verified.", field_key)
    except Exception as exc:
        LOGGER.exception("Edit Profile %s error verification failed: %s", field_key, exc)
        raise AssertionError(
            f"Edit Profile {field_key} error message verification failed. Error: {exc}"
        ) from exc


def _verify_change_password_field_error(context, field_key):
    LOGGER.info("Step: verifying Change Password error message for %s.", field_key)
    try:
        context.edit_profile_page.verify_change_password_field_error_message(field_key)
        LOGGER.info("Step passed: Change Password %s error message verified.", field_key)
    except Exception as exc:
        LOGGER.exception(
            "Change Password %s error verification failed: %s", field_key, exc
        )
        raise AssertionError(
            f"Change Password {field_key} error message verification failed. "
            f"Error: {exc}"
        ) from exc


@when("the user removes the first name")
@then("the user removes the first name")
def step_remove_first_name(context):
    LOGGER.info("Step: removing first name on Edit Profile screen.")
    try:
        context.edit_profile_page.clear_first_name()
        LOGGER.info("Step passed: first name cleared.")
    except Exception as exc:
        LOGGER.exception("Removing first name failed: %s", exc)
        raise AssertionError(f"Unable to remove first name. Error: {exc}") from exc


@when("the user removes the last name")
@then("the user removes the last name")
def step_remove_last_name(context):
    LOGGER.info("Step: removing last name on Edit Profile screen.")
    try:
        context.edit_profile_page.clear_last_name()
        LOGGER.info("Step passed: last name cleared.")
    except Exception as exc:
        LOGGER.exception("Removing last name failed: %s", exc)
        raise AssertionError(f"Unable to remove last name. Error: {exc}") from exc


@when("the user removes the email")
@then("the user removes the email")
def step_remove_email(context):
    LOGGER.info("Step: removing email on Edit Profile screen.")
    try:
        context.edit_profile_page.clear_email()
        LOGGER.info("Step passed: email cleared.")
    except Exception as exc:
        LOGGER.exception("Removing email failed: %s", exc)
        raise AssertionError(f"Unable to remove email. Error: {exc}") from exc


@when("the user scrolls up")
@then("the user scrolls up")
def step_scroll_up_edit_profile(context):
    LOGGER.info("Step: scrolling up on Edit Profile screen.")
    try:
        context.edit_profile_page.scroll_up()
        LOGGER.info("Step passed: Edit Profile screen scrolled up.")
    except Exception as exc:
        LOGGER.exception("Scrolling up on Edit Profile failed: %s", exc)
        raise AssertionError(f"Unable to scroll up on Edit Profile. Error: {exc}") from exc


@when("the user verifies the error message for first name")
@then("the user verifies the error message for first name")
def step_verify_edit_profile_first_name_error(context):
    _verify_edit_profile_field_error(context, "first name")


@when("the user verifies the error message for last name")
@then("the user verifies the error message for last name")
def step_verify_edit_profile_last_name_error(context):
    _verify_edit_profile_field_error(context, "last name")


@when("the user adds the first name")
@then("the user adds the first name")
def step_add_first_name(context):
    LOGGER.info("Step: adding first name on Edit Profile screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.edit_first_name(payload["first_name"])
        LOGGER.info("Step passed: first name set to %s.", payload["first_name"])
    except Exception as exc:
        LOGGER.exception("Adding first name failed: %s", exc)
        raise AssertionError(f"Unable to add first name. Error: {exc}") from exc


@when("the user adds the last name")
@then("the user adds the last name")
def step_add_last_name(context):
    LOGGER.info("Step: adding last name on Edit Profile screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.edit_last_name(payload["last_name"])
        LOGGER.info("Step passed: last name set to %s.", payload["last_name"])
    except Exception as exc:
        LOGGER.exception("Adding last name failed: %s", exc)
        raise AssertionError(f"Unable to add last name. Error: {exc}") from exc


@when("the user adds an invalid email")
@then("the user adds an invalid email")
def step_add_invalid_email(context):
    LOGGER.info("Step: adding invalid email on Edit Profile screen.")
    try:
        context.edit_profile_page.enter_invalid_email()
        LOGGER.info("Step passed: invalid email entered.")
    except Exception as exc:
        LOGGER.exception("Adding invalid email failed: %s", exc)
        raise AssertionError(f"Unable to add invalid email. Error: {exc}") from exc


@when("the user verifies the email error message")
@then("the user verifies the email error message")
def step_verify_edit_profile_email_error(context):
    _verify_edit_profile_field_error(context, "valid email")


@when("the user adds the valid email")
@then("the user adds the valid email")
def step_add_valid_email(context):
    LOGGER.info("Step: adding valid email on Edit Profile screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.edit_email(payload["email"])
        LOGGER.info("Step passed: valid email set to %s.", payload["email"])
    except Exception as exc:
        LOGGER.exception("Adding valid email failed: %s", exc)
        raise AssertionError(f"Unable to add valid email. Error: {exc}") from exc


@when("the user clicks on Change Password")
@then("the user clicks on Change Password")
def step_click_change_password(context):
    LOGGER.info("Step: opening Change Password from Edit Profile.")
    try:
        context.edit_profile_page.click_change_password()
        LOGGER.info("Step passed: Change Password screen opened.")
    except Exception as exc:
        LOGGER.exception("Opening Change Password failed: %s", exc)
        raise AssertionError(f"Unable to open Change Password. Error: {exc}") from exc


@when("the user enters the old password on change password screen")
@then("the user enters the old password on change password screen")
def step_enter_change_password_old(context):
    LOGGER.info("Step: entering old password on Change Password screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.enter_change_password_old(payload["change_password_old"])
        LOGGER.info("Step passed: old password entered.")
    except Exception as exc:
        LOGGER.exception("Entering old password failed: %s", exc)
        raise AssertionError(f"Unable to enter old password. Error: {exc}") from exc


@when("the user enters the new password on change password screen")
@then("the user enters the new password on change password screen")
def step_enter_change_password_new(context):
    LOGGER.info("Step: entering new password on Change Password screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.enter_change_password_new(payload["change_password_new"])
        LOGGER.info("Step passed: new password entered.")
    except Exception as exc:
        LOGGER.exception("Entering new password failed: %s", exc)
        raise AssertionError(f"Unable to enter new password. Error: {exc}") from exc


@when("the user enters the repeat new password on change password screen")
@then("the user enters the repeat new password on change password screen")
def step_enter_change_password_repeat(context):
    LOGGER.info("Step: entering repeat new password on Change Password screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.enter_change_password_repeat(payload["change_password_new"])
        LOGGER.info("Step passed: repeat new password entered.")
    except Exception as exc:
        LOGGER.exception("Entering repeat new password failed: %s", exc)
        raise AssertionError(f"Unable to enter repeat new password. Error: {exc}") from exc


@when("the user verifies the error message of the old password on change password screen")
@then("the user verifies the error message of the old password on change password screen")
def step_verify_change_password_old_error(context):
    _verify_change_password_field_error(context, "old password")


@when("the user verifies the new password error message on change password screen")
@then("the user verifies the new password error message on change password screen")
def step_verify_change_password_new_error(context):
    _verify_change_password_field_error(context, "new password")


@when("the user verifies the repeat new password error message on change password screen")
@then("the user verifies the repeat new password error message on change password screen")
def step_verify_change_password_repeat_error(context):
    _verify_change_password_field_error(context, "repeat new password")


@when("the user adds the OLD password on change password screen")
@then("the user adds the OLD password on change password screen")
def step_add_change_password_old(context):
    LOGGER.info("Step: adding OLD password on Change Password screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.enter_change_password_old(payload["change_password_old"])
        LOGGER.info("Step passed: OLD password entered.")
    except Exception as exc:
        LOGGER.exception("Adding OLD password failed: %s", exc)
        raise AssertionError(f"Unable to add OLD password. Error: {exc}") from exc


@when("the user adds the new password on change password screen")
@then("the user adds the new password on change password screen")
def step_add_change_password_new(context):
    LOGGER.info("Step: adding new password on Change Password screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.enter_change_password_new(payload["change_password_new"])
        LOGGER.info("Step passed: new password entered.")
    except Exception as exc:
        LOGGER.exception("Adding new password failed: %s", exc)
        raise AssertionError(f"Unable to add new password. Error: {exc}") from exc


@when("the user verifies the error message of the Repeat New Password on change password screen")
@then("the user verifies the error message of the Repeat New Password on change password screen")
def step_verify_change_password_repeat_mismatch_error(context):
    _verify_change_password_field_error(context, "repeat password mismatch")


@when("the user adds the Repeat New Password on change password screen")
@then("the user adds the Repeat New Password on change password screen")
def step_add_change_password_repeat_matching(context):
    LOGGER.info("Step: adding matching Repeat New Password on Change Password screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.enter_change_password_repeat(
            payload["change_password_new"]
        )
        LOGGER.info(
            "Step passed: Repeat New Password entered (matches new password)."
        )
    except Exception as exc:
        LOGGER.exception("Adding Repeat New Password failed: %s", exc)
        raise AssertionError(
            f"Unable to add Repeat New Password. Error: {exc}"
        ) from exc


@when("the user adds the wrong password on change password screen")
@then("the user adds the wrong password on change password screen")
def step_add_change_password_wrong_repeat(context):
    LOGGER.info("Step: adding mismatched repeat password on Change Password screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.enter_change_password_repeat(
            payload["change_password_wrong_repeat"]
        )
        LOGGER.info(
            "Step passed: wrong repeat password entered (does not match new password)."
        )
    except Exception as exc:
        LOGGER.exception("Adding wrong repeat password failed: %s", exc)
        raise AssertionError(
            f"Unable to add wrong repeat password. Error: {exc}"
        ) from exc


@when("the user clicks on the save password button")
@then("the user clicks on the save password button")
def step_click_save_password_button(context):
    LOGGER.info("Step: saving Change Password.")
    try:
        context.edit_profile_page.click_save_password_button()
        LOGGER.info("Step passed: Change Password saved.")
    except Exception as exc:
        LOGGER.exception("Saving Change Password failed: %s", exc)
        raise AssertionError(f"Unable to save Change Password. Error: {exc}") from exc


@when("the user logs in with the updated edit profile email and new password")
@then("the user logs in with the updated edit profile email and new password")
def step_login_with_updated_email_and_new_password(context):
    LOGGER.info(
        "Step: logging in with updated Edit Profile email and new password."
    )
    try:
        payload = _edit_profile_payload(context)
        context.login_page.login_with_credentials(
            payload["email"],
            payload["change_password_new"],
        )
        assert context.login_page.is_logged_in(), (
            "User was not logged in after signing in with updated email and new password."
        )
        context.ftue_page.complete_ftue_if_present()
        _mark_bootstrap_completed(context)
        LOGGER.info(
            "Step passed: logged in with %s and new password.",
            payload["email"],
        )
    except Exception as exc:
        LOGGER.exception(
            "Login with updated email and new password failed: %s", exc
        )
        raise AssertionError(
            "Unable to log in with updated edit profile email and new password. "
            f"Error: {exc}"
        ) from exc


@when("the user edits the first name")
@then("the user edits the first name")
def step_edit_first_name(context):
    LOGGER.info("Step: editing first name on Edit Profile screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.edit_first_name(payload["first_name"])
        LOGGER.info("Step passed: first name updated to %s.", payload["first_name"])
    except Exception as exc:
        LOGGER.exception("Editing first name failed: %s", exc)
        raise AssertionError(f"Unable to edit first name. Error: {exc}") from exc


@when("the user edits the last name")
@then("the user edits the last name")
def step_edit_last_name(context):
    LOGGER.info("Step: editing last name on Edit Profile screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.edit_last_name(payload["last_name"])
        LOGGER.info("Step passed: last name updated to %s.", payload["last_name"])
    except Exception as exc:
        LOGGER.exception("Editing last name failed: %s", exc)
        raise AssertionError(f"Unable to edit last name. Error: {exc}") from exc


@when("the user edits the email")
@then("the user edits the email")
def step_edit_email(context):
    LOGGER.info("Step: editing email on Edit Profile screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.edit_email(payload["email"])
        LOGGER.info("Step passed: email updated to %s.", payload["email"])
    except Exception as exc:
        LOGGER.exception("Editing email failed: %s", exc)
        raise AssertionError(f"Unable to edit email. Error: {exc}") from exc


@when("the user edits the birthdate")
@then("the user edits the birthdate")
def step_edit_birthdate(context):
    LOGGER.info("Step: selecting random birthdate on Edit Profile screen.")
    try:
        context.edit_profile_page.select_random_birthdate_and_confirm()
        LOGGER.info("Step passed: birthdate updated with random date.")
    except Exception as exc:
        LOGGER.exception("Editing birthdate failed: %s", exc)
        raise AssertionError(f"Unable to edit birthdate. Error: {exc}") from exc


@when("the user selects a random gender")
@then("the user selects a random gender")
def step_select_random_gender(context):
    LOGGER.info("Step: selecting random gender on Edit Profile screen.")
    try:
        payload = _edit_profile_payload(context)
        chosen = context.edit_profile_page.select_random_gender()
        payload["gender"] = chosen
        LOGGER.info("Step passed: gender selected as %s.", chosen)
    except Exception as exc:
        LOGGER.exception("Selecting random gender failed: %s", exc)
        raise AssertionError(f"Unable to select random gender. Error: {exc}") from exc


@when("the user clicks on the Height")
@then("the user clicks on the Height")
def step_click_height(context):
    LOGGER.info("Step: clicking Height field on Edit Profile screen.")
    try:
        context.edit_profile_page.click_height_field()
        LOGGER.info("Step passed: Height picker opened.")
    except Exception as exc:
        LOGGER.exception("Clicking Height field failed: %s", exc)
        raise AssertionError(f"Unable to click Height field. Error: {exc}") from exc


@when("the user selects a random height")
@then("the user selects a random height")
def step_select_random_height(context):
    LOGGER.info("Step: selecting random height on Edit Profile screen.")
    try:
        context.edit_profile_page.select_random_height_and_confirm()
        LOGGER.info("Step passed: random height selected and confirmed.")
    except Exception as exc:
        LOGGER.exception("Selecting random height failed: %s", exc)
        raise AssertionError(f"Unable to select random height. Error: {exc}") from exc


@when("the user clicks on the Weight")
@then("the user clicks on the Weight")
def step_click_weight(context):
    LOGGER.info("Step: clicking Weight field on Edit Profile screen.")
    try:
        context.edit_profile_page.click_weight_field()
        LOGGER.info("Step passed: Weight picker opened.")
    except Exception as exc:
        LOGGER.exception("Clicking Weight field failed: %s", exc)
        raise AssertionError(f"Unable to click Weight field. Error: {exc}") from exc


@when("the user selects a random weight")
@then("the user selects a random weight")
def step_select_random_weight(context):
    LOGGER.info("Step: selecting random weight on Edit Profile screen.")
    try:
        context.edit_profile_page.select_random_weight_and_confirm()
        LOGGER.info("Step passed: random weight selected and confirmed.")
    except Exception as exc:
        LOGGER.exception("Selecting random weight failed: %s", exc)
        raise AssertionError(f"Unable to select random weight. Error: {exc}") from exc


@when("the user clicks on the Country")
@then("the user clicks on the Country")
def step_click_country(context):
    LOGGER.info("Step: clicking Country field on Edit Profile screen.")
    try:
        context.edit_profile_page.click_country_field()
        LOGGER.info("Step passed: Choose Country list opened.")
    except Exception as exc:
        LOGGER.exception("Clicking Country field failed: %s", exc)
        raise AssertionError(f"Unable to click Country field. Error: {exc}") from exc


@when("the user selects a random country")
@then("the user selects a random country")
def step_select_random_country(context):
    LOGGER.info("Step: selecting random country on Edit Profile screen.")
    try:
        chosen = context.edit_profile_page.select_random_country()
        LOGGER.info("Step passed: country selected as %s.", chosen)
    except Exception as exc:
        LOGGER.exception("Selecting random country failed: %s", exc)
        raise AssertionError(f"Unable to select random country. Error: {exc}") from exc


@when("the user selects a random state if available")
@then("the user selects a random state if available")
def step_select_random_state_if_available(context):
    LOGGER.info("Step: selecting random state on Edit Profile screen (if available).")
    try:
        chosen = context.edit_profile_page.select_random_state_if_available()
        if chosen:
            LOGGER.info("Step passed: state selected as %s.", chosen)
        else:
            LOGGER.info("Step passed: state field not shown; skipped.")
    except Exception as exc:
        LOGGER.exception("Selecting random state failed: %s", exc)
        raise AssertionError(f"Unable to select random state. Error: {exc}") from exc


@when("the user selects a random city if available")
@then("the user selects a random city if available")
def step_select_random_city_if_available(context):
    LOGGER.info("Step: selecting random city on Edit Profile screen (if available).")
    try:
        chosen = context.edit_profile_page.select_random_city_if_available()
        if chosen:
            LOGGER.info("Step passed: city selected as %s.", chosen)
        else:
            LOGGER.info("Step passed: city field not shown; skipped.")
    except Exception as exc:
        LOGGER.exception("Selecting random city failed: %s", exc)
        raise AssertionError(f"Unable to select random city. Error: {exc}") from exc


@when("the user scrolls down")
@then("the user scrolls down")
def step_scroll_down_edit_profile(context):
    LOGGER.info("Step: scrolling down on Edit Profile screen.")
    try:
        context.edit_profile_page.scroll_down()
        LOGGER.info("Step passed: Edit Profile screen scrolled down.")
    except Exception as exc:
        LOGGER.exception("Scrolling down on Edit Profile failed: %s", exc)
        raise AssertionError(f"Unable to scroll down on Edit Profile. Error: {exc}") from exc


@when("the user adds the zip code")
@then("the user adds the zip code")
def step_add_zip_code(context):
    LOGGER.info("Step: adding zip code on Edit Profile screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.enter_zip_code(payload["zip_code"])
        LOGGER.info("Step passed: zip code updated to %s.", payload["zip_code"])
    except Exception as exc:
        LOGGER.exception("Adding zip code failed: %s", exc)
        raise AssertionError(f"Unable to add zip code. Error: {exc}") from exc


@when("the user adds a random company name")
@then("the user adds a random company name")
def step_add_random_company(context):
    LOGGER.info("Step: adding random company name on Edit Profile screen.")
    try:
        payload = _edit_profile_payload(context)
        context.edit_profile_page.enter_company(payload["company"])
        LOGGER.info("Step passed: company updated to %s.", payload["company"])
    except Exception as exc:
        LOGGER.exception("Adding company name failed: %s", exc)
        raise AssertionError(f"Unable to add company name. Error: {exc}") from exc


@when("the user clicks on the save button")
@then("the user clicks on the save button")
def step_click_save_button(context):
    LOGGER.info("Step: clicking Save on Edit Profile screen.")
    try:
        context.edit_profile_page.click_save_button()
        LOGGER.info("Step passed: Edit Profile saved.")
    except Exception as exc:
        LOGGER.exception("Clicking Save on Edit Profile failed: %s", exc)
        raise AssertionError(f"Unable to click Save on Edit Profile. Error: {exc}") from exc


@when("the user clicks on the back button")
@then("the user clicks on the back button")
def step_click_back_button(context):
    LOGGER.info("Step: navigating back to More menu from Edit Profile flow.")
    try:
        context.home_page.navigate_back_to_more_menu()
        LOGGER.info("Step passed: More menu is visible.")
    except Exception as exc:
        LOGGER.exception("Navigating back to More menu failed: %s", exc)
        raise AssertionError(f"Unable to navigate back to More menu. Error: {exc}") from exc


@when("the user clicks on the logout option")
@then("the user clicks on the logout option")
def step_click_logout_option(context):
    LOGGER.info("Step: clicking Logout in More menu.")
    try:
        context.home_page.tap_logout_menu_item()
        LOGGER.info("Step passed: Logout option tapped.")
    except Exception as exc:
        LOGGER.exception("Clicking Logout option failed: %s", exc)
        raise AssertionError(f"Unable to click Logout option. Error: {exc}") from exc


@when("the user confirms logout from the pop-up")
@then("the user confirms logout from the pop-up")
def step_confirm_logout_popup(context):
    LOGGER.info("Step: confirming Logout in pop-up.")
    try:
        context.home_page.tap_logout_confirm()
        reset_bootstrap_state(context)
        context.login_page.wait_for_login_screen()
        LOGGER.info("Step passed: user signed out and login screen is visible.")
    except Exception as exc:
        LOGGER.exception("Confirming Logout failed: %s", exc)
        raise AssertionError(f"Unable to confirm Logout. Error: {exc}") from exc


@when("the user logs in with the updated edit profile credentials")
@then("the user logs in with the updated edit profile credentials")
def step_login_with_updated_edit_profile_credentials(context):
    LOGGER.info("Step: logging in with updated Edit Profile email and current password.")
    try:
        payload = _edit_profile_payload(context)
        context.login_page.login_with_credentials(
            payload["email"],
            context.login_page.PASSWORD,
        )
        assert context.login_page.is_logged_in(), (
            "User was not logged in after signing in with updated email."
        )
        context.ftue_page.complete_ftue_if_present()
        _mark_bootstrap_completed(context)
        LOGGER.info(
            "Step passed: logged in with updated email %s.", payload["email"]
        )
    except Exception as exc:
        LOGGER.exception("Login with updated edit profile credentials failed: %s", exc)
        raise AssertionError(
            f"Unable to log in with updated edit profile credentials. Error: {exc}"
        ) from exc
