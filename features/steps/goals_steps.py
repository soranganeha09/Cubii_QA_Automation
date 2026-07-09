import logging

from behave import then, when

LOGGER = logging.getLogger("cubii_goals_steps")


@when("the user scrolls down to Today's Goals on the home screen")
@then("the user scrolls down to Today's Goals on the home screen")
def step_scroll_to_todays_goals(context):
    LOGGER.info("Step: scroll home screen to Today's Goals section.")
    try:
        context.goals_page.scroll_to_todays_goals_section()
        LOGGER.info("Step passed: Today's Goals section is in view.")
    except Exception as exc:
        LOGGER.exception("Scroll to Today's Goals failed: %s", exc)
        raise AssertionError(
            f"Could not scroll to Today's Goals on the home screen. Error: {exc}"
        ) from exc


@then("Today's Goals section should be visible on the home screen")
def step_verify_todays_goals_visible(context):
    LOGGER.info("Step: verify Today's Goals section is visible.")
    try:
        context.goals_page.verify_todays_goals_section_visible()
        LOGGER.info("Step passed: Today's Goals section verified.")
    except Exception as exc:
        LOGGER.exception("Today's Goals visibility check failed: %s", exc)
        raise AssertionError(
            f"Today's Goals section is not visible on the home screen. Error: {exc}"
        ) from exc


@when("the user scrolls down and taps the add goal button")
@then("the user scrolls down and taps the add goal button")
@when("the user taps the add goal button")
@then("the user taps the add goal button")
def step_tap_add_goal_button(context):
    LOGGER.info("Step: scroll down and tap add goal button (`btnAdd`).")
    try:
        context.goals_page.tap_add_goal_button()
        LOGGER.info("Step passed: add goal button tapped.")
    except Exception as exc:
        LOGGER.exception("Add goal button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the add goal button (`btnAdd`). Error: {exc}"
        ) from exc


@when("the user scrolls down and taps the edit goal button")
@then("the user scrolls down and taps the edit goal button")
@when("the user taps the edit goal button")
@then("the user taps the edit goal button")
def step_tap_edit_goal_button(context):
    LOGGER.info("Step: scroll down and tap edit goal button (`btn_edit`).")
    try:
        context.goals_page.tap_edit_goal_button()
        LOGGER.info("Step passed: edit goal button tapped.")
    except Exception as exc:
        LOGGER.exception("Edit goal button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the edit goal button (`btn_edit`). Error: {exc}"
        ) from exc


@when("the user taps Next on the goal introduction")
@then("the user taps Next on the goal introduction")
def step_tap_goal_ftue_next(context):
    LOGGER.info("Step: tap Next on goal introduction (`btnNext`).")
    try:
        context.goals_page.tap_goal_ftue_next_button()
        LOGGER.info("Step passed: goal FTUE Next tapped.")
    except Exception as exc:
        LOGGER.exception("Goal FTUE Next tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Next on the goal introduction (`btnNext`). Error: {exc}"
        ) from exc


@when("the user taps Next on the goal introduction if present")
@then("the user taps Next on the goal introduction if present")
def step_tap_goal_ftue_next_if_present(context):
    LOGGER.info("Step: tap Next on goal introduction (`btnNext`) if present.")
    try:
        tapped = context.goals_page.tap_goal_ftue_next_button_if_present()
        if tapped:
            LOGGER.info("Step passed: goal FTUE Next tapped.")
        else:
            LOGGER.info("Step passed: goal FTUE Next not shown; skipped.")
    except Exception as exc:
        LOGGER.exception("Goal FTUE Next optional tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Next on the goal introduction when shown (`btnNext`). "
            f"Error: {exc}"
        ) from exc


@when("the user taps Got it on the goal introduction")
@then("the user taps Got it on the goal introduction")
def step_tap_goal_ftue_got_it(context):
    LOGGER.info("Step: tap Got it on goal introduction (`btnGotIt1`).")
    try:
        context.goals_page.tap_goal_ftue_got_it_button()
        LOGGER.info("Step passed: goal FTUE Got it tapped.")
    except Exception as exc:
        LOGGER.exception("Goal FTUE Got it tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Got it on the goal introduction (`btnGotIt1`). Error: {exc}"
        ) from exc


@when("the user taps Got it on the goal introduction if present")
@then("the user taps Got it on the goal introduction if present")
def step_tap_goal_ftue_got_it_if_present(context):
    LOGGER.info("Step: tap Got it on goal introduction (`btnGotIt1`) if present.")
    try:
        tapped = context.goals_page.tap_goal_ftue_got_it_button_if_present()
        if tapped:
            LOGGER.info("Step passed: goal FTUE Got it tapped.")
        else:
            LOGGER.info("Step passed: goal FTUE Got it not shown; skipped.")
    except Exception as exc:
        LOGGER.exception("Goal FTUE Got it optional tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Got it on the goal introduction when shown (`btnGotIt1`). "
            f"Error: {exc}"
        ) from exc


@then("the goal introduction should be dismissed")
def step_verify_goal_introduction_dismissed(context):
    LOGGER.info("Step: verify goal introduction overlay is dismissed.")
    try:
        context.goals_page.verify_goal_introduction_dismissed()
        LOGGER.info("Step passed: goal introduction dismissed.")
    except Exception as exc:
        LOGGER.exception("Goal introduction dismissal check failed: %s", exc)
        raise AssertionError(
            f"Goal introduction overlay was not dismissed. Error: {exc}"
        ) from exc


@then("the goal introduction should be dismissed if present")
def step_verify_goal_introduction_dismissed_if_present(context):
    LOGGER.info("Step: verify goal introduction dismissed if `btnGotIt1` was shown.")
    try:
        checked = context.goals_page.verify_goal_introduction_dismissed_if_present()
        if checked:
            LOGGER.info("Step passed: goal introduction was present and is now dismissed.")
        else:
            LOGGER.info("Step passed: goal introduction was not shown; check skipped.")
    except Exception as exc:
        LOGGER.exception("Goal introduction optional dismissal check failed: %s", exc)
        raise AssertionError(
            f"Goal introduction overlay (`btnGotIt1`) was still visible. Error: {exc}"
        ) from exc


@then("the user verify the goal metrics Strides Calories Miles and Time")
def step_verify_goal_metrics(context):
    LOGGER.info(
        "Step: verify goal metrics Strides, Calories, Miles, and Time on add goal screen."
    )
    try:
        context.goals_page.verify_goal_metrics()
        LOGGER.info("Step passed: all goal metrics verified.")
    except Exception as exc:
        LOGGER.exception("Goal metrics verification failed: %s", exc)
        raise AssertionError(
            f"Goal metrics Strides, Calories, Miles, and Time were not all visible. "
            f"Error: {exc}"
        ) from exc


@when("the user click on Strides")
@then("the user click on Strides")
def step_click_strides_goal_metric(context):
    LOGGER.info("Step: tap Strides goal metric on add goal screen.")
    try:
        context.goals_page.tap_strides_goal_metric()
        LOGGER.info("Step passed: Strides goal metric tapped.")
    except Exception as exc:
        LOGGER.exception("Strides goal metric tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Strides goal metric. Error: {exc}"
        ) from exc


@then("the user verify the details of Strides")
def step_verify_strides_goal_details(context):
    LOGGER.info(
        "Step: verify Strides goal details (card, title, value, days label)."
    )
    try:
        context.goals_page.verify_strides_goal_details()
        LOGGER.info("Step passed: Strides goal details verified.")
    except Exception as exc:
        LOGGER.exception("Strides goal details verification failed: %s", exc)
        raise AssertionError(
            f"Strides goal details verification failed. Error: {exc}"
        ) from exc


@then("the user add the strides goals 100")
@when("the user add the strides goals 100")
def step_add_strides_goal_100(context):
    LOGGER.info("Step: enter Strides goal value 100 in `goalValue`.")
    try:
        context.goals_page.enter_strides_goal_value("100")
        LOGGER.info("Step passed: Strides goal value 100 entered.")
    except Exception as exc:
        LOGGER.exception("Enter Strides goal value failed: %s", exc)
        raise AssertionError(
            f"Could not add Strides goal value 100. Error: {exc}"
        ) from exc


@then("the user add the strides goals 0")
@when("the user add the strides goals 0")
def step_add_strides_goal_0(context):
    LOGGER.info("Step: enter Strides goal value 0 in `goalValue`.")
    try:
        context.goals_page.enter_strides_goal_value("0")
        LOGGER.info("Step passed: Strides goal value 0 entered.")
    except Exception as exc:
        LOGGER.exception("Enter Strides goal value 0 failed: %s", exc)
        raise AssertionError(
            f"Could not add Strides goal value 0. Error: {exc}"
        ) from exc


@when("the user click on Calories")
@then("the user click on Calories")
def step_click_calories_goal_metric(context):
    LOGGER.info("Step: tap Calories goal metric on add goal screen.")
    try:
        context.goals_page.tap_calories_goal_metric()
        LOGGER.info("Step passed: Calories goal metric tapped.")
    except Exception as exc:
        LOGGER.exception("Calories goal metric tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Calories goal metric. Error: {exc}"
        ) from exc


@then("the user add the calories goals 0.1")
@when("the user add the calories goals 0.1")
def step_add_calories_goal_0_1(context):
    LOGGER.info("Step: enter Calories goal value 0.1 in `goalValue`.")
    try:
        context.goals_page.enter_calories_goal_value("0.1")
        LOGGER.info("Step passed: Calories goal value 0.1 entered.")
    except Exception as exc:
        LOGGER.exception("Enter Calories goal value failed: %s", exc)
        raise AssertionError(
            f"Could not add Calories goal value 0.1. Error: {exc}"
        ) from exc


@when("the user click on Miles")
@then("the user click on Miles")
@when("the user click on Kms")
@then("the user click on Kms")
def step_click_miles_goal_metric(context):
    LOGGER.info("Step: tap Miles/Kms goal metric on add goal screen.")
    try:
        context.goals_page.tap_miles_goal_metric()
        LOGGER.info("Step passed: Miles/Kms goal metric tapped.")
    except Exception as exc:
        LOGGER.exception("Miles/Kms goal metric tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Miles/Kms goal metric. Error: {exc}"
        ) from exc


@then("the user add the miles goals 0.1")
@when("the user add the miles goals 0.1")
def step_add_miles_goal_0_1(context):
    LOGGER.info("Step: enter Miles goal value 0.1 in `goalValue`.")
    try:
        context.goals_page.enter_miles_goal_value("0.1")
        LOGGER.info("Step passed: Miles goal value 0.1 entered.")
    except Exception as exc:
        LOGGER.exception("Enter Miles goal value failed: %s", exc)
        raise AssertionError(
            f"Could not add Miles goal value 0.1. Error: {exc}"
        ) from exc


@when("the user click on Time")
@then("the user click on Time")
def step_click_time_goal_metric(context):
    LOGGER.info("Step: tap Time goal metric on add goal screen.")
    try:
        context.goals_page.tap_time_goal_metric()
        LOGGER.info("Step passed: Time goal metric tapped.")
    except Exception as exc:
        LOGGER.exception("Time goal metric tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Time goal metric. Error: {exc}"
        ) from exc


@then("the user add the time goals 1")
@when("the user add the time goals 1")
def step_add_time_goal_1(context):
    LOGGER.info("Step: enter Time goal value 1 in `goalValue`.")
    try:
        context.goals_page.enter_time_goal_value("1")
        LOGGER.info("Step passed: Time goal value 1 entered.")
    except Exception as exc:
        LOGGER.exception("Enter Time goal value failed: %s", exc)
        raise AssertionError(
            f"Could not add Time goal value 1. Error: {exc}"
        ) from exc


@when("the user click on Save goals")
@then("the user click on Save goals")
@when("the user click on the SAVE GOALS option")
@then("the user click on the SAVE GOALS option")
def step_click_save_goals(context):
    LOGGER.info("Step: tap SAVE GOALS button (`btnSave`).")
    try:
        context.goals_page.tap_save_goals_button()
        LOGGER.info("Step passed: SAVE GOALS button tapped.")
    except Exception as exc:
        LOGGER.exception("SAVE GOALS button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap SAVE GOALS button (`btnSave`). Error: {exc}"
        ) from exc


@then("the user scrolls down and verifies the validation for the strides")
@then("the user verify the validation for the strides")
def step_verify_strides_goal_validation(context):
    LOGGER.info("Step: scroll down and verify Strides validation (`txtTimeErrorText`).")
    try:
        context.goals_page.verify_strides_goal_validation()
        LOGGER.info("Step passed: Strides validation error verified.")
    except Exception as exc:
        LOGGER.exception("Strides validation verification failed: %s", exc)
        raise AssertionError(
            f"Strides goal validation was not shown as expected. Error: {exc}"
        ) from exc


@then("the user scrolls down and verifies the validation for the calories")
@then("the user verify the validation for the calories")
def step_verify_calories_goal_validation(context):
    LOGGER.info("Step: scroll down and verify Calories validation (`txtTimeErrorText`).")
    try:
        context.goals_page.verify_calories_goal_validation()
        LOGGER.info("Step passed: Calories validation error verified.")
    except Exception as exc:
        LOGGER.exception("Calories validation verification failed: %s", exc)
        raise AssertionError(
            f"Calories goal validation was not shown as expected. Error: {exc}"
        ) from exc


@then("the user scrolls down and verifies the validation for the kms")
@then("the user scrolls down and verifies the validation for the miles")
@then("the user verify the validation for the kms")
@then("the user verify the validation for the miles")
def step_verify_kms_goal_validation(context):
    LOGGER.info("Step: scroll down and verify Kms/Miles validation (`txtTimeErrorText`).")
    try:
        context.goals_page.verify_kms_goal_validation()
        LOGGER.info("Step passed: Kms/Miles validation error verified.")
    except Exception as exc:
        LOGGER.exception("Kms/Miles validation verification failed: %s", exc)
        raise AssertionError(
            f"Kms/Miles goal validation was not shown as expected. Error: {exc}"
        ) from exc


@then("the user scrolls down and verifies the validation for the time")
@then("the user verify the validation for the time")
def step_verify_time_goal_validation(context):
    LOGGER.info("Step: scroll down and verify Time validation (`txtTimeErrorText`).")
    try:
        context.goals_page.verify_time_goal_validation()
        LOGGER.info("Step passed: Time validation error verified.")
    except Exception as exc:
        LOGGER.exception("Time validation verification failed: %s", exc)
        raise AssertionError(
            f"Time goal validation was not shown as expected. Error: {exc}"
        ) from exc


@when("the user click down to click on EDIT GOALS option")
@then("the user click down to click on EDIT GOALS option")
def step_click_edit_goals_option(context):
    LOGGER.info("Step: scroll down and tap EDIT GOALS (`btn_edit`).")
    try:
        context.goals_page.tap_edit_goals_option()
        LOGGER.info("Step passed: EDIT GOALS option tapped.")
    except Exception as exc:
        LOGGER.exception("EDIT GOALS option tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap EDIT GOALS (`btn_edit`). Error: {exc}"
        ) from exc


@then("the user scrolls down and edits strides goals")
@when("the user scrolls down and edits strides goals")
def step_scroll_and_edit_strides_goals(context):
    LOGGER.info("Step: scroll down and edit Strides goal (`goalTitle` / `goalValue`) with random value 1–200.")
    try:
        chosen_value = context.goals_page.edit_strides_goal()
        context.edit_strides_goal_value = chosen_value
        LOGGER.info("Step passed: Strides goal edited to %s.", chosen_value)
    except Exception as exc:
        LOGGER.exception("Edit Strides goal failed: %s", exc)
        raise AssertionError(
            f"Could not edit Strides goal (`goalTitle` / `goalValue`). Error: {exc}"
        ) from exc


@then("the user edit strides goals")
@when("the user edit strides goals")
def step_edit_strides_goals(context):
    step_scroll_and_edit_strides_goals(context)


@then("the user scrolls down and edits the Calories")
@when("the user scrolls down and edits the Calories")
def step_scroll_and_edit_calories_goal(context):
    LOGGER.info("Step: scroll down and edit Calories goal (`goalTitle` / `goalValue`).")
    try:
        chosen_value = context.goals_page.edit_calories_goal()
        context.edit_calories_goal_value = chosen_value
        LOGGER.info("Step passed: Calories goal edited to %s.", chosen_value)
    except Exception as exc:
        LOGGER.exception("Edit Calories goal failed: %s", exc)
        raise AssertionError(
            f"Could not edit Calories goal (`goalTitle` / `goalValue`). Error: {exc}"
        ) from exc


@then("the user edit the Calories")
@when("the user edit the Calories")
def step_edit_calories_goal(context):
    step_scroll_and_edit_calories_goal(context)


@then("the user scrolls down and edits the KMS/Miles")
@when("the user scrolls down and edits the KMS/Miles")
def step_scroll_and_edit_kms_goal(context):
    LOGGER.info("Step: scroll down and edit Kms/Miles goal (`goalTitle` / `goalValue`).")
    try:
        chosen_value = context.goals_page.edit_kms_goal()
        context.edit_kms_goal_value = chosen_value
        LOGGER.info("Step passed: Kms/Miles goal edited to %s.", chosen_value)
    except Exception as exc:
        LOGGER.exception("Edit Kms/Miles goal failed: %s", exc)
        raise AssertionError(
            f"Could not edit Kms/Miles goal (`goalTitle` / `goalValue`). Error: {exc}"
        ) from exc


@then("the user edit the KMS/Miles")
@when("the user edit the KMS/Miles")
def step_edit_kms_goal(context):
    step_scroll_and_edit_kms_goal(context)


@then("the user scrolls down and edits the time")
@when("the user scrolls down and edits the time")
def step_scroll_and_edit_time_goal(context):
    LOGGER.info("Step: scroll down and edit Time goal (`goalTitle` / `goalValue`).")
    try:
        chosen_value = context.goals_page.edit_time_goal()
        context.edit_time_goal_value = chosen_value
        LOGGER.info("Step passed: Time goal edited to %s.", chosen_value)
    except Exception as exc:
        LOGGER.exception("Edit Time goal failed: %s", exc)
        raise AssertionError(
            f"Could not edit Time goal (`goalTitle` / `goalValue`). Error: {exc}"
        ) from exc


@then("the user edit the time")
@when("the user edit the time")
def step_edit_time_goal(context):
    step_scroll_and_edit_time_goal(context)


@when("the user click on the Done button")
@then("the user click on the Done button")
def step_click_done_button(context):
    LOGGER.info("Step: tap Done button (`btnDone`) on Edit Goal screen.")
    try:
        context.goals_page.tap_done_button()
        LOGGER.info("Step passed: Done button tapped.")
    except Exception as exc:
        LOGGER.exception("Done button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Done button (`btnDone`). Error: {exc}"
        ) from exc


@then("the user verify the updated goals")
def step_verify_updated_goals(context):
    LOGGER.info(
        "Step: wait after Done, then verify updated goals on home (no scroll)."
    )
    expected_values = {
        "strides": getattr(context, "edit_strides_goal_value", None),
        "calories": getattr(context, "edit_calories_goal_value", None),
        "kms": getattr(context, "edit_kms_goal_value", None),
        "time": getattr(context, "edit_time_goal_value", None),
    }
    try:
        context.goals_page.verify_updated_goals_on_home(expected_values)
        LOGGER.info("Step passed: updated goals verified on home screen.")
    except Exception as exc:
        LOGGER.exception("Updated goals verification failed: %s", exc)
        raise AssertionError(
            f"Updated goals were not verified on the home screen. Error: {exc}"
        ) from exc


@when("the user click on the goal cancel option")
@then("the user click on the goal cancel option")
def step_click_goal_cancel_option(context):
    LOGGER.info("Step: tap goal cancel option (`close`) on add goal screen.")
    try:
        context.goals_page.tap_goal_cancel_option()
        LOGGER.info("Step passed: goal cancel option tapped.")
    except Exception as exc:
        LOGGER.exception("Goal cancel option tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap goal cancel option (`close`). Error: {exc}"
        ) from exc


@when("the user click on the goals back button")
@then("the user click on the goals back button")
def step_click_goals_back_button(context):
    LOGGER.info("Step: tap goals screen back button (`Navigate up`).")
    try:
        context.goals_page.tap_goals_back_button()
        LOGGER.info("Step passed: goals back button tapped.")
    except Exception as exc:
        LOGGER.exception("Goals back button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap goals back button (`Navigate up`). Error: {exc}"
        ) from exc


@then("the user verify the Save changes pop-up on the screen")
def step_verify_save_changes_popup(context):
    LOGGER.info("Step: verify Save Changes popup is visible.")
    try:
        context.goals_page.verify_save_changes_popup_visible()
        LOGGER.info("Step passed: Save Changes popup verified.")
    except Exception as exc:
        LOGGER.exception("Save Changes popup verification failed: %s", exc)
        raise AssertionError(
            f"Save Changes popup was not verified on screen. Error: {exc}"
        ) from exc


@when("the user click on the no")
@then("the user click on the no")
def step_click_save_changes_popup_no(context):
    LOGGER.info("Step: tap NO on Save Changes popup (`btnNo`).")
    try:
        context.goals_page.tap_save_changes_popup_no_button()
        LOGGER.info("Step passed: Save Changes NO button tapped.")
    except Exception as exc:
        LOGGER.exception("Save Changes NO tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap NO on Save Changes popup (`btnNo`). Error: {exc}"
        ) from exc


@then("the user verify that goals are added and present")
def step_verify_goals_added_and_present(context):
    LOGGER.info(
        "Step: verify saved goals are present on Add Goal screen (`goalRecyclerView`)."
    )
    try:
        context.goals_page.verify_goals_added_and_present()
        LOGGER.info("Step passed: saved goals verified as present.")
    except Exception as exc:
        LOGGER.exception("Saved goals presence verification failed: %s", exc)
        raise AssertionError(
            f"Saved goals were not verified on the Add Goal screen. Error: {exc}"
        ) from exc


@when("the user click on DELETE ALL GOALS")
@then("the user click on DELETE ALL GOALS")
def step_click_delete_all_goals(context):
    LOGGER.info("Step: tap DELETE ALL GOALS button (`btnDeleteAll`).")
    try:
        context.goals_page.tap_delete_all_goals_button()
        LOGGER.info("Step passed: DELETE ALL GOALS tapped.")
    except Exception as exc:
        LOGGER.exception("DELETE ALL GOALS tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap DELETE ALL GOALS button (`btnDeleteAll`). Error: {exc}"
        ) from exc
