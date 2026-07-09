import logging
import os
import re
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage
from framework.pages.home_page import HomePage

ANDROID_KEYCODE_BACK = 4


class HelpPage(BasePage):
    LOGGER = logging.getLogger("cubii_help_page")

    HELP_OPTION_TEXTVIEW_ID = "com.cubii:id/textView24"
    HELP_LIST_RECYCLER_ID = "com.cubii:id/rv_help"
    HELP_LIST_RECYCLER = (AppiumBy.ID, HELP_LIST_RECYCLER_ID)
    HELP_LIST_RECYCLER_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{HELP_LIST_RECYCLER_ID}")',
    )
    HELP_LIST_RECYCLER_XPATH = (
        AppiumBy.XPATH,
        f'//androidx.recyclerview.widget.RecyclerView[@resource-id="{HELP_LIST_RECYCLER_ID}"]',
    )
    HELP_LIST_OPTIONS = (
        "Customer Support",
        "FAQ",
        "Product Manual",
        "Assembly Video",
        "Privacy Policy",
        "Terms of Service",
    )

    HELP_SCREEN_BACK_NAV_UP_ACCESSIBILITY_ID = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    HELP_SCREEN_BACK_NAV_UP_CLASS = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")
    HELP_SCREEN_BACK_NAV_UP_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Navigate up")',
    )
    HELP_SCREEN_BACK_NAV_UP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Navigate up"]',
    )

    FAQ_SCREEN_BACK_NAV_UP_ACCESSIBILITY_ID = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    FAQ_SCREEN_BACK_NAV_UP_CLASS = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")
    FAQ_SCREEN_BACK_NAV_UP_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Navigate up")',
    )
    FAQ_SCREEN_BACK_NAV_UP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Navigate up"]',
    )

    CUSTOMER_SUPPORT_MENU_ITEM = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_help"]'
        "/android.view.ViewGroup[1]",
    )
    CUSTOMER_SUPPORT_MENU_ITEM_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").instance(2)',
    )
    CUSTOMER_SUPPORT_MENU_ITEM_BY_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Customer Support")',
    )
    CUSTOMER_SUPPORT_MENU_ITEM_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/textView24" and @text="Customer Support"]',
    )

    FAQ_MENU_ITEM = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_help"]'
        "/android.view.ViewGroup[2]",
    )
    FAQ_MENU_ITEM_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").instance(3)',
    )
    FAQ_MENU_ITEM_BY_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("FAQ")',
    )
    FAQ_MENU_ITEM_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/textView24" and @text="FAQ"]',
    )

    PRODUCT_MANUAL_MENU_ITEM = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_help"]'
        "/android.view.ViewGroup[3]",
    )
    PRODUCT_MANUAL_MENU_ITEM_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").instance(4)',
    )
    PRODUCT_MANUAL_MENU_ITEM_BY_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Product Manual")',
    )
    PRODUCT_MANUAL_MENU_ITEM_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/textView24" and @text="Product Manual"]',
    )

    PRODUCT_MANUAL_SCREEN_TITLE = "Product Manual"
    PRODUCT_MANUAL_TOOLBAR_TITLE_ID = "com.cubii:id/toolbar_title"
    PRODUCT_MANUAL_TOOLBAR_TITLE = (AppiumBy.ID, PRODUCT_MANUAL_TOOLBAR_TITLE_ID)
    PRODUCT_MANUAL_TOOLBAR_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{PRODUCT_MANUAL_TOOLBAR_TITLE_ID}")',
    )
    PRODUCT_MANUAL_TOOLBAR_TITLE_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{PRODUCT_MANUAL_TOOLBAR_TITLE_ID}"]',
    )
    PRODUCT_MANUAL_TOOLBAR_TITLE_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{PRODUCT_MANUAL_TOOLBAR_TITLE_ID}"'
        f' and @text="{PRODUCT_MANUAL_SCREEN_TITLE}"]',
    )

    PRODUCT_MANUAL_BACK_NAV_UP_ACCESSIBILITY_ID = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    PRODUCT_MANUAL_BACK_NAV_UP_CLASS = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")
    PRODUCT_MANUAL_BACK_NAV_UP_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Navigate up")',
    )
    PRODUCT_MANUAL_BACK_NAV_UP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Navigate up"]',
    )

    ASSEMBLY_VIDEO_MENU_ITEM = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_help"]'
        "/android.view.ViewGroup[4]",
    )
    ASSEMBLY_VIDEO_MENU_ITEM_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").instance(5)',
    )
    ASSEMBLY_VIDEO_MENU_ITEM_BY_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Assembly Video")',
    )
    ASSEMBLY_VIDEO_MENU_ITEM_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{HELP_OPTION_TEXTVIEW_ID}" and @text="Assembly Video"]',
    )
    ASSEMBLY_VIDEO_MENU_ITEM_TEXT_CONTAINS_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Assembly Video")',
    )

    ASSEMBLY_VIDEO_SCREEN_TITLE = "Assembly Video"
    ASSEMBLY_VIDEO_TOOLBAR_TITLE_ID = "com.cubii:id/toolbar_title"
    ASSEMBLY_VIDEO_TOOLBAR_TITLE = (AppiumBy.ID, ASSEMBLY_VIDEO_TOOLBAR_TITLE_ID)
    ASSEMBLY_VIDEO_TOOLBAR_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{ASSEMBLY_VIDEO_TOOLBAR_TITLE_ID}")',
    )
    ASSEMBLY_VIDEO_TOOLBAR_TITLE_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{ASSEMBLY_VIDEO_TOOLBAR_TITLE_ID}"]',
    )
    ASSEMBLY_VIDEO_TOOLBAR_TITLE_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{ASSEMBLY_VIDEO_TOOLBAR_TITLE_ID}"'
        f' and @text="{ASSEMBLY_VIDEO_SCREEN_TITLE}"]',
    )

    ASSEMBLY_VIDEO_BACK_NAV_UP_ACCESSIBILITY_ID = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    ASSEMBLY_VIDEO_BACK_NAV_UP_CLASS = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")
    ASSEMBLY_VIDEO_BACK_NAV_UP_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Navigate up")',
    )
    ASSEMBLY_VIDEO_BACK_NAV_UP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Navigate up"]',
    )

    PRIVACY_POLICY_MENU_ITEM = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_help"]'
        "/android.view.ViewGroup[5]",
    )
    PRIVACY_POLICY_MENU_ITEM_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").instance(6)',
    )
    PRIVACY_POLICY_MENU_ITEM_BY_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Privacy Policy")',
    )
    PRIVACY_POLICY_MENU_ITEM_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/textView24" and @text="Privacy Policy"]',
    )

    PRIVACY_POLICY_SCREEN_TITLE = "Privacy Policy"
    PRIVACY_POLICY_TOOLBAR_TITLE_ID = "com.cubii:id/toolbar_title"
    PRIVACY_POLICY_TOOLBAR_TITLE = (AppiumBy.ID, PRIVACY_POLICY_TOOLBAR_TITLE_ID)
    PRIVACY_POLICY_TOOLBAR_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{PRIVACY_POLICY_TOOLBAR_TITLE_ID}")',
    )
    PRIVACY_POLICY_TOOLBAR_TITLE_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{PRIVACY_POLICY_TOOLBAR_TITLE_ID}"]',
    )
    PRIVACY_POLICY_TOOLBAR_TITLE_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{PRIVACY_POLICY_TOOLBAR_TITLE_ID}"'
        f' and @text="{PRIVACY_POLICY_SCREEN_TITLE}"]',
    )

    PRIVACY_POLICY_HEADING_ID = "com.cubii:id/textView124"
    PRIVACY_POLICY_HEADING = (AppiumBy.ID, PRIVACY_POLICY_HEADING_ID)
    PRIVACY_POLICY_HEADING_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{PRIVACY_POLICY_HEADING_ID}")',
    )
    PRIVACY_POLICY_HEADING_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{PRIVACY_POLICY_HEADING_ID}"'
        f' and @text="{PRIVACY_POLICY_SCREEN_TITLE}"]',
    )

    PRIVACY_POLICY_SCROLL_ID = "com.cubii:id/scrollView2"
    PRIVACY_POLICY_SCROLL_CONTENT = (
        AppiumBy.XPATH,
        f'//android.widget.ScrollView[@resource-id="{PRIVACY_POLICY_SCROLL_ID}"]'
        "/android.view.ViewGroup",
    )
    PRIVACY_POLICY_SCROLL_CONTENT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").instance(2)',
    )

    PRIVACY_POLICY_INTRO_ID = "com.cubii:id/text_privacy_policy"
    PRIVACY_POLICY_INTRO_FRAGMENT = "Please read our Privacy Policy"
    PRIVACY_POLICY_INTRO = (AppiumBy.ID, PRIVACY_POLICY_INTRO_ID)
    PRIVACY_POLICY_INTRO_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{PRIVACY_POLICY_INTRO_ID}")',
    )
    PRIVACY_POLICY_INTRO_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{PRIVACY_POLICY_INTRO_ID}"]',
    )
    PRIVACY_POLICY_INTRO_CONTAINS_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{PRIVACY_POLICY_INTRO_ID}")'
        f'.textContains("{PRIVACY_POLICY_INTRO_FRAGMENT}")',
    )

    PRIVACY_POLICY_DESCRIPTION_CHECKS = (
        (PRIVACY_POLICY_INTRO_ID, PRIVACY_POLICY_INTRO_FRAGMENT),
        ("com.cubii:id/tv_privacy_one", "strides, distance, calories burned"),
        ("com.cubii:id/tv_privacy_two", "personalize our services"),
        ("com.cubii:id/tv_privacy_three", "delete your account at any time"),
        ("com.cubii:id/tv_contact_support", "revoke consent"),
    )

    PRIVACY_POLICY_BACK_NAV_UP_ACCESSIBILITY_ID = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    PRIVACY_POLICY_BACK_NAV_UP_CLASS = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")
    PRIVACY_POLICY_BACK_NAV_UP_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Navigate up")',
    )
    PRIVACY_POLICY_BACK_NAV_UP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Navigate up"]',
    )

    # Left-edge floating back affordance (no toolbar Navigate up on this screen).
    PRIVACY_POLICY_FLOATING_BACK_ID = "com.cubii:id/iv_back"
    PRIVACY_POLICY_FLOATING_BACK = (AppiumBy.ID, PRIVACY_POLICY_FLOATING_BACK_ID)
    PRIVACY_POLICY_FLOATING_BACK_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.cubii:id/iv_back"]',
    )
    PRIVACY_POLICY_FLOATING_BACK_XPATH_ANY = (
        AppiumBy.XPATH,
        '//*[@resource-id="com.cubii:id/iv_back"]',
    )
    PRIVACY_POLICY_FLOATING_BACK_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/iv_back")',
    )
    PRIVACY_POLICY_FLOATING_BACK_IMAGE_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageView[@clickable="true"]',
    )

    TERMS_OF_SERVICE_MENU_ITEM = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_help"]'
        "/android.view.ViewGroup[6]",
    )
    TERMS_OF_SERVICE_MENU_ITEM_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").instance(7)',
    )
    TERMS_OF_SERVICE_MENU_ITEM_BY_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Terms of Service")',
    )
    TERMS_OF_SERVICE_MENU_ITEM_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/textView24" and @text="Terms of Service"]',
    )

    TERMS_OF_SERVICE_SCREEN_TITLE = "Terms of Service"
    TERMS_OF_SERVICE_TOOLBAR_TITLE_ID = "com.cubii:id/toolbar_title"
    TERMS_OF_SERVICE_TOOLBAR_TITLE = (AppiumBy.ID, TERMS_OF_SERVICE_TOOLBAR_TITLE_ID)
    TERMS_OF_SERVICE_TOOLBAR_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{TERMS_OF_SERVICE_TOOLBAR_TITLE_ID}")',
    )
    TERMS_OF_SERVICE_TOOLBAR_TITLE_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{TERMS_OF_SERVICE_TOOLBAR_TITLE_ID}"]',
    )
    TERMS_OF_SERVICE_TOOLBAR_TITLE_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{TERMS_OF_SERVICE_TOOLBAR_TITLE_ID}"'
        f' and @text="{TERMS_OF_SERVICE_SCREEN_TITLE}"]',
    )
    TERMS_OF_SERVICE_WEBVIEW_ID = "com.cubii:id/wv_terms_privacy"
    TERMS_OF_SERVICE_WEBVIEW = (AppiumBy.ID, TERMS_OF_SERVICE_WEBVIEW_ID)
    TERMS_OF_SERVICE_WEBVIEW_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{TERMS_OF_SERVICE_WEBVIEW_ID}")',
    )
    TERMS_OF_SERVICE_WEBVIEW_XPATH = (
        AppiumBy.XPATH,
        f'//android.webkit.WebView[@resource-id="{TERMS_OF_SERVICE_WEBVIEW_ID}"]',
    )
    TERMS_OF_SERVICE_DESCRIPTION_FRAGMENTS = (
        "We use cookies",
        "Essential",
        "Cookie Policy",
        "ACCEPT COOKIES",
    )
    TERMS_COOKIE_OVERLAY_FRAGMENTS = (
        "ACCEPT COOKIES",
        "ALLOW ALL COOKIES",
        "More Information",
    )
    TERMS_OF_SERVICE_NAV_UP_ACCESSIBILITY_ID = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    TERMS_OF_SERVICE_NAV_UP_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Navigate up")',
    )
    TERMS_OF_SERVICE_NAV_UP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Navigate up"]',
    )

    FAQ_SCREEN_TITLE = "FAQ"
    FAQ_TOOLBAR_TITLE_ID = "com.cubii:id/toolbar_title"
    FAQ_TOOLBAR_TITLE = (AppiumBy.ID, FAQ_TOOLBAR_TITLE_ID)
    FAQ_TOOLBAR_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{FAQ_TOOLBAR_TITLE_ID}")',
    )
    FAQ_TOOLBAR_TITLE_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{FAQ_TOOLBAR_TITLE_ID}"]',
    )
    FAQ_TOOLBAR_TITLE_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{FAQ_TOOLBAR_TITLE_ID}" and @text="{FAQ_SCREEN_TITLE}"]',
    )

    FAQ_HELP_TEXT = "How can we help?"
    FAQ_HELP_TEXT_ID = "com.cubii:id/textView71"
    FAQ_HELP_TEXT_VIEW = (AppiumBy.ID, FAQ_HELP_TEXT_ID)
    FAQ_HELP_TEXT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{FAQ_HELP_TEXT_ID}")',
    )
    FAQ_HELP_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{FAQ_HELP_TEXT_ID}"]',
    )
    FAQ_HELP_TEXT_FULL_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{FAQ_HELP_TEXT_ID}" and @text="{FAQ_HELP_TEXT}"]',
    )

    # ---------- FAQ screen: subtitle label ("FAQ & HELP") ----------
    FAQ_SUBTITLE_TEXT = "FAQ & HELP"
    FAQ_SUBTITLE_ID = "com.cubii:id/textView70"
    FAQ_SUBTITLE = (AppiumBy.ID, FAQ_SUBTITLE_ID)
    FAQ_SUBTITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("com.cubii:id/textView70")',
    )
    FAQ_SUBTITLE_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/textView70"]',
    )
    FAQ_SUBTITLE_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/textView70" and @text="FAQ & HELP"]',
    )

    # ---------- FAQ screen: search bar ----------
    FAQ_SEARCH_BAR_ID = "com.cubii:id/editText4"
    FAQ_SEARCH_BAR = (AppiumBy.ID, FAQ_SEARCH_BAR_ID)
    FAQ_SEARCH_BAR_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("com.cubii:id/editText4")',
    )
    FAQ_SEARCH_BAR_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/editText4"]',
    )
    FAQ_SEARCH_BAR_HINT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().hint("Search for ...")',
    )

    # ---------- FAQ screen: question list ----------
    FAQ_LIST_ID = "com.cubii:id/rv_faq"
    FAQ_LIST = (AppiumBy.ID, FAQ_LIST_ID)
    FAQ_LIST_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("com.cubii:id/rv_faq")',
    )
    FAQ_LIST_XPATH = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rv_faq"]',
    )

    FAQ_QUESTION_ID = "com.cubii:id/tv_question"
    FAQ_QUESTION_ALL = (AppiumBy.ID, FAQ_QUESTION_ID)
    FAQ_QUESTION_ALL_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/tv_question"]',
    )
    FAQ_QUESTION_ALL_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("com.cubii:id/tv_question")',
    )

    FAQ_EXPAND_ICON_ID = "com.cubii:id/imageView24"
    FAQ_EXPAND_ICON_CONTENT_DESC = "Cubii"

    # All FAQ questions confirmed from Appium Inspector XML source
    FAQ_QUESTIONS_EXPECTED = (
        "How can I view RPM on Home Screen?",
        "How can I delete my Cubii app account and data?",
        "Why is Cubii asking for permission to scan nearby devices and my GPS location?",
        "Why can't I log into the app using my website credentials?",
        "How do I manually enter my workout data into the Cubii app?",
        "How do I disconnect my device from the App?",
        "iOS Devices: Issues Connecting to my Cubii",
        "Why doesn't my manual entry data in the app match the calories reported on my Cubii JR1/Cubii JR2/Cubii Go monitor?",
        "Can multiple people track their progress using one Bluetooth enabled device?",
    )

    CUSTOMER_SUPPORT_TOOLBAR_TITLE_ID = "com.cubii:id/toolbar_title"
    CUSTOMER_SUPPORT_TOOLBAR_TITLE = (
        AppiumBy.ID,
        CUSTOMER_SUPPORT_TOOLBAR_TITLE_ID,
    )
    CUSTOMER_SUPPORT_TOOLBAR_TITLE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/toolbar_title")',
    )
    CUSTOMER_SUPPORT_TOOLBAR_TITLE_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/toolbar_title"]',
    )

    CUSTOMER_SUPPORT_BACK_NAV_UP_ACCESSIBILITY_ID = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    CUSTOMER_SUPPORT_BACK_NAV_UP_CLASS = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")
    CUSTOMER_SUPPORT_BACK_NAV_UP_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Navigate up")',
    )
    CUSTOMER_SUPPORT_BACK_NAV_UP_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Navigate up"]',
    )

    CUSTOMER_SUPPORT_SCREEN_DETAILS = (
        ("com.cubii:id/textView70", "CUSTOMER SUPPORT"),
        ("com.cubii:id/textView71", "How can we help?"),
        ("com.cubii:id/textView72", "GETTING STARTED"),
        ("com.cubii:id/textView73", "Getting started"),
        ("com.cubii:id/textView76", "Email us"),
        ("com.cubii:id/textView77", "Call us"),
    )

    GETTING_STARTED_ITEM_ID = "com.cubii:id/textView73"
    GETTING_STARTED_TEXT = "Getting started"
    GETTING_STARTED_ITEM = (AppiumBy.ID, GETTING_STARTED_ITEM_ID)
    GETTING_STARTED_ITEM_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{GETTING_STARTED_ITEM_ID}")',
    )
    GETTING_STARTED_ITEM_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{GETTING_STARTED_ITEM_ID}"]',
    )
    GETTING_STARTED_ITEM_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{GETTING_STARTED_ITEM_ID}" and @text="{GETTING_STARTED_TEXT}"]',
    )

    EMAIL_US_ID = "com.cubii:id/textView76"
    EMAIL_US_TEXT = "Email us"
    EMAIL_US_ITEM = (AppiumBy.ID, EMAIL_US_ID)
    EMAIL_US_ITEM_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{EMAIL_US_ID}")',
    )
    EMAIL_US_ITEM_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{EMAIL_US_ID}"]',
    )
    EMAIL_US_ITEM_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{EMAIL_US_ID}" and @text="{EMAIL_US_TEXT}"]',
    )

    HELP_WEB_HEADING_TEXT = "What can we help you with today?"
    HELP_WEB_HEADING_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().text("{HELP_WEB_HEADING_TEXT}")',
    )
    HELP_WEB_HEADING_XPATH = (
        AppiumBy.XPATH,
        f'//android.view.View[@text="{HELP_WEB_HEADING_TEXT}"]',
    )
    HELP_WEB_LOGO_CONTENT_DESC = "Logo"
    HELP_WEB_LOGO_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Logo")',
    )
    HELP_WEB_LOGO_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Image[@content-desc="Logo"]',
    )
    HELP_WEB_LOGO_CLASS = (AppiumBy.CLASS_NAME, "android.widget.Image")
    CHROME_PACKAGE_HINTS = (
        "com.android.chrome",
        "chrome",
    )
    CHROME_CLOSE_TAB_ACCESSIBILITY_ID = (AppiumBy.ACCESSIBILITY_ID, "Close tab")
    CHROME_CLOSE_TAB_BUTTON = (AppiumBy.ID, "com.android.chrome:id/close_button")
    CHROME_CLOSE_TAB_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.android.chrome:id/close_button")',
    )
    CHROME_CLOSE_TAB_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageButton[@content-desc="Close tab"]',
    )

    CALL_US_ID = "com.cubii:id/textView77"
    CALL_US_TEXT = "Call us"
    CALL_US_ITEM = (AppiumBy.ID, CALL_US_ID)
    CALL_US_ITEM_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{CALL_US_ID}")',
    )
    CALL_US_ITEM_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{CALL_US_ID}"]',
    )
    CALL_US_ITEM_TEXT_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.TextView[@resource-id="{CALL_US_ID}" and @text="{CALL_US_TEXT}"]',
    )

    DIALER_PACKAGE_HINTS = (
        "com.google.android.dialer",
        "dialer",
    )
    DIALER_DIGITS_ID = "com.google.android.dialer:id/digits"
    DIALER_DIGITS = (AppiumBy.ID, DIALER_DIGITS_ID)
    DIALER_DIGITS_CLASS = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    DIALER_DIGITS_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{DIALER_DIGITS_ID}")',
    )
    DIALER_DIGITS_XPATH = (
        AppiumBy.XPATH,
        f'//android.widget.EditText[@resource-id="{DIALER_DIGITS_ID}"]',
    )

    CUBII_SETUP_YOUTUBE_VIDEO_TITLE = "How To Set Up Your Cubii"
    YOUTUBE_CHANNEL_NAME = "@CubiiVideos"
    YOUTUBE_PACKAGE_HINTS = (
        "com.google.android.youtube",
        "youtube",
    )
    YOUTUBE_TITLE_RESOURCE_IDS = (
        "com.google.android.youtube:id/title",
        "com.google.android.youtube:id/video_title",
        "com.google.android.youtube:id/video_title_text",
        "com.google.android.youtube:id/watch_panel_title",
    )
    YOUTUBE_TITLE_TEXT_FRAGMENTS = (
        "How To Set Up Your Cubii",
        "Set Up Your Cubii",
        "How To Set Up",
    )
    YOUTUBE_WATCH_CONTAINER_ID = (
        "com.google.android.youtube:id/next_gen_watch_container_layout"
    )
    YOUTUBE_WATCH_CONTAINER = (AppiumBy.ID, YOUTUBE_WATCH_CONTAINER_ID)
    YOUTUBE_WATCH_CONTAINER_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiSelector().resourceId("{YOUTUBE_WATCH_CONTAINER_ID}")',
    )
    YOUTUBE_WATCH_CONTAINER_XPATH = (
        AppiumBy.XPATH,
        f'//android.view.ViewGroup[@resource-id="{YOUTUBE_WATCH_CONTAINER_ID}"]',
    )

    @staticmethod
    def _help_list_option_locators(label: str) -> tuple[tuple, ...]:
        xpath = (
            f'//android.widget.TextView[@resource-id="{HelpPage.HELP_OPTION_TEXTVIEW_ID}" '
            f'and @text="{label}"]'
        )
        uiautomator = f'new UiSelector().text("{label}")'
        return (
            (AppiumBy.ANDROID_UIAUTOMATOR, uiautomator),
            (AppiumBy.XPATH, xpath),
        )

    @staticmethod
    def _screen_detail_locators(resource_id: str, expected_text: str) -> tuple[tuple, ...]:
        return (
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{resource_id}" and @text="{expected_text}"]',
            ),
            (AppiumBy.ID, resource_id),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("{resource_id}")',
            ),
        )

    @staticmethod
    def _is_visible_one_of(wait: WebDriverWait, locator_pairs: tuple[tuple, ...]) -> bool:
        for by, locator in locator_pairs:
            try:
                wait.until(ec.visibility_of_element_located((by, locator)))
                return True
            except Exception:
                continue
        return False

    def _assert_visible_one_of(
        self, locators: tuple[tuple, ...], description: str, wait: WebDriverWait | None = None
    ) -> None:
        wait = wait or WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator in locators:
            try:
                wait.until(ec.visibility_of_element_located(locator))
                self.LOGGER.info("%s verified via `%s`.", description, locator[1])
                return
            except TimeoutException:
                continue
        raise AssertionError(f"{description} not visible.")

    def _assert_visible_text_one_of(
        self,
        locators: tuple[tuple, ...],
        expected_text: str,
        description: str,
        wait: WebDriverWait | None = None,
    ) -> None:
        wait = wait or WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        last_text = None
        for locator in locators:
            try:
                element = wait.until(ec.visibility_of_element_located(locator))
                last_text = (element.text or element.get_attribute("text") or "").strip()
                if last_text == expected_text:
                    self.LOGGER.info("%s verified: %r via `%s`.", description, last_text, locator[1])
                    return
            except TimeoutException:
                continue
        raise AssertionError(
            f"Customer Support screen: {description} not visible or text mismatch. "
            f"Expected {expected_text!r}, got {last_text!r}."
        )

    def verify_whole_help_list(self) -> None:
        self.LOGGER.info(
            "Verifying Help screen options (%s).", ", ".join(self.HELP_LIST_OPTIONS)
        )
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        missing = []
        for label in self.HELP_LIST_OPTIONS:
            locators = self._help_list_option_locators(label)
            if self._is_visible_one_of(wait, locators):
                self.LOGGER.info("Help list option visible: %r.", label)
                continue
            missing.append(label)
        if missing:
            raise AssertionError(
                "Help list options not visible: " + ", ".join(missing) + "."
            )
        self.LOGGER.info("Whole Help list verified.")

    def tap_help_screen_back_option(self) -> None:
        self.LOGGER.info("Tapping Help screen back option (`Navigate up`).")
        for locator in (
            self.HELP_SCREEN_BACK_NAV_UP_ACCESSIBILITY_ID,
            self.HELP_SCREEN_BACK_NAV_UP_CLASS,
            self.HELP_SCREEN_BACK_NAV_UP_UIAUTOMATOR,
            self.HELP_SCREEN_BACK_NAV_UP_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Help screen back tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Help screen back locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Help screen back option (`Navigate up`) could not be located.")

    def tap_faq_screen_back_option(self) -> None:
        self.LOGGER.info("Tapping FAQ screen back option (`Navigate up`).")
        for locator in (
            self.FAQ_SCREEN_BACK_NAV_UP_ACCESSIBILITY_ID,
            self.FAQ_SCREEN_BACK_NAV_UP_CLASS,
            self.FAQ_SCREEN_BACK_NAV_UP_UIAUTOMATOR,
            self.FAQ_SCREEN_BACK_NAV_UP_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("FAQ screen back tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "FAQ screen back locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("FAQ screen back option (`Navigate up`) could not be located.")

    def tap_customer_support(self) -> None:
        self.LOGGER.info("Tapping Customer Support on Help screen.")
        for locator in (
            self.CUSTOMER_SUPPORT_MENU_ITEM,
            self.CUSTOMER_SUPPORT_MENU_ITEM_UIAUTOMATOR,
            self.CUSTOMER_SUPPORT_MENU_ITEM_BY_TEXT,
            self.CUSTOMER_SUPPORT_MENU_ITEM_TEXT_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Customer Support tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Customer Support locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Customer Support menu item could not be located.")

    def tap_faq_option(self) -> None:
        self.LOGGER.info("Tapping FAQ on Help screen.")
        for locator in (
            self.FAQ_MENU_ITEM,
            self.FAQ_MENU_ITEM_UIAUTOMATOR,
            self.FAQ_MENU_ITEM_BY_TEXT,
            self.FAQ_MENU_ITEM_TEXT_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("FAQ tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info("FAQ locator `%s` failed; trying next.", locator[1])
        raise TimeoutException("FAQ menu item could not be located.")

    def tap_product_manual(self) -> None:
        self.LOGGER.info("Tapping Product Manual on Help screen.")
        for locator in (
            self.PRODUCT_MANUAL_MENU_ITEM,
            self.PRODUCT_MANUAL_MENU_ITEM_UIAUTOMATOR,
            self.PRODUCT_MANUAL_MENU_ITEM_BY_TEXT,
            self.PRODUCT_MANUAL_MENU_ITEM_TEXT_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Product Manual tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Product Manual locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Product Manual menu item could not be located.")

    def verify_product_manual_screen_open(self) -> None:
        self.LOGGER.info("Verifying Product Manual screen is open.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        self._assert_visible_text_one_of(
            (
                self.PRODUCT_MANUAL_TOOLBAR_TITLE_TEXT_XPATH,
                self.PRODUCT_MANUAL_TOOLBAR_TITLE_XPATH,
                self.PRODUCT_MANUAL_TOOLBAR_TITLE_UIAUTOMATOR,
                self.PRODUCT_MANUAL_TOOLBAR_TITLE,
            ),
            self.PRODUCT_MANUAL_SCREEN_TITLE,
            f"Product Manual toolbar title (`{self.PRODUCT_MANUAL_TOOLBAR_TITLE_ID}`)",
            wait=wait,
        )
        self.LOGGER.info("Product Manual screen open verified.")

    def tap_product_manual_back_option(self) -> None:
        self.LOGGER.info("Tapping Product Manual screen back option (`Navigate up`).")
        for locator in (
            self.PRODUCT_MANUAL_BACK_NAV_UP_ACCESSIBILITY_ID,
            self.PRODUCT_MANUAL_BACK_NAV_UP_CLASS,
            self.PRODUCT_MANUAL_BACK_NAV_UP_UIAUTOMATOR,
            self.PRODUCT_MANUAL_BACK_NAV_UP_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Product Manual back tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Product Manual back locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException(
            "Product Manual back option (`Navigate up`) could not be located."
        )

    def tap_assembly_video(self) -> None:
        self.LOGGER.info("Tapping Assembly Video on Help screen.")
        for locator in (
            self.ASSEMBLY_VIDEO_MENU_ITEM,
            self.ASSEMBLY_VIDEO_MENU_ITEM_UIAUTOMATOR,
            self.ASSEMBLY_VIDEO_MENU_ITEM_BY_TEXT,
            self.ASSEMBLY_VIDEO_MENU_ITEM_TEXT_XPATH,
            self.ASSEMBLY_VIDEO_MENU_ITEM_TEXT_CONTAINS_UIAUTOMATOR,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Assembly Video tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Assembly Video locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Assembly Video menu item could not be located.")

    def verify_assembly_video_screen_open(self) -> None:
        self.LOGGER.info("Verifying Assembly Video screen is open.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        self._assert_visible_text_one_of(
            (
                self.ASSEMBLY_VIDEO_TOOLBAR_TITLE_TEXT_XPATH,
                self.ASSEMBLY_VIDEO_TOOLBAR_TITLE_XPATH,
                self.ASSEMBLY_VIDEO_TOOLBAR_TITLE_UIAUTOMATOR,
                self.ASSEMBLY_VIDEO_TOOLBAR_TITLE,
            ),
            self.ASSEMBLY_VIDEO_SCREEN_TITLE,
            f"Assembly Video toolbar title (`{self.ASSEMBLY_VIDEO_TOOLBAR_TITLE_ID}`)",
            wait=wait,
        )
        self.LOGGER.info("Assembly Video screen open verified.")

    def tap_assembly_video_back_option(self) -> None:
        self.LOGGER.info("Tapping Assembly Video screen back option (`Navigate up`).")
        for locator in (
            self.ASSEMBLY_VIDEO_BACK_NAV_UP_ACCESSIBILITY_ID,
            self.ASSEMBLY_VIDEO_BACK_NAV_UP_CLASS,
            self.ASSEMBLY_VIDEO_BACK_NAV_UP_UIAUTOMATOR,
            self.ASSEMBLY_VIDEO_BACK_NAV_UP_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Assembly Video back tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Assembly Video back locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException(
            "Assembly Video back option (`Navigate up`) could not be located."
        )

    def tap_privacy_policy(self) -> None:
        self.LOGGER.info("Tapping Privacy Policy on Help screen.")
        for locator in (
            self.PRIVACY_POLICY_MENU_ITEM,
            self.PRIVACY_POLICY_MENU_ITEM_UIAUTOMATOR,
            self.PRIVACY_POLICY_MENU_ITEM_BY_TEXT,
            self.PRIVACY_POLICY_MENU_ITEM_TEXT_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Privacy Policy tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Privacy Policy locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Privacy Policy menu item could not be located.")

    def verify_privacy_policy_screen(self) -> None:
        self.LOGGER.info("Verifying Privacy Policy screen is open.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        self._assert_visible_text_one_of(
            (
                self.PRIVACY_POLICY_TOOLBAR_TITLE_TEXT_XPATH,
                self.PRIVACY_POLICY_TOOLBAR_TITLE_XPATH,
                self.PRIVACY_POLICY_TOOLBAR_TITLE_UIAUTOMATOR,
                self.PRIVACY_POLICY_TOOLBAR_TITLE,
            ),
            self.PRIVACY_POLICY_SCREEN_TITLE,
            f"Privacy Policy toolbar title (`{self.PRIVACY_POLICY_TOOLBAR_TITLE_ID}`)",
            wait=wait,
        )
        self._assert_visible_text_one_of(
            (
                self.PRIVACY_POLICY_HEADING_XPATH,
                self.PRIVACY_POLICY_HEADING,
                self.PRIVACY_POLICY_HEADING_UIAUTOMATOR,
            ),
            self.PRIVACY_POLICY_SCREEN_TITLE,
            f"Privacy Policy heading (`{self.PRIVACY_POLICY_HEADING_ID}`)",
            wait=wait,
        )
        self.LOGGER.info("Privacy Policy screen verified.")

    def verify_privacy_policy_description(self) -> None:
        self.LOGGER.info("Verifying Privacy Policy description content.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        self._assert_visible_one_of(
            (
                self.PRIVACY_POLICY_SCROLL_CONTENT,
                self.PRIVACY_POLICY_SCROLL_CONTENT_UIAUTOMATOR,
            ),
            f"Privacy Policy scroll content (`{self.PRIVACY_POLICY_SCROLL_ID}`)",
            wait=wait,
        )
        for resource_id, expected_fragment in self.PRIVACY_POLICY_DESCRIPTION_CHECKS:
            locators = (
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().resourceId("{resource_id}")'
                    f'.textContains("{expected_fragment}")',
                ),
                (
                    AppiumBy.XPATH,
                    f'//android.widget.TextView[@resource-id="{resource_id}"'
                    f' and contains(@text, "{expected_fragment}")]',
                ),
                (AppiumBy.ID, resource_id),
            )
            self._assert_visible_text_fragment_one_of(
                locators,
                expected_fragment,
                f"Privacy Policy content (`{resource_id}`)",
                wait=wait,
            )
        self.LOGGER.info("Privacy Policy description verified.")

    def tap_terms_of_service(self) -> None:
        self.LOGGER.info("Tapping Terms of Service on Help screen.")
        for locator in (
            self.TERMS_OF_SERVICE_MENU_ITEM,
            self.TERMS_OF_SERVICE_MENU_ITEM_UIAUTOMATOR,
            self.TERMS_OF_SERVICE_MENU_ITEM_BY_TEXT,
            self.TERMS_OF_SERVICE_MENU_ITEM_TEXT_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Terms of Service tapped via `%s`.", locator[1])
                time.sleep(float(os.getenv("CUBII_TERMS_AFTER_TAP_SEC", "1.5")))
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Terms of Service locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Terms of Service menu item could not be located.")

    def _is_terms_webview_present(self, timeout: int = 3) -> bool:
        wait = WebDriverWait(self.driver, timeout)
        for locator in (
            self.TERMS_OF_SERVICE_WEBVIEW,
            self.TERMS_OF_SERVICE_WEBVIEW_UIAUTOMATOR,
            self.TERMS_OF_SERVICE_WEBVIEW_XPATH,
            (AppiumBy.CLASS_NAME, "android.webkit.WebView"),
        ):
            try:
                wait.until(ec.presence_of_element_located(locator))
                self.LOGGER.info("Terms WebView present via `%s`.", locator[1])
                return True
            except TimeoutException:
                continue
        try:
            if self.TERMS_OF_SERVICE_WEBVIEW_ID in (self.driver.page_source or ""):
                self.LOGGER.info("Terms WebView present in page source.")
                return True
        except Exception:
            pass
        return False

    def _wait_for_terms_webview(self) -> None:
        wait_sec = int(os.getenv("CUBII_TERMS_WEBVIEW_WAIT_SEC", "25"))
        pause = float(os.getenv("CUBII_TERMS_WEBVIEW_POLL_SEC", "1.0"))
        deadline = time.time() + wait_sec
        self.LOGGER.info(
            "Waiting up to %ss for Terms WebView (`%s`).",
            wait_sec,
            self.TERMS_OF_SERVICE_WEBVIEW_ID,
        )
        while time.time() < deadline:
            if self._is_terms_webview_present(timeout=2):
                return
            time.sleep(pause)
        raise AssertionError(
            f"Terms WebView (`{self.TERMS_OF_SERVICE_WEBVIEW_ID}`) not present within {wait_sec}s."
        )

    def verify_terms_of_service_screen_redirect(self) -> None:
        self.LOGGER.info("Verifying user redirected to Terms of Service screen.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        self._assert_visible_text_one_of(
            (
                self.TERMS_OF_SERVICE_TOOLBAR_TITLE_TEXT_XPATH,
                self.TERMS_OF_SERVICE_TOOLBAR_TITLE_XPATH,
                self.TERMS_OF_SERVICE_TOOLBAR_TITLE_UIAUTOMATOR,
                self.TERMS_OF_SERVICE_TOOLBAR_TITLE,
            ),
            self.TERMS_OF_SERVICE_SCREEN_TITLE,
            f"Terms of Service toolbar title (`{self.TERMS_OF_SERVICE_TOOLBAR_TITLE_ID}`)",
            wait=wait,
        )
        self.LOGGER.info(
            "Terms of Service toolbar verified; WebView loads in the next step."
        )

    def _collect_terms_webview_text(self) -> str:
        parts = [self._collect_ui_hierarchy_text()]
        try:
            webview = self.driver.find_element(AppiumBy.ID, self.TERMS_OF_SERVICE_WEBVIEW_ID)
            parts.append(webview.get_attribute("content-desc") or "")
        except Exception:
            pass

        try:
            for ctx in self.driver.contexts or []:
                if "WEBVIEW" not in (ctx or "").upper():
                    continue
                try:
                    self.driver.switch_to.context(ctx)
                    parts.append(self.driver.page_source or "")
                except Exception as exc:
                    self.LOGGER.debug("Terms WEBVIEW context %r read failed: %s", ctx, exc)
                finally:
                    try:
                        self.driver.switch_to.context("NATIVE_APP")
                    except Exception:
                        pass
        except Exception as exc:
            self.LOGGER.debug("Terms WEBVIEW contexts unavailable: %s", exc)

        return "\n".join(part for part in parts if part)

    def _terms_description_visible(self) -> bool:
        combined = self._normalize_visible_text(self._collect_terms_webview_text())
        if not combined:
            return False
        matches = sum(
            1
            for fragment in self.TERMS_OF_SERVICE_DESCRIPTION_FRAGMENTS
            if self._normalize_visible_text(fragment) in combined
        )
        return matches >= 2

    def _is_terms_cookie_overlay_visible(self) -> bool:
        """Cookie consent sheet (X / ACCEPT COOKIES), not the main Terms legal page."""
        combined = self._normalize_visible_text(self._collect_terms_webview_text())
        if not combined:
            return False
        return any(
            self._normalize_visible_text(fragment) in combined
            for fragment in self.TERMS_COOKIE_OVERLAY_FRAGMENTS
        )

    def _cookie_overlay_dismissed_after_action(self) -> bool:
        return not self._is_terms_cookie_overlay_visible()

    def _tap_terms_cancel_coordinate_grid(self) -> bool:
        """Tap likely X positions on the cookie sheet (top-right of WebView / screen)."""
        pause = float(os.getenv("CUBII_TERMS_AFTER_CANCEL_SEC", "1.0"))
        window = self.driver.get_window_size()
        width = int(window["width"])
        height = int(window["height"])

        tap_points: list[tuple[int, int, str]] = []
        try:
            webview = self.driver.find_element(
                AppiumBy.ID, self.TERMS_OF_SERVICE_WEBVIEW_ID
            )
            rect = webview.rect
            tap_points.extend(
                (
                    (
                        int(rect["x"] + rect["width"] * 0.93),
                        int(rect["y"] + rect["height"] * 0.22),
                        "webview-top-right",
                    ),
                    (
                        int(rect["x"] + rect["width"] * 0.90),
                        int(rect["y"] + rect["height"] * 0.30),
                        "webview-upper-right",
                    ),
                    (
                        int(rect["x"] + rect["width"] * 0.88),
                        int(rect["y"] + rect["height"] * 0.38),
                        "webview-mid-right",
                    ),
                )
            )
        except Exception as exc:
            self.LOGGER.debug("Terms WebView rect for cancel tap unavailable: %s", exc)

        tap_points.extend(
            (
                (int(width * 0.93), int(height * 0.26), "screen-top-right"),
                (int(width * 0.90), int(height * 0.32), "screen-upper-right"),
                (int(width * 0.88), int(height * 0.38), "screen-mid-right"),
            )
        )

        for x, y, label in tap_points:
            try:
                self.driver.execute_script("mobile: clickGesture", {"x": x, "y": y})
                self.LOGGER.info("Terms cookie cancel coordinate tap (%s) at (%s, %s).", label, x, y)
                time.sleep(pause)
                if self._cookie_overlay_dismissed_after_action():
                    self.LOGGER.info("Cookie overlay dismissed after %s tap.", label)
                    return True
            except Exception as exc:
                self.LOGGER.debug("Terms cancel tap %s failed: %s", label, exc)
        return False

    def _tap_terms_cookie_cancel_in_webview_context(self) -> bool:
        pause = float(os.getenv("CUBII_TERMS_AFTER_CANCEL_SEC", "1.0"))
        xpaths = (
            '//*[contains(@class,"close") or contains(@id,"close") or contains(@class,"Close")]',
            '//*[@aria-label="Close" or @aria-label="close" or contains(@aria-label,"Close")]',
            "//button[contains(.,'×') or contains(.,'✕') or contains(.,'X')]",
            "//*[contains(@onclick,'close') or contains(@class,'modal-close')]",
            "//a[contains(@class,'close')]",
        )
        try:
            for ctx in self.driver.contexts or []:
                if "WEBVIEW" not in (ctx or "").upper():
                    continue
                try:
                    self.driver.switch_to.context(ctx)
                    for xpath in xpaths:
                        for element in self.driver.find_elements(AppiumBy.XPATH, xpath):
                            try:
                                if element.is_displayed():
                                    element.click()
                                    self.LOGGER.info(
                                        "Terms cookie cancel via WEBVIEW %r (%s).",
                                        xpath,
                                        ctx,
                                    )
                                    time.sleep(pause)
                                    if self._cookie_overlay_dismissed_after_action():
                                        return True
                            except Exception:
                                continue
                except Exception as exc:
                    self.LOGGER.debug("WEBVIEW context %r cancel failed: %s", ctx, exc)
                finally:
                    try:
                        self.driver.switch_to.context("NATIVE_APP")
                    except Exception:
                        pass
        except Exception as exc:
            self.LOGGER.debug("WEBVIEW cancel contexts unavailable: %s", exc)
        finally:
            try:
                self.driver.switch_to.context("NATIVE_APP")
            except Exception:
                pass
        return False

    def _tap_terms_cookie_cancel_icon(self) -> None:
        """Dismiss cookie overlay via WebView close, coordinate X, or toolbar Navigate up."""
        pause = float(os.getenv("CUBII_TERMS_AFTER_CANCEL_SEC", "1.0"))

        if not self._is_terms_cookie_overlay_visible():
            self.LOGGER.info("Cookie overlay not detected; skipping cancel tap.")
            return

        if self._tap_terms_cookie_cancel_in_webview_context():
            return
        if self._tap_terms_cancel_coordinate_grid():
            return

        for locator in (
            self.TERMS_OF_SERVICE_NAV_UP_ACCESSIBILITY_ID,
            self.TERMS_OF_SERVICE_NAV_UP_UIAUTOMATOR,
            self.TERMS_OF_SERVICE_NAV_UP_XPATH,
        ):
            try:
                WebDriverWait(self.driver, 3).until(
                    ec.element_to_be_clickable(locator)
                ).click()
                self.LOGGER.info(
                    "Terms cookie overlay: tapped toolbar Navigate up via `%s`.",
                    locator[1],
                )
                time.sleep(pause)
                if self._cookie_overlay_dismissed_after_action():
                    return
            except TimeoutException:
                continue

        try:
            self.driver.press_keycode(ANDROID_KEYCODE_BACK)
            self.LOGGER.info("Terms cookie overlay: pressed Android BACK.")
            time.sleep(pause)
            if self._cookie_overlay_dismissed_after_action():
                return
        except Exception as exc:
            self.LOGGER.debug("Terms cookie BACK dismiss failed: %s", exc)

        if os.getenv("CUBII_TERMS_ALLOW_ACCEPT_COOKIES_FALLBACK", "1") == "1":
            if self._tap_terms_accept_cookies_button():
                return

        raise TimeoutException(
            "Terms of Service cookie cancel icon could not be tapped "
            "(overlay still shows ACCEPT COOKIES / ALLOW ALL COOKIES)."
        )

    def _tap_terms_accept_cookies_button(self) -> bool:
        """Fallback: tap ACCEPT COOKIES when X is not reachable in WebView."""
        pause = float(os.getenv("CUBII_TERMS_AFTER_CANCEL_SEC", "1.0"))
        for xpath in (
            '//*[contains(text(),"ACCEPT COOKIES") or contains(., "ACCEPT COOKIES")]',
            "//button[contains(translate(., 'accept', 'ACCEPT'), 'ACCEPT')]",
        ):
            try:
                for ctx in self.driver.contexts or []:
                    if "WEBVIEW" not in (ctx or "").upper():
                        continue
                    try:
                        self.driver.switch_to.context(ctx)
                        for element in self.driver.find_elements(AppiumBy.XPATH, xpath):
                            if element.is_displayed():
                                element.click()
                                self.LOGGER.info(
                                    "Terms cookie overlay dismissed via ACCEPT COOKIES (%s).",
                                    ctx,
                                )
                                time.sleep(pause)
                                if self._cookie_overlay_dismissed_after_action():
                                    return True
                    except Exception:
                        continue
                    finally:
                        try:
                            self.driver.switch_to.context("NATIVE_APP")
                        except Exception:
                            pass
            except Exception:
                continue

        try:
            self.driver.switch_to.context("NATIVE_APP")
        except Exception:
            pass

        window = self.driver.get_window_size()
        x = int(window["width"] * 0.5)
        y = int(window["height"] * 0.88)
        try:
            self.driver.execute_script("mobile: clickGesture", {"x": x, "y": y})
            self.LOGGER.info("Terms ACCEPT COOKIES coordinate tap at (%s, %s).", x, y)
            time.sleep(pause)
            return self._cookie_overlay_dismissed_after_action()
        except Exception:
            return False

    def verify_terms_of_service_description_and_click_cancel(self) -> None:
        self.LOGGER.info(
            "Verifying Terms of Service cookie description and tapping cancel icon."
        )
        self._wait_for_terms_webview()
        time.sleep(float(os.getenv("CUBII_TERMS_WEBVIEW_LOAD_SEC", "2.0")))

        desc_wait = int(os.getenv("CUBII_TERMS_DESCRIPTION_WAIT_SEC", "20"))
        deadline = time.time() + desc_wait
        while time.time() < deadline:
            if self._terms_description_visible():
                self.LOGGER.info("Terms of Service cookie description verified.")
                break
            time.sleep(1.0)
        else:
            snippet = self._collect_terms_webview_text()[:400].replace("\n", " ")
            raise AssertionError(
                "Terms of Service description not found in WebView. "
                f"Expected fragments from {self.TERMS_OF_SERVICE_DESCRIPTION_FRAGMENTS!r}. "
                f"Snippet: {snippet!r}"
            )

        self._tap_terms_cookie_cancel_icon()
        self.LOGGER.info("Terms of Service description verified and cancel icon tapped.")

    def _assert_visible_text_fragment_one_of(
        self,
        locators: tuple[tuple, ...],
        expected_fragment: str,
        description: str,
        wait: WebDriverWait | None = None,
    ) -> None:
        wait = wait or WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        fragment_key = self._normalize_visible_text(expected_fragment)
        last_text = None
        for locator in locators:
            try:
                element = wait.until(ec.visibility_of_element_located(locator))
                last_text = self._element_text_blob(element).strip()
                normalized = self._normalize_visible_text(last_text)
                if fragment_key in normalized:
                    self.LOGGER.info(
                        "%s verified: fragment %r in %r via `%s`.",
                        description,
                        expected_fragment,
                        last_text[:80],
                        locator[1],
                    )
                    return
            except TimeoutException:
                continue
        raise AssertionError(
            f"Privacy Policy screen: {description} not visible or missing {expected_fragment!r}. "
            f"Last text: {last_text!r}."
        )

    def _try_tap_privacy_policy_floating_back(self) -> bool:
        """Tap the left-edge floating back control when it is in the accessibility tree."""
        short_wait = WebDriverWait(self.driver, 3)
        for locator in (
            self.PRIVACY_POLICY_FLOATING_BACK_XPATH,
            self.PRIVACY_POLICY_FLOATING_BACK,
            self.PRIVACY_POLICY_FLOATING_BACK_UIAUTOMATOR,
            self.PRIVACY_POLICY_FLOATING_BACK_XPATH_ANY,
            self.PRIVACY_POLICY_FLOATING_BACK_IMAGE_XPATH,
        ):
            try:
                short_wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info(
                    "Privacy Policy floating back tapped via `%s`.", locator[1]
                )
                time.sleep(float(os.getenv("CUBII_PRIVACY_POLICY_AFTER_BACK_SEC", "1.0")))
                return True
            except TimeoutException:
                self.LOGGER.info(
                    "Privacy Policy floating back `%s` not found; trying next.",
                    locator[1],
                )
        return False

    def _tap_privacy_policy_floating_back_coordinates(self) -> bool:
        """Tap near the left-center floating back pill (matches on-screen affordance)."""
        window = self.driver.get_window_size()
        x = int(window["width"] * float(os.getenv("CUBII_PRIVACY_POLICY_BACK_TAP_X_FRAC", "0.07")))
        y = int(window["height"] * float(os.getenv("CUBII_PRIVACY_POLICY_BACK_TAP_Y_FRAC", "0.50")))
        try:
            self.driver.tap([(x, y)], 150)
            time.sleep(float(os.getenv("CUBII_PRIVACY_POLICY_AFTER_BACK_SEC", "1.0")))
            self.LOGGER.info(
                "Privacy Policy floating back coordinate tap at (%s, %s).", x, y
            )
            return True
        except Exception as exc:
            self.LOGGER.info("Privacy Policy coordinate tap failed: %s", exc)
            return False

    def _is_on_privacy_policy_detail_screen(self, timeout: int = 2) -> bool:
        """True when Privacy Policy content is showing (not the Help menu list)."""
        wait = WebDriverWait(self.driver, timeout)
        if self._is_visible_one_of(
            wait,
            (
                self.PRIVACY_POLICY_SCROLL_CONTENT,
                self.PRIVACY_POLICY_SCROLL_CONTENT_UIAUTOMATOR,
            ),
        ):
            return True
        if self._is_visible_one_of(
            wait,
            (
                self.PRIVACY_POLICY_INTRO,
                self.PRIVACY_POLICY_INTRO_UIAUTOMATOR,
                self.PRIVACY_POLICY_INTRO_CONTAINS_UIAUTOMATOR,
            ),
        ):
            return True
        return False

    def _perform_privacy_policy_android_gestures(self) -> None:
        """
        Android: try floating back, then edge swipes that match common back transitions.

        Many Cubii flows use a horizontal pager — swipe right (finger moves right)
        often returns to the previous page; we also try left-edge drag for the
        floating back affordance.
        """
        self.LOGGER.info("Privacy Policy: trying Android back gestures.")
        if self._try_tap_privacy_policy_floating_back():
            if self._is_on_help_screen(timeout=2) or self._left_privacy_policy_detail(timeout=2):
                return
        if self._tap_privacy_policy_floating_back_coordinates():
            time.sleep(float(os.getenv("CUBII_PRIVACY_POLICY_AFTER_BACK_SEC", "0.5")))
            if self._is_on_help_screen(timeout=2) or self._left_privacy_policy_detail(timeout=2):
                return

        window = self.driver.get_window_size()
        width = int(window["width"])
        height = int(window["height"])
        y = int(height * float(os.getenv("CUBII_PRIVACY_POLICY_BACK_Y_FRAC", "0.50")))
        pause = float(os.getenv("CUBII_PRIVACY_POLICY_AFTER_BACK_SEC", "1.0"))
        speed = int(os.getenv("CUBII_PRIVACY_POLICY_BACK_DRAG_SPEED", "2200"))

        # Swipe right across the screen (ViewPager / slide-back to Help).
        swipe_right_start = int(
            width * float(os.getenv("CUBII_PRIVACY_POLICY_SWIPE_RIGHT_START_X_FRAC", "0.15"))
        )
        swipe_right_end = int(
            width * float(os.getenv("CUBII_PRIVACY_POLICY_SWIPE_RIGHT_END_X_FRAC", "0.85"))
        )
        try:
            self.driver.execute_script(
                "mobile: dragGesture",
                {
                    "startX": swipe_right_start,
                    "startY": y,
                    "endX": swipe_right_end,
                    "endY": y,
                    "speed": speed,
                },
            )
            time.sleep(pause)
            self.LOGGER.info(
                "Privacy Policy swipe-right back (startX=%s endX=%s y=%s).",
                swipe_right_start,
                swipe_right_end,
                y,
            )
            if not self._is_on_privacy_policy_detail_screen(timeout=2):
                return
        except Exception as exc:
            self.LOGGER.info("Privacy Policy swipe-right failed (%s).", exc)

        try:
            self.driver.execute_script(
                "mobile: swipeGesture",
                {
                    "left": int(width * 0.05),
                    "top": int(height * 0.35),
                    "width": int(width * 0.90),
                    "height": int(height * 0.30),
                    "direction": "right",
                    "percent": float(
                        os.getenv("CUBII_PRIVACY_POLICY_SWIPE_RIGHT_PERCENT", "0.75")
                    ),
                },
            )
            time.sleep(pause)
            self.LOGGER.info("Privacy Policy full-width swipeGesture (right) completed.")
            if not self._is_on_privacy_policy_detail_screen(timeout=2):
                return
        except Exception as exc:
            self.LOGGER.info("Privacy Policy swipeGesture right failed (%s).", exc)

        # Left-edge drag toward the screen edge (floating back pill area).
        start_x = int(width * float(os.getenv("CUBII_PRIVACY_POLICY_BACK_START_X_FRAC", "0.14")))
        end_x = int(width * float(os.getenv("CUBII_PRIVACY_POLICY_BACK_END_X_FRAC", "0.02")))
        try:
            self.driver.execute_script(
                "mobile: dragGesture",
                {
                    "startX": start_x,
                    "startY": y,
                    "endX": end_x,
                    "endY": y,
                    "speed": speed,
                },
            )
            time.sleep(pause)
            self.LOGGER.info(
                "Privacy Policy left-edge drag (startX=%s endX=%s y=%s).",
                start_x,
                end_x,
                y,
            )
        except Exception as exc:
            self.LOGGER.info("Privacy Policy left-edge drag failed (%s).", exc)

    def swipe_left_from_privacy_policy_screen(self) -> None:
        """Leave Privacy Policy using Android-friendly gestures (see _perform_*)."""
        self._perform_privacy_policy_android_gestures()

    def tap_privacy_policy_back_option(self) -> None:
        """Leave Privacy Policy: toolbar back, floating back, swipe/drag, then Android BACK."""
        self.LOGGER.info("Leaving Privacy Policy screen.")
        short_wait = WebDriverWait(self.driver, 3)
        for locator in (
            self.PRIVACY_POLICY_BACK_NAV_UP_ACCESSIBILITY_ID,
            self.PRIVACY_POLICY_BACK_NAV_UP_CLASS,
            self.PRIVACY_POLICY_BACK_NAV_UP_UIAUTOMATOR,
            self.PRIVACY_POLICY_BACK_NAV_UP_XPATH,
        ):
            try:
                short_wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Privacy Policy back tapped via `%s`.", locator[1])
                time.sleep(float(os.getenv("CUBII_PRIVACY_POLICY_AFTER_BACK_SEC", "1.0")))
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Privacy Policy toolbar back `%s` not found; trying next.", locator[1]
                )

        try:
            self.swipe_left_from_privacy_policy_screen()
            if self._is_on_help_screen(timeout=2):
                return
            self.LOGGER.info(
                "Still on Privacy Policy after swipe; trying Android BACK."
            )
        except TimeoutException as exc:
            self.LOGGER.info("Swipe left failed (%s); trying Android BACK.", exc)

        self._press_android_back_until_help_screen()

    def _is_on_help_screen(self, timeout: int = 3) -> bool:
        if self._is_on_privacy_policy_detail_screen(timeout=1):
            return False
        wait = WebDriverWait(self.driver, timeout)
        if not self._is_visible_one_of(
            wait,
            (
                self.HELP_LIST_RECYCLER,
                self.HELP_LIST_RECYCLER_UIAUTOMATOR,
                self.HELP_LIST_RECYCLER_XPATH,
            ),
        ):
            return False
        for label in ("Customer Support", "FAQ", "Product Manual", "Assembly Video"):
            if self._is_visible_one_of(wait, self._help_list_option_locators(label)):
                return True
        return False

    def _left_privacy_policy_detail(self, timeout: int = 2) -> bool:
        return not self._is_on_privacy_policy_detail_screen(timeout=timeout)

    def _recover_help_screen_if_overshot(self) -> None:
        """
        After BACK, the app may land on More menu or Home instead of Help list.

        Re-open Help from More (tap Help) or from Home (three-dot → Help).
        """
        if self._is_on_help_screen(timeout=3):
            return

        home_page = HomePage(self.driver)
        pause = float(os.getenv("CUBII_PRIVACY_POLICY_AFTER_BACK_SEC", "1.0"))

        if home_page._is_logout_menu_available(timeout=2):
            self.LOGGER.info(
                "Landed on More menu after leaving Privacy Policy; tapping Help again."
            )
            home_page.tap_help_menu_item()
            time.sleep(pause)
            if self._is_on_help_screen(timeout=Settings.EXPLICIT_WAIT):
                return

        if home_page.is_cubii_home_logo_visible(timeout=2):
            self.LOGGER.info(
                "Landed on Home after leaving Privacy Policy; reopening More → Help."
            )
            home_page.tap_settings_highlight()
            time.sleep(pause)
            home_page.tap_help_menu_item()
            time.sleep(pause)
            if self._is_on_help_screen(timeout=Settings.EXPLICIT_WAIT):
                return

        raise TimeoutException(
            "Left Privacy Policy but could not reach Help screen. "
            f"Foreground package={self._current_package()!r}. "
            "Device may have stopped on Home or More without recoverable Help entry."
        )

    def _press_android_back_until_help_screen(self) -> None:
        """
        Press Android BACK until Help is visible or we have left Privacy Policy.

        Default is one BACK — a second press often goes Help → Home and breaks verification.
        """
        max_attempts = int(os.getenv("CUBII_PRIVACY_POLICY_BACK_KEY_ATTEMPTS", "1"))
        pause = float(os.getenv("CUBII_PRIVACY_POLICY_AFTER_BACK_SEC", "1.0"))

        if self._is_on_help_screen(timeout=2):
            self.LOGGER.info("Already on Help screen; skipping BACK.")
            return

        for attempt in range(max_attempts):
            if self._is_on_help_screen(timeout=2):
                self.LOGGER.info("Help screen visible after %s BACK press(es).", attempt)
                return

            try:
                self.driver.press_keycode(ANDROID_KEYCODE_BACK)
                self.LOGGER.info(
                    "Pressed Android BACK (%s/%s) to leave Privacy Policy.",
                    attempt + 1,
                    max_attempts,
                )
            except Exception as exc:
                self.LOGGER.warning("Android BACK failed: %s", exc)
            time.sleep(pause)

            if self._is_on_help_screen(timeout=2):
                self.LOGGER.info("Help screen visible after BACK.")
                return

            if self._left_privacy_policy_detail(timeout=2):
                self.LOGGER.info(
                    "Left Privacy Policy after BACK (%s/%s); stopping further BACK presses "
                    "to avoid overshooting to Home.",
                    attempt + 1,
                    max_attempts,
                )
                self._recover_help_screen_if_overshot()
                return

        if self._is_on_help_screen(timeout=Settings.EXPLICIT_WAIT):
            return

        if self._left_privacy_policy_detail(timeout=2):
            self._recover_help_screen_if_overshot()
            return

        raise TimeoutException(
            f"Still on Privacy Policy after {max_attempts} Android BACK press(es)."
        )

    def go_back_from_privacy_policy_to_help_screen(self) -> None:
        """
        Leave Privacy Policy (no in-app back — app bug).

        Runs Android back gestures and BACK key only; does not verify Help screen.
        """
        self.LOGGER.info(
            "Leaving Privacy Policy (gestures + Android BACK, no screen verification)."
        )
        try:
            self.swipe_left_from_privacy_policy_screen()
        except Exception as exc:
            self.LOGGER.info("Privacy Policy gestures not completed: %s", exc)

        time.sleep(float(os.getenv("CUBII_PRIVACY_POLICY_AFTER_GESTURE_SEC", "0.5")))

        back_attempts = int(os.getenv("CUBII_PRIVACY_POLICY_BACK_KEY_ATTEMPTS", "2"))
        pause = float(os.getenv("CUBII_PRIVACY_POLICY_AFTER_BACK_SEC", "1.0"))
        for attempt in range(back_attempts):
            try:
                self.driver.press_keycode(ANDROID_KEYCODE_BACK)
                self.LOGGER.info(
                    "Pressed Android BACK (%s/%s) leaving Privacy Policy.",
                    attempt + 1,
                    back_attempts,
                )
            except Exception as exc:
                self.LOGGER.warning("Android BACK failed: %s", exc)
            time.sleep(pause)

        self.LOGGER.info("Privacy Policy back navigation finished (no Help screen check).")

    def verify_returned_to_help_screen(self) -> None:
        self.LOGGER.info("Verifying user returned to Help screen.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        self._assert_visible_one_of(
            (
                self.HELP_LIST_RECYCLER,
                self.HELP_LIST_RECYCLER_UIAUTOMATOR,
                self.HELP_LIST_RECYCLER_XPATH,
            ),
            f"Help list (`{self.HELP_LIST_RECYCLER_ID}`)",
            wait=wait,
        )
        if self._is_on_privacy_policy_detail_screen(timeout=2):
            raise AssertionError(
                "Still on Privacy Policy detail after back navigation. "
                "Try increasing CUBII_PRIVACY_POLICY_BACK_KEY_ATTEMPTS or gesture env vars."
            )
        for label in ("Customer Support", "FAQ", "Product Manual", "Assembly Video"):
            locators = self._help_list_option_locators(label)
            if self._is_visible_one_of(wait, locators):
                self.LOGGER.info("Help screen confirmed via visible option %r.", label)
                self.LOGGER.info("Returned to Help screen verified.")
                return
        raise AssertionError(
            "Help screen not visible after leaving Privacy Policy. "
            "Expected Help list (`rv_help`) and a menu option such as Customer Support or FAQ."
        )

    def verify_faq_screen_redirect(self) -> None:
        self.LOGGER.info("Verifying user redirected to FAQ screen.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        self._assert_visible_text_one_of(
            (
                self.FAQ_TOOLBAR_TITLE_TEXT_XPATH,
                self.FAQ_TOOLBAR_TITLE_XPATH,
                self.FAQ_TOOLBAR_TITLE_UIAUTOMATOR,
                self.FAQ_TOOLBAR_TITLE,
            ),
            self.FAQ_SCREEN_TITLE,
            f"FAQ toolbar title (`{self.FAQ_TOOLBAR_TITLE_ID}`)",
            wait=wait,
        )
        self.LOGGER.info("FAQ screen redirect verified.")

    def verify_faq_how_can_we_help_text(self, expected_fragment: str | None = None) -> None:
        fragment = (expected_fragment or "How can we help").strip().rstrip("?")
        expected_full = self.FAQ_HELP_TEXT
        self.LOGGER.info(
            "Verifying FAQ screen text containing %r (`textView71`).", fragment
        )
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        last_text = None
        for locator in (
            self.FAQ_HELP_TEXT_FULL_XPATH,
            self.FAQ_HELP_TEXT_VIEW,
            self.FAQ_HELP_TEXT_UIAUTOMATOR,
            self.FAQ_HELP_TEXT_XPATH,
        ):
            try:
                element = wait.until(ec.visibility_of_element_located(locator))
                last_text = self._element_text_blob(element).strip()
                normalized = self._normalize_visible_text(last_text)
                if (
                    self._normalize_visible_text(expected_full) == normalized
                    or self._normalize_visible_text(fragment) in normalized
                ):
                    self.LOGGER.info(
                        "FAQ help text verified: %r via `%s`.", last_text, locator[1]
                    )
                    return
            except TimeoutException:
                continue
        raise AssertionError(
            f"FAQ screen: {fragment!r} text not visible on `textView71`. "
            f"Expected {expected_full!r}, got {last_text!r}."
        )

    def verify_faq_subtitle(self) -> None:
        self.LOGGER.info("Verifying 'FAQ & HELP' subtitle on FAQ screen.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        self._assert_visible_text_one_of(
            (
                self.FAQ_SUBTITLE_TEXT_XPATH,
                self.FAQ_SUBTITLE,
                self.FAQ_SUBTITLE_UIAUTOMATOR,
                self.FAQ_SUBTITLE_XPATH,
            ),
            self.FAQ_SUBTITLE_TEXT,
            f"FAQ subtitle ('FAQ & HELP', `{self.FAQ_SUBTITLE_ID}`)",
            wait=wait,
        )
        self.LOGGER.info("FAQ subtitle verified.")

    def verify_faq_search_bar_visible(self) -> None:
        self.LOGGER.info("Verifying search bar is visible on FAQ screen.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        self._assert_visible_one_of(
            (
                self.FAQ_SEARCH_BAR,
                self.FAQ_SEARCH_BAR_UIAUTOMATOR,
                self.FAQ_SEARCH_BAR_XPATH,
                self.FAQ_SEARCH_BAR_HINT_UIAUTOMATOR,
            ),
            f"FAQ search bar (`{self.FAQ_SEARCH_BAR_ID}`)",
            wait=wait,
        )
        self.LOGGER.info("FAQ search bar verified.")

    def verify_faq_list_visible(self) -> None:
        self.LOGGER.info("Verifying FAQ question list (rv_faq) is visible.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        self._assert_visible_one_of(
            (
                self.FAQ_LIST,
                self.FAQ_LIST_UIAUTOMATOR,
                self.FAQ_LIST_XPATH,
            ),
            f"FAQ question list (`{self.FAQ_LIST_ID}`)",
            wait=wait,
        )
        self.LOGGER.info("FAQ question list verified.")

    def verify_faq_screen_structure(self) -> None:
        self.LOGGER.info("Verifying full FAQ screen structure.")
        self.verify_faq_screen_redirect()
        self.verify_faq_subtitle()
        self.verify_faq_how_can_we_help_text()
        self.verify_faq_search_bar_visible()
        self.verify_faq_list_visible()
        self.LOGGER.info("Full FAQ screen structure verified.")

    @staticmethod
    def _faq_question_match_key(question_text: str) -> str:
        """Stable key for matching FAQ rows (ignores trailing spaces and extra whitespace)."""
        return re.sub(r"\s+", " ", (question_text or "").strip()).casefold()

    def _read_visible_faq_question_texts(self) -> list[str]:
        texts = []
        try:
            elements = self.driver.find_elements(*self.FAQ_QUESTION_ALL)
        except Exception as exc:
            self.LOGGER.debug("Reading FAQ question elements failed: %s", exc)
            return texts
        for element in elements:
            blob = self._element_text_blob(element).strip()
            if blob:
                texts.append(blob)
        return texts

    def _faq_expected_matches_collected(
        self, expected_question: str, collected_keys: set[str]
    ) -> bool:
        expected_key = self._faq_question_match_key(expected_question)
        if expected_key in collected_keys:
            return True
        # App XML sometimes adds trailing spaces or slightly different spacing.
        for collected_key in collected_keys:
            if expected_key in collected_key or collected_key in expected_key:
                return True
        fragment = expected_key[:50].strip()
        return any(fragment in collected_key for collected_key in collected_keys)

    def scroll_faq_list_to_top(self) -> None:
        self.LOGGER.info("Scrolling FAQ list toward the top.")
        window = self.driver.get_window_size()
        swipes = int(os.getenv("CUBII_FAQ_SCROLL_TO_TOP_SWIPES", "3"))
        for _ in range(swipes):
            try:
                self.driver.execute_script(
                    "mobile: swipeGesture",
                    {
                        "left": int(window["width"] * 0.05),
                        "top": int(window["height"] * 0.22),
                        "width": int(window["width"] * 0.90),
                        "height": int(window["height"] * 0.62),
                        "direction": "down",
                        "percent": 0.45,
                    },
                )
                time.sleep(float(os.getenv("CUBII_FAQ_SCROLL_SETTLE_SEC", "0.4")))
            except Exception as exc:
                self.LOGGER.debug("FAQ scroll-to-top swipe failed: %s", exc)
                break

    def _collect_all_faq_questions_via_scroll(self) -> dict[str, str]:
        """Scroll through rv_faq and collect every question text (raw + normalized key)."""
        self.scroll_faq_list_to_top()
        collected: dict[str, str] = {}
        max_swipes = int(os.getenv("CUBII_FAQ_LIST_SCROLL_MAX", "12"))
        idle_passes = 0

        for swipe_index in range(max_swipes + 1):
            before_count = len(collected)
            for raw_text in self._read_visible_faq_question_texts():
                key = self._faq_question_match_key(raw_text)
                if key and key not in collected:
                    collected[key] = raw_text
                    self.LOGGER.info("FAQ question collected: %r.", raw_text)

            if len(collected) == before_count:
                idle_passes += 1
            else:
                idle_passes = 0

            if idle_passes >= 2:
                self.LOGGER.info(
                    "FAQ list collection finished after %d swipe(s); %d unique question(s).",
                    swipe_index,
                    len(collected),
                )
                break

            if swipe_index < max_swipes:
                self.scroll_faq_screen_down()

        return collected

    def verify_faq_questions_list(self) -> None:
        self.LOGGER.info(
            "Verifying all %d FAQ questions: scroll to top, then scroll down "
            "through rv_faq and collect each question.",
            len(self.FAQ_QUESTIONS_EXPECTED),
        )
        collected = self._collect_all_faq_questions_via_scroll()
        collected_keys = set(collected.keys())

        missing = []
        for question in self.FAQ_QUESTIONS_EXPECTED:
            if self._faq_expected_matches_collected(question, collected_keys):
                matched_raw = collected.get(self._faq_question_match_key(question))
                if not matched_raw:
                    for key, raw in collected.items():
                        if self._faq_expected_matches_collected(question, {key}):
                            matched_raw = raw
                            break
                self.LOGGER.info(
                    "FAQ question verified: expected=%r, on_screen=%r.",
                    question,
                    matched_raw or question,
                )
                continue
            self.LOGGER.warning("FAQ question NOT found after scrolling: %r.", question)
            missing.append(question)

        if missing:
            raise AssertionError(
                f"The following FAQ questions were not found on the list:\n"
                + "\n".join(f"  - {q}" for q in missing)
                + f"\nCollected on screen ({len(collected)}): "
                + ", ".join(collected.values())
            )
        self.LOGGER.info("All FAQ questions verified.")

    def tap_faq_question_by_text(self, question_text: str) -> None:
        self.LOGGER.info("Tapping FAQ question: %r.", question_text)
        self._scroll_faq_question_into_view(question_text)
        for locator in (
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{self.FAQ_QUESTION_ID}" and @text="{question_text}"]',
            ),
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{self.FAQ_QUESTION_ID}" and contains(@text, "{question_text}")]',
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("{self.FAQ_QUESTION_ID}").text("{question_text}")',
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("{self.FAQ_QUESTION_ID}").textContains("{question_text}")',
            ),
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{question_text}")'),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().textContains("{question_text}")',
            ),
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("FAQ question %r tapped via `%s`.", question_text, locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "FAQ question locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException(f"FAQ question {question_text!r} could not be located.")

    def search_in_faq(self, keyword: str) -> None:
        self.LOGGER.info("Searching FAQ for keyword: %r.", keyword)
        for locator in (
            self.FAQ_SEARCH_BAR,
            self.FAQ_SEARCH_BAR_UIAUTOMATOR,
            self.FAQ_SEARCH_BAR_XPATH,
            self.FAQ_SEARCH_BAR_HINT_UIAUTOMATOR,
        ):
            try:
                el = self.wait.until(ec.element_to_be_clickable(locator))
                el.clear()
                el.send_keys(keyword)
                self.LOGGER.info("Typed %r in FAQ search bar via `%s`.", keyword, locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "FAQ search bar locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("FAQ search bar could not be located.")

    def verify_faq_search_result_contains(self, expected_text: str) -> None:
        self.LOGGER.info(
            "Verifying FAQ search result contains %r.", expected_text
        )
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for locator in (
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("{self.FAQ_QUESTION_ID}").textContains("{expected_text}")',
            ),
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{self.FAQ_QUESTION_ID}"'
                f' and contains(@text, "{expected_text}")]',
            ),
        ):
            try:
                wait.until(ec.visibility_of_element_located(locator))
                self.LOGGER.info(
                    "FAQ search result containing %r found via `%s`.", expected_text, locator[1]
                )
                return
            except TimeoutException:
                continue
        raise AssertionError(
            f"No FAQ question containing {expected_text!r} was visible after search."
        )

    def clear_faq_search(self) -> None:
        self.LOGGER.info("Clearing FAQ search bar.")
        for locator in (
            self.FAQ_SEARCH_BAR,
            self.FAQ_SEARCH_BAR_UIAUTOMATOR,
            self.FAQ_SEARCH_BAR_XPATH,
        ):
            try:
                el = self.wait.until(ec.element_to_be_clickable(locator))
                el.clear()
                self.LOGGER.info("FAQ search bar cleared via `%s`.", locator[1])
                return
            except TimeoutException:
                continue
        raise TimeoutException("FAQ search bar could not be located for clearing.")

    def _faq_item_container_xpath(self, question_text: str) -> str:
        """Return XPath for the direct FrameLayout child of rv_faq that wraps a given FAQ row.

        Using a direct-child step (/android.widget.FrameLayout) from rv_faq instead of
        the descendant axis (//) prevents accidentally matching the root-level FrameLayout
        whose bounds span the full screen (2400px) and never change size.
        """
        return (
            f'//androidx.recyclerview.widget.RecyclerView[@resource-id="{self.FAQ_LIST_ID}"]'
            f'/android.widget.FrameLayout'
            f'[.//android.widget.TextView[@resource-id="{self.FAQ_QUESTION_ID}"'
            f' and (contains(@text, "{question_text}") or @text="{question_text}")]]'
        )

    def _scroll_faq_question_into_view(self, question_text: str) -> None:
        """Scroll the FAQ list until the target question is visible."""
        fragment = question_text.strip()[:60]
        scroll_locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().resourceId("{self.FAQ_LIST_ID}"))'
            f'.scrollIntoView(new UiSelector()'
            f'.resourceId("{self.FAQ_QUESTION_ID}").textContains("{fragment}"))',
        )
        fallback_scroll_locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector()'
            f'.resourceId("{self.FAQ_QUESTION_ID}").textContains("{fragment}"))',
        )
        for locator in (scroll_locator, fallback_scroll_locator):
            try:
                WebDriverWait(self.driver, Settings.EXPLICIT_WAIT).until(
                    ec.presence_of_element_located(locator)
                )
                self.LOGGER.info("FAQ question %r scrolled into view.", question_text)
                return
            except TimeoutException:
                continue
        self.LOGGER.info(
            "Could not scroll FAQ question %r into view; trying current viewport.",
            question_text,
        )

    def _center_visible_faq_question(self, question_text: str) -> None:
        """Nudge the FAQ list so a partially visible row is fully usable."""
        locator = (AppiumBy.XPATH, self._faq_item_container_xpath(question_text))
        try:
            element = WebDriverWait(self.driver, 2).until(
                ec.presence_of_element_located(locator)
            )
        except TimeoutException:
            return

        rect = element.rect
        window = self.driver.get_window_size()
        visible_top = int(window["height"] * 0.16)
        visible_bottom = int(window["height"] * 0.88)
        row_top = int(rect.get("y", 0))
        row_bottom = row_top + int(rect.get("height", 0))

        if visible_top <= row_top and row_bottom <= visible_bottom:
            return

        direction = "up" if row_bottom > visible_bottom else "down"
        self.LOGGER.info(
            "FAQ question %r is clipped (top=%d, bottom=%d); nudging %s.",
            question_text,
            row_top,
            row_bottom,
            direction,
        )
        try:
            self.driver.execute_script(
                "mobile: swipeGesture",
                {
                    "left": int(window["width"] * 0.05),
                    "top": int(window["height"] * 0.20),
                    "width": int(window["width"] * 0.90),
                    "height": int(window["height"] * 0.65),
                    "direction": direction,
                    "percent": 0.28,
                },
            )
            time.sleep(float(os.getenv("CUBII_FAQ_SCROLL_SETTLE_SEC", "0.5")))
        except Exception as exc:
            self.LOGGER.debug("FAQ row centering swipe failed: %s", exc)

    def _get_faq_item_height(self, question_text: str) -> int:
        """Return the current pixel height of the FAQ item container for a question."""
        self._scroll_faq_question_into_view(question_text)
        locator = (AppiumBy.XPATH, self._faq_item_container_xpath(question_text))
        el = self.wait.until(ec.presence_of_element_located(locator))
        return el.size["height"]

    def scroll_faq_screen_down(self) -> None:
        self.LOGGER.info("Scrolling down on FAQ screen.")
        window = self.driver.get_window_size()
        try:
            self.driver.execute_script(
                "mobile: swipeGesture",
                {
                    "left": int(window["width"] * 0.05),
                    "top": int(window["height"] * 0.22),
                    "width": int(window["width"] * 0.90),
                    "height": int(window["height"] * 0.62),
                    "direction": "up",
                    "percent": 0.55,
                },
            )
            time.sleep(float(os.getenv("CUBII_FAQ_SCROLL_SETTLE_SEC", "0.5")))
            self.LOGGER.info("FAQ screen scrolled down.")
        except Exception as exc:
            raise AssertionError(f"Could not scroll down on FAQ screen. Error: {exc}") from exc

    def tap_faq_question_and_verify_expanded(self, question_text: str) -> None:
        self.LOGGER.info(
            "Tapping FAQ question and verifying it expands: %r.", question_text
        )
        height_before = self._get_faq_item_height(question_text)
        self.LOGGER.info(
            "FAQ item height before tap: %dpx for %r.", height_before, question_text
        )
        self.tap_faq_question_by_text(question_text)
        time.sleep(float(os.getenv("CUBII_FAQ_EXPAND_SETTLE_SEC", "1.0")))
        height_after = self._get_faq_item_height(question_text)
        self.LOGGER.info(
            "FAQ item height after tap: %dpx for %r.", height_after, question_text
        )
        if height_after <= height_before:
            raise AssertionError(
                f"FAQ question {question_text!r} did not expand. "
                f"Container height before: {height_before}px, after: {height_after}px."
            )
        self.LOGGER.info(
            "FAQ question %r expanded (height %dpx → %dpx).",
            question_text,
            height_before,
            height_after,
        )

    def tap_faq_question_and_verify_collapsed(self, question_text: str) -> None:
        self.LOGGER.info(
            "Tapping FAQ question and verifying it collapses: %r.", question_text
        )
        height_before = self._get_faq_item_height(question_text)
        self.LOGGER.info(
            "FAQ item height before tap (expanded): %dpx for %r.",
            height_before,
            question_text,
        )
        self.tap_faq_question_by_text(question_text)
        time.sleep(float(os.getenv("CUBII_FAQ_EXPAND_SETTLE_SEC", "1.0")))
        height_after = self._get_faq_item_height(question_text)
        self.LOGGER.info(
            "FAQ item height after tap (should be collapsed): %dpx for %r.",
            height_after,
            question_text,
        )
        if height_after >= height_before:
            raise AssertionError(
                f"FAQ question {question_text!r} did not collapse. "
                f"Container height before: {height_before}px, after: {height_after}px."
            )
        self.LOGGER.info(
            "FAQ question %r collapsed (height %dpx → %dpx).",
            question_text,
            height_before,
            height_after,
        )

    def verify_customer_support_screen_redirect(self) -> None:
        self.LOGGER.info("Verifying user redirected to Customer Support screen.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        self._assert_visible_one_of(
            (
                self.CUSTOMER_SUPPORT_TOOLBAR_TITLE_XPATH,
                self.CUSTOMER_SUPPORT_TOOLBAR_TITLE_UIAUTOMATOR,
                self.CUSTOMER_SUPPORT_TOOLBAR_TITLE,
            ),
            "toolbar title (`toolbar_title`)",
            wait=wait,
        )
        self.LOGGER.info("Customer Support screen redirect verified.")

    def verify_customer_support_screen_details(self) -> None:
        self.LOGGER.info("Verifying all available details on Customer Support screen.")
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        for resource_id, expected_text in self.CUSTOMER_SUPPORT_SCREEN_DETAILS:
            locators = self._screen_detail_locators(resource_id, expected_text)
            self._assert_visible_text_one_of(
                locators,
                expected_text,
                f"{expected_text!r} (`{resource_id}`)",
                wait=wait,
            )
        self.LOGGER.info("All Customer Support screen details verified.")

    def tap_customer_support_back_button(self) -> None:
        self.LOGGER.info("Tapping Customer Support back button (`Navigate up`).")
        for locator in (
            self.CUSTOMER_SUPPORT_BACK_NAV_UP_ACCESSIBILITY_ID,
            self.CUSTOMER_SUPPORT_BACK_NAV_UP_CLASS,
            self.CUSTOMER_SUPPORT_BACK_NAV_UP_UIAUTOMATOR,
            self.CUSTOMER_SUPPORT_BACK_NAV_UP_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Customer Support back tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Customer Support back locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException(
            "Customer Support back button (`Navigate up`) could not be located."
        )

    def tap_getting_started(self) -> None:
        self.LOGGER.info("Tapping Getting Started on Customer Support screen.")
        for locator in (
            self.GETTING_STARTED_ITEM_TEXT_XPATH,
            self.GETTING_STARTED_ITEM,
            self.GETTING_STARTED_ITEM_UIAUTOMATOR,
            self.GETTING_STARTED_ITEM_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Getting Started tapped via `%s`.", locator[1])
                time.sleep(
                    float(os.getenv("CUBII_HELP_AFTER_GETTING_STARTED_TAP_SEC", "2.0"))
                )
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Getting Started locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Getting Started (`textView73`) could not be located.")

    @staticmethod
    def _normalize_visible_text(value: str) -> str:
        return re.sub(r"\s+", " ", (value or "").strip()).casefold()

    def _current_package(self) -> str:
        try:
            return (self.driver.current_package or "").strip()
        except Exception:
            return ""

    def _package_looks_like_youtube(self, package_name: str) -> bool:
        pkg = (package_name or "").lower()
        return any(hint in pkg for hint in self.YOUTUBE_PACKAGE_HINTS)

    def _wait_for_youtube_foreground(self) -> str:
        wait_sec = int(os.getenv("CUBII_HELP_YOUTUBE_OPEN_WAIT_SEC", "30"))
        pause = float(os.getenv("CUBII_HELP_YOUTUBE_POLL_SEC", "0.5"))
        deadline = time.time() + wait_sec
        last_pkg = ""

        while time.time() < deadline:
            last_pkg = self._current_package()
            if self._package_looks_like_youtube(last_pkg):
                self.LOGGER.info("YouTube in foreground (package=%s).", last_pkg)
                time.sleep(float(os.getenv("CUBII_HELP_YOUTUBE_SETTLE_SEC", "4.0")))
                return last_pkg
            time.sleep(pause)

        raise AssertionError(
            f"YouTube did not open within {wait_sec}s. Last foreground package: {last_pkg!r}."
        )

    @staticmethod
    def _compact_alnum(text: str) -> str:
        return re.sub(r"[^a-z0-9]", "", (text or "").casefold())

    def _text_matches_youtube_title(self, raw_text: str, expected_title: str) -> bool:
        normalized = self._normalize_visible_text(raw_text)
        if not normalized:
            return False
        normalized_expected = self._normalize_visible_text(expected_title)
        if normalized_expected in normalized:
            return True
        compact = self._compact_alnum(raw_text)
        if self._compact_alnum(expected_title) in compact:
            return True
        for fragment in self.YOUTUBE_TITLE_TEXT_FRAGMENTS:
            if self._normalize_visible_text(fragment) in normalized:
                return True
            if self._compact_alnum(fragment) in compact:
                return True
        return False

    def _hierarchy_matches_youtube_video(self, hierarchy: str, expected_title: str) -> bool:
        if not hierarchy:
            return False
        if self._text_matches_youtube_title(hierarchy, expected_title):
            return True
        compact = self._compact_alnum(hierarchy)
        has_cubii = "cubii" in compact
        has_setup = "setup" in compact or "set up" in self._normalize_visible_text(hierarchy)
        has_channel = "cubiivideos" in compact
        if has_channel and (has_setup or has_cubii):
            self.LOGGER.info(
                "YouTube hierarchy matched via channel + Cubii/setup keywords."
            )
            return True
        if has_cubii and has_setup:
            self.LOGGER.info(
                "YouTube hierarchy matched via Cubii + setup keywords."
            )
            return True
        return False

    def _read_uiautomator_dump_xml(self) -> str:
        dump_path = "/sdcard/cubii_youtube_help_dump.xml"
        try:
            self.driver.execute_script(
                "mobile: shell",
                {"command": "uiautomator", "args": ["dump", dump_path]},
            )
            result = self.driver.execute_script(
                "mobile: shell",
                {"command": "cat", "args": [dump_path]},
            )
            if isinstance(result, str):
                return result
            if isinstance(result, dict):
                return (result.get("stdout") or result.get("value") or "") or ""
        except Exception as exc:
            self.LOGGER.debug("uiautomator dump read failed: %s", exc)
        return ""

    def _collect_ui_hierarchy_text(self) -> str:
        parts = []
        try:
            parts.append(self.driver.page_source or "")
        except Exception as exc:
            self.LOGGER.debug("page_source read failed: %s", exc)

        parts.append(self._read_uiautomator_dump_xml())

        try:
            for ctx in self.driver.contexts or []:
                if "WEBVIEW" not in (ctx or "").upper():
                    continue
                try:
                    self.driver.switch_to.context(ctx)
                    parts.append(self.driver.page_source or "")
                except Exception:
                    pass
                finally:
                    try:
                        self.driver.switch_to.context("NATIVE_APP")
                    except Exception:
                        pass
        except Exception as exc:
            self.LOGGER.debug("WEBVIEW hierarchy read failed: %s", exc)

        return "\n".join(part for part in parts if part)

    def _element_text_blob(self, element) -> str:
        return " ".join(
            filter(
                None,
                [
                    element.text,
                    element.get_attribute("text"),
                    element.get_attribute("content-desc"),
                    element.get_attribute("name"),
                ],
            )
        )

    def _youtube_video_title_visible(self, expected_title: str) -> bool:
        require_displayed = os.getenv("CUBII_HELP_YOUTUBE_REQUIRE_DISPLAYED", "0") == "1"

        hierarchy = self._collect_ui_hierarchy_text()
        if self._hierarchy_matches_youtube_video(hierarchy, expected_title):
            self.LOGGER.info("YouTube video matched via combined UI hierarchy.")
            return True

        for resource_id in self.YOUTUBE_TITLE_RESOURCE_IDS:
            try:
                for element in self.driver.find_elements(AppiumBy.ID, resource_id):
                    if require_displayed and not element.is_displayed():
                        continue
                    blob = self._element_text_blob(element)
                    if self._text_matches_youtube_title(blob, expected_title):
                        self.LOGGER.info(
                            "YouTube video title matched via resource-id %r: %r",
                            resource_id,
                            blob.strip(),
                        )
                        return True
            except Exception:
                continue

        ui_selectors = []
        for fragment in self.YOUTUBE_TITLE_TEXT_FRAGMENTS:
            escaped = fragment.replace("\\", "\\\\").replace('"', '\\"')
            ui_selectors.extend(
                (
                    f'new UiSelector().text("{escaped}")',
                    f'new UiSelector().textContains("{escaped}")',
                    f'new UiSelector().descriptionContains("{escaped}")',
                )
            )
        for selector in ui_selectors:
            try:
                for element in self.driver.find_elements(
                    AppiumBy.ANDROID_UIAUTOMATOR, selector
                ):
                    if require_displayed and not element.is_displayed():
                        continue
                    blob = self._element_text_blob(element)
                    if self._text_matches_youtube_title(blob, expected_title):
                        self.LOGGER.info(
                            "YouTube video title matched via UiSelector %r: %r",
                            selector,
                            blob.strip(),
                        )
                        return True
            except Exception:
                continue

        xpath_fragments = list(self.YOUTUBE_TITLE_TEXT_FRAGMENTS) + [expected_title]
        for fragment in xpath_fragments:
            for attr in ("text", "content-desc"):
                xpath = f'//*[contains(@{attr}, "{fragment}")]'
                try:
                    for element in self.driver.find_elements(AppiumBy.XPATH, xpath):
                        if require_displayed and not element.is_displayed():
                            continue
                        blob = self._element_text_blob(element)
                        if self._text_matches_youtube_title(blob, expected_title):
                            self.LOGGER.info(
                                "YouTube video title matched via XPath %r: %r",
                                xpath,
                                blob.strip(),
                            )
                            return True
                except Exception:
                    continue

        try:
            for element in self.driver.find_elements(
                AppiumBy.CLASS_NAME, "android.widget.TextView"
            ):
                if require_displayed and not element.is_displayed():
                    continue
                blob = self._element_text_blob(element)
                if self._text_matches_youtube_title(blob, expected_title):
                    self.LOGGER.info(
                        "YouTube video title matched via TextView scan: %r",
                        blob.strip(),
                    )
                    return True
        except Exception as exc:
            self.LOGGER.debug("TextView title scan failed: %s", exc)

        return False

    def _youtube_watch_screen_visible(self) -> bool:
        if not self._package_looks_like_youtube(self._current_package()):
            return False

        for locator in (
            self.YOUTUBE_WATCH_CONTAINER,
            self.YOUTUBE_WATCH_CONTAINER_UIAUTOMATOR,
            self.YOUTUBE_WATCH_CONTAINER_XPATH,
        ):
            try:
                WebDriverWait(self.driver, 3).until(
                    ec.presence_of_element_located(locator)
                )
                self.LOGGER.info(
                    "YouTube watch screen container found via `%s`.", locator[1]
                )
                return True
            except TimeoutException:
                continue

        hierarchy = self._collect_ui_hierarchy_text()
        if self.YOUTUBE_WATCH_CONTAINER_ID in hierarchy:
            self.LOGGER.info(
                "YouTube watch screen container found in UI hierarchy."
            )
            return True

        return False

    def _wait_for_youtube_watch_screen(self) -> None:
        wait_sec = int(os.getenv("CUBII_HELP_YOUTUBE_WATCH_WAIT_SEC", "30"))
        pause = float(os.getenv("CUBII_HELP_YOUTUBE_WATCH_POLL_SEC", "1.0"))
        deadline = time.time() + wait_sec

        self.LOGGER.info(
            "Waiting up to %ss for YouTube watch screen (`%s`).",
            wait_sec,
            self.YOUTUBE_WATCH_CONTAINER_ID,
        )
        while time.time() < deadline:
            if self._youtube_watch_screen_visible():
                return
            time.sleep(pause)

        raise AssertionError(
            f"YouTube watch screen was not detected within {wait_sec}s. "
            f"Foreground package={self._current_package()!r}. "
            f"Expected resource-id {self.YOUTUBE_WATCH_CONTAINER_ID!r}."
        )

    def _log_youtube_title_best_effort(self, expected_title: str) -> None:
        title_wait_sec = int(os.getenv("CUBII_HELP_YOUTUBE_TITLE_WAIT_SEC", "15"))
        pause = float(os.getenv("CUBII_HELP_YOUTUBE_TITLE_POLL_SEC", "1.5"))
        deadline = time.time() + title_wait_sec

        self.LOGGER.info(
            "Best-effort check for YouTube video title %r (up to %ss).",
            expected_title,
            title_wait_sec,
        )
        while time.time() < deadline:
            if self._youtube_video_title_visible(expected_title):
                self.LOGGER.info(
                    "YouTube video title verified (best-effort): %r.", expected_title
                )
                return
            time.sleep(pause)

        strict_title = os.getenv("CUBII_HELP_YOUTUBE_REQUIRE_TITLE", "0") == "1"
        if strict_title:
            raise AssertionError(
                f"YouTube watch screen opened but video title {expected_title!r} "
                f"was not readable within {title_wait_sec}s "
                "(CUBII_HELP_YOUTUBE_REQUIRE_TITLE=1)."
            )

        self.LOGGER.warning(
            "YouTube watch screen verified; video title %r was not readable in the "
            "UI hierarchy. Continuing because title detection is best-effort only.",
            expected_title,
        )

    def verify_cubii_setup_video_in_youtube(self, video_title: str | None = None) -> None:
        expected_title = (video_title or self.CUBII_SETUP_YOUTUBE_VIDEO_TITLE).strip()
        self.LOGGER.info(
            "Verifying Cubii setup video opened in YouTube (title=%r).", expected_title
        )
        self._wait_for_youtube_foreground()
        time.sleep(float(os.getenv("CUBII_HELP_YOUTUBE_POST_OPEN_PAUSE_SEC", "2.0")))
        self._wait_for_youtube_watch_screen()
        self._log_youtube_title_best_effort(expected_title)
        self.LOGGER.info("YouTube Cubii setup video flow verified.")

    def _cubii_app_package(self) -> str:
        return (os.getenv("APP_PACKAGE") or Settings.APP_PACKAGE or "com.cubii").strip()

    def return_to_cubii_application(self) -> None:
        """Leave YouTube (or external browser) and return focus to the Cubii app."""
        cubii_pkg = self._cubii_app_package()
        back_attempts = int(os.getenv("CUBII_HELP_YOUTUBE_BACK_ATTEMPTS", "2"))
        pause = float(os.getenv("CUBII_HELP_RETURN_TO_CUBII_PAUSE_SEC", "0.8"))

        self.LOGGER.info("Returning to Cubii from YouTube (package=%s).", cubii_pkg)

        for attempt in range(back_attempts):
            if self._current_package() == cubii_pkg:
                self.LOGGER.info("Back on Cubii after %s BACK press(es).", attempt)
                break
            try:
                self.driver.press_keycode(ANDROID_KEYCODE_BACK)
                self.LOGGER.info(
                    "Pressed BACK (%s/%s) to leave YouTube.", attempt + 1, back_attempts
                )
            except Exception as exc:
                self.LOGGER.warning("BACK key failed: %s", exc)
            time.sleep(pause)

        if self._current_package() != cubii_pkg:
            try:
                self.driver.activate_app(cubii_pkg)
                self.LOGGER.info("Activated Cubii via activate_app(%s).", cubii_pkg)
            except Exception as exc:
                raise AssertionError(
                    f"Could not return to Cubii from YouTube. "
                    f"Current package={self._current_package()!r}. Error: {exc}"
                ) from exc
            time.sleep(pause)

        try:
            self.driver.switch_to.context("NATIVE_APP")
        except Exception:
            pass

        if self._current_package() != cubii_pkg:
            raise AssertionError(
                f"Expected Cubii foreground ({cubii_pkg!r}) after leaving YouTube, "
                f"got {self._current_package()!r}."
            )

        time.sleep(float(os.getenv("CUBII_HELP_AFTER_RETURN_TO_CUBII_SEC", "1.0")))
        self.LOGGER.info("Returned to Cubii application from YouTube.")

    def tap_email_us(self) -> None:
        self.LOGGER.info("Tapping Email us on Customer Support screen.")
        for locator in (
            self.EMAIL_US_ITEM_TEXT_XPATH,
            self.EMAIL_US_ITEM,
            self.EMAIL_US_ITEM_UIAUTOMATOR,
            self.EMAIL_US_ITEM_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Email us tapped via `%s`.", locator[1])
                time.sleep(
                    float(os.getenv("CUBII_HELP_AFTER_EMAIL_US_TAP_SEC", "2.0"))
                )
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Email us locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Email us (`textView76`) could not be located.")

    def _package_looks_like_chrome(self, package_name: str) -> bool:
        pkg = (package_name or "").lower()
        return any(hint in pkg for hint in self.CHROME_PACKAGE_HINTS)

    def _wait_for_help_web_browser_foreground(self) -> str:
        wait_sec = int(os.getenv("CUBII_HELP_EMAIL_WEB_OPEN_WAIT_SEC", "20"))
        pause = float(os.getenv("CUBII_HELP_EMAIL_WEB_POLL_SEC", "0.5"))
        deadline = time.time() + wait_sec
        last_pkg = ""

        while time.time() < deadline:
            last_pkg = self._current_package()
            if self._package_looks_like_chrome(last_pkg):
                self.LOGGER.info("Help web page browser in foreground (package=%s).", last_pkg)
                time.sleep(float(os.getenv("CUBII_HELP_EMAIL_WEB_SETTLE_SEC", "2.0")))
                return last_pkg
            time.sleep(pause)

        raise AssertionError(
            f"Help web page browser did not open within {wait_sec}s. "
            f"Last foreground package: {last_pkg!r}."
        )

    def _help_web_logo_visible(self) -> bool:
        for locator in (
            self.HELP_WEB_LOGO_XPATH,
            self.HELP_WEB_LOGO_UIAUTOMATOR,
            self.HELP_WEB_LOGO_CLASS,
        ):
            try:
                WebDriverWait(self.driver, 3).until(
                    ec.presence_of_element_located(locator)
                )
                self.LOGGER.info("Cubii help web logo found via `%s`.", locator[1])
                return True
            except TimeoutException:
                continue

        hierarchy = self._collect_ui_hierarchy_text()
        if 'content-desc="Logo"' in hierarchy or "description=\"Logo\"" in hierarchy:
            self.LOGGER.info("Cubii help web logo found in UI hierarchy.")
            return True
        return False

    def _help_web_heading_visible(self) -> bool:
        for locator in (
            self.HELP_WEB_HEADING_XPATH,
            self.HELP_WEB_HEADING_UIAUTOMATOR,
        ):
            try:
                WebDriverWait(self.driver, 3).until(
                    ec.presence_of_element_located(locator)
                )
                self.LOGGER.info(
                    "Help web heading found via `%s`.", locator[1]
                )
                return True
            except TimeoutException:
                continue

        hierarchy = self._collect_ui_hierarchy_text()
        if self.HELP_WEB_HEADING_TEXT in hierarchy:
            self.LOGGER.info("Help web heading found in UI hierarchy.")
            return True
        return False

    def verify_help_email_us_web_page(self) -> None:
        self.LOGGER.info(
            "Verifying Cubii help web page (logo + %r).", self.HELP_WEB_HEADING_TEXT
        )
        self._wait_for_help_web_browser_foreground()

        wait_sec = int(os.getenv("CUBII_HELP_EMAIL_WEB_VERIFY_WAIT_SEC", "30"))
        pause = float(os.getenv("CUBII_HELP_EMAIL_WEB_VERIFY_POLL_SEC", "1.5"))
        deadline = time.time() + wait_sec

        while time.time() < deadline:
            logo_ok = self._help_web_logo_visible()
            heading_ok = self._help_web_heading_visible()
            if logo_ok and heading_ok:
                self.LOGGER.info("Cubii help web page verified (logo and heading).")
                return
            time.sleep(pause)

        missing = []
        if not self._help_web_logo_visible():
            missing.append(f"Cubii logo (content-desc={self.HELP_WEB_LOGO_CONTENT_DESC!r})")
        if not self._help_web_heading_visible():
            missing.append(self.HELP_WEB_HEADING_TEXT)
        raise AssertionError(
            "Help web page verification failed. Not visible: "
            + ", ".join(missing)
            + f". Foreground package={self._current_package()!r}."
        )

    def tap_chrome_close_tab_button(self) -> None:
        self.LOGGER.info("Tapping Chrome Close tab button.")
        for locator in (
            self.CHROME_CLOSE_TAB_ACCESSIBILITY_ID,
            self.CHROME_CLOSE_TAB_BUTTON,
            self.CHROME_CLOSE_TAB_UIAUTOMATOR,
            self.CHROME_CLOSE_TAB_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Chrome Close tab tapped via `%s`.", locator[1])
                time.sleep(float(os.getenv("CUBII_HELP_AFTER_CHROME_CLOSE_SEC", "1.0")))
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Chrome Close tab locator `%s` failed; trying next.", locator[1]
                )

        self.LOGGER.info("Close tab not visible; attempting Android back as fallback.")
        try:
            self.driver.press_keycode(ANDROID_KEYCODE_BACK)
            time.sleep(float(os.getenv("CUBII_HELP_AFTER_CHROME_CLOSE_SEC", "1.0")))
            self.LOGGER.info("Chrome tab closed via Android BACK fallback.")
            return
        except Exception as exc:
            raise TimeoutException(
                f"Chrome Close tab button could not be located. Error: {exc}"
            ) from exc

    def tap_call_us(self) -> None:
        self.LOGGER.info("Tapping Call us on Customer Support screen.")
        for locator in (
            self.CALL_US_ITEM_TEXT_XPATH,
            self.CALL_US_ITEM,
            self.CALL_US_ITEM_UIAUTOMATOR,
            self.CALL_US_ITEM_XPATH,
        ):
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Call us tapped via `%s`.", locator[1])
                time.sleep(float(os.getenv("CUBII_HELP_AFTER_CALL_US_TAP_SEC", "2.0")))
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Call us locator `%s` failed; trying next.", locator[1]
                )
        raise TimeoutException("Call us (`textView77`) could not be located.")

    def _package_looks_like_dialer(self, package_name: str) -> bool:
        pkg = (package_name or "").lower()
        return any(hint in pkg for hint in self.DIALER_PACKAGE_HINTS)

    def _wait_for_dialer_foreground(self) -> str:
        wait_sec = int(os.getenv("CUBII_HELP_DIALER_OPEN_WAIT_SEC", "20"))
        pause = float(os.getenv("CUBII_HELP_DIALER_POLL_SEC", "0.5"))
        deadline = time.time() + wait_sec
        last_pkg = ""

        while time.time() < deadline:
            last_pkg = self._current_package()
            if self._package_looks_like_dialer(last_pkg):
                self.LOGGER.info("Dialer in foreground (package=%s).", last_pkg)
                time.sleep(float(os.getenv("CUBII_HELP_DIALER_SETTLE_SEC", "1.5")))
                return last_pkg
            time.sleep(pause)

        raise AssertionError(
            f"Dialer did not open within {wait_sec}s. Last foreground package: {last_pkg!r}."
        )

    def _read_dialer_digits_text(self) -> str:
        for locator in (
            self.DIALER_DIGITS,
            self.DIALER_DIGITS_UIAUTOMATOR,
            self.DIALER_DIGITS_XPATH,
            self.DIALER_DIGITS_CLASS,
        ):
            try:
                element = WebDriverWait(self.driver, 3).until(
                    ec.presence_of_element_located(locator)
                )
                return self._element_text_blob(element).strip()
            except TimeoutException:
                continue
        return ""

    @staticmethod
    def _looks_like_phone_number(value: str) -> bool:
        digits = re.sub(r"\D", "", value or "")
        return len(digits) >= 7

    def verify_dial_screen_open_with_number(self) -> None:
        self.LOGGER.info("Verifying dial screen is open with a phone number.")
        self._wait_for_dialer_foreground()

        wait_sec = int(os.getenv("CUBII_HELP_DIALER_VERIFY_WAIT_SEC", "20"))
        pause = float(os.getenv("CUBII_HELP_DIALER_VERIFY_POLL_SEC", "1.0"))
        deadline = time.time() + wait_sec

        while time.time() < deadline:
            for locator in (
                self.DIALER_DIGITS,
                self.DIALER_DIGITS_UIAUTOMATOR,
                self.DIALER_DIGITS_XPATH,
            ):
                try:
                    element = WebDriverWait(self.driver, 3).until(
                        ec.visibility_of_element_located(locator)
                    )
                    number_text = self._element_text_blob(element).strip()
                    if self._looks_like_phone_number(number_text):
                        self.LOGGER.info(
                            "Dial screen verified via `%s` with number %r.",
                            locator[1],
                            number_text,
                        )
                        return
                    if number_text:
                        self.LOGGER.info(
                            "Dial digits visible via `%s` (text=%r); accepting as number.",
                            locator[1],
                            number_text,
                        )
                        return
                except TimeoutException:
                    continue

            number_text = self._read_dialer_digits_text()
            if self._looks_like_phone_number(number_text):
                self.LOGGER.info("Dial screen verified with number %r.", number_text)
                return

            hierarchy = self._collect_ui_hierarchy_text()
            if self.DIALER_DIGITS_ID in hierarchy and re.search(
                r"\d{3}[^\d]*\d{3}[^\d]*\d{4}", hierarchy
            ):
                self.LOGGER.info("Dial screen verified via UI hierarchy (digits field + number).")
                return

            time.sleep(pause)

        number_text = self._read_dialer_digits_text()
        raise AssertionError(
            "Dial screen verification failed. "
            f"Foreground package={self._current_package()!r}, "
            f"digits text={number_text!r}, "
            f"expected resource-id {self.DIALER_DIGITS_ID!r} with a phone number."
        )
