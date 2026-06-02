import logging

from behave import then, when

LOGGER = logging.getLogger("cubii_communitii_friends_steps")


@when("the user opens the Communitii Friends tab from any tab")
def step_open_communitii_friends_from_any_tab(context):
    LOGGER.info(
        "Step: open Communitii Friends (from any tab, or continue if already on Friends)."
    )
    try:
        context.communitii_page.open_communitii_friends_from_any_tab()
        LOGGER.info("Step passed: user is on the Communitii Friends tab.")
    except Exception as exc:
        LOGGER.exception("Open Communitii Friends from any tab failed: %s", exc)
        raise AssertionError(
            "Could not open the Communitii Friends tab from a bottom-nav tab. "
            f"Error: {exc}"
        ) from exc


@then("the Communitii Friends tab should be displayed")
def step_verify_communitii_friends_tab(context):
    LOGGER.info("Step: verify Communitii Friends tab.")
    try:
        context.communitii_page.verify_communitii_friends_tab()
        LOGGER.info("Step passed: Communitii Friends tab verified.")
    except Exception as exc:
        LOGGER.exception("Communitii Friends tab verification failed: %s", exc)
        raise AssertionError(
            f"Communitii Friends tab was not displayed correctly. Error: {exc}"
        ) from exc


@when("the user taps Invite Friends")
def step_tap_invite_friends(context):
    LOGGER.info("Step: tap Invite Friends button.")
    try:
        context.communitii_page.tap_invite_friends_button()
        LOGGER.info("Step passed: Invite Friends tapped.")
    except Exception as exc:
        LOGGER.exception("Tap Invite Friends failed: %s", exc)
        raise AssertionError(
            f"Could not tap Invite Friends. Error: {exc}"
        ) from exc


@when("the user taps the add friend search field")
def step_tap_add_friend_search(context):
    LOGGER.info("Step: tap add friend search field.")
    try:
        context.communitii_page.tap_add_new_chat_search_field()
        LOGGER.info("Step passed: add friend search field tapped.")
    except Exception as exc:
        LOGGER.exception("Tap add friend search field failed: %s", exc)
        raise AssertionError(
            f"Could not tap add friend search field. Error: {exc}"
        ) from exc


@when('the user enters the invite friend name "{name}"')
def step_enter_invite_friend_name(context, name):
    LOGGER.info("Step: enter invite friend search name %r.", name)
    try:
        context.communitii_page.enter_invite_friend_search_name(name)
        LOGGER.info("Step passed: invite friend name entered.")
    except Exception as exc:
        LOGGER.exception("Enter invite friend name failed: %s", exc)
        raise AssertionError(
            f"Could not enter invite friend name {name!r}. Error: {exc}"
        ) from exc


@when("the user taps the invite friend add icon")
def step_tap_invite_friend_add_icon(context):
    LOGGER.info("Step: tap invite friend add icon (+).")
    try:
        context.communitii_page.tap_invite_friend_add_icon()
        LOGGER.info("Step passed: invite friend add icon tapped.")
    except Exception as exc:
        LOGGER.exception("Tap invite friend add icon failed: %s", exc)
        raise AssertionError(
            f"Could not tap invite friend add icon. Error: {exc}"
        ) from exc


@when("the user taps the first friend chat profile in the list")
def step_tap_first_friend_chat_profile(context):
    LOGGER.info("Step: tap first friend chat profile in Friends list.")
    try:
        context.communitii_page.tap_first_friend_chat_profile()
        LOGGER.info("Step passed: first friend chat profile opened.")
    except Exception as exc:
        LOGGER.exception("Tap first friend chat profile failed: %s", exc)
        raise AssertionError(
            f"Could not open the first friend chat profile. Error: {exc}"
        ) from exc


@then("the friend chat profile name and status should be displayed")
def step_verify_friend_chat_profile_toolbar(context):
    LOGGER.info("Step: verify friend chat profile toolbar name and status.")
    try:
        context.communitii_page.verify_friend_chat_profile_toolbar()
        LOGGER.info("Step passed: chat profile name and status verified.")
    except Exception as exc:
        LOGGER.exception("Friend chat profile toolbar verification failed: %s", exc)
        raise AssertionError(
            f"Friend chat profile name/status verification failed. Error: {exc}"
        ) from exc


@when("the user taps the chat message input field")
def step_tap_chat_message_input(context):
    LOGGER.info("Step: tap chat message input (Type Something).")
    try:
        context.communitii_page.tap_chat_conversation_message_field()
        LOGGER.info("Step passed: chat message input tapped.")
    except Exception as exc:
        LOGGER.exception("Tap chat message input failed: %s", exc)
        raise AssertionError(
            f"Could not tap chat message input field. Error: {exc}"
        ) from exc


@when("the user taps the Chiir motivation strides target if available")
@then("the user taps the Chiir motivation strides target if available")
def step_tap_chiir_motivation_if_available(context):
    LOGGER.info("Step: tap Chiir motivation strides target card if present.")
    try:
        tapped = context.communitii_page.tap_chiir_motivation_strides_target_if_present()
        context.chiir_motivation_card_tapped = tapped
        if tapped:
            LOGGER.info("Step passed: Chiir motivation strides target tapped.")
        else:
            LOGGER.info("Step passed: Chiir motivation card not available (skipped).")
    except Exception as exc:
        LOGGER.exception("Tap Chiir motivation card failed: %s", exc)
        raise AssertionError(
            f"Could not tap Chiir motivation strides target. Error: {exc}"
        ) from exc


@when("the user taps the chat conversation options menu")
def step_tap_chat_conversation_options(context):
    LOGGER.info("Step: tap chat conversation three-dot options menu.")
    try:
        context.communitii_page.tap_chat_conversation_options_menu()
        LOGGER.info("Step passed: chat options menu opened.")
    except Exception as exc:
        LOGGER.exception("Tap chat conversation options menu failed: %s", exc)
        raise AssertionError(
            f"Could not tap chat conversation options menu. Error: {exc}"
        ) from exc


@then("the View Info option should be visible in the chat menu")
def step_verify_view_info_option_visible(context):
    LOGGER.info("Step: verify View Info option in chat menu.")
    try:
        context.communitii_page.verify_view_info_option_visible()
        LOGGER.info("Step passed: View Info option visible.")
    except Exception as exc:
        LOGGER.exception("View Info option verification failed: %s", exc)
        raise AssertionError(
            f"View Info option was not visible in chat menu. Error: {exc}"
        ) from exc


@when("the user taps View Info from the chat options")
def step_tap_view_info_from_chat_options(context):
    LOGGER.info("Step: tap View Info from chat options.")
    try:
        context.communitii_page.tap_view_info_from_chat_options()
        LOGGER.info("Step passed: View Info tapped.")
    except Exception as exc:
        LOGGER.exception("Tap View Info failed: %s", exc)
        raise AssertionError(
            f"Could not tap View Info from chat options. Error: {exc}"
        ) from exc


@when("the user taps Unfriend from the chat options")
def step_tap_unfriend_from_chat_options(context):
    LOGGER.info("Step: tap Unfriend from chat options (txtOptionUnFriend).")
    try:
        context.communitii_page.tap_unfriend_from_chat_options()
        LOGGER.info("Step passed: Unfriend option tapped from chat menu.")
    except Exception as exc:
        LOGGER.exception("Tap Unfriend from chat options failed: %s", exc)
        raise AssertionError(
            f"Could not tap Unfriend from chat options. Error: {exc}"
        ) from exc


@when("the user taps Report from the chat options")
def step_tap_report_from_chat_options(context):
    LOGGER.info("Step: tap Report from chat options (txtOptionReport).")
    try:
        context.communitii_page.tap_report_from_chat_options()
        LOGGER.info("Step passed: Report option tapped from chat menu.")
    except Exception as exc:
        LOGGER.exception("Tap Report from chat options failed: %s", exc)
        raise AssertionError(
            f"Could not tap Report from chat options. Error: {exc}"
        ) from exc


@when("the user taps Block from the chat options")
def step_tap_block_from_chat_options(context):
    LOGGER.info("Step: tap Block from chat options (txtOptionBlock).")
    try:
        context.communitii_page.tap_block_from_chat_options()
        LOGGER.info("Step passed: Block option tapped from chat menu.")
    except Exception as exc:
        LOGGER.exception("Tap Block from chat options failed: %s", exc)
        raise AssertionError(
            f"Could not tap Block from chat options. Error: {exc}"
        ) from exc


@when("the user taps Block on the block confirmation dialog")
def step_tap_block_confirmation_dialog_confirm(context):
    LOGGER.info("Step: tap Block on block confirmation popup (btnBlock).")
    try:
        context.communitii_page.tap_block_confirmation_dialog_confirm()
        LOGGER.info("Step passed: Block confirmation dialog confirmed.")
    except Exception as exc:
        LOGGER.exception("Tap Block on block confirmation dialog failed: %s", exc)
        raise AssertionError(
            f"Could not tap Block on block confirmation dialog. Error: {exc}"
        ) from exc


@then("the View Info screen should display profile and action options")
def step_verify_view_info_screen(context):
    LOGGER.info("Step: verify View Info screen profile and actions.")
    try:
        context.communitii_page.verify_view_info_screen()
        LOGGER.info("Step passed: View Info screen verified.")
    except Exception as exc:
        LOGGER.exception("View Info screen verification failed: %s", exc)
        raise AssertionError(
            f"View Info screen was not displayed correctly. Error: {exc}"
        ) from exc


@when("the user taps View Profile on the View Info screen")
def step_tap_view_profile_on_view_info_screen(context):
    LOGGER.info("Step: tap View Profile on View Info screen (txtViewProfile).")
    try:
        context.communitii_page.tap_view_profile_on_view_info_screen()
        LOGGER.info("Step passed: View Profile tapped on View Info screen.")
    except Exception as exc:
        LOGGER.exception("Tap View Profile on View Info failed: %s", exc)
        raise AssertionError(
            f"Could not tap View Profile on View Info screen. Error: {exc}"
        ) from exc


@then("the friend View Profile screen should show available profile sections")
def step_verify_friend_view_profile_sections(context):
    LOGGER.info(
        "Step: verify friend View Profile sections (Bio, Focus, Interests, Badges if present)."
    )
    try:
        context.communitii_page.verify_friend_view_profile_sections_if_available()
        LOGGER.info("Step passed: friend View Profile sections verified.")
    except Exception as exc:
        LOGGER.exception("Friend View Profile verification failed: %s", exc)
        raise AssertionError(
            f"Friend View Profile verification failed. Error: {exc}"
        ) from exc


@when("the user taps the profile back button")
def step_tap_profile_back_button(context):
    LOGGER.info("Step: tap profile back button (iv_back).")
    try:
        context.communitii_page.tap_viewed_member_profile_screen_back_button()
        LOGGER.info("Step passed: profile back button tapped.")
    except Exception as exc:
        LOGGER.exception("Profile back button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap profile back button (`iv_back`). Error: {exc}"
        ) from exc


@when("the user taps the chat back button")
def step_tap_chat_back_button(context):
    LOGGER.info("Step: tap chat back button (iv_back).")
    try:
        context.communitii_page.tap_chat_conversation_back_button()
        LOGGER.info("Step passed: chat back button tapped.")
    except Exception as exc:
        LOGGER.exception("Chat back button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap chat back button (`iv_back`). Error: {exc}"
        ) from exc


@when("the user taps Report on the View Info screen")
def step_tap_report_on_view_info_screen(context):
    LOGGER.info("Step: tap Report on View Info screen (btnReport).")
    try:
        context.communitii_page.tap_report_on_user_details_sheet()
        LOGGER.info("Step passed: Report tapped on View Info screen.")
    except Exception as exc:
        LOGGER.exception("Tap Report on View Info failed: %s", exc)
        raise AssertionError(
            f"Could not tap Report on View Info screen. Error: {exc}"
        ) from exc


@when("the user taps Block on the View Info screen")
def step_tap_block_on_view_info_screen(context):
    LOGGER.info("Step: tap Block on View Info screen (btnBlock).")
    try:
        context.communitii_page.tap_block_on_view_info_screen()
        LOGGER.info("Step passed: Block tapped on View Info screen.")
    except Exception as exc:
        LOGGER.exception("Tap Block on View Info failed: %s", exc)
        raise AssertionError(
            f"Could not tap Block on View Info screen. Error: {exc}"
        ) from exc


@when("the user taps Unfriend on the View Info screen")
def step_tap_unfriend_on_view_info_screen(context):
    LOGGER.info("Step: tap Unfriend on View Info screen (btnUnfriend).")
    try:
        context.communitii_page.tap_unfriend_on_view_info_screen()
        LOGGER.info("Step passed: Unfriend tapped on View Info screen.")
    except Exception as exc:
        LOGGER.exception("Tap Unfriend on View Info failed: %s", exc)
        raise AssertionError(
            f"Could not tap Unfriend on View Info screen. Error: {exc}"
        ) from exc


@when("the user taps Yes on the unfriend confirmation")
def step_tap_unfriend_confirmation_yes(context):
    LOGGER.info("Step: tap Yes on unfriend confirmation dialog (btnYes).")
    try:
        context.communitii_page.tap_unfriend_confirmation_yes()
        LOGGER.info("Step passed: unfriend confirmation Yes tapped.")
    except Exception as exc:
        LOGGER.exception("Tap Yes on unfriend confirmation failed: %s", exc)
        raise AssertionError(
            f"Could not tap Yes on unfriend confirmation. Error: {exc}"
        ) from exc


@when("the user taps Cancel on the block confirmation dialog")
def step_tap_block_confirmation_cancel(context):
    LOGGER.info("Step: tap Cancel on block confirmation dialog (btnCancel).")
    try:
        context.communitii_page.tap_block_confirmation_dialog_cancel()
        LOGGER.info("Step passed: block confirmation Cancel tapped.")
    except Exception as exc:
        LOGGER.exception("Block confirmation Cancel failed: %s", exc)
        raise AssertionError(
            f"Could not tap Cancel on block confirmation dialog. Error: {exc}"
        ) from exc


@then("the blocked chat conversation should show unblock option")
def step_verify_blocked_chat_shows_unblock(context):
    LOGGER.info("Step: verify blocked chat shows blocked-by text and Unblock.")
    try:
        context.communitii_page.verify_blocked_chat_conversation_shows_unblock()
        LOGGER.info("Step passed: blocked chat Unblock option verified.")
    except Exception as exc:
        LOGGER.exception("Blocked chat verification failed: %s", exc)
        raise AssertionError(
            f"Blocked chat conversation did not show unblock UI. Error: {exc}"
        ) from exc


@when("the user taps Unblock on the blocked chat conversation")
def step_tap_unblock_on_blocked_chat(context):
    LOGGER.info("Step: tap Unblock on blocked chat conversation (btnUnblock).")
    try:
        context.communitii_page.tap_unblock_on_blocked_chat_conversation()
        LOGGER.info("Step passed: chat Unblock tapped.")
    except Exception as exc:
        LOGGER.exception("Tap Unblock on blocked chat failed: %s", exc)
        raise AssertionError(
            f"Could not tap Unblock on blocked chat conversation. Error: {exc}"
        ) from exc


@then("the blocked user should be listed on the Blocked users screen")
def step_verify_blocked_user_listed(context):
    LOGGER.info(
        "Step: verify at least one blocked user appears on Blocked users screen (any name)."
    )
    try:
        context.communitii_page.verify_blocked_user_listed_on_blocked_users_screen()
        LOGGER.info("Step passed: blocked user listed on Blocked users screen.")
    except Exception as exc:
        LOGGER.exception("Blocked user list verification failed: %s", exc)
        raise AssertionError(
            f"Blocked user was not listed on Blocked users screen. Error: {exc}"
        ) from exc


@when("the user taps the blocked user profile on the Blocked users screen")
def step_tap_blocked_user_profile_on_list(context):
    LOGGER.info("Step: tap blocked user profile row on Blocked users screen.")
    try:
        context.communitii_page.tap_blocked_user_profile_row_at_position(1)
        LOGGER.info("Step passed: blocked user profile row tapped.")
    except Exception as exc:
        LOGGER.exception("Tap blocked user profile row failed: %s", exc)
        raise AssertionError(
            f"Could not tap blocked user profile on Blocked users screen. Error: {exc}"
        ) from exc


@when("the user taps the Unblock button on the Blocked users screen")
def step_tap_unblock_on_blocked_users_screen(context):
    LOGGER.info("Step: tap Unblock button on Blocked users screen (btnUnblock).")
    try:
        context.communitii_page.tap_unblock_button_on_blocked_users_screen()
        LOGGER.info("Step passed: Unblock button tapped on Blocked users screen.")
    except Exception as exc:
        LOGGER.exception("Tap Unblock on Blocked users screen failed: %s", exc)
        raise AssertionError(
            f"Could not tap Unblock on Blocked users screen. Error: {exc}"
        ) from exc


@then('the blocked user should be listed on the Blocked users screen for "{name}"')
def step_verify_blocked_user_listed_for_name(context, name):
    LOGGER.info("Step: verify blocked user %r on Blocked users screen.", name)
    try:
        context.communitii_page.verify_blocked_user_listed_on_blocked_users_screen(name)
        LOGGER.info("Step passed: blocked user %r found in list.", name)
    except Exception as exc:
        LOGGER.exception("Blocked user list verification failed: %s", exc)
        raise AssertionError(
            f"Blocked user {name!r} not listed on Blocked users screen. Error: {exc}"
        ) from exc


@then("the Report button on the View Info screen should be disabled")
def step_verify_view_info_report_button_disabled(context):
    LOGGER.info("Step: verify Report is disabled on View Info screen.")
    try:
        context.communitii_page.verify_view_info_report_button_disabled()
        LOGGER.info("Step passed: Report button disabled on View Info screen.")
    except Exception as exc:
        LOGGER.exception("View Info Report disabled verification failed: %s", exc)
        raise AssertionError(
            f"Report button should be disabled on View Info screen. Error: {exc}"
        ) from exc


@when("the user taps Close on the View Info screen")
def step_tap_close_on_view_info_screen(context):
    LOGGER.info("Step: tap Close on View Info screen (fabClose).")
    try:
        context.communitii_page.tap_close_on_user_details_sheet()
        LOGGER.info("Step passed: View Info Close FAB tapped.")
    except Exception as exc:
        LOGGER.exception("Tap Close on View Info failed: %s", exc)
        raise AssertionError(
            f"Could not tap Close on View Info screen. Error: {exc}"
        ) from exc


@then('the View Info screen should display profile and action options for "{name}"')
def step_verify_view_info_screen_for_name(context, name):
    LOGGER.info("Step: verify View Info screen for profile %r.", name)
    try:
        context.communitii_page.verify_view_info_screen(name)
        LOGGER.info("Step passed: View Info screen verified for %r.", name)
    except Exception as exc:
        LOGGER.exception("View Info screen verification failed: %s", exc)
        raise AssertionError(
            f"View Info screen verification failed for {name!r}. Error: {exc}"
        ) from exc


@when("the user sends a random chat message")
def step_send_random_chat_message(context):
    LOGGER.info("Step: type and send a random chat message.")
    try:
        sent_text = context.communitii_page.type_and_send_random_chat_message()
        context.last_chat_message_sent = sent_text
        LOGGER.info("Step passed: random chat message sent (%r).", sent_text)
    except Exception as exc:
        LOGGER.exception("Send random chat message failed: %s", exc)
        raise AssertionError(
            f"Could not send random chat message. Error: {exc}"
        ) from exc


@then('the friend chat profile name and status should be displayed for "{name}"')
def step_verify_friend_chat_profile_toolbar_for_name(context, name):
    LOGGER.info("Step: verify friend chat profile toolbar for name %r.", name)
    try:
        context.communitii_page.verify_friend_chat_profile_toolbar(name)
        LOGGER.info("Step passed: chat profile verified for %r.", name)
    except Exception as exc:
        LOGGER.exception("Friend chat profile verification failed: %s", exc)
        raise AssertionError(
            f"Friend chat profile verification failed for {name!r}. Error: {exc}"
        ) from exc


@then("the invite friend add icon should be visible")
def step_verify_invite_friend_add_icon_visible(context):
    LOGGER.info("Step: verify invite friend add icon is visible.")
    try:
        context.communitii_page.verify_invite_friend_add_icon_visible()
        LOGGER.info("Step passed: invite friend add icon verified.")
    except Exception as exc:
        LOGGER.exception("Invite friend add icon verification failed: %s", exc)
        raise AssertionError(
            f"Invite friend add icon was not visible. Error: {exc}"
        ) from exc
