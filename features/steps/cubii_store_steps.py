import logging

from behave import then, when

LOGGER = logging.getLogger("cubii_store_steps")


@when("the user click on the The Cubii Store option")
@then("the user click on the The Cubii Store option")
def step_click_the_cubii_store_option(context):
    LOGGER.info("Step: clicking The Cubii Store from Settings menu.")
    try:
        context.home_page.tap_cubii_store_menu_item()
        LOGGER.info("Step passed: The Cubii Store menu item tapped.")
    except Exception as exc:
        LOGGER.exception("Clicking The Cubii Store menu item failed: %s", exc)
        raise AssertionError(
            f"Unable to click The Cubii Store menu item. Error: {exc}"
        ) from exc


@when("the user click on the cancel icon")
@then("the user click on the cancel icon")
def step_click_cubii_store_cancel_icon(context):
    LOGGER.info("Step: tap cookie cancel (X) on Chrome Cubii Store page.")
    try:
        context.cubii_store_page.tap_chrome_cookie_cancel_option()
        LOGGER.info("Step passed: Chrome cookie cancel icon tapped.")
    except Exception as exc:
        LOGGER.exception("Chrome cookie cancel tap failed: %s", exc)
        raise AssertionError(
            f"Unable to tap Chrome cookie cancel icon. Error: {exc}"
        ) from exc


@when("the user verify the cubii store link is open")
@then("the user verify the cubii store link is open")
def step_verify_cubii_store_link_is_open(context):
    LOGGER.info("Step: verify The Cubii Store link opened in external browser.")
    try:
        context.cubii_store_page.verify_cubii_store_link_opened()
        LOGGER.info("Step passed: The Cubii Store link verified in browser.")
    except Exception as exc:
        LOGGER.exception("The Cubii Store link verification failed: %s", exc)
        raise AssertionError(
            f"The Cubii Store link was not verified in the browser. Error: {exc}"
        ) from exc
