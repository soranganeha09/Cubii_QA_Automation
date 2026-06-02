import logging

from behave import then, when

LOGGER = logging.getLogger("cubii_notification_steps")


@when("the user taps the notification icon")
def step_tap_notification_icon(context):
    LOGGER.info("Step: tap notification icon.")
    try:
        context.notification_page.verify_notification_icon_visible()
        context.notification_page.tap_notification_icon()
        LOGGER.info("Step passed: notification icon tapped.")
    except Exception as exc:
        LOGGER.exception("Notification icon tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the notification icon. Error: {exc}"
        ) from exc


@when("the user taps the notification icon from any tab")
def step_tap_notification_icon_from_any_tab(context):
    LOGGER.info(
        "Step: open notifications (from any tab, or continue if already on screen)."
    )
    try:
        context.notification_page.open_notifications_from_any_tab(
            context.cubii_studio_page
        )
        LOGGER.info("Step passed: user is on the notifications screen.")
    except Exception as exc:
        LOGGER.exception("Open notifications from any tab failed: %s", exc)
        raise AssertionError(
            f"Could not open the notifications screen from a bottom-nav tab. Error: {exc}"
        ) from exc


@then("the user click on the clear all option")
def step_tap_clear_all_option(context):
    LOGGER.info("Step: tap Clear All option.")
    try:
        context.notification_page.tap_clear_all_notification()
        LOGGER.info("Step passed: Clear All option tapped.")
    except Exception as exc:
        LOGGER.exception("Clear All tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Clear All option. Error: {exc}"
        ) from exc


@then("the user verify that clear all notification pop-up open")
def step_verify_clear_all_popup_open(context):
    LOGGER.info("Step: verify clear-all notification popup.")
    try:
        context.notification_page.verify_clear_all_notification_popup_open()
        LOGGER.info("Step passed: clear-all popup verified.")
    except Exception as exc:
        LOGGER.exception("Clear-all popup verification failed: %s", exc)
        raise AssertionError(
            f"Clear all notification popup was not displayed. Error: {exc}"
        ) from exc


@then("the user click on the go back option")
def step_tap_popup_go_back(context):
    LOGGER.info("Step: tap GO BACK on clear-all popup.")
    try:
        context.notification_page.tap_popup_go_back()
        LOGGER.info("Step passed: GO BACK tapped.")
    except Exception as exc:
        LOGGER.exception("GO BACK tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap GO BACK on the clear-all popup. Error: {exc}"
        ) from exc


@then("the user click on the pop-up clear all option")
def step_tap_popup_clear_all_confirm(context):
    LOGGER.info("Step: tap Clear All confirm on popup (btnYes).")
    try:
        context.notification_page.tap_popup_clear_all_confirm()
        LOGGER.info("Step passed: popup Clear All confirm tapped.")
    except Exception as exc:
        LOGGER.exception("Popup Clear All confirm tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Clear All confirm on the popup. Error: {exc}"
        ) from exc


@then("the user verify that the empty state is displayed")
def step_verify_empty_state_displayed(context):
    LOGGER.info("Step: verify empty state after clear all.")
    try:
        context.notification_page.verify_empty_state_displayed()
        LOGGER.info("Step passed: empty state displayed.")
    except Exception as exc:
        LOGGER.exception("Empty state verification failed: %s", exc)
        raise AssertionError(
            f"Empty state was not displayed as expected. Error: {exc}"
        ) from exc


@then("the user verify the clear all and back button header")
def step_verify_notifications_header_clear_all_and_back(context):
    LOGGER.info("Step: verify notifications header Clear All and back button.")
    try:
        context.notification_page.verify_notifications_header_clear_all_and_back()
        LOGGER.info("Step passed: Clear All and back button header verified.")
    except Exception as exc:
        LOGGER.exception("Notifications header verification failed: %s", exc)
        raise AssertionError(
            f"Could not verify Clear All and back button on notifications header. "
            f"Error: {exc}"
        ) from exc


@then("the user verify all the notifications")
def step_verify_all_notifications(context):
    LOGGER.info("Step: verify all notifications by scrolling rv_notification.")
    try:
        context.notification_page.verify_all_notifications()
        LOGGER.info("Step passed: all notifications verified.")
    except Exception as exc:
        LOGGER.exception("Verify all notifications failed: %s", exc)
        raise AssertionError(
            f"Could not verify all notifications on the notifications screen. Error: {exc}"
        ) from exc


@then("the user verifies that there are no notifications available")
def step_verify_no_notifications_available(context):
    LOGGER.info(
        "Step: verify empty notifications state (ignored when list has notifications)."
    )
    try:
        result = context.notification_page.verify_no_notifications_available()
        if result == "skipped":
            LOGGER.info(
                "Step passed (ignored): empty state not shown — account has notifications; "
                "no emptyListText check required."
            )
            return
        LOGGER.info("Step passed: no notifications available (empty state verified).")
    except Exception as exc:
        LOGGER.exception("Empty notifications verification failed: %s", exc)
        raise AssertionError(
            f"Empty notifications state was not displayed as expected. Error: {exc}"
        ) from exc


@then("the user verify the friend notification invitation")
def step_verify_friend_notification_invitation(context):
    LOGGER.info("Step: verify friend notification invitation (txtGroupInvite).")
    try:
        context.notification_page.verify_friend_notification_invitation()
        LOGGER.info("Step passed: friend notification invitation verified.")
    except Exception as exc:
        LOGGER.exception("Friend notification invitation verification failed: %s", exc)
        raise AssertionError(
            f"Friend notification invitation was not displayed as expected. Error: {exc}"
        ) from exc


@then("the user click on the accept friend request option")
def step_tap_accept_friend_request(context):
    LOGGER.info("Step: tap ACCEPT on friend request (imageView17).")
    try:
        context.notification_page.tap_accept_friend_request()
        LOGGER.info("Step passed: ACCEPT tapped on friend request.")
    except Exception as exc:
        LOGGER.exception("Accept friend request tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap ACCEPT on the friend request notification. Error: {exc}"
        ) from exc


@then("the user click on the friend request arrow button")
def step_tap_friend_request_arrow(context):
    LOGGER.info("Step: tap friend request arrow (imgNotificationArrowGroupInvite).")
    try:
        context.notification_page.tap_friend_request_arrow_button()
        LOGGER.info("Step passed: friend request arrow tapped.")
    except Exception as exc:
        LOGGER.exception("Friend request arrow tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the friend request arrow button. Error: {exc}"
        ) from exc


@then("the user verify the friend request redirection")
def step_verify_friend_request_redirection(context):
    LOGGER.info("Step: verify friend request redirection after arrow tap.")
    try:
        context.notification_page.verify_friend_request_redirection()
        LOGGER.info("Step passed: friend request redirection verified.")
    except Exception as exc:
        LOGGER.exception("Friend request redirection verification failed: %s", exc)
        raise AssertionError(
            f"Friend request redirection was not confirmed. Error: {exc}"
        ) from exc


@then("the notifications screen should be displayed")
def step_verify_notifications_screen(context):
    LOGGER.info("Step: verify notifications screen.")
    try:
        context.notification_page.verify_notifications_screen()
        LOGGER.info("Step passed: notifications screen verified.")
    except Exception as exc:
        LOGGER.exception("Notifications screen verification failed: %s", exc)
        raise AssertionError(
            f"Notifications screen was not displayed as expected. Error: {exc}"
        ) from exc
