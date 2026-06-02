import logging

from behave import then, when

LOGGER = logging.getLogger("cubii_wellness_journii_steps")


@when("the user opens the Wellness Journii tab")
def step_open_wellness_journii_tab(context):
    LOGGER.info("Step: open Wellness Journii tab.")
    try:
        context.wellness_journii_page.open_wellness_journii_tab()
        if hasattr(context, "ftue_page"):
            context.ftue_page.handle_wellness_journii_webview()
        LOGGER.info("Step passed: Wellness Journii tab opened.")
    except Exception as exc:
        LOGGER.exception("Open Wellness Journii tab failed: %s", exc)
        raise AssertionError(
            f"Could not open Wellness Journii tab. Error: {exc}"
        ) from exc


@then("the current and previous Journii tabs should be visible")
def step_verify_current_and_previous_journii_tabs(context):
    LOGGER.info("Step: verify current and previous Journii tabs.")
    try:
        context.wellness_journii_page.verify_current_and_previous_tabs()
        LOGGER.info("Step passed: current and previous tabs verified.")
    except Exception as exc:
        LOGGER.exception("Current/previous Journii tab verification failed: %s", exc)
        raise AssertionError(
            f"Current and previous Journii tabs verification failed. Error: {exc}"
        ) from exc


@then("the current month Journii image should be displayed")
def step_verify_current_month_journii_image(context):
    LOGGER.info("Step: verify current month Journii image.")
    try:
        context.wellness_journii_page.verify_current_month_journii_image()
        LOGGER.info("Step passed: current month Journii image verified.")
    except Exception as exc:
        LOGGER.exception("Current month Journii image verification failed: %s", exc)
        raise AssertionError(
            f"Current month Journii image verification failed. Error: {exc}"
        ) from exc


@then("the current month Journii title should be displayed")
def step_verify_current_month_journii_title(context):
    LOGGER.info("Step: verify current month Journii title.")
    try:
        context.wellness_journii_page.verify_current_month_journii_name()
        LOGGER.info("Step passed: current month Journii title verified.")
    except Exception as exc:
        LOGGER.exception("Current month Journii title verification failed: %s", exc)
        raise AssertionError(
            f"Current month Journii title verification failed. Error: {exc}"
        ) from exc


@then("the joined Journii members highlight should be displayed")
def step_verify_joined_journii_members_highlight(context):
    LOGGER.info("Step: verify joined Journii members highlight.")
    try:
        context.wellness_journii_page.verify_joined_journii_members_highlight()
        LOGGER.info("Step passed: joined Journii members highlight verified.")
    except Exception as exc:
        LOGGER.exception("Joined Journii members highlight verification failed: %s", exc)
        raise AssertionError(
            f"Joined Journii members highlight verification failed. Error: {exc}"
        ) from exc


@then(
    "all visible Journii tasks should show date name and people joined count"
)
def step_verify_all_journii_tasks(context):
    LOGGER.info("Step: verify all Journii tasks (date, name, people joined).")
    try:
        context.wellness_journii_page.verify_all_journii_tasks()
        LOGGER.info("Step passed: all Journii tasks verified.")
    except Exception as exc:
        LOGGER.exception("Journii tasks verification failed: %s", exc)
        raise AssertionError(
            f"Journii tasks verification failed. Error: {exc}"
        ) from exc


@when("the user taps the Previous Journii segment tab")
def step_tap_previous_journii_segment_tab(context):
    LOGGER.info("Step: tap Previous Journii segment tab (sbPrevious).")
    try:
        context.wellness_journii_page.tap_previous_journii_segment_tab()
        LOGGER.info("Step passed: Previous Journii segment tab tapped.")
    except Exception as exc:
        LOGGER.exception("Tap Previous Journii segment tab failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Previous Journii segment tab (sbPrevious). Error: {exc}"
        ) from exc


@then(
    "the Previous Journii list should show No Journiis when there are no past programs"
)
def step_verify_previous_journii_empty_when_no_programs(context):
    LOGGER.info(
        "Step: verify Previous Journii list (programs with scroll, or No Journiis if empty)."
    )
    try:
        context.wellness_journii_page.verify_previous_journii_empty_state_if_no_programs()
        LOGGER.info("Step passed: Previous Journii empty state verified.")
    except Exception as exc:
        LOGGER.exception("Previous Journii empty state verification failed: %s", exc)
        raise AssertionError(
            f"Previous Journii empty state verification failed. Error: {exc}"
        ) from exc


@then("the user click on the current tab")
def step_click_current_journii_tab(context):
    LOGGER.info("Step: tap Current Journii segment tab (sbCurrent).")
    try:
        context.wellness_journii_page.tap_current_journii_segment_tab()
        LOGGER.info("Step passed: Current Journii segment tab tapped.")
    except Exception as exc:
        LOGGER.exception("Tap Current Journii segment tab failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Current Journii segment tab (sbCurrent). Error: {exc}"
        ) from exc


@when("the user taps the Journii banner card on the Wellness screen")
def step_tap_journii_banner_card(context):
    LOGGER.info("Step: tap Journii banner card (ivJourniiImage).")
    try:
        context.wellness_journii_page.tap_journii_banner_card()
        if hasattr(context, "ftue_page"):
            context.ftue_page.handle_wellness_journii_webview()
        LOGGER.info("Step passed: Journii banner card tapped.")
    except Exception as exc:
        LOGGER.exception("Journii banner card tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Journii banner card. Error: {exc}"
        ) from exc


@then("the Wellness Journii detail screen title should be displayed")
def step_verify_journii_detail_screen_title(context):
    LOGGER.info("Step: verify Wellness Journii detail screen title.")
    try:
        context.wellness_journii_page.verify_journii_detail_screen_title()
        LOGGER.info("Step passed: detail screen title verified.")
    except Exception as exc:
        LOGGER.exception("Journii detail screen title verification failed: %s", exc)
        raise AssertionError(
            f"Wellness Journii detail screen title verification failed. Error: {exc}"
        ) from exc


@then("the Wellness Journii detail description should match the join button state")
def step_verify_journii_detail_description(context):
    LOGGER.info(
        "Step: verify Wellness Journii detail description (conditional on join button)."
    )
    try:
        context.wellness_journii_page.verify_journii_detail_description()
        LOGGER.info("Step passed: detail description verified.")
    except Exception as exc:
        LOGGER.exception("Journii detail description verification failed: %s", exc)
        raise AssertionError(
            f"Wellness Journii detail description verification failed. Error: {exc}"
        ) from exc


@when("the user scrolls down to the View All button on the Journii detail screen")
def step_scroll_to_view_all_on_journii_detail(context):
    LOGGER.info("Step: scroll down on Journii detail until View All (btnViewAll) is visible.")
    try:
        context.wellness_journii_page.scroll_detail_until_view_all_visible()
        LOGGER.info("Step passed: View All button is visible on screen.")
    except Exception as exc:
        LOGGER.exception("Scroll to View All button failed: %s", exc)
        raise AssertionError(
            f"Could not scroll to the View All button on the Journii detail screen. "
            f"Error: {exc}"
        ) from exc


@when("the user taps the View All button on the Journii detail screen")
def step_tap_view_all_on_journii_detail(context):
    LOGGER.info("Step: tap View All button (btnViewAll) on Journii detail screen.")
    try:
        context.wellness_journii_page.tap_view_all_button()
        LOGGER.info("Step passed: View All button tapped.")
    except Exception as exc:
        LOGGER.exception("Tap View All button failed: %s", exc)
        raise AssertionError(
            f"Could not tap the View All button (btnViewAll). Error: {exc}"
        ) from exc


@then("the user click on back button")
def step_click_back_button(context):
    LOGGER.info("Step: tap Back on Journii screen (toolbar or Back text).")
    try:
        context.wellness_journii_page.tap_journii_detail_back_button()
        LOGGER.info("Step passed: Back button tapped.")
    except Exception as exc:
        LOGGER.exception("Tap Back button failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Back button (toolbar / text Back). Error: {exc}"
        ) from exc


@when("the user taps the filter option")
@when("the user taps the upcoming tasks filter option")
def step_tap_filter_option(context):
    LOGGER.info("Step: tap filter option (FILTERS) on upcoming tasks.")
    try:
        context.wellness_journii_page.tap_upcoming_tasks_filter_option()
        LOGGER.info("Step passed: filter option opened.")
    except Exception as exc:
        LOGGER.exception("Tap filter option failed: %s", exc)
        raise AssertionError(
            f'Could not tap the filter option (cvShowFilters). Error: {exc}'
        ) from exc


@when("the user taps the Incomplete filter option")
def step_tap_incomplete_filter_option(context):
    LOGGER.info("Step: tap Incomplete filter (mcvIncomplete).")
    try:
        context.wellness_journii_page.tap_incomplete_filter_option()
        LOGGER.info("Step passed: Incomplete filter selected.")
    except Exception as exc:
        LOGGER.exception("Tap Incomplete filter failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Incomplete filter (mcvIncomplete). Error: {exc}"
        ) from exc


@when("the user taps Show Results on the upcoming tasks filter")
@when("the user taps Show Results on the Completed tasks filter")
@when("the user taps Show Results on the All tasks filter")
def step_tap_filter_show_results(context):
    LOGGER.info("Step: tap Show Results (btnShowResults) on filter sheet.")
    try:
        context.wellness_journii_page.tap_filter_show_results()
        LOGGER.info("Step passed: Show Results tapped.")
    except Exception as exc:
        LOGGER.exception("Tap Show Results failed: %s", exc)
        raise AssertionError(
            f"Could not tap Show Results (btnShowResults). Error: {exc}"
        ) from exc


@when("the user taps the Completed filter option")
def step_tap_completed_filter_option(context):
    LOGGER.info("Step: tap Completed filter (mcvCompleted).")
    try:
        context.wellness_journii_page.tap_completed_filter_option()
        LOGGER.info("Step passed: Completed filter selected.")
    except Exception as exc:
        LOGGER.exception("Tap Completed filter failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Completed filter (mcvCompleted). Error: {exc}"
        ) from exc


@then(
    "all filtered incomplete upcoming Journii tasks should show date name and people joined"
)
def step_verify_filtered_incomplete_upcoming_tasks(context):
    LOGGER.info(
        "Step: verify filtered incomplete upcoming tasks "
        "(task cards or no-results empty state)."
    )
    try:
        context.wellness_journii_page.verify_all_filtered_incomplete_upcoming_tasks()
        LOGGER.info("Step passed: filtered incomplete upcoming tasks verified.")
    except Exception as exc:
        LOGGER.exception("Filtered incomplete upcoming tasks verification failed: %s", exc)
        raise AssertionError(
            f"Filtered incomplete upcoming Journii tasks verification failed. "
            f"Error: {exc}"
        ) from exc


@when("the user taps the All filter option")
def step_tap_all_filter_option(context):
    LOGGER.info("Step: tap All filter (mcvAll).")
    try:
        context.wellness_journii_page.tap_all_filter_option()
        LOGGER.info("Step passed: All filter selected.")
    except Exception as exc:
        LOGGER.exception("Tap All filter failed: %s", exc)
        raise AssertionError(
            f"Could not tap the All filter (mcvAll). Error: {exc}"
        ) from exc


@then(
    "all filtered complete upcoming Journii tasks should show date name and people joined"
)
def step_verify_filtered_complete_upcoming_tasks(context):
    LOGGER.info(
        "Step: verify filtered complete upcoming tasks "
        "(task cards or no-results empty state)."
    )
    try:
        context.wellness_journii_page.verify_all_filtered_complete_upcoming_tasks()
        LOGGER.info("Step passed: filtered complete upcoming tasks verified.")
    except Exception as exc:
        LOGGER.exception("Filtered complete upcoming tasks verification failed: %s", exc)
        raise AssertionError(
            f"Filtered complete upcoming Journii tasks verification failed. Error: {exc}"
        ) from exc


@then(
    "all filtered All upcoming Journii tasks should show date name and people joined"
)
def step_verify_filtered_all_upcoming_tasks(context):
    LOGGER.info(
        "Step: verify All-filtered upcoming tasks "
        "(task cards or no-results empty state)."
    )
    try:
        context.wellness_journii_page.verify_all_filtered_all_upcoming_tasks()
        LOGGER.info("Step passed: All-filtered upcoming tasks verified.")
    except Exception as exc:
        LOGGER.exception("Filtered All upcoming tasks verification failed: %s", exc)
        raise AssertionError(
            f"Filtered All upcoming Journii tasks verification failed. Error: {exc}"
        ) from exc


@when("the user taps the Journii join button if it is displayed")
def step_tap_journii_join_button_if_displayed(context):
    LOGGER.info("Step: tap Journii join button (btnViewAll) if displayed.")
    try:
        tapped = context.wellness_journii_page.tap_join_button_if_displayed()
        if tapped:
            LOGGER.info("Step passed: join button tapped.")
        else:
            LOGGER.info("Step passed: join button not shown; skipped tap.")
    except Exception as exc:
        LOGGER.exception("Journii join button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Journii join button. Error: {exc}"
        ) from exc


@then("the Journii banner image month title and tasks progress should be displayed")
def step_verify_journii_banner_month_title_and_progress(context):
    LOGGER.info(
        "Step: verify Journii banner image, month title, and tasks progress highlight."
    )
    try:
        context.wellness_journii_page.verify_journii_banner_month_title_and_progress()
        LOGGER.info("Step passed: banner, title, and progress verified.")
    except Exception as exc:
        LOGGER.exception("Journii banner/progress verification failed: %s", exc)
        raise AssertionError(
            f"Journii banner and month progress verification failed. Error: {exc}"
        ) from exc


@when("the user taps the Wellness Journii title description arrow")
def step_tap_journii_title_description_arrow(context):
    LOGGER.info("Step: tap Wellness Journii title description arrow (tvTitleDescIcon).")
    try:
        context.wellness_journii_page.tap_journii_title_description_arrow()
        LOGGER.info("Step passed: title description arrow tapped.")
    except Exception as exc:
        LOGGER.exception("Title description arrow tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Wellness Journii title description arrow. Error: {exc}"
        ) from exc


@then("the Wellness Journii description link should be displayed")
def step_verify_journii_description_link(context):
    LOGGER.info("Step: verify Wellness Journii description link (txtLink).")
    try:
        context.wellness_journii_page.verify_journii_description_link_displayed()
        LOGGER.info("Step passed: description link verified.")
    except Exception as exc:
        LOGGER.exception("Description link verification failed: %s", exc)
        raise AssertionError(
            f"Wellness Journii description link verification failed. Error: {exc}"
        ) from exc


@when("the user taps the Wellness Journii Download PDF link")
def step_tap_journii_download_pdf_link(context):
    LOGGER.info("Step: tap Wellness Journii Download PDF link (txtLink).")
    try:
        context.wellness_journii_page.tap_journii_download_pdf_link()
        LOGGER.info("Step passed: Download PDF link tapped.")
    except Exception as exc:
        LOGGER.exception("Download PDF link tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Wellness Journii Download PDF link. Error: {exc}"
        ) from exc


@then("the PDF link should open in Chrome with a cubii.com URL")
def step_verify_pdf_link_opened_in_chrome(context):
    LOGGER.info("Step: verify PDF link opened in external Chrome with cubii.com URL.")
    try:
        context.wellness_journii_page.verify_pdf_link_opened_in_external_chrome()
        LOGGER.info("Step passed: Chrome opened with cubii.com URL.")
    except Exception as exc:
        LOGGER.exception("Chrome PDF link verification failed: %s", exc)
        raise AssertionError(
            f"PDF link did not open in Chrome with cubii.com URL. Error: {exc}"
        ) from exc


@when("the user returns to the Cubii app from Chrome")
def step_return_to_cubii_from_chrome(context):
    LOGGER.info("Step: return to Cubii app from external Chrome.")
    try:
        context.wellness_journii_page.return_to_cubii_from_chrome()
        LOGGER.info("Step passed: returned to Cubii from Chrome.")
    except Exception as exc:
        LOGGER.exception("Return to Cubii from Chrome failed: %s", exc)
        raise AssertionError(
            f"Could not return to the Cubii app from Chrome. Error: {exc}"
        ) from exc


@then("the Upcoming Tasks and Previous Tasks tabs should be visible")
def step_verify_upcoming_and_previous_tasks_tabs(context):
    LOGGER.info("Step: verify Upcoming Tasks and Previous Tasks tabs.")
    try:
        context.wellness_journii_page.verify_upcoming_and_previous_tasks_tabs()
        LOGGER.info("Step passed: Upcoming and Previous Tasks tabs verified.")
    except Exception as exc:
        LOGGER.exception("Upcoming/Previous Tasks tab verification failed: %s", exc)
        raise AssertionError(
            f"Upcoming Tasks and Previous Tasks tabs verification failed. Error: {exc}"
        ) from exc


@when("the user taps the Previous Tasks tab")
def step_tap_previous_tasks_tab(context):
    LOGGER.info("Step: tap Previous Tasks tab (tvCompletedTasks).")
    try:
        context.wellness_journii_page.tap_previous_tasks_tab()
        LOGGER.info("Step passed: Previous Tasks tab tapped.")
    except Exception as exc:
        LOGGER.exception("Tap Previous Tasks tab failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Previous Tasks tab. Error: {exc}"
        ) from exc


@when("the user taps the Back button on the Journii detail screen")
def step_tap_journii_detail_back_button(context):
    LOGGER.info("Step: tap Back on the Wellness Journii detail screen.")
    try:
        context.wellness_journii_page.tap_journii_detail_back_button()
        LOGGER.info("Step passed: Back button tapped.")
    except Exception as exc:
        LOGGER.exception("Tap Journii detail Back button failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Back button on the Journii detail screen. Error: {exc}"
        ) from exc


@then("all previous Journii tasks should show date name and people joined")
def step_verify_all_previous_journii_task_cards(context):
    LOGGER.info(
        "Step: verify all previous Journii tasks (date, name, people joined)."
    )
    try:
        context.wellness_journii_page.verify_all_previous_task_cards()
        LOGGER.info("Step passed: all previous task cards verified.")
    except Exception as exc:
        LOGGER.exception("Previous Journii task cards verification failed: %s", exc)
        raise AssertionError(
            f"Previous Journii task cards verification failed. Error: {exc}"
        ) from exc


@when("the user scrolls up to the Journii banner")
def step_scroll_up_to_journii_banner(context):
    LOGGER.info("Step: scroll up to the Journii banner on the detail screen.")
    try:
        context.wellness_journii_page.scroll_up_to_journii_banner()
        LOGGER.info("Step passed: Journii banner visible at top.")
    except Exception as exc:
        LOGGER.exception("Scroll up to Journii banner failed: %s", exc)
        raise AssertionError(
            f"Could not scroll up to the Journii banner. Error: {exc}"
        ) from exc


@then(
    "all upcoming Journii tasks should show date name progress and people joined"
)
def step_verify_all_upcoming_journii_task_cards(context):
    LOGGER.info(
        "Step: verify all upcoming Journii tasks (date, name, progress, people joined)."
    )
    try:
        context.wellness_journii_page.verify_all_upcoming_task_cards()
        LOGGER.info("Step passed: all upcoming task cards verified.")
    except Exception as exc:
        LOGGER.exception("Upcoming Journii task cards verification failed: %s", exc)
        raise AssertionError(
            f"Upcoming Journii task cards verification failed. Error: {exc}"
        ) from exc
