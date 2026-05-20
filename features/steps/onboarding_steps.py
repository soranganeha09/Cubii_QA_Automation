from behave import given, then, when


@given("the user is on the Cubii home screen")
def step_user_on_home_screen(context):
    assert context.home_page.is_visible_by_accessibility_id(
        context.home_page.GET_STARTED_BUTTON
    ), "Home screen is not visible. Verify app launch and locator values."


@when("the user taps the Get Started button")
def step_tap_get_started(context):
    context.home_page.tap_get_started()


@then("the onboarding screen is displayed")
def step_verify_onboarding(context):
    assert context.home_page.is_onboarding_visible(), (
        "Onboarding screen did not appear. "
        "Verify the onboarding header locator value."
    )
