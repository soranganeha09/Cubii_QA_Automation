import logging

from behave import then, when

LOGGER = logging.getLogger("cubii_help_steps")


@when("the user click on the Help")
@then("the user click on the Help")
def step_click_help(context):
    LOGGER.info("Step: clicking Help from Settings menu.")
    try:
        context.home_page.tap_help_menu_item()
        LOGGER.info("Step passed: Help screen opened.")
    except Exception as exc:
        LOGGER.exception("Clicking Help menu item failed: %s", exc)
        raise AssertionError(
            f"Unable to click Help menu item. Error: {exc}"
        ) from exc


@when("the user verify whole list")
@then("the user verify whole list")
def step_verify_whole_help_list(context):
    LOGGER.info("Step: verifying whole Help list.")
    try:
        context.help_page.verify_whole_help_list()
        LOGGER.info("Step passed: whole Help list verified.")
    except Exception as exc:
        LOGGER.exception("Whole Help list verification failed: %s", exc)
        raise AssertionError(
            f"Whole Help list verification failed. Error: {exc}"
        ) from exc


@when("the user click on back option of the help screen")
@then("the user click on back option of the help screen")
def step_click_help_screen_back_option(context):
    LOGGER.info("Step: clicking Help screen back option (Navigate up).")
    try:
        context.help_page.tap_help_screen_back_option()
        LOGGER.info("Step passed: Help screen back option clicked.")
    except Exception as exc:
        LOGGER.exception("Help screen back option click failed: %s", exc)
        raise AssertionError(
            f"Could not click Help screen back option. Error: {exc}"
        ) from exc


@when("the user click on back option of the FAQ screen")
@then("the user click on back option of the FAQ screen")
def step_click_faq_screen_back_option(context):
    LOGGER.info("Step: clicking FAQ screen back option (Navigate up).")
    try:
        context.help_page.tap_faq_screen_back_option()
        LOGGER.info("Step passed: FAQ screen back option clicked.")
    except Exception as exc:
        LOGGER.exception("FAQ screen back option click failed: %s", exc)
        raise AssertionError(
            f"Could not click FAQ screen back option. Error: {exc}"
        ) from exc


@when("the user click on back option of the more screen")
@then("the user click on back option of the more screen")
@when("the user click back option of the more screen")
@then("the user click back option of the more screen")
def step_click_more_screen_back_option(context):
    LOGGER.info("Step: clicking More screen back option (`iv_back`).")
    try:
        context.home_page.tap_back_button()
        LOGGER.info("Step passed: More screen back option clicked.")
    except Exception as exc:
        LOGGER.exception("More screen back option click failed: %s", exc)
        raise AssertionError(
            f"Could not click More screen back option. Error: {exc}"
        ) from exc


@when("the user click on the Privacy policy")
@then("the user click on the Privacy policy")
def step_click_privacy_policy(context):
    LOGGER.info("Step: clicking Privacy Policy on Help screen.")
    try:
        context.help_page.tap_privacy_policy()
        LOGGER.info("Step passed: Privacy Policy opened.")
    except Exception as exc:
        LOGGER.exception("Clicking Privacy Policy failed: %s", exc)
        raise AssertionError(
            f"Unable to click Privacy Policy. Error: {exc}"
        ) from exc


@when("the user verify the Privacy policy screen")
@then("the user verify the Privacy policy screen")
def step_verify_privacy_policy_screen(context):
    LOGGER.info("Step: verifying Privacy Policy screen.")
    try:
        context.help_page.verify_privacy_policy_screen()
        LOGGER.info("Step passed: Privacy Policy screen verified.")
    except Exception as exc:
        LOGGER.exception("Privacy Policy screen verification failed: %s", exc)
        raise AssertionError(
            f"Privacy Policy screen verification failed. Error: {exc}"
        ) from exc


@when("the user verify the Privacy policy description")
@then("the user verify the Privacy policy description")
def step_verify_privacy_policy_description(context):
    LOGGER.info("Step: verifying Privacy Policy description.")
    try:
        context.help_page.verify_privacy_policy_description()
        LOGGER.info("Step passed: Privacy Policy description verified.")
    except Exception as exc:
        LOGGER.exception("Privacy Policy description verification failed: %s", exc)
        raise AssertionError(
            f"Privacy Policy description verification failed. Error: {exc}"
        ) from exc


@when("the user go back from the Privacy policy screen")
@then("the user go back from the Privacy policy screen")
def step_go_back_from_privacy_policy_screen(context):
    LOGGER.info("Step: go back from Privacy Policy screen.")
    try:
        context.help_page.tap_privacy_policy_back_option()
        LOGGER.info("Step passed: left Privacy Policy screen.")
    except Exception as exc:
        LOGGER.exception("Go back from Privacy Policy failed: %s", exc)
        raise AssertionError(
            f"Go back from Privacy Policy failed. Error: {exc}"
        ) from exc


@when("the user comeback to help screen")
@then("the user comeback to help screen")
def step_verify_returned_to_help_screen(context):
    LOGGER.info("Step: verifying user returned to Help screen.")
    try:
        context.help_page.verify_returned_to_help_screen()
        LOGGER.info("Step passed: user is on Help screen.")
    except Exception as exc:
        LOGGER.exception("Return to Help screen verification failed: %s", exc)
        raise AssertionError(
            f"Return to Help screen verification failed. Error: {exc}"
        ) from exc


@when("the user click on the Terms of Service")
@then("the user click on the Terms of Service")
def step_click_terms_of_service(context):
    LOGGER.info("Step: clicking Terms of Service on Help screen.")
    try:
        context.help_page.tap_terms_of_service()
        LOGGER.info("Step passed: Terms of Service opened.")
    except Exception as exc:
        LOGGER.exception("Clicking Terms of Service failed: %s", exc)
        raise AssertionError(
            f"Unable to click Terms of Service. Error: {exc}"
        ) from exc


@when("the user redirect to the Terms of Service screen")
@then("the user redirect to the Terms of Service screen")
def step_verify_terms_of_service_screen_redirect(context):
    LOGGER.info("Step: verifying redirect to Terms of Service screen.")
    try:
        context.help_page.verify_terms_of_service_screen_redirect()
        LOGGER.info("Step passed: Terms of Service screen redirect verified.")
    except Exception as exc:
        LOGGER.exception("Terms of Service screen redirect verification failed: %s", exc)
        raise AssertionError(
            f"Terms of Service screen redirect verification failed. Error: {exc}"
        ) from exc


@when("the user verify the Terms of Service description and click on the cancel icon")
@then("the user verify the Terms of Service description and click on the cancel icon")
def step_verify_terms_description_and_click_cancel(context):
    LOGGER.info(
        "Step: verify Terms of Service cookie description and tap cancel icon."
    )
    try:
        context.help_page.verify_terms_of_service_description_and_click_cancel()
        LOGGER.info("Step passed: Terms description verified and cancel tapped.")
    except Exception as exc:
        LOGGER.exception("Terms description / cancel step failed: %s", exc)
        raise AssertionError(
            f"Terms of Service description or cancel icon step failed. Error: {exc}"
        ) from exc


@when("the user swipe left and comeback to help screen")
@then("the user swipe left and comeback to help screen")
def step_swipe_left_and_comeback_to_help_screen(context):
    LOGGER.info("Step: go back from Privacy Policy (gestures + BACK, no verification).")
    try:
        context.help_page.go_back_from_privacy_policy_to_help_screen()
        LOGGER.info("Step passed: back navigation from Privacy Policy completed.")
    except Exception as exc:
        LOGGER.exception("Privacy Policy back navigation failed: %s", exc)
        raise AssertionError(
            f"Privacy Policy back navigation failed. Error: {exc}"
        ) from exc


@when("the user go back and comeback to help screen")
@then("the user go back and comeback to help screen")
def step_go_back_and_comeback_to_help_screen(context):
    LOGGER.info("Step: go back from Privacy Policy (no screen verification).")
    try:
        context.help_page.go_back_from_privacy_policy_to_help_screen()
        LOGGER.info("Step passed: back navigation from Privacy Policy completed.")
    except Exception as exc:
        LOGGER.exception("Go back and return to Help screen failed: %s", exc)
        raise AssertionError(
            f"Go back and return to Help screen failed. Error: {exc}"
        ) from exc


@when("the user click on back option of the Privacy policy")
@then("the user click on back option of the Privacy policy")
def step_click_privacy_policy_back_option(context):
    LOGGER.info("Step: clicking Privacy Policy screen back option (Navigate up).")
    try:
        context.help_page.tap_privacy_policy_back_option()
        LOGGER.info("Step passed: Privacy Policy back option clicked.")
    except Exception as exc:
        LOGGER.exception("Privacy Policy back option click failed: %s", exc)
        raise AssertionError(
            f"Could not click Privacy Policy back option. Error: {exc}"
        ) from exc


@when("the user click on the Assembly Video")
@then("the user click on the Assembly Video")
def step_click_assembly_video(context):
    LOGGER.info("Step: clicking Assembly Video on Help screen.")
    try:
        context.help_page.tap_assembly_video()
        LOGGER.info("Step passed: Assembly Video opened.")
    except Exception as exc:
        LOGGER.exception("Clicking Assembly Video failed: %s", exc)
        raise AssertionError(
            f"Unable to click Assembly Video. Error: {exc}"
        ) from exc


@when("the user verify that Assembly video screen open")
@then("the user verify that Assembly video screen open")
def step_verify_assembly_video_screen_open(context):
    LOGGER.info("Step: verifying Assembly Video screen is open.")
    try:
        context.help_page.verify_assembly_video_screen_open()
        LOGGER.info("Step passed: Assembly Video screen verified.")
    except Exception as exc:
        LOGGER.exception("Assembly Video screen verification failed: %s", exc)
        raise AssertionError(
            f"Assembly Video screen verification failed. Error: {exc}"
        ) from exc


@when("the user click on back option of Assembly video")
@then("the user click on back option of Assembly video")
def step_click_assembly_video_back_option(context):
    LOGGER.info("Step: clicking Assembly Video screen back option (Navigate up).")
    try:
        context.help_page.tap_assembly_video_back_option()
        LOGGER.info("Step passed: Assembly Video back option clicked.")
    except Exception as exc:
        LOGGER.exception("Assembly Video back option click failed: %s", exc)
        raise AssertionError(
            f"Could not click Assembly Video back option. Error: {exc}"
        ) from exc


@when("the user click on the Product Manual")
@then("the user click on the Product Manual")
def step_click_product_manual(context):
    LOGGER.info("Step: clicking Product Manual on Help screen.")
    try:
        context.help_page.tap_product_manual()
        LOGGER.info("Step passed: Product Manual opened.")
    except Exception as exc:
        LOGGER.exception("Clicking Product Manual failed: %s", exc)
        raise AssertionError(
            f"Unable to click Product Manual. Error: {exc}"
        ) from exc


@when("the user click on back option for the Product Manual")
@then("the user click on back option for the Product Manual")
def step_click_product_manual_back_option(context):
    LOGGER.info("Step: clicking Product Manual screen back option (Navigate up).")
    try:
        context.help_page.tap_product_manual_back_option()
        LOGGER.info("Step passed: Product Manual back option clicked.")
    except Exception as exc:
        LOGGER.exception("Product Manual back option click failed: %s", exc)
        raise AssertionError(
            f"Could not click Product Manual back option. Error: {exc}"
        ) from exc


@when("verify that product manual screen open")
@then("verify that product manual screen open")
def step_verify_product_manual_screen_open(context):
    LOGGER.info("Step: verifying Product Manual screen is open.")
    try:
        context.help_page.verify_product_manual_screen_open()
        LOGGER.info("Step passed: Product Manual screen verified.")
    except Exception as exc:
        LOGGER.exception("Product Manual screen verification failed: %s", exc)
        raise AssertionError(
            f"Product Manual screen verification failed. Error: {exc}"
        ) from exc


@when("the user click on the FAQ option")
@then("the user click on the FAQ option")
def step_click_faq_option(context):
    LOGGER.info("Step: clicking FAQ on Help screen.")
    try:
        context.help_page.tap_faq_option()
        LOGGER.info("Step passed: FAQ screen opened.")
    except Exception as exc:
        LOGGER.exception("Clicking FAQ failed: %s", exc)
        raise AssertionError(f"Unable to click FAQ option. Error: {exc}") from exc


@when("the user redirect to the FAQ screen")
@then("the user redirect to the FAQ screen")
def step_verify_faq_screen_redirect(context):
    LOGGER.info("Step: verifying redirect to FAQ screen.")
    try:
        context.help_page.verify_faq_screen_redirect()
        LOGGER.info("Step passed: FAQ screen redirect verified.")
    except Exception as exc:
        LOGGER.exception("FAQ screen redirect verification failed: %s", exc)
        raise AssertionError(
            f"FAQ screen redirect verification failed. Error: {exc}"
        ) from exc


@when('the user verify the text "{expected_text}"')
@then('the user verify the text "{expected_text}"')
def step_verify_faq_text(context, expected_text):
    LOGGER.info("Step: verifying FAQ screen text %r.", expected_text)
    try:
        context.help_page.verify_faq_how_can_we_help_text(expected_fragment=expected_text)
        LOGGER.info("Step passed: FAQ screen text verified.")
    except Exception as exc:
        LOGGER.exception("FAQ screen text verification failed: %s", exc)
        raise AssertionError(
            f"FAQ screen text verification failed. Error: {exc}"
        ) from exc


@when("the user verify the FAQ screen structure")
@then("the user verify the FAQ screen structure")
def step_verify_faq_screen_structure(context):
    LOGGER.info("Step: verifying full FAQ screen structure.")
    try:
        context.help_page.verify_faq_screen_structure()
        LOGGER.info("Step passed: FAQ screen structure verified.")
    except Exception as exc:
        LOGGER.exception("FAQ screen structure verification failed: %s", exc)
        raise AssertionError(
            f"FAQ screen structure verification failed. Error: {exc}"
        ) from exc


@when("the user verify all FAQ questions are listed")
@then("the user verify all FAQ questions are listed")
def step_verify_faq_questions_list(context):
    LOGGER.info("Step: verifying all FAQ questions are listed.")
    try:
        context.help_page.verify_faq_questions_list()
        LOGGER.info("Step passed: all FAQ questions verified.")
    except Exception as exc:
        LOGGER.exception("FAQ questions list verification failed: %s", exc)
        raise AssertionError(
            f"FAQ questions list verification failed. Error: {exc}"
        ) from exc


@when("the user scroll down and verify all FAQ questions are listed")
@then("the user scroll down and verify all FAQ questions are listed")
def step_scroll_down_and_verify_faq_questions_list(context):
    LOGGER.info("Step: scroll down FAQ list and verify all FAQ questions are listed.")
    try:
        context.help_page.verify_faq_questions_list()
        LOGGER.info("Step passed: FAQ list scrolled and all questions verified.")
    except Exception as exc:
        LOGGER.exception("FAQ scroll-and-verify list failed: %s", exc)
        raise AssertionError(
            f"FAQ scroll-and-verify list failed. Error: {exc}"
        ) from exc


@when('the user tap on the FAQ question "{question_text}"')
@then('the user tap on the FAQ question "{question_text}"')
def step_tap_faq_question(context, question_text):
    LOGGER.info("Step: tapping FAQ question %r.", question_text)
    try:
        context.help_page.tap_faq_question_by_text(question_text)
        LOGGER.info("Step passed: FAQ question %r tapped.", question_text)
    except Exception as exc:
        LOGGER.exception("Tapping FAQ question %r failed: %s", question_text, exc)
        raise AssertionError(
            f"Could not tap FAQ question {question_text!r}. Error: {exc}"
        ) from exc


@when('the user search for "{keyword}" in the FAQ search bar')
@then('the user search for "{keyword}" in the FAQ search bar')
def step_search_in_faq(context, keyword):
    LOGGER.info("Step: searching FAQ for %r.", keyword)
    try:
        context.help_page.search_in_faq(keyword)
        LOGGER.info("Step passed: searched FAQ for %r.", keyword)
    except Exception as exc:
        LOGGER.exception("FAQ search for %r failed: %s", keyword, exc)
        raise AssertionError(
            f"FAQ search for {keyword!r} failed. Error: {exc}"
        ) from exc


@when('the user verify the FAQ search result contains "{expected_text}"')
@then('the user verify the FAQ search result contains "{expected_text}"')
def step_verify_faq_search_result(context, expected_text):
    LOGGER.info("Step: verifying FAQ search result contains %r.", expected_text)
    try:
        context.help_page.verify_faq_search_result_contains(expected_text)
        LOGGER.info("Step passed: FAQ search result contains %r.", expected_text)
    except Exception as exc:
        LOGGER.exception("FAQ search result verification failed: %s", exc)
        raise AssertionError(
            f"FAQ search result verification failed. Error: {exc}"
        ) from exc


@when("the user clear the FAQ search bar")
@then("the user clear the FAQ search bar")
def step_clear_faq_search(context):
    LOGGER.info("Step: clearing FAQ search bar.")
    try:
        context.help_page.clear_faq_search()
        LOGGER.info("Step passed: FAQ search bar cleared.")
    except Exception as exc:
        LOGGER.exception("Clearing FAQ search bar failed: %s", exc)
        raise AssertionError(
            f"Could not clear FAQ search bar. Error: {exc}"
        ) from exc


@when('the user tap on the FAQ question "{question_text}" and verify it is expanded')
@then('the user tap on the FAQ question "{question_text}" and verify it is expanded')
def step_tap_faq_question_and_verify_expanded(context, question_text):
    LOGGER.info("Step: tapping FAQ question %r and verifying expansion.", question_text)
    try:
        context.help_page.tap_faq_question_and_verify_expanded(question_text)
        LOGGER.info("Step passed: FAQ question %r expanded.", question_text)
    except Exception as exc:
        LOGGER.exception("FAQ question %r expand verification failed: %s", question_text, exc)
        raise AssertionError(
            f"FAQ question {question_text!r} expand verification failed. Error: {exc}"
        ) from exc


@when('the user tap on the FAQ question "{question_text}" and verify it is collapsed')
@then('the user tap on the FAQ question "{question_text}" and verify it is collapsed')
def step_tap_faq_question_and_verify_collapsed(context, question_text):
    LOGGER.info("Step: tapping FAQ question %r and verifying collapse.", question_text)
    try:
        context.help_page.tap_faq_question_and_verify_collapsed(question_text)
        LOGGER.info("Step passed: FAQ question %r collapsed.", question_text)
    except Exception as exc:
        LOGGER.exception("FAQ question %r collapse verification failed: %s", question_text, exc)
        raise AssertionError(
            f"FAQ question {question_text!r} collapse verification failed. Error: {exc}"
        ) from exc


@when("the user scroll down on the FAQ screen")
@then("the user scroll down on the FAQ screen")
def step_scroll_down_on_faq_screen(context):
    LOGGER.info("Step: scrolling down on FAQ screen.")
    try:
        context.help_page.scroll_faq_screen_down()
        LOGGER.info("Step passed: FAQ screen scrolled down.")
    except Exception as exc:
        LOGGER.exception("Scrolling down on FAQ screen failed: %s", exc)
        raise AssertionError(
            f"Scrolling down on FAQ screen failed. Error: {exc}"
        ) from exc


@when("the user click on the Customer support back button")
@then("the user click on the Customer support back button")
def step_click_customer_support_back_button(context):
    LOGGER.info("Step: clicking Customer Support back button (Navigate up).")
    try:
        context.help_page.tap_customer_support_back_button()
        LOGGER.info("Step passed: Customer Support back button clicked.")
    except Exception as exc:
        LOGGER.exception("Customer Support back button click failed: %s", exc)
        raise AssertionError(
            f"Could not click Customer Support back button. Error: {exc}"
        ) from exc


@when("the user click on the customer support")
@then("the user click on the customer support")
def step_click_customer_support(context):
    LOGGER.info("Step: clicking Customer Support on Help screen.")
    try:
        context.help_page.tap_customer_support()
        LOGGER.info("Step passed: Customer Support screen opened.")
    except Exception as exc:
        LOGGER.exception("Clicking Customer Support failed: %s", exc)
        raise AssertionError(
            f"Unable to click Customer Support. Error: {exc}"
        ) from exc


@when("verify user redirect to the Customer Support screen")
@then("verify user redirect to the Customer Support screen")
def step_verify_customer_support_screen_redirect(context):
    LOGGER.info("Step: verifying redirect to Customer Support screen.")
    try:
        context.help_page.verify_customer_support_screen_redirect()
        LOGGER.info("Step passed: Customer Support screen redirect verified.")
    except Exception as exc:
        LOGGER.exception("Customer Support screen redirect verification failed: %s", exc)
        raise AssertionError(
            f"Customer Support screen redirect verification failed. Error: {exc}"
        ) from exc


@when("the user verify all the available details on the screen")
@then("the user verify all the available details on the screen")
def step_verify_customer_support_screen_details(context):
    LOGGER.info("Step: verifying all available details on Customer Support screen.")
    try:
        context.help_page.verify_customer_support_screen_details()
        LOGGER.info("Step passed: Customer Support screen details verified.")
    except Exception as exc:
        LOGGER.exception("Customer Support screen details verification failed: %s", exc)
        raise AssertionError(
            f"Customer Support screen details verification failed. Error: {exc}"
        ) from exc


@when("the user click on the Getting Started")
@then("the user click on the Getting Started")
def step_click_getting_started(context):
    LOGGER.info("Step: clicking Getting Started on Customer Support screen.")
    try:
        context.help_page.tap_getting_started()
        LOGGER.info("Step passed: Getting Started clicked.")
    except Exception as exc:
        LOGGER.exception("Getting Started click failed: %s", exc)
        raise AssertionError(
            f"Unable to click Getting Started. Error: {exc}"
        ) from exc


@when('the user redirect to the cubii video into the youtube and verify the video name "{video_name}"')
@then('the user redirect to the cubii video into the youtube and verify the video name "{video_name}"')
def step_verify_cubii_video_in_youtube(context, video_name):
    LOGGER.info(
        "Step: verify redirect to Cubii video in YouTube (title=%r).", video_name
    )
    try:
        context.help_page.verify_cubii_setup_video_in_youtube(video_title=video_name)
        LOGGER.info("Step passed: YouTube Cubii setup video verified.")
    except Exception as exc:
        LOGGER.exception("YouTube Cubii video verification failed: %s", exc)
        raise AssertionError(
            f"YouTube Cubii video verification failed. Error: {exc}"
        ) from exc


@when("the user go back to cubii application")
@then("the user go back to cubii application")
def step_return_to_cubii_application(context):
    LOGGER.info("Step: return to Cubii application from YouTube.")
    try:
        context.help_page.return_to_cubii_application()
        LOGGER.info("Step passed: returned to Cubii application.")
    except Exception as exc:
        LOGGER.exception("Return to Cubii application failed: %s", exc)
        raise AssertionError(
            f"Could not return to Cubii application. Error: {exc}"
        ) from exc


@when("the user click on the Email us")
@then("the user click on the Email us")
def step_click_email_us(context):
    LOGGER.info("Step: clicking Email us on Customer Support screen.")
    try:
        context.help_page.tap_email_us()
        LOGGER.info("Step passed: Email us clicked.")
    except Exception as exc:
        LOGGER.exception("Email us click failed: %s", exc)
        raise AssertionError(
            f"Unable to click Email us. Error: {exc}"
        ) from exc


@when('the user verify that the cubii logo and "What can we help you with today?" text')
@then('the user verify that the cubii logo and "What can we help you with today?" text')
def step_verify_help_email_us_web_page(context):
    LOGGER.info(
        'Step: verify Cubii logo and "What can we help you with today?" on help web page.'
    )
    try:
        context.help_page.verify_help_email_us_web_page()
        LOGGER.info("Step passed: help web page verified.")
    except Exception as exc:
        LOGGER.exception("Help web page verification failed: %s", exc)
        raise AssertionError(
            f"Help web page verification failed. Error: {exc}"
        ) from exc


@when("the user click on the close button")
@then("the user click on the close button")
def step_click_chrome_close_button(context):
    LOGGER.info("Step: clicking Chrome Close tab button.")
    try:
        context.help_page.tap_chrome_close_tab_button()
        LOGGER.info("Step passed: Chrome Close tab button clicked.")
    except Exception as exc:
        LOGGER.exception("Chrome Close tab button click failed: %s", exc)
        raise AssertionError(
            f"Could not click Chrome Close tab button. Error: {exc}"
        ) from exc


@when("the user click on the Call us")
@then("the user click on the Call us")
def step_click_call_us(context):
    LOGGER.info("Step: clicking Call us on Customer Support screen.")
    try:
        context.help_page.tap_call_us()
        LOGGER.info("Step passed: Call us clicked.")
    except Exception as exc:
        LOGGER.exception("Call us click failed: %s", exc)
        raise AssertionError(
            f"Unable to click Call us. Error: {exc}"
        ) from exc


@when("the user verify the dial screen open with the number")
@then("the user verify the dial screen open with the number")
def step_verify_dial_screen_open_with_number(context):
    LOGGER.info("Step: verify dial screen is open with phone number.")
    try:
        context.help_page.verify_dial_screen_open_with_number()
        LOGGER.info("Step passed: dial screen verified.")
    except Exception as exc:
        LOGGER.exception("Dial screen verification failed: %s", exc)
        raise AssertionError(
            f"Dial screen verification failed. Error: {exc}"
        ) from exc
