import logging

from behave import then, when

LOGGER = logging.getLogger("cubii_studio_steps")


@when("the user opens the Cubii Studio tab")
def step_open_cubii_studio_tab(context):
    LOGGER.info("Step: open Cubii Studio tab.")
    try:
        context.cubii_studio_page.open_cubii_studio_tab()
        LOGGER.info("Step passed: Cubii Studio tab opened.")
    except Exception as exc:
        LOGGER.exception("Open Cubii Studio tab failed: %s", exc)
        raise AssertionError(f"Could not open Cubii Studio tab. Error: {exc}") from exc


@when("the user taps any visible video card on the Studio screen")
def step_tap_any_studio_video_card(context):
    LOGGER.info("Step: tap any visible video/category card on Studio screen.")
    try:
        context.cubii_studio_page.tap_any_visible_video_card_on_studio_screen()
        LOGGER.info("Step passed: Studio video/category card tapped.")
    except Exception as exc:
        LOGGER.exception("Studio video card tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap a video card on the Studio screen. Error: {exc}"
        ) from exc


@then("the user click on the search bar")
def step_tap_studio_search_bar(context):
    LOGGER.info("Step: tap Studio search bar.")
    try:
        context.cubii_studio_page.tap_studio_search_bar()
        LOGGER.info("Step passed: Studio search bar tapped.")
    except Exception as exc:
        LOGGER.exception("Studio search bar tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Studio search bar. Error: {exc}"
        ) from exc


@then('the user add the valid data with text "{search_text}"')
def step_enter_studio_search_text(context, search_text):
    LOGGER.info("Step: enter Studio search text.")
    try:
        context.cubii_studio_page.enter_studio_search_text(search_text)
        LOGGER.info("Step passed: search text entered.")
    except Exception as exc:
        LOGGER.exception("Studio search text entry failed: %s", exc)
        raise AssertionError(
            f"Could not enter search text in the Studio search bar. Error: {exc}"
        ) from exc


@then("the user click on the search video")
def step_tap_search_result_video(context):
    LOGGER.info("Step: tap search result video in rvSearchList.")
    try:
        context.cubii_studio_page.tap_search_result_video()
        LOGGER.info("Step passed: search result video tapped.")
    except Exception as exc:
        LOGGER.exception("Search result tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the search result video. Error: {exc}"
        ) from exc


@then("the user click on the search cancel button")
def step_tap_search_cancel_button(context):
    LOGGER.info("Step: tap search cancel (ivSearchCancel).")
    try:
        context.cubii_studio_page.tap_search_cancel_button()
        LOGGER.info("Step passed: search cancel tapped.")
    except Exception as exc:
        LOGGER.exception("Search cancel tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the search cancel button. Error: {exc}"
        ) from exc


@then("the user add the invalid video name")
def step_enter_invalid_studio_search_text(context):
    LOGGER.info("Step: enter invalid Studio search text.")
    try:
        context.cubii_studio_page.enter_studio_search_invalid_text(None)
        LOGGER.info("Step passed: invalid search text entered.")
    except Exception as exc:
        LOGGER.exception("Invalid Studio search text entry failed: %s", exc)
        raise AssertionError(
            f"Could not enter invalid search text. Error: {exc}"
        ) from exc


@then('the user add the invalid video name with text "{search_text}"')
def step_enter_invalid_studio_search_text_explicit(context, search_text):
    LOGGER.info("Step: enter invalid Studio search text (explicit).")
    try:
        context.cubii_studio_page.enter_studio_search_invalid_text(search_text)
        LOGGER.info("Step passed: invalid search text entered.")
    except Exception as exc:
        LOGGER.exception("Invalid Studio search text entry failed: %s", exc)
        raise AssertionError(
            f"Could not enter invalid search text. Error: {exc}"
        ) from exc


@then("the user verify the search no results empty state")
def step_verify_search_no_results_empty(context):
    LOGGER.info("Step: verify search no-results empty state.")
    try:
        context.cubii_studio_page.verify_search_no_results_empty_state()
        LOGGER.info("Step passed: no-results empty state verified.")
    except Exception as exc:
        LOGGER.exception("No-results empty state verification failed: %s", exc)
        raise AssertionError(
            f"No-results empty state verification failed. Error: {exc}"
        ) from exc


@then("the user add the valid data in the Studio search bar")
def step_enter_default_studio_search_text(context):
    LOGGER.info("Step: enter default valid Studio search text.")
    try:
        context.cubii_studio_page.enter_studio_search_text(None)
        LOGGER.info("Step passed: default search text entered.")
    except Exception as exc:
        LOGGER.exception("Studio search text entry failed: %s", exc)
        raise AssertionError(
            f"Could not enter search text in the Studio search bar. Error: {exc}"
        ) from exc


@when("the user taps any visible video in the Studio category list")
def step_tap_any_studio_video(context):
    LOGGER.info("Step: tap any visible video in Studio category list.")
    try:
        context.cubii_studio_page.tap_any_visible_video_in_category_list()
        LOGGER.info("Step passed: Studio category video tapped.")
    except Exception as exc:
        LOGGER.exception("Studio category video tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap a video in the Studio category list. Error: {exc}"
        ) from exc


@then(
    "the video detail screen should show scroll view title duration bookmark "
    "equipment and music played cards"
)
def step_verify_video_detail_screen(context):
    LOGGER.info("Step: verify Studio video detail screen.")
    try:
        context.cubii_studio_page.verify_video_detail_screen()
        LOGGER.info("Step passed: Studio video detail screen verified.")
    except Exception as exc:
        LOGGER.exception("Studio video detail verification failed: %s", exc)
        raise AssertionError(
            f"Video detail screen verification failed. Error: {exc}"
        ) from exc


@then(
    "the video player should show start time end time title fullscreen and play controls"
)
def step_verify_video_player_controls(context):
    LOGGER.info("Step: verify Studio video player controls.")
    try:
        context.cubii_studio_page.verify_video_player_controls()
        LOGGER.info("Step passed: Studio video player controls verified.")
    except Exception as exc:
        LOGGER.exception("Studio video player controls verification failed: %s", exc)
        raise AssertionError(
            f"Video player controls verification failed. Error: {exc}"
        ) from exc


@when("the user taps the Full Screen button on the video player")
def step_tap_full_screen_button(context):
    LOGGER.info("Step: tap Full Screen on video player.")
    try:
        context.cubii_studio_page.tap_full_screen_button()
        LOGGER.info("Step passed: Full Screen tapped.")
    except Exception as exc:
        LOGGER.exception("Full Screen tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Full Screen on the video player. Error: {exc}"
        ) from exc


@then("the video player should be in full screen mode")
def step_verify_video_full_screen_mode(context):
    LOGGER.info("Step: verify video player full screen mode.")
    try:
        context.cubii_studio_page.verify_video_player_full_screen_mode()
        LOGGER.info("Step passed: full screen mode verified.")
    except Exception as exc:
        LOGGER.exception("Full screen mode verification failed: %s", exc)
        raise AssertionError(
            f"Video player is not in full screen mode. Error: {exc}"
        ) from exc


@when("the user taps the Exit Full Screen button on the video player")
def step_tap_exit_full_screen_button(context):
    LOGGER.info("Step: tap Exit Full Screen on video player.")
    try:
        context.cubii_studio_page.tap_exit_full_screen_button()
        LOGGER.info("Step passed: Exit Full Screen tapped.")
    except Exception as exc:
        LOGGER.exception("Exit Full Screen tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap Exit Full Screen on the video player. Error: {exc}"
        ) from exc


@then("the Full Screen button should be displayed on the video player")
def step_verify_full_screen_button_displayed(context):
    LOGGER.info("Step: verify Full Screen button is displayed.")
    try:
        context.cubii_studio_page.verify_full_screen_button_displayed()
        LOGGER.info("Step passed: Full Screen button displayed.")
    except Exception as exc:
        LOGGER.exception("Full Screen button display verification failed: %s", exc)
        raise AssertionError(
            f"Full Screen button is not displayed on the video player. Error: {exc}"
        ) from exc


@when("the user pauses the video on the video player")
def step_pause_video_on_player(context):
    LOGGER.info("Step: pause video on player (topLayout).")
    try:
        context.cubii_studio_page.pause_video_on_player()
        LOGGER.info("Step passed: video paused.")
    except Exception as exc:
        LOGGER.exception("Pause video failed: %s", exc)
        raise AssertionError(
            f"Could not pause the video on the video player. Error: {exc}"
        ) from exc


@then("the user click on the back button")
def step_click_back_button(context):
    LOGGER.info("Step: tap back button (Navigate up).")
    try:
        context.cubii_studio_page.tap_back_button()
        LOGGER.info("Step passed: back button tapped.")
    except Exception as exc:
        LOGGER.exception("Back button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the back button (Navigate up). Error: {exc}"
        ) from exc


@then("the user click on video screen back button")
def step_click_video_screen_back_button(context):
    LOGGER.info("Step: tap video screen back button (Navigate up).")
    try:
        context.cubii_studio_page.tap_video_screen_back_button()
        LOGGER.info("Step passed: video screen back button tapped.")
    except Exception as exc:
        LOGGER.exception("Video screen back button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the video screen back button (Navigate up). Error: {exc}"
        ) from exc


@then("the user verifies a category video card and bookmarks it on the category screen")
def step_verify_and_bookmark_category_video_card(context):
    LOGGER.info("Step: verify category video card and bookmark on category screen.")
    try:
        context.cubii_studio_page.verify_and_bookmark_category_video_card()
        LOGGER.info("Step passed: category card verified and bookmarked.")
    except Exception as exc:
        LOGGER.exception("Verify and bookmark category card failed: %s", exc)
        raise AssertionError(
            f"Could not verify and bookmark the category video card. Error: {exc}"
        ) from exc


@when("the user opens the same bookmarked video from the category list")
def step_open_same_bookmarked_category_video(context):
    LOGGER.info("Step: open the same bookmarked video from category list.")
    try:
        context.cubii_studio_page.open_stored_category_video_card()
        LOGGER.info("Step passed: same bookmarked video opened.")
    except Exception as exc:
        LOGGER.exception("Open same bookmarked video failed: %s", exc)
        raise AssertionError(
            f"Could not open the bookmarked video from the category list. Error: {exc}"
        ) from exc


@when("the user click on bookmark the video on the Studio category screen")
def step_bookmark_video_on_studio_category_screen(context):
    LOGGER.info("Step: bookmark video on Studio category screen if not already bookmarked.")
    try:
        context.cubii_studio_page.tap_bookmark_on_studio_category_screen()
        LOGGER.info("Step passed: Studio category bookmark handled.")
    except Exception as exc:
        LOGGER.exception("Studio category bookmark failed: %s", exc)
        raise AssertionError(
            f"Could not bookmark the video on the Studio category screen. Error: {exc}"
        ) from exc


@when("the user taps the bookmark option on the video detail screen")
def step_tap_bookmark_option(context):
    LOGGER.info("Step: bookmark video if not already bookmarked.")
    try:
        context.cubii_studio_page.tap_bookmark_option()
        LOGGER.info("Step passed: bookmark state handled (tap skipped or bookmark applied).")
    except Exception as exc:
        LOGGER.exception("Bookmark option step failed: %s", exc)
        raise AssertionError(
            f"Could not bookmark the video on the detail screen. Error: {exc}"
        ) from exc


@then("the bookmark button should display Bookmarked text")
def step_verify_bookmarked_text(context):
    LOGGER.info("Step: verify Bookmarked text on bookmark button.")
    try:
        context.cubii_studio_page.verify_bookmarked_button_text()
        LOGGER.info("Step passed: Bookmarked text verified.")
    except Exception as exc:
        LOGGER.exception("Bookmarked text verification failed: %s", exc)
        raise AssertionError(
            f"Bookmark button did not display Bookmarked text. Error: {exc}"
        ) from exc


@then("the user scroll down to identify the My Library section")
def step_scroll_to_my_library(context):
    LOGGER.info("Step: scroll to My Library section.")
    try:
        context.cubii_studio_page.scroll_to_my_library_section()
        LOGGER.info("Step passed: My Library section identified.")
    except Exception as exc:
        LOGGER.exception("Scroll to My Library failed: %s", exc)
        raise AssertionError(
            f"Could not find My Library section after scrolling. Error: {exc}"
        ) from exc


@then('the user verifies the "{category}" category is visible on Studio')
def step_verify_studio_category_on_home(context, category):
    LOGGER.info("Step: verify category %r on Studio home.", category)
    try:
        context.cubii_studio_page.verify_studio_category_visible_on_home(category)
        LOGGER.info("Step passed: category %r visible.", category)
    except Exception as exc:
        LOGGER.exception("Category visibility check failed for %r: %s", category, exc)
        raise AssertionError(
            f"Category {category!r} not found on Studio. Error: {exc}"
        ) from exc


@then("the user verifies the Class Collections category is visible on Studio")
def step_verify_class_collections_on_studio(context):
    step_verify_studio_category_on_home(context, "Class Collections")


@when('the user taps View All for "{category}" on the Studio screen')
def step_tap_view_all_for_category(context, category):
    LOGGER.info("Step: tap View All for category %r.", category)
    try:
        context.cubii_studio_page.tap_view_all_for_category_on_studio_home(category)
        LOGGER.info("Step passed: View All tapped for %r.", category)
    except Exception as exc:
        LOGGER.exception("View All tap failed for %r: %s", category, exc)
        raise AssertionError(
            f"Could not tap View All for {category!r}. Error: {exc}"
        ) from exc


@when("the user taps View All for Class Collections on the Studio screen")
def step_tap_view_all_class_collections(context):
    step_tap_view_all_for_category(context, "Class Collections")


@then("the Studio category video list should be visible")
def step_verify_studio_category_video_list(context):
    LOGGER.info("Step: verify Studio category video list (rvCategoryVideos).")
    try:
        context.cubii_studio_page.verify_studio_category_video_list_visible()
        LOGGER.info("Step passed: category video list visible.")
    except Exception as exc:
        LOGGER.exception("Category video list verification failed: %s", exc)
        raise AssertionError(
            f"Category video list not visible after View All. Error: {exc}"
        ) from exc


@then("the user verify all the video list")
def step_verify_all_video_list(context):
    LOGGER.info("Step: verify all videos in collections list with full scroll.")
    try:
        context.cubii_studio_page.verify_all_video_list_with_full_scroll()
        LOGGER.info("Step passed: full collections video list verified.")
    except Exception as exc:
        LOGGER.exception("Full video list verification failed: %s", exc)
        raise AssertionError(
            f"Could not verify the full video list. Error: {exc}"
        ) from exc


@then("the user click on the bookmarks option")
def step_click_bookmarks_option(context):
    LOGGER.info("Step: tap bookmarks option (savedVideosBtn).")
    try:
        context.cubii_studio_page.tap_bookmarks_option()
        LOGGER.info("Step passed: bookmarks option tapped.")
    except Exception as exc:
        LOGGER.exception("Bookmarks option tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the bookmarks option. Error: {exc}"
        ) from exc


@then("the user verify the empty saved videos screen")
def step_verify_empty_saved_videos_screen(context):
    LOGGER.info("Step: verify empty saved videos screen.")
    try:
        context.cubii_studio_page.verify_empty_saved_videos_screen()
        LOGGER.info("Step passed: empty saved videos screen verified.")
    except Exception as exc:
        LOGGER.exception("Empty saved videos screen verification failed: %s", exc)
        raise AssertionError(
            f"Empty saved videos screen verification failed. Error: {exc}"
        ) from exc


@then("the user click on the explore video button")
def step_tap_explore_videos_button(context):
    LOGGER.info("Step: tap Explore Videos button (btnExploreVideos).")
    try:
        context.cubii_studio_page.tap_explore_videos_button()
        LOGGER.info("Step passed: Explore Videos button tapped.")
    except Exception as exc:
        LOGGER.exception("Explore Videos button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the Explore Videos button. Error: {exc}"
        ) from exc


@then("the user verify the bookmarked videos")
def step_verify_bookmarked_videos(context):
    LOGGER.info("Step: verify bookmarked videos screen.")
    try:
        context.cubii_studio_page.verify_bookmarked_videos_screen()
        LOGGER.info("Step passed: bookmarked videos verified.")
    except Exception as exc:
        LOGGER.exception("Bookmarked videos verification failed: %s", exc)
        raise AssertionError(
            f"Bookmarked videos verification failed. Error: {exc}"
        ) from exc


@then("the user click on unbookmark the video")
def step_unbookmark_video_on_saved_list(context):
    LOGGER.info("Step: unbookmark video on saved videos screen.")
    try:
        context.cubii_studio_page.tap_unbookmark_video_on_saved_list()
        LOGGER.info("Step passed: unbookmark handled.")
    except Exception as exc:
        LOGGER.exception("Unbookmark video failed: %s", exc)
        raise AssertionError(
            f"Could not unbookmark the video on the saved videos screen. Error: {exc}"
        ) from exc


@then("the user verify that video removed from saved list")
def step_verify_video_removed_from_saved_list(context):
    LOGGER.info("Step: verify unbookmarked video removed from saved list.")
    try:
        context.cubii_studio_page.verify_unbookmarked_video_removed()
        LOGGER.info("Step passed: video removal verified.")
    except Exception as exc:
        LOGGER.exception("Video removal verification failed: %s", exc)
        raise AssertionError(
            f"Video removal verification failed. Error: {exc}"
        ) from exc


@then("the user click on the back button on the saved videos screen")
def step_click_saved_videos_back_button(context):
    LOGGER.info("Step: tap back button on saved videos screen (Navigate up).")
    try:
        context.cubii_studio_page.tap_saved_videos_back_button()
        LOGGER.info("Step passed: saved videos back button tapped.")
    except Exception as exc:
        LOGGER.exception("Saved videos back button tap failed: %s", exc)
        raise AssertionError(
            f"Could not tap the back button on the saved videos screen. Error: {exc}"
        ) from exc
