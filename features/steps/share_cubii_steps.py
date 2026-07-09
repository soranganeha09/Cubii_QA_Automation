import logging

from behave import then, when

LOGGER = logging.getLogger("cubii_share_cubii_steps")


@when("the user click on the Share Cubii")
@then("the user click on the Share Cubii")
def step_click_share_cubii(context):
    LOGGER.info("Step: clicking Share Cubii from Settings menu.")
    try:
        context.home_page.tap_share_cubii_menu_item()
        LOGGER.info("Step passed: Share Cubii menu item tapped.")
    except Exception as exc:
        LOGGER.exception("Clicking Share Cubii menu item failed: %s", exc)
        raise AssertionError(
            f"Unable to click Share Cubii menu item. Error: {exc}"
        ) from exc


@when("the user select the chrome browser")
@then("the user select the chrome browser")
def step_select_chrome_browser_from_share_sheet(context):
    LOGGER.info("Step: selecting Chrome from Android share sheet.")
    try:
        context.share_cubii_page.tap_chrome_browser_from_share_sheet()
        LOGGER.info("Step passed: Chrome selected from share sheet.")
    except Exception as exc:
        LOGGER.exception("Selecting Chrome from share sheet failed: %s", exc)
        raise AssertionError(
            f"Unable to select Chrome browser from share sheet. Error: {exc}"
        ) from exc


@when("the user click on the cancel option")
@then("the user click on the cancel option")
def step_click_chrome_cookie_cancel_option(context):
    LOGGER.info("Step: tap cookie cancel (X) on Chrome cubii.com page.")
    try:
        context.share_cubii_page.tap_chrome_cookie_cancel_option()
        LOGGER.info("Step passed: Chrome cookie cancel option tapped.")
    except Exception as exc:
        LOGGER.exception("Chrome cookie cancel tap failed: %s", exc)
        raise AssertionError(
            f"Unable to tap Chrome cookie cancel option. Error: {exc}"
        ) from exc


@when("the user verify the link is open into chrome browser")
@then("the user verify the link is open into chrome browser")
def step_verify_link_opened_in_chrome_browser(context):
    LOGGER.info("Step: verify Share Cubii link opened in Chrome with cubii.com.")
    try:
        context.share_cubii_page.verify_link_opened_in_chrome_browser()
        LOGGER.info("Step passed: cubii.com verified in Chrome browser.")
    except Exception as exc:
        LOGGER.exception("Chrome link verification failed: %s", exc)
        raise AssertionError(
            f"Share Cubii link was not verified in Chrome browser. Error: {exc}"
        ) from exc


@when("the user go back to application")
@then("the user go back to application")
@when("the user go back to the application")
@then("the user go back to the application")
@when("go back to the application")
@then("go back to the application")
def step_go_back_to_application(context):
    LOGGER.info("Step: return to Cubii app from external share flow.")
    try:
        context.share_cubii_page.return_to_application()
        LOGGER.info("Step passed: returned to Cubii application.")
    except Exception as exc:
        LOGGER.exception("Return to Cubii application failed: %s", exc)
        raise AssertionError(
            f"Could not go back to the Cubii application. Error: {exc}"
        ) from exc


@when("the user click on the gmail option")
@then("the user click on the gmail option")
def step_click_gmail_option(context):
    LOGGER.info("Step: selecting Gmail from share sheet.")
    try:
        context.share_cubii_page.tap_gmail_from_share_sheet()
        LOGGER.info("Step passed: Gmail selected from share sheet.")
    except Exception as exc:
        LOGGER.exception("Gmail selection failed: %s", exc)
        raise AssertionError(
            f"Unable to select Gmail from share sheet. Error: {exc}"
        ) from exc


@when("the user select the aubergine account")
@then("the user select the aubergine account")
def step_select_aubergine_gmail_account(context):
    LOGGER.info("Step: select Aubergine Gmail account.")
    try:
        context.share_cubii_page.select_aubergine_gmail_account()
        LOGGER.info("Step passed: Aubergine Gmail account selected.")
    except Exception as exc:
        LOGGER.exception("Gmail account selection failed: %s", exc)
        raise AssertionError(
            f"Unable to select Aubergine Gmail account. Error: {exc}"
        ) from exc


@when("the user click on the search and search the Neha")
@then("the user click on the search and search the Neha")
def step_search_gmail_recipient_neha(context):
    LOGGER.info("Step: search Gmail recipient Neha.")
    try:
        context.share_cubii_page.search_and_select_gmail_recipient()
        LOGGER.info("Step passed: Gmail recipient searched and selected.")
    except Exception as exc:
        LOGGER.exception("Gmail recipient search failed: %s", exc)
        raise AssertionError(
            f"Unable to search and select Gmail recipient. Error: {exc}"
        ) from exc


@when("the user share the link with user and click on send message")
@then("the user share the link with user and click on send message")
def step_share_link_and_send_gmail_message(context):
    LOGGER.info("Step: tap Gmail Post message (send).")
    try:
        context.share_cubii_page.tap_gmail_post_message_send()
        LOGGER.info("Step passed: Gmail message sent.")
    except Exception as exc:
        LOGGER.exception("Gmail send message failed: %s", exc)
        raise AssertionError(
            f"Unable to send Gmail share message. Error: {exc}"
        ) from exc


@when("the user click on the drive option")
@then("the user click on the drive option")
def step_click_drive_option(context):
    LOGGER.info("Step: selecting Drive from share sheet.")
    try:
        context.share_cubii_page.tap_drive_from_share_sheet()
        LOGGER.info("Step passed: Drive selected from share sheet.")
    except Exception as exc:
        LOGGER.exception("Drive selection failed: %s", exc)
        raise AssertionError(
            f"Unable to select Drive from share sheet. Error: {exc}"
        ) from exc


@when("the user verify the details file name, email and drive location")
@then("the user verify the details file name, email and drive location")
def step_verify_drive_upload_details(context):
    LOGGER.info("Step: verify Drive upload file name, account, and location.")
    try:
        context.share_cubii_page.verify_drive_upload_details()
        LOGGER.info("Step passed: Drive upload details verified.")
    except Exception as exc:
        LOGGER.exception("Drive upload details verification failed: %s", exc)
        raise AssertionError(
            f"Drive upload details verification failed. Error: {exc}"
        ) from exc


@when("the user click on the upload button")
@then("the user click on the upload button")
def step_click_drive_upload_button(context):
    LOGGER.info("Step: tap Drive Upload button.")
    try:
        context.share_cubii_page.tap_drive_upload_button()
        LOGGER.info("Step passed: Drive Upload button tapped.")
    except Exception as exc:
        LOGGER.exception("Drive upload button tap failed: %s", exc)
        raise AssertionError(
            f"Unable to tap Drive Upload button. Error: {exc}"
        ) from exc
