import logging
import os

from behave import then, when


LOGGER = logging.getLogger("cubii_community_steps")


@when("the user opens the Communitii tab")
def step_open_communitii_tab(context):
    LOGGER.info("Step: open Communitii tab.")
    try:
        context.communitii_page.open_communitii_tab()
        LOGGER.info("Step passed: Communitii tab opened.")
    except Exception as exc:
        LOGGER.exception("Open Communitii tab failed: %s", exc)
        raise AssertionError(f"Could not open Communitii tab. Error: {exc}") from exc


@then(
    "the Community main screen should show Groups, Friends, Explore Groups, "
    "My Groups, and Create Group"
)
def step_verify_community_main_screen(context):
    LOGGER.info("Step: verify Community main screen elements.")
    try:
        context.communitii_page.verify_communitii_main_screen()
        LOGGER.info("Step passed: Community main screen verified.")
    except Exception as exc:
        LOGGER.exception("Community main screen verification failed: %s", exc)
        raise AssertionError(f"Community screen verification failed. Error: {exc}") from exc


@when("the user taps the Create Group button")
def step_tap_create_group_button(context):
    LOGGER.info("Step: tap CREATE GROUP on community main.")
    try:
        context.communitii_page.tap_create_group_button()
        LOGGER.info("Step passed: Create Group tapped.")
    except Exception as exc:
        LOGGER.exception("Create Group button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Create Group button on community main. Error: {exc}"
        ) from exc


@when("the user enters a create group name with special characters")
def step_enter_create_group_name_with_special_characters(context):
    LOGGER.info("Step: enter create group name with special characters.")
    try:
        context.communitii_page.enter_create_group_name_with_special_characters()
        LOGGER.info("Step passed: invalid special-character group name entered.")
    except Exception as exc:
        LOGGER.exception("Create group special-character name entry failed: %s", exc)
        raise AssertionError(
            f"Could not enter create group name with special characters. Error: {exc}"
        ) from exc


@when("the user enters a create group name and description")
def step_enter_create_group_name_and_description(context):
    LOGGER.info("Step: enter valid create group name and description (no special characters).")
    try:
        context.communitii_page.enter_create_group_name_and_description()
        LOGGER.info("Step passed: create group name and description entered.")
    except Exception as exc:
        LOGGER.exception("Create group name/description entry failed: %s", exc)
        raise AssertionError(
            f"Could not enter create group name and description. Error: {exc}"
        ) from exc


@when("the user turns on the Make the group public switch")
def step_turn_on_create_group_public_switch(context):
    LOGGER.info("Step: turn on Make the group public (switchCompat7).")
    try:
        context.communitii_page.turn_on_create_group_public_switch()
        LOGGER.info("Step passed: public switch on.")
    except Exception as exc:
        LOGGER.exception("Public switch failed: %s", exc)
        raise AssertionError(
            f"Could not turn on Make the group public switch. Error: {exc}"
        ) from exc


@when("the user turns on the Allow members to add more friends switch")
def step_turn_on_create_group_allow_add_friends_switch(context):
    LOGGER.info("Step: turn on Allow members to add more friends (switchCompat8).")
    try:
        context.communitii_page.turn_on_create_group_allow_members_add_friends_switch()
        LOGGER.info("Step passed: allow add friends switch on.")
    except Exception as exc:
        LOGGER.exception("Allow add friends switch failed: %s", exc)
        raise AssertionError(
            f"Could not turn on Allow members to add more friends switch. Error: {exc}"
        ) from exc


@when("the user taps the Invite members button on the create group screen")
def step_tap_create_group_invite_members(context):
    LOGGER.info("Step: tap Invite / add new member on create group screen.")
    try:
        context.communitii_page.tap_create_group_invite_members_button()
        LOGGER.info("Step passed: Invite members button tapped.")
    except Exception as exc:
        LOGGER.exception("Invite members button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Invite members button on create group screen. Error: {exc}"
        ) from exc


@when("the user selects an invite member checkbox if one is shown")
def step_select_invite_member_checkbox_if_shown(context):
    LOGGER.info("Step: tap invite-member radioButton / CheckBox if available.")
    try:
        context.communitii_page.tap_create_group_invite_member_checkbox_if_available()
        LOGGER.info("Step passed: invite member checkbox handled (tap or skip).")
    except Exception as exc:
        LOGGER.exception("Invite member checkbox step failed: %s", exc)
        raise AssertionError(
            f"Invite member checkbox step failed unexpectedly. Error: {exc}"
        ) from exc


@when("the user taps the Done button on the create group screen")
def step_tap_create_group_done(context):
    LOGGER.info("Step: tap Done (btn_done) on create group flow.")
    try:
        context.communitii_page.tap_create_group_done_button()
        LOGGER.info("Step passed: Done tapped.")
    except Exception as exc:
        LOGGER.exception("Create group Done tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Done on create group screen. Error: {exc}"
        ) from exc


@when("the user scrolls down and taps the Create button on the create group screen")
def step_scroll_and_tap_create_group_submit(context):
    LOGGER.info("Step: scroll create group screen and tap CREATE (btn_create).")
    try:
        context.communitii_page.scroll_down_and_tap_create_group_submit_button()
        LOGGER.info("Step passed: CREATE tapped.")
    except Exception as exc:
        LOGGER.exception("Create group CREATE tap failed: %s", exc)
        raise AssertionError(
            f"Could not scroll to and tap Create on create group screen. Error: {exc}"
        ) from exc


@then("the create group screen should show the group name error message")
def step_verify_create_group_name_error_message(context):
    LOGGER.info("Step: verify textinput_error (Enter group name).")
    try:
        context.communitii_page.verify_create_group_missing_name_error_message()
        LOGGER.info("Step passed: group name validation error visible.")
    except Exception as exc:
        LOGGER.exception("Create group name error verification failed: %s", exc)
        raise AssertionError(
            f"Expected create group name error message was not shown. Error: {exc}"
        ) from exc


@then("the create group screen should show the special character error message")
def step_verify_create_group_special_character_error_message(context):
    LOGGER.info("Step: verify textinput_error for special characters in group name.")
    try:
        context.communitii_page.verify_create_group_special_character_error_message()
        LOGGER.info("Step passed: special character validation error visible.")
    except Exception as exc:
        LOGGER.exception("Create group special-character error verification failed: %s", exc)
        raise AssertionError(
            f"Expected special character error on create group screen was not shown. Error: {exc}"
        ) from exc


@then("the created group should be visible after scrolling on the community screen")
def step_verify_created_group_visible_after_scroll(context):
    LOGGER.info("Step: scroll community Groups list and verify created group name.")
    try:
        context.communitii_page.scroll_community_main_and_verify_created_group_name_visible()
        LOGGER.info("Step passed: created group name visible.")
    except Exception as exc:
        LOGGER.exception("Created group visibility check failed: %s", exc)
        raise AssertionError(
            f"Created group was not visible after scrolling. Error: {exc}"
        ) from exc


@when("the user taps the Groups segment on the community main screen")
def step_tap_groups_segment_on_community_main(context):
    LOGGER.info("Step: tap Groups segment (sb_my_group).")
    try:
        context.communitii_page.tap_groups_segment_on_community_main()
        LOGGER.info("Step passed: Groups segment tapped.")
    except Exception as exc:
        LOGGER.exception("Groups segment tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Groups segment on community main screen. Error: {exc}"
        ) from exc


@when("the user taps a random visible joined group card")
def step_tap_random_joined_group_card(context):
    LOGGER.info("Step: tap random visible joined group under rv_chiirgroup.")
    try:
        context.communitii_page.tap_random_visible_joined_group_card()
        LOGGER.info("Step passed: joined group card tapped.")
    except Exception as exc:
        LOGGER.exception("Joined group card tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap a joined group card on the list. Error: {exc}"
        ) from exc


@when("the user taps the Explore Groups banner and waits for the explore list")
def step_tap_explore_groups_banner_wait_list(context):
    LOGGER.info("Step: tap Explore Groups banner and wait for explore RecyclerView.")
    try:
        context.communitii_page.tap_explore_groups_banner_and_wait_for_list()
        LOGGER.info("Step passed: Explore list visible after banner tap.")
    except Exception as exc:
        LOGGER.exception("Explore Groups banner / list wait failed: %s", exc)
        raise AssertionError(
            f"Explore Groups banner tap or list wait failed. Error: {exc}"
        ) from exc


@when("the user taps the first visible join group plus icon on the explore list")
def step_tap_first_visible_join_group_plus_on_explore_list(context):
    LOGGER.info("Step: tap first visible join (+) imageView19 on explore list.")
    try:
        context.communitii_page.tap_first_visible_join_group_plus_on_explore_list()
        LOGGER.info("Step passed: join group plus icon tapped.")
    except Exception as exc:
        LOGGER.exception("Join group plus tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap join group plus icon on explore list. Error: {exc}"
        ) from exc


@when("the user taps the explore groups search field")
def step_tap_explore_groups_search_field(context):
    LOGGER.info("Step: tap Explore Groups search field (editText3).")
    try:
        context.communitii_page.tap_explore_groups_search_field()
        LOGGER.info("Step passed: explore search field tapped.")
    except Exception as exc:
        LOGGER.exception("Explore search field tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap explore groups search field. Error: {exc}"
        ) from exc


@when("the user enters an invalid group name in the explore search field")
def step_enter_invalid_explore_search(context):
    invalid = os.getenv(
        "CUBII_EXPLORE_SEARCH_INVALID_QUERY", "zzzzno_matching_group_qa_999"
    ).strip()
    if not invalid:
        invalid = "zzzzno_matching_group_qa_999"
    LOGGER.info("Step: enter invalid explore search query %r.", invalid)
    try:
        context.communitii_page.enter_explore_groups_search_query(invalid)
        LOGGER.info("Step passed: invalid explore search query entered.")
    except Exception as exc:
        LOGGER.exception("Invalid explore search entry failed: %s", exc)
        raise AssertionError(
            f"Could not enter invalid group name in explore search. Error: {exc}"
        ) from exc


@when("the user enters the valid group name in the explore search field")
def step_enter_valid_explore_search(context):
    valid = (os.getenv("CUBII_EXPLORE_SEARCH_VALID_QUERY", "Over 40") or "Over 40").strip()
    if not valid:
        valid = "Over 40"
    context.explore_search_valid_query = valid
    LOGGER.info("Step: enter valid explore search query %r.", valid)
    try:
        context.communitii_page.enter_explore_groups_search_query(valid)
        LOGGER.info("Step passed: valid explore search query entered.")
    except Exception as exc:
        LOGGER.exception("Valid explore search entry failed: %s", exc)
        raise AssertionError(
            f"Could not enter valid group name in explore search. Error: {exc}"
        ) from exc


@then("the explore search results should show a card matching the valid group search")
def step_verify_explore_search_result_card(context):
    valid = getattr(context, "explore_search_valid_query", None) or (
        os.getenv("CUBII_EXPLORE_SEARCH_VALID_QUERY", "Over 40") or "Over 40"
    ).strip()
    if not valid:
        valid = "Over 40"
    LOGGER.info("Step: verify explore search result contains %r.", valid)
    try:
        context.communitii_page.verify_explore_search_shows_result_card_containing(valid)
        LOGGER.info("Step passed: explore search result card verified.")
    except Exception as exc:
        LOGGER.exception("Explore search result verification failed: %s", exc)
        raise AssertionError(
            f"Explore search should show a card matching {valid!r}. Error: {exc}"
        ) from exc


@when("the user opens a random Explore group card")
def step_open_random_explore_group_card(context):
    LOGGER.info("Step: open a random visible Explore group card.")
    try:
        context.communitii_page.tap_random_visible_explore_group_card()
        LOGGER.info("Step passed: random Explore group card tapped.")
    except Exception as exc:
        LOGGER.exception("Opening random Explore group card failed: %s", exc)
        raise AssertionError(
            f"Could not open a random Explore group card. Error: {exc}"
        ) from exc


@when("the user taps the group details overflow menu")
def step_tap_group_details_overflow_menu(context):
    LOGGER.info("Step: tap group details three-dot menu (imgGroupDetailOptions).")
    try:
        context.communitii_page.tap_group_details_overflow_menu()
        LOGGER.info("Step passed: group details overflow menu tapped.")
    except Exception as exc:
        LOGGER.exception("Group details overflow menu tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap group details overflow menu. Error: {exc}"
        ) from exc


@when("the user taps Leave Group in the overflow menu")
def step_tap_leave_group_in_overflow_menu(context):
    LOGGER.info("Step: tap Leave Group in overflow / sheet.")
    try:
        context.communitii_page.tap_leave_group_in_overflow_menu()
        LOGGER.info("Step passed: Leave Group tapped.")
    except Exception as exc:
        LOGGER.exception("Leave Group menu tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Leave Group in overflow menu. Error: {exc}"
        ) from exc


@when("the user taps No on the leave group confirmation")
def step_tap_leave_group_confirm_no(context):
    LOGGER.info("Step: tap No on leave group confirmation (btn_no).")
    try:
        context.communitii_page.tap_leave_group_confirm_no()
        LOGGER.info("Step passed: leave confirmation No tapped.")
    except Exception as exc:
        LOGGER.exception("Leave group No button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap No on leave group confirmation. Error: {exc}"
        ) from exc


@when("the user taps Yes on the leave group confirmation")
def step_tap_leave_group_confirm_yes(context):
    LOGGER.info("Step: tap Yes on leave group confirmation (btn_yes).")
    try:
        context.communitii_page.tap_leave_group_confirm_yes()
        LOGGER.info("Step passed: leave confirmation Yes tapped.")
    except Exception as exc:
        LOGGER.exception("Leave group Yes button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Yes on leave group confirmation. Error: {exc}"
        ) from exc


@when("the user taps Delete Group in the overflow menu")
def step_tap_delete_group_in_overflow_menu(context):
    LOGGER.info("Step: tap Delete Group in overflow / sheet (textView106).")
    try:
        context.communitii_page.tap_delete_group_in_overflow_menu()
        LOGGER.info("Step passed: Delete Group tapped.")
    except Exception as exc:
        LOGGER.exception("Delete Group menu tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Delete Group in overflow menu. Error: {exc}"
        ) from exc


@when("the user taps No on the delete group confirmation")
def step_tap_delete_group_confirm_no(context):
    LOGGER.info("Step: tap No on delete group confirmation (btn_no).")
    try:
        context.communitii_page.tap_delete_group_confirm_no()
        LOGGER.info("Step passed: delete confirmation No tapped.")
    except Exception as exc:
        LOGGER.exception("Delete group No button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap No on delete group confirmation. Error: {exc}"
        ) from exc


@when("the user taps Yes on the delete group confirmation")
def step_tap_delete_group_confirm_yes(context):
    LOGGER.info("Step: tap Yes on delete group confirmation (btn_yes).")
    try:
        context.communitii_page.tap_delete_group_confirm_yes()
        LOGGER.info("Step passed: delete confirmation Yes tapped.")
    except Exception as exc:
        LOGGER.exception("Delete group Yes button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Yes on delete group confirmation. Error: {exc}"
        ) from exc


@then("the left group should not appear on the community Groups list")
def step_verify_left_group_absent_on_groups_list(context):
    LOGGER.info("Step: verify remembered left group absent under My Groups list.")
    try:
        context.communitii_page.verify_left_group_absent_on_community_groups_list()
        LOGGER.info("Step passed: left group not on community Groups list.")
    except Exception as exc:
        LOGGER.exception("Left group absence verification failed: %s", exc)
        raise AssertionError(
            f"Left group still appears or verification failed. Error: {exc}"
        ) from exc


@then("the deleted group should not appear on the community Groups list")
def step_verify_deleted_group_absent_on_groups_list(context):
    LOGGER.info("Step: verify remembered deleted group absent under Groups list.")
    try:
        context.communitii_page.verify_deleted_group_absent_on_community_groups_list()
        LOGGER.info("Step passed: deleted group not on community Groups list.")
    except Exception as exc:
        LOGGER.exception("Deleted group absence verification failed: %s", exc)
        raise AssertionError(
            f"Deleted group still appears or verification failed. Error: {exc}"
        ) from exc


@when("the user scrolls down on the Groups list and taps the created QA group for delete")
def step_tap_created_qa_group_for_delete(context):
    LOGGER.info("Step: scroll Groups list and tap created QA group for delete flow.")
    try:
        context.communitii_page.scroll_groups_list_and_tap_created_qa_group_for_delete()
        LOGGER.info("Step passed: QA group opened for delete from Groups list.")
    except Exception as exc:
        LOGGER.exception("Tap created QA group for delete failed: %s", exc)
        raise AssertionError(
            "Could not open the created QA group for delete. Run @create_group first. "
            f"Error: {exc}"
        ) from exc


@when("the user scrolls down on the Groups list and taps the created QA group")
@when("the user taps on the created group on the Groups list")
@when("the user taps the joined group card matching the created or configured group name")
def step_tap_joined_group_matching_created_name(context):
    LOGGER.info("Step: scroll Groups list and tap created QA group (last create / env name).")
    try:
        context.communitii_page.scroll_groups_list_and_tap_created_qa_group()
        LOGGER.info("Step passed: created QA group card opened from Groups list.")
    except Exception as exc:
        LOGGER.exception("Tap created QA group on Groups list failed: %s", exc)
        raise AssertionError(
            "Could not scroll and tap the created QA group on the Groups list. Run a "
            f"@create_group scenario first in the same Behave run. Error: {exc}"
        ) from exc


@when("the user taps Edit Group from the group options menu")
def step_tap_edit_group_option(context):
    LOGGER.info("Step: tap Edit Group (txtGrpOptionEditGroupOption).")
    try:
        context.communitii_page.tap_group_details_edit_group_option()
        LOGGER.info("Step passed: Edit Group tapped.")
    except Exception as exc:
        LOGGER.exception("Edit Group tap failed: %s", exc)
        raise AssertionError(f"Could not tap Edit Group. Error: {exc}") from exc


@when("the user updates the edit group name and description")
def step_update_edit_group_name_description(context):
    LOGGER.info("Step: update edit group name and description fields.")
    try:
        context.communitii_page.update_edit_group_name_and_description()
        LOGGER.info("Step passed: edit group name and description updated.")
    except Exception as exc:
        LOGGER.exception("Edit group name/description update failed: %s", exc)
        raise AssertionError(
            f"Could not update edit group name and description. Error: {exc}"
        ) from exc


@when("the user flips the public and allow-friends toggles on the edit group form")
def step_flip_edit_group_toggles(context):
    LOGGER.info("Step: flip switchCompat8 then switchCompat7 on edit form.")
    try:
        context.communitii_page.flip_edit_group_allow_friends_and_public_toggles()
        LOGGER.info("Step passed: edit group toggles flipped.")
    except Exception as exc:
        LOGGER.exception("Edit group toggle flip failed: %s", exc)
        raise AssertionError(
            f"Could not flip edit group toggles. Error: {exc}"
        ) from exc


@when("the user taps the Save button on the edit group form")
def step_tap_edit_group_save(context):
    LOGGER.info("Step: tap Save (btn_create) on edit group form.")
    try:
        context.communitii_page.tap_group_edit_form_save_button()
        LOGGER.info("Step passed: edit group Save tapped.")
    except Exception as exc:
        LOGGER.exception("Edit group Save tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Save on edit group form. Error: {exc}"
        ) from exc


@then("the group details screen should show the edited group name")
def step_verify_group_details_edited_name(context):
    LOGGER.info("Step: verify group details header shows edited name.")
    try:
        context.communitii_page.verify_group_details_reflects_edited_group_name()
        LOGGER.info("Step passed: edited group name visible on details.")
    except Exception as exc:
        LOGGER.exception("Edited group name verification failed: %s", exc)
        raise AssertionError(
            f"Group details did not show the edited name. Error: {exc}"
        ) from exc


@when("the user opens the first Explore group card")
def step_open_first_explore_group_card(context):
    """Backward-compatible: now selects a random visible card (same as random step)."""
    LOGGER.info("Step: open Explore group card (random visible; legacy step wording).")
    try:
        context.communitii_page.tap_random_visible_explore_group_card()
        LOGGER.info("Step passed: Explore group card tapped.")
    except Exception as exc:
        LOGGER.exception("Opening Explore group card failed: %s", exc)
        raise AssertionError(
            f"Could not open first Explore group card. Error: {exc}"
        ) from exc


@then(
    "the group details screen should show name member summary visibility and member list"
)
def step_verify_group_details_screen(context):
    LOGGER.info("Step: verify group details header and member list.")
    try:
        context.communitii_page.verify_group_details_header()
        context.communitii_page.verify_group_member_list_present()
        LOGGER.info("Step passed: group details and member list verified.")
    except Exception as exc:
        LOGGER.exception("Group details verification failed: %s", exc)
        raise AssertionError(f"Group details verification failed. Error: {exc}") from exc


@then("the group member list should show the current user labeled You")
def step_verify_group_member_list_shows_you(context):
    LOGGER.info("Step: verify member list shows current user as You (textView50).")
    try:
        context.communitii_page.verify_group_member_list_shows_current_user_as_you()
        LOGGER.info("Step passed: current user You label visible on member list.")
    except Exception as exc:
        LOGGER.exception("You label verification failed: %s", exc)
        raise AssertionError(
            f"Group member list should show the current user as You. Error: {exc}"
        ) from exc


@then("the group date duration filter card should be visible")
def step_verify_group_date_filter_card(context):
    LOGGER.info("Step: verify group date duration filter card visible.")
    try:
        context.communitii_page.verify_group_date_duration_filter_card_visible()
        LOGGER.info("Step passed: date filter card visible.")
    except Exception as exc:
        LOGGER.exception("Date filter card verification failed: %s", exc)
        raise AssertionError(
            f"Date duration filter card not visible on group details. Error: {exc}"
        ) from exc


@when("the user taps the group date duration filter card")
def step_tap_group_date_filter_card(context):
    LOGGER.info("Step: tap group date duration filter card.")
    try:
        context.communitii_page.tap_group_date_duration_filter_card()
        LOGGER.info("Step passed: date filter card tapped.")
    except Exception as exc:
        LOGGER.exception("Date filter card tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap group date duration filter card. Error: {exc}"
        ) from exc


@when("the user taps the Yesterday option in the date filter")
def step_tap_yesterday_date_filter(context):
    LOGGER.info("Step: tap Yesterday in group date filter.")
    try:
        context.communitii_page.tap_yesterday_option_in_group_date_filter()
        LOGGER.info("Step passed: Yesterday date filter tapped.")
    except Exception as exc:
        LOGGER.exception("Yesterday date filter tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Yesterday in date filter. Error: {exc}"
        ) from exc


@when("the user taps the Last 7 Days option in the date filter")
def step_tap_last_seven_days_date_filter(context):
    LOGGER.info("Step: tap Last 7 Days in group date filter.")
    try:
        context.communitii_page.tap_last_seven_days_option_in_group_date_filter()
        LOGGER.info("Step passed: Last 7 Days date filter tapped.")
    except Exception as exc:
        LOGGER.exception("Last 7 Days date filter tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Last 7 Days in date filter. Error: {exc}"
        ) from exc


@when("the user taps the Last 30 Days option in the date filter")
def step_tap_last_thirty_days_date_filter(context):
    LOGGER.info("Step: tap Last 30 Days in group date filter.")
    try:
        context.communitii_page.tap_last_thirty_days_option_in_group_date_filter()
        LOGGER.info("Step passed: Last 30 Days date filter tapped.")
    except Exception as exc:
        LOGGER.exception("Last 30 Days date filter tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Last 30 Days in date filter. Error: {exc}"
        ) from exc


@when("the user waits for the group member list to refresh after the date filter")
def step_wait_after_date_filter(context):
    LOGGER.info("Step: wait after date filter for list refresh.")
    try:
        context.communitii_page.wait_after_group_date_filter_for_list_refresh()
        LOGGER.info("Step passed: post-filter wait complete.")
    except Exception as exc:
        LOGGER.exception("Post date filter wait failed: %s", exc)
        raise AssertionError(f"Wait after date filter failed. Error: {exc}") from exc


@then("the group member list should show at least one visible user row")
def step_verify_group_member_list_rows(context):
    LOGGER.info("Step: verify group member list has visible rows.")
    try:
        context.communitii_page.verify_group_member_list_present()
        LOGGER.info("Step passed: group member list has visible row(s).")
    except Exception as exc:
        LOGGER.exception("Group member list verification failed: %s", exc)
        raise AssertionError(
            f"Group member list should show at least one visible user row. Error: {exc}"
        ) from exc


@when("the user taps the All Data filter card")
def step_tap_all_data_filter_card(context):
    LOGGER.info("Step: tap All Data filter card (cardTypeOfUser).")
    try:
        context.communitii_page.tap_all_data_filter_user_type_card()
        LOGGER.info("Step passed: All Data filter card tapped.")
    except Exception as exc:
        LOGGER.exception("All Data filter card tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap All Data filter card. Error: {exc}"
        ) from exc


@when("the user taps on the All Data data filter card")
def step_tap_on_all_data_data_filter_card(context):
    """Re-tap user-type / All Data filter (`cardTypeOfUser`) after a selection (opens sheet again)."""
    LOGGER.info("Step: tap on All Data data filter card (cardTypeOfUser).")
    try:
        context.communitii_page.tap_all_data_filter_user_type_card()
        LOGGER.info("Step passed: All Data data filter card tapped.")
    except Exception as exc:
        LOGGER.exception("All Data data filter card tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap on All Data data filter card. Error: {exc}"
        ) from exc


@when("the user taps the ALL DATA option in the All Data filter")
def step_tap_all_data_option_in_sheet(context):
    LOGGER.info("Step: tap ALL DATA option in All Data filter sheet.")
    try:
        context.communitii_page.tap_all_data_sheet_all_data_option()
        LOGGER.info("Step passed: ALL DATA option tapped.")
    except Exception as exc:
        LOGGER.exception("ALL DATA option tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap ALL DATA option in All Data filter. Error: {exc}"
        ) from exc


@when("the user taps the Automated Data option in the All Data filter")
def step_tap_automated_data_option(context):
    LOGGER.info("Step: tap Automated Data in All Data filter.")
    try:
        context.communitii_page.tap_automated_data_option_in_all_data_filter()
        LOGGER.info("Step passed: Automated Data option tapped.")
    except Exception as exc:
        LOGGER.exception("Automated Data option tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Automated Data in All Data filter. Error: {exc}"
        ) from exc


@when("the user taps the Manual Data option in the All Data filter")
def step_tap_manual_data_option(context):
    LOGGER.info("Step: tap Manual Data in All Data filter.")
    try:
        context.communitii_page.tap_manual_data_option_in_all_data_filter()
        LOGGER.info("Step passed: Manual Data option tapped.")
    except Exception as exc:
        LOGGER.exception("Manual Data option tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Manual Data in All Data filter. Error: {exc}"
        ) from exc


@when("the user taps the Both Data option in the All Data filter")
def step_tap_both_data_option(context):
    LOGGER.info("Step: tap Both Data in All Data filter.")
    try:
        context.communitii_page.tap_both_data_option_in_all_data_filter()
        LOGGER.info("Step passed: Both Data option tapped.")
    except Exception as exc:
        LOGGER.exception("Both Data option tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Both Data in All Data filter. Error: {exc}"
        ) from exc


@when("the user waits for the group member list to refresh after the All Data filter")
def step_wait_after_all_data_filter(context):
    LOGGER.info("Step: wait after All Data filter for list refresh.")
    try:
        context.communitii_page.wait_after_all_data_filter_for_list_refresh()
        LOGGER.info("Step passed: post All Data filter wait complete.")
    except Exception as exc:
        LOGGER.exception("Post All Data filter wait failed: %s", exc)
        raise AssertionError(f"Wait after All Data filter failed. Error: {exc}") from exc


@then("the All Data filter card should show the selected Automated Data filter")
def step_verify_all_data_card_selection(context):
    LOGGER.info("Step: verify All Data filter card shows selected label.")
    try:
        context.communitii_page.verify_all_data_filter_card_shows_selected_label()
        LOGGER.info("Step passed: All Data filter card shows expected selection.")
    except Exception as exc:
        LOGGER.exception("All Data filter card label verification failed: %s", exc)
        raise AssertionError(
            f"All Data filter card should show selected filter. Error: {exc}"
        ) from exc


@then("the All Data filter card should show the selected Manual Data filter")
def step_verify_all_data_card_manual_selection(context):
    LOGGER.info("Step: verify All Data filter card shows Manual Data selection.")
    try:
        context.communitii_page.verify_all_data_filter_card_shows_manual_data_label()
        LOGGER.info("Step passed: All Data filter card shows Manual Data selection.")
    except Exception as exc:
        LOGGER.exception("All Data filter card Manual Data verification failed: %s", exc)
        raise AssertionError(
            f"All Data filter card should show Manual Data selection. Error: {exc}"
        ) from exc


@then("the All Data filter card should show the selected Both Data filter")
def step_verify_all_data_card_both_selection(context):
    LOGGER.info("Step: verify All Data filter card shows Both Data selection.")
    try:
        context.communitii_page.verify_all_data_filter_card_shows_both_data_label()
        LOGGER.info("Step passed: All Data filter card shows Both Data selection.")
    except Exception as exc:
        LOGGER.exception("All Data filter card Both Data verification failed: %s", exc)
        raise AssertionError(
            f"All Data filter card should show Both Data selection. Error: {exc}"
        ) from exc


@when("the user taps the group metrics filter card")
def step_tap_group_metrics_filter_card(context):
    LOGGER.info("Step: tap group metrics filter card (cardTypeOfMetric).")
    try:
        context.communitii_page.tap_metrics_filter_card()
        LOGGER.info("Step passed: metrics filter card tapped.")
    except Exception as exc:
        LOGGER.exception("Metrics filter card tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap group metrics filter card. Error: {exc}"
        ) from exc


@when("the user taps the Calories option in the metrics filter")
def step_tap_calories_in_metrics_filter(context):
    LOGGER.info("Step: tap Calories in metrics filter (linearLayout8).")
    try:
        context.communitii_page.tap_calories_option_in_metrics_filter()
        LOGGER.info("Step passed: Calories option tapped.")
    except Exception as exc:
        LOGGER.exception("Calories option tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Calories in metrics filter. Error: {exc}"
        ) from exc


@when("the user taps the Miles option in the metrics filter")
def step_tap_miles_in_metrics_filter(context):
    LOGGER.info("Step: tap Miles in metrics filter (linearLayout9).")
    try:
        context.communitii_page.tap_miles_option_in_metrics_filter()
        LOGGER.info("Step passed: Miles option tapped.")
    except Exception as exc:
        LOGGER.exception("Miles option tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Miles in metrics filter. Error: {exc}"
        ) from exc


@when("the user taps the Strides option in the metrics filter")
def step_tap_strides_in_metrics_filter(context):
    LOGGER.info("Step: tap Strides in metrics filter (linearLayout10).")
    try:
        context.communitii_page.tap_strides_option_in_metrics_filter()
        LOGGER.info("Step passed: Strides option tapped.")
    except Exception as exc:
        LOGGER.exception("Strides option tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Strides in metrics filter. Error: {exc}"
        ) from exc


@when("the user taps the Time option in the metrics filter")
def step_tap_time_in_metrics_filter(context):
    LOGGER.info("Step: tap Time in metrics filter (linearLayout11).")
    try:
        context.communitii_page.tap_time_option_in_metrics_filter()
        LOGGER.info("Step passed: Time option tapped.")
    except Exception as exc:
        LOGGER.exception("Time option tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Time in metrics filter. Error: {exc}"
        ) from exc


@when("the user waits for the group member list to refresh after the metrics filter")
def step_wait_after_metrics_filter(context):
    LOGGER.info("Step: wait after metrics filter for list refresh.")
    try:
        context.communitii_page.wait_after_metrics_filter_for_list_refresh()
        LOGGER.info("Step passed: post metrics filter wait complete.")
    except Exception as exc:
        LOGGER.exception("Post metrics filter wait failed: %s", exc)
        raise AssertionError(f"Wait after metrics filter failed. Error: {exc}") from exc


@then("the metrics filter card should show the selected Calories filter")
def step_verify_metrics_card_calories(context):
    LOGGER.info("Step: verify metrics filter card shows Calories selection.")
    try:
        context.communitii_page.verify_metrics_filter_card_shows_calories_label()
        LOGGER.info("Step passed: metrics filter card shows Calories.")
    except Exception as exc:
        LOGGER.exception("Metrics filter card Calories verification failed: %s", exc)
        raise AssertionError(
            f"Metrics filter card should show Calories selection. Error: {exc}"
        ) from exc


@then("the group member list visible rows should indicate calories")
def step_verify_member_rows_calories(context):
    LOGGER.info("Step: verify visible member rows show calories values.")
    try:
        context.communitii_page.verify_group_member_list_visible_rows_indicate_calories()
        LOGGER.info("Step passed: member rows indicate calories.")
    except Exception as exc:
        LOGGER.exception("Member list calories verification failed: %s", exc)
        raise AssertionError(
            f"Group member list should indicate calories in visible rows. Error: {exc}"
        ) from exc


@then("the metrics filter card should show the selected Miles filter")
def step_verify_metrics_card_miles(context):
    LOGGER.info("Step: verify metrics filter card shows Miles selection.")
    try:
        context.communitii_page.verify_metrics_filter_card_shows_miles_label()
        LOGGER.info("Step passed: metrics filter card shows Miles.")
    except Exception as exc:
        LOGGER.exception("Metrics filter card Miles verification failed: %s", exc)
        raise AssertionError(
            f"Metrics filter card should show Miles selection. Error: {exc}"
        ) from exc


@then("the group member list visible rows should indicate miles")
def step_verify_member_rows_miles(context):
    LOGGER.info("Step: verify visible member rows show miles values.")
    try:
        context.communitii_page.verify_group_member_list_visible_rows_indicate_miles()
        LOGGER.info("Step passed: member rows indicate miles.")
    except Exception as exc:
        LOGGER.exception("Member list miles verification failed: %s", exc)
        raise AssertionError(
            f"Group member list should indicate miles in visible rows. Error: {exc}"
        ) from exc


@then("the metrics filter card should show the selected Strides filter")
def step_verify_metrics_card_strides(context):
    LOGGER.info("Step: verify metrics filter card shows Strides selection.")
    try:
        context.communitii_page.verify_metrics_filter_card_shows_strides_label()
        LOGGER.info("Step passed: metrics filter card shows Strides.")
    except Exception as exc:
        LOGGER.exception("Metrics filter card Strides verification failed: %s", exc)
        raise AssertionError(
            f"Metrics filter card should show Strides selection. Error: {exc}"
        ) from exc


@then("the group member list visible rows should indicate strides")
def step_verify_member_rows_strides(context):
    LOGGER.info("Step: verify visible member rows show strides values.")
    try:
        context.communitii_page.verify_group_member_list_visible_rows_indicate_strides()
        LOGGER.info("Step passed: member rows indicate strides.")
    except Exception as exc:
        LOGGER.exception("Member list strides verification failed: %s", exc)
        raise AssertionError(
            f"Group member list should indicate strides in visible rows. Error: {exc}"
        ) from exc


@then("the metrics filter card should show the selected Time filter")
def step_verify_metrics_card_time(context):
    LOGGER.info("Step: verify metrics filter card shows Time selection.")
    try:
        context.communitii_page.verify_metrics_filter_card_shows_time_label()
        LOGGER.info("Step passed: metrics filter card shows Time.")
    except Exception as exc:
        LOGGER.exception("Metrics filter card Time verification failed: %s", exc)
        raise AssertionError(
            f"Metrics filter card should show Time selection. Error: {exc}"
        ) from exc


@then("the group member list visible rows should indicate time")
def step_verify_member_rows_time(context):
    LOGGER.info("Step: verify visible member rows show time values.")
    try:
        context.communitii_page.verify_group_member_list_visible_rows_indicate_time()
        LOGGER.info("Step passed: member rows indicate time.")
    except Exception as exc:
        LOGGER.exception("Member list time verification failed: %s", exc)
        raise AssertionError(
            f"Group member list should indicate time in visible rows. Error: {exc}"
        ) from exc


@when("the user scrolls the group member list down and back up")
def step_scroll_group_member_list(context):
    LOGGER.info("Step: scroll group member list down then up.")
    try:
        context.communitii_page.scroll_group_details_member_list_down_and_up()
        LOGGER.info("Step passed: group member list scrolled.")
    except Exception as exc:
        LOGGER.exception("Group member list scroll failed: %s", exc)
        raise AssertionError(f"Group member list scroll failed. Error: {exc}") from exc


@when("the user taps any visible group member list card")
def step_tap_any_group_member_card(context):
    LOGGER.info("Step: tap any visible group member row.")
    try:
        context.communitii_page.tap_any_visible_group_member_row()
        LOGGER.info("Step passed: group member row tapped.")
    except Exception as exc:
        LOGGER.exception("Tap group member row failed: %s", exc)
        raise AssertionError(f"Could not tap a group member list card. Error: {exc}") from exc


@then(
    "the user details sheet should show card name View Profile Report Block and Add Friend"
)
def step_verify_user_details_sheet(context):
    LOGGER.info("Step: verify member user details sheet.")
    try:
        context.communitii_page.verify_member_user_details_sheet()
        LOGGER.info("Step passed: user details sheet verified.")
    except Exception as exc:
        LOGGER.exception("User details sheet verification failed: %s", exc)
        raise AssertionError(f"User details verification failed. Error: {exc}") from exc


@when("the user taps View Profile on the user details sheet")
def step_tap_view_profile_on_user_details_sheet(context):
    LOGGER.info("Step: tap View Profile on member user details sheet.")
    try:
        context.communitii_page.tap_view_profile_on_user_details_sheet()
        LOGGER.info("Step passed: View Profile tapped.")
    except Exception as exc:
        LOGGER.exception("View Profile tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap View Profile on user details sheet. Error: {exc}"
        ) from exc


@then("the viewed member profile screen should show profile image name and badges")
def step_verify_viewed_member_profile_screen(context):
    LOGGER.info(
        "Step: verify viewed member profile (image, name, badges; Focus/Interests if present)."
    )
    try:
        context.communitii_page.verify_viewed_member_profile_screen_shows_profile_details()
        LOGGER.info("Step passed: viewed member profile details verified.")
    except Exception as exc:
        LOGGER.exception("Viewed member profile verification failed: %s", exc)
        raise AssertionError(
            "Viewed member profile should show image, name, and badges. "
            f"Error: {exc}"
        ) from exc


@when("the user taps the back button on the viewed member profile screen")
def step_tap_viewed_member_profile_back(context):
    LOGGER.info("Step: tap back on viewed member profile (iv_back).")
    try:
        context.communitii_page.tap_viewed_member_profile_screen_back_button()
        LOGGER.info("Step passed: viewed member profile back tapped.")
    except Exception as exc:
        LOGGER.exception("Viewed member profile back tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap back on viewed member profile screen. Error: {exc}"
        ) from exc


@then("the Report button on the user details sheet should be disabled")
def step_verify_user_details_report_disabled(context):
    LOGGER.info("Step: verify Report is disabled on user details sheet.")
    try:
        context.communitii_page.verify_user_details_report_button_disabled()
        LOGGER.info("Step passed: Report button disabled.")
    except Exception as exc:
        LOGGER.exception("Report disabled verification failed: %s", exc)
        raise AssertionError(
            f"Report button should be disabled on user details sheet. Error: {exc}"
        ) from exc


@when("the user taps the Report button on the user details sheet")
def step_tap_report_on_user_details_sheet(context):
    LOGGER.info("Step: tap Report on user details sheet.")
    try:
        context.communitii_page.tap_report_on_user_details_sheet()
        LOGGER.info("Step passed: Report tapped.")
    except Exception as exc:
        LOGGER.exception("Report tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Report on user details sheet. Error: {exc}"
        ) from exc


@when("the user enters the report subject and description for reporting")
def step_enter_report_subject_and_description(context):
    LOGGER.info("Step: enter report form subject and description.")
    subject = os.getenv("CUBII_REPORT_FORM_SUBJECT", "QA automated report subject")
    description = os.getenv(
        "CUBII_REPORT_FORM_DESCRIPTION",
        "QA automated report description body.",
    )
    try:
        context.communitii_page.enter_report_form_subject_and_description(
            subject, description
        )
        LOGGER.info("Step passed: report subject and description entered.")
    except Exception as exc:
        LOGGER.exception("Report form subject/description failed: %s", exc)
        raise AssertionError(
            f"Could not enter report subject and description. Error: {exc}"
        ) from exc


@when("the user taps the REPORT button on the report form")
def step_tap_report_form_report_button(context):
    LOGGER.info("Step: tap REPORT on report form.")
    try:
        context.communitii_page.tap_report_form_report_submit_button()
        LOGGER.info("Step passed: REPORT button on report form tapped.")
    except Exception as exc:
        LOGGER.exception("Report form REPORT tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap REPORT on report form. Error: {exc}"
        ) from exc


@when("the user taps the cancel button on the user details sheet")
def step_tap_user_details_cancel_close(context):
    """Close FAB (`fabClose`); product labels it Close in accessibility."""
    LOGGER.info("Step: tap cancel/Close on user details sheet.")
    try:
        context.communitii_page.tap_close_on_user_details_sheet()
        LOGGER.info("Step passed: user details Close FAB tapped.")
    except Exception as exc:
        LOGGER.exception("User details Close tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap cancel/Close on user details sheet. Error: {exc}"
        ) from exc


@when("the user taps the Add Friend button on the user details sheet")
def step_tap_add_friend_on_user_details(context):
    LOGGER.info("Step: tap Add Friend on user details sheet.")
    try:
        context.communitii_page.tap_add_friend_on_user_details_sheet()
        LOGGER.info("Step passed: Add Friend tapped.")
    except Exception as exc:
        LOGGER.exception("Add Friend tap failed: %s", exc)
        raise AssertionError(f"Could not tap Add Friend. Error: {exc}") from exc


@when("the user taps Block on the user details sheet")
def step_tap_block_on_user_details(context):
    LOGGER.info("Step: tap Block on user details sheet.")
    try:
        context.communitii_page.tap_block_on_user_details_sheet()
        LOGGER.info("Step passed: Block tapped.")
    except Exception as exc:
        LOGGER.exception("Block tap failed: %s", exc)
        raise AssertionError(f"Could not tap Block on user details sheet. Error: {exc}") from exc


@when("the user confirms block in the dialog if shown")
def step_confirm_block_dialog(context):
    LOGGER.info("Step: confirm Block dialog if present.")
    try:
        context.communitii_page.tap_block_confirmation_if_present()
        LOGGER.info("Step passed: block confirmation handled.")
    except Exception as exc:
        LOGGER.exception("Block confirmation failed: %s", exc)
        raise AssertionError(f"Block confirmation step failed. Error: {exc}") from exc


@when("the user taps Navigate up")
def step_tap_navigate_up(context):
    LOGGER.info("Step: tap Navigate up.")
    try:
        context.communitii_page.tap_navigate_up()
        LOGGER.info("Step passed: Navigate up tapped.")
    except Exception as exc:
        LOGGER.exception("Navigate up failed: %s", exc)
        raise AssertionError(f"Could not tap Navigate up. Error: {exc}") from exc


@when("the user taps the toolbar back control")
def step_tap_toolbar_back(context):
    LOGGER.info("Step: tap toolbar back LinearLayout.")
    try:
        context.communitii_page.tap_toolbar_back_linear_layout()
        LOGGER.info("Step passed: toolbar back tapped.")
    except Exception as exc:
        LOGGER.exception("Toolbar back failed: %s", exc)
        raise AssertionError(f"Could not tap toolbar back. Error: {exc}") from exc


@when("the user taps the Explore Groups screen back button")
def step_tap_explore_groups_screen_back(context):
    LOGGER.info("Step: tap Explore Groups tvBackButton.")
    try:
        context.communitii_page.tap_explore_groups_screen_back_button()
        LOGGER.info("Step passed: Explore Groups screen back tapped.")
    except Exception as exc:
        LOGGER.exception("Explore Groups screen back failed: %s", exc)
        raise AssertionError(
            f"Could not tap Explore Groups screen back (tvBackButton). Error: {exc}"
        ) from exc


@when("the user opens the More menu on the toolbar")
def step_open_more_menu(context):
    LOGGER.info("Step: open More menu.")
    try:
        context.communitii_page.tap_toolbar_more_menu()
        LOGGER.info("Step passed: More menu opened.")
    except Exception as exc:
        LOGGER.exception("More menu failed: %s", exc)
        raise AssertionError(f"Could not open More menu. Error: {exc}") from exc


@when("the user taps Blocked users in the menu")
def step_tap_blocked_users_menu(context):
    LOGGER.info("Step: tap Blocked users menu option.")
    try:
        context.communitii_page.tap_blocked_users_menu_option()
        LOGGER.info("Step passed: Blocked users option tapped.")
    except Exception as exc:
        LOGGER.exception("Blocked users menu tap failed: %s", exc)
        raise AssertionError(f"Could not tap Blocked users. Error: {exc}") from exc


@then("the Blocked users screen should show the users list")
def step_verify_blocked_users_list(context):
    LOGGER.info("Step: verify Blocked users list.")
    try:
        context.communitii_page.verify_blocked_users_list_visible()
        LOGGER.info("Step passed: Blocked users list visible.")
    except Exception as exc:
        LOGGER.exception("Blocked users list verification failed: %s", exc)
        raise AssertionError(f"Blocked users list verification failed. Error: {exc}") from exc


@when("the user taps unblock on the blocked user at list position {position:d}")
def step_tap_blocked_user_unblock_at_position(context, position):
    LOGGER.info("Step: tap UNBLOCK on blocked user row position %s.", position)
    try:
        context.communitii_page.tap_blocked_users_list_unblock_at_position(position)
        LOGGER.info("Step passed: UNBLOCK tapped at position %s.", position)
    except Exception as exc:
        LOGGER.exception("Tap UNBLOCK on blocked user row failed: %s", exc)
        raise AssertionError(
            f"Could not tap UNBLOCK at list position {position}. Error: {exc}"
        ) from exc


@when("the user taps Cancel on the unblock confirmation dialog")
def step_tap_unblock_dialog_cancel(context):
    LOGGER.info("Step: tap Cancel on unblock confirmation dialog.")
    try:
        context.communitii_page.tap_unblock_user_dialog_cancel()
        LOGGER.info("Step passed: unblock dialog Cancel tapped.")
    except Exception as exc:
        LOGGER.exception("Unblock dialog Cancel failed: %s", exc)
        raise AssertionError(f"Could not tap Cancel on unblock dialog. Error: {exc}") from exc


@when("the user taps Unblock on the unblock confirmation dialog")
def step_tap_unblock_dialog_confirm(context):
    LOGGER.info("Step: tap UNBLOCK on unblock confirmation dialog.")
    try:
        context.communitii_page.tap_unblock_user_dialog_confirm()
        LOGGER.info("Step passed: unblock dialog UNBLOCK tapped.")
    except Exception as exc:
        LOGGER.exception("Unblock dialog UNBLOCK failed: %s", exc)
        raise AssertionError(
            f"Could not tap UNBLOCK on unblock dialog. Error: {exc}"
        ) from exc


@when("the user taps the back button")
def step_tap_ll_back(context):
    LOGGER.info("Step: tap llBack screen back LinearLayout.")
    try:
        context.communitii_page.tap_ll_back_button()
        LOGGER.info("Step passed: llBack back tapped.")
    except Exception as exc:
        LOGGER.exception("llBack tap failed: %s", exc)
        raise AssertionError(f"Could not tap back (`llBack`). Error: {exc}") from exc
