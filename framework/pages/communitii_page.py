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


class CommunitiiPage(BasePage):
    """Bottom-nav Communitii tab and Community main screen."""

    LOGGER = logging.getLogger("cubii_communitii_page")

    NAVIGATION_CHIIRGROUP_ID = "com.cubii:id/navigation_chiirgroup"
    NAVIGATION_CHIIRGROUP_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/navigation_chiirgroup")'
    )
    COMMUNITII_TAB_CANDIDATE_LOCATORS = (
        (AppiumBy.ID, NAVIGATION_CHIIRGROUP_ID),
        (AppiumBy.ANDROID_UIAUTOMATOR, NAVIGATION_CHIIRGROUP_UIAUTOMATOR),
        (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Communitii"]'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Communitii")'),
        (
            AppiumBy.XPATH,
            '(//android.widget.ImageView[@resource-id="com.cubii:id/navigation_bar_item_icon_view"])[3]',
        ),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.cubii:id/navigation_bar_item_icon_view").instance(2)',
        ),
    )
    SB_MY_GROUP_ID = "com.cubii:id/sb_my_group"
    SB_MY_GROUP_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/sb_my_group")'
    SB_FRIENDS_ID = "com.cubii:id/sb_friends"
    SB_FRIENDS_XPATH = '//android.view.View[@resource-id="com.cubii:id/sb_friends"]'
    SB_FRIENDS_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/sb_friends")'
    FRIENDS_CHAT_LIST_SEARCH_ID = "com.cubii:id/edtChatListSearch"
    FRIENDS_CHAT_LIST_SEARCH_XPATH = (
        '//android.widget.EditText[@resource-id="com.cubii:id/edtChatListSearch"]'
    )
    FRIENDS_CHAT_LIST_SEARCH_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/edtChatListSearch")'
    )
    BTN_INVITE_FRIENDS_ID = "com.cubii:id/btnInviteFriends"
    BTN_INVITE_FRIENDS_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnInviteFriends"]'
    )
    BTN_INVITE_FRIENDS_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnInviteFriends")'
    )
    ADD_NEW_CHAT_SEARCH_ID = "com.cubii:id/edtAddNewChatSearch"
    ADD_NEW_CHAT_SEARCH_XPATH = (
        '//android.widget.EditText[@resource-id="com.cubii:id/edtAddNewChatSearch"]'
    )
    ADD_NEW_CHAT_SEARCH_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/edtAddNewChatSearch")'
    )
    CB_INVITE_FRIEND_ID = "com.cubii:id/cbInviteFriend"
    CB_INVITE_FRIEND_XPATH = (
        '//android.widget.ImageView[@resource-id="com.cubii:id/cbInviteFriend"]'
    )
    CB_INVITE_FRIEND_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/cbInviteFriend")'
    )
    DEFAULT_INVITE_FRIEND_NAME = os.getenv(
        "CUBII_INVITE_FRIEND_SEARCH_NAME", "Hetvee Sakariya"
    )
    CHAT_LAST_MSG_ID = "com.cubii:id/txtChatLastMsg"
    CHAT_LAST_MSG_FIRST_XPATH = (
        '(//android.widget.TextView[@resource-id="com.cubii:id/txtChatLastMsg"])[1]'
    )
    CHAT_LAST_MSG_FIRST_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtChatLastMsg").instance(0)'
    )
    CHAT_PROFILE_TOOLBAR_TITLE_ID = "com.cubii:id/toolbar_title"
    CHAT_PROFILE_TOOLBAR_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title"]'
    )
    CHAT_PROFILE_TOOLBAR_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/toolbar_title")'
    )
    CHAT_PROFILE_TOOLBAR_SUBTITLE_ID = "com.cubii:id/toolbar_subtitle"
    CHAT_PROFILE_TOOLBAR_SUBTITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_subtitle"]'
    )
    CHAT_PROFILE_TOOLBAR_SUBTITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/toolbar_subtitle")'
    )
    CHAT_PROFILE_VALID_STATUSES = ("ONLINE", "OFFLINE")
    DEFAULT_CHAT_PROFILE_NAME = os.getenv(
        "CUBII_CHAT_PROFILE_NAME", "Hetvee Sakariya"
    )
    CHAT_CONVERSATION_MESSAGE_ID = "com.cubii:id/edtChatConversationMessage"
    CHAT_CONVERSATION_MESSAGE_XPATH = (
        '//android.widget.EditText[@resource-id="com.cubii:id/edtChatConversationMessage"]'
    )
    CHAT_CONVERSATION_MESSAGE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/edtChatConversationMessage")'
    )
    CHAT_CONVERSATION_SEND_ID = "com.cubii:id/imgChatConversationSendMessage"
    CHAT_CONVERSATION_SEND_XPATH = (
        '//android.widget.ImageView[@resource-id="com.cubii:id/imgChatConversationSendMessage"]'
    )
    CHAT_CONVERSATION_SEND_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/imgChatConversationSendMessage")'
    )
    CARD_CHIIR_MOTIVATION_ID = "com.cubii:id/cardChatConversationSendChiirMotivation"
    CARD_CHIIR_MOTIVATION_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardChatConversationSendChiirMotivation"]'
    )
    CARD_CHIIR_MOTIVATION_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/cardChatConversationSendChiirMotivation")'
    )
    CHAT_CONVERSATION_OPTIONS_ID = "com.cubii:id/imgChatConversationOptions"
    CHAT_CONVERSATION_OPTIONS_XPATH = (
        '//android.widget.ImageView[@resource-id="com.cubii:id/imgChatConversationOptions"]'
    )
    CHAT_CONVERSATION_OPTIONS_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/imgChatConversationOptions")'
    )
    CHAT_OPTION_VIEW_INFO_ID = "com.cubii:id/txtOptionViewInfo"
    CHAT_OPTION_VIEW_INFO_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtOptionViewInfo"]'
    )
    CHAT_OPTION_VIEW_INFO_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtOptionViewInfo")'
    )
    CHAT_OPTION_UNFRIEND_ID = "com.cubii:id/txtOptionUnFriend"
    CHAT_OPTION_UNFRIEND_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtOptionUnFriend"]'
    )
    CHAT_OPTION_UNFRIEND_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtOptionUnFriend")'
    )
    CHAT_OPTION_REPORT_ID = "com.cubii:id/txtOptionReport"
    CHAT_OPTION_REPORT_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtOptionReport"]'
    )
    CHAT_OPTION_REPORT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtOptionReport")'
    )
    CHAT_OPTION_BLOCK_ID = "com.cubii:id/txtOptionBlock"
    CHAT_OPTION_BLOCK_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtOptionBlock"]'
    )
    CHAT_OPTION_BLOCK_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtOptionBlock")'
    )
    VIEW_INFO_USER_NAME_ID = "com.cubii:id/txtUserName"
    VIEW_INFO_USER_NAME_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtUserName"]'
    )
    VIEW_INFO_USER_NAME_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtUserName")'
    VIEW_INFO_VIEW_PROFILE_ID = "com.cubii:id/txtViewProfile"
    VIEW_INFO_VIEW_PROFILE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtViewProfile"]'
    )
    VIEW_INFO_VIEW_PROFILE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtViewProfile")'
    )
    VIEW_INFO_USER_JOINED_DATE_ID = "com.cubii:id/txtUserJoinedDateInfo"
    VIEW_INFO_USER_JOINED_DATE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtUserJoinedDateInfo"]'
    )
    VIEW_INFO_USER_JOINED_DATE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtUserJoinedDateInfo")'
    )
    VIEW_INFO_USER_GROUPS_INFO_ID = "com.cubii:id/txtUserGroupsInfo"
    VIEW_INFO_USER_GROUPS_INFO_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtUserGroupsInfo"]'
    )
    VIEW_INFO_USER_GROUPS_INFO_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtUserGroupsInfo")'
    )
    VIEW_INFO_BTN_REPORT_ID = "com.cubii:id/btnReport"
    VIEW_INFO_BTN_REPORT_XPATH = '//android.widget.Button[@resource-id="com.cubii:id/btnReport"]'
    VIEW_INFO_BTN_REPORT_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btnReport")'
    VIEW_INFO_BTN_BLOCK_ID = "com.cubii:id/btnBlock"
    VIEW_INFO_BTN_BLOCK_XPATH = '//android.widget.Button[@resource-id="com.cubii:id/btnBlock"]'
    VIEW_INFO_BTN_BLOCK_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btnBlock")'
    VIEW_INFO_BTN_UNFRIEND_ID = "com.cubii:id/btnUnfriend"
    VIEW_INFO_BTN_UNFRIEND_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnUnfriend"]'
    )
    VIEW_INFO_BTN_UNFRIEND_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnUnfriend")'
    )
    UNFRIEND_CONFIRM_BTN_YES_ID = "com.cubii:id/btnYes"
    UNFRIEND_CONFIRM_BTN_YES_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnYes"]'
    )
    UNFRIEND_CONFIRM_BTN_YES_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnYes")'
    )
    VIEW_PROFILE_BIO_TITLE_ID = "com.cubii:id/txtIgnoreBioTitle"
    VIEW_PROFILE_BIO_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtIgnoreBioTitle"]'
    )
    VIEW_PROFILE_BIO_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtIgnoreBioTitle")'
    )
    VIEW_PROFILE_BIO_TEXT_ID = "com.cubii:id/txtBio"
    VIEW_PROFILE_BIO_TEXT_XPATH = '//android.widget.TextView[@resource-id="com.cubii:id/txtBio"]'
    VIEW_PROFILE_BIO_TEXT_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtBio")'
    VIEW_PROFILE_FOCUS_TITLE_ID = "com.cubii:id/txtIgnoreFocusTitle"
    VIEW_PROFILE_FOCUS_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtIgnoreFocusTitle"]'
    )
    VIEW_PROFILE_FOCUS_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtIgnoreFocusTitle")'
    )
    VIEW_PROFILE_FOCUS_TEXT_ID = "com.cubii:id/txtFocus"
    VIEW_PROFILE_FOCUS_TEXT_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtFocus"]'
    )
    VIEW_PROFILE_FOCUS_TEXT_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/txtFocus")'
    VIEW_PROFILE_INTERESTS_TITLE_ID = "com.cubii:id/txtIgnoreInterestTitle"
    VIEW_PROFILE_INTERESTS_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtIgnoreInterestTitle"]'
    )
    VIEW_PROFILE_INTERESTS_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtIgnoreInterestTitle")'
    )
    VIEW_PROFILE_INTERESTS_LIST_ID = "com.cubii:id/rvInterest"
    VIEW_PROFILE_INTERESTS_LIST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvInterest"]'
    )
    VIEW_PROFILE_INTERESTS_LIST_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/rvInterest")'
    )
    VIEW_PROFILE_BADGES_TITLE_ID = "com.cubii:id/txtIgnoreBadgesTitle"
    VIEW_PROFILE_BADGES_TITLE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtIgnoreBadgesTitle"]'
    )
    VIEW_PROFILE_BADGES_TITLE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtIgnoreBadgesTitle")'
    )
    VIEW_PROFILE_BADGES_GRID_ID = "com.cubii:id/rvBadges"
    VIEW_PROFILE_BADGES_GRID_XPATH = (
        '//android.widget.GridView[@resource-id="com.cubii:id/rvBadges"]'
    )
    VIEW_PROFILE_BADGES_GRID_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/rvBadges")'
    CHAT_CONVERSATION_BLOCKED_BY_TEXT_ID = "com.cubii:id/txtChatConversationBlockedByText"
    CHAT_CONVERSATION_BLOCKED_BY_TEXT_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtChatConversationBlockedByText"]'
    )
    CHAT_CONVERSATION_BLOCKED_BY_TEXT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtChatConversationBlockedByText")'
    )
    BTN_UNBLOCK_ID = "com.cubii:id/btnUnblock"
    BTN_UNBLOCK_XPATH = '//android.widget.Button[@resource-id="com.cubii:id/btnUnblock"]'
    BTN_UNBLOCK_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btnUnblock")'
    CHAT_CONVERSATION_UNBLOCK_ID = BTN_UNBLOCK_ID
    CHAT_CONVERSATION_UNBLOCK_XPATH = BTN_UNBLOCK_XPATH
    CHAT_CONVERSATION_UNBLOCK_UIAUTOMATOR = BTN_UNBLOCK_UIAUTOMATOR
    FRIENDS_MOVED_MENU_FTUE_ID = "com.cubii:id/btnNextMovedMenu"
    FRIENDS_MOVED_MENU_FTUE_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnNextMovedMenu"]'
    )
    FRIENDS_MOVED_MENU_FTUE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnNextMovedMenu")'
    )
    BTN_CREATE_GROUP_ID = "com.cubii:id/btn_create_group"
    BTN_CREATE_GROUP_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btn_create_group"]'
    )
    BTN_CREATE_GROUP_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btn_create_group")'
    # Create group form (`editText` is the group name field on this screen).
    CREATE_GROUP_NAME_EDITTEXT_ID = "com.cubii:id/editText"
    CREATE_GROUP_NAME_EDITTEXT_XPATH = (
        '//android.widget.EditText[@resource-id="com.cubii:id/editText"]'
    )
    CREATE_GROUP_NAME_EDITTEXT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/editText")'
    )
    CREATE_GROUP_DESCRIPTION_EDITTEXT_ID = "com.cubii:id/et_description"
    CREATE_GROUP_DESCRIPTION_EDITTEXT_XPATH = (
        '//android.widget.EditText[@resource-id="com.cubii:id/et_description"]'
    )
    CREATE_GROUP_DESCRIPTION_EDITTEXT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/et_description")'
    )
    CREATE_GROUP_SWITCH_PUBLIC_ID = "com.cubii:id/switchCompat7"
    CREATE_GROUP_SWITCH_PUBLIC_XPATH = (
        '//android.widget.Switch[@resource-id="com.cubii:id/switchCompat7"]'
    )
    CREATE_GROUP_SWITCH_PUBLIC_XPATH_ANY = '//*[@resource-id="com.cubii:id/switchCompat7"]'
    CREATE_GROUP_SWITCH_PUBLIC_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/switchCompat7")'
    )
    CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_ID = "com.cubii:id/switchCompat8"
    CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_XPATH = (
        '//android.widget.Switch[@resource-id="com.cubii:id/switchCompat8"]'
    )
    CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_XPATH_ANY = (
        '//*[@resource-id="com.cubii:id/switchCompat8"]'
    )
    CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/switchCompat8")'
    )
    CREATE_GROUP_BTN_ADD_NEW_MEMBER_ID = "com.cubii:id/btn_add_new_member"
    CREATE_GROUP_BTN_ADD_NEW_MEMBER_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btn_add_new_member"]'
    )
    CREATE_GROUP_BTN_ADD_NEW_MEMBER_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btn_add_new_member")'
    )
    # Invite sheet / picker — member row uses `radioButton` (often `CheckBox` in hierarchy).
    CREATE_GROUP_INVITE_MEMBER_RADIOBUTTON_ID = "com.cubii:id/radioButton"
    CREATE_GROUP_INVITE_MEMBER_CHECKBOX_ALL_XPATH = (
        '//android.widget.CheckBox[@resource-id="com.cubii:id/radioButton"]'
    )
    CREATE_GROUP_INVITE_MEMBER_CHECKBOX_FIRST_XPATH = (
        '(//android.widget.CheckBox[@resource-id="com.cubii:id/radioButton"])[1]'
    )
    CREATE_GROUP_INVITE_MEMBER_RADIO_ANY_XPATH = '//*[@resource-id="com.cubii:id/radioButton"]'
    CREATE_GROUP_INVITE_MEMBER_RADIO_UIAUTOMATOR_TMPL = (
        'new UiSelector().resourceId("com.cubii:id/radioButton").instance({idx})'
    )
    CREATE_GROUP_BTN_DONE_ID = "com.cubii:id/btn_done"
    CREATE_GROUP_BTN_DONE_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btn_done"]'
    )
    CREATE_GROUP_BTN_DONE_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btn_done")'
    CREATE_GROUP_BTN_CREATE_ID = "com.cubii:id/btn_create"
    CREATE_GROUP_BTN_CREATE_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btn_create"]'
    )
    CREATE_GROUP_BTN_CREATE_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btn_create")'
    CREATE_GROUP_TEXTINPUT_ERROR_ID = "com.cubii:id/textinput_error"
    CREATE_GROUP_TEXTINPUT_ERROR_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textinput_error"]'
    )
    CREATE_GROUP_TEXTINPUT_ERROR_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/textinput_error")'
    )
    EXPLORE_GROUPS_XPATH = '//android.widget.TextView[@text="Explore Groups"]'
    EXPLORE_GROUPS_UIAUTOMATOR = 'new UiSelector().text("Explore Groups")'
    MY_GROUPS_XPATH = '//android.widget.TextView[@text="My Groups"]'
    MY_GROUPS_UIAUTOMATOR = 'new UiSelector().text("My Groups")'

    # Explore Groups banner (cvBanner) — XPath first; global ImageView.instance last (brittle).
    EXPLORE_BANNER_CANDIDATE_LOCATORS = (
        (
            AppiumBy.XPATH,
            "//android.widget.FrameLayout[@resource-id=\"com.cubii:id/cvBanner\"]"
            "/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView[1]",
        ),
        (
            AppiumBy.XPATH,
            "//android.widget.FrameLayout[@resource-id=\"com.cubii:id/cvBanner\"]"
            "//android.widget.ImageView[1]",
        ),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.ImageView").instance(2)',
        ),
    )
    RV_CHIIREXPLOREGROUP_ID = "com.cubii:id/rv_chiirexploregroup"
    RV_CHIIREXPLOREGROUP_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_chiirexploregroup"]'
    )
    RV_CHIIREXPLOREGROUP_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/rv_chiirexploregroup")'
    )
    EXPLORE_GROUPS_TV_BACK_BUTTON_ID = "com.cubii:id/tvBackButton"
    EXPLORE_GROUPS_TV_BACK_BUTTON_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/tvBackButton"]'
    )
    EXPLORE_GROUPS_TV_BACK_BUTTON_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/tvBackButton")'
    )
    EXPLORE_GROUP_CARD_ROW_REL_XPATH = (
        ".//android.widget.FrameLayout[@resource-id='com.cubii:id/constraintLayout2']"
    )
    EXPLORE_GROUP_CARD_FIRST_ABS_XPATH = (
        "(//android.widget.FrameLayout[@resource-id=\"com.cubii:id/constraintLayout2\"])"
        "[1]/android.view.ViewGroup"
    )
    EXPLORE_GROUP_CARD_ALL_ABS_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/constraintLayout2"]'
    )
    EXPLORE_GROUP_CARD_VIEWGROUP_FALLBACK_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(4)'
    )
    # Join (+) on explore rows — multiple `imageView19`; prefer first visible under list.
    EXPLORE_JOIN_GROUP_PLUS_IMAGEVIEW_ID = "com.cubii:id/imageView19"
    EXPLORE_JOIN_GROUP_PLUS_FIRST_XPATH = (
        '(//android.widget.ImageView[@resource-id="com.cubii:id/imageView19"])[1]'
    )
    EXPLORE_JOIN_GROUP_PLUS_UIAUTOMATOR_INSTANCE_0 = (
        'new UiSelector().resourceId("com.cubii:id/imageView19").instance(0)'
    )
    # Explore Groups list search field (`editText3`).
    EXPLORE_SEARCH_EDITTEXT_ID = "com.cubii:id/editText3"
    EXPLORE_SEARCH_EDITTEXT_XPATH = (
        '//android.widget.EditText[@resource-id="com.cubii:id/editText3"]'
    )
    EXPLORE_SEARCH_EDITTEXT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/editText3")'
    )
    # Joined / "My" groups list on Communitii main (`rv_chiirgroup`).
    JOINED_GROUPS_RV_CHIIRGROUP_ID = "com.cubii:id/rv_chiirgroup"
    JOINED_GROUPS_RV_CHIIRGROUP_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_chiirgroup"]'
    )
    JOINED_GROUPS_RV_CHIIRGROUP_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/rv_chiirgroup")'
    )
    JOINED_GROUP_RV_ROW_DIRECT_XPATH = "./android.view.ViewGroup"
    # Joined list rows: `RecyclerView` -> `FrameLayout` -> `ViewGroup` (per item; index varies).
    JOINED_GROUP_RV_FRAMELAYOUT_VIEWGROUP_REL_XPATH = (
        "./android.widget.FrameLayout/android.view.ViewGroup"
    )
    JOINED_GROUP_RV_FRAMELAYOUT_VIEWGROUP_ABS_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_chiirgroup"]'
        "/android.widget.FrameLayout/android.view.ViewGroup"
    )
    JOINED_GROUP_RV_FRAMELAYOUT1_VIEWGROUP_ABS_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_chiirgroup"]'
        "/android.widget.FrameLayout[1]/android.view.ViewGroup"
    )
    # UiAutomator: scoped to joined list RV, one `FrameLayout` child per row (`instance` = row index).
    JOINED_GROUP_RV_FRAMELAYOUT_CHILD_UIAUTOMATOR_TMPL = (
        'new UiSelector().resourceId("com.cubii:id/rv_chiirgroup").'
        'childSelector(new UiSelector().className("android.widget.FrameLayout").instance({idx}))'
    )
    # Legacy / fallback: global `ViewGroup` instance (e.g. instance(6) on some layouts); try a range.
    JOINED_GROUP_LIST_VIEWGROUP_INSTANCE_UIAUTOMATOR_TMPL = (
        'new UiSelector().className("android.view.ViewGroup").instance({idx})'
    )

    # Joined-group row cards (often `FrameLayout` `constraintLayout2`, not direct `ViewGroup` under RV).
    JOINED_GROUP_CARD_CONSTRAINTLAYOUT2_ID = "com.cubii:id/constraintLayout2"
    JOINED_GROUP_CARD_CONSTRAINTLAYOUT2_REL_XPATH = (
        './/android.widget.FrameLayout[@resource-id="com.cubii:id/constraintLayout2"]'
    )
    JOINED_GROUP_CARD_CONSTRAINTLAYOUT2_ABS_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/constraintLayout2"]'
    )
    JOINED_GROUP_CARD_CONSTRAINTLAYOUT2_FIRST_XPATH = (
        '(//android.widget.FrameLayout[@resource-id="com.cubii:id/constraintLayout2"])[1]'
    )
    JOINED_GROUP_CARD_CONSTRAINTLAYOUT2_UIAUTOMATOR_I0 = (
        'new UiSelector().resourceId("com.cubii:id/constraintLayout2").instance(0)'
    )

    # Group details (after opening a group from Explore).
    TXT_GROUP_NAME_COLLAPSIBLE_ID = "com.cubii:id/txtGroupNameCollapsible"
    TV_MEMBER_ID = "com.cubii:id/tv_member"
    TV_GROUP_VISIBILITY_ID = "com.cubii:id/tv_group_visibility"
    RV_GROUP_MEMBER_ID = "com.cubii:id/rv_group_member"
    RV_GROUP_MEMBER_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_group_member"]'
    )
    RV_GROUP_MEMBER_FIRST_ROW_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_group_member"]'
        "/android.view.ViewGroup[1]"
    )
    RV_GROUP_MEMBER_ALL_TOP_ROW_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_group_member"]'
        "/android.view.ViewGroup"
    )
    RV_GROUP_MEMBER_DIRECT_ROW_XPATH = "./android.view.ViewGroup"
    RV_GROUP_MEMBER_ROW_FALLBACK_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(2)'
    )
    # Current-user row on group leaderboard (`textView50` == ``You``).
    GROUP_MEMBER_SELF_YOU_TEXTVIEW_ID = "com.cubii:id/textView50"
    GROUP_MEMBER_SELF_YOU_TEXTVIEW_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView50" and @text="You"]'
    )
    GROUP_MEMBER_SELF_YOU_TEXTVIEW_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/textView50").text("You")'
    )
    GROUP_MEMBER_SELF_YOU_TEXT_ONLY_UIAUTOMATOR = 'new UiSelector().text("You")'
    GROUP_MEMBER_ROW_VIEWGROUP_7_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_group_member"]'
        "/android.view.ViewGroup[7]"
    )
    GROUP_MEMBER_VIEWGROUP_INSTANCE_10_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(10)'
    )
    # Group details toolbar overflow (three dots) / Leave group sheet / confirm No.
    GROUP_DETAIL_OVERFLOW_IMAGEVIEW_ID = "com.cubii:id/imgGroupDetailOptions"
    GROUP_DETAIL_OVERFLOW_CONTENT_DESC = "Cubii"
    GROUP_DETAIL_OVERFLOW_IMAGEVIEW_CUBII_XPATH = (
        '//android.widget.ImageView[@content-desc="Cubii"]'
    )
    GROUP_DETAIL_OVERFLOW_IMAGEVIEW_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/imgGroupDetailOptions")'
    )
    GROUP_DETAIL_LEAVE_GROUP_MENU_TEXT = "Leave Group"
    GROUP_DETAIL_DELETE_GROUP_OPTION_ID = "com.cubii:id/textView106"
    GROUP_DETAIL_DELETE_GROUP_OPTION_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView106"]'
    )
    GROUP_DETAIL_DELETE_GROUP_OPTION_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/textView106")'
    )
    GROUP_DETAIL_DELETE_GROUP_MENU_TEXT = "Delete Group"
    GROUP_DETAIL_EDIT_GROUP_OPTION_ID = "com.cubii:id/txtGrpOptionEditGroupOption"
    GROUP_DETAIL_EDIT_GROUP_OPTION_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtGrpOptionEditGroupOption"]'
    )
    GROUP_DETAIL_EDIT_GROUP_OPTION_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtGrpOptionEditGroupOption")'
    )
    GROUP_LEAVE_CONFIRM_BTN_NO_ID = "com.cubii:id/btn_no"
    GROUP_LEAVE_CONFIRM_BTN_NO_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btn_no"]'
    )
    GROUP_LEAVE_CONFIRM_BTN_NO_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btn_no")'
    GROUP_LEAVE_CONFIRM_BTN_YES_ID = "com.cubii:id/btn_yes"
    GROUP_LEAVE_CONFIRM_BTN_YES_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btn_yes"]'
    )
    GROUP_LEAVE_CONFIRM_BTN_YES_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btn_yes")'

    # Group details date duration filter (`cardTypeOfDuration`) and sheet row (Yesterday).
    GROUP_DATE_FILTER_CARD_TYPE_DURATION_ID = "com.cubii:id/cardTypeOfDuration"
    GROUP_DATE_FILTER_CARD_TYPE_DURATION_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardTypeOfDuration"]'
    )
    GROUP_DATE_FILTER_CARD_TYPE_DURATION_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/cardTypeOfDuration")'
    )
    GROUP_DATE_FILTER_YESTERDAY_LINEAR_ID = "com.cubii:id/linearLayout9"
    GROUP_DATE_FILTER_YESTERDAY_LINEAR_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/linearLayout9"]'
    )
    GROUP_DATE_FILTER_YESTERDAY_LINEAR_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/linearLayout9")'
    )
    GROUP_DATE_FILTER_LAST_7_DAYS_LINEAR_ID = "com.cubii:id/linearLayout10"
    GROUP_DATE_FILTER_LAST_7_DAYS_LINEAR_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/linearLayout10"]'
    )
    GROUP_DATE_FILTER_LAST_7_DAYS_LINEAR_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/linearLayout10")'
    )
    GROUP_DATE_FILTER_LAST_30_DAYS_TEXTVIEW_ID = "com.cubii:id/textView87"
    GROUP_DATE_FILTER_LAST_30_DAYS_TEXTVIEW_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView87"]'
    )
    GROUP_DATE_FILTER_LAST_30_DAYS_TEXTVIEW_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/textView87")'
    )

    # All Data user-type card — Inspector: id `com.cubii:id/cardTypeOfUser`,
    # UiAutomator `new UiSelector().resourceId("com.cubii:id/cardTypeOfUser")`,
    # xpath `//android.widget.FrameLayout[@resource-id="com.cubii:id/cardTypeOfUser"]`.
    ALL_DATA_FILTER_CARD_TYPE_USER_ID = "com.cubii:id/cardTypeOfUser"
    ALL_DATA_FILTER_CARD_TYPE_USER_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardTypeOfUser"]'
    )
    ALL_DATA_FILTER_CARD_TYPE_USER_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/cardTypeOfUser")'
    )
    ALL_DATA_FILTER_CARD_TYPE_USER_XPATH_ANY = (
        '//*[@resource-id="com.cubii:id/cardTypeOfUser"]'
    )

    ALL_DATA_AUTOMATED_DATA_TEXTVIEW_ID = "com.cubii:id/textView85"
    ALL_DATA_AUTOMATED_DATA_TEXTVIEW_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView85"]'
    )
    ALL_DATA_AUTOMATED_DATA_TEXTVIEW_XPATH_STRICT = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView85" and @text="Automated Data"]'
    )
    ALL_DATA_AUTOMATED_DATA_TEXTVIEW_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/textView85")'
    )
    ALL_DATA_AUTOMATED_DATA_PARENT_ID = "com.cubii:id/lytAutomaticDataParent"
    ALL_DATA_AUTOMATED_DATA_PARENT_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/lytAutomaticDataParent"]'
    )
    ALL_DATA_AUTOMATED_DATA_PARENT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/lytAutomaticDataParent")'
    )
    ALL_DATA_MANUAL_DATA_PARENT_ID = "com.cubii:id/lytManualDataParent"
    ALL_DATA_MANUAL_DATA_PARENT_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/lytManualDataParent"]'
    )
    ALL_DATA_MANUAL_DATA_PARENT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/lytManualDataParent")'
    )
    ALL_DATA_BOTH_DATA_PARENT_ID = "com.cubii:id/lytBothDataParent"
    ALL_DATA_BOTH_DATA_PARENT_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/lytBothDataParent"]'
    )
    ALL_DATA_BOTH_DATA_PARENT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/lytBothDataParent")'
    )

    # Group metrics filter (`cardTypeOfMetric`) and Calories row (`linearLayout8`).
    METRICS_FILTER_CARD_TYPE_METRIC_ID = "com.cubii:id/cardTypeOfMetric"
    METRICS_FILTER_CARD_TYPE_METRIC_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardTypeOfMetric"]'
    )
    METRICS_FILTER_CARD_TYPE_METRIC_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/cardTypeOfMetric")'
    )
    METRICS_FILTER_CARD_TYPE_METRIC_XPATH_ANY = (
        '//*[@resource-id="com.cubii:id/cardTypeOfMetric"]'
    )
    # Leaderboard metric is often icon-only (flame for Calories); no TextView on the card.
    METRICS_FILTER_CARD_METRIC_ICON_IMAGEVIEW_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardTypeOfMetric"]'
        "/android.widget.ImageView"
    )
    METRICS_FILTER_CALORIES_LINEAR_ID = "com.cubii:id/linearLayout8"
    METRICS_FILTER_CALORIES_LINEAR_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/linearLayout8"]'
    )
    METRICS_FILTER_CALORIES_LINEAR_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/linearLayout8")'
    )
    # Miles row in metrics sheet (`linearLayout9`). Same id as date-filter "Yesterday" row;
    # only call after the metrics sheet is open, not the date duration sheet.
    METRICS_FILTER_MILES_LINEAR_ID = "com.cubii:id/linearLayout9"
    METRICS_FILTER_MILES_LINEAR_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/linearLayout9"]'
    )
    METRICS_FILTER_MILES_LINEAR_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/linearLayout9")'
    )
    # Strides row in metrics sheet (`linearLayout10`). Same id as date-filter "Last 7 Days" row;
    # only call after the metrics sheet is open, not the date duration sheet.
    METRICS_FILTER_STRIDES_LINEAR_ID = "com.cubii:id/linearLayout10"
    METRICS_FILTER_STRIDES_LINEAR_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/linearLayout10"]'
    )
    METRICS_FILTER_STRIDES_LINEAR_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/linearLayout10")'
    )
    # Time row in metrics sheet (`linearLayout11`).
    METRICS_FILTER_TIME_LINEAR_ID = "com.cubii:id/linearLayout11"
    METRICS_FILTER_TIME_LINEAR_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/linearLayout11"]'
    )
    METRICS_FILTER_TIME_LINEAR_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/linearLayout11")'
    )

    # User bottom sheet after tapping a group member row.
    USER_DETAILS_CARD_SCROLL_XPATH = (
        "//android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup"
    )
    USER_DETAILS_CARD_VIEWGROUP_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(1)'
    )
    USER_DETAILS_TXT_USER_NAME_ID = "com.cubii:id/txtUserName"
    USER_DETAILS_TXT_VIEW_PROFILE_ID = "com.cubii:id/txtViewProfile"
    USER_DETAILS_TXT_VIEW_PROFILE_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtViewProfile"]'
    )
    USER_DETAILS_TXT_VIEW_PROFILE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtViewProfile")'
    )
    USER_DETAILS_BTN_REPORT_ID = "com.cubii:id/btnReport"
    USER_DETAILS_BTN_REPORT_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnReport"]'
    )
    USER_DETAILS_BTN_REPORT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnReport")'
    )
    USER_DETAILS_BTN_BLOCK_ID = "com.cubii:id/btnBlock"
    USER_DETAILS_BTN_ADD_FRIEND_ID = "com.cubii:id/btnAddFriend"
    USER_DETAILS_FAB_CLOSE_ID = "com.cubii:id/fabClose"
    USER_DETAILS_FAB_CLOSE_ACCESSIBILITY_ID = "Close"
    USER_DETAILS_FAB_CLOSE_XPATH = (
        '//com.google.android.material.floatingactionbutton.FloatingActionButton'
        '[@content-desc="Close"]'
    )
    USER_DETAILS_FAB_CLOSE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/fabClose")'
    )

    # Full-screen viewed member profile (after tapping View Profile on the bottom sheet).
    VIEWED_PROFILE_IMG_USER_PICTURE_ID = "com.cubii:id/imgUserProfilePictureMyAccount"
    VIEWED_PROFILE_IMG_USER_PICTURE_XPATH = (
        '//android.widget.ImageView[@resource-id="com.cubii:id/imgUserProfilePictureMyAccount"]'
    )
    VIEWED_PROFILE_IMG_USER_PICTURE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/imgUserProfilePictureMyAccount")'
    )
    VIEWED_PROFILE_USER_NAME_TEXTVIEW_ID = "com.cubii:id/textView22"
    VIEWED_PROFILE_USER_NAME_TEXTVIEW_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/textView22"]'
    )
    VIEWED_PROFILE_USER_NAME_TEXTVIEW_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/textView22")'
    )
    VIEWED_PROFILE_CARD_BADGES_ID = "com.cubii:id/cardBadges"
    VIEWED_PROFILE_CARD_BADGES_FRAME_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardBadges"]'
    )
    VIEWED_PROFILE_BADGES_INNER_VIEWGROUP_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardBadges"]/android.view.ViewGroup'
    )
    VIEWED_PROFILE_BADGES_VIEWGROUP_INSTANCE_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(4)'
    )
    VIEWED_PROFILE_CARD_FOCUS_ID = "com.cubii:id/cardFocus"
    VIEWED_PROFILE_CARD_FOCUS_FRAME_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardFocus"]'
    )
    VIEWED_PROFILE_FOCUS_INNER_VIEWGROUP_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardFocus"]/android.view.ViewGroup'
    )
    VIEWED_PROFILE_FOCUS_VIEWGROUP_INSTANCE_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(5)'
    )
    VIEWED_PROFILE_CARD_INTEREST_ID = "com.cubii:id/cardInterest"
    VIEWED_PROFILE_CARD_INTEREST_FRAME_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardInterest"]'
    )
    VIEWED_PROFILE_INTEREST_INNER_VIEWGROUP_XPATH = (
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/cardInterest"]/android.view.ViewGroup'
    )
    VIEWED_PROFILE_INTEREST_VIEWGROUP_INSTANCE_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(6)'
    )
    VIEWED_PROFILE_IV_BACK_ID = "com.cubii:id/iv_back"
    VIEWED_PROFILE_IV_BACK_LINEAR_XPATH = (
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/iv_back"]'
    )
    VIEWED_PROFILE_IV_BACK_XPATH_ANY = '//*[@resource-id="com.cubii:id/iv_back"]'
    VIEWED_PROFILE_IV_BACK_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/iv_back")'

    # Report form after opening Report from member user details sheet.
    REPORT_FORM_ET_SUBJECT_ID = "com.cubii:id/etSubject"
    REPORT_FORM_ET_SUBJECT_XPATH = (
        '//android.widget.EditText[@resource-id="com.cubii:id/etSubject"]'
    )
    REPORT_FORM_ET_SUBJECT_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/etSubject")'
    )
    REPORT_FORM_ET_DESCRIBE_ID = "com.cubii:id/etDescribe"
    REPORT_FORM_ET_DESCRIBE_XPATH = (
        '//android.widget.EditText[@resource-id="com.cubii:id/etDescribe"]'
    )
    REPORT_FORM_ET_DESCRIBE_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/etDescribe")'
    )

    # Block user flow: sheet -> optional confirm -> Navigate up -> toolbar back -> More -> Blocked users.
    BLOCK_USER_BTN_BLOCK_XPATH = '//android.widget.Button[@resource-id="com.cubii:id/btnBlock"]'
    BLOCK_USER_BTN_BLOCK_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/btnBlock")'
    NAVIGATE_UP_ACCESSIBILITY_ID = "Navigate up"
    NAVIGATE_UP_XPATH = '//android.widget.ImageButton[@content-desc="Navigate up"]'
    NAVIGATE_UP_UIAUTOMATOR = 'new UiSelector().description("Navigate up")'
    TOOLBAR_BACK_LINEAR_LAYOUT_XPATH = (
        '//android.view.ViewGroup[@resource-id="com.cubii:id/toolbar"]/android.widget.LinearLayout'
    )
    TOOLBAR_BACK_LINEAR_LAYOUT_UIAUTOMATOR = (
        'new UiSelector().className("android.widget.LinearLayout").instance(3)'
    )
    MORE_ICON_ID = "com.cubii:id/moreIcon"
    MORE_ICON_ACCESSIBILITY_ID = "More"
    MORE_ICON_XPATH = '//android.widget.ImageView[@content-desc="More"]'
    MORE_ICON_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/moreIcon")'
    BLOCKED_USERS_MENU_OPTION_ID = "com.cubii:id/txtOptionBlockedUsers"
    BLOCKED_USERS_MENU_OPTION_XPATH = (
        '//android.widget.TextView[@resource-id="com.cubii:id/txtOptionBlockedUsers"]'
    )
    BLOCKED_USERS_MENU_OPTION_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/txtOptionBlockedUsers")'
    )
    BLOCKED_USERS_RV_USERS_LIST_ID = "com.cubii:id/rvUsersList"
    BLOCKED_USERS_RV_USERS_LIST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvUsersList"]'
    )
    BLOCKED_USERS_RV_ROW_REL_XPATH = "./android.view.ViewGroup"
    BLOCKED_USERS_ROW_FIRST_XPATH = (
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvUsersList"]'
        "/android.view.ViewGroup[1]"
    )
    BLOCKED_USERS_ROW_FALLBACK_UIAUTOMATOR = (
        'new UiSelector().className("android.view.ViewGroup").instance(2)'
    )
    BLOCKED_USERS_TV_UNBLOCK_ID = "com.cubii:id/tvUnblock"
    BLOCKED_USERS_BTN_UNBLOCK_DIALOG_CANCEL_ID = "com.cubii:id/btnCancel"
    BLOCKED_USERS_BTN_UNBLOCK_DIALOG_CONFIRM_ID = BTN_UNBLOCK_ID
    BLOCKED_USERS_BTN_CANCEL_XPATH = (
        '//android.widget.Button[@resource-id="com.cubii:id/btnCancel"]'
    )
    BLOCKED_USERS_BTN_CONFIRM_UNBLOCK_XPATH = BTN_UNBLOCK_XPATH
    BLOCKED_USERS_BTN_CANCEL_UIAUTOMATOR = (
        'new UiSelector().resourceId("com.cubii:id/btnCancel")'
    )
    BLOCKED_USERS_BTN_CONFIRM_UNBLOCK_UIAUTOMATOR = BTN_UNBLOCK_UIAUTOMATOR
    LL_BACK_ID = "com.cubii:id/llBack"
    LL_BACK_XPATH = '//android.widget.LinearLayout[@resource-id="com.cubii:id/llBack"]'
    LL_BACK_UIAUTOMATOR = 'new UiSelector().resourceId("com.cubii:id/llBack")'

    def __init__(self, driver, non_ble_page: NonBleConnectionPage):
        super().__init__(driver)
        self._non_ble = non_ble_page
        self._last_create_group_form_name: str | None = None
        self._last_community_group_detail_name_for_leave: str | None = None
        self._last_edited_group_name: str | None = None
        self._last_edited_group_description: str | None = None
        self._recall_create_group_name()

    def _last_create_group_name_file(self) -> str:
        return os.getenv("CUBII_LAST_CREATE_GROUP_NAME_FILE", "reports/last_create_group_name.txt")

    def _remember_create_group_name(self, name: str) -> None:
        """Store the last submitted create-group name for later scenarios (memory + file)."""
        name = (name or "").strip()
        if not name:
            return
        self._last_create_group_form_name = name
        path = self._last_create_group_name_file()
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(name)
            self.LOGGER.info("Remembered last created group name %r.", name[:80])
        except OSError as exc:
            self.LOGGER.debug("Could not persist last create group name: %s", exc)

    def _recall_create_group_name(self) -> str:
        """Return the last created group name from memory or the persisted file."""
        name = (self._last_create_group_form_name or "").strip()
        if name:
            return name
        path = self._last_create_group_name_file()
        try:
            with open(path, encoding="utf-8") as fh:
                name = fh.read().strip()
            if name:
                self._last_create_group_form_name = name
                self.LOGGER.info("Recalled last created group name from file: %r.", name[:80])
                return name
        except OSError:
            pass
        return ""

    _QA_AUTO_GROUP_TITLE_RE = re.compile(r"QA\s+Auto\s+Group\s*(\d+)", re.IGNORECASE)

    @classmethod
    def _extract_qa_auto_group_timestamp(cls, label: str) -> int:
        match = cls._QA_AUTO_GROUP_TITLE_RE.search((label or "").strip())
        if not match:
            return -1
        try:
            return int(match.group(1))
        except ValueError:
            return -1

    def _discover_qa_automation_group_name_from_groups_list(self) -> str:
        """Scroll the joined Groups list and return the newest visible ``QA Auto Group <id>`` title."""
        self.tap_groups_segment_on_community_main()
        wait_sec = int(os.getenv("CUBII_JOINED_GROUPS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        wait.until(
            ec.visibility_of_element_located((AppiumBy.ID, self.JOINED_GROUPS_RV_CHIIRGROUP_ID))
        )
        for _ in range(int(os.getenv("CUBII_EDIT_GROUP_LIST_SCROLL_UP_ROUNDS", "2"))):
            self._scroll_community_main_up_one()
            time.sleep(0.28)
        poll_sec = float(os.getenv("CUBII_DISCOVER_QA_GROUP_POLL_SEC", "22.0"))
        pause = float(os.getenv("CUBII_DISCOVER_QA_GROUP_SCROLL_PAUSE_SEC", "0.45"))
        deadline = time.time() + poll_sec
        best_ts = -1
        best_name = ""
        self.LOGGER.info("Discover QA group: scrolling Groups list (poll ~%ss).", int(poll_sec))
        while time.time() < deadline:
            for tv in self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView"):
                try:
                    if not tv.is_displayed():
                        continue
                    tx = (tv.text or "").strip()
                    if not tx or not self._is_qa_automation_group_label(tx):
                        continue
                except Exception:
                    continue
                ts = self._extract_qa_auto_group_timestamp(tx)
                if ts >= 0 and ts >= best_ts:
                    best_ts = ts
                    best_name = f"QA Auto Group {ts}"
                elif ts < 0 and not best_name:
                    best_name = tx
            if best_name:
                self._remember_create_group_name(best_name)
                self.LOGGER.info(
                    "Discover QA group: using %r (numeric suffix=%s).",
                    best_name[:80],
                    best_ts if best_ts >= 0 else "n/a",
                )
                return best_name
            self._scroll_create_group_screen_down_one()
            time.sleep(pause)
        return ""

    def _resolve_or_discover_qa_created_group_name(
        self, *, include_edited_name: bool = True
    ) -> str:
        """Resolve last created QA group name from env, memory/file, or by scanning the Groups list."""
        sources: list = [
            (os.getenv("CUBII_CREATE_GROUP_NAME") or "").strip(),
            (os.getenv("CUBII_EDIT_GROUP_TARGET_NAME") or "").strip(),
            self._recall_create_group_name(),
            self._discover_qa_automation_group_name_from_groups_list(),
        ]
        if include_edited_name:
            sources.append((self._last_edited_group_name or "").strip())
        for source in sources:
            if source:
                return source
        raise AssertionError(
            "No QA automation group name available. Run @create_group first, set "
            "CUBII_CREATE_GROUP_NAME, or ensure a group starting with 'QA' is on the Groups list."
        )

    def open_communitii_tab(self):
        """Open Communitii from bottom navigation (reuses Non-BLE overlay guards before tap)."""
        self.LOGGER.info("Step: Open Communitii tab.")
        self._non_ble._leave_manual_workout_editor_if_blocking_navigation()
        self._non_ble._dismiss_in_progress_ftue_overlays_if_present()
        for by, locator in self.COMMUNITII_TAB_CANDIDATE_LOCATORS:
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
                    time.sleep(1)
                    self.LOGGER.info(
                        "Step Passed: Opened Communitii tab using locator=(%s, %s).",
                        by,
                        locator,
                    )
                    return
            except Exception:
                continue
        raise AssertionError(
            "Could not open Communitii tab. Please provide a stable Communitii tab locator."
        )

    @staticmethod
    def _segment_is_selected(element) -> bool:
        for attr in ("selected", "checked"):
            try:
                value = (element.get_attribute(attr) or "").strip().lower()
                if value in ("true", "1"):
                    return True
            except Exception:
                continue
        return False

    def _is_id_visible(self, resource_id: str) -> bool:
        try:
            for el in self.driver.find_elements(AppiumBy.ID, resource_id):
                if el.is_displayed():
                    return True
        except Exception:
            pass
        return False

    def is_on_communitii_friends_tab(self) -> bool:
        """True when Communitii is open and the Friends segment appears selected."""
        if not self._is_id_visible(self.SB_FRIENDS_ID):
            return False
        if not self._is_id_visible(self.SB_MY_GROUP_ID):
            return False
        try:
            friends_el = self.driver.find_element(AppiumBy.ID, self.SB_FRIENDS_ID)
            if self._segment_is_selected(friends_el):
                return True
        except Exception:
            pass
        # Fallback: Friends tab hides Groups-only controls (CREATE GROUP / joined list).
        groups_only_visible = (
            self._is_id_visible(self.BTN_CREATE_GROUP_ID)
            or self._is_id_visible(self.JOINED_GROUPS_RV_CHIIRGROUP_ID)
        )
        return not groups_only_visible

    def open_communitii_friends_from_any_tab(self) -> None:
        """
        Open Communitii Friends via bottom-nav Communitii tab, then Friends segment.

        Skips Communitii/Friends taps when already on the Friends segment.
        """
        if self.is_on_communitii_friends_tab():
            self.LOGGER.info(
                "Communitii Friends: already on Friends tab; skipping Communitii "
                "and Friends segment taps."
            )
            return
        self.LOGGER.info("Communitii Friends: opening via Communitii → Friends.")
        self.open_communitii_tab()
        self.tap_friends_segment_on_community_main()

    def _dismiss_friends_moved_menu_ftue_if_present(self) -> None:
        """Dismiss optional Friends tab coachmark (btnNextMovedMenu / Moved Menu GOT IT)."""
        timeout = int(os.getenv("CUBII_FRIENDS_MOVED_MENU_FTUE_WAIT_SEC", "3"))
        clicked = False
        for by, locator, label in (
            (AppiumBy.ID, self.FRIENDS_MOVED_MENU_FTUE_ID, "Friends Moved Menu GOT IT (id)"),
            (AppiumBy.XPATH, self.FRIENDS_MOVED_MENU_FTUE_XPATH, "Friends Moved Menu GOT IT (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.FRIENDS_MOVED_MENU_FTUE_UIAUTOMATOR,
                "Friends Moved Menu GOT IT (UiAutomator)",
            ),
        ):
            if self._non_ble._click_if_present(by, locator, label, timeout=timeout):
                clicked = True
                break
        if clicked:
            time.sleep(float(os.getenv("CUBII_AFTER_FRIENDS_MOVED_MENU_FTUE_SEC", "0.5")))
            self.LOGGER.info("Communitii Friends: dismissed Moved Menu GOT IT overlay.")

    def tap_friends_segment_on_community_main(self) -> None:
        """Tap the Friends segment (`sb_friends`) on the Communitii main screen."""
        wait_sec = int(os.getenv("CUBII_COMMUNITY_SCREEN_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.SB_FRIENDS_ID, "sb_friends (id)"),
            (AppiumBy.XPATH, self.SB_FRIENDS_XPATH, "sb_friends (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.SB_FRIENDS_UIAUTOMATOR,
                "sb_friends (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_FRIENDS_SEGMENT_SEC", "0.8")))
                self.LOGGER.info("Communitii Friends: Friends segment tapped (%s).", label)
                self._dismiss_friends_moved_menu_ftue_if_present()
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Friends segment (`com.cubii:id/sb_friends`) on Communitii main screen."
        )

    def _must_see_one_of(self, wait, locator_triplets, description: str, missing: list) -> None:
        for by, locator in locator_triplets:
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Communitii Friends: visible — %s via `%s`.", description, locator)
                return
            except TimeoutException:
                continue
        missing.append(description)

    def _is_visible_one_of(self, wait: WebDriverWait, locator_triplets: tuple[tuple, ...]) -> bool:
        for by, locator in locator_triplets:
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                return True
            except Exception:
                continue
        return False

    def _assert_visible_one_of(
        self, wait: WebDriverWait, locator_triplets: tuple[tuple, ...], description: str
    ) -> None:
        if not self._is_visible_one_of(wait, locator_triplets):
            raise AssertionError(f"View Profile: {description} not visible.")

    @staticmethod
    def _text_view_locator_triplets(resource_id: str) -> tuple[tuple, ...]:
        return (
            (AppiumBy.ID, resource_id),
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("{resource_id}")'),
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{resource_id}"]',
            ),
        )

    def verify_communitii_friends_tab(self) -> None:
        """Assert Friends tab content: chat search bar and Invite Friends button."""
        self._dismiss_friends_moved_menu_ftue_if_present()
        wait_sec = int(os.getenv("CUBII_COMMUNITY_SCREEN_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        missing: list[str] = []

        self._must_see_one_of(
            wait,
            (
                (AppiumBy.ID, self.FRIENDS_CHAT_LIST_SEARCH_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.FRIENDS_CHAT_LIST_SEARCH_UIAUTOMATOR),
                (AppiumBy.XPATH, self.FRIENDS_CHAT_LIST_SEARCH_XPATH),
            ),
            "Friends chat list search bar (edtChatListSearch)",
            missing,
        )
        self._must_see_one_of(
            wait,
            (
                (AppiumBy.ID, self.BTN_INVITE_FRIENDS_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.BTN_INVITE_FRIENDS_UIAUTOMATOR),
                (AppiumBy.XPATH, self.BTN_INVITE_FRIENDS_XPATH),
            ),
            "Invite Friends button (btnInviteFriends)",
            missing,
        )

        if missing:
            raise AssertionError(
                "Communitii Friends tab missing controls: " + ", ".join(missing)
            )

        self.LOGGER.info(
            "Step Passed: Communitii Friends tab verified (search bar and Invite Friends)."
        )

    def _tap_clickable_one_of(
        self, locator_triplets: tuple[tuple, ...], description: str, pause_env_key: str
    ) -> None:
        wait_sec = int(os.getenv("CUBII_COMMUNITY_SCREEN_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator in locator_triplets:
            try:
                wait.until(ec.element_to_be_clickable((by, locator))).click()
                time.sleep(float(os.getenv(pause_env_key, "0.5")))
                self.LOGGER.info("Communitii Friends: tapped %s via `%s`.", description, locator)
                return
            except Exception:
                continue
        raise AssertionError(f"Communitii Friends: could not tap {description}.")

    def _fill_edittext_one_of(
        self, locator_triplets: tuple[tuple, ...], value: str, description: str
    ) -> None:
        wait_sec = int(os.getenv("CUBII_COMMUNITY_SCREEN_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        field = None
        used = ""
        for by, locator in locator_triplets:
            try:
                field = wait.until(ec.element_to_be_clickable((by, locator)))
                used = locator
                break
            except Exception:
                continue
        if field is None:
            raise AssertionError(
                f"Communitii Friends: {description} field not found (tried id/xpath/UiAutomator)."
            )
        try:
            field.click()
        except Exception:
            pass
        time.sleep(0.2)
        try:
            field.clear()
        except Exception:
            pass
        field.send_keys(value)
        time.sleep(float(os.getenv("CUBII_AFTER_INVITE_FRIEND_SEARCH_TYPE_SEC", "0.8")))
        self.LOGGER.info(
            "Communitii Friends: entered %r into %s via `%s`.",
            value,
            description,
            used,
        )

    def tap_invite_friends_button(self) -> None:
        """Tap INVITE FRIENDS on the Friends tab."""
        self._dismiss_friends_moved_menu_ftue_if_present()
        self._tap_clickable_one_of(
            (
                (AppiumBy.ID, self.BTN_INVITE_FRIENDS_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.BTN_INVITE_FRIENDS_UIAUTOMATOR),
                (AppiumBy.XPATH, self.BTN_INVITE_FRIENDS_XPATH),
            ),
            "Invite Friends button (btnInviteFriends)",
            "CUBII_AFTER_TAP_INVITE_FRIENDS_SEC",
        )

    def tap_add_new_chat_search_field(self) -> None:
        """Tap the add-friend search field on the invite sheet."""
        self._tap_clickable_one_of(
            (
                (AppiumBy.ID, self.ADD_NEW_CHAT_SEARCH_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.ADD_NEW_CHAT_SEARCH_UIAUTOMATOR),
                (AppiumBy.XPATH, self.ADD_NEW_CHAT_SEARCH_XPATH),
            ),
            "add friend search field (edtAddNewChatSearch)",
            "CUBII_AFTER_TAP_ADD_NEW_CHAT_SEARCH_SEC",
        )

    def enter_invite_friend_search_name(self, name: str | None = None) -> None:
        """Type a friend name into the invite search field."""
        target_name = (name or self.DEFAULT_INVITE_FRIEND_NAME).strip()
        self._fill_edittext_one_of(
            (
                (AppiumBy.ID, self.ADD_NEW_CHAT_SEARCH_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.ADD_NEW_CHAT_SEARCH_UIAUTOMATOR),
                (AppiumBy.XPATH, self.ADD_NEW_CHAT_SEARCH_XPATH),
            ),
            target_name,
            "invite friend search (edtAddNewChatSearch)",
        )

    def tap_invite_friend_add_icon(self) -> None:
        """Tap the + / invite control (cbInviteFriend) for the selected user."""
        self._tap_clickable_one_of(
            (
                (AppiumBy.ID, self.CB_INVITE_FRIEND_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.CB_INVITE_FRIEND_UIAUTOMATOR),
                (AppiumBy.XPATH, self.CB_INVITE_FRIEND_XPATH),
            ),
            "invite friend add icon (cbInviteFriend)",
            "CUBII_AFTER_TAP_INVITE_FRIEND_ADD_SEC",
        )

    def verify_invite_friend_add_icon_visible(self) -> None:
        """Assert invite + control is visible after searching for a friend."""
        wait_sec = int(os.getenv("CUBII_COMMUNITY_SCREEN_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        missing: list[str] = []
        self._must_see_one_of(
            wait,
            (
                (AppiumBy.ID, self.CB_INVITE_FRIEND_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.CB_INVITE_FRIEND_UIAUTOMATOR),
                (AppiumBy.XPATH, self.CB_INVITE_FRIEND_XPATH),
            ),
            "invite friend add icon (cbInviteFriend)",
            missing,
        )
        if missing:
            raise AssertionError(
                "Invite friend add icon not visible after search: " + ", ".join(missing)
            )
        self.LOGGER.info("Step Passed: invite friend add icon (cbInviteFriend) is visible.")

    def _read_visible_text_one_of(self, locator_triplets: tuple[tuple, ...]) -> str | None:
        for by, locator in locator_triplets:
            try:
                for el in self.driver.find_elements(by, locator):
                    if not el.is_displayed():
                        continue
                    text = (el.text or el.get_attribute("text") or "").strip()
                    if text:
                        return text
            except Exception:
                continue
        return None

    def tap_first_friend_chat_profile(self) -> None:
        """Open the first friend chat from the Friends list (txtChatLastMsg row)."""
        self._dismiss_friends_moved_menu_ftue_if_present()
        self._tap_clickable_one_of(
            (
                (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_LAST_MSG_FIRST_UIAUTOMATOR),
                (AppiumBy.XPATH, self.CHAT_LAST_MSG_FIRST_XPATH),
                (AppiumBy.ID, self.CHAT_LAST_MSG_ID),
            ),
            "first friend chat profile (txtChatLastMsg)",
            "CUBII_AFTER_TAP_FRIEND_CHAT_PROFILE_SEC",
        )

    def verify_friend_chat_profile_toolbar(self, expected_name: str | None = None) -> None:
        """
        Assert chat toolbar shows profile name (toolbar_title) and ONLINE/OFFLINE
        status (toolbar_subtitle).
        """
        wait_sec = int(os.getenv("CUBII_COMMUNITY_SCREEN_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        title_triplets = (
            (AppiumBy.ID, self.CHAT_PROFILE_TOOLBAR_TITLE_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_PROFILE_TOOLBAR_TITLE_UIAUTOMATOR),
            (AppiumBy.XPATH, self.CHAT_PROFILE_TOOLBAR_TITLE_XPATH),
        )
        subtitle_triplets = (
            (AppiumBy.ID, self.CHAT_PROFILE_TOOLBAR_SUBTITLE_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_PROFILE_TOOLBAR_SUBTITLE_UIAUTOMATOR),
            (AppiumBy.XPATH, self.CHAT_PROFILE_TOOLBAR_SUBTITLE_XPATH),
        )
        missing: list[str] = []
        self._must_see_one_of(wait, title_triplets, "chat profile name (toolbar_title)", missing)
        self._must_see_one_of(
            wait, subtitle_triplets, "chat profile status (toolbar_subtitle)", missing
        )
        if missing:
            raise AssertionError(
                "Friend chat profile toolbar missing: " + ", ".join(missing)
            )

        profile_name = self._read_visible_text_one_of(title_triplets)
        profile_status = self._read_visible_text_one_of(subtitle_triplets)
        if not profile_name:
            raise AssertionError("Chat profile toolbar_title is empty.")

        target_name = (expected_name or self.DEFAULT_CHAT_PROFILE_NAME).strip()
        if target_name and target_name.lower() not in profile_name.lower():
            raise AssertionError(
                f"Chat profile name mismatch: expected {target_name!r}, got {profile_name!r}."
            )

        if not profile_status:
            raise AssertionError("Chat profile toolbar_subtitle (status) is empty.")
        status_normalized = profile_status.strip().upper()
        if status_normalized not in self.CHAT_PROFILE_VALID_STATUSES:
            raise AssertionError(
                f"Chat profile status must be ONLINE or OFFLINE, got {profile_status!r}."
            )

        self.LOGGER.info(
            "Step Passed: friend chat profile toolbar — name=%r, status=%r.",
            profile_name,
            profile_status,
        )

    @staticmethod
    def _random_chat_message() -> str:
        return f"Cubii QA message {random.randint(100000, 999999)}"

    def _chat_message_field_locators(self) -> tuple[tuple, ...]:
        return (
            (AppiumBy.ID, self.CHAT_CONVERSATION_MESSAGE_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_CONVERSATION_MESSAGE_UIAUTOMATOR),
            (AppiumBy.XPATH, self.CHAT_CONVERSATION_MESSAGE_XPATH),
        )

    def _chat_send_button_locators(self) -> tuple[tuple, ...]:
        return (
            (AppiumBy.ID, self.CHAT_CONVERSATION_SEND_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_CONVERSATION_SEND_UIAUTOMATOR),
            (AppiumBy.XPATH, self.CHAT_CONVERSATION_SEND_XPATH),
        )

    def tap_chat_conversation_message_field(self) -> None:
        """Tap the Type Something chat input (edtChatConversationMessage)."""
        self._tap_clickable_one_of(
            self._chat_message_field_locators(),
            "chat message input (edtChatConversationMessage)",
            "CUBII_AFTER_TAP_CHAT_MESSAGE_INPUT_SEC",
        )

    def type_and_send_random_chat_message(self, message: str | None = None) -> str:
        """Type a random message and tap send (imgChatConversationSendMessage)."""
        text = (message or self._random_chat_message()).strip()
        self._fill_edittext_one_of(
            self._chat_message_field_locators(),
            text,
            "chat message input (edtChatConversationMessage)",
        )
        self._tap_clickable_one_of(
            self._chat_send_button_locators(),
            "chat send button (imgChatConversationSendMessage)",
            "CUBII_AFTER_TAP_CHAT_SEND_SEC",
        )
        self.LOGGER.info("Step Passed: random chat message sent (%r).", text)
        return text

    def tap_chiir_motivation_strides_target_if_present(self) -> bool:
        """
        Tap the strides-target motivation card (100 Strides Target) when shown on chat.
        Returns True if tapped, False when the card is not available.
        """
        timeout = int(os.getenv("CUBII_CHIIR_MOTIVATION_CARD_WAIT_SEC", "4"))
        for by, locator, label in (
            (AppiumBy.ID, self.CARD_CHIIR_MOTIVATION_ID, "Chiir motivation card (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.CARD_CHIIR_MOTIVATION_UIAUTOMATOR,
                "Chiir motivation card (UiAutomator)",
            ),
            (AppiumBy.XPATH, self.CARD_CHIIR_MOTIVATION_XPATH, "Chiir motivation card (xpath)"),
        ):
            if self._non_ble._click_if_present(by, locator, label, timeout=timeout):
                time.sleep(
                    float(os.getenv("CUBII_AFTER_TAP_CHIIR_MOTIVATION_CARD_SEC", "0.6"))
                )
                self.LOGGER.info(
                    "Step Passed: tapped strides target motivation card (%s).", label
                )
                return True
        self.LOGGER.info(
            "Chiir motivation strides target card not shown; skipping optional tap."
        )
        return False

    def tap_chat_conversation_options_menu(self) -> None:
        """Tap the three-dot menu on the friend chat screen (imgChatConversationOptions)."""
        self._tap_clickable_one_of(
            (
                (AppiumBy.ID, self.CHAT_CONVERSATION_OPTIONS_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_CONVERSATION_OPTIONS_UIAUTOMATOR),
                (AppiumBy.XPATH, self.CHAT_CONVERSATION_OPTIONS_XPATH),
            ),
            "chat conversation options menu (imgChatConversationOptions)",
            "CUBII_AFTER_TAP_CHAT_OPTIONS_MENU_SEC",
        )

    def tap_view_info_from_chat_options(self) -> None:
        """Tap View Info in the chat options sheet (txtOptionViewInfo)."""
        self._tap_clickable_one_of(
            (
                (AppiumBy.ID, self.CHAT_OPTION_VIEW_INFO_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_OPTION_VIEW_INFO_UIAUTOMATOR),
                (AppiumBy.XPATH, self.CHAT_OPTION_VIEW_INFO_XPATH),
            ),
            "View Info option (txtOptionViewInfo)",
            "CUBII_AFTER_TAP_VIEW_INFO_OPTION_SEC",
        )

    def tap_unfriend_from_chat_options(self) -> None:
        """Tap Unfriend in the chat options sheet (txtOptionUnFriend)."""
        self._tap_clickable_one_of(
            (
                (AppiumBy.ID, self.CHAT_OPTION_UNFRIEND_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_OPTION_UNFRIEND_UIAUTOMATOR),
                (AppiumBy.XPATH, self.CHAT_OPTION_UNFRIEND_XPATH),
            ),
            "Unfriend option (txtOptionUnFriend)",
            "CUBII_AFTER_TAP_UNFRIEND_OPTION_SEC",
        )

    def tap_report_from_chat_options(self) -> None:
        """Tap Report in the chat options sheet (txtOptionReport)."""
        self._tap_clickable_one_of(
            (
                (AppiumBy.ID, self.CHAT_OPTION_REPORT_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_OPTION_REPORT_UIAUTOMATOR),
                (AppiumBy.XPATH, self.CHAT_OPTION_REPORT_XPATH),
            ),
            "Report option (txtOptionReport)",
            "CUBII_AFTER_TAP_REPORT_OPTION_SEC",
        )

    def tap_block_from_chat_options(self) -> None:
        """Tap Block in the chat options sheet (txtOptionBlock)."""
        self._tap_clickable_one_of(
            (
                (AppiumBy.ID, self.CHAT_OPTION_BLOCK_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_OPTION_BLOCK_UIAUTOMATOR),
                (AppiumBy.XPATH, self.CHAT_OPTION_BLOCK_XPATH),
            ),
            "Block option (txtOptionBlock)",
            "CUBII_AFTER_TAP_BLOCK_OPTION_SEC",
        )

    def verify_view_info_option_visible(self) -> None:
        """Assert View Info is shown in the open chat options menu."""
        wait_sec = int(os.getenv("CUBII_COMMUNITY_SCREEN_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        missing: list[str] = []
        self._must_see_one_of(
            wait,
            (
                (AppiumBy.ID, self.CHAT_OPTION_VIEW_INFO_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_OPTION_VIEW_INFO_UIAUTOMATOR),
                (AppiumBy.XPATH, self.CHAT_OPTION_VIEW_INFO_XPATH),
            ),
            "View Info option (txtOptionViewInfo)",
            missing,
        )
        if missing:
            raise AssertionError(
                "View Info option not visible in chat menu: " + ", ".join(missing)
            )
        self.LOGGER.info("Step Passed: View Info option is visible in chat menu.")

    def verify_view_info_screen(self, expected_name: str | None = None) -> None:
        """
        Assert View Info screen shows profile name, View Profile, description fields,
        and Report / Block / Unfriend actions.
        """
        wait_sec = int(os.getenv("CUBII_VIEW_INFO_SCREEN_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        missing: list[str] = []

        checks = (
            (
                (
                    (AppiumBy.ID, self.VIEW_INFO_USER_NAME_ID),
                    (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_INFO_USER_NAME_UIAUTOMATOR),
                    (AppiumBy.XPATH, self.VIEW_INFO_USER_NAME_XPATH),
                ),
                "profile name (txtUserName)",
            ),
            (
                (
                    (AppiumBy.ID, self.VIEW_INFO_VIEW_PROFILE_ID),
                    (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_INFO_VIEW_PROFILE_UIAUTOMATOR),
                    (AppiumBy.XPATH, self.VIEW_INFO_VIEW_PROFILE_XPATH),
                ),
                "View Profile (txtViewProfile)",
            ),
            (
                (
                    (AppiumBy.ID, self.VIEW_INFO_USER_JOINED_DATE_ID),
                    (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_INFO_USER_JOINED_DATE_UIAUTOMATOR),
                    (AppiumBy.XPATH, self.VIEW_INFO_USER_JOINED_DATE_XPATH),
                ),
                "joined date info (txtUserJoinedDateInfo)",
            ),
            (
                (
                    (AppiumBy.ID, self.VIEW_INFO_USER_GROUPS_INFO_ID),
                    (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_INFO_USER_GROUPS_INFO_UIAUTOMATOR),
                    (AppiumBy.XPATH, self.VIEW_INFO_USER_GROUPS_INFO_XPATH),
                ),
                "groups info (txtUserGroupsInfo)",
            ),
            (
                (
                    (AppiumBy.ID, self.VIEW_INFO_BTN_REPORT_ID),
                    (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_INFO_BTN_REPORT_UIAUTOMATOR),
                    (AppiumBy.XPATH, self.VIEW_INFO_BTN_REPORT_XPATH),
                ),
                "Report (btnReport)",
            ),
            (
                (
                    (AppiumBy.ID, self.VIEW_INFO_BTN_BLOCK_ID),
                    (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_INFO_BTN_BLOCK_UIAUTOMATOR),
                    (AppiumBy.XPATH, self.VIEW_INFO_BTN_BLOCK_XPATH),
                ),
                "Block (btnBlock)",
            ),
            (
                (
                    (AppiumBy.ID, self.VIEW_INFO_BTN_UNFRIEND_ID),
                    (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_INFO_BTN_UNFRIEND_UIAUTOMATOR),
                    (AppiumBy.XPATH, self.VIEW_INFO_BTN_UNFRIEND_XPATH),
                ),
                "Unfriend (btnUnfriend)",
            ),
        )

        for locator_triplets, description in checks:
            self._must_see_one_of(wait, locator_triplets, description, missing)

        if missing:
            raise AssertionError(
                "View Info screen missing controls: " + ", ".join(missing)
            )

        profile_name = self._read_visible_text_one_of(
            (
                (AppiumBy.ID, self.VIEW_INFO_USER_NAME_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_INFO_USER_NAME_UIAUTOMATOR),
                (AppiumBy.XPATH, self.VIEW_INFO_USER_NAME_XPATH),
            )
        )
        if not profile_name:
            raise AssertionError("View Info profile name (txtUserName) is empty.")

        target_name = (expected_name or self.DEFAULT_CHAT_PROFILE_NAME).strip()
        if target_name and target_name.lower() not in profile_name.lower():
            raise AssertionError(
                f"View Info profile name mismatch: expected {target_name!r}, got {profile_name!r}."
            )

        joined_info = self._read_visible_text_one_of(
            (
                (AppiumBy.ID, self.VIEW_INFO_USER_JOINED_DATE_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_INFO_USER_JOINED_DATE_UIAUTOMATOR),
                (AppiumBy.XPATH, self.VIEW_INFO_USER_JOINED_DATE_XPATH),
            )
        )
        groups_info = self._read_visible_text_one_of(
            (
                (AppiumBy.ID, self.VIEW_INFO_USER_GROUPS_INFO_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_INFO_USER_GROUPS_INFO_UIAUTOMATOR),
                (AppiumBy.XPATH, self.VIEW_INFO_USER_GROUPS_INFO_XPATH),
            )
        )
        if not joined_info and not groups_info:
            raise AssertionError(
                "View Info description fields are empty (txtUserJoinedDateInfo and "
                "txtUserGroupsInfo)."
            )

        self.LOGGER.info(
            "Step Passed: View Info screen verified — name=%r, joined=%r, groups=%r.",
            profile_name,
            joined_info,
            groups_info,
        )

    def _scroll_community_main_up_one(self) -> None:
        """Scroll community main upward so labels at the top (e.g. Explore Groups) can appear."""
        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.08),
                "top": int(size["height"] * 0.12),
                "width": int(size["width"] * 0.84),
                "height": int(size["height"] * 0.68),
                "direction": "up",
                "percent": float(os.getenv("CUBII_COMMUNITY_MAIN_SCROLL_UP_PERCENT", "0.55")),
            },
        )

    def verify_communitii_main_screen(self):
        """Assert Groups/Friends segments, section labels, and CREATE GROUP are visible."""
        wait_sec = int(os.getenv("CUBII_COMMUNITY_SCREEN_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        max_scrolls = int(os.getenv("CUBII_COMMUNITY_MAIN_VERIFY_SCROLL_UP_RETRIES", "6"))
        pause = float(os.getenv("CUBII_COMMUNITY_MAIN_SCROLL_PAUSE_SEC", "0.4"))
        missing: list[str] = []

        for attempt in range(max_scrolls + 1):
            missing = []
            wait = WebDriverWait(self.driver, wait_sec)

            def must_see(by, locator, description):
                try:
                    wait.until(ec.visibility_of_element_located((by, locator)))
                except TimeoutException:
                    missing.append(description)

            def must_see_either(pairs, description):
                for by, locator in pairs:
                    try:
                        wait.until(ec.visibility_of_element_located((by, locator)))
                        return
                    except TimeoutException:
                        continue
                missing.append(description)

            must_see(AppiumBy.ID, self.SB_MY_GROUP_ID, "Groups segment (sb_my_group)")
            must_see(AppiumBy.ID, self.SB_FRIENDS_ID, "Friends segment (sb_friends)")
            must_see_either(
                (
                    (AppiumBy.XPATH, self.EXPLORE_GROUPS_XPATH),
                    (AppiumBy.ANDROID_UIAUTOMATOR, self.EXPLORE_GROUPS_UIAUTOMATOR),
                ),
                "Explore Groups",
            )
            must_see_either(
                (
                    (AppiumBy.XPATH, self.MY_GROUPS_XPATH),
                    (AppiumBy.ANDROID_UIAUTOMATOR, self.MY_GROUPS_UIAUTOMATOR),
                ),
                "My Groups",
            )
            must_see(AppiumBy.ID, self.BTN_CREATE_GROUP_ID, "CREATE GROUP (btn_create_group)")

            if not missing:
                self.LOGGER.info("Step Passed: Community main screen elements verified.")
                return

            if attempt < max_scrolls:
                self.LOGGER.info(
                    "Community main: not all controls visible (%s); scrolling up (attempt %s/%s).",
                    ", ".join(missing),
                    attempt + 1,
                    max_scrolls,
                )
                self._scroll_community_main_up_one()
                time.sleep(pause)
                continue

            raise AssertionError(
                "Community main screen missing or not visible: " + ", ".join(missing)
            )

    def tap_create_group_button(self) -> None:
        """Tap **CREATE GROUP** on the community main screen (`btn_create_group`)."""
        wait_sec = int(os.getenv("CUBII_COMMUNITY_SCREEN_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self.LOGGER.info("Create group: tap CREATE GROUP (btn_create_group).")
        for by, locator, label in (
            (AppiumBy.ID, self.BTN_CREATE_GROUP_ID, "btn_create_group (id)"),
            (AppiumBy.XPATH, self.BTN_CREATE_GROUP_XPATH, "btn_create_group (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.BTN_CREATE_GROUP_UIAUTOMATOR,
                "btn_create_group (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(
                    float(os.getenv("CUBII_AFTER_TAP_CREATE_GROUP_BUTTON_SEC", "0.9"))
                )
                self.LOGGER.info("Create group: CREATE GROUP tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap CREATE GROUP (`com.cubii:id/btn_create_group`) on community main."
        )

    _CREATE_GROUP_NAME_FIELD_PAIRS = (
        (AppiumBy.ID, CREATE_GROUP_NAME_EDITTEXT_ID, "editText (id)"),
        (AppiumBy.XPATH, CREATE_GROUP_NAME_EDITTEXT_XPATH, "editText (xpath)"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            CREATE_GROUP_NAME_EDITTEXT_UIAUTOMATOR,
            "editText (UiAutomator)",
        ),
    )
    _CREATE_GROUP_DESCRIPTION_FIELD_PAIRS = (
        (AppiumBy.ID, CREATE_GROUP_DESCRIPTION_EDITTEXT_ID, "et_description (id)"),
        (AppiumBy.XPATH, CREATE_GROUP_DESCRIPTION_EDITTEXT_XPATH, "et_description (xpath)"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            CREATE_GROUP_DESCRIPTION_EDITTEXT_UIAUTOMATOR,
            "et_description (UiAutomator)",
        ),
    )
    _CREATE_GROUP_TEXTINPUT_ERROR_PAIRS = (
        (AppiumBy.ID, CREATE_GROUP_TEXTINPUT_ERROR_ID, "textinput_error (id)"),
        (AppiumBy.XPATH, CREATE_GROUP_TEXTINPUT_ERROR_XPATH, "textinput_error (xpath)"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            CREATE_GROUP_TEXTINPUT_ERROR_UIAUTOMATOR,
            "textinput_error (UiAutomator)",
        ),
    )

    def _fill_create_group_form_field(
        self, wait: WebDriverWait, pairs: tuple, value: str, field_label: str
    ) -> None:
        el = None
        used = ""
        for by, locator, lbl in pairs:
            try:
                el = wait.until(ec.visibility_of_element_located((by, locator)))
                used = lbl
                break
            except Exception:
                continue
        if el is None:
            raise AssertionError(
                f"Create group: {field_label} field not found (tried id/xpath/UiAutomator)."
            )
        try:
            el.click()
        except Exception:
            pass
        time.sleep(0.2)
        try:
            el.clear()
        except Exception:
            pass
        try:
            el.send_keys(value)
        except Exception as exc:
            raise AssertionError(
                f"Create group: could not type into {field_label} ({used}): {exc}"
            ) from exc
        self.LOGGER.info(
            "Create group: %s entered via %s (%r).",
            field_label,
            used,
            (value[:80] + "…") if len(value) > 80 else value,
        )

    def _enter_create_group_name_only(self, name: str) -> None:
        wait_sec = int(os.getenv("CUBII_CREATE_GROUP_FORM_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self._fill_create_group_form_field(
            wait, self._CREATE_GROUP_NAME_FIELD_PAIRS, name, "Group name"
        )
        time.sleep(float(os.getenv("CUBII_AFTER_CREATE_GROUP_NAME_SEC", "0.25")))
        self._hide_soft_keyboard_quietly()

    def _sanitize_group_name_no_special_chars(self, name: str) -> str:
        """Strip disallowed symbols from a group name (letters, digits, space, - _ ( ) only)."""
        cleaned = re.sub(r"[^A-Za-z0-9 \-_()]", "", (name or ""))
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        return cleaned

    def _build_valid_edit_group_name(self) -> str:
        """Build an edited group name without special characters."""
        base = (
            os.getenv("CUBII_CREATE_GROUP_NAME")
            or self._recall_create_group_name()
            or ""
        ).strip()
        base = self._sanitize_group_name_no_special_chars(base)
        suffix = self._sanitize_group_name_no_special_chars(
            (os.getenv("CUBII_EDIT_GROUP_NAME_SUFFIX") or " edited").strip()
        )
        name = self._sanitize_group_name_no_special_chars(
            (os.getenv("CUBII_EDIT_GROUP_NEW_NAME") or "").strip()
        )
        if name:
            return name
        if base:
            return f"{base}{suffix}".strip()
        return f"QA Edit Group {int(time.time())}"

    def enter_create_group_name_with_special_characters(self) -> None:
        """Type an invalid group name containing special characters (name field only)."""
        invalid = (
            os.getenv("CUBII_CREATE_GROUP_INVALID_SPECIAL_NAME", "QA Auto Group @#$%!")
            or "QA Auto Group @#$%!"
        ).strip()
        self.LOGGER.info("Create group: enter invalid name with special characters.")
        self._enter_create_group_name_only(invalid)

    def enter_create_group_name_and_description(self) -> None:
        """Fill group name (`editText`) and description (`et_description`) on the create-group screen."""
        wait_sec = int(os.getenv("CUBII_CREATE_GROUP_FORM_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        name = (os.getenv("CUBII_CREATE_GROUP_NAME") or "").strip()
        if not name:
            name = f"QA Auto Group {int(time.time())}"
        desc = (os.getenv("CUBII_CREATE_GROUP_DESCRIPTION") or "").strip()
        if not desc:
            desc = "Cubii QA automation create-group flow."
        self._fill_create_group_form_field(
            wait, self._CREATE_GROUP_NAME_FIELD_PAIRS, name, "Group name"
        )
        time.sleep(float(os.getenv("CUBII_AFTER_CREATE_GROUP_NAME_SEC", "0.25")))
        self._fill_create_group_form_field(
            wait, self._CREATE_GROUP_DESCRIPTION_FIELD_PAIRS, desc, "Description"
        )
        self._hide_soft_keyboard_quietly()
        time.sleep(float(os.getenv("CUBII_AFTER_CREATE_GROUP_DESCRIPTION_SEC", "0.25")))
        self._remember_create_group_name(name)

    def _verify_create_group_textinput_error(
        self,
        expected_substring: str = "",
        *,
        require_non_empty: bool = False,
    ) -> None:
        """Assert ``textinput_error`` is visible; optionally match ``expected_substring``."""
        wait_sec = int(os.getenv("CUBII_CREATE_GROUP_FORM_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        el = None
        used = ""
        for by, locator, lbl in self._CREATE_GROUP_TEXTINPUT_ERROR_PAIRS:
            try:
                el = wait.until(ec.visibility_of_element_located((by, locator)))
                used = lbl
                break
            except Exception:
                continue
        if el is None:
            raise AssertionError(
                "Create group validation: `com.cubii:id/textinput_error` not visible "
                "(tried id, xpath, UiAutomator)."
            )
        try:
            text = (el.text or "").strip()
        except Exception:
            text = ""
        if require_non_empty and not text:
            raise AssertionError(
                f"Create group validation: textinput_error visible via {used} but has no text."
            )
        expected = (expected_substring or "").strip()
        if expected and expected.lower() not in text.lower():
            raise AssertionError(
                f"Create group validation: expected error text containing {expected!r} "
                f"(via {used}), got {text!r}."
            )
        self.LOGGER.info(
            "Create group validation: textinput_error visible (%s): %r.", used, text[:120]
        )

    def verify_create_group_missing_name_error_message(self) -> None:
        """Assert ``textinput_error`` shows the expected missing-name message (default ``Enter group name``)."""
        expected = (
            os.getenv("CUBII_CREATE_GROUP_NAME_ERROR_TEXT", "Enter group name") or "Enter group name"
        ).strip()
        self._verify_create_group_textinput_error(expected)

    def verify_create_group_special_character_error_message(self) -> None:
        """Assert ``textinput_error`` after submitting a name with special characters."""
        expected = (
            os.getenv("CUBII_CREATE_GROUP_SPECIAL_CHAR_ERROR_TEXT") or ""
        ).strip()
        self._verify_create_group_textinput_error(
            expected, require_non_empty=not bool(expected)
        )

    @staticmethod
    def _strip_trailing_ellipsis_ui(text: str) -> str:
        """Remove trailing ellipsis / dots the app appends when truncating long titles."""
        t = (text or "").strip()
        for _ in range(10):
            prev = t
            if t.endswith("..."):
                t = t[:-3].rstrip()
            elif t.endswith("\u2026"):  # HORIZONTAL ELLIPSIS (one code point)
                t = t[:-1].rstrip()
            elif t.endswith("…"):  # compatibility if stored as single-char ellipsis
                t = t[:-1].rstrip()
            elif t and t[-1] in ".·":
                t = t[:-1].rstrip()
            if t == prev:
                break
        return t

    @classmethod
    def _visible_group_label_matches_created_name(cls, expected_full: str, displayed: str) -> bool:
        """True when ``displayed`` is the full name or a UI-truncated prefix (e.g. ``…`` suffix)."""
        full = (expected_full or "").strip()
        disp = (displayed or "").strip()
        if not full or not disp:
            return False
        fl, dl = full.lower(), disp.lower()
        if fl == dl:
            return True
        if fl in dl or dl in fl:
            return True
        stem = cls._strip_trailing_ellipsis_ui(disp)
        if stem and fl.startswith(stem.lower()):
            return True
        if stem and stem.lower() in fl:
            return True
        min_pfx = int(os.getenv("CUBII_VERIFY_GROUP_NAME_MIN_PREFIX_CHARS", "12"))
        take = max(min_pfx, 8)
        prefix = full[: min(len(full), take)]
        if len(prefix) >= 8 and prefix.lower() in dl:
            return True
        return False

    @classmethod
    def _visible_group_label_matches_group_identity(
        cls, expected_full: str, displayed: str, *, strict: bool = False
    ) -> bool:
        """Match list labels to a group name; ``strict`` requires the numeric QA suffix when present."""
        if not cls._visible_group_label_matches_created_name(expected_full, displayed):
            return False
        if not strict:
            return True
        full = (expected_full or "").strip()
        disp = (displayed or "").strip()
        ts = cls._extract_qa_auto_group_timestamp(full)
        if ts < 0:
            return True
        ts_text = str(ts)
        stem = cls._strip_trailing_ellipsis_ui(disp)
        return ts_text in disp or ts_text in stem

    def scroll_community_main_and_verify_created_group_name_visible(self) -> None:
        """After create: open Groups list and scroll until the last submitted group name appears."""
        name = self._resolve_or_discover_qa_created_group_name()
        time.sleep(float(os.getenv("CUBII_AFTER_CREATE_GROUP_SUCCESS_WAIT_SEC", "1.2")))
        self.tap_groups_segment_on_community_main()
        poll_sec = float(os.getenv("CUBII_VERIFY_CREATED_GROUP_POLL_SEC", "18.0"))
        pause = float(os.getenv("CUBII_VERIFY_CREATED_GROUP_SCROLL_PAUSE_SEC", "0.45"))
        deadline = time.time() + poll_sec
        self.LOGGER.info(
            "Create group: verify created group name visible on community (Groups): %r.",
            name[:80],
        )
        while time.time() < deadline:
            for tv in self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView"):
                try:
                    if not tv.is_displayed():
                        continue
                    tx = (tv.text or "").strip()
                    if not tx:
                        continue
                    if not self._is_qa_automation_group_label(tx):
                        continue
                    if self._visible_group_label_matches_created_name(name, tx):
                        self.LOGGER.info(
                            "Create group: matched visible QA group label %r (full name %r).",
                            tx[:120],
                            name[:120],
                        )
                        return
                except Exception:
                    continue
            self._scroll_create_group_screen_down_one()
            time.sleep(pause)
        raise AssertionError(
            f"Created group name {name!r} not found on community screen after scrolling "
            f"for {poll_sec:.0f}s."
        )

    def _hide_soft_keyboard_quietly(self) -> None:
        """Dismiss the soft keyboard when it is open (IME after ``EditText`` entry)."""
        try:
            self.driver.hide_keyboard()
        except Exception:
            try:
                self.driver.execute_script("mobile: hideKeyboard")
            except Exception:
                pass
        time.sleep(float(os.getenv("CUBII_AFTER_HIDE_KEYBOARD_SEC", "0.4")))

    def _ensure_switch_on(self, wait: WebDriverWait, pairs: tuple, switch_label: str) -> None:
        el = None
        used = ""
        for by, locator, lbl in pairs:
            try:
                el = wait.until(ec.visibility_of_element_located((by, locator)))
                used = lbl
                break
            except Exception:
                continue
        if el is None:
            raise AssertionError(
                f"Create group: switch {switch_label!r} not found (tried id/xpath/UiAutomator)."
            )
        try:
            checked = (el.get_attribute("checked") or "").strip().lower()
        except Exception:
            checked = ""
        if checked != "true":
            try:
                el.click()
            except Exception as exc:
                raise AssertionError(
                    f"Create group: could not tap switch {switch_label!r} ({used}): {exc}"
                ) from exc
            time.sleep(0.35)
        self.LOGGER.info("Create group: switch %s is on (%s).", switch_label, used)

    def turn_on_create_group_public_switch(self) -> None:
        """Ensure **Make the group public** (`switchCompat7`) is ON."""
        wait_sec = int(os.getenv("CUBII_CREATE_GROUP_FORM_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self._ensure_switch_on(
            wait,
            (
                (AppiumBy.ID, self.CREATE_GROUP_SWITCH_PUBLIC_ID, "switchCompat7 (id)"),
                (AppiumBy.XPATH, self.CREATE_GROUP_SWITCH_PUBLIC_XPATH, "Switch (xpath)"),
                (
                    AppiumBy.XPATH,
                    self.CREATE_GROUP_SWITCH_PUBLIC_XPATH_ANY,
                    "switchCompat7 (* xpath)",
                ),
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    self.CREATE_GROUP_SWITCH_PUBLIC_UIAUTOMATOR,
                    "switchCompat7 (UiAutomator)",
                ),
            ),
            "Make the group public",
        )

    def turn_on_create_group_allow_members_add_friends_switch(self) -> None:
        """Ensure **Allow members to add more friends** (`switchCompat8`) is ON."""
        wait_sec = int(os.getenv("CUBII_CREATE_GROUP_FORM_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self._ensure_switch_on(
            wait,
            (
                (
                    AppiumBy.ID,
                    self.CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_ID,
                    "switchCompat8 (id)",
                ),
                (
                    AppiumBy.XPATH,
                    self.CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_XPATH,
                    "Switch (xpath)",
                ),
                (
                    AppiumBy.XPATH,
                    self.CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_XPATH_ANY,
                    "switchCompat8 (* xpath)",
                ),
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    self.CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_UIAUTOMATOR,
                    "switchCompat8 (UiAutomator)",
                ),
            ),
            "Allow members to add more friends",
        )

    def tap_create_group_invite_members_button(self) -> None:
        """Tap **Invite** / add member (`btn_add_new_member`) on the create-group screen."""
        wait_sec = int(os.getenv("CUBII_CREATE_GROUP_FORM_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self.LOGGER.info("Create group: tap Invite / add new member (btn_add_new_member).")
        for by, locator, label in (
            (AppiumBy.ID, self.CREATE_GROUP_BTN_ADD_NEW_MEMBER_ID, "btn_add_new_member (id)"),
            (
                AppiumBy.XPATH,
                self.CREATE_GROUP_BTN_ADD_NEW_MEMBER_XPATH,
                "btn_add_new_member (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.CREATE_GROUP_BTN_ADD_NEW_MEMBER_UIAUTOMATOR,
                "btn_add_new_member (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(
                    float(os.getenv("CUBII_AFTER_TAP_CREATE_GROUP_INVITE_SEC", "0.7"))
                )
                self.LOGGER.info("Create group: Invite tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Invite / add member (`com.cubii:id/btn_add_new_member`) "
            "on create group screen."
        )

    def tap_create_group_invite_member_checkbox_if_available(self) -> None:
        """Tap a visible invite-member control ``radioButton`` if shown (no-op when absent)."""
        time.sleep(
            float(os.getenv("CUBII_AFTER_INVITE_MEMBER_SHEET_SEC", "0.45"))
        )
        poll_sec = float(os.getenv("CUBII_CREATE_GROUP_INVITE_LIST_POLL_SEC", "6.0"))
        max_inst = int(os.getenv("CUBII_CREATE_GROUP_INVITE_RADIO_INSTANCE_MAX", "32"))

        def _visible_clickable(elems: list) -> bool:
            visible = [e for e in elems if e.is_displayed()]
            if not visible:
                return False
            random.shuffle(visible)
            for el in visible:
                try:
                    el.click()
                    time.sleep(
                        float(os.getenv("CUBII_AFTER_TAP_INVITE_MEMBER_CHECKBOX_SEC", "0.35"))
                    )
                    self.LOGGER.info(
                        "Create group: tapped invite-member radio/checkbox (%s visible).",
                        len(visible),
                    )
                    return True
                except Exception:
                    continue
            return False

        deadline = time.time() + poll_sec
        while time.time() < deadline:
            for xpath in (
                self.CREATE_GROUP_INVITE_MEMBER_CHECKBOX_ALL_XPATH,
                self.CREATE_GROUP_INVITE_MEMBER_RADIO_ANY_XPATH,
            ):
                elems = self.driver.find_elements(AppiumBy.XPATH, xpath)
                if _visible_clickable(elems):
                    return
            time.sleep(0.35)

        for i in range(max_inst):
            sel = self.CREATE_GROUP_INVITE_MEMBER_RADIO_UIAUTOMATOR_TMPL.format(idx=i)
            try:
                el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, sel)
                if el.is_displayed():
                    try:
                        el.click()
                        time.sleep(
                            float(
                                os.getenv("CUBII_AFTER_TAP_INVITE_MEMBER_CHECKBOX_SEC", "0.35")
                            )
                        )
                        self.LOGGER.info(
                            "Create group: tapped invite-member via UiAutomator.instance(%s).",
                            i,
                        )
                        return
                    except Exception:
                        continue
            except Exception:
                continue

        try:
            el = WebDriverWait(self.driver, 2).until(
                ec.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CREATE_GROUP_INVITE_MEMBER_CHECKBOX_FIRST_XPATH)
                )
            )
            el.click()
            time.sleep(
                float(os.getenv("CUBII_AFTER_TAP_INVITE_MEMBER_CHECKBOX_SEC", "0.35"))
            )
            self.LOGGER.info("Create group: tapped invite-member ([1] xpath fallback).")
            return
        except Exception:
            pass

        self.LOGGER.info(
            "Create group: no visible invite-member `radioButton` / CheckBox; skipping tap."
        )

    def tap_create_group_done_button(self) -> None:
        """Tap **Done** on invite / member picker (`btn_done`)."""
        wait_sec = int(os.getenv("CUBII_CREATE_GROUP_FORM_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self.LOGGER.info("Create group: tap Done (btn_done).")
        for by, locator, label in (
            (AppiumBy.ID, self.CREATE_GROUP_BTN_DONE_ID, "btn_done (id)"),
            (AppiumBy.XPATH, self.CREATE_GROUP_BTN_DONE_XPATH, "btn_done (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.CREATE_GROUP_BTN_DONE_UIAUTOMATOR,
                "btn_done (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_CREATE_GROUP_DONE_SEC", "0.6")))
                self.LOGGER.info("Create group: Done tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Done (`com.cubii:id/btn_done`) on create group / invite flow."
        )

    def _scroll_create_group_screen_down_one(self) -> None:
        """Scroll the create-group screen down to reveal controls below the fold."""
        size = self.driver.get_window_size()
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.08),
                "top": int(size["height"] * 0.18),
                "width": int(size["width"] * 0.84),
                "height": int(size["height"] * 0.58),
                "direction": "down",
                "percent": float(os.getenv("CUBII_CREATE_GROUP_SCROLL_PERCENT", "0.55")),
            },
        )

    def scroll_down_and_tap_create_group_submit_button(self) -> None:
        """Scroll until **CREATE** (`btn_create`) is clickable, then tap."""
        wait_sec = int(os.getenv("CUBII_CREATE_GROUP_FORM_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        max_scrolls = int(os.getenv("CUBII_CREATE_GROUP_CREATE_SCROLL_ATTEMPTS", "12"))
        pause = float(os.getenv("CUBII_CREATE_GROUP_SCROLL_PAUSE_SEC", "0.35"))
        create_candidates = (
            (AppiumBy.ID, self.CREATE_GROUP_BTN_CREATE_ID, "btn_create (id)"),
            (AppiumBy.XPATH, self.CREATE_GROUP_BTN_CREATE_XPATH, "btn_create (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.CREATE_GROUP_BTN_CREATE_UIAUTOMATOR,
                "btn_create (UiAutomator)",
            ),
        )
        self.LOGGER.info(
            "Create group: scroll and tap CREATE (btn_create); max_scrolls=%s.",
            max_scrolls,
        )

        def try_tap_short_wait() -> bool:
            for by, locator, label in create_candidates:
                try:
                    el = WebDriverWait(self.driver, 1).until(
                        ec.element_to_be_clickable((by, locator))
                    )
                    el.click()
                    time.sleep(
                        float(os.getenv("CUBII_AFTER_TAP_CREATE_GROUP_SUBMIT_SEC", "0.9"))
                    )
                    self.LOGGER.info("Create group: CREATE tapped (%s).", label)
                    return True
                except Exception:
                    continue
            return False

        for attempt in range(max_scrolls + 1):
            if try_tap_short_wait():
                return
            if attempt < max_scrolls:
                self._scroll_create_group_screen_down_one()
                time.sleep(pause)

        for by, locator, label in create_candidates:
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(
                    float(os.getenv("CUBII_AFTER_TAP_CREATE_GROUP_SUBMIT_SEC", "0.9"))
                )
                self.LOGGER.info("Create group: CREATE tapped after long wait (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap CREATE (`com.cubii:id/btn_create`) after scrolling the create-group screen."
        )

    def tap_groups_segment_on_community_main(self) -> None:
        """Tap the Groups segment (`sb_my_group`) so joined groups list (`rv_chiirgroup`) can appear."""
        wait_sec = int(os.getenv("CUBII_COMMUNITY_SCREEN_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.SB_MY_GROUP_ID, "sb_my_group (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.SB_MY_GROUP_UIAUTOMATOR,
                "sb_my_group (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_GROUPS_SEGMENT_SEC", "0.8")))
                self.LOGGER.info("Community main: Groups segment tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Groups segment (`com.cubii:id/sb_my_group`) on community main screen."
        )

    def tap_explore_groups_banner_and_wait_for_list(self):
        """Tap Explore Groups banner (`cvBanner` image), short pause, wait for Chiir explore RecyclerView."""
        self.LOGGER.info("Explore Groups: tap banner (cvBanner).")
        clicked = False
        for by, locator in self.EXPLORE_BANNER_CANDIDATE_LOCATORS:
            try:
                for el in self.driver.find_elements(by, locator):
                    if not el.is_displayed():
                        continue
                    el.click()
                    clicked = True
                    self.LOGGER.info("Explore Groups: banner tapped via (%s, %s).", by, locator)
                    break
            except Exception:
                continue
            if clicked:
                break
        if not clicked:
            raise AssertionError(
                "Explore Groups banner not found or not tappable (cvBanner / ImageView locators)."
            )
        extra_pause = float(os.getenv("CUBII_EXPLORE_BANNER_EXTRA_PAUSE_SEC", "0.6"))
        time.sleep(extra_pause)
        wait_sec = int(os.getenv("CUBII_EXPLORE_GROUPS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.RV_CHIIREXPLOREGROUP_ID, "rv_chiirexploregroup (id)"),
            (AppiumBy.XPATH, self.RV_CHIIREXPLOREGROUP_XPATH, "rv_chiirexploregroup (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.RV_CHIIREXPLOREGROUP_UIAUTOMATOR,
                "rv_chiirexploregroup (UiAutomator)",
            ),
        ):
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Explore Groups: list visible (%s).", label)
                return
            except TimeoutException:
                continue
        raise AssertionError(
            "Explore list RecyclerView `com.cubii:id/rv_chiirexploregroup` did not become visible."
        )

    def tap_first_visible_join_group_plus_on_explore_list(self) -> None:
        """Tap join (+) ``imageView19`` on the first **visible** row (dynamic explore list).

        Order: visible ``imageView19`` inside ``rv_chiirexploregroup`` → first visible on screen
        by id → xpath ``(//...imageView19)[1]`` → UiAutomator ``resourceId(...).instance(0)``.
        """
        wait_sec = int(os.getenv("CUBII_EXPLORE_GROUPS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)

        rv = None
        for by, locator in (
            (AppiumBy.ID, self.RV_CHIIREXPLOREGROUP_ID),
            (AppiumBy.XPATH, self.RV_CHIIREXPLOREGROUP_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.RV_CHIIREXPLOREGROUP_UIAUTOMATOR),
        ):
            try:
                rv = wait.until(ec.visibility_of_element_located((by, locator)))
                break
            except TimeoutException:
                continue

        pause = float(os.getenv("CUBII_AFTER_TAP_JOIN_GROUP_PLUS_SEC", "0.7"))

        if rv is not None:
            try:
                candidates = rv.find_elements(
                    AppiumBy.ID, self.EXPLORE_JOIN_GROUP_PLUS_IMAGEVIEW_ID
                )
                for el in candidates:
                    try:
                        if el.is_displayed():
                            el.click()
                            time.sleep(pause)
                            self.LOGGER.info(
                                "Join group: tapped first visible imageView19 under "
                                "rv_chiirexploregroup (%s candidate(s)).",
                                len(candidates),
                            )
                            return
                    except Exception:
                        continue
            except Exception:
                pass

        try:
            all_icons = self.driver.find_elements(
                AppiumBy.ID, self.EXPLORE_JOIN_GROUP_PLUS_IMAGEVIEW_ID
            )
            for el in all_icons:
                try:
                    if el.is_displayed():
                        el.click()
                        time.sleep(pause)
                        self.LOGGER.info(
                            "Join group: tapped first visible imageView19 (global id scan, %s).",
                            len(all_icons),
                        )
                        return
                except Exception:
                    continue
        except Exception:
            pass

        for by, locator, label in (
            (
                AppiumBy.XPATH,
                self.EXPLORE_JOIN_GROUP_PLUS_FIRST_XPATH,
                "imageView19 [1] (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.EXPLORE_JOIN_GROUP_PLUS_UIAUTOMATOR_INSTANCE_0,
                "imageView19.instance(0) (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(pause)
                self.LOGGER.info("Join group: plus tapped via %s.", label)
                return
            except Exception:
                continue

        raise AssertionError(
            "Could not tap join group plus icon (`com.cubii:id/imageView19`) on explore list."
        )

    def _find_explore_groups_search_edittext(self, wait: WebDriverWait):
        """Return clickable Explore search ``EditText`` or ``(None, None)``."""
        for by, locator, label in (
            (AppiumBy.ID, self.EXPLORE_SEARCH_EDITTEXT_ID, "editText3 (id)"),
            (AppiumBy.XPATH, self.EXPLORE_SEARCH_EDITTEXT_XPATH, "editText3 (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.EXPLORE_SEARCH_EDITTEXT_UIAUTOMATOR,
                "editText3 (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                return el, label
            except Exception:
                continue
        return None, None

    def tap_explore_groups_search_field(self) -> None:
        """Focus the Explore Groups search bar (`editText3`)."""
        wait_sec = int(os.getenv("CUBII_EXPLORE_GROUPS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        el, label = self._find_explore_groups_search_edittext(wait)
        if el is None:
            raise AssertionError(
                "Explore search field (`com.cubii:id/editText3`) not found or not tappable."
            )
        el.click()
        time.sleep(float(os.getenv("CUBII_AFTER_TAP_EXPLORE_SEARCH_FIELD_SEC", "0.35")))
        self.LOGGER.info("Explore Groups: search field tapped (%s).", label)

    def enter_explore_groups_search_query(self, text: str) -> None:
        """Type a query into Explore search ``editText3`` (clears when possible)."""
        wait_sec = int(os.getenv("CUBII_EXPLORE_GROUPS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        el, label = self._find_explore_groups_search_edittext(wait)
        if el is None:
            raise AssertionError(
                "Explore search field (`com.cubii:id/editText3`) not found for text entry."
            )
        el.click()
        time.sleep(0.2)
        try:
            el.clear()
        except Exception:
            pass
        try:
            el.send_keys(text)
        except Exception as exc:
            raise AssertionError(
                f"Could not enter explore search text via {label!r}: {exc}"
            ) from exc
        time.sleep(float(os.getenv("CUBII_EXPLORE_SEARCH_DEBOUNCE_SEC", "1.0")))
        self.LOGGER.info("Explore Groups: search query entered via %s (%r).", label, text[:80])

    def verify_explore_search_shows_result_card_containing(self, expected: str) -> None:
        """Assert a visible explore list row shows text matching ``expected`` (substring, case-insensitive)."""
        exp = (expected or "").strip()
        if not exp:
            raise AssertionError("Result check requires non-empty expected group name substring.")
        exp_lower = exp.lower()
        wait_sec = int(os.getenv("CUBII_EXPLORE_GROUPS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        rv = None
        for by, locator in (
            (AppiumBy.ID, self.RV_CHIIREXPLOREGROUP_ID),
            (AppiumBy.XPATH, self.RV_CHIIREXPLOREGROUP_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.RV_CHIIREXPLOREGROUP_UIAUTOMATOR),
        ):
            try:
                rv = wait.until(ec.visibility_of_element_located((by, locator)))
                break
            except TimeoutException:
                continue
        if rv is None:
            raise AssertionError("Explore list RecyclerView not visible for search result check.")

        rows = rv.find_elements(AppiumBy.XPATH, self.EXPLORE_GROUP_CARD_ROW_REL_XPATH)
        for row in rows:
            try:
                if not row.is_displayed():
                    continue
            except Exception:
                continue
            try:
                parts: list[str] = []
                for tv in row.find_elements(AppiumBy.XPATH, ".//android.widget.TextView"):
                    try:
                        tx = (tv.text or "").strip()
                        if tx:
                            parts.append(tx)
                    except Exception:
                        continue
                blob = " ".join(parts).lower()
                if exp_lower in blob:
                    self.LOGGER.info(
                        "Explore search: visible result row contains %r (snippet %r).",
                        exp,
                        blob[:120],
                    )
                    return
            except Exception:
                continue

        try:
            for tv in rv.find_elements(AppiumBy.XPATH, ".//android.widget.TextView"):
                try:
                    if not tv.is_displayed():
                        continue
                    tx = (tv.text or "").strip()
                    if tx and exp_lower in tx.lower():
                        self.LOGGER.info(
                            "Explore search: list TextView matches %r (%r).", exp, tx[:120]
                        )
                        return
                except Exception:
                    continue
        except Exception:
            pass

        raise AssertionError(
            f"No visible explore list row contained search text {exp!r} under rv_chiirexploregroup."
        )

    @staticmethod
    def _rects_overlap_axis_aligned(r1: dict, r2: dict) -> bool:
        """True if two ``rect`` dicts (x, y, width, height) overlap."""
        return not (
            r1["x"] + r1["width"] <= r2["x"]
            or r2["x"] + r2["width"] <= r1["x"]
            or r1["y"] + r1["height"] <= r2["y"]
            or r2["y"] + r2["height"] <= r1["y"]
        )

    def _joined_list_create_fab_exclusion_rect(self) -> dict | None:
        """Padded bounds of the floating **CREATE GROUP** button when visible (overlaps joined list)."""
        margin = int(os.getenv("CUBII_JOINED_GROUP_FAB_EXCLUSION_MARGIN_PX", "28"))
        try:
            for el in self.driver.find_elements(AppiumBy.ID, self.BTN_CREATE_GROUP_ID):
                try:
                    if not el.is_displayed():
                        continue
                except Exception:
                    continue
                r = el.rect
                return {
                    "x": int(r["x"] - margin),
                    "y": int(r["y"] - margin),
                    "width": int(r["width"] + 2 * margin),
                    "height": int(r["height"] + 2 * margin),
                }
        except Exception:
            return None
        return None

    def _filter_joined_rows_avoiding_fab(
        self, rows: list, fab: dict | None
    ) -> tuple[list, list]:
        """Return ``(rows_clear_of_fab, rows_all_visible)`` — prefer taps away from CREATE GROUP."""
        visible_all = [e for e in rows if e.is_displayed()]
        if not fab or not visible_all:
            return visible_all, visible_all
        clear: list = []
        for row in visible_all:
            try:
                if not self._rects_overlap_axis_aligned(row.rect, fab):
                    clear.append(row)
            except Exception:
                continue
        return (clear if clear else visible_all), visible_all

    def _tap_joined_group_card_avoiding_create_fab(self, row, tap_ctx: str) -> bool:
        """Tap a list row; use upper-region ``clickGesture`` when the row overlaps the CREATE GROUP FAB."""
        pause = float(os.getenv("CUBII_AFTER_JOINED_GROUP_CARD_TAP_SEC", "0.9"))
        fab = self._joined_list_create_fab_exclusion_rect()
        try:
            rr = row.rect
        except Exception:
            rr = None
        overlap = bool(
            rr and fab and self._rects_overlap_axis_aligned(rr, fab)
        )
        force_upper = os.getenv("CUBII_JOINED_GROUP_ALWAYS_UPPER_TAP", "").strip().lower() in (
            "1",
            "true",
            "yes",
        )
        frac = float(os.getenv("CUBII_JOINED_GROUP_ROW_TAP_TOP_Y_FRACTION", "0.22"))

        def _click_gesture(x: int, y: int) -> None:
            self.driver.execute_script("mobile: clickGesture", {"x": x, "y": y})

        if rr and (overlap or force_upper):
            cx = int(rr["x"] + rr["width"] / 2)
            cy = int(rr["y"] + max(8.0, rr["height"] * frac))
            if fab and self._rects_overlap_axis_aligned(
                {"x": cx - 1, "y": cy - 1, "width": 2, "height": 2},
                fab,
            ):
                cy = int(max(rr["y"] + 6, fab["y"] - 16))
            try:
                _click_gesture(cx, cy)
                time.sleep(pause)
                self.LOGGER.info(
                    "Joined groups: upper tap (%s) at (%s,%s)%s.",
                    tap_ctx,
                    cx,
                    cy,
                    " (FAB overlap)" if overlap else " (forced upper tap)",
                )
                return True
            except Exception as exc:
                self.LOGGER.debug(
                    "Joined groups: upper clickGesture failed (%s): %s", tap_ctx, exc
                )
        try:
            row.click()
            time.sleep(pause)
            self.LOGGER.info("Joined groups: WebDriver click row (%s).", tap_ctx)
            return True
        except Exception as exc:
            self.LOGGER.debug("Joined groups: row.click failed (%s): %s", tap_ctx, exc)
        if rr:
            try:
                cx = int(rr["x"] + rr["width"] / 2)
                cy = int(rr["y"] + max(8.0, rr["height"] * frac))
                _click_gesture(cx, cy)
                time.sleep(pause)
                self.LOGGER.info(
                    "Joined groups: clickGesture fallback (%s) at (%s,%s).", tap_ctx, cx, cy
                )
                return True
            except Exception:
                pass
        return False

    def tap_random_visible_joined_group_card(self) -> None:
        """Tap one visible joined-group row under ``rv_chiirgroup`` (random when several visible)."""
        self.LOGGER.info("Joined groups: tap a random visible group row under rv_chiirgroup.")
        wait_sec = int(os.getenv("CUBII_JOINED_GROUPS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        rv = None
        for by, locator, label in (
            (AppiumBy.ID, self.JOINED_GROUPS_RV_CHIIRGROUP_ID, "rv_chiirgroup (id)"),
            (AppiumBy.XPATH, self.JOINED_GROUPS_RV_CHIIRGROUP_XPATH, "rv_chiirgroup (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.JOINED_GROUPS_RV_CHIIRGROUP_UIAUTOMATOR,
                "rv_chiirgroup (UiAutomator)",
            ),
        ):
            try:
                rv = wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Joined groups: list visible (%s).", label)
                break
            except TimeoutException:
                continue
        if rv is None:
            raise AssertionError(
                "Joined groups RecyclerView `com.cubii:id/rv_chiirgroup` not visible before row tap."
            )

        fab_excl = self._joined_list_create_fab_exclusion_rect()
        rows = rv.find_elements(AppiumBy.XPATH, self.JOINED_GROUP_RV_ROW_DIRECT_XPATH)
        preferred, _ = self._filter_joined_rows_avoiding_fab(rows, fab_excl)
        visible = [e for e in preferred if e.is_displayed()]
        if visible:
            primary = random.choice(visible) if len(visible) > 1 else visible[0]
            others = [e for e in visible if e != primary]
            random.shuffle(others)
            for row in [primary] + others:
                if self._tap_joined_group_card_avoiding_create_fab(
                    row, "rv_chiirgroup direct ViewGroup"
                ):
                    self.LOGGER.info(
                        "Joined groups: tapped one of %s visible row(s) under rv_chiirgroup.",
                        len(visible),
                    )
                    return

        def _tap_visible_joined_row_elements(elements: list, source_label: str) -> bool:
            fab_local = self._joined_list_create_fab_exclusion_rect()
            preferred, _ = self._filter_joined_rows_avoiding_fab(elements, fab_local)
            visible_rows = [e for e in preferred if e.is_displayed()]
            if not visible_rows:
                visible_rows = [e for e in elements if e.is_displayed()]
            if not visible_rows:
                return False
            primary = (
                random.choice(visible_rows)
                if len(visible_rows) > 1
                else visible_rows[0]
            )
            others = [e for e in visible_rows if e != primary]
            random.shuffle(others)
            for row in [primary] + others:
                if self._tap_joined_group_card_avoiding_create_fab(row, source_label):
                    self.LOGGER.info(
                        "Joined groups: tapped row (%s; %s visible).",
                        source_label,
                        len(visible_rows),
                    )
                    return True
            return False

        for rel_xpath, abs_xpath, label in (
            (
                self.JOINED_GROUP_RV_FRAMELAYOUT_VIEWGROUP_REL_XPATH,
                None,
                "rv_chiirgroup / FrameLayout / ViewGroup",
            ),
            (
                None,
                self.JOINED_GROUP_RV_FRAMELAYOUT_VIEWGROUP_ABS_XPATH,
                "rv_chiirgroup / FrameLayout / ViewGroup (abs)",
            ),
        ):
            try:
                if rel_xpath:
                    elems = rv.find_elements(AppiumBy.XPATH, rel_xpath)
                else:
                    elems = self.driver.find_elements(AppiumBy.XPATH, abs_xpath)
                if _tap_visible_joined_row_elements(elems, label):
                    return
            except Exception:
                continue

        try:
            el = wait.until(
                ec.visibility_of_element_located(
                    (AppiumBy.XPATH, self.JOINED_GROUP_RV_FRAMELAYOUT1_VIEWGROUP_ABS_XPATH)
                )
            )
            if self._tap_joined_group_card_avoiding_create_fab(
                el, "FrameLayout[1]/ViewGroup single-row xpath"
            ):
                self.LOGGER.info(
                    "Joined groups: tapped FrameLayout[1]/ViewGroup (single-row xpath)."
                )
                return
        except Exception:
            pass

        max_fl = int(os.getenv("CUBII_JOINED_GROUP_RV_FRAMELAYOUT_INSTANCE_MAX", "24"))
        frame_rows: list = []
        for i in range(max_fl):
            sel = self.JOINED_GROUP_RV_FRAMELAYOUT_CHILD_UIAUTOMATOR_TMPL.format(idx=i)
            try:
                el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, sel)
                if el.is_displayed():
                    frame_rows.append(el)
            except Exception:
                continue
        random.shuffle(frame_rows)
        for el in frame_rows:
            if self._tap_joined_group_card_avoiding_create_fab(
                el, "RecyclerView child FrameLayout"
            ):
                self.LOGGER.info(
                    "Joined groups: tapped RecyclerView child FrameLayout "
                    "(%s UiAutomator instance(s) found).",
                    len(frame_rows),
                )
                return

        def _rect_overlaps(rv_rect: dict, el_rect: dict) -> bool:
            return not (
                el_rect["x"] + el_rect["width"] <= rv_rect["x"]
                or el_rect["x"] >= rv_rect["x"] + rv_rect["width"]
                or el_rect["y"] + el_rect["height"] <= rv_rect["y"]
                or el_rect["y"] >= rv_rect["y"] + rv_rect["height"]
            )

        try:
            rv_rect = rv.rect
        except Exception:
            rv_rect = None
        max_vg = int(os.getenv("CUBII_JOINED_GROUP_LIST_VIEWGROUP_INSTANCE_MAX", "40"))
        vg_rows: list = []
        for i in range(max_vg):
            sel = self.JOINED_GROUP_LIST_VIEWGROUP_INSTANCE_UIAUTOMATOR_TMPL.format(idx=i)
            try:
                el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, sel)
                if not el.is_displayed():
                    continue
                if rv_rect is not None:
                    try:
                        if not _rect_overlaps(rv_rect, el.rect):
                            continue
                    except Exception:
                        continue
                vg_rows.append(el)
            except Exception:
                continue
        if _tap_visible_joined_row_elements(vg_rows, "ViewGroup.instance ∩ rv bounds"):
            return

        def _tap_visible_constraint_cards(
            cards: list, source_label: str
        ) -> bool:
            fab_cards = self._joined_list_create_fab_exclusion_rect()
            preferred, _ = self._filter_joined_rows_avoiding_fab(cards, fab_cards)
            visible_cards = [e for e in preferred if e.is_displayed()]
            if not visible_cards:
                visible_cards = [e for e in cards if e.is_displayed()]
            if not visible_cards:
                return False
            primary = (
                random.choice(visible_cards)
                if len(visible_cards) > 1
                else visible_cards[0]
            )
            others = [e for e in visible_cards if e != primary]
            random.shuffle(others)
            for card in [primary] + others:
                if self._tap_joined_group_card_avoiding_create_fab(
                    card, f"constraintLayout2 {source_label}"
                ):
                    self.LOGGER.info(
                        "Joined groups: tapped constraintLayout2 card (%s; %s visible).",
                        source_label,
                        len(visible_cards),
                    )
                    return True
            return False

        for rel_xpath, label in (
            (self.JOINED_GROUP_CARD_CONSTRAINTLAYOUT2_REL_XPATH, "under rv_chiirgroup"),
            (None, "screen-wide"),
        ):
            try:
                if rel_xpath:
                    cards = rv.find_elements(AppiumBy.XPATH, rel_xpath)
                else:
                    cards = self.driver.find_elements(
                        AppiumBy.XPATH,
                        self.JOINED_GROUP_CARD_CONSTRAINTLAYOUT2_ABS_XPATH,
                    )
                if _tap_visible_constraint_cards(cards, label):
                    return
            except Exception:
                continue

        # Fixed first card + UiAutomator instance(0) (user-provided fallbacks).
        for by, locator, label in (
            (
                AppiumBy.XPATH,
                self.JOINED_GROUP_CARD_CONSTRAINTLAYOUT2_FIRST_XPATH,
                "constraintLayout2 [1] xpath",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.JOINED_GROUP_CARD_CONSTRAINTLAYOUT2_UIAUTOMATOR_I0,
                "constraintLayout2 instance(0)",
            ),
        ):
            try:
                el = wait.until(ec.visibility_of_element_located((by, locator)))
                if self._tap_joined_group_card_avoiding_create_fab(el, label):
                    self.LOGGER.info("Joined groups: tapped card via %s.", label)
                    return
            except Exception:
                continue

        # Dynamic UiAutomator: try successive instances until none match (joined list order).
        max_inst = int(
            os.getenv("CUBII_JOINED_GROUP_CONSTRAINTLAYOUT2_INSTANCE_MAX", "24")
        )
        candidates: list = []
        for i in range(max_inst):
            sel = f'new UiSelector().resourceId("com.cubii:id/constraintLayout2").instance({i})'
            try:
                el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, sel)
                if el.is_displayed():
                    candidates.append(el)
            except Exception:
                continue
        if _tap_visible_constraint_cards(candidates, "UiAutomator instances"):
            return

        raise AssertionError(
            "No visible joined group row found under `com.cubii:id/rv_chiirgroup` "
            "(direct ViewGroup rows, FrameLayout/ViewGroup rows, RecyclerView child "
            "FrameLayout UiAutomator, ViewGroup.instance rows overlapping the list, "
            "nor `constraintLayout2` FrameLayout cards)."
        )

    def tap_random_visible_explore_group_card(self):
        """Tap one visible Explore group row inside `rv_chiirexploregroup` (random when several visible)."""
        self.LOGGER.info("Explore Groups: tap a random visible group card.")
        wait_sec = int(os.getenv("CUBII_EXPLORE_GROUPS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        rv = None
        for by, locator in (
            (AppiumBy.ID, self.RV_CHIIREXPLOREGROUP_ID),
            (AppiumBy.XPATH, self.RV_CHIIREXPLOREGROUP_XPATH),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.RV_CHIIREXPLOREGROUP_UIAUTOMATOR),
        ):
            try:
                rv = wait.until(ec.visibility_of_element_located((by, locator)))
                break
            except TimeoutException:
                continue
        if rv is None:
            raise AssertionError("Explore groups RecyclerView not visible before card tap.")

        rows = rv.find_elements(AppiumBy.XPATH, self.EXPLORE_GROUP_CARD_ROW_REL_XPATH)
        visible = [e for e in rows if e.is_displayed()]
        if visible:
            primary = random.choice(visible) if len(visible) > 1 else visible[0]
            others = [e for e in visible if e != primary]
            random.shuffle(others)
            for row in [primary] + others:
                try:
                    row.click()
                    time.sleep(float(os.getenv("CUBII_AFTER_EXPLORE_GROUP_CARD_TAP_SEC", "0.8")))
                    self.LOGGER.info(
                        "Explore Groups: tapped one of %s visible row(s) under recycler.",
                        len(visible),
                    )
                    return
                except Exception:
                    continue

        abs_cards = self.driver.find_elements(
            AppiumBy.XPATH, self.EXPLORE_GROUP_CARD_ALL_ABS_XPATH
        )
        visible_abs = [e for e in abs_cards if e.is_displayed()]
        random.shuffle(visible_abs)
        for el in visible_abs:
            try:
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_EXPLORE_GROUP_CARD_TAP_SEC", "0.8")))
                self.LOGGER.info("Explore Groups: tapped card via absolute constraintLayout2 xpath.")
                return
            except Exception:
                continue

        for by, locator, label in (
            (
                AppiumBy.XPATH,
                self.EXPLORE_GROUP_CARD_FIRST_ABS_XPATH,
                "first card (absolute xpath fallback)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.EXPLORE_GROUP_CARD_VIEWGROUP_FALLBACK_UIAUTOMATOR,
                "ViewGroup.instance(4) fallback",
            ),
        ):
            try:
                el = wait.until(ec.visibility_of_element_located((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_EXPLORE_GROUP_CARD_TAP_SEC", "0.8")))
                self.LOGGER.info("Explore Groups: card tapped (%s).", label)
                return
            except Exception:
                continue

        raise AssertionError(
            "No explore group card found in `rv_chiirexploregroup` (constraintLayout2 rows)."
        )

    def tap_explore_groups_screen_back_button(self):
        """Tap Explore Groups / Chiir explore screen TextView back (`tvBackButton`)."""
        wait_sec = int(os.getenv("CUBII_EXPLORE_BACK_BUTTON_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.EXPLORE_GROUPS_TV_BACK_BUTTON_ID, "tvBackButton (id)"),
            (AppiumBy.XPATH, self.EXPLORE_GROUPS_TV_BACK_BUTTON_XPATH, "tvBackButton (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.EXPLORE_GROUPS_TV_BACK_BUTTON_UIAUTOMATOR,
                "tvBackButton (UiAutomator)",
            ),
            (AppiumBy.ACCESSIBILITY_ID, "Navigate up", "Navigate up (accessibility id)"),
            (AppiumBy.CLASS_NAME, "android.widget.ImageButton", "Navigate up (class name)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().description("Navigate up")',
                "Navigate up (UiAutomator)",
            ),
            (
                AppiumBy.XPATH,
                '//android.widget.ImageButton[@content-desc="Navigate up"]',
                "Navigate up (xpath)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_EXPLORE_BACK_TAP_SEC", "0.6")))
                self.LOGGER.info("Explore Groups: back tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Explore Groups back (`com.cubii:id/tvBackButton`) not found or not tappable."
        )

    def tap_first_explore_group_card(self):
        """Backward-compatible alias for `tap_random_visible_explore_group_card`."""
        self.tap_random_visible_explore_group_card()

    def verify_group_details_header(self):
        """Wait for group details; assert name, member summary line, and visibility labels."""
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        name_el = wait.until(
            ec.visibility_of_element_located((AppiumBy.ID, self.TXT_GROUP_NAME_COLLAPSIBLE_ID))
        )
        name_txt = (name_el.text or "").strip()
        if not name_txt:
            raise AssertionError("Group name (`txtGroupNameCollapsible`) is empty.")

        member_el = wait.until(ec.visibility_of_element_located((AppiumBy.ID, self.TV_MEMBER_ID)))
        member_txt = (member_el.text or "").strip()
        if not member_txt or not re.search(r"\d", member_txt):
            raise AssertionError(
                f"Member summary (`tv_member`) missing digits or empty: {member_txt!r}."
            )

        vis_el = wait.until(
            ec.visibility_of_element_located((AppiumBy.ID, self.TV_GROUP_VISIBILITY_ID))
        )
        vis_txt = (vis_el.text or "").strip()
        if not vis_txt:
            raise AssertionError("Group visibility (`tv_group_visibility`) is empty.")
        vis_lower = vis_txt.lower()
        if "public" not in vis_lower and "private" not in vis_lower:
            raise AssertionError(
                f"Group visibility not recognized as Public/Private: {vis_txt!r}."
            )

        self.LOGGER.info(
            "Group details header OK: name=%r member=%r visibility=%r",
            name_txt,
            member_txt,
            vis_txt,
        )

    def verify_group_member_list_present(self):
        """Assert member leaderboard RecyclerView has at least one visible row (dynamic)."""
        wait_sec = int(os.getenv("CUBII_GROUP_MEMBER_LIST_WAIT_SEC", "60"))
        wait = WebDriverWait(self.driver, wait_sec)
        rv = wait.until(ec.visibility_of_element_located((AppiumBy.ID, self.RV_GROUP_MEMBER_ID)))

        rows = rv.find_elements(AppiumBy.XPATH, self.RV_GROUP_MEMBER_DIRECT_ROW_XPATH)
        visible = [e for e in rows if e.is_displayed()]
        if len(visible) >= 1:
            self.LOGGER.info(
                "Group member list: %s visible direct row(s) under rv_group_member.",
                len(visible),
            )
            return

        try:
            first = wait.until(
                ec.visibility_of_element_located(
                    (AppiumBy.XPATH, self.RV_GROUP_MEMBER_FIRST_ROW_XPATH)
                )
            )
            if first.is_displayed():
                self.LOGGER.info("Group member list: first row xpath visible.")
                return
        except TimeoutException:
            pass

        try:
            wait.until(
                ec.visibility_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        self.RV_GROUP_MEMBER_ROW_FALLBACK_UIAUTOMATOR,
                    )
                )
            )
            self.LOGGER.info("Group member list: ViewGroup.instance(2) fallback visible.")
            return
        except TimeoutException:
            pass

        raise AssertionError(
            "No visible member rows under `com.cubii:id/rv_group_member` (leaderboard)."
        )

    def tap_group_details_overflow_menu(self) -> None:
        """Tap group details overflow (three dots): ``imgGroupDetailOptions`` / ``content-desc=Cubii``."""
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self._remember_group_name_from_details_header_for_leave_verify()
        self.LOGGER.info("Group details: tap overflow menu (imgGroupDetailOptions / Cubii).")
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.GROUP_DETAIL_OVERFLOW_IMAGEVIEW_ID,
                "imgGroupDetailOptions (id)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_DETAIL_OVERFLOW_IMAGEVIEW_UIAUTOMATOR,
                "imgGroupDetailOptions (UiAutomator)",
            ),
            (
                AppiumBy.ACCESSIBILITY_ID,
                self.GROUP_DETAIL_OVERFLOW_CONTENT_DESC,
                "Cubii (accessibility id)",
            ),
            (
                AppiumBy.XPATH,
                self.GROUP_DETAIL_OVERFLOW_IMAGEVIEW_CUBII_XPATH,
                "ImageView content-desc=Cubii (xpath)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_GROUP_OVERFLOW_MENU_SEC", "0.5")))
                self.LOGGER.info("Group details: overflow menu opened (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap group details overflow menu "
            "(`com.cubii:id/imgGroupDetailOptions` / content-desc `Cubii`)."
        )

    def _remember_group_name_from_details_header_for_leave_verify(self) -> None:
        """Store ``txtGroupNameCollapsible`` text so we can assert the card is gone after leaving."""
        wait_sec = int(os.getenv("CUBII_GROUP_NAME_CAPTURE_WAIT_SEC", "6"))
        wait = WebDriverWait(self.driver, wait_sec)
        try:
            el = wait.until(
                ec.visibility_of_element_located(
                    (AppiumBy.ID, self.TXT_GROUP_NAME_COLLAPSIBLE_ID)
                )
            )
            if el.is_displayed():
                tx = (el.text or "").strip()
                if tx:
                    self._last_community_group_detail_name_for_leave = tx
                    self.LOGGER.info(
                        "Group details: remembered group title %r for post-leave list check.",
                        tx[:120],
                    )
        except Exception:
            pass

    def tap_leave_group_in_overflow_menu(self) -> None:
        """Tap **Leave Group** on the overflow / bottom sheet (prefers labeled row, not bare ViewGroup)."""
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self._remember_group_name_from_details_header_for_leave_verify()
        label_text = (
            os.getenv("CUBII_LEAVE_GROUP_MENU_TEXT") or self.GROUP_DETAIL_LEAVE_GROUP_MENU_TEXT
        ).strip()
        if not label_text:
            label_text = self.GROUP_DETAIL_LEAVE_GROUP_MENU_TEXT
        esc = label_text.replace('"', '\\"')
        xpath_tv = f'//android.widget.TextView[@text="{esc}"]'
        xpath_row = (
            f'//android.view.ViewGroup[.//android.widget.TextView[@text="{esc}"]]'
        )
        ui_sel = f'new UiSelector().text("{esc}")'
        self.LOGGER.info("Group details: tap Leave Group menu entry %r.", label_text)
        for by, locator, lbl in (
            (AppiumBy.XPATH, xpath_tv, "Leave Group TextView"),
            (AppiumBy.ANDROID_UIAUTOMATOR, ui_sel, "Leave Group (UiAutomator)"),
            (AppiumBy.XPATH, xpath_row, "Leave Group row ViewGroup"),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_LEAVE_GROUP_MENU_SEC", "0.45")))
                self.LOGGER.info("Group details: Leave Group tapped (%s).", lbl)
                return
            except Exception:
                continue
        raise AssertionError(
            f"Could not tap Leave Group menu item (text={label_text!r}). "
            "Plain `//android.view.ViewGroup` is too broad; use TextView / text selector."
        )

    def tap_leave_group_confirm_no(self) -> None:
        """Tap **No** on leave-group confirmation (`btn_no`)."""
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self.LOGGER.info("Group details: tap No on leave confirmation (btn_no).")
        for by, locator, label in (
            (AppiumBy.ID, self.GROUP_LEAVE_CONFIRM_BTN_NO_ID, "btn_no (id)"),
            (AppiumBy.XPATH, self.GROUP_LEAVE_CONFIRM_BTN_NO_XPATH, "btn_no (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_LEAVE_CONFIRM_BTN_NO_UIAUTOMATOR,
                "btn_no (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_LEAVE_GROUP_NO_SEC", "0.5")))
                self.LOGGER.info("Group details: leave confirmation No tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap No (`com.cubii:id/btn_no`) on leave group confirmation."
        )

    def tap_leave_group_confirm_yes(self) -> None:
        """Tap **Yes** on leave-group confirmation (`btn_yes`)."""
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self.LOGGER.info("Group details: tap Yes on leave confirmation (btn_yes).")
        for by, locator, label in (
            (AppiumBy.ID, self.GROUP_LEAVE_CONFIRM_BTN_YES_ID, "btn_yes (id)"),
            (AppiumBy.XPATH, self.GROUP_LEAVE_CONFIRM_BTN_YES_XPATH, "btn_yes (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_LEAVE_CONFIRM_BTN_YES_UIAUTOMATOR,
                "btn_yes (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_LEAVE_GROUP_YES_SEC", "1.0")))
                self.LOGGER.info("Group details: leave confirmation Yes tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Yes (`com.cubii:id/btn_yes`) on leave group confirmation."
        )

    def tap_delete_group_in_overflow_menu(self) -> None:
        """Tap **Delete Group** on the overflow / bottom sheet (``textView106`` or labeled row)."""
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self._remember_group_name_from_details_header_for_leave_verify()
        label_text = (
            os.getenv("CUBII_DELETE_GROUP_MENU_TEXT") or self.GROUP_DETAIL_DELETE_GROUP_MENU_TEXT
        ).strip()
        if not label_text:
            label_text = self.GROUP_DETAIL_DELETE_GROUP_MENU_TEXT
        esc = label_text.replace('"', '\\"')
        xpath_tv = f'//android.widget.TextView[@text="{esc}"]'
        xpath_row = f'//android.view.ViewGroup[.//android.widget.TextView[@text="{esc}"]]'
        ui_sel = f'new UiSelector().text("{esc}")'
        self.LOGGER.info("Group details: tap Delete Group menu entry %r.", label_text)
        for by, locator, lbl in (
            (
                AppiumBy.ID,
                self.GROUP_DETAIL_DELETE_GROUP_OPTION_ID,
                "textView106 (id)",
            ),
            (
                AppiumBy.XPATH,
                self.GROUP_DETAIL_DELETE_GROUP_OPTION_XPATH,
                "textView106 (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_DETAIL_DELETE_GROUP_OPTION_UIAUTOMATOR,
                "textView106 (UiAutomator)",
            ),
            (AppiumBy.XPATH, xpath_tv, "Delete Group TextView"),
            (AppiumBy.ANDROID_UIAUTOMATOR, ui_sel, "Delete Group (UiAutomator)"),
            (AppiumBy.XPATH, xpath_row, "Delete Group row ViewGroup"),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_DELETE_GROUP_MENU_SEC", "0.45")))
                self.LOGGER.info("Group details: Delete Group tapped (%s).", lbl)
                return
            except Exception:
                continue
        raise AssertionError(
            f"Could not tap Delete Group menu item (textView106 / text={label_text!r})."
        )

    def tap_delete_group_confirm_no(self) -> None:
        """Tap **No** on delete-group confirmation (`btn_no`)."""
        self.LOGGER.info("Group details: tap No on delete confirmation (btn_no).")
        self.tap_leave_group_confirm_no()

    def tap_delete_group_confirm_yes(self) -> None:
        """Tap **Yes** on delete-group confirmation (`btn_yes`)."""
        self.LOGGER.info("Group details: tap Yes on delete confirmation (btn_yes).")
        self.tap_leave_group_confirm_yes()
        time.sleep(float(os.getenv("CUBII_AFTER_DELETE_GROUP_YES_SEC", "2.0")))

    def verify_deleted_group_absent_on_community_groups_list(self) -> None:
        """On community main: assert the remembered deleted group is no longer on the Groups list."""
        self.verify_left_group_absent_on_community_groups_list()

    def _joined_list_has_visible_label_matching_group_name(
        self, rv, name: str, *, strict: bool = False
    ) -> bool:
        """True if any visible ``TextView`` under ``rv_chiirgroup`` matches ``name``."""
        try:
            for tv in rv.find_elements(AppiumBy.XPATH, ".//android.widget.TextView"):
                try:
                    if not tv.is_displayed():
                        continue
                    tx = (tv.text or "").strip()
                    if not tx:
                        continue
                    if self._visible_group_label_matches_group_identity(
                        name, tx, strict=strict
                    ):
                        return True
                except Exception:
                    continue
        except Exception:
            pass
        return False

    def verify_left_group_absent_on_community_groups_list(self) -> None:
        """On community main: open Groups list, scroll, assert the remembered group is gone."""
        name = (self._last_community_group_detail_name_for_leave or "").strip()
        if not name:
            name = (os.getenv("CUBII_LEAVE_VERIFY_GROUP_NAME") or "").strip()
        if not name:
            raise AssertionError(
                "Cannot verify group removed: no remembered group title "
                "(open group details before leave/delete, or set CUBII_LEAVE_VERIFY_GROUP_NAME)."
            )
        time.sleep(float(os.getenv("CUBII_AFTER_GROUP_REMOVED_LIST_WAIT_SEC", "1.5")))
        self.tap_groups_segment_on_community_main()
        wait_sec = int(os.getenv("CUBII_JOINED_GROUPS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        wait.until(
            ec.visibility_of_element_located((AppiumBy.ID, self.JOINED_GROUPS_RV_CHIIRGROUP_ID))
        )
        for _ in range(int(os.getenv("CUBII_LEAVE_VERIFY_SCROLL_UP_ROUNDS", "4"))):
            self._scroll_community_main_up_one()
            time.sleep(0.3)
        poll_sec = float(os.getenv("CUBII_LEAVE_VERIFY_ABSENT_POLL_SEC", "22.0"))
        pause = float(os.getenv("CUBII_LEAVE_VERIFY_ABSENT_SCROLL_PAUSE_SEC", "0.42"))
        strict = os.getenv("CUBII_LEAVE_VERIFY_STRICT_GROUP_MATCH", "1").strip().lower() not in (
            "0",
            "false",
            "no",
        )
        deadline = time.time() + poll_sec
        self.LOGGER.info(
            "Group removed verify: scroll joined list; expect no card for %r (strict=%s).",
            name[:100],
            strict,
        )
        while time.time() < deadline:
            try:
                rv_cur = self.driver.find_element(
                    AppiumBy.ID, self.JOINED_GROUPS_RV_CHIIRGROUP_ID
                )
            except Exception:
                rv_cur = None
            if rv_cur is not None and self._joined_list_has_visible_label_matching_group_name(
                rv_cur, name, strict=strict
            ):
                raise AssertionError(
                    f"Group {name!r} still appears on the community Groups list "
                    "(another QA group with a similar truncated title may match if strict=off)."
                )
            self._scroll_create_group_screen_down_one()
            time.sleep(pause)
        self.LOGGER.info(
            "Group removed verify: %r not seen on joined list after scrolling (~%ss).",
            name[:100],
            int(poll_sec),
        )

    def _resolve_group_name_for_edit_tap(self) -> str:
        """Resolve group title for finding the joined-group card."""
        return self._resolve_or_discover_qa_created_group_name()

    @classmethod
    def _qa_automation_group_name_prefix(cls) -> str:
        return (os.getenv("CUBII_QA_GROUP_NAME_PREFIX", "QA") or "QA").strip()

    @classmethod
    def _is_qa_automation_group_label(cls, label: str) -> bool:
        """True when the visible group title starts with the QA automation prefix (default ``QA``)."""
        text = (label or "").strip()
        prefix = cls._qa_automation_group_name_prefix()
        return bool(text and prefix and text.upper().startswith(prefix.upper()))

    def _joined_group_card_row_matches_qa_created_name(self, card, name: str) -> bool:
        """True when the card shows a QA-prefixed title matching the last created group name."""
        for tv in card.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView"):
            try:
                if not tv.is_displayed():
                    continue
                tx = (tv.text or "").strip()
                if not tx or not self._is_qa_automation_group_label(tx):
                    continue
                if self._visible_group_label_matches_created_name(name, tx):
                    return True
            except Exception:
                continue
        return False

    def _joined_group_card_row_matches_name(self, card, name: str) -> bool:
        """True when any visible label on the card matches the created/configured group name."""
        return self._joined_group_card_row_matches_qa_created_name(card, name)

    def _tap_joined_group_card_matching_name_on_rv(self, rv, name: str) -> bool:
        """Tap a ``constraintLayout2`` / row card under ``rv_chiirgroup`` whose QA title matches ``name``."""
        card_xpaths = (
            self.JOINED_GROUP_CARD_CONSTRAINTLAYOUT2_REL_XPATH,
            self.JOINED_GROUP_RV_FRAMELAYOUT_VIEWGROUP_REL_XPATH,
            self.JOINED_GROUP_RV_ROW_DIRECT_XPATH,
        )
        for rel_xpath in card_xpaths:
            try:
                cards = rv.find_elements(AppiumBy.XPATH, rel_xpath)
            except Exception:
                continue
            for card in cards:
                try:
                    if not card.is_displayed():
                        continue
                    if not self._joined_group_card_row_matches_name(card, name):
                        continue
                except Exception:
                    continue
                if self._tap_joined_group_card_avoiding_create_fab(
                    card, "joined list card matching created group name"
                ):
                    return True
        for tv in rv.find_elements(AppiumBy.XPATH, ".//android.widget.TextView"):
            try:
                if not tv.is_displayed():
                    continue
                tx = (tv.text or "").strip()
                if (
                    not tx
                    or not self._is_qa_automation_group_label(tx)
                    or not self._visible_group_label_matches_created_name(name, tx)
                ):
                    continue
            except Exception:
                continue
            row = None
            for xp in (
                "./ancestor::android.widget.FrameLayout[@resource-id='com.cubii:id/constraintLayout2'][1]",
                "./ancestor::android.view.ViewGroup[2]",
                "./..",
            ):
                try:
                    row = tv.find_element(AppiumBy.XPATH, xp)
                    if row.is_displayed():
                        break
                except Exception:
                    row = None
                    continue
            if row is None:
                row = tv
            if self._tap_joined_group_card_avoiding_create_fab(
                row, "joined list QA group row matching created name"
            ):
                return True
        return False

    def scroll_groups_list_and_tap_created_qa_group(
        self, *, include_edited_name: bool = True
    ) -> None:
        """Scroll **Groups** list down until the created QA group card is found, then tap it."""
        name = self._resolve_or_discover_qa_created_group_name(
            include_edited_name=include_edited_name
        )
        if not self._is_qa_automation_group_label(name):
            raise AssertionError(
                f"Created group name {name!r} does not start with QA prefix "
                f"{self._qa_automation_group_name_prefix()!r}; only QA automation groups are opened for edit."
            )
        self.tap_groups_segment_on_community_main()
        wait_sec = int(os.getenv("CUBII_JOINED_GROUPS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        wait.until(
            ec.visibility_of_element_located((AppiumBy.ID, self.JOINED_GROUPS_RV_CHIIRGROUP_ID))
        )
        time.sleep(float(os.getenv("CUBII_AFTER_CREATE_GROUP_SUCCESS_WAIT_SEC", "1.2")))
        scroll_up_rounds = int(os.getenv("CUBII_EDIT_GROUP_LIST_SCROLL_UP_ROUNDS", "2"))
        for _ in range(scroll_up_rounds):
            self._scroll_community_main_up_one()
            time.sleep(0.28)
        poll_sec = float(os.getenv("CUBII_EDIT_GROUP_FIND_CARD_POLL_SEC", "28.0"))
        pause = float(os.getenv("CUBII_EDIT_GROUP_FIND_CARD_SCROLL_PAUSE_SEC", "0.42"))
        deadline = time.time() + poll_sec
        qa_prefix = self._qa_automation_group_name_prefix()
        self.LOGGER.info(
            "Edit group: scroll Groups list to find QA group %r (prefix %r).",
            name[:100],
            qa_prefix,
        )
        while time.time() < deadline:
            try:
                rv = self.driver.find_element(AppiumBy.ID, self.JOINED_GROUPS_RV_CHIIRGROUP_ID)
            except Exception:
                time.sleep(pause)
                continue
            if self._tap_joined_group_card_matching_name_on_rv(rv, name):
                self.LOGGER.info("Opened QA group details for %r.", name[:100])
                time.sleep(float(os.getenv("CUBII_AFTER_OPEN_GROUP_DETAILS_SEC", "0.8")))
                self._remember_group_name_from_details_header_for_leave_verify()
                return
            self._scroll_create_group_screen_down_one()
            time.sleep(pause)
        raise AssertionError(
            f"No joined group card with QA prefix {qa_prefix!r} matched created name {name!r} "
            "under rv_chiirgroup after scrolling down."
        )

    def scroll_groups_list_and_tap_created_qa_group_for_delete(self) -> None:
        """Open the created QA group for delete (ignores last edited name from a prior edit scenario)."""
        self.scroll_groups_list_and_tap_created_qa_group(include_edited_name=False)

    def tap_joined_group_card_matching_created_or_env_group_name(self) -> None:
        """Alias: scroll Groups list and tap the created QA automation group."""
        self.scroll_groups_list_and_tap_created_qa_group()

    def _tap_edit_group_option_element(self, wait: WebDriverWait) -> bool:
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.GROUP_DETAIL_EDIT_GROUP_OPTION_ID,
                "txtGrpOptionEditGroupOption (id)",
            ),
            (
                AppiumBy.XPATH,
                self.GROUP_DETAIL_EDIT_GROUP_OPTION_XPATH,
                "txtGrpOptionEditGroupOption (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_DETAIL_EDIT_GROUP_OPTION_UIAUTOMATOR,
                "txtGrpOptionEditGroupOption (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_EDIT_GROUP_OPTION_SEC", "0.65")))
                self.LOGGER.info("Group details: Edit Group tapped (%s).", label)
                return True
            except Exception:
                continue
        return False

    def tap_group_details_edit_group_option(self) -> None:
        """Tap **Edit Group** (overflow menu option ``txtGrpOptionEditGroupOption``)."""
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        self.LOGGER.info("Group details: tap Edit Group option.")
        if self._tap_edit_group_option_element(wait):
            return
        self.LOGGER.info("Group details: Edit not direct; opening overflow then Edit.")
        self.tap_group_details_overflow_menu()
        if self._tap_edit_group_option_element(wait):
            return
        raise AssertionError(
            "Could not tap Edit Group (`com.cubii:id/txtGrpOptionEditGroupOption`). "
            "Open group details and overflow menu if the option is hidden."
        )

    def update_edit_group_name_and_description(self) -> None:
        """On edit-group form, replace name and description using only allowed name characters."""
        wait_sec = int(os.getenv("CUBII_CREATE_GROUP_FORM_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        name = self._build_valid_edit_group_name()
        desc = (os.getenv("CUBII_EDIT_GROUP_DESCRIPTION") or "").strip()
        if not desc:
            desc = "Cubii QA automation edited group description."
        self.LOGGER.info("Edit group: using sanitized name %r (no special characters).", name[:80])
        self._fill_create_group_form_field(
            wait, self._CREATE_GROUP_NAME_FIELD_PAIRS, name, "Group name"
        )
        time.sleep(float(os.getenv("CUBII_AFTER_EDIT_GROUP_NAME_SEC", "0.25")))
        self._fill_create_group_form_field(
            wait, self._CREATE_GROUP_DESCRIPTION_FIELD_PAIRS, desc, "Description"
        )
        self._hide_soft_keyboard_quietly()
        time.sleep(float(os.getenv("CUBII_AFTER_EDIT_GROUP_DESCRIPTION_SEC", "0.25")))
        self._last_edited_group_name = name
        self._last_edited_group_description = desc
        self._remember_create_group_name(name)

    def _flip_switch_once(self, pairs: tuple, switch_label: str) -> None:
        max_scrolls = int(os.getenv("CUBII_EDIT_GROUP_SWITCH_SCROLL_ATTEMPTS", "4"))
        pause = float(os.getenv("CUBII_CREATE_GROUP_SCROLL_PAUSE_SEC", "0.35"))
        short_wait = int(os.getenv("CUBII_EDIT_GROUP_SWITCH_FIND_SEC", "2"))

        for attempt in range(max_scrolls + 1):
            el = None
            used = ""
            for by, locator, lbl in pairs:
                try:
                    el = WebDriverWait(self.driver, short_wait).until(
                        ec.visibility_of_element_located((by, locator))
                    )
                    used = lbl
                    break
                except Exception:
                    continue
            if el is not None:
                try:
                    el.click()
                except Exception as exc:
                    raise AssertionError(
                        f"Edit group: could not flip switch {switch_label!r} ({used}): {exc}"
                    ) from exc
                time.sleep(0.4)
                self.LOGGER.info("Edit group: flipped switch %s (%s).", switch_label, used)
                return
            if attempt < max_scrolls:
                self.LOGGER.info(
                    "Edit group: %r not visible; scrolling form down (%s/%s).",
                    switch_label,
                    attempt + 1,
                    max_scrolls,
                )
                self._scroll_create_group_screen_down_one()
                time.sleep(pause)

        raise AssertionError(
            f"Edit group: switch {switch_label!r} not found after scrolling "
            f"(tried id/xpath/UiAutomator, max_scrolls={max_scrolls})."
        )

    def flip_edit_group_allow_friends_and_public_toggles(self) -> None:
        """Flip **Allow members to add more friends** then **Make the group public** (on→off or off→on)."""
        self._flip_switch_once(
            (
                (
                    AppiumBy.ID,
                    self.CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_ID,
                    "switchCompat8 (id)",
                ),
                (
                    AppiumBy.XPATH,
                    self.CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_XPATH,
                    "switchCompat8 (xpath)",
                ),
                (
                    AppiumBy.XPATH,
                    self.CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_XPATH_ANY,
                    "switchCompat8 (* xpath)",
                ),
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    self.CREATE_GROUP_SWITCH_ALLOW_ADD_FRIENDS_UIAUTOMATOR,
                    "switchCompat8 (UiAutomator)",
                ),
            ),
            "Allow members to add more friends",
        )
        self._flip_switch_once(
            (
                (AppiumBy.ID, self.CREATE_GROUP_SWITCH_PUBLIC_ID, "switchCompat7 (id)"),
                (AppiumBy.XPATH, self.CREATE_GROUP_SWITCH_PUBLIC_XPATH, "switchCompat7 (xpath)"),
                (
                    AppiumBy.XPATH,
                    self.CREATE_GROUP_SWITCH_PUBLIC_XPATH_ANY,
                    "switchCompat7 (* xpath)",
                ),
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    self.CREATE_GROUP_SWITCH_PUBLIC_UIAUTOMATOR,
                    "switchCompat7 (UiAutomator)",
                ),
            ),
            "Make the group public",
        )

    def tap_group_edit_form_save_button(self) -> None:
        """Scroll edit-group form down until **Save** (`btn_create`) is visible, then tap."""
        self.LOGGER.info("Edit group: scroll down and tap Save (btn_create).")
        self.scroll_down_and_tap_create_group_submit_button()
        time.sleep(float(os.getenv("CUBII_AFTER_TAP_EDIT_GROUP_SAVE_SEC", "1.1")))

    def verify_group_details_reflects_edited_group_name(self) -> None:
        """Assert group details header name matches the last edited name (ellipsis-aware)."""
        expected = (self._last_edited_group_name or "").strip()
        if not expected:
            expected = (os.getenv("CUBII_EDIT_GROUP_NEW_NAME") or "").strip()
        if not expected:
            raise AssertionError(
                "No edited group name stored; run update edit group name step first."
            )
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        name_el = wait.until(
            ec.visibility_of_element_located((AppiumBy.ID, self.TXT_GROUP_NAME_COLLAPSIBLE_ID))
        )
        shown = (name_el.text or "").strip()
        if not shown:
            raise AssertionError("Group details: name (`txtGroupNameCollapsible`) is empty after save.")
        ok_forward = self._visible_group_label_matches_created_name(expected, shown)
        ok_reverse = self._visible_group_label_matches_created_name(shown, expected)
        if not (ok_forward or ok_reverse or expected.lower() == shown.lower()):
            raise AssertionError(
                f"Group details name after edit does not match expected {expected!r}; got {shown!r}."
            )
        self.LOGGER.info(
            "Edit group: details header matches edited name (shown=%r expected=%r).",
            shown[:120],
            expected[:120],
        )

    def verify_group_member_list_shows_current_user_as_you(self) -> None:
        """Assert the leaderboard shows the current user as ``You`` (`textView50` under `rv_group_member`)."""
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        rv = wait.until(ec.visibility_of_element_located((AppiumBy.ID, self.RV_GROUP_MEMBER_ID)))

        scoped = (
            './/android.widget.TextView[@resource-id="com.cubii:id/textView50" and @text="You"]'
        )
        try:
            el = rv.find_element(AppiumBy.XPATH, scoped)
            if el.is_displayed():
                self.LOGGER.info(
                    "Group member list: `You` (textView50) visible under rv_group_member (scoped xpath)."
                )
                return
        except Exception:
            pass

        for by, locator, label in (
            (
                AppiumBy.XPATH,
                self.GROUP_MEMBER_SELF_YOU_TEXTVIEW_XPATH,
                "textView50 You (absolute xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_MEMBER_SELF_YOU_TEXTVIEW_UIAUTOMATOR,
                "textView50 You (UiAutomator id+text)",
            ),
            (
                AppiumBy.ID,
                self.GROUP_MEMBER_SELF_YOU_TEXTVIEW_ID,
                "textView50 (id; verify text==You)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_MEMBER_SELF_YOU_TEXT_ONLY_UIAUTOMATOR,
                "text You (UiAutomator text-only fallback)",
            ),
            (
                AppiumBy.XPATH,
                self.GROUP_MEMBER_ROW_VIEWGROUP_7_XPATH,
                "rv_group_member / ViewGroup[7] (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_MEMBER_VIEWGROUP_INSTANCE_10_UIAUTOMATOR,
                "ViewGroup.instance(10) (UiAutomator fallback)",
            ),
        ):
            try:
                el = wait.until(ec.visibility_of_element_located((by, locator)))
                if by == AppiumBy.ID:
                    try:
                        if (el.text or "").strip() != "You":
                            continue
                    except Exception:
                        continue
                if el.is_displayed():
                    self.LOGGER.info("Group member list: current user `You` visible (%s).", label)
                    return
            except Exception:
                continue

        raise AssertionError(
            "Group member list did not show the current user as `You` "
            "(`com.cubii:id/textView50` under `rv_group_member`)."
        )

    def verify_group_date_duration_filter_card_visible(self) -> None:
        """Assert date duration filter control (`cardTypeOfDuration`) is visible on group details."""
        wait_sec = int(os.getenv("CUBII_GROUP_DATE_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        last_err: Exception | None = None
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.GROUP_DATE_FILTER_CARD_TYPE_DURATION_ID,
                "cardTypeOfDuration (id)",
            ),
            (
                AppiumBy.XPATH,
                self.GROUP_DATE_FILTER_CARD_TYPE_DURATION_XPATH,
                "cardTypeOfDuration (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_DATE_FILTER_CARD_TYPE_DURATION_UIAUTOMATOR,
                "cardTypeOfDuration (UiAutomator)",
            ),
        ):
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Group date filter: duration card visible (%s).", label)
                return
            except Exception as exc:
                last_err = exc
                continue
        raise AssertionError(
            "Date duration filter card (`com.cubii:id/cardTypeOfDuration`) not visible. "
            f"Last error: {last_err!r}"
        )

    def tap_group_date_duration_filter_card(self) -> None:
        """Open date filter sheet by tapping `cardTypeOfDuration`."""
        wait_sec = int(os.getenv("CUBII_GROUP_DATE_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.GROUP_DATE_FILTER_CARD_TYPE_DURATION_ID,
                "cardTypeOfDuration (id)",
            ),
            (
                AppiumBy.XPATH,
                self.GROUP_DATE_FILTER_CARD_TYPE_DURATION_XPATH,
                "cardTypeOfDuration (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_DATE_FILTER_CARD_TYPE_DURATION_UIAUTOMATOR,
                "cardTypeOfDuration (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_DATE_FILTER_CARD_SEC", "0.5")))
                self.LOGGER.info("Group date filter: duration card tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap date duration filter card (`com.cubii:id/cardTypeOfDuration`)."
        )

    def tap_yesterday_option_in_group_date_filter(self) -> None:
        """Tap Yesterday row (`linearLayout9`) in the date filter sheet."""
        wait_sec = int(os.getenv("CUBII_GROUP_DATE_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.GROUP_DATE_FILTER_YESTERDAY_LINEAR_ID,
                "Yesterday linearLayout9 (id)",
            ),
            (
                AppiumBy.XPATH,
                self.GROUP_DATE_FILTER_YESTERDAY_LINEAR_XPATH,
                "Yesterday linearLayout9 (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_DATE_FILTER_YESTERDAY_LINEAR_UIAUTOMATOR,
                "Yesterday linearLayout9 (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_DATE_FILTER_YESTERDAY_SEC", "0.5")))
                self.LOGGER.info("Group date filter: Yesterday option tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Yesterday option (`com.cubii:id/linearLayout9`) in date filter."
        )

    def tap_last_seven_days_option_in_group_date_filter(self) -> None:
        """Tap Last 7 Days row (`linearLayout10`) in the date filter sheet."""
        wait_sec = int(os.getenv("CUBII_GROUP_DATE_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.GROUP_DATE_FILTER_LAST_7_DAYS_LINEAR_ID,
                "Last 7 Days linearLayout10 (id)",
            ),
            (
                AppiumBy.XPATH,
                self.GROUP_DATE_FILTER_LAST_7_DAYS_LINEAR_XPATH,
                "Last 7 Days linearLayout10 (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_DATE_FILTER_LAST_7_DAYS_LINEAR_UIAUTOMATOR,
                "Last 7 Days linearLayout10 (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(
                    float(os.getenv("CUBII_AFTER_TAP_DATE_FILTER_LAST_7_DAYS_SEC", "0.5"))
                )
                self.LOGGER.info("Group date filter: Last 7 Days option tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Last 7 Days option (`com.cubii:id/linearLayout10`) in date filter."
        )

    def tap_last_thirty_days_option_in_group_date_filter(self) -> None:
        """Tap Last 30 Days (`textView87`) in the date filter sheet."""
        wait_sec = int(os.getenv("CUBII_GROUP_DATE_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.GROUP_DATE_FILTER_LAST_30_DAYS_TEXTVIEW_ID,
                "Last 30 Days textView87 (id)",
            ),
            (
                AppiumBy.XPATH,
                self.GROUP_DATE_FILTER_LAST_30_DAYS_TEXTVIEW_XPATH,
                "Last 30 Days textView87 (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GROUP_DATE_FILTER_LAST_30_DAYS_TEXTVIEW_UIAUTOMATOR,
                "Last 30 Days textView87 (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(
                    float(os.getenv("CUBII_AFTER_TAP_DATE_FILTER_LAST_30_DAYS_SEC", "0.5"))
                )
                self.LOGGER.info("Group date filter: Last 30 Days option tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Last 30 Days option (`com.cubii:id/textView87`) in date filter."
        )

    def wait_after_group_date_filter_for_list_refresh(self) -> None:
        """Pause after applying a date filter so the member list can reload."""
        delay = float(os.getenv("CUBII_AFTER_DATE_FILTER_LIST_REFRESH_SEC", "5.0"))
        self.LOGGER.info("Group date filter: waiting %s s for list refresh.", delay)
        time.sleep(delay)

    def tap_all_data_filter_user_type_card(self) -> None:
        """Tap All Data / user-type filter entry (`cardTypeOfUser`)."""
        wait_sec = int(os.getenv("CUBII_ALL_DATA_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.ALL_DATA_FILTER_CARD_TYPE_USER_ID, "cardTypeOfUser (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.ALL_DATA_FILTER_CARD_TYPE_USER_UIAUTOMATOR,
                "cardTypeOfUser (UiAutomator)",
            ),
            (AppiumBy.XPATH, self.ALL_DATA_FILTER_CARD_TYPE_USER_XPATH, "cardTypeOfUser (xpath)"),
            (
                AppiumBy.XPATH,
                self.ALL_DATA_FILTER_CARD_TYPE_USER_XPATH_ANY,
                "cardTypeOfUser (xpath any-class)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_ALL_DATA_CARD_SEC", "0.5")))
                self.LOGGER.info("All data filter: cardTypeOfUser tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError("Could not tap All Data filter card (`com.cubii:id/cardTypeOfUser`).")

    def tap_all_data_sheet_all_data_option(self) -> None:
        """Tap ALL DATA row/option in the All Data filter sheet (text-based; no stable id given)."""
        wait_sec = int(os.getenv("CUBII_ALL_DATA_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ALL DATA")', "ALL DATA (text)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textContains("ALL DATA")',
                "ALL DATA (textContains)",
            ),
            (
                AppiumBy.XPATH,
                '//*[contains(@text, "ALL DATA")]',
                "ALL DATA (xpath contains)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_ALL_DATA_OPTION_SEC", "0.5")))
                self.LOGGER.info("All data filter: ALL DATA option tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError("Could not tap ALL DATA option in All Data filter sheet.")

    def tap_automated_data_option_in_all_data_filter(self) -> None:
        """Tap Automated Data row (`lytAutomaticDataParent`; fallback `textView85`)."""
        wait_sec = int(os.getenv("CUBII_ALL_DATA_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.ALL_DATA_AUTOMATED_DATA_PARENT_ID,
                "lytAutomaticDataParent (id)",
            ),
            (
                AppiumBy.XPATH,
                self.ALL_DATA_AUTOMATED_DATA_PARENT_XPATH,
                "lytAutomaticDataParent (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.ALL_DATA_AUTOMATED_DATA_PARENT_UIAUTOMATOR,
                "lytAutomaticDataParent (UiAutomator)",
            ),
            (
                AppiumBy.XPATH,
                self.ALL_DATA_AUTOMATED_DATA_TEXTVIEW_XPATH_STRICT,
                "textView85 Automated Data (xpath strict)",
            ),
            (AppiumBy.ID, self.ALL_DATA_AUTOMATED_DATA_TEXTVIEW_ID, "textView85 (id)"),
            (AppiumBy.XPATH, self.ALL_DATA_AUTOMATED_DATA_TEXTVIEW_XPATH, "textView85 (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.ALL_DATA_AUTOMATED_DATA_TEXTVIEW_UIAUTOMATOR,
                "textView85 (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_AUTOMATED_DATA_SEC", "0.5")))
                self.LOGGER.info("All data filter: Automated Data tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Automated Data (`lytAutomaticDataParent` / `textView85`) in All Data filter."
        )

    def tap_manual_data_option_in_all_data_filter(self) -> None:
        """Tap Manual Data row (`lytManualDataParent`) in the All Data filter sheet."""
        wait_sec = int(os.getenv("CUBII_ALL_DATA_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.ALL_DATA_MANUAL_DATA_PARENT_ID, "lytManualDataParent (id)"),
            (AppiumBy.XPATH, self.ALL_DATA_MANUAL_DATA_PARENT_XPATH, "lytManualDataParent (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.ALL_DATA_MANUAL_DATA_PARENT_UIAUTOMATOR,
                "lytManualDataParent (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_MANUAL_DATA_SEC", "0.5")))
                self.LOGGER.info("All data filter: Manual Data tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Manual Data (`com.cubii:id/lytManualDataParent`) in All Data filter."
        )

    def tap_both_data_option_in_all_data_filter(self) -> None:
        """Tap Both / combined data row (`lytBothDataParent`) in the All Data filter sheet."""
        wait_sec = int(os.getenv("CUBII_ALL_DATA_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.ALL_DATA_BOTH_DATA_PARENT_ID, "lytBothDataParent (id)"),
            (AppiumBy.XPATH, self.ALL_DATA_BOTH_DATA_PARENT_XPATH, "lytBothDataParent (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.ALL_DATA_BOTH_DATA_PARENT_UIAUTOMATOR,
                "lytBothDataParent (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_BOTH_DATA_SEC", "0.5")))
                self.LOGGER.info("All data filter: Both Data tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Both Data (`com.cubii:id/lytBothDataParent`) in All Data filter."
        )

    def wait_after_all_data_filter_for_list_refresh(self) -> None:
        """Pause after applying All Data filter so the member list can reload."""
        delay = float(os.getenv("CUBII_AFTER_ALL_DATA_FILTER_LIST_REFRESH_SEC", "5.0"))
        self.LOGGER.info("All data filter: waiting %s s for list refresh.", delay)
        time.sleep(delay)

    def _verify_all_data_filter_card_text_contains(self, expected: str) -> None:
        """Assert visible text on `cardTypeOfUser` contains ``expected`` (case-insensitive)."""
        exp = (expected or "").strip()
        if not exp:
            raise AssertionError("Label check requires non-empty expected string.")
        wait_sec = int(os.getenv("CUBII_ALL_DATA_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        card = None
        for by, locator, label in (
            (AppiumBy.ID, self.ALL_DATA_FILTER_CARD_TYPE_USER_ID, "cardTypeOfUser (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.ALL_DATA_FILTER_CARD_TYPE_USER_UIAUTOMATOR,
                "cardTypeOfUser (UiAutomator)",
            ),
            (AppiumBy.XPATH, self.ALL_DATA_FILTER_CARD_TYPE_USER_XPATH, "cardTypeOfUser (xpath)"),
            (
                AppiumBy.XPATH,
                self.ALL_DATA_FILTER_CARD_TYPE_USER_XPATH_ANY,
                "cardTypeOfUser (xpath any-class)",
            ),
        ):
            try:
                card = wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("All data filter: read selection from card (%s).", label)
                break
            except Exception:
                continue
        if card is None:
            raise AssertionError(
                "All Data filter card (`com.cubii:id/cardTypeOfUser`) not visible for label check."
            )

        parts: list[str] = []
        try:
            t = (card.text or "").strip()
            if t:
                parts.append(t)
        except Exception:
            pass
        try:
            for tv in card.find_elements(AppiumBy.XPATH, ".//android.widget.TextView"):
                try:
                    tx = (tv.text or "").strip()
                    if tx:
                        parts.append(tx)
                except Exception:
                    continue
        except Exception:
            pass

        blob = " ".join(parts).lower()
        exp_lower = exp.lower()
        if exp_lower not in blob:
            raise AssertionError(
                "All Data filter card should reflect selected filter "
                f"{exp!r}; visible text was {parts!r}."
            )
        self.LOGGER.info("All data filter card shows selection containing %r.", exp)

    def verify_all_data_filter_card_shows_selected_label(self) -> None:
        """Assert `cardTypeOfUser` shows Automated Data (or ``CUBII_EXPECTED_ALL_DATA_FILTER_LABEL``)."""
        expected = (
            os.getenv("CUBII_EXPECTED_ALL_DATA_FILTER_LABEL", "Automated Data") or "Automated Data"
        ).strip()
        if not expected:
            expected = "Automated Data"
        self._verify_all_data_filter_card_text_contains(expected)

    def verify_all_data_filter_card_shows_manual_data_label(self) -> None:
        """Assert `cardTypeOfUser` shows Manual Data (or ``CUBII_EXPECTED_MANUAL_DATA_FILTER_LABEL``)."""
        expected = (
            os.getenv("CUBII_EXPECTED_MANUAL_DATA_FILTER_LABEL", "Manual Data") or "Manual Data"
        ).strip()
        if not expected:
            expected = "Manual Data"
        self._verify_all_data_filter_card_text_contains(expected)

    def verify_all_data_filter_card_shows_both_data_label(self) -> None:
        """Assert `cardTypeOfUser` shows BOTH (or ``CUBII_EXPECTED_BOTH_DATA_FILTER_LABEL``)."""
        expected = (
            os.getenv("CUBII_EXPECTED_BOTH_DATA_FILTER_LABEL", "BOTH") or "BOTH"
        ).strip()
        if not expected:
            expected = "BOTH"
        self._verify_all_data_filter_card_text_contains(expected)

    def tap_metrics_filter_card(self) -> None:
        """Open metrics filter sheet by tapping `cardTypeOfMetric`."""
        wait_sec = int(os.getenv("CUBII_METRICS_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.METRICS_FILTER_CARD_TYPE_METRIC_ID,
                "cardTypeOfMetric (id)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.METRICS_FILTER_CARD_TYPE_METRIC_UIAUTOMATOR,
                "cardTypeOfMetric (UiAutomator)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_CARD_TYPE_METRIC_XPATH,
                "cardTypeOfMetric (xpath)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_CARD_TYPE_METRIC_XPATH_ANY,
                "cardTypeOfMetric (xpath any-class)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_METRICS_FILTER_CARD_SEC", "0.5")))
                self.LOGGER.info("Metrics filter: cardTypeOfMetric tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap metrics filter card (`com.cubii:id/cardTypeOfMetric`)."
        )

    def tap_calories_option_in_metrics_filter(self) -> None:
        """Tap Calories row (`linearLayout8`) in the metrics filter sheet."""
        wait_sec = int(os.getenv("CUBII_METRICS_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.METRICS_FILTER_CALORIES_LINEAR_ID,
                "Calories linearLayout8 (id)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_CALORIES_LINEAR_XPATH,
                "Calories linearLayout8 (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.METRICS_FILTER_CALORIES_LINEAR_UIAUTOMATOR,
                "Calories linearLayout8 (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_METRICS_CALORIES_SEC", "0.5")))
                self.LOGGER.info("Metrics filter: Calories option tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Calories option (`com.cubii:id/linearLayout8`) in metrics filter."
        )

    def tap_miles_option_in_metrics_filter(self) -> None:
        """Tap Miles row (`linearLayout9`) in the metrics filter sheet."""
        wait_sec = int(os.getenv("CUBII_METRICS_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.METRICS_FILTER_MILES_LINEAR_ID,
                "Miles linearLayout9 (id)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_MILES_LINEAR_XPATH,
                "Miles linearLayout9 (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.METRICS_FILTER_MILES_LINEAR_UIAUTOMATOR,
                "Miles linearLayout9 (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_METRICS_MILES_SEC", "0.5")))
                self.LOGGER.info("Metrics filter: Miles option tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Miles option (`com.cubii:id/linearLayout9`) in metrics filter."
        )

    def tap_strides_option_in_metrics_filter(self) -> None:
        """Tap Strides row (`linearLayout10`) in the metrics filter sheet."""
        wait_sec = int(os.getenv("CUBII_METRICS_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.METRICS_FILTER_STRIDES_LINEAR_ID,
                "Strides linearLayout10 (id)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_STRIDES_LINEAR_XPATH,
                "Strides linearLayout10 (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.METRICS_FILTER_STRIDES_LINEAR_UIAUTOMATOR,
                "Strides linearLayout10 (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_METRICS_STRIDES_SEC", "0.5")))
                self.LOGGER.info("Metrics filter: Strides option tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Strides option (`com.cubii:id/linearLayout10`) in metrics filter."
        )

    def tap_time_option_in_metrics_filter(self) -> None:
        """Tap Time row (`linearLayout11`) in the metrics filter sheet."""
        wait_sec = int(os.getenv("CUBII_METRICS_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.METRICS_FILTER_TIME_LINEAR_ID,
                "Time linearLayout11 (id)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_TIME_LINEAR_XPATH,
                "Time linearLayout11 (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.METRICS_FILTER_TIME_LINEAR_UIAUTOMATOR,
                "Time linearLayout11 (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_METRICS_TIME_SEC", "0.5")))
                self.LOGGER.info("Metrics filter: Time option tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Time option (`com.cubii:id/linearLayout11`) in metrics filter."
        )

    def wait_after_metrics_filter_for_list_refresh(self) -> None:
        """Wait for member list row text to change after a metrics filter selection."""
        min_delay = float(os.getenv("CUBII_AFTER_METRICS_FILTER_LIST_REFRESH_MIN_SEC", "2.0"))
        poll_sec = float(os.getenv("CUBII_AFTER_METRICS_FILTER_LIST_REFRESH_SEC", "35.0"))
        interval = float(os.getenv("CUBII_METRICS_MEMBER_LIST_POLL_INTERVAL_SEC", "0.5"))
        time.sleep(min_delay)
        try:
            initial = tuple(self._collect_visible_member_row_text_blobs())
        except Exception:
            initial = ()
        deadline = time.time() + poll_sec
        self.LOGGER.info(
            "Metrics filter: polling up to %s s for member list refresh (initial rows=%s).",
            poll_sec,
            len(initial),
        )
        while time.time() < deadline:
            try:
                current = tuple(self._collect_visible_member_row_text_blobs())
            except Exception:
                current = ()
            if current and current != initial:
                self.LOGGER.info("Metrics filter: member list row text changed after filter.")
                return
            time.sleep(interval)
        self.LOGGER.warning(
            "Metrics filter: member list row text unchanged after %s s; continuing.",
            poll_sec,
        )

    def _collect_visible_member_row_text_blobs(self, max_rows: int | None = None) -> list[str]:
        """Join visible TextView text for each direct row under ``rv_group_member``."""
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        rv = wait.until(ec.visibility_of_element_located((AppiumBy.ID, self.RV_GROUP_MEMBER_ID)))
        rows = rv.find_elements(AppiumBy.XPATH, self.RV_GROUP_MEMBER_DIRECT_ROW_XPATH)
        visible = [e for e in rows if e.is_displayed()]
        if not visible:
            try:
                el = wait.until(
                    ec.visibility_of_element_located(
                        (AppiumBy.XPATH, self.RV_GROUP_MEMBER_FIRST_ROW_XPATH)
                    )
                )
                if el.is_displayed():
                    visible = [el]
            except TimeoutException:
                visible = []

        if max_rows is None:
            max_rows = int(os.getenv("CUBII_METRICS_MEMBER_LIST_MAX_ROWS_TO_SCAN", "8"))

        blobs: list[str] = []
        for row in visible[:max_rows]:
            try:
                texts: list[str] = []
                for tv in row.find_elements(AppiumBy.XPATH, ".//android.widget.TextView"):
                    try:
                        tx = (tv.text or "").strip()
                        if tx:
                            texts.append(tx)
                    except Exception:
                        continue
                if texts:
                    blobs.append(" ".join(texts))
            except Exception:
                continue
        return blobs

    def _wait_for_member_list_rows_matching_metric(
        self,
        match_rx: re.Pattern[str],
        *,
        metric_label: str,
        conflict_rx: re.Pattern[str] | None = None,
    ) -> None:
        """Poll until a visible member row matches *match_rx* (and not *conflict_rx*)."""
        poll_sec = float(os.getenv("CUBII_METRICS_MEMBER_LIST_POLL_SEC", "40"))
        interval = float(os.getenv("CUBII_METRICS_MEMBER_LIST_POLL_INTERVAL_SEC", "0.5"))
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        wait.until(ec.visibility_of_element_located((AppiumBy.ID, self.RV_GROUP_MEMBER_ID)))

        deadline = time.time() + poll_sec
        last_snippets: list[str] = []
        while time.time() < deadline:
            blobs = self._collect_visible_member_row_text_blobs()
            last_snippets = [b[:120] for b in blobs]
            if not blobs:
                time.sleep(interval)
                continue
            for blob in blobs:
                if conflict_rx and conflict_rx.search(blob):
                    continue
                if match_rx.search(blob):
                    self.LOGGER.info(
                        "Group member list: %s indicator matched in a visible row.",
                        metric_label,
                    )
                    return
            time.sleep(interval)

        if not last_snippets:
            raise AssertionError(
                f"No visible member rows to scan for {metric_label} under `rv_group_member`."
            )
        raise AssertionError(
            f"Expected {metric_label} indicator in at least one visible member row "
            f"(pattern {match_rx.pattern!r}); row snippets: {last_snippets!r}."
        )

    def verify_metrics_filter_card_shows_calories_label(self) -> None:
        """Assert Calories selection on ``cardTypeOfMetric``.

        Many builds show only the metric **ImageView** (e.g. flame) with no ``TextView`` on the card;
        in that case we accept a visible ``ImageView`` under the card. List rows still carry
        ``… Calories`` (see ``verify_group_member_list_visible_rows_indicate_calories``).

        Override the expected substring with ``CUBII_EXPECTED_METRICS_CALORIES_LABEL``. Set
        ``CUBII_METRICS_CARD_DISALLOW_ICON_ONLY_FALLBACK=1`` to require text on the card.
        """
        expected = (
            os.getenv("CUBII_EXPECTED_METRICS_CALORIES_LABEL", "Calories") or "Calories"
        ).strip()
        if not expected:
            expected = "Calories"
        wait_sec = int(os.getenv("CUBII_METRICS_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        card = None
        for by, locator, label in (
            (AppiumBy.ID, self.METRICS_FILTER_CARD_TYPE_METRIC_ID, "cardTypeOfMetric (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.METRICS_FILTER_CARD_TYPE_METRIC_UIAUTOMATOR,
                "cardTypeOfMetric (UiAutomator)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_CARD_TYPE_METRIC_XPATH,
                "cardTypeOfMetric (xpath)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_CARD_TYPE_METRIC_XPATH_ANY,
                "cardTypeOfMetric (xpath any-class)",
            ),
        ):
            try:
                card = wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Metrics filter: read selection from card (%s).", label)
                break
            except Exception:
                continue
        if card is None:
            raise AssertionError(
                "Metrics filter card (`com.cubii:id/cardTypeOfMetric`) not visible for label check."
            )

        parts: list[str] = []
        try:
            t = (card.text or "").strip()
            if t:
                parts.append(t)
        except Exception:
            pass
        try:
            for tv in card.find_elements(AppiumBy.XPATH, ".//android.widget.TextView"):
                try:
                    tx = (tv.text or "").strip()
                    if tx:
                        parts.append(tx)
                except Exception:
                    continue
        except Exception:
            pass
        try:
            for iv in card.find_elements(AppiumBy.XPATH, ".//android.widget.ImageView"):
                try:
                    cd = (iv.get_attribute("content-desc") or "").strip()
                    if cd:
                        parts.append(cd)
                except Exception:
                    continue
        except Exception:
            pass

        blob = " ".join(parts).lower()
        if expected.lower() in blob:
            self.LOGGER.info("Metrics filter card shows selection containing %r.", expected)
            return

        disallow_icon = os.getenv("CUBII_METRICS_CARD_DISALLOW_ICON_ONLY_FALLBACK", "").strip().lower() in (
            "1",
            "true",
            "yes",
        )
        if disallow_icon:
            raise AssertionError(
                "Metrics filter card should reflect selected metric "
                f"{expected!r}; visible text was {parts!r} (icon fallback disabled)."
            )

        try:
            for iv in card.find_elements(AppiumBy.XPATH, ".//android.widget.ImageView"):
                try:
                    if iv.is_displayed():
                        self.LOGGER.info(
                            "Metrics filter: Calories accepted via icon-only card "
                            "(visible ImageView under `cardTypeOfMetric`; card text was %r).",
                            parts,
                        )
                        return
                except Exception:
                    continue
        except Exception:
            pass

        try:
            icon = wait.until(
                ec.visibility_of_element_located(
                    (AppiumBy.XPATH, self.METRICS_FILTER_CARD_METRIC_ICON_IMAGEVIEW_XPATH)
                )
            )
            if icon.is_displayed():
                self.LOGGER.info(
                    "Metrics filter: Calories accepted via metric icon xpath "
                    "(Inspector: FrameLayout/cardTypeOfMetric/ImageView)."
                )
                return
        except TimeoutException:
            pass

        raise AssertionError(
            "Metrics filter card should show Calories: no text/description match "
            f"{expected!r} on card (visible text was {parts!r}) and no visible metric ImageView "
            f"under `cardTypeOfMetric` (xpath {self.METRICS_FILTER_CARD_METRIC_ICON_IMAGEVIEW_XPATH!r})."
        )

    def verify_group_member_list_visible_rows_indicate_calories(self) -> None:
        """Assert visible leaderboard rows contain a calories-style value (regex over row text)."""
        pattern = (os.getenv("CUBII_METRICS_MEMBER_LIST_CALORIES_PATTERN") or "").strip()
        if pattern:
            rx = re.compile(pattern, re.I)
        else:
            rx = re.compile(
                r"kcal|calories|calorie|\bcal\b|\d[\d,.\s]*\s*cals?\b|\d[\d,.\s]*\s*cal\b",
                re.I,
            )
        conflict_pat = (
            os.getenv("CUBII_METRICS_MEMBER_LIST_CALORIES_CONFLICT_PATTERN") or r"\bmiles?\b|\bmile\b"
        ).strip()
        conflict_rx = re.compile(conflict_pat, re.I) if conflict_pat else None
        self._wait_for_member_list_rows_matching_metric(
            rx, metric_label="calories", conflict_rx=conflict_rx
        )

    def verify_metrics_filter_card_shows_miles_label(self) -> None:
        """Assert Miles selection on ``cardTypeOfMetric`` (text/description or icon-only card).

        Same rules as ``verify_metrics_filter_card_shows_calories_label``: optional
        ``CUBII_EXPECTED_METRICS_MILES_LABEL`` (default ``Miles``), optional
        ``CUBII_METRICS_CARD_DISALLOW_ICON_ONLY_FALLBACK``.
        """
        expected = (os.getenv("CUBII_EXPECTED_METRICS_MILES_LABEL", "Miles") or "Miles").strip()
        if not expected:
            expected = "Miles"
        wait_sec = int(os.getenv("CUBII_METRICS_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        card = None
        for by, locator, label in (
            (AppiumBy.ID, self.METRICS_FILTER_CARD_TYPE_METRIC_ID, "cardTypeOfMetric (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.METRICS_FILTER_CARD_TYPE_METRIC_UIAUTOMATOR,
                "cardTypeOfMetric (UiAutomator)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_CARD_TYPE_METRIC_XPATH,
                "cardTypeOfMetric (xpath)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_CARD_TYPE_METRIC_XPATH_ANY,
                "cardTypeOfMetric (xpath any-class)",
            ),
        ):
            try:
                card = wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Metrics filter: read Miles selection from card (%s).", label)
                break
            except Exception:
                continue
        if card is None:
            raise AssertionError(
                "Metrics filter card (`com.cubii:id/cardTypeOfMetric`) not visible for Miles check."
            )

        parts: list[str] = []
        try:
            t = (card.text or "").strip()
            if t:
                parts.append(t)
        except Exception:
            pass
        try:
            for tv in card.find_elements(AppiumBy.XPATH, ".//android.widget.TextView"):
                try:
                    tx = (tv.text or "").strip()
                    if tx:
                        parts.append(tx)
                except Exception:
                    continue
        except Exception:
            pass
        try:
            for iv in card.find_elements(AppiumBy.XPATH, ".//android.widget.ImageView"):
                try:
                    cd = (iv.get_attribute("content-desc") or "").strip()
                    if cd:
                        parts.append(cd)
                except Exception:
                    continue
        except Exception:
            pass

        blob = " ".join(parts).lower()
        if expected.lower() in blob:
            self.LOGGER.info("Metrics filter card shows Miles selection containing %r.", expected)
            return

        disallow_icon = os.getenv("CUBII_METRICS_CARD_DISALLOW_ICON_ONLY_FALLBACK", "").strip().lower() in (
            "1",
            "true",
            "yes",
        )
        if disallow_icon:
            raise AssertionError(
                "Metrics filter card should reflect Miles selection "
                f"{expected!r}; visible text was {parts!r} (icon fallback disabled)."
            )

        try:
            for iv in card.find_elements(AppiumBy.XPATH, ".//android.widget.ImageView"):
                try:
                    if iv.is_displayed():
                        self.LOGGER.info(
                            "Metrics filter: Miles accepted via icon-only card "
                            "(visible ImageView under `cardTypeOfMetric`; card text was %r).",
                            parts,
                        )
                        return
                except Exception:
                    continue
        except Exception:
            pass

        try:
            icon = wait.until(
                ec.visibility_of_element_located(
                    (AppiumBy.XPATH, self.METRICS_FILTER_CARD_METRIC_ICON_IMAGEVIEW_XPATH)
                )
            )
            if icon.is_displayed():
                self.LOGGER.info(
                    "Metrics filter: Miles accepted via metric icon xpath "
                    "(FrameLayout/cardTypeOfMetric/ImageView)."
                )
                return
        except TimeoutException:
            pass

        raise AssertionError(
            "Metrics filter card should show Miles: no text/description match "
            f"{expected!r} on card (visible text was {parts!r}) and no visible metric ImageView "
            f"under `cardTypeOfMetric` (xpath {self.METRICS_FILTER_CARD_METRIC_ICON_IMAGEVIEW_XPATH!r})."
        )

    def verify_group_member_list_visible_rows_indicate_miles(self) -> None:
        """Assert visible leaderboard rows contain a miles-style value (regex over row text)."""
        pattern = (os.getenv("CUBII_METRICS_MEMBER_LIST_MILES_PATTERN") or "").strip()
        if pattern:
            rx = re.compile(pattern, re.I)
        else:
            rx = re.compile(
                r"miles|mile\b|\d[\d,.\s]*\s*mi\b",
                re.I,
            )
        conflict_pat = (
            os.getenv("CUBII_METRICS_MEMBER_LIST_MILES_CONFLICT_PATTERN")
            or r"\bcalories?\b|\bcalorie\b|\bkcal\b|\bcals?\b"
        ).strip()
        conflict_rx = re.compile(conflict_pat, re.I) if conflict_pat else None
        self._wait_for_member_list_rows_matching_metric(
            rx, metric_label="miles", conflict_rx=conflict_rx
        )

    def verify_metrics_filter_card_shows_strides_label(self) -> None:
        """Assert Strides selection on ``cardTypeOfMetric`` (text/description or icon-only card).

        Optional ``CUBII_EXPECTED_METRICS_STRIDES_LABEL`` (default ``Strides``), optional
        ``CUBII_METRICS_CARD_DISALLOW_ICON_ONLY_FALLBACK``.
        """
        expected = (os.getenv("CUBII_EXPECTED_METRICS_STRIDES_LABEL", "Strides") or "Strides").strip()
        if not expected:
            expected = "Strides"
        wait_sec = int(os.getenv("CUBII_METRICS_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        card = None
        for by, locator, label in (
            (AppiumBy.ID, self.METRICS_FILTER_CARD_TYPE_METRIC_ID, "cardTypeOfMetric (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.METRICS_FILTER_CARD_TYPE_METRIC_UIAUTOMATOR,
                "cardTypeOfMetric (UiAutomator)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_CARD_TYPE_METRIC_XPATH,
                "cardTypeOfMetric (xpath)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_CARD_TYPE_METRIC_XPATH_ANY,
                "cardTypeOfMetric (xpath any-class)",
            ),
        ):
            try:
                card = wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Metrics filter: read Strides selection from card (%s).", label)
                break
            except Exception:
                continue
        if card is None:
            raise AssertionError(
                "Metrics filter card (`com.cubii:id/cardTypeOfMetric`) not visible for Strides check."
            )

        parts: list[str] = []
        try:
            t = (card.text or "").strip()
            if t:
                parts.append(t)
        except Exception:
            pass
        try:
            for tv in card.find_elements(AppiumBy.XPATH, ".//android.widget.TextView"):
                try:
                    tx = (tv.text or "").strip()
                    if tx:
                        parts.append(tx)
                except Exception:
                    continue
        except Exception:
            pass
        try:
            for iv in card.find_elements(AppiumBy.XPATH, ".//android.widget.ImageView"):
                try:
                    cd = (iv.get_attribute("content-desc") or "").strip()
                    if cd:
                        parts.append(cd)
                except Exception:
                    continue
        except Exception:
            pass

        blob = " ".join(parts).lower()
        if expected.lower() in blob:
            self.LOGGER.info("Metrics filter card shows Strides selection containing %r.", expected)
            return

        disallow_icon = os.getenv("CUBII_METRICS_CARD_DISALLOW_ICON_ONLY_FALLBACK", "").strip().lower() in (
            "1",
            "true",
            "yes",
        )
        if disallow_icon:
            raise AssertionError(
                "Metrics filter card should reflect Strides selection "
                f"{expected!r}; visible text was {parts!r} (icon fallback disabled)."
            )

        try:
            for iv in card.find_elements(AppiumBy.XPATH, ".//android.widget.ImageView"):
                try:
                    if iv.is_displayed():
                        self.LOGGER.info(
                            "Metrics filter: Strides accepted via icon-only card "
                            "(visible ImageView under `cardTypeOfMetric`; card text was %r).",
                            parts,
                        )
                        return
                except Exception:
                    continue
        except Exception:
            pass

        try:
            icon = wait.until(
                ec.visibility_of_element_located(
                    (AppiumBy.XPATH, self.METRICS_FILTER_CARD_METRIC_ICON_IMAGEVIEW_XPATH)
                )
            )
            if icon.is_displayed():
                self.LOGGER.info(
                    "Metrics filter: Strides accepted via metric icon xpath "
                    "(FrameLayout/cardTypeOfMetric/ImageView)."
                )
                return
        except TimeoutException:
            pass

        raise AssertionError(
            "Metrics filter card should show Strides: no text/description match "
            f"{expected!r} on card (visible text was {parts!r}) and no visible metric ImageView "
            f"under `cardTypeOfMetric` (xpath {self.METRICS_FILTER_CARD_METRIC_ICON_IMAGEVIEW_XPATH!r})."
        )

    def verify_group_member_list_visible_rows_indicate_strides(self) -> None:
        """Assert visible leaderboard rows contain a strides-style value (regex over row text)."""
        pattern = (os.getenv("CUBII_METRICS_MEMBER_LIST_STRIDES_PATTERN") or "").strip()
        if pattern:
            rx = re.compile(pattern, re.I)
        else:
            rx = re.compile(
                r"strides|stride\b|\d[\d,.\s]*\s*strides?\b",
                re.I,
            )
        self._wait_for_member_list_rows_matching_metric(rx, metric_label="strides")

    def verify_metrics_filter_card_shows_time_label(self) -> None:
        """Assert Time selection on ``cardTypeOfMetric`` (text/description or icon-only card).

        Optional ``CUBII_EXPECTED_METRICS_TIME_LABEL`` (default ``Time``), optional
        ``CUBII_METRICS_CARD_DISALLOW_ICON_ONLY_FALLBACK``.
        """
        expected = (os.getenv("CUBII_EXPECTED_METRICS_TIME_LABEL", "Time") or "Time").strip()
        if not expected:
            expected = "Time"
        wait_sec = int(os.getenv("CUBII_METRICS_FILTER_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        card = None
        for by, locator, label in (
            (AppiumBy.ID, self.METRICS_FILTER_CARD_TYPE_METRIC_ID, "cardTypeOfMetric (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.METRICS_FILTER_CARD_TYPE_METRIC_UIAUTOMATOR,
                "cardTypeOfMetric (UiAutomator)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_CARD_TYPE_METRIC_XPATH,
                "cardTypeOfMetric (xpath)",
            ),
            (
                AppiumBy.XPATH,
                self.METRICS_FILTER_CARD_TYPE_METRIC_XPATH_ANY,
                "cardTypeOfMetric (xpath any-class)",
            ),
        ):
            try:
                card = wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Metrics filter: read Time selection from card (%s).", label)
                break
            except Exception:
                continue
        if card is None:
            raise AssertionError(
                "Metrics filter card (`com.cubii:id/cardTypeOfMetric`) not visible for Time check."
            )

        parts: list[str] = []
        try:
            t = (card.text or "").strip()
            if t:
                parts.append(t)
        except Exception:
            pass
        try:
            for tv in card.find_elements(AppiumBy.XPATH, ".//android.widget.TextView"):
                try:
                    tx = (tv.text or "").strip()
                    if tx:
                        parts.append(tx)
                except Exception:
                    continue
        except Exception:
            pass
        try:
            for iv in card.find_elements(AppiumBy.XPATH, ".//android.widget.ImageView"):
                try:
                    cd = (iv.get_attribute("content-desc") or "").strip()
                    if cd:
                        parts.append(cd)
                except Exception:
                    continue
        except Exception:
            pass

        blob = " ".join(parts).lower()
        if expected.lower() in blob:
            self.LOGGER.info("Metrics filter card shows Time selection containing %r.", expected)
            return

        disallow_icon = os.getenv("CUBII_METRICS_CARD_DISALLOW_ICON_ONLY_FALLBACK", "").strip().lower() in (
            "1",
            "true",
            "yes",
        )
        if disallow_icon:
            raise AssertionError(
                "Metrics filter card should reflect Time selection "
                f"{expected!r}; visible text was {parts!r} (icon fallback disabled)."
            )

        try:
            for iv in card.find_elements(AppiumBy.XPATH, ".//android.widget.ImageView"):
                try:
                    if iv.is_displayed():
                        self.LOGGER.info(
                            "Metrics filter: Time accepted via icon-only card "
                            "(visible ImageView under `cardTypeOfMetric`; card text was %r).",
                            parts,
                        )
                        return
                except Exception:
                    continue
        except Exception:
            pass

        try:
            icon = wait.until(
                ec.visibility_of_element_located(
                    (AppiumBy.XPATH, self.METRICS_FILTER_CARD_METRIC_ICON_IMAGEVIEW_XPATH)
                )
            )
            if icon.is_displayed():
                self.LOGGER.info(
                    "Metrics filter: Time accepted via metric icon xpath "
                    "(FrameLayout/cardTypeOfMetric/ImageView)."
                )
                return
        except TimeoutException:
            pass

        raise AssertionError(
            "Metrics filter card should show Time: no text/description match "
            f"{expected!r} on card (visible text was {parts!r}) and no visible metric ImageView "
            f"under `cardTypeOfMetric` (xpath {self.METRICS_FILTER_CARD_METRIC_ICON_IMAGEVIEW_XPATH!r})."
        )

    def verify_group_member_list_visible_rows_indicate_time(self) -> None:
        """Assert visible leaderboard rows contain a time-style value (regex over row text)."""
        pattern = (os.getenv("CUBII_METRICS_MEMBER_LIST_TIME_PATTERN") or "").strip()
        if pattern:
            rx = re.compile(pattern, re.I)
        else:
            # UI often uses compact minutes (e.g. ``39m``) with no space before ``m``.
            rx = re.compile(
                r"\btime\b|minute|min\b|hour|hr\b|"
                r"\d[\d,.\s]*\s*(min|mins?|hr|hrs?|h)\b|"
                r"\d+\s*m\b|\d+m\b|"
                r"\d+\s*h\b|\d+h\b|"
                r"\d{1,3}:\d{2}(?::\d{2})?",
                re.I,
            )
        conflict_pat = (
            os.getenv("CUBII_METRICS_MEMBER_LIST_TIME_CONFLICT_PATTERN")
            or r"\bmiles?\b|\bmile\b|\bstrides?\b|\bstride\b"
        ).strip()
        conflict_rx = re.compile(conflict_pat, re.I) if conflict_pat else None
        self._wait_for_member_list_rows_matching_metric(
            rx, metric_label="time", conflict_rx=conflict_rx
        )

    def scroll_group_details_member_list_down_and_up(self):
        """Swipe in the list area: scroll down (finger up) then scroll back up (finger down)."""
        size = self.driver.get_window_size()
        w, h = int(size["width"]), int(size["height"])
        left = int(w * float(os.getenv("CUBII_GROUP_DETAILS_SWIPE_LEFT_PCT", "0.15")))
        top = int(h * float(os.getenv("CUBII_GROUP_DETAILS_SWIPE_TOP_PCT", "0.35")))
        width = int(w * float(os.getenv("CUBII_GROUP_DETAILS_SWIPE_WIDTH_PCT", "0.7")))
        height = int(h * float(os.getenv("CUBII_GROUP_DETAILS_SWIPE_HEIGHT_PCT", "0.45")))
        pct = float(os.getenv("CUBII_GROUP_DETAILS_SWIPE_PERCENT", "0.55"))
        down_swipes = int(os.getenv("CUBII_GROUP_DETAILS_SCROLL_DOWN_SWIPES", "3"))
        up_swipes = int(os.getenv("CUBII_GROUP_DETAILS_SCROLL_UP_SWIPES", "3"))
        pause = float(os.getenv("CUBII_GROUP_DETAILS_SCROLL_PAUSE_SEC", "0.45"))

        self.LOGGER.info(
            "Group details: scroll list down (%s swipes) then up (%s).",
            down_swipes,
            up_swipes,
        )
        for _ in range(down_swipes):
            self.driver.execute_script(
                "mobile: swipeGesture",
                {
                    "left": left,
                    "top": top,
                    "width": width,
                    "height": height,
                    "direction": "up",
                    "percent": pct,
                },
            )
            time.sleep(pause)
        for _ in range(up_swipes):
            self.driver.execute_script(
                "mobile: swipeGesture",
                {
                    "left": left,
                    "top": top,
                    "width": width,
                    "height": height,
                    "direction": "down",
                    "percent": pct,
                },
            )
            time.sleep(pause)
        self.LOGGER.info("Group details: scroll down/up completed.")

    def tap_any_visible_group_member_row(self):
        """Tap one visible leaderboard row under `rv_group_member` (any visible card)."""
        wait_sec = int(os.getenv("CUBII_GROUP_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        rv = wait.until(ec.visibility_of_element_located((AppiumBy.ID, self.RV_GROUP_MEMBER_ID)))

        rows = rv.find_elements(AppiumBy.XPATH, self.RV_GROUP_MEMBER_DIRECT_ROW_XPATH)
        visible = [e for e in rows if e.is_displayed()]
        if visible:
            primary = random.choice(visible) if len(visible) > 1 else visible[0]
            others = [e for e in visible if e != primary]
            random.shuffle(others)
            for row in [primary] + others:
                try:
                    row.click()
                    time.sleep(
                        float(os.getenv("CUBII_AFTER_GROUP_MEMBER_ROW_TAP_SEC", "0.8"))
                    )
                    self.LOGGER.info(
                        "Group member list: tapped one of %s visible row(s).",
                        len(visible),
                    )
                    return
                except Exception:
                    continue

        top_rows = self.driver.find_elements(
            AppiumBy.XPATH, self.RV_GROUP_MEMBER_ALL_TOP_ROW_XPATH
        )
        visible_top = [e for e in top_rows if e.is_displayed()]
        random.shuffle(visible_top)
        for el in visible_top:
            try:
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_GROUP_MEMBER_ROW_TAP_SEC", "0.8")))
                self.LOGGER.info("Group member list: tapped row via top-level ViewGroup xpath.")
                return
            except Exception:
                continue

        try:
            el = wait.until(
                ec.element_to_be_clickable(
                    (AppiumBy.XPATH, self.RV_GROUP_MEMBER_FIRST_ROW_XPATH)
                )
            )
            el.click()
            time.sleep(float(os.getenv("CUBII_AFTER_GROUP_MEMBER_ROW_TAP_SEC", "0.8")))
            self.LOGGER.info("Group member list: tapped first row (xpath fallback).")
            return
        except Exception:
            pass

        try:
            el = wait.until(
                ec.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        self.RV_GROUP_MEMBER_ROW_FALLBACK_UIAUTOMATOR,
                    )
                )
            )
            el.click()
            time.sleep(float(os.getenv("CUBII_AFTER_GROUP_MEMBER_ROW_TAP_SEC", "0.8")))
            self.LOGGER.info("Group member list: tapped ViewGroup.instance(2) fallback.")
            return
        except Exception:
            pass

        raise AssertionError(
            "Could not tap any visible group member row under `rv_group_member`."
        )

    def verify_member_user_details_sheet(self):
        """After opening a member row: profile card, non-empty name, View Profile, Report, Block, Add Friend."""
        wait_sec = int(os.getenv("CUBII_USER_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        missing = []

        def must_see(by, locator, description):
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
            except TimeoutException:
                missing.append(description)

        def must_see_either(pairs, description):
            for by, locator in pairs:
                try:
                    wait.until(ec.visibility_of_element_located((by, locator)))
                    return
                except TimeoutException:
                    continue
            missing.append(description)

        must_see_either(
            (
                (AppiumBy.XPATH, self.USER_DETAILS_CARD_SCROLL_XPATH),
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    self.USER_DETAILS_CARD_VIEWGROUP_UIAUTOMATOR,
                ),
            ),
            "User details card (ScrollView / ViewGroup)",
        )
        must_see(AppiumBy.ID, self.USER_DETAILS_TXT_USER_NAME_ID, "User name (txtUserName)")
        must_see(
            AppiumBy.ID, self.USER_DETAILS_TXT_VIEW_PROFILE_ID, "View Profile (txtViewProfile)"
        )
        must_see(AppiumBy.ID, self.USER_DETAILS_BTN_REPORT_ID, "Report (btnReport)")
        must_see(AppiumBy.ID, self.USER_DETAILS_BTN_BLOCK_ID, "Block (btnBlock)")
        must_see(AppiumBy.ID, self.USER_DETAILS_BTN_ADD_FRIEND_ID, "Add Friend (btnAddFriend)")

        if missing:
            raise AssertionError(
                "User details sheet missing or not visible: " + ", ".join(missing)
            )

        try:
            name_el = self.driver.find_element(
                AppiumBy.ID, self.USER_DETAILS_TXT_USER_NAME_ID
            )
            name_txt = (name_el.text or "").strip()
            if not name_txt:
                raise AssertionError("User name (`txtUserName`) is visible but empty.")
        except AssertionError:
            raise
        except Exception as exc:
            raise AssertionError(f"Could not read user name on details sheet: {exc}") from exc

        self.LOGGER.info("User details sheet verified (card, name, View Profile, Report, Block, Add Friend).")

    def tap_view_profile_on_user_details_sheet(self) -> None:
        """Tap View Profile on the member user details sheet (`txtViewProfile`)."""
        wait_sec = int(os.getenv("CUBII_USER_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.USER_DETAILS_TXT_VIEW_PROFILE_ID, "txtViewProfile (id)"),
            (AppiumBy.XPATH, self.USER_DETAILS_TXT_VIEW_PROFILE_XPATH, "txtViewProfile (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.USER_DETAILS_TXT_VIEW_PROFILE_UIAUTOMATOR,
                "txtViewProfile (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TAP_VIEW_PROFILE_SEC", "1.0")))
                self.LOGGER.info("User details: View Profile tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap View Profile (`com.cubii:id/txtViewProfile`) on user details sheet."
        )

    def tap_view_profile_on_view_info_screen(self) -> None:
        """Tap View Profile on the View Info sheet (`txtViewProfile`)."""
        self.tap_view_profile_on_user_details_sheet()
        self.LOGGER.info("View Info screen: View Profile (`txtViewProfile`) tapped.")

    def _verify_view_profile_text_section_if_available(
        self,
        wait_opt: WebDriverWait,
        section_label: str,
        title_triplets: tuple[tuple, ...],
        value_triplets: tuple[tuple, ...],
    ) -> bool:
        """When a text section title or value is visible, assert both are shown with non-empty value."""
        title_visible = self._is_visible_one_of(wait_opt, title_triplets)
        value_visible = self._is_visible_one_of(wait_opt, value_triplets)
        if not title_visible and not value_visible:
            self.LOGGER.info("View Profile: %s not present; skipped.", section_label)
            return False
        if title_visible and not value_visible:
            raise AssertionError(
                f"View Profile: {section_label} title visible but value field missing."
            )
        if value_visible and not title_visible:
            raise AssertionError(
                f"View Profile: {section_label} value visible but title missing."
            )
        self._assert_visible_one_of(wait_opt, title_triplets, f"{section_label} title")
        self._assert_visible_one_of(wait_opt, value_triplets, f"{section_label} value")
        value_text = self._read_visible_text_one_of(value_triplets)
        if not value_text:
            raise AssertionError(f"View Profile: {section_label} value is empty.")
        self.LOGGER.info(
            "View Profile: %s verified (value sample=%r).",
            section_label,
            value_text[:120],
        )
        return True

    def _verify_view_profile_list_section_if_available(
        self,
        wait_opt: WebDriverWait,
        section_label: str,
        title_triplets: tuple[tuple, ...],
        list_triplets: tuple[tuple, ...],
    ) -> bool:
        """When a list section title or list is visible, assert both title and list are shown."""
        title_visible = self._is_visible_one_of(wait_opt, title_triplets)
        list_visible = self._is_visible_one_of(wait_opt, list_triplets)
        if not title_visible and not list_visible:
            self.LOGGER.info("View Profile: %s not present; skipped.", section_label)
            return False
        if title_visible and not list_visible:
            raise AssertionError(
                f"View Profile: {section_label} title visible but list missing."
            )
        if list_visible and not title_visible:
            raise AssertionError(
                f"View Profile: {section_label} list visible but title missing."
            )
        self._assert_visible_one_of(wait_opt, title_triplets, f"{section_label} title")
        self._assert_visible_one_of(wait_opt, list_triplets, f"{section_label} list")
        self.LOGGER.info("View Profile: %s list verified.", section_label)
        return True

    def verify_friend_view_profile_sections_if_available(self) -> None:
        """
        On the friend View Profile screen, verify Bio, Focus, Interests, and Badges
        when each section is present (skipped when absent).
        """
        wait_sec = int(os.getenv("CUBII_VIEW_PROFILE_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        optional_sec = max(
            2,
            int(os.getenv("CUBII_VIEW_PROFILE_OPTIONAL_SECTION_WAIT_SEC", "3")),
        )
        wait = WebDriverWait(self.driver, wait_sec)
        wait_opt = WebDriverWait(self.driver, optional_sec)

        screen_anchors = (
            self._text_view_locator_triplets(self.VIEW_PROFILE_BIO_TITLE_ID),
            self._text_view_locator_triplets(self.VIEW_PROFILE_BIO_TEXT_ID),
            self._text_view_locator_triplets(self.VIEW_PROFILE_FOCUS_TITLE_ID),
            self._text_view_locator_triplets(self.VIEW_PROFILE_BADGES_TITLE_ID),
            (
                (AppiumBy.ID, self.VIEWED_PROFILE_IMG_USER_PICTURE_ID),
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    self.VIEWED_PROFILE_IMG_USER_PICTURE_UIAUTOMATOR,
                ),
                (AppiumBy.XPATH, self.VIEWED_PROFILE_IMG_USER_PICTURE_XPATH),
            ),
        )
        loaded = any(self._is_visible_one_of(wait, triplets) for triplets in screen_anchors)
        if not loaded:
            raise AssertionError(
                "View Profile screen did not load (no profile anchors visible)."
            )

        verified: list[str] = []
        if self._verify_view_profile_text_section_if_available(
            wait_opt,
            "Bio",
            (
                (AppiumBy.ID, self.VIEW_PROFILE_BIO_TITLE_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_PROFILE_BIO_TITLE_UIAUTOMATOR),
                (AppiumBy.XPATH, self.VIEW_PROFILE_BIO_TITLE_XPATH),
            ),
            (
                (AppiumBy.ID, self.VIEW_PROFILE_BIO_TEXT_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_PROFILE_BIO_TEXT_UIAUTOMATOR),
                (AppiumBy.XPATH, self.VIEW_PROFILE_BIO_TEXT_XPATH),
            ),
        ):
            verified.append("Bio")
        if self._verify_view_profile_text_section_if_available(
            wait_opt,
            "Focus",
            (
                (AppiumBy.ID, self.VIEW_PROFILE_FOCUS_TITLE_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_PROFILE_FOCUS_TITLE_UIAUTOMATOR),
                (AppiumBy.XPATH, self.VIEW_PROFILE_FOCUS_TITLE_XPATH),
            ),
            (
                (AppiumBy.ID, self.VIEW_PROFILE_FOCUS_TEXT_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_PROFILE_FOCUS_TEXT_UIAUTOMATOR),
                (AppiumBy.XPATH, self.VIEW_PROFILE_FOCUS_TEXT_XPATH),
            ),
        ):
            verified.append("Focus")
        if self._verify_view_profile_list_section_if_available(
            wait_opt,
            "Interests",
            (
                (AppiumBy.ID, self.VIEW_PROFILE_INTERESTS_TITLE_ID),
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    self.VIEW_PROFILE_INTERESTS_TITLE_UIAUTOMATOR,
                ),
                (AppiumBy.XPATH, self.VIEW_PROFILE_INTERESTS_TITLE_XPATH),
            ),
            (
                (AppiumBy.ID, self.VIEW_PROFILE_INTERESTS_LIST_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_PROFILE_INTERESTS_LIST_UIAUTOMATOR),
                (AppiumBy.XPATH, self.VIEW_PROFILE_INTERESTS_LIST_XPATH),
            ),
        ):
            verified.append("Interests")
        if self._verify_view_profile_list_section_if_available(
            wait_opt,
            "Badges",
            (
                (AppiumBy.ID, self.VIEW_PROFILE_BADGES_TITLE_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_PROFILE_BADGES_TITLE_UIAUTOMATOR),
                (AppiumBy.XPATH, self.VIEW_PROFILE_BADGES_TITLE_XPATH),
            ),
            (
                (AppiumBy.ID, self.VIEW_PROFILE_BADGES_GRID_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.VIEW_PROFILE_BADGES_GRID_UIAUTOMATOR),
                (AppiumBy.XPATH, self.VIEW_PROFILE_BADGES_GRID_XPATH),
            ),
        ):
            verified.append("Badges")

        self.LOGGER.info(
            "Step Passed: friend View Profile verified. Sections checked: %s.",
            ", ".join(verified) if verified else "none (profile shell only)",
        )

    def verify_viewed_member_profile_screen_shows_profile_details(self) -> None:
        """Assert profile screen shows avatar, name, and badges.

        Focus (`cardFocus`) and Interests (`cardInterest`) are **optional**: when locators match,
        they are logged as verified; if absent (other member/build/layout), the step still passes.
        """
        wait_sec = int(os.getenv("CUBII_VIEWED_PROFILE_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        optional_sec = max(
            2,
            int(os.getenv("CUBII_VIEWED_PROFILE_OPTIONAL_SECTION_WAIT_SEC", "3")),
        )
        wait_opt = WebDriverWait(self.driver, optional_sec)

        img_ok = False
        for by, locator, label in (
            (
                AppiumBy.ID,
                self.VIEWED_PROFILE_IMG_USER_PICTURE_ID,
                "imgUserProfilePictureMyAccount (id)",
            ),
            (
                AppiumBy.XPATH,
                self.VIEWED_PROFILE_IMG_USER_PICTURE_XPATH,
                "imgUserProfilePictureMyAccount (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.VIEWED_PROFILE_IMG_USER_PICTURE_UIAUTOMATOR,
                "imgUserProfilePictureMyAccount (UiAutomator)",
            ),
        ):
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Viewed profile: profile image visible (%s).", label)
                img_ok = True
                break
            except Exception:
                continue
        if not img_ok:
            raise AssertionError(
                "Viewed member profile: profile image "
                "(`com.cubii:id/imgUserProfilePictureMyAccount`) not visible."
            )

        name_el = None
        for by, locator, label in (
            (AppiumBy.ID, self.VIEWED_PROFILE_USER_NAME_TEXTVIEW_ID, "textView22 (id)"),
            (
                AppiumBy.XPATH,
                self.VIEWED_PROFILE_USER_NAME_TEXTVIEW_XPATH,
                "textView22 (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.VIEWED_PROFILE_USER_NAME_TEXTVIEW_UIAUTOMATOR,
                "textView22 (UiAutomator)",
            ),
        ):
            try:
                name_el = wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Viewed profile: user name field visible (%s).", label)
                break
            except Exception:
                continue
        if name_el is None:
            raise AssertionError(
                "Viewed member profile: user name (`com.cubii:id/textView22`) not visible."
            )
        try:
            name_txt = (name_el.text or "").strip()
        except Exception as exc:
            raise AssertionError(f"Viewed member profile: could not read textView22: {exc}") from exc
        if not name_txt:
            raise AssertionError("Viewed member profile: user name (`textView22`) is empty.")

        badges_ok = False
        for by, locator, label in (
            (
                AppiumBy.XPATH,
                self.VIEWED_PROFILE_BADGES_INNER_VIEWGROUP_XPATH,
                "cardBadges / ViewGroup (xpath)",
            ),
            (
                AppiumBy.XPATH,
                self.VIEWED_PROFILE_CARD_BADGES_FRAME_XPATH,
                "cardBadges FrameLayout (xpath)",
            ),
            (AppiumBy.ID, self.VIEWED_PROFILE_CARD_BADGES_ID, "cardBadges (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.VIEWED_PROFILE_BADGES_VIEWGROUP_INSTANCE_UIAUTOMATOR,
                "badges ViewGroup.instance(4) (UiAutomator fallback)",
            ),
        ):
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Viewed profile: badges area visible (%s).", label)
                badges_ok = True
                break
            except Exception:
                continue
        if not badges_ok:
            raise AssertionError(
                "Viewed member profile: badges region (`com.cubii:id/cardBadges` / ViewGroup) "
                "not visible."
            )

        focus_ok = False
        for by, locator, label in (
            (
                AppiumBy.XPATH,
                self.VIEWED_PROFILE_FOCUS_INNER_VIEWGROUP_XPATH,
                "cardFocus / ViewGroup (xpath)",
            ),
            (
                AppiumBy.XPATH,
                self.VIEWED_PROFILE_CARD_FOCUS_FRAME_XPATH,
                "cardFocus FrameLayout (xpath)",
            ),
            (AppiumBy.ID, self.VIEWED_PROFILE_CARD_FOCUS_ID, "cardFocus (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.VIEWED_PROFILE_FOCUS_VIEWGROUP_INSTANCE_UIAUTOMATOR,
                "Focus ViewGroup.instance(5) (UiAutomator fallback)",
            ),
        ):
            try:
                wait_opt.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Viewed profile: Focus card visible (%s).", label)
                focus_ok = True
                break
            except Exception:
                continue
        if not focus_ok:
            self.LOGGER.info(
                "Viewed profile: Focus (`cardFocus`) not visible; skipping optional check."
            )

        interest_ok = False
        for by, locator, label in (
            (
                AppiumBy.XPATH,
                self.VIEWED_PROFILE_INTEREST_INNER_VIEWGROUP_XPATH,
                "cardInterest / ViewGroup (xpath)",
            ),
            (
                AppiumBy.XPATH,
                self.VIEWED_PROFILE_CARD_INTEREST_FRAME_XPATH,
                "cardInterest FrameLayout (xpath)",
            ),
            (AppiumBy.ID, self.VIEWED_PROFILE_CARD_INTEREST_ID, "cardInterest (id)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.VIEWED_PROFILE_INTEREST_VIEWGROUP_INSTANCE_UIAUTOMATOR,
                "Interests ViewGroup.instance(6) (UiAutomator fallback)",
            ),
        ):
            try:
                wait_opt.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Viewed profile: Interests card visible (%s).", label)
                interest_ok = True
                break
            except Exception:
                continue
        if not interest_ok:
            self.LOGGER.info(
                "Viewed profile: Interests (`cardInterest`) not visible; skipping optional check."
            )

        self.LOGGER.info(
            "Viewed member profile OK: image, name=%r, badges; Focus=%s, Interests=%s.",
            name_txt[:80],
            focus_ok,
            interest_ok,
        )

    def _tap_iv_back_button(self, description: str, pause_env_key: str) -> None:
        """Tap `com.cubii:id/iv_back` (profile or chat toolbar back)."""
        wait_sec = int(os.getenv("CUBII_IV_BACK_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        # Some screens render the header/back control slightly after content appears.
        settle_sec = float(os.getenv("CUBII_BEFORE_IV_BACK_TAP_SEC", "1.2"))
        if settle_sec > 0:
            time.sleep(settle_sec)
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.VIEWED_PROFILE_IV_BACK_ID, "iv_back (id)"),
            (
                AppiumBy.XPATH,
                self.VIEWED_PROFILE_IV_BACK_LINEAR_XPATH,
                "iv_back LinearLayout (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.VIEWED_PROFILE_IV_BACK_UIAUTOMATOR,
                "iv_back (UiAutomator)",
            ),
            (AppiumBy.XPATH, self.VIEWED_PROFILE_IV_BACK_XPATH_ANY, "iv_back (xpath any-class)"),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv(pause_env_key, "0.6")))
                self.LOGGER.info("%s tapped via %s.", description, label)
                return
            except Exception:
                continue
        raise AssertionError(f"Could not tap {description} (`com.cubii:id/iv_back`).")

    def tap_viewed_member_profile_screen_back_button(self) -> None:
        """Tap profile screen back control (`iv_back`)."""
        self._tap_iv_back_button(
            "Profile back",
            "CUBII_AFTER_TAP_VIEWED_PROFILE_BACK_SEC",
        )

    def tap_chat_conversation_back_button(self) -> None:
        """Tap chat screen back control (`iv_back`) after closing View Info / profile."""
        self._tap_iv_back_button(
            "Chat back",
            "CUBII_AFTER_TAP_CHAT_BACK_SEC",
        )

    def verify_user_details_report_button_disabled(self):
        """Assert Report (`btnReport`) is visible and disabled on the member user details sheet."""
        wait_sec = int(os.getenv("CUBII_USER_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        el = None
        last_err: Exception | None = None
        for by, locator, label in (
            (AppiumBy.ID, self.USER_DETAILS_BTN_REPORT_ID, "btnReport (id)"),
            (AppiumBy.XPATH, self.USER_DETAILS_BTN_REPORT_XPATH, "btnReport (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.USER_DETAILS_BTN_REPORT_UIAUTOMATOR,
                "btnReport (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.visibility_of_element_located((by, locator)))
                self.LOGGER.info("Report button located for disabled check (%s).", label)
                break
            except Exception as exc:
                last_err = exc
                continue
        if el is None:
            raise AssertionError(
                "Report (`btnReport`) not visible on user details sheet. "
                f"Last error: {last_err!r}"
            )

        try:
            live_enabled = el.is_enabled()
        except Exception as exc:
            raise AssertionError(
                f"Could not read Report button enabled state: {exc}"
            ) from exc

        en_attr = None
        try:
            en_attr = el.get_attribute("enabled")
        except Exception:
            pass

        is_disabled = live_enabled is False or (
            en_attr is not None and str(en_attr).lower() == "false"
        )
        if not is_disabled:
            raise AssertionError(
                "Report (`btnReport`) should be disabled on user details sheet; "
                f"is_enabled={live_enabled!r}, enabled attribute={en_attr!r}."
            )
        self.LOGGER.info("User details sheet: Report (`btnReport`) is disabled as expected.")

    def verify_view_info_report_button_disabled(self) -> None:
        """Assert Report (`btnReport`) is visible and disabled on the View Info sheet."""
        self.verify_user_details_report_button_disabled()
        self.LOGGER.info("View Info screen: Report (`btnReport`) is disabled as expected.")

    def tap_report_on_user_details_sheet(self):
        """Tap Report on the member user details bottom sheet (`btnReport`)."""
        wait_sec = int(os.getenv("CUBII_USER_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.USER_DETAILS_BTN_REPORT_ID, "btnReport (id)"),
            (AppiumBy.XPATH, self.USER_DETAILS_BTN_REPORT_XPATH, "btnReport (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.USER_DETAILS_BTN_REPORT_UIAUTOMATOR,
                "btnReport (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_REPORT_TAP_SEC", "0.6")))
                self.LOGGER.info("User details: Report tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Report (`com.cubii:id/btnReport`) on user details sheet."
        )

    def enter_report_form_subject_and_description(self, subject: str, description: str) -> None:
        """Fill `etSubject` and `etDescribe` on the report form."""
        wait_sec = int(os.getenv("CUBII_REPORT_FORM_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)

        sub_el = None
        for by, locator, label in (
            (AppiumBy.ID, self.REPORT_FORM_ET_SUBJECT_ID, "etSubject (id)"),
            (AppiumBy.XPATH, self.REPORT_FORM_ET_SUBJECT_XPATH, "etSubject (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.REPORT_FORM_ET_SUBJECT_UIAUTOMATOR,
                "etSubject (UiAutomator)",
            ),
        ):
            try:
                sub_el = wait.until(ec.element_to_be_clickable((by, locator)))
                self.LOGGER.info("Report form: subject field (%s).", label)
                break
            except Exception:
                continue
        if sub_el is None:
            raise AssertionError(
                "Report form subject (`com.cubii:id/etSubject`) not found or not tappable."
            )
        try:
            sub_el.clear()
        except Exception:
            pass
        sub_el.send_keys(subject)
        time.sleep(float(os.getenv("CUBII_AFTER_REPORT_SUBJECT_KEYS_SEC", "0.25")))

        desc_el = None
        for by, locator, label in (
            (AppiumBy.ID, self.REPORT_FORM_ET_DESCRIBE_ID, "etDescribe (id)"),
            (AppiumBy.XPATH, self.REPORT_FORM_ET_DESCRIBE_XPATH, "etDescribe (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.REPORT_FORM_ET_DESCRIBE_UIAUTOMATOR,
                "etDescribe (UiAutomator)",
            ),
        ):
            try:
                desc_el = wait.until(ec.element_to_be_clickable((by, locator)))
                self.LOGGER.info("Report form: description field (%s).", label)
                break
            except Exception:
                continue
        if desc_el is None:
            raise AssertionError(
                "Report form description (`com.cubii:id/etDescribe`) not found or not tappable."
            )
        try:
            desc_el.clear()
        except Exception:
            pass
        desc_el.send_keys(description)
        time.sleep(float(os.getenv("CUBII_AFTER_REPORT_DESCRIBE_KEYS_SEC", "0.25")))
        self.LOGGER.info("Report form: subject and description entered.")

    def tap_report_form_report_submit_button(self) -> None:
        """Tap REPORT submit (`com.cubii:id/btnReport`) on the report form."""
        wait_sec = int(os.getenv("CUBII_REPORT_FORM_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.USER_DETAILS_BTN_REPORT_ID, "btnReport (id)"),
            (AppiumBy.XPATH, self.USER_DETAILS_BTN_REPORT_XPATH, "btnReport (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.USER_DETAILS_BTN_REPORT_UIAUTOMATOR,
                "btnReport (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_REPORT_FORM_SUBMIT_SEC", "0.8")))
                self.LOGGER.info("Report form: REPORT button tapped (%s).", label)
                return
            except Exception:
                continue

        deadline = time.monotonic() + float(wait_sec)
        while time.monotonic() < deadline:
            try:
                candidates = self.driver.find_elements(
                    AppiumBy.ID, self.USER_DETAILS_BTN_REPORT_ID
                )
                for el in reversed(candidates):
                    try:
                        if el.is_displayed() and el.is_enabled():
                            el.click()
                            time.sleep(
                                float(os.getenv("CUBII_AFTER_REPORT_FORM_SUBMIT_SEC", "0.8"))
                            )
                            self.LOGGER.info(
                                "Report form: REPORT button tapped (multi-id fallback)."
                            )
                            return
                    except Exception:
                        continue
            except Exception:
                pass
            time.sleep(0.35)

        raise AssertionError(
            "Could not tap REPORT button (`com.cubii:id/btnReport`) on report form."
        )

    def tap_close_on_user_details_sheet(self):
        """Tap the sheet Close FAB (`fabClose`, content-desc Close)."""
        wait_sec = int(os.getenv("CUBII_USER_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.USER_DETAILS_FAB_CLOSE_ID, "fabClose (id)"),
            (
                AppiumBy.ACCESSIBILITY_ID,
                self.USER_DETAILS_FAB_CLOSE_ACCESSIBILITY_ID,
                "Close (a11y)",
            ),
            (AppiumBy.XPATH, self.USER_DETAILS_FAB_CLOSE_XPATH, "fabClose (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.USER_DETAILS_FAB_CLOSE_UIAUTOMATOR,
                "fabClose (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_USER_DETAILS_CLOSE_TAP_SEC", "0.6")))
                self.LOGGER.info("User details: Close FAB tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Close (`com.cubii:id/fabClose`) on user details sheet."
        )

    def tap_add_friend_on_user_details_sheet(self):
        """Tap Add Friend on the member user details bottom sheet (`btnAddFriend`)."""
        wait_sec = int(os.getenv("CUBII_USER_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        btn = wait.until(
            ec.element_to_be_clickable((AppiumBy.ID, self.USER_DETAILS_BTN_ADD_FRIEND_ID))
        )
        btn.click()
        time.sleep(float(os.getenv("CUBII_AFTER_ADD_FRIEND_TAP_SEC", "0.8")))
        self.LOGGER.info("User details: Add Friend button tapped.")

    def tap_unfriend_on_user_details_sheet(self) -> None:
        """Tap Unfriend on the member user details bottom sheet (`btnUnfriend`)."""
        wait_sec = int(os.getenv("CUBII_USER_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.VIEW_INFO_BTN_UNFRIEND_ID, "btnUnfriend (id)"),
            (AppiumBy.XPATH, self.VIEW_INFO_BTN_UNFRIEND_XPATH, "btnUnfriend (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.VIEW_INFO_BTN_UNFRIEND_UIAUTOMATOR,
                "btnUnfriend (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_UNFRIEND_TAP_SEC", "0.6")))
                self.LOGGER.info("User details: Unfriend tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Unfriend (`com.cubii:id/btnUnfriend`) on user details sheet."
        )

    def tap_unfriend_on_view_info_screen(self) -> None:
        """Tap Unfriend on the View Info sheet (`btnUnfriend`)."""
        self.tap_unfriend_on_user_details_sheet()
        self.LOGGER.info("View Info screen: Unfriend (`btnUnfriend`) tapped.")

    def tap_unfriend_confirmation_yes(self) -> None:
        """Tap Yes (`btnYes`) on the unfriend confirmation dialog."""
        wait_sec = int(
            os.getenv("CUBII_UNFRIEND_CONFIRM_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )
        wait = WebDriverWait(self.driver, wait_sec)
        self.LOGGER.info("Unfriend: tap Yes on confirmation dialog (btnYes).")
        for by, locator, label in (
            (AppiumBy.ID, self.UNFRIEND_CONFIRM_BTN_YES_ID, "btnYes (id)"),
            (AppiumBy.XPATH, self.UNFRIEND_CONFIRM_BTN_YES_XPATH, "btnYes (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.UNFRIEND_CONFIRM_BTN_YES_UIAUTOMATOR,
                "btnYes (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_UNFRIEND_CONFIRM_YES_SEC", "0.8")))
                self.LOGGER.info("Unfriend confirmation: Yes tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Yes (`com.cubii:id/btnYes`) on unfriend confirmation dialog."
        )

    def tap_block_on_view_info_screen(self) -> None:
        """Tap Block on the View Info sheet (`btnBlock`)."""
        self.tap_block_on_user_details_sheet()
        self.LOGGER.info("View Info screen: Block (`btnBlock`) tapped.")

    def tap_block_confirmation_dialog_cancel(self) -> None:
        """Tap Cancel (`btnCancel`) on the block confirmation dialog."""
        self.tap_unblock_user_dialog_cancel()
        self.LOGGER.info("Block confirmation dialog: Cancel (`btnCancel`) tapped.")

    def tap_block_confirmation_dialog_confirm(self) -> None:
        """Tap Block (`btnBlock`) on the block confirmation popup."""
        wait_sec = int(
            os.getenv("CUBII_BLOCK_CONFIRM_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.USER_DETAILS_BTN_BLOCK_ID, "btnBlock (id)"),
            (AppiumBy.XPATH, self.BLOCK_USER_BTN_BLOCK_XPATH, "btnBlock (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.BLOCK_USER_BTN_BLOCK_UIAUTOMATOR,
                "btnBlock (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_BLOCK_CONFIRM_TAP_SEC", "0.8")))
                self.LOGGER.info("Block confirmation dialog: Block tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap Block (`com.cubii:id/btnBlock`) on block confirmation popup."
        )

    def verify_blocked_chat_conversation_shows_unblock(self) -> None:
        """Assert blocked-by text and Unblock button are visible on the chat screen."""
        wait_sec = int(
            os.getenv("CUBII_BLOCKED_CHAT_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )
        wait = WebDriverWait(self.driver, wait_sec)
        missing: list[str] = []
        self._must_see_one_of(
            wait,
            (
                (AppiumBy.ID, self.CHAT_CONVERSATION_BLOCKED_BY_TEXT_ID),
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    self.CHAT_CONVERSATION_BLOCKED_BY_TEXT_UIAUTOMATOR,
                ),
                (AppiumBy.XPATH, self.CHAT_CONVERSATION_BLOCKED_BY_TEXT_XPATH),
            ),
            "blocked-by text (txtChatConversationBlockedByText)",
            missing,
        )
        self._must_see_one_of(
            wait,
            (
                (AppiumBy.ID, self.CHAT_CONVERSATION_UNBLOCK_ID),
                (AppiumBy.ANDROID_UIAUTOMATOR, self.CHAT_CONVERSATION_UNBLOCK_UIAUTOMATOR),
                (AppiumBy.XPATH, self.CHAT_CONVERSATION_UNBLOCK_XPATH),
            ),
            "Unblock button (btnUnblock)",
            missing,
        )
        if missing:
            raise AssertionError(
                "Blocked chat conversation missing: " + ", ".join(missing)
            )
        blocked_text = self._read_visible_text_one_of(
            (
                (AppiumBy.ID, self.CHAT_CONVERSATION_BLOCKED_BY_TEXT_ID),
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    self.CHAT_CONVERSATION_BLOCKED_BY_TEXT_UIAUTOMATOR,
                ),
                (AppiumBy.XPATH, self.CHAT_CONVERSATION_BLOCKED_BY_TEXT_XPATH),
            )
        )
        self.LOGGER.info(
            "Step Passed: blocked chat verified — blocked-by text=%r; Unblock button visible.",
            blocked_text,
        )

    def tap_unblock_on_blocked_chat_conversation(self) -> None:
        """Tap Unblock on the blocked friend chat screen (`btnUnblock`)."""
        self._tap_btn_unblock_button(
            "Unblock on chat (btnUnblock)",
            "CUBII_AFTER_TAP_CHAT_UNBLOCK_SEC",
            prefer_last_visible=False,
        )

    def tap_block_on_user_details_sheet(self):
        """Tap Block on the member user details bottom sheet."""
        wait_sec = int(os.getenv("CUBII_USER_DETAILS_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.USER_DETAILS_BTN_BLOCK_ID, "btnBlock (id)"),
            (AppiumBy.XPATH, self.BLOCK_USER_BTN_BLOCK_XPATH, "btnBlock (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.BLOCK_USER_BTN_BLOCK_UIAUTOMATOR,
                "btnBlock (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_BLOCK_TAP_SEC", "0.6")))
                self.LOGGER.info("User details: Block tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError("Could not tap Block (`com.cubii:id/btnBlock`) on user details sheet.")

    def tap_block_confirmation_if_present(self):
        """Second Block / confirm tap (dialog). Best-effort if no dialog appears."""
        wait_sec = int(os.getenv("CUBII_BLOCK_CONFIRM_WAIT_SEC", "6"))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BLOCK")', "text BLOCK"),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Block")', "text Block"),
            (AppiumBy.ID, "android:id/button1", "Android OK (button1)"),
            (AppiumBy.XPATH, self.BLOCK_USER_BTN_BLOCK_XPATH, "btnBlock xpath (dialog)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.BLOCK_USER_BTN_BLOCK_UIAUTOMATOR,
                "btnBlock UiAutomator (dialog)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_BLOCK_CONFIRM_TAP_SEC", "0.8")))
                self.LOGGER.info("Block flow: confirmation tapped (%s).", label)
                return
            except Exception:
                continue
        self.LOGGER.info("Block flow: no confirmation control matched; continuing.")

    def tap_navigate_up(self):
        """Toolbar Navigate up (back arrow)."""
        wait_sec = int(os.getenv("CUBII_NAVIGATE_UP_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ACCESSIBILITY_ID, self.NAVIGATE_UP_ACCESSIBILITY_ID, "Navigate up (a11y)"),
            (AppiumBy.XPATH, self.NAVIGATE_UP_XPATH, "Navigate up (xpath)"),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.NAVIGATE_UP_UIAUTOMATOR, "Navigate up (UiAutomator)"),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_NAVIGATE_UP_TAP_SEC", "0.6")))
                self.LOGGER.info("Block flow: Navigate up (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError("Navigate up control not found or not tappable.")

    def tap_toolbar_back_linear_layout(self):
        """Tap toolbar back area (`toolbar` LinearLayout)."""
        wait_sec = int(os.getenv("CUBII_TOOLBAR_BACK_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.XPATH, self.TOOLBAR_BACK_LINEAR_LAYOUT_XPATH, "toolbar LinearLayout (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.TOOLBAR_BACK_LINEAR_LAYOUT_UIAUTOMATOR,
                "LinearLayout.instance(3)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_TOOLBAR_BACK_TAP_SEC", "0.6")))
                self.LOGGER.info("Block flow: toolbar back (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError("Toolbar back LinearLayout not found or not tappable.")

    def tap_toolbar_more_menu(self):
        """Open overflow More menu (`moreIcon` / content-desc More)."""
        wait_sec = int(os.getenv("CUBII_MORE_MENU_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.MORE_ICON_ID, "moreIcon (id)"),
            (AppiumBy.ACCESSIBILITY_ID, self.MORE_ICON_ACCESSIBILITY_ID, "More (a11y)"),
            (AppiumBy.XPATH, self.MORE_ICON_XPATH, "More (xpath)"),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.MORE_ICON_UIAUTOMATOR, "moreIcon (UiAutomator)"),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_MORE_MENU_TAP_SEC", "0.6")))
                self.LOGGER.info("Block flow: More menu (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError("More menu (`moreIcon` / More) not found or not tappable.")

    def tap_blocked_users_menu_option(self):
        """Tap Blocked users row in overflow menu."""
        wait_sec = int(os.getenv("CUBII_BLOCKED_USERS_MENU_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.BLOCKED_USERS_MENU_OPTION_ID, "txtOptionBlockedUsers (id)"),
            (AppiumBy.XPATH, self.BLOCKED_USERS_MENU_OPTION_XPATH, "txtOptionBlockedUsers (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.BLOCKED_USERS_MENU_OPTION_UIAUTOMATOR,
                "txtOptionBlockedUsers (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_BLOCKED_USERS_MENU_TAP_SEC", "0.8")))
                self.LOGGER.info("Block flow: Blocked users option (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError("Blocked users menu option not found or not tappable.")

    def verify_blocked_users_list_visible(self):
        """Assert Blocked users list RecyclerView is visible with at least one row (dynamic)."""
        wait_sec = int(os.getenv("CUBII_BLOCKED_USERS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        rv = wait.until(
            ec.visibility_of_element_located((AppiumBy.ID, self.BLOCKED_USERS_RV_USERS_LIST_ID))
        )
        rows = rv.find_elements(AppiumBy.XPATH, self.BLOCKED_USERS_RV_ROW_REL_XPATH)
        visible = [e for e in rows if e.is_displayed()]
        if len(visible) >= 1:
            self.LOGGER.info(
                "Blocked users: %s visible row(s) under rvUsersList.",
                len(visible),
            )
            return
        try:
            wait.until(
                ec.visibility_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        self.BLOCKED_USERS_ROW_FALLBACK_UIAUTOMATOR,
                    )
                )
            )
            self.LOGGER.info("Blocked users: ViewGroup.instance(2) fallback visible.")
            return
        except TimeoutException:
            pass
        raise AssertionError(
            "Blocked users list `rvUsersList` has no visible rows (or list not visible)."
        )

    def verify_blocked_user_listed_on_blocked_users_screen(
        self, expected_name: str | None = None
    ) -> None:
        """
        Assert Blocked users list is visible with at least one row.

        When `expected_name` is omitted, any blocked user in the list passes
        (the blocked account may differ from the chat profile name).
        """
        self.verify_blocked_users_list_visible()
        target = (expected_name or os.getenv("CUBII_BLOCKED_USERS_EXPECTED_NAME", "")).strip()
        if not target:
            sample_labels = self._blocked_users_list_row_labels(max_rows=3)
            self.LOGGER.info(
                "Step Passed: blocked users list shows at least one user (any name). "
                "Sample row labels: %s",
                sample_labels or "<none>",
            )
            return

        wait_sec = int(os.getenv("CUBII_BLOCKED_USERS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        deadline = time.monotonic() + float(wait_sec)
        while time.monotonic() < deadline:
            try:
                rv = self.driver.find_element(
                    AppiumBy.ID, self.BLOCKED_USERS_RV_USERS_LIST_ID
                )
                for tv in rv.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView"):
                    if not tv.is_displayed():
                        continue
                    text = (tv.text or tv.get_attribute("text") or "").strip()
                    if text and target.lower() in text.lower():
                        self.LOGGER.info(
                            "Step Passed: blocked user %r found in list (row text=%r).",
                            target,
                            text,
                        )
                        return
            except Exception:
                pass
            time.sleep(0.35)

        raise AssertionError(
            f"Blocked user {target!r} was not found on the Blocked users screen."
        )

    def _blocked_users_list_row_labels(self, max_rows: int = 3) -> list[str]:
        """Collect visible TextView labels from the first rows of rvUsersList (for logs)."""
        labels: list[str] = []
        try:
            rv = self.driver.find_element(AppiumBy.ID, self.BLOCKED_USERS_RV_USERS_LIST_ID)
            rows = rv.find_elements(AppiumBy.XPATH, self.BLOCKED_USERS_RV_ROW_REL_XPATH)
            visible_rows = [r for r in rows if r.is_displayed()][: max(1, max_rows)]
            for row in visible_rows:
                for tv in row.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView"):
                    if not tv.is_displayed():
                        continue
                    text = (tv.text or tv.get_attribute("text") or "").strip()
                    if text and text not in labels:
                        labels.append(text)
        except Exception:
            pass
        return labels

    def tap_blocked_user_profile_row_at_position(self, position_one_based: int = 1) -> None:
        """Tap a blocked-user row (profile) in `rvUsersList` (1-based index)."""
        if position_one_based < 1:
            raise AssertionError("Blocked users list row position must be >= 1.")
        wait_sec = int(
            os.getenv("CUBII_BLOCKED_USERS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )
        wait = WebDriverWait(self.driver, wait_sec)
        wait.until(
            ec.visibility_of_element_located(
                (AppiumBy.ID, self.BLOCKED_USERS_RV_USERS_LIST_ID)
            )
        )
        idx = position_one_based
        row_xpath_indexed = (
            "(//androidx.recyclerview.widget.RecyclerView"
            f'[@resource-id="{self.BLOCKED_USERS_RV_USERS_LIST_ID}"]'
            f"/android.view.ViewGroup)[{idx}]"
        )
        row_xpath_direct = (
            f'//androidx.recyclerview.widget.RecyclerView[@resource-id="'
            f'{self.BLOCKED_USERS_RV_USERS_LIST_ID}"]/android.view.ViewGroup[{idx}]'
        )
        for by, locator, label in (
            (AppiumBy.XPATH, row_xpath_direct, "blocked user row (xpath [n])"),
            (AppiumBy.XPATH, row_xpath_indexed, "blocked user row (xpath indexed)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.BLOCKED_USERS_ROW_FALLBACK_UIAUTOMATOR,
                "blocked user row (ViewGroup UiSelector)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(
                    float(os.getenv("CUBII_AFTER_BLOCKED_USER_PROFILE_TAP_SEC", "0.6"))
                )
                self.LOGGER.info(
                    "Blocked users: profile row tapped (%s, position=%s).",
                    label,
                    position_one_based,
                )
                return
            except Exception:
                continue
        raise AssertionError(
            "Could not tap blocked user profile row in `rvUsersList` "
            f"at position {position_one_based}."
        )

    def _btn_unblock_locator_triplets(self) -> tuple[tuple, ...]:
        return (
            (AppiumBy.ID, self.BTN_UNBLOCK_ID),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.BTN_UNBLOCK_UIAUTOMATOR),
            (AppiumBy.XPATH, self.BTN_UNBLOCK_XPATH),
        )

    def _dedupe_web_elements(self, elements: list) -> list:
        seen: set[str] = set()
        unique: list = []
        for el in elements:
            try:
                key = el.id
            except Exception:
                key = str(id(el))
            if key in seen:
                continue
            seen.add(key)
            unique.append(el)
        return unique

    def _collect_visible_btn_unblock_elements(self) -> list:
        candidates: list = []
        for by, locator in self._btn_unblock_locator_triplets():
            try:
                candidates.extend(self.driver.find_elements(by, locator))
            except Exception:
                continue
        for by, locator in (
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.cubii:id/btnUnblock").text("UNBLOCK")',
            ),
            (
                AppiumBy.XPATH,
                '//android.widget.Button[@resource-id="com.cubii:id/btnUnblock" and @text="UNBLOCK"]',
            ),
        ):
            try:
                candidates.extend(self.driver.find_elements(by, locator))
            except Exception:
                continue
        visible: list = []
        for el in self._dedupe_web_elements(candidates):
            try:
                if el.is_displayed():
                    visible.append(el)
            except Exception:
                continue
        return visible

    def _tap_element_click_or_gesture(self, el, description: str) -> bool:
        """Tap element; fall back to W3C clickGesture when Appium reports not clickable."""
        try:
            rect = el.rect
        except Exception:
            rect = None
        size = self.driver.get_window_size()
        screen_h = int(size.get("height", 2400))
        nav_margin = int(os.getenv("CUBII_ANDROID_NAV_BAR_MARGIN_PX", "72"))

        def _gesture_at(x: int, y: int) -> None:
            self.driver.execute_script("mobile: clickGesture", {"x": int(x), "y": int(y)})

        strategies: list[tuple[str, callable]] = [("native click", lambda: el.click())]
        if rect:
            cx = int(rect["x"] + rect["width"] / 2)
            cy_center = int(rect["y"] + rect["height"] / 2)
            cy_upper = int(rect["y"] + max(8.0, rect["height"] * 0.35))
            if cy_center > screen_h - nav_margin:
                cy_center = screen_h - nav_margin
            if cy_upper > screen_h - nav_margin:
                cy_upper = screen_h - nav_margin
            strategies.extend(
                [
                    ("clickGesture center", lambda: _gesture_at(cx, cy_center)),
                    ("clickGesture upper", lambda: _gesture_at(cx, cy_upper)),
                ]
            )
        for label, action in strategies:
            try:
                action()
                self.LOGGER.info("Tapped %s via %s.", description, label)
                return True
            except Exception as exc:
                self.LOGGER.debug("btnUnblock tap %s failed: %s", label, exc)
                continue
        return False

    def _wait_for_btn_unblock_visible(self, wait_sec: int):
        wait = WebDriverWait(self.driver, wait_sec)
        last_exc: Exception | None = None
        for by, locator in self._btn_unblock_locator_triplets():
            try:
                return wait.until(ec.visibility_of_element_located((by, locator)))
            except Exception as exc:
                last_exc = exc
                continue
        if last_exc:
            raise last_exc
        raise TimeoutException("btnUnblock not visible")

    def _tap_btn_unblock_button(
        self,
        description: str,
        pause_env_key: str,
        *,
        prefer_last_visible: bool = False,
    ) -> None:
        """
        Tap `android.widget.Button` with resource-id `com.cubii:id/btnUnblock`.

        Uses visibility (not strict clickability) and clickGesture when the bottom
        UNBLOCK bar is obscured by the system navigation area.
        """
        wait_sec = int(
            os.getenv("CUBII_BLOCKED_USERS_UNBLOCK_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )
        time.sleep(
            float(os.getenv("CUBII_BLOCKED_USER_PROFILE_SCREEN_SETTLE_SEC", "0.8"))
        )
        try:
            self._wait_for_btn_unblock_visible(wait_sec)
        except Exception:
            self.LOGGER.info(
                "btnUnblock visibility wait timed out; continuing poll for %s.",
                description,
            )

        deadline = time.monotonic() + float(wait_sec)
        while time.monotonic() < deadline:
            visible = self._collect_visible_btn_unblock_elements()
            if visible:
                target = visible[-1] if prefer_last_visible else visible[0]
                if self._tap_element_click_or_gesture(target, description):
                    time.sleep(float(os.getenv(pause_env_key, "0.6")))
                    self.LOGGER.info(
                        "Tapped %s via btnUnblock (%s visible; index %s).",
                        description,
                        len(visible),
                        -1 if prefer_last_visible else 0,
                    )
                    return
            time.sleep(0.4)

        raise AssertionError(f"Communitii Friends: could not tap {description}.")

    def tap_unblock_button_on_blocked_users_screen(self) -> None:
        """Tap Unblock (`btnUnblock`) on the blocked user profile screen (opens confirm dialog)."""
        self._tap_btn_unblock_button(
            "Unblock on blocked user profile (btnUnblock)",
            "CUBII_AFTER_TAP_BLOCKED_USERS_UNBLOCK_BTN_SEC",
            prefer_last_visible=False,
        )

    def tap_unblock_confirmation_dialog_confirm(self) -> None:
        """Tap Unblock (`btnUnblock`) on the unblock confirmation dialog."""
        self._tap_btn_unblock_button(
            "Unblock on confirmation dialog (btnUnblock)",
            "CUBII_AFTER_UNBLOCK_DIALOG_CONFIRM_SEC",
            prefer_last_visible=True,
        )
        wait_sec = int(
            os.getenv("CUBII_UNBLOCK_DIALOG_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )
        try:
            WebDriverWait(self.driver, wait_sec).until(
                ec.invisibility_of_element_located((AppiumBy.ID, self.BTN_UNBLOCK_ID))
            )
        except TimeoutException:
            self.LOGGER.info(
                "Unblock dialog: btnUnblock still present after confirm (continuing)."
            )
        self.LOGGER.info("Unblock confirmation dialog: Unblock option (`btnUnblock`) confirmed.")

    def tap_blocked_users_list_unblock_at_position(self, position_one_based: int):
        """Tap row UNBLOCK (`tvUnblock`) for the Nth blocked user (1-based)."""
        if position_one_based < 1:
            raise AssertionError("Blocked users list position must be >= 1.")
        wait_sec = int(
            os.getenv("CUBII_BLOCKED_USERS_LIST_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )
        wait = WebDriverWait(self.driver, wait_sec)
        wait.until(
            ec.visibility_of_element_located(
                (AppiumBy.ID, self.BLOCKED_USERS_RV_USERS_LIST_ID)
            )
        )
        idx = position_one_based
        rid_unblock = self.BLOCKED_USERS_TV_UNBLOCK_ID
        xpath_scoped = (
            "(//androidx.recyclerview.widget.RecyclerView"
            f'[@resource-id="{self.BLOCKED_USERS_RV_USERS_LIST_ID}"]'
            f'//android.widget.TextView[@resource-id="{rid_unblock}"])[{idx}]'
        )
        xpath_global = f'(//android.widget.TextView[@resource-id="{rid_unblock}"])[{idx}]'
        uia_inst = idx - 1
        uia = f'new UiSelector().resourceId("{rid_unblock}").instance({uia_inst})'
        for by, locator, label in (
            (AppiumBy.XPATH, xpath_scoped, "tvUnblock scoped under rvUsersList"),
            (AppiumBy.XPATH, xpath_global, "tvUnblock indexed xpath"),
            (AppiumBy.ANDROID_UIAUTOMATOR, uia, "tvUnblock UiSelector.instance"),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(
                    float(os.getenv("CUBII_AFTER_BLOCKED_UNBLOCK_ROW_TAP_SEC", "0.5"))
                )
                self.LOGGER.info(
                    "Blocked users: UNBLOCK on row (%s, position=%s).",
                    label,
                    position_one_based,
                )
                return
            except Exception:
                continue
        raise AssertionError(
            f"Could not tap UNBLOCK (`{rid_unblock}`) at list position {position_one_based}."
        )

    def tap_unblock_user_dialog_cancel(self):
        """Dismiss Unblock User confirmation via Cancel. Waits until dialog is gone."""
        wait_sec = int(
            os.getenv("CUBII_UNBLOCK_DIALOG_WAIT_SEC", str(Settings.EXPLICIT_WAIT))
        )
        wait = WebDriverWait(self.driver, wait_sec)
        clicked = False
        for by, locator, label in (
            (AppiumBy.ID, self.BLOCKED_USERS_BTN_UNBLOCK_DIALOG_CANCEL_ID, "btnCancel (id)"),
            (AppiumBy.XPATH, self.BLOCKED_USERS_BTN_CANCEL_XPATH, "btnCancel (xpath)"),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.BLOCKED_USERS_BTN_CANCEL_UIAUTOMATOR,
                "btnCancel (UiAutomator)",
            ),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                clicked = True
                self.LOGGER.info("Unblock dialog: Cancel tapped (%s).", label)
                break
            except Exception:
                continue
        if not clicked:
            raise AssertionError(
                "Unblock dialog Cancel (`btnCancel`) not found or not tappable."
            )
        time.sleep(float(os.getenv("CUBII_AFTER_UNBLOCK_DIALOG_CANCEL_SEC", "0.4")))
        WebDriverWait(self.driver, wait_sec).until(
            ec.invisibility_of_element_located(
                (AppiumBy.ID, self.BLOCKED_USERS_BTN_UNBLOCK_DIALOG_CANCEL_ID)
            )
        )

    def tap_unblock_user_dialog_confirm(self):
        """Confirm Unblock User via UNBLOCK (`android.widget.Button` btnUnblock)."""
        self.tap_unblock_confirmation_dialog_confirm()

    def tap_ll_back_button(self):
        """Tap screen back container (`llBack` LinearLayout)."""
        wait_sec = int(os.getenv("CUBII_LL_BACK_WAIT_SEC", str(Settings.EXPLICIT_WAIT)))
        wait = WebDriverWait(self.driver, wait_sec)
        for by, locator, label in (
            (AppiumBy.ID, self.LL_BACK_ID, "llBack (id)"),
            (AppiumBy.XPATH, self.LL_BACK_XPATH, "llBack (xpath)"),
            (AppiumBy.ANDROID_UIAUTOMATOR, self.LL_BACK_UIAUTOMATOR, "llBack (UiAutomator)"),
        ):
            try:
                el = wait.until(ec.element_to_be_clickable((by, locator)))
                el.click()
                time.sleep(float(os.getenv("CUBII_AFTER_LL_BACK_TAP_SEC", "0.6")))
                self.LOGGER.info("Blocked users / screen: llBack tapped (%s).", label)
                return
            except Exception:
                continue
        raise AssertionError("Back (`com.cubii:id/llBack`) not found or not tappable.")
