import logging

from behave import then, when

LOGGER = logging.getLogger("cubii_upper_body_workout_steps")


@when("the user clicks on the Upper Body workout tab")
def step_click_upper_body_tab(context):
    LOGGER.info("Step: click Upper Body tab.")
    try:
        context.upper_body_workout_page.open_upper_body_tab()
        LOGGER.info("Step passed: Upper Body tab clicked.")
    except Exception as exc:
        LOGGER.exception("Upper Body tab click failed: %s", exc)
        raise AssertionError(f"Could not click Upper Body tab. Error: {exc}") from exc


@when("the user opens the Upper Body workout tab and records the current state")
def step_open_upper_body_and_record_state(context):
    LOGGER.info("Step: open Upper Body tab and record baseline state.")
    try:
        context.upper_body_workout_page.open_upper_body_tab()
        context.upper_body_baseline = context.upper_body_workout_page.record_upper_body_baseline()
        LOGGER.info("Step passed: Upper Body baseline recorded.")
    except Exception as exc:
        LOGGER.exception("Upper Body baseline step failed: %s", exc)
        raise AssertionError(f"Could not open Upper Body and record state. Error: {exc}") from exc


@when(
    "the user adds an Upper Body workout set with row 1 reps {row1_reps:d} "
    "and row 2 reps {row2_reps:d} using {input_mode} entry"
)
def step_add_upper_body_workout_set(context, row1_reps, row2_reps, input_mode):
    LOGGER.info(
        "Step: add Upper Body workout set row1=%s row2=%s mode=%s.",
        row1_reps,
        row2_reps,
        input_mode,
    )
    try:
        context.upper_body_workout_result = context.upper_body_workout_page.add_upper_body_workout(
            row1_reps,
            row2_reps,
            input_mode,
        )
        LOGGER.info("Step passed: Upper Body workout submitted.")
    except Exception as exc:
        LOGGER.exception("Upper Body workout submission failed: %s", exc)
        raise AssertionError(f"Could not submit Upper Body workout set. Error: {exc}") from exc


@when(
    "the user adds an Upper Body workout with rows 1 to 3 reps {row1_reps:d} "
    "{row2_reps:d} {row3_reps:d} using {input_mode} entry"
)
def step_add_upper_body_workout_three_sets(context, row1_reps, row2_reps, row3_reps, input_mode):
    LOGGER.info(
        "Step: add Upper Body 3-set workout row1=%s row2=%s row3=%s mode=%s.",
        row1_reps,
        row2_reps,
        row3_reps,
        input_mode,
    )
    try:
        context.upper_body_workout_result = (
            context.upper_body_workout_page.add_upper_body_workout_with_three_sets(
                row1_reps,
                row2_reps,
                row3_reps,
                input_mode,
            )
        )
        LOGGER.info("Step passed: Upper Body 3-set workout submitted.")
    except Exception as exc:
        LOGGER.exception("Upper Body 3-set workout submission failed: %s", exc)
        raise AssertionError(f"Could not submit Upper Body 3-set workout. Error: {exc}") from exc


@then(
    "the Upper Body workout entry popup should confirm rows 1 through 3 reps {row1_reps:d} "
    "{row2_reps:d} {row3_reps:d} with scroll"
)
def step_verify_upper_body_workout_popup_three_sets_scroll(context, row1_reps, row2_reps, row3_reps):
    LOGGER.info("Step: verify Upper Body 3-set confirmation popup (with scroll).")
    try:
        context.upper_body_workout_page.verify_workout_entry_popup_three_sets_with_scroll(
            row1_reps,
            row2_reps,
            row3_reps,
        )
        LOGGER.info("Step passed: Upper Body 3-set popup verified.")
    except Exception as exc:
        LOGGER.exception("Upper Body 3-set popup verification failed: %s", exc)
        raise AssertionError(f"Upper Body 3-set popup validation failed. Error: {exc}") from exc


@then(
    "the Upper Body workout entry popup should confirm row 1 reps {row1_reps:d} "
    "and row 2 reps {row2_reps:d}"
)
def step_verify_upper_body_workout_popup(context, row1_reps, row2_reps):
    LOGGER.info("Step: verify Upper Body workout confirmation popup.")
    try:
        context.upper_body_workout_page.verify_workout_entry_popup(row1_reps, row2_reps)
        LOGGER.info("Step passed: Upper Body workout popup verified.")
    except Exception as exc:
        LOGGER.exception("Upper Body workout popup verification failed: %s", exc)
        raise AssertionError(f"Upper Body workout popup validation failed. Error: {exc}") from exc


@then("the user dismisses the Upper Body workout entry popup")
def step_dismiss_upper_body_workout_popup(context):
    LOGGER.info("Step: dismiss Upper Body workout confirmation popup.")
    try:
        context.upper_body_workout_page.dismiss_workout_entry_popup()
        LOGGER.info("Step passed: Upper Body workout popup dismissed.")
    except Exception as exc:
        LOGGER.exception("Upper Body workout popup dismissal failed: %s", exc)
        raise AssertionError(f"Could not dismiss Upper Body workout popup. Error: {exc}") from exc


@then(
    "the new Upper Body workout entry should be persisted with row 1 reps {row1_reps:d} "
    "and row 2 reps {row2_reps:d}"
)
def step_verify_upper_body_workout_persisted(context, row1_reps, row2_reps):
    LOGGER.info("Step: verify new Upper Body workout entry persisted.")
    try:
        context.upper_body_workout_page.verify_new_entry_persisted(row1_reps, row2_reps)
        LOGGER.info("Step passed: Upper Body workout entry persisted.")
    except Exception as exc:
        LOGGER.exception("Upper Body workout persistence verification failed: %s", exc)
        raise AssertionError(
            f"Upper Body workout persistence validation failed. Error: {exc}"
        ) from exc
