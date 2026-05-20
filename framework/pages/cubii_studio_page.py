import logging
import os
import random
import re
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage
from framework.pages.non_ble_connection import NonBleConnectionPage


class CubiiStudioPage(BasePage):
    """Cubii Studio bottom-nav tab, category browsing, and video detail screen."""

    LOGGER = logging.getLogger("cubii_studio_page")

    STUDIO_TAB_CANDIDATE_LOCATORS = (
        (AppiumBy.ACCESSIBILITY_ID, "Cubii Studio"),
        (AppiumBy.ID, "com.cubii:id/navigation_studio"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.cubii:id/navigation_studio")',
        ),
        (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Cubii Studio"]'),
    )

    STUDIO_SEARCH_BAR_ID = "com.cubii:id/studio_search_bar"
    STUDIO_SEARCH_BAR_XPATH = (
        '//android.widget.EditText[@resource-id="com.cubii:id/studio_search_bar"]'
    )
    STUDIO_SEARCH_BAR_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/studio_search_bar")'
    )
    STUDIO_SEARCH_BAR_LOCATORS = (
        (AppiumBy.ID, STUDIO_SEARCH_BAR_ID),
        (AppiumBy.XPATH, STUDIO_SEARCH_BAR_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, STUDIO_SEARCH_BAR_UIAUTOMATOR),
    )
    DEFAULT_STUDIO_SEARCH_VALID_TEXT = "10-Min Grip and Go with Anne"

    RV_SEARCH_LIST_ID = "com.cubii:id/rvSearchList"
    RV_SEARCH_LIST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvSearchList"]'
    )
    RV_SEARCH_LIST_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/rvSearchList")'
    RV_SEARCH_LIST_LOCATORS = (
        (AppiumBy.ID, RV_SEARCH_LIST_ID),
        (AppiumBy.XPATH, RV_SEARCH_LIST_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, RV_SEARCH_LIST_UIAUTOMATOR),
    )
    SEARCH_RESULT_ROW_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvSearchList"]'
        "/android.view.ViewGroup/android.view.ViewGroup"
    )
    SEARCH_RESULT_TITLE_ID = "com.cubii:id/tvTitle"
    SEARCH_RESULT_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/tvTitle"]'
    )
    SEARCH_RESULT_TITLE_IN_RV_SEARCH_LIST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvSearchList"]'
        '//android.widget.TextView[@resource-id="com.cubii:id/tvTitle"]'
    )
    SEARCH_RESULT_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/tvTitle")'
    )
    SEARCH_RESULT_TITLE_LOCATORS = (
        (AppiumBy.ID, SEARCH_RESULT_TITLE_ID),
        (AppiumBy.XPATH, SEARCH_RESULT_TITLE_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, SEARCH_RESULT_TITLE_UIAUTOMATOR),
    )
    SEARCH_RESULT_VIEWGROUP_FALLBACK_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(3)'
    )

    SEARCH_CANCEL_ID = "com.cubii:id/ivSearchCancel"
    SEARCH_CANCEL_XPATH = (
        '//android.widget.ImageView[@resource-id="com.cubii:id/ivSearchCancel"]'
    )
    SEARCH_CANCEL_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/ivSearchCancel")'
    SEARCH_CANCEL_LOCATORS = (
        (AppiumBy.ID, SEARCH_CANCEL_ID),
        (AppiumBy.XPATH, SEARCH_CANCEL_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, SEARCH_CANCEL_UIAUTOMATOR),
    )

    NO_RESULTS_FOUND_TEXT_UIAUTOMATOR = 'new UiSelector().text("No results found")'
    NO_RESULTS_FOUND_TEXT_XPATH = '//android.widget.TextView[@text="No results found"]'
    NO_RESULTS_FOUND_LOCATORS = (
        (AppiumBy.ANDROID_UIAUTOMATOR, NO_RESULTS_FOUND_TEXT_UIAUTOMATOR),
        (AppiumBy.XPATH, NO_RESULTS_FOUND_TEXT_XPATH),
    )

    SEARCH_EMPTY_MESSAGE_ID = "com.cubii:id/txtEmptyMessage"
    SEARCH_EMPTY_MESSAGE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtEmptyMessage"]'
    )
    SEARCH_EMPTY_MESSAGE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtEmptyMessage")'
    )
    SEARCH_EMPTY_MESSAGE_LOCATORS = (
        (AppiumBy.ID, SEARCH_EMPTY_MESSAGE_ID),
        (AppiumBy.XPATH, SEARCH_EMPTY_MESSAGE_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, SEARCH_EMPTY_MESSAGE_UIAUTOMATOR),
    )

    FAB_EMPTY_ICON_ID = "com.cubii:id/fabEmptyIconIndicator"
    FAB_EMPTY_ICON_ACCESSIBILITY_ID = "It's empty here!"
    FAB_EMPTY_ICON_XPATH = (
        '//com.google.android.material.floatingactionbutton.FloatingActionButton'
        '[@resource-id="com.cubii:id/fabEmptyIconIndicator"]'
    )
    FAB_EMPTY_ICON_XPATH_CONTENT_DESC = (
        '//com.google.android.material.floatingactionbutton.FloatingActionButton'
        '[@content-desc="It\'s empty here!"]'
    )
    FAB_EMPTY_ICON_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/fabEmptyIconIndicator")'
    )
    FAB_EMPTY_ICON_LOCATORS = (
        (AppiumBy.ID, FAB_EMPTY_ICON_ID),
        (AppiumBy.ACCESSIBILITY_ID, FAB_EMPTY_ICON_ACCESSIBILITY_ID),
        (AppiumBy.XPATH, FAB_EMPTY_ICON_XPATH),
        (AppiumBy.XPATH, FAB_EMPTY_ICON_XPATH_CONTENT_DESC),
        (AppiumBy.ANDROID_UIAUTOMATOR, FAB_EMPTY_ICON_UIAUTOMATOR),
    )

    DEFAULT_STUDIO_SEARCH_INVALID_TEXT = "zzzNoResultsInvalidStudio999"

    RV_CATEGORIES_ID = "com.cubii:id/rvCategories"
    RV_CATEGORIES_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvCategories"]'
    )
    RV_CATEGORIES_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/rvCategories")'
    RV_CATEGORIES_CATEGORY_CARD_REL_XPATH = "./android.view.ViewGroup"
    RV_CATEGORIES_CATEGORY_CARD_FALLBACK_XPATH = (
        "//androidx.recyclerview.widget.RecyclerView"
        '[@resource-id="com.cubii:id/rvCategories"]/android.view.ViewGroup[3]'
    )
    RV_CATEGORIES_CATEGORY_CARD_FALLBACK_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(12)'
    )

    RV_CATEGORY_ITEMS_ID = "com.cubii:id/rvCategoryItems"
    RV_CATEGORY_ITEMS_XPATH_TMPL = (
        '(//android.widget.GridView[@resource-id="com.cubii:id/rvCategoryItems"])[{index}]'
    )
    RV_CATEGORY_ITEMS_UIAUTOMATOR_TMPL = (
        'new UiSelector().resourceId("com.cubii:id/rvCategoryItems").instance({instance})'
    )
    RV_CATEGORY_ITEMS_GRID_CHILD_REL_XPATH = ".//*[@clickable='true']"

    RV_CATEGORY_VIDEOS_ID = "com.cubii:id/rvCategoryVideos"
    RV_CATEGORY_VIDEOS_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvCategoryVideos"]'
    )
    RV_CATEGORY_VIDEOS_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/rvCategoryVideos")'
    )
    RV_CATEGORY_VIDEOS_ROW_REL_XPATH = "./android.view.ViewGroup"
    RV_CATEGORY_VIDEOS_FIRST_ROW_XPATH = (
        "//androidx.recyclerview.widget.RecyclerView"
        '[@resource-id="com.cubii:id/rvCategoryVideos"]/android.view.ViewGroup[1]'
    )
    RV_CATEGORY_VIDEOS_FIRST_ROW_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(2)'
    )

    VIDEOS_LAYOUT_ID = "com.cubii:id/videosLayout"
    CATEGORY_VIDEO_CARD_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/videosLayout"]'
        "/android.widget.RelativeLayout/android.view.ViewGroup"
    )
    CATEGORY_VIDEO_CARD_XPATH_IN_LIST = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvCategoryVideos"]'
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/videosLayout"]'
        "/android.widget.RelativeLayout/android.view.ViewGroup"
    )
    CATEGORY_VIDEO_CARD_XPATH_FIRST = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/videosLayout"])[1]'
        "/android.widget.RelativeLayout/android.view.ViewGroup"
    )
    CATEGORY_VIDEO_CARD_UIAUTOMATOR_TMPL = (
        'new UiSelector().className("android.view.ViewGroup").instance({instance})'
    )
    CATEGORY_VIDEO_CARD_FALLBACK_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(3)'
    )

    TXT_CATEGORY_TITLE_ID = "com.cubii:id/txtCategoryTitle"
    TXT_VIEW_ALL_TITLE_ID = "com.cubii:id/txtViewAllTitle"

    STUDIO_VIEW_ALL_CATEGORIES = (
        "Class Collections",
        "Choose by Class Format",
        "Choose by Class Length",
        "Choose by Instructor",
        "Choose by Class Functionality",
    )

    RV_COLLECTIONS_LIST_ID = "com.cubii:id/rvCollectionsList"
    RV_COLLECTIONS_LIST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView'
        '[@resource-id="com.cubii:id/rvCollectionsList"]'
    )
    RV_COLLECTIONS_LIST_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/rvCollectionsList")'
    )
    RV_COLLECTIONS_LIST_LOCATORS = (
        (AppiumBy.ID, RV_COLLECTIONS_LIST_ID),
        (AppiumBy.XPATH, RV_COLLECTIONS_LIST_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, RV_COLLECTIONS_LIST_UIAUTOMATOR),
    )
    COLLECTIONS_VIDEO_TITLE_IN_LIST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvCollectionsList"]'
        '//android.widget.TextView[@resource-id="com.cubii:id/txtVideoTitle"]'
    )
    COLLECTIONS_VIDEO_CARD_IN_LIST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvCollectionsList"]'
        f'//android.widget.FrameLayout[@resource-id="{VIDEOS_LAYOUT_ID}"]'
    )
    COLLECTIONS_LIST_ROW_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvCollectionsList"]'
        "/android.view.ViewGroup"
    )
    COLLECTIONS_LIST_CHILD_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvCollectionsList"]/*'
    )
    COLLECTIONS_LIST_TEXT_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvCollectionsList"]'
        '//android.widget.TextView[@text!=""]'
    )
    COLLECTIONS_LIST_SKIP_LABELS = frozenset(
        {
            "",
            "View All",
            "My Library",
            "Saved Videos",
            "Explore Videos",
        }
    ) | frozenset(STUDIO_VIEW_ALL_CATEGORIES)

    VIDEO_DETAILS_SCROLL_ID = "com.cubii:id/nsvVideoDetails"
    VIDEO_DETAILS_SCROLL_XPATH = (
        '//android.widget.ScrollView[@resource-id="com.cubii:id/nsvVideoDetails"]'
    )
    VIDEO_DETAILS_SCROLL_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/nsvVideoDetails")'
    )

    VIDEO_TITLE_LAYOUT_ID = "com.cubii:id/linLayoutVideoTitle"
    VIDEO_TITLE_LAYOUT_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/linLayoutVideoTitle"]'
    )
    VIDEO_TITLE_LAYOUT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/linLayoutVideoTitle")'
    )
    VIDEO_DETAIL_TITLE_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/linLayoutVideoTitle"]'
        '//android.widget.TextView[@resource-id="com.cubii:id/txtVideoTitle"]'
    )
    VIDEO_DETAIL_TITLE_IN_SCROLL_XPATH = (
        '//android.widget.ScrollView[@resource-id="com.cubii:id/nsvVideoDetails"]'
        '//android.widget.TextView[@resource-id="com.cubii:id/txtVideoTitle"]'
    )
    VIDEO_DURATION_ID = "com.cubii:id/txtDuration"
    VIDEO_DURATION_XPATH = '//android.widget.TextView[@resource-id="com.cubii:id/txtDuration"]'
    VIDEO_DURATION_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtDuration")'

    VIDEO_BOOKMARK_LAYOUT_ID = "com.cubii:id/linLayoutBookmarkOption"
    VIDEO_BOOKMARK_LAYOUT_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/linLayoutBookmarkOption"]'
    )
    VIDEO_BOOKMARK_LAYOUT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/linLayoutBookmarkOption")'
    )
    VIDEO_BOOKMARK_LAYOUT_LOCATORS = (
        (AppiumBy.ID, VIDEO_BOOKMARK_LAYOUT_ID),
        (AppiumBy.XPATH, VIDEO_BOOKMARK_LAYOUT_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, VIDEO_BOOKMARK_LAYOUT_UIAUTOMATOR),
    )

    BOOKMARKED_TEXT_UIAUTOMATOR = 'new UiSelector().text("Bookmarked")'
    BOOKMARKED_TEXT_XPATH = '//android.widget.TextView[@text="Bookmarked"]'
    BOOKMARKED_TEXT_LOCATORS = (
        (AppiumBy.ANDROID_UIAUTOMATOR, BOOKMARKED_TEXT_UIAUTOMATOR),
        (AppiumBy.XPATH, BOOKMARKED_TEXT_XPATH),
    )
    BOOKMARKED_TEXT_IN_LAYOUT_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/linLayoutBookmarkOption"]'
        '//android.widget.TextView[@text="Bookmarked"]'
    )

    BOOKMARK_TEXT_UIAUTOMATOR = 'new UiSelector().text("Bookmark")'
    BOOKMARK_TEXT_XPATH = '//android.widget.TextView[@text="Bookmark"]'
    BOOKMARK_TEXT_IN_LAYOUT_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/linLayoutBookmarkOption"]'
        '//android.widget.TextView[@text="Bookmark"]'
    )

    STUDIO_CARD_BOOKMARK_ICON_ID = "com.cubii:id/imgBookmarkIcon"
    STUDIO_CARD_BOOKMARK_ICON_XPATH = (
        '//android.widget.ImageView[@content-desc="Bookmarks"]'
    )
    STUDIO_CARD_BOOKMARK_ICON_XPATH_FIRST = (
        '(//android.widget.ImageView[@content-desc="Bookmarks"])[1]'
    )
    STUDIO_CARD_BOOKMARK_ICON_UIAUTOMATOR_TMPL = (
        'new UiSelector().resourceId("com.cubii:id/imgBookmarkIcon").instance({instance})'
    )
    STUDIO_CARD_BOOKMARK_ICON_LOCATORS = (
        (AppiumBy.ID, STUDIO_CARD_BOOKMARK_ICON_ID),
        (AppiumBy.XPATH, STUDIO_CARD_BOOKMARK_ICON_XPATH_FIRST),
        (AppiumBy.XPATH, STUDIO_CARD_BOOKMARK_ICON_XPATH),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            STUDIO_CARD_BOOKMARK_ICON_UIAUTOMATOR_TMPL.format(instance=0),
        ),
    )

    VIDEO_DETAIL_BOOKMARK_ICON_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/imgBookmarkIcon").instance(0)'
    )
    VIDEO_DETAIL_BOOKMARK_ICON_XPATH = (
        '(//android.widget.ImageView[@content-desc="Bookmarks"])[1]'
    )
    VIDEO_DETAIL_BOOKMARK_ICON_LOCATORS = (
        (AppiumBy.ANDROID_UIAUTOMATOR, VIDEO_DETAIL_BOOKMARK_ICON_UIAUTOMATOR),
        (AppiumBy.XPATH, VIDEO_DETAIL_BOOKMARK_ICON_XPATH),
    )

    SAVED_LIST_UNBOOKMARK_ICON_LOCATORS = (
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            STUDIO_CARD_BOOKMARK_ICON_UIAUTOMATOR_TMPL.format(instance=0),
        ),
        (AppiumBy.XPATH, STUDIO_CARD_BOOKMARK_ICON_XPATH_FIRST),
        (AppiumBy.ID, STUDIO_CARD_BOOKMARK_ICON_ID),
        (AppiumBy.XPATH, STUDIO_CARD_BOOKMARK_ICON_XPATH),
    )

    MY_LIBRARY_TEXT_ID = "com.cubii:id/my_library_text"
    MY_LIBRARY_TEXT_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/my_library_text"]'
    )
    MY_LIBRARY_TEXT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/my_library_text")'
    )
    MY_LIBRARY_TEXT_LOCATORS = (
        (AppiumBy.ID, MY_LIBRARY_TEXT_ID),
        (AppiumBy.XPATH, MY_LIBRARY_TEXT_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, MY_LIBRARY_TEXT_UIAUTOMATOR),
    )

    SAVED_VIDEOS_BTN_ID = "com.cubii:id/savedVideosBtn"
    SAVED_VIDEOS_BTN_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/savedVideosBtn"]'
    )
    SAVED_VIDEOS_BTN_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/savedVideosBtn")'
    )
    SAVED_VIDEOS_BTN_LOCATORS = (
        (AppiumBy.ID, SAVED_VIDEOS_BTN_ID),
        (AppiumBy.XPATH, SAVED_VIDEOS_BTN_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, SAVED_VIDEOS_BTN_UIAUTOMATOR),
    )

    SAVED_VIDEOS_TOOLBAR_TITLE_ID = "com.cubii:id/toolbar_title"
    SAVED_VIDEOS_TOOLBAR_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title"]'
    )
    SAVED_VIDEOS_TOOLBAR_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/toolbar_title")'
    )
    SAVED_VIDEOS_TOOLBAR_TITLE_LOCATORS = (
        (AppiumBy.ID, SAVED_VIDEOS_TOOLBAR_TITLE_ID),
        (AppiumBy.XPATH, SAVED_VIDEOS_TOOLBAR_TITLE_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, SAVED_VIDEOS_TOOLBAR_TITLE_UIAUTOMATOR),
    )

    EMPTY_SAVED_ICON_CARD_ID = "com.cubii:id/emptyIconCard"
    EMPTY_SAVED_ICON_CARD_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/emptyIconCard"]'
    )
    EMPTY_SAVED_ICON_CARD_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/emptyIconCard")'
    )
    EMPTY_SAVED_ICON_CARD_LOCATORS = (
        (AppiumBy.ID, EMPTY_SAVED_ICON_CARD_ID),
        (AppiumBy.XPATH, EMPTY_SAVED_ICON_CARD_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, EMPTY_SAVED_ICON_CARD_UIAUTOMATOR),
    )

    NO_VIDEOS_TEXT_ID = "com.cubii:id/txtNoVideos"
    NO_VIDEOS_TEXT_XPATH = '//android.widget.TextView[@resource-id="com.cubii:id/txtNoVideos"]'
    NO_VIDEOS_TEXT_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtNoVideos")'
    NO_VIDEOS_TEXT_LOCATORS = (
        (AppiumBy.ID, NO_VIDEOS_TEXT_ID),
        (AppiumBy.XPATH, NO_VIDEOS_TEXT_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, NO_VIDEOS_TEXT_UIAUTOMATOR),
    )
    NO_VIDEOS_LABEL = "No Videos"

    NO_VIDEOS_DESCRIPTION_ID = "com.cubii:id/txtNoVideosDescription"
    NO_VIDEOS_DESCRIPTION_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtNoVideosDescription"]'
    )
    NO_VIDEOS_DESCRIPTION_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtNoVideosDescription")'
    )
    NO_VIDEOS_DESCRIPTION_LOCATORS = (
        (AppiumBy.ID, NO_VIDEOS_DESCRIPTION_ID),
        (AppiumBy.XPATH, NO_VIDEOS_DESCRIPTION_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, NO_VIDEOS_DESCRIPTION_UIAUTOMATOR),
    )
    NO_VIDEOS_DESCRIPTION_TEXT = "Your saved Cubii Studio Classes will appear here"

    EXPLORE_VIDEOS_BTN_ID = "com.cubii:id/btnExploreVideos"
    EXPLORE_VIDEOS_BTN_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnExploreVideos"]'
    )
    EXPLORE_VIDEOS_BTN_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnExploreVideos")'
    )
    EXPLORE_VIDEOS_BTN_LOCATORS = (
        (AppiumBy.ID, EXPLORE_VIDEOS_BTN_ID),
        (AppiumBy.XPATH, EXPLORE_VIDEOS_BTN_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, EXPLORE_VIDEOS_BTN_UIAUTOMATOR),
    )
    EXPLORE_VIDEOS_BTN_TEXT = "EXPLORE VIDEOS"

    RV_SAVED_VIDEOS_ID = "com.cubii:id/rv_saved_videos"
    RV_SAVED_VIDEOS_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_saved_videos"]'
    )
    RV_SAVED_VIDEOS_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/rv_saved_videos")'
    )
    RV_SAVED_VIDEOS_LOCATORS = (
        (AppiumBy.ID, RV_SAVED_VIDEOS_ID),
        (AppiumBy.CLASS_NAME, "androidx.recyclerview.widget.RecyclerView"),
        (AppiumBy.XPATH, RV_SAVED_VIDEOS_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, RV_SAVED_VIDEOS_UIAUTOMATOR),
    )

    SAVED_VIDEO_TITLE_ID = "com.cubii:id/txtVideoTitle"
    SAVED_VIDEO_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtVideoTitle"]'
    )
    SAVED_VIDEO_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtVideoTitle")'
    )
    SAVED_VIDEO_TITLE_LOCATORS = (
        (AppiumBy.ID, SAVED_VIDEO_TITLE_ID),
        (AppiumBy.XPATH, SAVED_VIDEO_TITLE_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, SAVED_VIDEO_TITLE_UIAUTOMATOR),
    )
    SAVED_VIDEO_TITLE_IN_LIST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_saved_videos"]'
        '//android.widget.TextView[@resource-id="com.cubii:id/txtVideoTitle"]'
    )

    CARD_EQUIPMENT_ID = "com.cubii:id/cardEquipment"
    CARD_EQUIPMENT_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardEquipment"]'
        "/android.widget.LinearLayout"
    )
    CARD_EQUIPMENT_UIAUTOMATOR = (
        'new UiSelector().className("android.widget.LinearLayout").instance(5)'
    )

    CARD_MUSIC_PLAYED_ID = "com.cubii:id/cardMusicPlayed"
    CARD_MUSIC_PLAYED_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardMusicPlayed"]'
        "/android.widget.LinearLayout"
    )
    CARD_MUSIC_PLAYED_UIAUTOMATOR = (
        'new UiSelector().className("android.widget.LinearLayout").instance(4)'
    )

    EXO_POSITION_ID = "com.cubii:id/exo_position"
    EXO_POSITION_XPATH = '//android.widget.TextView[@resource-id="com.cubii:id/exo_position"]'
    EXO_POSITION_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/exo_position")'

    EXO_TOTAL_DURATION_ID = "com.cubii:id/txtExoPlayerTotalDuration"
    EXO_TOTAL_DURATION_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtExoPlayerTotalDuration"]'
    )
    EXO_TOTAL_DURATION_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtExoPlayerTotalDuration")'
    )

    FULL_SCREEN_BTN_ID = "com.cubii:id/imgBtnFullScreen"
    FULL_SCREEN_BTN_XPATH = '//android.widget.ImageButton[@content-desc="Full Screen"]'
    FULL_SCREEN_BTN_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/imgBtnFullScreen")'
    FULL_SCREEN_BTN_LOCATORS = (
        (AppiumBy.ACCESSIBILITY_ID, "Full Screen"),
        (AppiumBy.ID, FULL_SCREEN_BTN_ID),
        (AppiumBy.XPATH, FULL_SCREEN_BTN_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, FULL_SCREEN_BTN_UIAUTOMATOR),
    )

    EXIT_FULL_SCREEN_BTN_ID = "com.cubii:id/imgBtnExitFullScreen"
    EXIT_FULL_SCREEN_BTN_XPATH = (
        '//android.widget.ImageButton[@content-desc="Exit Full Screen"]'
    )
    EXIT_FULL_SCREEN_BTN_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/imgBtnExitFullScreen")'
    )
    EXIT_FULL_SCREEN_BTN_LOCATORS = (
        (AppiumBy.ACCESSIBILITY_ID, "Exit Full Screen"),
        (AppiumBy.ID, EXIT_FULL_SCREEN_BTN_ID),
        (AppiumBy.XPATH, EXIT_FULL_SCREEN_BTN_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, EXIT_FULL_SCREEN_BTN_UIAUTOMATOR),
    )

    TOP_LAYOUT_ID = "com.cubii:id/topLayout"
    TOP_LAYOUT_XPATH = '//android.view.ViewGroup[@resource-id="com.cubii:id/topLayout"]'
    TOP_LAYOUT_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/topLayout")'
    TOP_LAYOUT_LOCATORS = (
        (AppiumBy.ID, TOP_LAYOUT_ID),
        (AppiumBy.XPATH, TOP_LAYOUT_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, TOP_LAYOUT_UIAUTOMATOR),
    )

    EXO_PLAY_PAUSE_ID = "com.cubii:id/exo_play_pause"
    EXO_PLAY_PAUSE_PLAY_XPATH = '//android.widget.ImageView[@content-desc="Play"]'
    EXO_PLAY_PAUSE_PAUSE_XPATH = '//android.widget.ImageView[@content-desc="Pause"]'
    EXO_PLAY_PAUSE_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/exo_play_pause")'
    EXO_PLAY_PAUSE_PLAY_LOCATORS = (
        (AppiumBy.ACCESSIBILITY_ID, "Play"),
        (AppiumBy.XPATH, EXO_PLAY_PAUSE_PLAY_XPATH),
        (AppiumBy.ID, EXO_PLAY_PAUSE_ID),
        (AppiumBy.ANDROID_UIAUTOMATOR, EXO_PLAY_PAUSE_UIAUTOMATOR),
    )

    TOOLBAR_VIDEO_TITLE_ID = "com.cubii:id/txtToolbarTitle"
    TOOLBAR_VIDEO_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtToolbarTitle"]'
    )
    TOOLBAR_VIDEO_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtToolbarTitle")'
    )

    NAVIGATE_UP_ACCESSIBILITY_ID = "Navigate up"
    NAVIGATE_UP_XPATH = '//android.widget.ImageButton[@content-desc="Navigate up"]'
    NAVIGATE_UP_UIAUTOMATOR = 'new UiSelector().description("Navigate up")'
    NAVIGATE_UP_LOCATORS = (
        (AppiumBy.ACCESSIBILITY_ID, NAVIGATE_UP_ACCESSIBILITY_ID),
        (AppiumBy.XPATH, NAVIGATE_UP_XPATH),
        (AppiumBy.ANDROID_UIAUTOMATOR, NAVIGATE_UP_UIAUTOMATOR),
    )

    def __init__(self, driver, non_ble_page: NonBleConnectionPage):
        super().__init__(driver)
        self._non_ble = non_ble_page
        self._last_bookmarked_video_title = ""
        self._selected_category_video_title = ""

    def _wait_sec(self, env_key: str, default: int | None = None) -> int:
        default = default if default is not None else Settings.EXPLICIT_WAIT
        return int(os.getenv(env_key, str(default)))

    @staticmethod
    def _uiautomator_escape(text: str) -> str:
        """Escape double quotes for UiAutomator text/description selectors."""
        return (text or "").replace('"', '\\"')

    @classmethod
    def _category_title_locators(cls, category_name: str) -> tuple[tuple, ...]:
        """Locators for a Studio home category row title (txtCategoryTitle)."""
        title = (category_name or "").strip()
        xpath = (
            '//android.widget.TextView[@resource-id="com.cubii:id/txtCategoryTitle" '
            f'and @text="{title}"]'
        )
        uia = f'new UiSelector().text("{cls._uiautomator_escape(title)}")'
        return (
            (AppiumBy.XPATH, xpath),
            (AppiumBy.ANDROID_UIAUTOMATOR, uia),
        )

    @classmethod
    def _view_all_locators_for_category(cls, category_name: str) -> tuple[tuple, ...]:
        """Locators for View All (txtViewAllTitle) on the row matching category_name."""
        title = (category_name or "").strip()
        title_xpath = (
            '//android.widget.TextView[@resource-id="com.cubii:id/txtCategoryTitle" '
            f'and @text="{title}"]'
        )
        view_all_id = cls.TXT_VIEW_ALL_TITLE_ID
        xpaths = (
            (
                f"{title_xpath}/following-sibling::android.widget.TextView"
                f'[@resource-id="{view_all_id}"]'
            ),
            (
                f"{title_xpath}/parent::*/android.widget.TextView"
                f'[@resource-id="{view_all_id}"]'
            ),
            (
                f"{title_xpath}/ancestor::*[1]//android.widget.TextView"
                f'[@resource-id="{view_all_id}"][1]'
            ),
            (
                f"{title_xpath}/ancestor::*[2]//android.widget.TextView"
                f'[@resource-id="{view_all_id}"][1]'
            ),
        )
        locators: list[tuple] = [(AppiumBy.XPATH, xp) for xp in xpaths]
        locators.append((AppiumBy.ID, view_all_id))
        return tuple(locators)

    def _pause_after_tap(self, env_key: str, default: str = "0.8") -> None:
        time.sleep(float(os.getenv(env_key, default)))

    def _dismiss_navigation_blockers(self) -> None:
        self._non_ble._leave_manual_workout_editor_if_blocking_navigation()
        self._non_ble._dismiss_in_progress_ftue_overlays_if_present()

    def _wait_for_visible(
        self,
        locator_triplets: tuple[tuple, ...],
        env_key: str = "CUBII_STUDIO_WAIT_SEC",
        label: str = "element",
    ):
        wait_sec = self._wait_sec(env_key)
        wait = WebDriverWait(self.driver, wait_sec)
        last_exc: Exception | None = None
        for by, locator in locator_triplets:
            try:
                return wait.until(ec.visibility_of_element_located((by, locator)))
            except Exception as exc:
                last_exc = exc
                continue
        raise TimeoutException(
            f"{label} not visible within {wait_sec}s (last error: {last_exc})"
        )

    def _must_see(
        self,
        locator_triplets: tuple[tuple, ...],
        description: str,
        wait: WebDriverWait,
        missing: list[str],
    ) -> None:
        for by, locator in locator_triplets:
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                return
            except TimeoutException:
                continue
        missing.append(description)

    def _must_see_any(
        self,
        locator_triplets: tuple[tuple, ...],
        description: str,
        wait_sec: int,
        missing: list[str],
        poll_frequency: float = 0.5,
    ) -> None:
        """Assert one of several locators becomes visible within a single wait window."""

        def _any_visible(_driver):
            for by, locator in locator_triplets:
                try:
                    el = _driver.find_element(by, locator)
                    if el.is_displayed():
                        return el
                except Exception:
                    continue
            return False

        wait = WebDriverWait(self.driver, wait_sec, poll_frequency=poll_frequency)
        try:
            wait.until(_any_visible)
        except TimeoutException:
            missing.append(description)

    def _is_visible(self, locator_triplets: tuple[tuple, ...]) -> bool:
        for by, locator in locator_triplets:
            try:
                el = self.driver.find_element(by, locator)
                if el.is_displayed():
                    return True
            except Exception:
                continue
        return False

    def _scroll_video_detail_down_one(self) -> None:
        """Scroll the video detail screen down to reveal cards below bookmark."""
        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.08),
                "top": int(size["height"] * 0.22),
                "width": int(size["width"] * 0.84),
                "height": int(size["height"] * 0.55),
                "direction": "down",
                "percent": float(os.getenv("CUBII_STUDIO_VIDEO_DETAIL_SCROLL_PERCENT", "0.55")),
            },
        )

    def _looks_like_video_title(self, text: str) -> bool:
        """Heuristic: video titles usually include duration digits (e.g. 30-Min ...)."""
        cleaned = (text or "").strip()
        if not cleaned:
            return False
        return bool(re.search(r"\d", cleaned)) or "min" in cleaned.lower()

    def _is_on_video_detail_screen(self) -> bool:
        detail_locators = (
            (AppiumBy.ID, self.VIDEO_DETAILS_SCROLL_ID),
            (AppiumBy.XPATH, self.VIDEO_DETAILS_SCROLL_XPATH),
            (AppiumBy.ID, self.VIDEO_BOOKMARK_LAYOUT_ID),
            (AppiumBy.XPATH, self.VIDEO_BOOKMARK_LAYOUT_XPATH),
        )
        return self._is_visible(detail_locators)

    def _scroll_category_videos_list(self, direction: str) -> None:
        """Scroll the category video list (rvCategoryVideos)."""
        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.1),
                "top": int(size["height"] * 0.3),
                "width": int(size["width"] * 0.8),
                "height": int(size["height"] * 0.5),
                "direction": direction,
                "percent": float(os.getenv("CUBII_STUDIO_CATEGORY_LIST_SCROLL_PERCENT", "0.45")),
            },
        )

    def _find_collections_recycler_element(self):
        """Return the visible rvCollectionsList RecyclerView element, if present."""
        for by, locator in self.RV_COLLECTIONS_LIST_LOCATORS:
            try:
                el = self.driver.find_element(by, locator)
                if el.is_displayed():
                    return el
            except Exception:
                continue
        return None

    def _scroll_recycler_element(self, recycler, direction: str, percent: float) -> bool:
        """Scroll a RecyclerView via element scrollGesture, swipeGesture, or screen fallback."""
        if recycler is not None:
            try:
                element_id = recycler.id
                if element_id:
                    self.driver.execute_script(
                        "mobile: scrollGesture",
                        {
                            "elementId": element_id,
                            "direction": direction,
                            "percent": percent,
                        },
                    )
                    return True
            except Exception as exc:
                self.LOGGER.debug(
                    "Studio: element scrollGesture on rvCollectionsList failed: %s", exc
                )
            try:
                rect = recycler.rect
                margin_x = max(8, int(rect["width"] * 0.08))
                left = int(rect["x"]) + margin_x
                width = max(1, int(rect["width"]) - (2 * margin_x))
                height = max(1, int(rect["height"]))
                if direction == "down":
                    top = int(rect["y"] + height * 0.72)
                    swipe_dir = "up"
                else:
                    top = int(rect["y"] + height * 0.12)
                    swipe_dir = "down"
                swipe_height = max(1, int(height * 0.55))
                self.driver.execute_script(
                    "mobile: swipeGesture",
                    {
                        "left": left,
                        "top": top,
                        "width": width,
                        "height": swipe_height,
                        "direction": swipe_dir,
                        "percent": percent,
                    },
                )
                return True
            except Exception as exc:
                self.LOGGER.debug(
                    "Studio: swipeGesture on rvCollectionsList failed: %s", exc
                )

        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.1),
                "top": int(size["height"] * 0.25),
                "width": int(size["width"] * 0.8),
                "height": int(size["height"] * 0.55),
                "direction": direction,
                "percent": percent,
            },
        )
        return True

    def _scroll_collections_video_list(self, direction: str) -> None:
        """Scroll rvCollectionsList down/up until the list end (element-first, then screen)."""
        percent = float(
            os.getenv("CUBII_STUDIO_COLLECTIONS_LIST_SCROLL_PERCENT", "0.75")
        )
        recycler = self._find_collections_recycler_element()
        self._scroll_recycler_element(recycler, direction, percent)

    def _read_title_and_bookmark_from_video_card(
        self, card_el,
    ) -> tuple[str, object | None]:
        """Read txtVideoTitle and imgBookmarkIcon from a videosLayout card ViewGroup."""
        title = ""
        icon = None
        try:
            title_el = card_el.find_element(AppiumBy.ID, self.SAVED_VIDEO_TITLE_ID)
            title = self._element_text(title_el)
        except Exception:
            pass
        try:
            for candidate in card_el.find_elements(AppiumBy.ID, self.STUDIO_CARD_BOOKMARK_ICON_ID):
                if candidate.is_displayed():
                    icon = candidate
                    break
        except Exception:
            pass
        return title, icon

    def _collect_visible_category_video_card_entries(
        self,
    ) -> list[tuple[str, object, object]]:
        """Return (video_title, card ViewGroup, bookmark_icon) for visible videosLayout cards."""
        entries: list[tuple[str, object, object]] = []
        seen_cards: set[str] = set()

        for xpath in (
            self.CATEGORY_VIDEO_CARD_XPATH_IN_LIST,
            self.CATEGORY_VIDEO_CARD_XPATH,
        ):
            try:
                cards = self.driver.find_elements(AppiumBy.XPATH, xpath)
            except Exception:
                cards = []
            for card in cards:
                if not card.is_displayed():
                    continue
                card_key = getattr(card, "id", None) or str(card.location)
                if card_key in seen_cards:
                    continue
                seen_cards.add(card_key)
                title, icon = self._read_title_and_bookmark_from_video_card(card)
                if not title or not self._looks_like_video_title(title):
                    continue
                entries.append((title, card, icon))

        return entries

    def _collect_visible_category_row_entries(self) -> list[tuple[str, object, object]]:
        """Return (video_title, row_element, bookmark_icon) for visible category list rows."""
        entries = self._collect_visible_category_video_card_entries()
        if entries:
            return entries

        entries = []
        rv = None
        for by, locator in (
            (AppiumBy.ID, self.RV_CATEGORY_VIDEOS_ID),
            (AppiumBy.XPATH, self.RV_CATEGORY_VIDEOS_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.RV_CATEGORY_VIDEOS_UIAUTOMATOR),
        ):
            try:
                rv = self.driver.find_element(by, locator)
                if rv.is_displayed():
                    break
            except Exception:
                rv = None
        if rv is None:
            return entries

        rows = rv.find_elements(AppiumBy.XPATH, self.RV_CATEGORY_VIDEOS_ROW_REL_XPATH)
        for row in rows:
            if not row.is_displayed():
                continue
            title, icon = self._read_title_and_bookmark_from_video_card(row)
            if not title or not self._looks_like_video_title(title):
                continue
            if icon is not None:
                entries.append((title, row, icon))
        return entries

    def _find_category_bookmark_icon_for_title(self, title: str):
        """Scroll category list; return imgBookmarkIcon on the row matching title."""
        if not title:
            return None
        pause = float(os.getenv("CUBII_STUDIO_CATEGORY_LIST_SCROLL_PAUSE_SEC", "0.5"))
        up_scrolls = int(os.getenv("CUBII_STUDIO_CATEGORY_LIST_SCROLL_UP_ATTEMPTS", "3"))
        max_scrolls = int(os.getenv("CUBII_STUDIO_CATEGORY_LIST_SCROLL_ATTEMPTS", "8"))

        for _ in range(up_scrolls):
            self._scroll_category_videos_list("up")
            time.sleep(pause)

        for attempt in range(max_scrolls + 1):
            for row_title, _row, icon in self._collect_visible_category_row_entries():
                if self._titles_match(title, row_title):
                    self.LOGGER.info(
                        "Studio: category bookmark icon found for %r (scroll %s).",
                        title[:120],
                        attempt,
                    )
                    return icon
            if attempt < max_scrolls:
                self._scroll_category_videos_list("down")
                time.sleep(pause)
        return None

    def _tap_bookmark_icon_for_title(
        self,
        title: str,
        *,
        list_name: str,
        pause_env: str = "CUBII_AFTER_STUDIO_CARD_BOOKMARK_TAP_SEC",
    ) -> None:
        """Tap imgBookmarkIcon on the list row for title (same locator toggles bookmark/unbookmark)."""
        if not title:
            raise AssertionError(f"No video title provided to bookmark on {list_name}.")

        self.LOGGER.info(
            "Studio: tapping bookmark icon for %r on %s (imgBookmarkIcon toggles state; "
            "filled/outlined share the same resource-id and content-desc).",
            title[:120],
            list_name,
        )
        icon = self._find_category_bookmark_icon_for_title(title)
        if icon is None and list_name == "saved videos list":
            icon = self._find_saved_list_bookmark_icon_for_title(title)
        if icon is None:
            raise AssertionError(
                f"Could not find bookmark icon for {title!r} on {list_name} after scrolling."
            )
        icon.click()
        self._pause_after_tap(pause_env, "0.8")
        self._last_bookmarked_video_title = title
        self.LOGGER.info("Studio: bookmark icon tapped for %r on %s.", title[:120], list_name)

    def _scroll_studio_screen_down_one(self) -> None:
        """Scroll the Studio home screen down to reveal sections below the fold."""
        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.1),
                "top": int(size["height"] * 0.25),
                "width": int(size["width"] * 0.8),
                "height": int(size["height"] * 0.5),
                "direction": "down",
                "percent": float(os.getenv("CUBII_STUDIO_HOME_SCROLL_PERCENT", "0.45")),
            },
        )

    def _scroll_saved_videos_list(self, direction: str) -> None:
        """Scroll the saved videos list up or down."""
        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.1),
                "top": int(size["height"] * 0.35),
                "width": int(size["width"] * 0.8),
                "height": int(size["height"] * 0.45),
                "direction": direction,
                "percent": float(os.getenv("CUBII_STUDIO_SAVED_LIST_SCROLL_PERCENT", "0.5")),
            },
        )

    def _titles_match(self, expected: str, actual: str) -> bool:
        return expected in actual or actual in expected

    def _collect_visible_saved_video_titles(self) -> list[str]:
        """Collect unique video titles currently visible inside rv_saved_videos."""
        seen: set[str] = set()
        titles: list[str] = []
        try:
            elements = self.driver.find_elements(
                AppiumBy.XPATH, self.SAVED_VIDEO_TITLE_IN_LIST_XPATH
            )
        except Exception:
            elements = []
        for el in elements:
            if not el.is_displayed():
                continue
            text = self._element_text(el)
            if text and text not in seen:
                seen.add(text)
                titles.append(text)
        return titles

    def _collect_saved_video_titles_with_scroll(self) -> list[str]:
        """Scroll saved videos list and merge all unique titles discovered."""
        pause = float(os.getenv("CUBII_STUDIO_SAVED_LIST_SCROLL_PAUSE_SEC", "0.5"))
        up_scrolls = int(os.getenv("CUBII_STUDIO_SAVED_LIST_SCROLL_UP_ATTEMPTS", "3"))
        down_scrolls = int(os.getenv("CUBII_STUDIO_SAVED_LIST_SCROLL_ATTEMPTS", "8"))

        for _ in range(up_scrolls):
            self._scroll_saved_videos_list("up")
            time.sleep(pause)

        all_titles: list[str] = []
        seen: set[str] = set()
        for attempt in range(down_scrolls + 1):
            for title in self._collect_visible_saved_video_titles():
                if title not in seen:
                    seen.add(title)
                    all_titles.append(title)
            if attempt < down_scrolls:
                self.LOGGER.info(
                    "Studio: scrolling saved videos list down (%s/%s); titles so far=%s.",
                    attempt + 1,
                    down_scrolls,
                    all_titles,
                )
                self._scroll_saved_videos_list("down")
                time.sleep(pause)
        return all_titles

    def _wait_for_bookmarked_title_in_saved_list(self, target_title: str) -> list[str]:
        """Poll and scroll saved list until target title appears; return all titles found."""
        wait_sec = self._wait_sec("CUBII_STUDIO_SAVED_TITLE_WAIT_SEC", default=30)
        poll = float(os.getenv("CUBII_STUDIO_SAVED_TITLE_POLL_SEC", "1.0"))
        deadline = time.time() + wait_sec
        last_titles: list[str] = []

        while time.time() < deadline:
            last_titles = self._collect_saved_video_titles_with_scroll()
            if any(self._titles_match(target_title, title) for title in last_titles):
                self.LOGGER.info(
                    "Studio: bookmarked title %r found in saved list %r.",
                    target_title[:120],
                    last_titles,
                )
                return last_titles
            self.LOGGER.info(
                "Studio: bookmarked title %r not in list yet %r; retrying.",
                target_title[:120],
                last_titles,
            )
            time.sleep(poll)

        return last_titles

    def _must_see_with_scroll(
        self,
        locator_triplets: tuple[tuple, ...],
        description: str,
        missing: list[str],
    ) -> None:
        """Assert element is visible, scrolling the detail screen down between attempts."""
        wait_sec = self._wait_sec("CUBII_STUDIO_VIDEO_DETAIL_WAIT_SEC")
        max_scrolls = int(os.getenv("CUBII_STUDIO_VIDEO_DETAIL_SCROLL_ATTEMPTS", "8"))
        pause = float(os.getenv("CUBII_STUDIO_VIDEO_DETAIL_SCROLL_PAUSE_SEC", "0.4"))
        wait = WebDriverWait(self.driver, wait_sec)

        for attempt in range(max_scrolls + 1):
            found = False
            for by, locator in locator_triplets:
                try:
                    wait.until(ec.visibility_of_element_located((by, locator)))
                    found = True
                    break
                except TimeoutException:
                    continue
            if found:
                if attempt:
                    self.LOGGER.info(
                        "%s visible after %s scroll(s) on video detail.", description, attempt
                    )
                return
            if attempt < max_scrolls:
                self.LOGGER.info(
                    "%s not visible; scrolling video detail down (%s/%s).",
                    description,
                    attempt + 1,
                    max_scrolls,
                )
                self._scroll_video_detail_down_one()
                time.sleep(pause)
        missing.append(description)

    def _tap_random_visible(self, elements: list, label: str) -> bool:
        visible = [el for el in elements if el.is_displayed()]
        if not visible:
            return False
        ordered = visible[:]
        if len(ordered) > 1:
            primary = random.choice(ordered)
            others = [el for el in ordered if el != primary]
            random.shuffle(others)
            ordered = [primary] + others
        for el in ordered:
            try:
                el.click()
                self._pause_after_tap("CUBII_AFTER_STUDIO_TAP_SEC")
                self.LOGGER.info("%s: tapped one of %s visible element(s).", label, len(visible))
                return True
            except Exception:
                continue
        return False

    def open_cubii_studio_tab(self) -> None:
        """Open Cubii Studio from bottom navigation."""
        self.LOGGER.info("Open Cubii Studio tab.")
        self._dismiss_navigation_blockers()
        for by, locator in self.STUDIO_TAB_CANDIDATE_LOCATORS:
            try:
                for el in self.driver.find_elements(by, locator):
                    if not el.is_displayed():
                        continue
                    try:
                        if not el.is_enabled():
                            continue
                    except Exception:
                        pass
                    el.click()
                    self._pause_after_tap("CUBII_AFTER_STUDIO_TAB_TAP_SEC", "1.0")
                    self.LOGGER.info(
                        "Opened Cubii Studio tab using locator=(%s, %s).", by, locator
                    )
                    return
            except Exception:
                continue
        raise AssertionError(
            "Could not open Cubii Studio tab. Tried accessibility id, resource id, "
            "UiAutomator, and content-desc xpath."
        )

    def tap_studio_search_bar(self) -> None:
        """Tap the Studio search EditText (studio_search_bar)."""
        self.LOGGER.info("Studio: tap search bar (studio_search_bar).")
        self._tap_any_clickable(
            self.STUDIO_SEARCH_BAR_LOCATORS,
            "Studio search bar (studio_search_bar)",
            wait_sec=self._wait_sec("CUBII_STUDIO_SEARCH_BAR_TAP_WAIT_SEC", default=30),
            reveal_controls=False,
        )
        self._pause_after_tap("CUBII_AFTER_STUDIO_SEARCH_BAR_TAP_SEC", "0.5")

    def _fill_studio_search_bar(self, resolved: str) -> None:
        """Focus studio_search_bar, clear, and type the given string."""
        wait_sec = self._wait_sec("CUBII_STUDIO_SEARCH_INPUT_WAIT_SEC", default=30)
        wait = WebDriverWait(self.driver, wait_sec)
        last_exc: Exception | None = None
        for by, locator in self.STUDIO_SEARCH_BAR_LOCATORS:
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                try:
                    el.clear()
                except Exception:
                    pass
                el.send_keys(resolved)
                self._pause_after_tap("CUBII_AFTER_STUDIO_SEARCH_KEYS_SEC", "0.5")
                self.LOGGER.info("Studio: search bar text entered.")
                return
            except Exception as exc:
                last_exc = exc
                continue
        raise AssertionError(
            f"Could not enter text in Studio search bar. Last error: {last_exc}"
        )

    def enter_studio_search_text(self, text: str | None = None) -> None:
        """Type into studio_search_bar. Uses CUBII_STUDIO_SEARCH_VALID_TEXT env if text is empty."""
        resolved = (text or "").strip() or os.getenv(
            "CUBII_STUDIO_SEARCH_VALID_TEXT", self.DEFAULT_STUDIO_SEARCH_VALID_TEXT
        )
        self.LOGGER.info("Studio: enter search text %r.", resolved[:120])
        self._fill_studio_search_bar(resolved)

    def enter_studio_search_invalid_text(self, text: str | None = None) -> None:
        """Type invalid query into studio_search_bar. Uses CUBII_STUDIO_SEARCH_INVALID_TEXT when empty."""
        resolved = (text or "").strip() or os.getenv(
            "CUBII_STUDIO_SEARCH_INVALID_TEXT", self.DEFAULT_STUDIO_SEARCH_INVALID_TEXT
        )
        self.LOGGER.info("Studio: enter invalid search text %r.", resolved[:120])
        self._fill_studio_search_bar(resolved)

    def tap_search_cancel_button(self) -> None:
        """Tap search clear/cancel (ivSearchCancel)."""
        self.LOGGER.info("Studio: tap search cancel (ivSearchCancel).")
        self._tap_any_clickable(
            self.SEARCH_CANCEL_LOCATORS,
            "Search cancel (ivSearchCancel)",
            wait_sec=self._wait_sec("CUBII_STUDIO_SEARCH_CANCEL_TAP_WAIT_SEC", default=30),
            reveal_controls=False,
        )
        self._pause_after_tap("CUBII_AFTER_STUDIO_SEARCH_CANCEL_TAP_SEC", "0.5")

    def verify_search_no_results_empty_state(self) -> None:
        """Assert empty search state: No results, txtEmptyMessage, and fabEmptyIconIndicator."""
        self.LOGGER.info("Studio: verify search no-results empty state.")
        debounce = float(os.getenv("CUBII_STUDIO_NO_RESULTS_DEBOUNCE_SEC", "1.2"))
        time.sleep(debounce)
        wait_sec = self._wait_sec("CUBII_STUDIO_NO_RESULTS_VERIFY_WAIT_SEC", default=30)
        missing: list[str] = []
        self._must_see_any(
            self.NO_RESULTS_FOUND_LOCATORS,
            'No results found (TextView)',
            wait_sec,
            missing,
        )
        self._must_see_any(
            self.SEARCH_EMPTY_MESSAGE_LOCATORS,
            "Empty message (txtEmptyMessage)",
            wait_sec,
            missing,
        )
        self._must_see_any(
            self.FAB_EMPTY_ICON_LOCATORS,
            "Empty FAB illustration (fabEmptyIconIndicator)",
            wait_sec,
            missing,
        )
        if missing:
            raise AssertionError(
                "No-results empty state verification failed. Missing: " + ", ".join(missing)
            )

        msg_text = ""
        for by, locator in self.SEARCH_EMPTY_MESSAGE_LOCATORS:
            try:
                el = self.driver.find_element(by, locator)
                if el.is_displayed():
                    msg_text = self._element_text(el)
                    if msg_text:
                        break
            except Exception:
                continue
        if not msg_text:
            raise AssertionError("txtEmptyMessage visible but text could not be read.")

        if "We couldn't find what you're" not in msg_text:
            raise AssertionError(
                "txtEmptyMessage missing expected lead-in. "
                f"Got {msg_text!r}."
            )
        if "looking for" not in msg_text:
            raise AssertionError(
                "txtEmptyMessage missing expected trailing phrase. "
                f"Got {msg_text!r}."
            )

        self.LOGGER.info("Studio: no-results empty state verified (messages + empty icon).")

    def tap_search_result_video(self) -> None:
        """Tap a search result row in rvSearchList (prefers tvTitle)."""
        self.LOGGER.info("Studio: tap search result in rvSearchList.")

        debounce = float(os.getenv("CUBII_STUDIO_SEARCH_RESULT_DEBOUNCE_SEC", "1.0"))
        time.sleep(debounce)

        wait_sec = self._wait_sec("CUBII_STUDIO_SEARCH_RESULT_WAIT_SEC", default=30)
        wait = WebDriverWait(self.driver, wait_sec)
        rv_ok = False
        for by, locator in self.RV_SEARCH_LIST_LOCATORS:
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                rv_ok = True
                break
            except TimeoutException:
                continue
        if not rv_ok:
            raise AssertionError(
                "Search results list `com.cubii:id/rvSearchList` not visible before row tap."
            )

        title_els = self.driver.find_elements(
            AppiumBy.XPATH, self.SEARCH_RESULT_TITLE_IN_RV_SEARCH_LIST_XPATH
        )
        visible_titles = [el for el in title_els if el.is_displayed()]
        ordered_titles = visible_titles[:]
        if len(ordered_titles) > 1:
            primary = random.choice(ordered_titles)
            ordered_titles = [primary] + [e for e in ordered_titles if e != primary]
            random.shuffle(ordered_titles[1:])
        for title_el in ordered_titles:
            try:
                title_el.click()
                self._pause_after_tap("CUBII_AFTER_STUDIO_SEARCH_RESULT_TAP_SEC", "1.0")
                self.LOGGER.info("Studio: tapped search result via tvTitle.")
                return
            except Exception:
                continue

        rows = self.driver.find_elements(AppiumBy.XPATH, self.SEARCH_RESULT_ROW_XPATH)
        visible_rows = [r for r in rows if r.is_displayed()]
        ordered = visible_rows[:]
        if len(ordered) > 1:
            primary = random.choice(ordered)
            ordered = [primary] + [r for r in ordered if r != primary]
            random.shuffle(ordered[1:])
        for row in ordered:
            try:
                row.click()
                self._pause_after_tap("CUBII_AFTER_STUDIO_SEARCH_RESULT_TAP_SEC", "1.0")
                self.LOGGER.info("Studio: tapped search result row (ViewGroup path fallback).")
                return
            except Exception:
                continue

        last_exc: Exception | None = None
        for by, locator in self.SEARCH_RESULT_TITLE_LOCATORS:
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                self._pause_after_tap("CUBII_AFTER_STUDIO_SEARCH_RESULT_TAP_SEC", "1.0")
                self.LOGGER.info(
                    "Studio: tapped search result via tvTitle locator fallback (%s, %s).",
                    by,
                    locator,
                )
                return
            except Exception as exc:
                last_exc = exc
                continue

        try:
            el = wait.until(
                ec.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        self.SEARCH_RESULT_VIEWGROUP_FALLBACK_UIAUTOMATOR,
                    )
                )
            )
            el.click()
            self._pause_after_tap("CUBII_AFTER_STUDIO_SEARCH_RESULT_TAP_SEC", "1.0")
            self.LOGGER.info(
                "Studio: tapped search result via ViewGroup.instance(3) fallback."
            )
            return
        except Exception as exc:
            last_exc = exc

        raise AssertionError(
            "Could not tap a search result in rvSearchList (tvTitle, row, or fallbacks). "
            f"Last error: {last_exc}"
        )

    def tap_any_visible_video_card_on_studio_screen(self) -> None:
        """Tap a visible category or grid card on the Studio home/browse screen."""
        self.LOGGER.info("Studio: tap any visible video/category card.")
        wait_sec = self._wait_sec("CUBII_STUDIO_VIDEO_CARD_WAIT_SEC")
        wait = WebDriverWait(self.driver, wait_sec)

        rv_categories = None
        for by, locator in (
            (AppiumBy.ID, self.RV_CATEGORIES_ID),
            (AppiumBy.XPATH, self.RV_CATEGORIES_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.RV_CATEGORIES_UIAUTOMATOR),
        ):
            try:
                rv_categories = wait.until(ec.visibility_of_element_located((by, locator)))
                break
            except TimeoutException:
                continue

        if rv_categories is not None:
            cards = rv_categories.find_elements(
                AppiumBy.XPATH, self.RV_CATEGORIES_CATEGORY_CARD_REL_XPATH
            )
            if self._tap_random_visible(cards, "Studio category card (rvCategories)"):
                return

        for grid_index, instance in ((2, 1), (4, 3)):
            grid_xpath = self.RV_CATEGORY_ITEMS_XPATH_TMPL.format(index=grid_index)
            uia = self.RV_CATEGORY_ITEMS_UIAUTOMATOR_TMPL.format(instance=instance)
            grid = None
            for by, locator in (
                (AppiumBy.XPATH, grid_xpath),
                (AppiumBy.ANDROID_UIAUTOMATOR, uia),
                (AppiumBy.ID, self.RV_CATEGORY_ITEMS_ID),
            ):
                try:
                    grids = self.driver.find_elements(by, locator)
                    visible_grids = [g for g in grids if g.is_displayed()]
                    if visible_grids:
                        grid = visible_grids[min(len(visible_grids) - 1, instance)]
                        break
                except Exception:
                    continue
            if grid is None:
                continue
            children = grid.find_elements(
                AppiumBy.XPATH, self.RV_CATEGORY_ITEMS_GRID_CHILD_REL_XPATH
            )
            if not children:
                children = grid.find_elements(AppiumBy.XPATH, ".//android.view.ViewGroup")
            if self._tap_random_visible(
                children, f"Studio grid card (rvCategoryItems grid {grid_index})"
            ):
                return

        for by, locator, label in (
            (
                AppiumBy.XPATH,
                self.RV_CATEGORIES_CATEGORY_CARD_FALLBACK_XPATH,
                "rvCategories ViewGroup[3]",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.RV_CATEGORIES_CATEGORY_CARD_FALLBACK_UIAUTOMATOR,
                "ViewGroup.instance(12)",
            ),
            (
                AppiumBy.XPATH,
                self.RV_CATEGORY_ITEMS_XPATH_TMPL.format(index=2),
                "rvCategoryItems[2]",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.RV_CATEGORY_ITEMS_UIAUTOMATOR_TMPL.format(instance=1),
                "rvCategoryItems.instance(1)",
            ),
            (
                AppiumBy.XPATH,
                self.RV_CATEGORY_ITEMS_XPATH_TMPL.format(index=4),
                "rvCategoryItems[4]",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.RV_CATEGORY_ITEMS_UIAUTOMATOR_TMPL.format(instance=3),
                "rvCategoryItems.instance(3)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                self._pause_after_tap("CUBII_AFTER_STUDIO_VIDEO_CARD_TAP_SEC")
                self.LOGGER.info("Studio: tapped video/category card via fallback (%s).", label)
                return
            except Exception:
                continue

        raise AssertionError(
            "No Studio video/category card found. Checked rvCategories rows, rvCategoryItems "
            "grids, and documented fallback locators."
        )

    def _store_selected_category_video_title(self, title: str) -> None:
        """Remember which category-list video was opened (txtVideoTitle on videosLayout card)."""
        if not title:
            return
        self._selected_category_video_title = title
        self._last_bookmarked_video_title = title
        self.LOGGER.info(
            "Studio: stored category video title (txtVideoTitle)=%r.", title[:120]
        )

    def _verify_detail_title_matches_stored(self) -> None:
        """Assert video detail txtVideoTitle matches the category card title we opened."""
        expected = self._selected_category_video_title or self._last_bookmarked_video_title
        if not expected:
            self.LOGGER.warning(
                "Studio: no stored category video title; skipping detail title match check."
            )
            return
        actual = self._read_video_detail_title()
        if not actual:
            raise AssertionError(
                f"Could not read txtVideoTitle on video detail to match {expected!r}."
            )
        if not self._titles_match(expected, actual):
            raise AssertionError(
                "Video detail title does not match the category card that was opened. "
                f"Expected {expected!r}, detail shows {actual!r}."
            )
        self.LOGGER.info(
            "Studio: detail txtVideoTitle matches opened card title %r.", actual[:120]
        )

    def _wait_for_category_video_list(self) -> None:
        """Wait until rvCategoryVideos is visible."""
        wait_sec = self._wait_sec("CUBII_STUDIO_VIDEO_LIST_WAIT_SEC")
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator in (
            (AppiumBy.ID, self.RV_CATEGORY_VIDEOS_ID),
            (AppiumBy.XPATH, self.RV_CATEGORY_VIDEOS_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.RV_CATEGORY_VIDEOS_UIAUTOMATOR),
        ):
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                return
            except TimeoutException:
                continue
        raise AssertionError(
            "Category video list `com.cubii:id/rvCategoryVideos` not visible."
        )

    def _pick_category_video_card_entry(
        self,
    ) -> tuple[str, object, object]:
        """Pick a visible videosLayout card with txtVideoTitle and imgBookmarkIcon."""
        entries = [
            e for e in self._collect_visible_category_video_card_entries() if e[2] is not None
        ]
        if not entries:
            raise AssertionError(
                "No category video card with txtVideoTitle and imgBookmarkIcon found."
            )
        if len(entries) == 1:
            return entries[0]
        return random.choice(entries)

    def verify_and_bookmark_category_video_card(self) -> None:
        """Verify videosLayout card details, tap bookmark icon, store txtVideoTitle."""
        self.LOGGER.info(
            "Studio: verify category video card (txtVideoTitle + imgBookmarkIcon) and bookmark."
        )
        self._wait_for_category_video_list()
        title, card, icon = self._pick_category_video_card_entry()

        if not card.is_displayed():
            raise AssertionError("Category video card (videosLayout ViewGroup) is not visible.")
        if not title:
            raise AssertionError(
                "Category video card has no txtVideoTitle text."
            )
        if icon is None or not icon.is_displayed():
            raise AssertionError(
                f"Bookmark icon (imgBookmarkIcon) not visible on card for {title!r}."
            )

        self.LOGGER.info(
            "Studio: verified card title=%r with bookmark icon on category list.", title[:120]
        )
        self._store_selected_category_video_title(title)

        if self._is_studio_bookmark_icon_active(icon):
            self.LOGGER.info(
                "Studio: card already bookmarked for %r; skipping icon tap.", title[:120]
            )
            return

        icon.click()
        self._pause_after_tap("CUBII_AFTER_STUDIO_CARD_BOOKMARK_TAP_SEC", "0.8")
        self.LOGGER.info("Studio: tapped imgBookmarkIcon on category card for %r.", title[:120])

    def open_stored_category_video_card(self) -> None:
        """Open the same videosLayout card previously bookmarked (match by stored txtVideoTitle)."""
        expected = self._selected_category_video_title or self._last_bookmarked_video_title
        if not expected:
            raise AssertionError(
                "No stored category video title; bookmark a card before opening it."
            )
        self.LOGGER.info(
            "Studio: open bookmarked category card for %r.", expected[:120]
        )
        self._wait_for_category_video_list()
        pause = float(os.getenv("CUBII_STUDIO_CATEGORY_LIST_SCROLL_PAUSE_SEC", "0.5"))
        up_scrolls = int(os.getenv("CUBII_STUDIO_CATEGORY_LIST_SCROLL_UP_ATTEMPTS", "3"))
        max_scrolls = int(os.getenv("CUBII_STUDIO_CATEGORY_LIST_SCROLL_ATTEMPTS", "8"))

        for _ in range(up_scrolls):
            self._scroll_category_videos_list("up")
            time.sleep(pause)

        for attempt in range(max_scrolls + 1):
            for row_title, card, _icon in self._collect_visible_category_video_card_entries():
                if self._titles_match(expected, row_title):
                    card.click()
                    self._pause_after_tap("CUBII_AFTER_STUDIO_VIDEO_TAP_SEC")
                    self.LOGGER.info(
                        "Studio: opened videosLayout card for %r (scroll %s).",
                        expected[:120],
                        attempt,
                    )
                    return
            if attempt < max_scrolls:
                self._scroll_category_videos_list("down")
                time.sleep(pause)

        raise AssertionError(
            f"Could not find category video card for {expected!r} after scrolling."
        )

    def tap_any_visible_video_in_category_list(self) -> None:
        """Tap a videosLayout card in rvCategoryVideos; store txtVideoTitle before opening."""
        self.LOGGER.info("Studio: tap a videosLayout video card in rvCategoryVideos.")
        wait_sec = self._wait_sec("CUBII_STUDIO_VIDEO_LIST_WAIT_SEC")
        wait = WebDriverWait(self.driver, wait_sec)

        rv = None
        for by, locator in (
            (AppiumBy.ID, self.RV_CATEGORY_VIDEOS_ID),
            (AppiumBy.XPATH, self.RV_CATEGORY_VIDEOS_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.RV_CATEGORY_VIDEOS_UIAUTOMATOR),
        ):
            try:
                rv = wait.until(ec.visibility_of_element_located((by, locator)))
                break
            except TimeoutException:
                continue
        if rv is None:
            raise AssertionError(
                "Category video list `com.cubii:id/rvCategoryVideos` not visible before video tap."
            )

        entries = self._collect_visible_category_video_card_entries()
        if entries:
            ordered = entries[:]
            if len(ordered) > 1:
                primary = random.choice(ordered)
                ordered = [primary] + [e for e in ordered if e[0] != primary[0]]
            for title, card, _icon in ordered:
                try:
                    self._store_selected_category_video_title(title)
                    card.click()
                    self._pause_after_tap("CUBII_AFTER_STUDIO_VIDEO_TAP_SEC")
                    self.LOGGER.info(
                        "Studio: opened videosLayout card for %r.", title[:120]
                    )
                    return
                except Exception:
                    continue

        rows = rv.find_elements(AppiumBy.XPATH, self.RV_CATEGORY_VIDEOS_ROW_REL_XPATH)
        if self._tap_random_visible(rows, "Studio video row (rvCategoryVideos dynamic)"):
            return

        max_instance = int(os.getenv("CUBII_STUDIO_VIDEO_ROW_INSTANCE_MAX", "12"))
        instance_rows: list = []
        for idx in range(max_instance):
            sel = f'new UiSelector().className("android.view.ViewGroup").instance({idx})'
            try:
                el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, sel)
                if el.is_displayed():
                    instance_rows.append(el)
            except Exception:
                continue
        if self._tap_random_visible(instance_rows, "Studio video row (UiAutomator instances)"):
            return

        for by, locator, label in (
            (
                AppiumBy.XPATH,
                self.CATEGORY_VIDEO_CARD_XPATH_FIRST,
                "videosLayout card [1]",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.CATEGORY_VIDEO_CARD_FALLBACK_UIAUTOMATOR,
                "ViewGroup.instance(3)",
            ),
            (
                AppiumBy.XPATH,
                self.RV_CATEGORY_VIDEOS_FIRST_ROW_XPATH,
                "rvCategoryVideos/ViewGroup[1]",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.RV_CATEGORY_VIDEOS_FIRST_ROW_UIAUTOMATOR,
                "ViewGroup.instance(2)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                if "videosLayout" in label:
                    title, _ = self._read_title_and_bookmark_from_video_card(el)
                    if title:
                        self._store_selected_category_video_title(title)
                el.click()
                self._pause_after_tap("CUBII_AFTER_STUDIO_VIDEO_TAP_SEC")
                self.LOGGER.info("Studio: tapped video via fallback (%s).", label)
                return
            except Exception:
                continue

        raise AssertionError(
            "No video row found in `rvCategoryVideos` (videosLayout cards, dynamic rows, "
            "UiAutomator instances, or fallbacks)."
        )

    def verify_video_detail_screen(self) -> None:
        """Assert video detail header controls, then scroll to equipment and music cards."""
        self.LOGGER.info("Studio: verify video detail screen.")
        wait_sec = self._wait_sec("CUBII_STUDIO_VIDEO_DETAIL_WAIT_SEC")
        wait = WebDriverWait(self.driver, wait_sec)
        missing: list[str] = []

        self._must_see(
            (
                (AppiumBy.ID, self.VIDEO_DETAILS_SCROLL_ID),
                (AppiumBy.XPATH, self.VIDEO_DETAILS_SCROLL_XPATH),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIDEO_DETAILS_SCROLL_UIAUTOMATOR),
            ),
            "Video details scroll view (nsvVideoDetails)",
            wait,
            missing,
        )
        self._must_see(
            (
                (AppiumBy.ID, self.VIDEO_TITLE_LAYOUT_ID),
                (AppiumBy.XPATH, self.VIDEO_TITLE_LAYOUT_XPATH),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIDEO_TITLE_LAYOUT_UIAUTOMATOR),
            ),
            "Video title layout (linLayoutVideoTitle)",
            wait,
            missing,
        )
        self._must_see(
            (
                (AppiumBy.ID, self.VIDEO_DURATION_ID),
                (AppiumBy.XPATH, self.VIDEO_DURATION_XPATH),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIDEO_DURATION_UIAUTOMATOR),
            ),
            "Video duration (txtDuration)",
            wait,
            missing,
        )
        self._must_see(
            (
                (AppiumBy.ID, self.VIDEO_BOOKMARK_LAYOUT_ID),
                (AppiumBy.XPATH, self.VIDEO_BOOKMARK_LAYOUT_XPATH),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIDEO_BOOKMARK_LAYOUT_UIAUTOMATOR),
            ),
            "Bookmark option layout (linLayoutBookmarkOption)",
            wait,
            missing,
        )

        equipment_locators = (
            (AppiumBy.ID, self.CARD_EQUIPMENT_ID),
            (AppiumBy.XPATH, self.CARD_EQUIPMENT_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.CARD_EQUIPMENT_UIAUTOMATOR),
        )
        music_locators = (
            (AppiumBy.ID, self.CARD_MUSIC_PLAYED_ID),
            (AppiumBy.XPATH, self.CARD_MUSIC_PLAYED_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.CARD_MUSIC_PLAYED_UIAUTOMATOR),
        )

        if not self._is_visible(equipment_locators) or not self._is_visible(music_locators):
            self.LOGGER.info(
                "Studio: equipment/music cards below fold; scrolling video detail to verify."
            )

        self._must_see_with_scroll(
            equipment_locators,
            "Equipment card (cardEquipment)",
            missing,
        )
        self._must_see_with_scroll(
            music_locators,
            "Music played card (cardMusicPlayed)",
            missing,
        )

        if missing:
            raise AssertionError(
                "Video detail screen verification failed. Missing: " + ", ".join(missing)
            )
        self.LOGGER.info(
            "Studio: video detail screen verified (header, bookmark, equipment, music)."
        )

    def _reveal_exo_player_controls(self) -> None:
        """Tap the player area so ExoPlayer overlay (times, play) can appear."""
        tap_candidates = (
            (AppiumBy.ID, self.EXO_PLAY_PAUSE_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.EXO_PLAY_PAUSE_UIAUTOMATOR),
            (AppiumBy.ID, self.VIDEO_DETAILS_SCROLL_ID),
            (AppiumBy.ID, self.VIDEO_TITLE_LAYOUT_ID),
            (AppiumBy.ID, self.TOOLBAR_VIDEO_TITLE_ID),
        )
        for by, locator in tap_candidates:
            try:
                el = self.driver.find_element(by, locator)
                if el.is_displayed():
                    el.click()
                    self.LOGGER.info(
                        "Studio: tapped player surface to reveal controls (%s).", locator
                    )
                    return
            except Exception:
                continue
        size = self.driver.get_window_size()
        x = int(size["width"] * 0.5)
        y = int(size["height"] * 0.35)
        self.driver.tap([(x, y)])
        self.LOGGER.info("Studio: tapped screen center-top to reveal player controls.")

    def verify_video_player_controls(self) -> None:
        """Assert ExoPlayer times, play/pause, fullscreen, and toolbar video title are visible."""
        self.LOGGER.info("Studio: verify video player controls and toolbar title.")
        controls_wait_sec = self._wait_sec("CUBII_STUDIO_PLAYER_CONTROLS_WAIT_SEC", default=45)
        time_wait_sec = self._wait_sec("CUBII_STUDIO_PLAYER_TIME_WAIT_SEC", default=60)
        reveal_attempts = int(os.getenv("CUBII_STUDIO_PLAYER_REVEAL_ATTEMPTS", "3"))
        reveal_pause = float(os.getenv("CUBII_STUDIO_PLAYER_REVEAL_PAUSE_SEC", "1.5"))
        retry_time_wait_sec = self._wait_sec("CUBII_STUDIO_PLAYER_TIME_RETRY_WAIT_SEC", default=25)
        retry_controls_wait_sec = self._wait_sec(
            "CUBII_STUDIO_PLAYER_CONTROLS_RETRY_WAIT_SEC", default=20
        )

        exo_position_locators = (
            (AppiumBy.ID, self.EXO_POSITION_ID),
            (AppiumBy.XPATH, self.EXO_POSITION_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.EXO_POSITION_UIAUTOMATOR),
        )
        exo_duration_locators = (
            (AppiumBy.ID, self.EXO_TOTAL_DURATION_ID),
            (AppiumBy.XPATH, self.EXO_TOTAL_DURATION_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.EXO_TOTAL_DURATION_UIAUTOMATOR),
        )
        fullscreen_locators = self.FULL_SCREEN_BTN_LOCATORS
        play_pause_locators = (
            (AppiumBy.ACCESSIBILITY_ID, "Play"),
            (AppiumBy.XPATH, self.EXO_PLAY_PAUSE_PLAY_XPATH),
            (AppiumBy.ACCESSIBILITY_ID, "Pause"),
            (AppiumBy.XPATH, self.EXO_PLAY_PAUSE_PAUSE_XPATH),
            (AppiumBy.ID, self.EXO_PLAY_PAUSE_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.EXO_PLAY_PAUSE_UIAUTOMATOR),
        )
        title_locators = (
            (AppiumBy.ID, self.TOOLBAR_VIDEO_TITLE_ID),
            (AppiumBy.XPATH, self.TOOLBAR_VIDEO_TITLE_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.TOOLBAR_VIDEO_TITLE_UIAUTOMATOR),
        )

        missing: list[str] = []
        for attempt in range(1, reveal_attempts + 1):
            if attempt > 1:
                self.LOGGER.info(
                    "Studio: retry player controls reveal (%s/%s).", attempt, reveal_attempts
                )
            self._reveal_exo_player_controls()
            time.sleep(reveal_pause)
            missing = []
            attempt_time_wait = time_wait_sec if attempt == 1 else retry_time_wait_sec
            attempt_controls_wait = (
                controls_wait_sec if attempt == 1 else retry_controls_wait_sec
            )

            self._must_see_any(
                exo_position_locators,
                "Player start time (exo_position)",
                attempt_time_wait,
                missing,
            )
            self._must_see_any(
                exo_duration_locators,
                "Player end time (txtExoPlayerTotalDuration)",
                attempt_time_wait,
                missing,
            )
            self._must_see_any(
                fullscreen_locators,
                "Full Screen button (imgBtnFullScreen)",
                attempt_controls_wait,
                missing,
            )
            self._must_see_any(
                play_pause_locators,
                "Play/Pause control (exo_play_pause)",
                attempt_controls_wait,
                missing,
            )

            title_el = None
            title_wait = WebDriverWait(
                self.driver, attempt_controls_wait, poll_frequency=0.5
            )
            for by, locator in title_locators:
                try:
                    title_el = title_wait.until(ec.visibility_of_element_located((by, locator)))
                    break
                except TimeoutException:
                    continue
            if title_el is None:
                missing.append("Toolbar video title (txtToolbarTitle)")
            else:
                title_text = (title_el.text or title_el.get_attribute("text") or "").strip()
                if not title_text:
                    missing.append("Toolbar video title (txtToolbarTitle) — empty text")
                else:
                    self.LOGGER.info("Studio: toolbar video title=%r.", title_text[:120])

            if not missing:
                self.LOGGER.info(
                    "Studio: player controls verified on attempt %s/%s.",
                    attempt,
                    reveal_attempts,
                )
                return

            self.LOGGER.info(
                "Studio: player controls not ready (missing: %s).", ", ".join(missing)
            )

        raise AssertionError(
            "Video player controls verification failed. Missing: " + ", ".join(missing)
        )

    def _tap_any_clickable(
        self,
        locator_triplets: tuple[tuple, ...],
        label: str,
        wait_sec: int | None = None,
        reveal_controls: bool = True,
    ) -> None:
        if reveal_controls:
            self._reveal_exo_player_controls()
            time.sleep(float(os.getenv("CUBII_STUDIO_PLAYER_REVEAL_PAUSE_SEC", "1.0")))
        wait_sec = wait_sec or self._wait_sec("CUBII_STUDIO_FULLSCREEN_WAIT_SEC", default=30)
        wait = WebDriverWait(self.driver, wait_sec)
        last_exc: Exception | None = None
        for by, locator in locator_triplets:
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                self._pause_after_tap("CUBII_AFTER_STUDIO_FULLSCREEN_TAP_SEC", "1.2")
                self.LOGGER.info("Studio: tapped %s using (%s, %s).", label, by, locator)
                return
            except Exception as exc:
                last_exc = exc
                continue
        raise AssertionError(
            f"Could not tap {label} within {wait_sec}s (last error: {last_exc})"
        )

    def tap_full_screen_button(self) -> None:
        """Tap Full Screen on the video player."""
        self.LOGGER.info("Studio: tap Full Screen button.")
        self._tap_any_clickable(self.FULL_SCREEN_BTN_LOCATORS, "Full Screen (imgBtnFullScreen)")

    def verify_video_player_full_screen_mode(self) -> None:
        """Assert Exit Full Screen is visible (player is in fullscreen)."""
        self.LOGGER.info("Studio: verify video player is in full screen mode.")
        wait_sec = self._wait_sec("CUBII_STUDIO_FULLSCREEN_VERIFY_WAIT_SEC", default=30)
        missing: list[str] = []
        self._must_see_any(
            self.EXIT_FULL_SCREEN_BTN_LOCATORS,
            "Exit Full Screen button (imgBtnExitFullScreen)",
            wait_sec,
            missing,
        )
        if missing:
            raise AssertionError(
                "Video is not in full screen mode. Missing: " + ", ".join(missing)
            )
        self.LOGGER.info("Studio: full screen mode verified (Exit Full Screen visible).")

    def tap_exit_full_screen_button(self) -> None:
        """Tap Exit Full Screen on the video player."""
        self.LOGGER.info("Studio: tap Exit Full Screen button.")
        self._tap_any_clickable(
            self.EXIT_FULL_SCREEN_BTN_LOCATORS,
            "Exit Full Screen (imgBtnExitFullScreen)",
            reveal_controls=False,
        )

    def verify_full_screen_button_displayed(self) -> None:
        """Assert Full Screen button is visible again after exiting fullscreen."""
        self.LOGGER.info("Studio: verify Full Screen button is displayed.")
        wait_sec = self._wait_sec("CUBII_STUDIO_FULLSCREEN_VERIFY_WAIT_SEC", default=30)
        missing: list[str] = []
        self._reveal_exo_player_controls()
        time.sleep(float(os.getenv("CUBII_STUDIO_PLAYER_REVEAL_PAUSE_SEC", "1.0")))
        self._must_see_any(
            self.FULL_SCREEN_BTN_LOCATORS,
            "Full Screen button (imgBtnFullScreen)",
            wait_sec,
            missing,
        )
        if missing:
            raise AssertionError(
                "Full Screen button not displayed. Missing: " + ", ".join(missing)
            )
        self.LOGGER.info("Studio: Full Screen button is displayed.")

    def pause_video_on_player(self) -> None:
        """Tap topLayout to pause video playback and confirm Play control is shown."""
        self.LOGGER.info("Studio: pause video via topLayout.")
        self._reveal_exo_player_controls()
        time.sleep(float(os.getenv("CUBII_STUDIO_PLAYER_REVEAL_PAUSE_SEC", "1.0")))
        wait_sec = self._wait_sec("CUBII_STUDIO_PAUSE_WAIT_SEC", default=30)
        self._tap_any_clickable(
            self.TOP_LAYOUT_LOCATORS,
            "topLayout (pause video)",
            wait_sec=wait_sec,
            reveal_controls=False,
        )
        verify_pause = os.getenv("CUBII_STUDIO_VERIFY_PAUSE", "true").lower() == "true"
        if not verify_pause:
            return
        pause_wait = self._wait_sec("CUBII_STUDIO_PAUSE_VERIFY_WAIT_SEC", default=20)
        missing: list[str] = []
        self._must_see_any(
            self.EXO_PLAY_PAUSE_PLAY_LOCATORS,
            "Play control after pause (exo_play_pause)",
            pause_wait,
            missing,
        )
        if missing:
            raise AssertionError(
                "Video did not pause. Play control not visible after tapping topLayout. "
                f"Missing: {', '.join(missing)}"
            )
        self.LOGGER.info("Studio: video paused (Play control visible).")

    def tap_back_button(self) -> None:
        """Tap toolbar Navigate up (back) on the video detail screen."""
        self.LOGGER.info("Studio: tap back button (Navigate up).")
        self._tap_any_clickable(
            self.NAVIGATE_UP_LOCATORS,
            "Navigate up (back button)",
            wait_sec=self._wait_sec("CUBII_STUDIO_BACK_WAIT_SEC", default=30),
            reveal_controls=False,
        )

    def tap_video_screen_back_button(self) -> None:
        """Tap toolbar Navigate up (back) on the Studio video screen."""
        self.LOGGER.info("Studio: tap video screen back button (Navigate up).")
        self._tap_any_clickable(
            self.NAVIGATE_UP_LOCATORS,
            "Navigate up (video screen back button)",
            wait_sec=self._wait_sec("CUBII_STUDIO_VIDEO_SCREEN_BACK_WAIT_SEC", default=30),
            reveal_controls=False,
        )

    def _element_text(self, element) -> str:
        return (element.text or element.get_attribute("text") or "").strip()

    def _capture_and_store_bookmarked_video_title(self) -> str:
        """Read txtVideoTitle from detail and store for saved-list / unbookmark correlation."""
        title = self._read_video_detail_title()
        if not title:
            for by, locator in self.SAVED_VIDEO_TITLE_LOCATORS:
                try:
                    el = self.driver.find_element(by, locator)
                    if el.is_displayed():
                        title = self._element_text(el)
                        if title:
                            break
                except Exception:
                    continue
        if title:
            self._last_bookmarked_video_title = title
            self.LOGGER.info(
                "Studio: stored bookmarked video title (txtVideoTitle)=%r.",
                title[:120],
            )
        else:
            self.LOGGER.warning(
                "Studio: could not read txtVideoTitle to store bookmarked video title."
            )
        return title

    def _read_video_detail_title(self) -> str:
        """Read the video title from the detail body (not toolbar category name)."""
        detail_title_locators = (
            (AppiumBy.XPATH, self.VIDEO_DETAIL_TITLE_XPATH),
            (AppiumBy.XPATH, self.VIDEO_DETAIL_TITLE_IN_SCROLL_XPATH),
        )
        for by, locator in detail_title_locators:
            try:
                el = self.driver.find_element(by, locator)
                if el.is_displayed():
                    text = self._element_text(el)
                    if text:
                        self.LOGGER.info("Studio: video title from detail txtVideoTitle=%r.", text[:120])
                        return text
            except Exception:
                continue

        try:
            layout = self.driver.find_element(AppiumBy.ID, self.VIDEO_TITLE_LAYOUT_ID)
            for child in layout.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView"):
                if not child.is_displayed():
                    continue
                text = self._element_text(child)
                if text:
                    self.LOGGER.info(
                        "Studio: video title from linLayoutVideoTitle child=%r.", text[:120]
                    )
                    return text
        except Exception:
            pass

        toolbar_locators = (
            (AppiumBy.ID, self.TOOLBAR_VIDEO_TITLE_ID),
            (AppiumBy.XPATH, self.TOOLBAR_VIDEO_TITLE_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.TOOLBAR_VIDEO_TITLE_UIAUTOMATOR),
        )
        for by, locator in toolbar_locators:
            try:
                el = self.driver.find_element(by, locator)
                if not el.is_displayed():
                    continue
                text = self._element_text(el)
                if text:
                    self.LOGGER.warning(
                        "Studio: using toolbar title as fallback (may be category name): %r.",
                        text[:120],
                    )
                    return text
            except Exception:
                continue
        return ""

    def _is_studio_bookmark_icon_active(self, icon_el) -> bool:
        """Return True when a Studio list bookmark icon appears already bookmarked."""
        for attr in ("selected", "checked"):
            try:
                value = icon_el.get_attribute(attr)
                if value and str(value).lower() == "true":
                    return True
            except Exception:
                continue
        try:
            desc = (
                icon_el.get_attribute("content-desc")
                or icon_el.get_attribute("contentDescription")
                or ""
            ).strip().lower()
            if any(token in desc for token in ("bookmarked", "saved", "remove bookmark")):
                return True
        except Exception:
            pass
        return False

    def _find_visible_studio_bookmark_icons(self) -> list:
        """Find visible bookmark icons on the Studio category video list (dynamic instances)."""
        seen_ids: set[str] = set()
        icons: list = []
        max_instances = int(os.getenv("CUBII_STUDIO_CARD_BOOKMARK_MAX_INSTANCES", "12"))

        def _add_icon(el) -> None:
            if not el.is_displayed():
                return
            key = getattr(el, "id", None) or str(el.location)
            if key in seen_ids:
                return
            seen_ids.add(key)
            icons.append(el)

        for by, locator in ((AppiumBy.ID, self.STUDIO_CARD_BOOKMARK_ICON_ID),):
            try:
                for el in self.driver.find_elements(by, locator):
                    _add_icon(el)
            except Exception:
                continue

        try:
            for el in self.driver.find_elements(
                AppiumBy.XPATH, self.STUDIO_CARD_BOOKMARK_ICON_XPATH
            ):
                _add_icon(el)
        except Exception:
            pass

        for instance in range(max_instances):
            uia = self.STUDIO_CARD_BOOKMARK_ICON_UIAUTOMATOR_TMPL.format(instance=instance)
            try:
                el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, uia)
                _add_icon(el)
            except Exception:
                continue

        return icons

    def _read_studio_category_video_title(self, bookmark_icon=None) -> str:
        """Read a video title from the Studio category list near a bookmark icon."""
        if bookmark_icon is not None:
            current = bookmark_icon
            for _ in range(6):
                for by, locator in (
                    (AppiumBy.ID, self.SAVED_VIDEO_TITLE_ID),
                    (AppiumBy.XPATH, self.SAVED_VIDEO_TITLE_XPATH),
                ):
                    try:
                        for el in current.find_elements(by, locator):
                            if not el.is_displayed():
                                continue
                            text = self._element_text(el)
                            if text:
                                return text
                    except Exception:
                        continue
                try:
                    current = current.find_element(AppiumBy.XPATH, "./..")
                except Exception:
                    break

        rv = None
        for by, locator in (
            (AppiumBy.ID, self.RV_CATEGORY_VIDEOS_ID),
            (AppiumBy.XPATH, self.RV_CATEGORY_VIDEOS_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.RV_CATEGORY_VIDEOS_UIAUTOMATOR),
        ):
            try:
                rv = self.driver.find_element(by, locator)
                if rv.is_displayed():
                    break
            except Exception:
                rv = None
        search_root = rv if rv is not None else self.driver
        for by, locator in (
            (AppiumBy.ID, self.SAVED_VIDEO_TITLE_ID),
            (AppiumBy.XPATH, self.SAVED_VIDEO_TITLE_XPATH),
        ):
            try:
                for el in search_root.find_elements(by, locator):
                    if not el.is_displayed():
                        continue
                    text = self._element_text(el)
                    if text:
                        return text
            except Exception:
                continue
        return ""

    def tap_bookmark_on_studio_category_screen(self) -> None:
        """Bookmark a visible category-list video via imgBookmarkIcon when not already saved."""
        self.LOGGER.info("Studio: bookmark video on category screen (imgBookmarkIcon).")
        wait_sec = self._wait_sec("CUBII_STUDIO_CARD_BOOKMARK_WAIT_SEC", default=30)
        wait = WebDriverWait(self.driver, wait_sec)

        icons = self._find_visible_studio_bookmark_icons()
        if not icons:
            last_exc: Exception | None = None
            for by, locator in self.STUDIO_CARD_BOOKMARK_ICON_LOCATORS:
                try:
                    el = wait.until(ec.element_to_be_clickable((by, locator)))
                    icons = [el]
                    break
                except Exception as exc:
                    last_exc = exc
            if not icons:
                raise AssertionError(
                    "No Studio category bookmark icon (imgBookmarkIcon) found. "
                    f"Last error: {last_exc}"
                )

        ordered = icons[:]
        if len(ordered) > 1:
            primary = random.choice(ordered)
            ordered = [primary] + [el for el in ordered if el != primary]

        card_entries = [
            e for e in self._collect_visible_category_video_card_entries() if e[2] is not None
        ]
        if card_entries:
            title, _card, icon = (
                card_entries[0]
                if len(card_entries) == 1
                else random.choice(card_entries)
            )
            self._store_selected_category_video_title(title)
            if self._is_studio_bookmark_icon_active(icon):
                self.LOGGER.info(
                    "Studio: category card already bookmarked for %r; skipping tap.", title[:120]
                )
                return
            try:
                icon.click()
                self._pause_after_tap("CUBII_AFTER_STUDIO_CARD_BOOKMARK_TAP_SEC", "0.8")
                self.LOGGER.info(
                    "Studio: tapped bookmark on videosLayout card for %r.", title[:120]
                )
                return
            except Exception as exc:
                self.LOGGER.warning(
                    "Studio: card-matched bookmark tap failed (%s); trying icon scan.", exc
                )

        for icon in ordered:
            title = self._read_studio_category_video_title(icon)
            if title:
                self._store_selected_category_video_title(title)

            if self._is_studio_bookmark_icon_active(icon):
                self.LOGGER.info(
                    "Studio: category video already bookmarked; skipping icon tap for %r.",
                    (title or "unknown")[:120],
                )
                return

            try:
                icon.click()
                self._pause_after_tap("CUBII_AFTER_STUDIO_CARD_BOOKMARK_TAP_SEC", "0.8")
                self.LOGGER.info(
                    "Studio: tapped category bookmark icon for %r.",
                    (title or "unknown")[:120],
                )
                return
            except Exception:
                continue

        raise AssertionError(
            "Could not tap a Studio category bookmark icon (imgBookmarkIcon)."
        )

    def _is_video_already_bookmarked(self) -> bool:
        """Return True when the detail screen bookmark control already shows Bookmarked."""
        try:
            el = self.driver.find_element(
                AppiumBy.XPATH, self.BOOKMARKED_TEXT_IN_LAYOUT_XPATH
            )
            if el.is_displayed():
                return True
        except Exception:
            pass
        return self._is_visible(self.BOOKMARKED_TEXT_LOCATORS)

    def _scroll_detail_until_bookmark_icon_visible(self) -> None:
        """Scroll video detail until imgBookmarkIcon is visible."""
        max_scrolls = int(os.getenv("CUBII_STUDIO_BOOKMARK_SCROLL_ATTEMPTS", "6"))
        pause = float(os.getenv("CUBII_STUDIO_VIDEO_DETAIL_SCROLL_PAUSE_SEC", "0.4"))
        for attempt in range(max_scrolls + 1):
            if self._is_visible(self.VIDEO_DETAIL_BOOKMARK_ICON_LOCATORS):
                return
            if attempt < max_scrolls:
                self._scroll_video_detail_down_one()
                time.sleep(pause)
        raise AssertionError(
            "Bookmark icon (imgBookmarkIcon) not visible on video detail after "
            f"{max_scrolls} scroll(s)."
        )

    def tap_bookmark_option(self) -> None:
        """Bookmark the selected video on detail screen or category list by title row."""
        if self._is_on_video_detail_screen():
            self._verify_detail_title_matches_stored()
            title = self._capture_and_store_bookmarked_video_title()
            if not title:
                title = self._selected_category_video_title or self._last_bookmarked_video_title
            if self._is_video_already_bookmarked():
                self.LOGGER.info(
                    "Studio: detail video already shows Bookmarked for %r; skipping tap.",
                    (title or "unknown")[:120],
                )
                return
            self.LOGGER.info(
                "Studio: bookmark on video detail for %r (imgBookmarkIcon).",
                (title or "unknown")[:120],
            )
            self._scroll_detail_until_bookmark_icon_visible()
            self._tap_any_clickable(
                self.VIDEO_DETAIL_BOOKMARK_ICON_LOCATORS,
                "Bookmark icon on video detail (imgBookmarkIcon)",
                wait_sec=self._wait_sec("CUBII_STUDIO_BOOKMARK_TAP_WAIT_SEC", default=30),
                reveal_controls=False,
            )
            self._pause_after_tap("CUBII_AFTER_STUDIO_BOOKMARK_TAP_SEC", "0.8")
            self._capture_and_store_bookmarked_video_title()
            return

        title = (
            self._read_video_detail_title()
            or self._selected_category_video_title
            or self._last_bookmarked_video_title
        )
        if title and self._looks_like_video_title(title):
            self._last_bookmarked_video_title = title

        if not title or not self._looks_like_video_title(title):
            entries = self._collect_visible_category_row_entries()
            if entries:
                title = entries[0][0]
            if not title:
                raise AssertionError(
                    "Not on video detail and no category video title available to bookmark."
                )

        self.LOGGER.info(
            "Studio: still on category list; bookmark %r via row imgBookmarkIcon.",
            title[:120],
        )
        self._tap_bookmark_icon_for_title(title, list_name="category video list")

    def verify_bookmarked_button_text(self) -> None:
        """Assert the bookmark control shows Bookmarked text after tapping."""
        self.LOGGER.info("Studio: verify Bookmarked text on bookmark button.")
        wait_sec = self._wait_sec("CUBII_STUDIO_BOOKMARK_VERIFY_WAIT_SEC", default=20)
        missing: list[str] = []
        self._must_see_any(
            self.BOOKMARKED_TEXT_LOCATORS,
            'Bookmarked text',
            wait_sec,
            missing,
        )
        if missing:
            raise AssertionError(
                "Bookmark button did not show Bookmarked text. Missing: " + ", ".join(missing)
            )
        self.LOGGER.info("Studio: Bookmarked text verified.")
        self._verify_detail_title_matches_stored()
        stored = self._capture_and_store_bookmarked_video_title()
        if not stored:
            raise AssertionError(
                "Bookmarked state verified but txtVideoTitle could not be read on video detail."
            )

    def scroll_to_my_library_section(self) -> None:
        """Scroll Studio home until My Library label and bookmarks entry are visible."""
        self.LOGGER.info(
            "Studio: scroll to My Library (my_library_text) and bookmarks (savedVideosBtn)."
        )
        max_scrolls = int(os.getenv("CUBII_STUDIO_MY_LIBRARY_SCROLL_ATTEMPTS", "12"))
        pause = float(os.getenv("CUBII_STUDIO_MY_LIBRARY_SCROLL_PAUSE_SEC", "0.5"))
        for attempt in range(max_scrolls + 1):
            library_visible = self._is_visible(self.MY_LIBRARY_TEXT_LOCATORS)
            bookmarks_visible = self._is_visible(self.SAVED_VIDEOS_BTN_LOCATORS)
            if library_visible and bookmarks_visible:
                self.LOGGER.info(
                    "Studio: My Library and bookmarks option visible after %s scroll(s).",
                    attempt,
                )
                return
            if attempt < max_scrolls:
                self.LOGGER.info(
                    "Studio: scrolling down (%s/%s); my_library=%s, savedVideosBtn=%s.",
                    attempt + 1,
                    max_scrolls,
                    library_visible,
                    bookmarks_visible,
                )
                self._scroll_studio_screen_down_one()
                time.sleep(pause)
        raise AssertionError(
            "My Library section not ready after "
            f"{max_scrolls} scroll(s). "
            f"my_library_text={self._is_visible(self.MY_LIBRARY_TEXT_LOCATORS)}, "
            f"savedVideosBtn={self._is_visible(self.SAVED_VIDEOS_BTN_LOCATORS)}."
        )

    def verify_studio_category_visible_on_home(self, category_name: str) -> None:
        """Scroll Studio home until the given category title (txtCategoryTitle) is visible."""
        title = (category_name or "").strip()
        if not title:
            raise AssertionError("Studio category name is empty.")
        locators = self._category_title_locators(title)
        self.LOGGER.info("Studio: verify category %r (txtCategoryTitle) is visible.", title)
        max_scrolls = int(os.getenv("CUBII_STUDIO_CATEGORY_SCROLL_ATTEMPTS", "14"))
        pause = float(os.getenv("CUBII_STUDIO_CATEGORY_SCROLL_PAUSE_SEC", "0.5"))
        for attempt in range(max_scrolls + 1):
            if self._is_visible(locators):
                self.LOGGER.info(
                    "Studio: category %r visible after %s scroll(s).", title, attempt
                )
                return
            if attempt < max_scrolls:
                self.LOGGER.info(
                    "Studio: scrolling for category %r (%s/%s).",
                    title,
                    attempt + 1,
                    max_scrolls,
                )
                self._scroll_studio_screen_down_one()
                time.sleep(pause)
        raise AssertionError(
            f"Category {title!r} (txtCategoryTitle) not found on Studio home after scrolling."
        )

    def tap_view_all_for_category_on_studio_home(self, category_name: str) -> None:
        """Tap View All (txtViewAllTitle) on the row for the given Studio category."""
        title = (category_name or "").strip()
        if not title:
            raise AssertionError("Studio category name is empty.")
        if not self._is_visible(self._category_title_locators(title)):
            self.verify_studio_category_visible_on_home(title)
        self.LOGGER.info("Studio: tap View All (txtViewAllTitle) for category %r.", title)
        self._tap_any_clickable(
            self._view_all_locators_for_category(title),
            f"View All (txtViewAllTitle) for {title}",
            wait_sec=self._wait_sec("CUBII_STUDIO_VIEW_ALL_TAP_WAIT_SEC", default=30),
            reveal_controls=False,
        )
        self._pause_after_tap("CUBII_AFTER_STUDIO_VIEW_ALL_TAP_SEC", "1.0")

    def verify_class_collections_category_on_studio_home(self) -> None:
        """Scroll Studio home until Class Collections (txtCategoryTitle) is visible."""
        self.verify_studio_category_visible_on_home("Class Collections")

    def tap_view_all_for_class_collections_on_studio_home(self) -> None:
        """Tap View All (txtViewAllTitle) after Class Collections row is on screen."""
        self.tap_view_all_for_category_on_studio_home("Class Collections")

    def _wait_for_collections_video_list(self) -> None:
        """Wait until rvCollectionsList is visible."""
        wait_sec = self._wait_sec("CUBII_STUDIO_COLLECTIONS_LIST_WAIT_SEC", default=30)
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator in self.RV_COLLECTIONS_LIST_LOCATORS:
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                return
            except TimeoutException:
                continue
        raise AssertionError(
            "Collections video list `com.cubii:id/rvCollectionsList` not visible."
        )

    def _collect_visible_collections_list_items(self) -> tuple[list[str], int, int]:
        """Return (labels, video_card_count, row_count) currently visible in rvCollectionsList."""
        seen_labels: set[str] = set()
        labels: list[str] = []

        def _add_label(text: str) -> None:
            cleaned = (text or "").strip()
            if not cleaned or cleaned in self.COLLECTIONS_LIST_SKIP_LABELS:
                return
            if cleaned in seen_labels:
                return
            seen_labels.add(cleaned)
            labels.append(cleaned)

        for xpath in (
            self.COLLECTIONS_VIDEO_TITLE_IN_LIST_XPATH,
            self.COLLECTIONS_LIST_TEXT_XPATH,
        ):
            try:
                elements = self.driver.find_elements(AppiumBy.XPATH, xpath)
            except Exception:
                elements = []
            for el in elements:
                if not el.is_displayed():
                    continue
                _add_label(self._element_text(el))

        recycler = self._find_collections_recycler_element()
        if recycler is not None:
            try:
                for card in recycler.find_elements(AppiumBy.ID, self.VIDEOS_LAYOUT_ID):
                    if not card.is_displayed():
                        continue
                    title, _icon = self._read_title_and_bookmark_from_video_card(card)
                    if title:
                        _add_label(title)
            except Exception:
                pass

        for xpath in (self.COLLECTIONS_VIDEO_CARD_IN_LIST_XPATH, self.CATEGORY_VIDEO_CARD_XPATH):
            try:
                cards = self.driver.find_elements(AppiumBy.XPATH, xpath)
            except Exception:
                cards = []
            for card in cards:
                if not card.is_displayed():
                    continue
                title, _icon = self._read_title_and_bookmark_from_video_card(card)
                if title:
                    _add_label(title)

        row_count = 0
        for row_xpath in (self.COLLECTIONS_LIST_ROW_XPATH, self.COLLECTIONS_LIST_CHILD_XPATH):
            try:
                rows = self.driver.find_elements(AppiumBy.XPATH, row_xpath)
            except Exception:
                rows = []
            row_count = max(row_count, sum(1 for row in rows if row.is_displayed()))

        try:
            cards = self.driver.find_elements(
                AppiumBy.XPATH, self.COLLECTIONS_VIDEO_CARD_IN_LIST_XPATH
            )
        except Exception:
            cards = []
        card_count = sum(1 for card in cards if card.is_displayed())

        return labels, card_count, row_count

    def _collect_collections_video_titles_with_full_scroll(self) -> tuple[list[str], int, int]:
        """Scroll rvCollectionsList from top to bottom; merge labels and row counts."""
        pause = float(os.getenv("CUBII_STUDIO_COLLECTIONS_LIST_SCROLL_PAUSE_SEC", "0.6"))
        up_scrolls = int(os.getenv("CUBII_STUDIO_COLLECTIONS_LIST_SCROLL_UP_ATTEMPTS", "4"))
        max_down_scrolls = int(
            os.getenv("CUBII_STUDIO_COLLECTIONS_LIST_SCROLL_DOWN_ATTEMPTS", "30")
        )
        min_down_scrolls = int(
            os.getenv("CUBII_STUDIO_COLLECTIONS_LIST_MIN_DOWN_SCROLLS", "10")
        )
        stale_limit = int(os.getenv("CUBII_STUDIO_COLLECTIONS_LIST_STALE_SCROLLS", "4"))

        for _ in range(up_scrolls):
            self._scroll_collections_video_list("up")
            time.sleep(pause)

        all_labels: list[str] = []
        seen: set[str] = set()
        max_row_count = 0
        max_card_count = 0
        stale = 0
        down_scrolls_done = 0

        for attempt in range(max_down_scrolls + 1):
            labels, card_count, row_count = self._collect_visible_collections_list_items()
            max_row_count = max(max_row_count, row_count)
            max_card_count = max(max_card_count, card_count)
            new_count = 0
            for label in labels:
                if label not in seen:
                    seen.add(label)
                    all_labels.append(label)
                    new_count += 1

            at_end = (
                down_scrolls_done >= min_down_scrolls
                and new_count == 0
                and down_scrolls_done > 0
            )
            if at_end:
                stale += 1
                if stale >= stale_limit:
                    self.LOGGER.info(
                        "Studio: collections list end after %s down scroll(s); "
                        "labels=%s, max_rows=%s, max_cards=%s.",
                        down_scrolls_done,
                        len(all_labels),
                        max_row_count,
                        max_card_count,
                    )
                    break
            else:
                stale = 0

            if attempt < max_down_scrolls:
                self.LOGGER.info(
                    "Studio: scrolling collections list down (%s/%s, min=%s); "
                    "labels=%s, rows=%s, cards=%s.",
                    down_scrolls_done + 1,
                    max_down_scrolls,
                    min_down_scrolls,
                    all_labels,
                    row_count,
                    card_count,
                )
                self._scroll_collections_video_list("down")
                down_scrolls_done += 1
                time.sleep(pause)

        return all_labels, max_row_count, max_card_count

    def verify_studio_category_video_list_visible(self) -> None:
        """Assert video list RecyclerView is shown after View All (collections or category)."""
        self.LOGGER.info(
            "Studio: verify video list (rvCollectionsList or rvCategoryVideos) is visible."
        )
        if self._is_visible(self.RV_COLLECTIONS_LIST_LOCATORS):
            self._wait_for_collections_video_list()
            return
        self._wait_for_category_video_list()

    def verify_all_video_list_with_full_scroll(self) -> None:
        """Verify rvCollectionsList is present and scroll through the full video list."""
        self.LOGGER.info(
            "Studio: verify all videos in collections list (rvCollectionsList) with full scroll."
        )
        self._wait_for_collections_video_list()
        labels, max_rows, max_cards = self._collect_collections_video_titles_with_full_scroll()
        if labels:
            self.LOGGER.info(
                "Studio: verified %s list item(s) after full scroll: %s.",
                len(labels),
                labels,
            )
            return
        if max_cards > 0:
            self.LOGGER.info(
                "Studio: verified %s video card(s) after full scroll (no readable titles).",
                max_cards,
            )
            return
        if max_rows > 0:
            self.LOGGER.info(
                "Studio: verified %s list row(s) after full scroll (no readable titles).",
                max_rows,
            )
            return
        raise AssertionError(
            "No list items found in rvCollectionsList after scrolling to the end. "
            "Increase CUBII_STUDIO_COLLECTIONS_LIST_SCROLL_DOWN_ATTEMPTS or "
            "CUBII_STUDIO_COLLECTIONS_LIST_MIN_DOWN_SCROLLS if the list is long."
        )

    def tap_bookmarks_option(self) -> None:
        """Tap Saved Videos / bookmarks entry under My Library."""
        self.LOGGER.info("Studio: tap bookmarks option (savedVideosBtn).")
        self._tap_any_clickable(
            self.SAVED_VIDEOS_BTN_LOCATORS,
            "Bookmarks option (savedVideosBtn)",
            wait_sec=self._wait_sec("CUBII_STUDIO_SAVED_VIDEOS_TAP_WAIT_SEC", default=30),
            reveal_controls=False,
        )
        self._pause_after_tap("CUBII_AFTER_STUDIO_SAVED_VIDEOS_TAP_SEC", "1.0")

    def _read_visible_text_from_locators(
        self, locator_triplets: tuple[tuple, ...]
    ) -> str:
        """Return text from the first visible element matching any locator."""
        for by, locator in locator_triplets:
            try:
                el = self.driver.find_element(by, locator)
                if el.is_displayed():
                    text = self._element_text(el)
                    if text:
                        return text
            except Exception:
                continue
        return ""

    def verify_empty_saved_videos_screen(self) -> None:
        """Assert empty saved videos UI when no bookmarks exist."""
        self.LOGGER.info("Studio: verify empty saved videos screen.")
        wait_sec = self._wait_sec("CUBII_STUDIO_EMPTY_SAVED_VERIFY_WAIT_SEC", default=30)
        missing: list[str] = []

        self._must_see_any(
            self.SAVED_VIDEOS_TOOLBAR_TITLE_LOCATORS,
            "Saved videos toolbar title (toolbar_title)",
            wait_sec,
            missing,
        )
        self._must_see_any(
            self.EMPTY_SAVED_ICON_CARD_LOCATORS,
            "Empty saved videos icon card (emptyIconCard)",
            wait_sec,
            missing,
        )
        self._must_see_any(
            self.NO_VIDEOS_TEXT_LOCATORS,
            "No Videos label (txtNoVideos)",
            wait_sec,
            missing,
        )
        self._must_see_any(
            self.NO_VIDEOS_DESCRIPTION_LOCATORS,
            "No videos description (txtNoVideosDescription)",
            wait_sec,
            missing,
        )
        self._must_see_any(
            self.EXPLORE_VIDEOS_BTN_LOCATORS,
            "Explore Videos button (btnExploreVideos)",
            wait_sec,
            missing,
        )

        if missing:
            raise AssertionError(
                "Empty saved videos screen verification failed. Missing: "
                + ", ".join(missing)
            )

        no_videos_label = os.getenv(
            "CUBII_STUDIO_NO_VIDEOS_LABEL", self.NO_VIDEOS_LABEL
        )
        no_videos_text = self._read_visible_text_from_locators(self.NO_VIDEOS_TEXT_LOCATORS)
        if no_videos_label.lower() not in no_videos_text.lower():
            raise AssertionError(
                f"txtNoVideos text mismatch. Expected {no_videos_label!r}, got {no_videos_text!r}."
            )

        description_expected = os.getenv(
            "CUBII_STUDIO_NO_VIDEOS_DESCRIPTION_TEXT", self.NO_VIDEOS_DESCRIPTION_TEXT
        )
        description_actual = self._read_visible_text_from_locators(
            self.NO_VIDEOS_DESCRIPTION_LOCATORS
        )
        if description_expected not in description_actual:
            raise AssertionError(
                "txtNoVideosDescription text mismatch. "
                f"Expected {description_expected!r}, got {description_actual!r}."
            )

        explore_expected = os.getenv(
            "CUBII_STUDIO_EXPLORE_VIDEOS_BTN_TEXT", self.EXPLORE_VIDEOS_BTN_TEXT
        )
        explore_actual = self._read_visible_text_from_locators(self.EXPLORE_VIDEOS_BTN_LOCATORS)
        if explore_expected.upper() not in explore_actual.upper():
            raise AssertionError(
                f"btnExploreVideos text mismatch. Expected {explore_expected!r}, "
                f"got {explore_actual!r}."
            )

        self.LOGGER.info(
            "Studio: empty saved videos screen verified "
            "(no videos message, description, EXPLORE VIDEOS button)."
        )

    def tap_explore_videos_button(self) -> None:
        """Tap EXPLORE VIDEOS on the empty saved videos screen."""
        self.LOGGER.info("Studio: tap Explore Videos (btnExploreVideos).")
        self._tap_any_clickable(
            self.EXPLORE_VIDEOS_BTN_LOCATORS,
            "Explore Videos button (btnExploreVideos)",
            wait_sec=self._wait_sec("CUBII_STUDIO_EXPLORE_VIDEOS_TAP_WAIT_SEC", default=30),
            reveal_controls=False,
        )
        self._pause_after_tap("CUBII_AFTER_EXPLORE_VIDEOS_TAP_SEC", "1.0")

    def verify_bookmarked_videos_screen(self) -> None:
        """Assert saved videos screen, newly bookmarked title, and other saved videos."""
        self.LOGGER.info("Studio: verify bookmarked videos screen.")
        wait_sec = self._wait_sec("CUBII_STUDIO_SAVED_VIDEOS_VERIFY_WAIT_SEC", default=30)
        missing: list[str] = []
        self._must_see_any(
            self.SAVED_VIDEOS_TOOLBAR_TITLE_LOCATORS,
            "Saved videos toolbar title (toolbar_title)",
            wait_sec,
            missing,
        )
        self._must_see_any(
            self.RV_SAVED_VIDEOS_LOCATORS,
            "Saved videos list (rv_saved_videos)",
            wait_sec,
            missing,
        )
        self._must_see_any(
            self.SAVED_VIDEO_TITLE_LOCATORS,
            "Saved video title (txtVideoTitle)",
            wait_sec,
            missing,
        )
        if missing:
            raise AssertionError(
                "Bookmarked videos screen verification failed. Missing: " + ", ".join(missing)
            )

        min_total = int(os.getenv("CUBII_STUDIO_MIN_SAVED_VIDEOS_COUNT", "1"))
        min_other = int(os.getenv("CUBII_STUDIO_MIN_OTHER_SAVED_VIDEOS", "0"))

        if self._last_bookmarked_video_title:
            listed_titles = self._wait_for_bookmarked_title_in_saved_list(
                self._last_bookmarked_video_title
            )
        else:
            listed_titles = self._collect_saved_video_titles_with_scroll()

        if not listed_titles:
            raise AssertionError(
                "No saved video titles found in rv_saved_videos after scrolling."
            )

        self.LOGGER.info("Studio: saved video titles collected: %r.", listed_titles)

        if self._last_bookmarked_video_title:
            if not any(
                self._titles_match(self._last_bookmarked_video_title, title)
                for title in listed_titles
            ):
                raise AssertionError(
                    "Bookmarked video title not found in saved list. "
                    f"Expected title containing {self._last_bookmarked_video_title!r}; "
                    f"found {listed_titles!r}."
                )
            self.LOGGER.info(
                "Studio: newly bookmarked video %r verified in saved list.",
                self._last_bookmarked_video_title[:120],
            )

        other_titles = [
            title
            for title in listed_titles
            if not self._last_bookmarked_video_title
            or not self._titles_match(self._last_bookmarked_video_title, title)
        ]

        if len(listed_titles) < min_total:
            raise AssertionError(
                f"Expected at least {min_total} saved video(s) in the list; "
                f"found {len(listed_titles)}: {listed_titles!r}."
            )

        if len(other_titles) < min_other:
            raise AssertionError(
                f"Expected at least {min_other} other bookmarked video(s) besides the one "
                f"just saved; found {len(other_titles)}: {other_titles!r}. "
                f"All titles: {listed_titles!r}."
            )

        self.LOGGER.info(
            "Studio: verified newly bookmarked video and %s other saved video(s): %r.",
            len(other_titles),
            other_titles,
        )
        self.LOGGER.info("Studio: bookmarked videos screen verified.")

    def _find_visible_saved_list_bookmark_icon_for_title(self, title: str):
        """Find bookmark icon on a currently visible saved-list row matching the title."""
        try:
            rows = self.driver.find_elements(
                AppiumBy.XPATH,
                '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_saved_videos"]'
                "//android.view.ViewGroup",
            )
        except Exception:
            rows = []
        for row in rows:
            if not row.is_displayed():
                continue
            try:
                title_el = row.find_element(AppiumBy.ID, self.SAVED_VIDEO_TITLE_ID)
                row_title = self._element_text(title_el)
                if not row_title or not self._titles_match(title, row_title):
                    continue
                for icon in row.find_elements(AppiumBy.ID, self.STUDIO_CARD_BOOKMARK_ICON_ID):
                    if icon.is_displayed():
                        return icon
            except Exception:
                continue
        return None

    def _find_saved_list_bookmark_icon_for_title(self, title: str):
        """Scroll saved list and return bookmark icon on the row matching the title."""
        if not title:
            return None
        pause = float(os.getenv("CUBII_STUDIO_SAVED_LIST_SCROLL_PAUSE_SEC", "0.5"))
        up_scrolls = int(os.getenv("CUBII_STUDIO_SAVED_LIST_SCROLL_UP_ATTEMPTS", "3"))
        max_scrolls = int(os.getenv("CUBII_STUDIO_UNBOOKMARK_SCROLL_ATTEMPTS", "8"))

        for _ in range(up_scrolls):
            self._scroll_saved_videos_list("up")
            time.sleep(pause)

        for attempt in range(max_scrolls + 1):
            icon = self._find_visible_saved_list_bookmark_icon_for_title(title)
            if icon is not None:
                self.LOGGER.info(
                    "Studio: found bookmark icon for %r after %s scroll(s).",
                    title[:120],
                    attempt,
                )
                return icon
            if attempt < max_scrolls:
                self.LOGGER.info(
                    "Studio: %r not visible in saved list; scrolling down (%s/%s).",
                    title[:120],
                    attempt + 1,
                    max_scrolls,
                )
                self._scroll_saved_videos_list("down")
                time.sleep(pause)
        return None

    def tap_unbookmark_video_on_saved_list(self) -> None:
        """Toggle bookmark off via row-matched imgBookmarkIcon (same locator as bookmark)."""
        title = self._last_bookmarked_video_title
        if not title:
            raise AssertionError(
                "No bookmarked video title stored; cannot unbookmark the correct saved video."
            )
        self.LOGGER.info("Studio: unbookmark saved video %r via row bookmark icon.", title[:120])
        self._tap_bookmark_icon_for_title(
            title,
            list_name="saved videos list",
            pause_env="CUBII_AFTER_STUDIO_UNBOOKMARK_TAP_SEC",
        )

    def verify_unbookmarked_video_removed(self) -> None:
        """Assert the unbookmarked video is no longer listed in saved videos."""
        self.LOGGER.info("Studio: verify unbookmarked video removed from saved list.")
        wait_sec = self._wait_sec("CUBII_STUDIO_UNBOOKMARK_VERIFY_WAIT_SEC", default=30)
        poll = float(os.getenv("CUBII_STUDIO_UNBOOKMARK_VERIFY_POLL_SEC", "1.0"))
        deadline = time.time() + wait_sec
        removed_title = self._last_bookmarked_video_title

        while time.time() < deadline:
            listed_titles = self._collect_saved_video_titles_with_scroll()
            still_listed = bool(
                removed_title
                and any(self._titles_match(removed_title, title) for title in listed_titles)
            )
            if not still_listed:
                self.LOGGER.info(
                    "Studio: video %r removed from saved list; remaining=%r.",
                    (removed_title or "unknown")[:120],
                    listed_titles,
                )
                return
            self.LOGGER.info(
                "Studio: waiting for removal (still_listed=%s, titles=%r).",
                still_listed,
                listed_titles,
            )
            time.sleep(poll)

        listed_titles = self._collect_saved_video_titles_with_scroll()
        if removed_title and any(
            self._titles_match(removed_title, title) for title in listed_titles
        ):
            raise AssertionError(
                f"Unbookmarked video {removed_title!r} is still in saved list: {listed_titles!r}."
            )
        if not removed_title:
            raise AssertionError(
                "No bookmarked video title was stored; cannot verify removal."
            )
        raise AssertionError(
            "Could not verify video removal within timeout. "
            f"title={removed_title!r}, titles={listed_titles!r}."
        )

    def tap_saved_videos_back_button(self) -> None:
        """Tap Navigate up on the saved videos screen toolbar."""
        self.LOGGER.info("Studio: tap back button on saved videos screen (Navigate up).")
        self._tap_any_clickable(
            self.NAVIGATE_UP_LOCATORS,
            "Navigate up (saved videos back button)",
            wait_sec=self._wait_sec("CUBII_STUDIO_SAVED_VIDEOS_BACK_WAIT_SEC", default=30),
            reveal_controls=False,
        )

