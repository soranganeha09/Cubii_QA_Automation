import logging
import os
import random
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage


class EditProfilePage(BasePage):
    LOGGER = logging.getLogger("cubii_edit_profile_page")

    FIRST_NAME_INPUT = (AppiumBy.ID, "com.cubii:id/editText")
    FIRST_NAME_INPUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/editText"]',
    )
    FIRST_NAME_INPUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/editText")',
    )

    TEXTINPUT_ERROR_ID = "com.cubii:id/textinput_error"
    FIRST_NAME_TIL_ID = "com.cubii:id/til_first_name"
    EDIT_PROFILE_FIELD_ERROR_MESSAGES = {
        "first name": "Please enter your first name",
        "last name": "Please enter your last name",
        "email": "Please enter your email",
        "valid email": "Please enter a valid email",
    }
    CHANGE_PASSWORD_FIELD_ERROR_MESSAGES = {
        "old password": "Enter old password",
        "new password": "Enter new password",
        "repeat new password": "Please enter repeat password",
        "repeat password mismatch": "Both the password should be same",
    }
    INVALID_EMAIL_VALUE = "invalid-email"

    LAST_NAME_INPUT = (AppiumBy.ID, "com.cubii:id/et_last_name")
    LAST_NAME_INPUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/et_last_name"]',
    )
    LAST_NAME_INPUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/et_last_name")',
    )

    EMAIL_INPUT = (AppiumBy.ID, "com.cubii:id/et_email")
    EMAIL_INPUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/et_email"]',
    )
    EMAIL_INPUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/et_email")',
    )

    BIRTHDAY_INPUT = (AppiumBy.ID, "com.cubii:id/et_birthday")
    BIRTHDAY_INPUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/et_birthday"]',
    )
    BIRTHDAY_INPUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/et_birthday")',
    )

    DATE_PICKER_OK_BUTTON = (AppiumBy.ID, "android:id/button1")
    DATE_PICKER_OK_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="android:id/button1"]',
    )
    DATE_PICKER_OK_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("android:id/button1")',
    )

    DATE_PICKER_PREV_MONTH_BUTTONS = (
        (AppiumBy.ACCESSIBILITY_ID, "Previous month"),
        (
            AppiumBy.XPATH,
            '//android.widget.ImageButton[contains(@content-desc,"Previous month")]',
        ),
    )
    DATE_PICKER_DAY_CELLS = (
        AppiumBy.XPATH,
        '//android.view.View[@clickable="true" and @enabled="true" '
        'and string-length(normalize-space(@text))>0 and '
        'translate(@text,"0123456789","")=""]',
    )

    GENDER_OPTIONS = ("Male", "Female", "Neutral")
    GENDER_OPTION_ID = "com.cubii:id/txtGenderEditProfiler"
    GENDER_SECTION_LABEL_XPATH = (
        AppiumBy.XPATH,
        '//*[contains(@text,"your gender") or contains(@text,"What\'s your gender")]',
    )

    PROFILE_FIRST_NAMES = (
        "James",
        "Emma",
        "Olivia",
        "Liam",
        "Sophia",
        "Noah",
        "Ava",
        "Ethan",
        "Mia",
        "Lucas",
        "Charlotte",
        "Mason",
        "Amelia",
        "Logan",
        "Harper",
    )
    PROFILE_LAST_NAMES = (
        "Smith",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Garcia",
        "Miller",
        "Davis",
        "Rodriguez",
        "Martinez",
        "Wilson",
        "Anderson",
        "Taylor",
        "Thomas",
        "Moore",
    )

    HEIGHT_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Height")')
    HEIGHT_FIELD_XPATH = (AppiumBy.XPATH, '//android.widget.TextView[@text="Height"]')

    HEIGHT_PICKERS_CONTAINER = (AppiumBy.ID, "com.cubii:id/llPickers")
    HEIGHT_PICKERS_CONTAINER_XPATH = (
        AppiumBy.XPATH,
        '//androidx.appcompat.widget.LinearLayoutCompat[@resource-id="com.cubii:id/llPickers"]',
    )
    HEIGHT_PICKERS_CONTAINER_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/llPickers")',
    )

    HEIGHT_NUMBER_PICKER_INPUT = (AppiumBy.ID, "android:id/numberpicker_input")
    HEIGHT_NUMBER_PICKERS_XPATH = (
        AppiumBy.XPATH,
        '//androidx.appcompat.widget.LinearLayoutCompat[@resource-id="com.cubii:id/llPickers"]'
        "//android.widget.NumberPicker",
    )

    HEIGHT_UNIT_CMS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("CMS")')
    HEIGHT_UNIT_CMS_XPATH = (AppiumBy.XPATH, '//android.widget.Button[@text="CMS"]')

    HEIGHT_UNIT_FT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="FT"]',
    )
    HEIGHT_UNIT_FT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("android:id/numberpicker_input").text("FT")',
    )

    PROFILE_MODAL_OK_BUTTON = (AppiumBy.ID, "com.cubii:id/btnOkay")
    PROFILE_MODAL_OK_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btnOkay"]',
    )
    PROFILE_MODAL_OK_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/btnOkay")',
    )

    HEIGHT_OK_BUTTON = PROFILE_MODAL_OK_BUTTON
    HEIGHT_OK_BUTTON_XPATH = PROFILE_MODAL_OK_BUTTON_XPATH
    HEIGHT_OK_BUTTON_UIAUTOMATOR = PROFILE_MODAL_OK_BUTTON_UIAUTOMATOR

    WEIGHT_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Weight")')
    WEIGHT_FIELD_XPATH = (AppiumBy.XPATH, '//android.widget.TextView[@text="Weight"]')

    WEIGHT_MODAL_ROOT = (AppiumBy.ID, "com.cubii:id/cl_root")
    WEIGHT_MODAL_ROOT_XPATH = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@resource-id="com.cubii:id/cl_root"]',
    )
    WEIGHT_MODAL_ROOT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/cl_root")',
    )

    WEIGHT_KG = (AppiumBy.ID, "com.cubii:id/tvKg")
    WEIGHT_KG_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.cubii:id/tvKg"]',
    )
    WEIGHT_KG_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/tvKg")',
    )

    WEIGHT_LB = (AppiumBy.ID, "com.cubii:id/flLb")
    WEIGHT_LB_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="com.cubii:id/flLb"]',
    )
    WEIGHT_LB_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/flLb")',
    )

    WEIGHT_INPUT = (AppiumBy.ID, "com.cubii:id/etWeight")
    WEIGHT_INPUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/etWeight"]',
    )
    WEIGHT_INPUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/etWeight")',
    )

    WEIGHT_UNITS = ("Kg", "LBs")

    COUNTRY_FIELD = (AppiumBy.ID, "com.cubii:id/et_country")
    COUNTRY_FIELD_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/et_country"]',
    )
    COUNTRY_FIELD_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/et_country")',
    )

    SIMPLE_LIST_RECYCLER = (AppiumBy.ID, "com.cubii:id/rvSimpleItems")
    SIMPLE_LIST_RECYCLER_XPATH = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvSimpleItems"]',
    )
    SIMPLE_LIST_RECYCLER_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/rvSimpleItems")',
    )

    SIMPLE_LIST_ITEM_IN_RECYCLER_XPATH = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.cubii:id/rvSimpleItems"]'
        "//android.widget.RelativeLayout",
    )
    SIMPLE_LIST_ITEM_CUSTOM_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/custom"]'
        "/android.widget.RelativeLayout",
    )

    COUNTRY_LIST_RECYCLER = SIMPLE_LIST_RECYCLER
    COUNTRY_LIST_RECYCLER_XPATH = SIMPLE_LIST_RECYCLER_XPATH
    COUNTRY_LIST_RECYCLER_UIAUTOMATOR = SIMPLE_LIST_RECYCLER_UIAUTOMATOR
    COUNTRY_LIST_ITEM_IN_RECYCLER_XPATH = SIMPLE_LIST_ITEM_IN_RECYCLER_XPATH
    COUNTRY_LIST_ITEM_CUSTOM_XPATH = SIMPLE_LIST_ITEM_CUSTOM_XPATH

    STATE_FIELD = (AppiumBy.ID, "com.cubii:id/et_state")
    STATE_FIELD_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/et_state"]',
    )
    STATE_FIELD_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/et_state")',
    )

    CITY_FIELD = (AppiumBy.ID, "com.cubii:id/et_city")
    CITY_FIELD_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/et_city"]',
    )
    CITY_FIELD_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/et_city")',
    )

    ZIP_CODE_INPUT = (AppiumBy.ID, "com.cubii:id/et_zip")
    ZIP_CODE_INPUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/et_zip"]',
    )
    ZIP_CODE_INPUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/et_zip")',
    )

    COMPANY_INPUT = (AppiumBy.ID, "com.cubii:id/et_company")
    COMPANY_INPUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.AutoCompleteTextView[@resource-id="com.cubii:id/et_company"]',
    )
    COMPANY_INPUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/et_company")',
    )

    SAVE_BUTTON = (AppiumBy.ID, "com.cubii:id/btn_save")
    SAVE_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btn_save"]',
    )
    SAVE_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/btn_save")',
    )

    CHANGE_PASSWORD_LINK = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Change Password")',
    )
    CHANGE_PASSWORD_LINK_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Change Password"]',
    )

    CHANGE_PASSWORD_OLD_INPUT = (AppiumBy.ID, "com.cubii:id/editText")
    CHANGE_PASSWORD_OLD_INPUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/editText"]',
    )
    CHANGE_PASSWORD_OLD_INPUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/editText")',
    )

    CHANGE_PASSWORD_NEW_INPUT = (AppiumBy.ID, "com.cubii:id/editText1")
    CHANGE_PASSWORD_NEW_INPUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/editText1"]',
    )
    CHANGE_PASSWORD_NEW_INPUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/editText1")',
    )

    CHANGE_PASSWORD_REPEAT_INPUT = (AppiumBy.ID, "com.cubii:id/editText2")
    CHANGE_PASSWORD_REPEAT_INPUT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/editText2"]',
    )
    CHANGE_PASSWORD_REPEAT_INPUT_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/editText2")',
    )

    SAVE_PASSWORD_BUTTON = (AppiumBy.ID, "com.cubii:id/btn_save_password")
    SAVE_PASSWORD_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btn_save_password"]',
    )
    SAVE_PASSWORD_BUTTON_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.cubii:id/btn_save_password")',
    )

    DEFAULT_CHANGE_PASSWORD_OLD = os.getenv("CUBII_CHANGE_PASSWORD_OLD", "123123s")
    DEFAULT_CHANGE_PASSWORD_NEW = os.getenv("CUBII_CHANGE_PASSWORD_NEW", "Neha@1999")
    DEFAULT_CHANGE_PASSWORD_WRONG_REPEAT = os.getenv(
        "CUBII_CHANGE_PASSWORD_WRONG_REPEAT", "WrongPass@123"
    )

    PASSWORD_MANAGER_CLOSE_BUTTON = (AppiumBy.ID, "android:id/closeButton")
    PASSWORD_MANAGER_CLOSE_ACCESSIBILITY = (AppiumBy.ACCESSIBILITY_ID, "Close")
    PASSWORD_MANAGER_CLOSE_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.ImageView[@content-desc="Close"]',
    )
    PASSWORD_MANAGER_CLOSE_UIAUTOMATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("android:id/closeButton")',
    )
    PASSWORD_MANAGER_CLOSE_CLICKABLE_XPATH = (
        AppiumBy.XPATH,
        '//*[@content-desc="Close" and @clickable="true"]',
    )
    PASSWORD_MANAGER_CANCEL = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Cancel")',
    )
    PASSWORD_MANAGER_CANCEL_XPATH = (AppiumBy.XPATH, '//*[@text="Cancel"]')

    PROFILE_COMPANY_NAMES = (
        "Acme Wellness",
        "Summit Health Group",
        "Blue Ridge Medical",
        "Nova Fitness Co",
        "Harbor Care Partners",
        "Pinnacle Rehab",
        "Evergreen Therapeutics",
        "Atlas Mobility",
        "BrightPath Clinics",
        "Sterling Health Systems",
    )

    def generate_edit_profile_data(self):
        first_name = random.choice(self.PROFILE_FIRST_NAMES)
        last_name = random.choice(self.PROFILE_LAST_NAMES)
        unique_suffix = random.randint(100, 999)
        email = f"{first_name.lower()}.{last_name.lower()}{unique_suffix}@yopmail.com"
        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "gender": random.choice(self.GENDER_OPTIONS),
            "zip_code": str(random.randint(10000, 99999)),
            "company": random.choice(self.PROFILE_COMPANY_NAMES),
            "change_password_old": self.DEFAULT_CHANGE_PASSWORD_OLD,
            "change_password_new": self.DEFAULT_CHANGE_PASSWORD_NEW,
            "change_password_wrong_repeat": self.DEFAULT_CHANGE_PASSWORD_WRONG_REPEAT,
        }

    def clear_first_name(self):
        self.LOGGER.info("Clearing first name on Edit Profile screen.")
        element = self._locate_first_name_input()
        self._clear_field_text(element, "first name")

    def clear_last_name(self):
        self.LOGGER.info("Clearing last name on Edit Profile screen.")
        self._clear_field_by_locators(
            "last name",
            (
                self.LAST_NAME_INPUT,
                self.LAST_NAME_INPUT_XPATH,
                self.LAST_NAME_INPUT_UIAUTOMATOR,
            ),
        )

    def clear_email(self):
        self.LOGGER.info("Clearing email on Edit Profile screen.")
        self._clear_field_by_locators(
            "email",
            (
                self.EMAIL_INPUT,
                self.EMAIL_INPUT_XPATH,
                self.EMAIL_INPUT_UIAUTOMATOR,
            ),
            hide_keyboard_after=True,
        )

    def scroll_up(self, times=2):
        self.LOGGER.info("Scrolling up on Edit Profile screen (%s swipe(s)).", times)
        for _ in range(max(1, int(times))):
            self._swipe_down()

    def verify_field_error_message(self, field_label):
        expected = self.EDIT_PROFILE_FIELD_ERROR_MESSAGES.get(field_label)
        if not expected:
            raise AssertionError(
                f"Unknown Edit Profile field for error validation: {field_label!r}"
            )

        self.LOGGER.info(
            "Verifying Edit Profile error message for %s: %r",
            field_label,
            expected,
        )
        locators = self._field_error_locators(field_label, expected)
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        last_err = None
        for by, locator, label in locators:
            try:
                element = wait.until(ec.visibility_of_element_located((by, locator)))
                observed = (element.text or element.get_attribute("text") or "").strip()
                if observed != expected:
                    raise AssertionError(
                        f"Edit Profile {field_label} error mismatch via {label}: "
                        f"expected {expected!r}, got {observed!r}."
                    )
                self.LOGGER.info(
                    "Edit Profile %s validation error verified via %s: %r",
                    field_label,
                    label,
                    observed,
                )
                return
            except (TimeoutException, AssertionError) as exc:
                last_err = exc
                continue

        raise AssertionError(
            f"Edit Profile {field_label} validation error not visible. "
            f"Expected text: {expected!r}. Last error: {last_err!r}"
        )

    def verify_change_password_field_error_message(self, field_label):
        expected = self.CHANGE_PASSWORD_FIELD_ERROR_MESSAGES.get(field_label)
        if not expected:
            raise AssertionError(
                f"Unknown Change Password field for error validation: {field_label!r}"
            )

        self.LOGGER.info(
            "Verifying Change Password error message for %s: %r",
            field_label,
            expected,
        )
        locators = self._field_error_locators(field_label, expected)
        wait = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT)
        last_err = None
        for by, locator, label in locators:
            try:
                element = wait.until(ec.visibility_of_element_located((by, locator)))
                observed = (element.text or element.get_attribute("text") or "").strip()
                if observed != expected:
                    raise AssertionError(
                        f"Change Password {field_label} error mismatch via {label}: "
                        f"expected {expected!r}, got {observed!r}."
                    )
                self.LOGGER.info(
                    "Change Password %s validation error verified via %s: %r",
                    field_label,
                    label,
                    observed,
                )
                return
            except (TimeoutException, AssertionError) as exc:
                last_err = exc
                continue

        raise AssertionError(
            f"Change Password {field_label} validation error not visible. "
            f"Expected text: {expected!r}. Last error: {last_err!r}"
        )

    def edit_first_name(self, value):
        self.LOGGER.info("Editing first name on Edit Profile screen.")
        element = self._locate_first_name_input()
        self._replace_field_text(element, value, "first name")

    def edit_last_name(self, value):
        self.LOGGER.info("Editing last name on Edit Profile screen.")
        self._enter_text_with_fallbacks(
            value,
            "last name",
            (
                self.LAST_NAME_INPUT,
                self.LAST_NAME_INPUT_XPATH,
                self.LAST_NAME_INPUT_UIAUTOMATOR,
            ),
        )

    def edit_email(self, value):
        self.LOGGER.info("Editing email on Edit Profile screen.")
        self._enter_text_with_fallbacks(
            value,
            "email",
            (
                self.EMAIL_INPUT,
                self.EMAIL_INPUT_XPATH,
                self.EMAIL_INPUT_UIAUTOMATOR,
            ),
            hide_keyboard_after=True,
        )

    def enter_invalid_email(self):
        self.LOGGER.info(
            "Entering invalid email on Edit Profile screen: %s",
            self.INVALID_EMAIL_VALUE,
        )
        self.edit_email(self.INVALID_EMAIL_VALUE)

    def select_random_birthdate_and_confirm(self):
        self.LOGGER.info("Selecting a random birthdate on Edit Profile screen.")
        self._scroll_into_view(self.BIRTHDAY_INPUT, max_swipes=6)
        self._click_with_fallbacks(
            "birthdate field",
            (
                self.BIRTHDAY_INPUT,
                self.BIRTHDAY_INPUT_XPATH,
                self.BIRTHDAY_INPUT_UIAUTOMATOR,
            ),
        )
        self._scroll_random_months_back(max_months=18)
        day_selected = self._select_random_day_cell()
        self.LOGGER.info("Random birthdate day selected: %s", day_selected)
        self._click_with_fallbacks(
            "date picker OK",
            (
                self.DATE_PICKER_OK_BUTTON,
                self.DATE_PICKER_OK_BUTTON_XPATH,
                self.DATE_PICKER_OK_BUTTON_UIAUTOMATOR,
            ),
        )

    def select_random_gender(self, gender=None):
        self.LOGGER.info("Selecting gender on Edit Profile screen.")
        time.sleep(0.4)
        self._scroll_to_gender_section()

        current = self._get_current_gender_selection()
        self.LOGGER.info("Current gender before selection: %s", current or "none")

        chosen = self._resolve_gender_to_select(gender, current)
        order = [chosen] + [option for option in self.GENDER_OPTIONS if option != chosen]

        for option in order:
            self.LOGGER.info("Attempting to select gender: %s", option)
            if self._tap_gender_option(option):
                chosen = option
                break
        else:
            raise AssertionError(
                "Unable to tap any gender option on Edit Profile screen."
            )

        if self._verify_gender_selected(chosen):
            self.LOGGER.info("Gender selected and verified: %s", chosen)
        else:
            self.LOGGER.info(
                "Gender `%s` tapped; UI selection state could not be verified via "
                "standard attributes (teal/checkmark chips). Continuing.",
                chosen,
            )
        return chosen

    def _scroll_to_gender_section(self):
        self._scroll_into_view(self.GENDER_SECTION_LABEL_XPATH, max_swipes=6)
        for locator in (
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{self.GENDER_OPTION_ID}"]',
            ),
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("{self.GENDER_OPTION_ID}")'),
        ):
            self._scroll_into_view(locator, max_swipes=2)

    def _get_current_gender_selection(self):
        for name in self.GENDER_OPTIONS:
            if self._is_gender_selected(name):
                return name
        return None

    def _resolve_gender_to_select(self, preferred, current):
        if preferred in self.GENDER_OPTIONS and preferred != current:
            return preferred

        candidates = [option for option in self.GENDER_OPTIONS if option != current]
        if not candidates:
            return random.choice(self.GENDER_OPTIONS)
        return random.choice(candidates)

    def _gender_option_locators(self, chosen):
        return (
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{self.GENDER_OPTION_ID}" '
                f'and @text="{chosen}"]/parent::android.view.ViewGroup',
            ),
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{self.GENDER_OPTION_ID}" '
                f'and @text="{chosen}"]/..',
            ),
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{self.GENDER_OPTION_ID}" '
                f'and @text="{chosen}"]',
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("{self.GENDER_OPTION_ID}").text("{chosen}")',
            ),
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{chosen}")'),
        )

    def _tap_gender_option(self, chosen):
        short_wait = WebDriverWait(self.driver, 4)
        for locator in self._gender_option_locators(chosen):
            try:
                element = short_wait.until(ec.visibility_of_element_located(locator))
                if not element.is_displayed():
                    continue
                try:
                    element.click()
                except Exception:
                    self._tap_element_center(element)
                time.sleep(0.4)
                self.LOGGER.info("Gender `%s` tapped via `%s`.", chosen, locator[1])
                return True
            except TimeoutException:
                self.LOGGER.debug(
                    "Gender element not visible for `%s` via `%s`.", chosen, locator[1]
                )
            except Exception as exc:
                self.LOGGER.debug(
                    "Gender tap failed for `%s` via `%s`: %s", chosen, locator[1], exc
                )

        try:
            label = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("{self.GENDER_OPTION_ID}").text("{chosen}")',
            )
            self._tap_element_center(label)
            time.sleep(0.4)
            self.LOGGER.info("Gender `%s` tapped via center gesture fallback.", chosen)
            return True
        except Exception as exc:
            self.LOGGER.debug("Gender center-tap fallback failed for `%s`: %s", chosen, exc)
        return False

    def _tap_element_center(self, element):
        rect = element.rect
        x = int(rect["x"] + rect["width"] / 2)
        y = int(rect["y"] + rect["height"] / 2)
        self.driver.execute_script(
            "mobile: clickGesture",
            {"x": x, "y": y},
        )

    def _is_gender_selected(self, name):
        selected_xpaths = (
            f'//android.widget.TextView[@resource-id="{self.GENDER_OPTION_ID}" '
            f'and @text="{name}" and @selected="true"]',
            f'//android.view.ViewGroup[@selected="true"][.//android.widget.TextView'
            f'[@resource-id="{self.GENDER_OPTION_ID}" and @text="{name}"]]',
            f'//android.view.ViewGroup[.//android.widget.TextView'
            f'[@resource-id="{self.GENDER_OPTION_ID}" and @text="{name}"]]'
            f'//android.widget.ImageView',
            f'//android.view.ViewGroup[.//android.widget.TextView'
            f'[@resource-id="{self.GENDER_OPTION_ID}" and @text="{name}"]]'
            f'//*[contains(@content-desc,"check") or contains(@content-desc,"selected")]',
        )
        for xpath in selected_xpaths:
            matches = self.driver.find_elements(AppiumBy.XPATH, xpath)
            if any(match.is_displayed() for match in matches):
                return True

        try:
            label = self.driver.find_element(
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{self.GENDER_OPTION_ID}" '
                f'and @text="{name}"]',
            )
            node = label
            for _ in range(4):
                for attr in ("selected", "checked", "activated", "focused"):
                    value = str(node.get_attribute(attr) or "").lower()
                    if value in {"true", "1"}:
                        return True
                try:
                    node = node.find_element(AppiumBy.XPATH, "./..")
                except Exception:
                    break
        except Exception:
            pass
        return False

    def _verify_gender_selected(self, chosen):
        deadline = time.monotonic() + 2
        while time.monotonic() < deadline:
            if self._is_gender_selected(chosen):
                return True
            time.sleep(0.2)
        return False

    def click_height_field(self):
        self.LOGGER.info("Opening Height picker on Edit Profile screen.")
        locators = (
            self.HEIGHT_FIELD_XPATH,
            self.HEIGHT_FIELD,
        )
        self._scroll_into_view(locators[0], max_swipes=4)
        self._click_with_fallbacks("Height field", locators)

    def select_random_height_and_confirm(self):
        self.LOGGER.info("Selecting a random height on Edit Profile screen.")
        pickers_container = self._locate_visible_with_fallbacks(
            "height pickers",
            (
                self.HEIGHT_PICKERS_CONTAINER,
                self.HEIGHT_PICKERS_CONTAINER_XPATH,
                self.HEIGHT_PICKERS_CONTAINER_UIAUTOMATOR,
            ),
        )
        self._randomize_height_picker(pickers_container)
        self._confirm_profile_modal("height picker")
        self.LOGGER.info("Random height selected and confirmed.")

    def click_weight_field(self):
        self.LOGGER.info("Opening Weight picker on Edit Profile screen.")
        locators = (
            self.WEIGHT_FIELD_XPATH,
            self.WEIGHT_FIELD,
        )
        self._scroll_into_view(locators[0], max_swipes=4)
        self._click_with_fallbacks("Weight field", locators)

    def select_random_weight_and_confirm(self):
        self.LOGGER.info("Selecting a random weight on Edit Profile screen.")
        self._locate_visible_with_fallbacks(
            "weight modal",
            (
                self.WEIGHT_MODAL_ROOT,
                self.WEIGHT_MODAL_ROOT_XPATH,
                self.WEIGHT_MODAL_ROOT_UIAUTOMATOR,
            ),
        )
        unit = random.choice(self.WEIGHT_UNITS)
        self._select_weight_unit(unit)
        weight_value = self._random_weight_value(unit)
        self._enter_text_with_fallbacks(
            weight_value,
            "weight",
            (
                self.WEIGHT_INPUT,
                self.WEIGHT_INPUT_XPATH,
                self.WEIGHT_INPUT_UIAUTOMATOR,
            ),
        )
        self._confirm_profile_modal("weight picker")
        self.LOGGER.info("Random weight selected: %s %s.", weight_value, unit)

    def click_country_field(self):
        self.LOGGER.info("Opening Choose Country list on Edit Profile screen.")
        locators = (
            self.COUNTRY_FIELD_XPATH,
            self.COUNTRY_FIELD,
            self.COUNTRY_FIELD_UIAUTOMATOR,
        )
        self._scroll_into_view(locators[0], max_swipes=6)
        self._click_with_fallbacks("country field", locators)

    def select_random_country(self):
        self.LOGGER.info("Selecting a random country on Edit Profile screen.")
        recycler = self._locate_simple_list_recycler("country list")
        chosen = self._tap_random_item_from_recycler(recycler, "country")
        self.LOGGER.info("Random country selected: %s.", chosen)
        return chosen

    def select_random_state_if_available(self):
        field_locators = (
            self.STATE_FIELD_XPATH,
            self.STATE_FIELD,
            self.STATE_FIELD_UIAUTOMATOR,
        )
        if not self._is_field_available(field_locators):
            self.LOGGER.info("State field not available; skipping state selection.")
            return None

        self.LOGGER.info("Selecting a random state on Edit Profile screen.")
        self._scroll_into_view(field_locators[0], max_swipes=4)
        self._click_with_fallbacks("state field", field_locators)
        recycler = self._locate_simple_list_recycler("state list")
        chosen = self._tap_random_item_from_recycler(recycler, "state")
        self.LOGGER.info("Random state selected: %s.", chosen)
        return chosen

    def select_random_city_if_available(self):
        time.sleep(0.5)
        field_locators = (
            self.CITY_FIELD_XPATH,
            self.CITY_FIELD,
            self.CITY_FIELD_UIAUTOMATOR,
        )
        if not self._is_field_available(field_locators):
            self.LOGGER.info("City field not available; skipping city selection.")
            return None

        self.LOGGER.info("Selecting a random city on Edit Profile screen.")
        self._scroll_into_view(field_locators[0], max_swipes=4)
        self._click_with_fallbacks("city field", field_locators)
        recycler = self._locate_simple_list_recycler("city list")
        chosen = self._tap_random_item_from_recycler(recycler, "city")
        self.LOGGER.info("Random city selected: %s.", chosen)
        return chosen

    def scroll_down(self, times=2):
        self.LOGGER.info("Scrolling down on Edit Profile screen (%s swipe(s)).", times)
        for _ in range(max(1, int(times))):
            self._swipe_up()

    def _field_error_locators(self, field_label, expected_message):
        common = (
            (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@resource-id="{self.TEXTINPUT_ERROR_ID}" '
                f'and @text="{expected_message}"]',
                "textinput_error (xpath)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("{self.TEXTINPUT_ERROR_ID}")'
                f'.text("{expected_message}")',
                "textinput_error (UiAutomator id+text)",
            ),
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{expected_message}")',
                "textinput_error (UiAutomator text)",
            ),
        )
        if field_label == "first name":
            return (
                (
                    AppiumBy.XPATH,
                    f'//android.widget.LinearLayout[@resource-id="{self.FIRST_NAME_TIL_ID}"]'
                    f'//android.widget.TextView[@resource-id="{self.TEXTINPUT_ERROR_ID}" '
                    f'and @text="{expected_message}"]',
                    "first name til textinput_error",
                ),
            ) + common
        return common

    def _clear_field_by_locators(self, label, locators, hide_keyboard_after=False):
        last_err = None
        for locator in locators:
            try:
                element = self.wait.until(ec.visibility_of_element_located(locator))
                self._clear_field_text(element, label, hide_keyboard_after=hide_keyboard_after)
                return
            except TimeoutException as exc:
                last_err = exc
        raise AssertionError(
            f"Unable to clear {label} on Edit Profile screen. Last error: {last_err!r}"
        )

    def enter_zip_code(self, value):
        self.LOGGER.info("Entering zip code on Edit Profile screen.")
        self._scroll_into_view(self.ZIP_CODE_INPUT_XPATH, max_swipes=4)
        self._enter_text_with_fallbacks(
            value,
            "zip code",
            (
                self.ZIP_CODE_INPUT,
                self.ZIP_CODE_INPUT_XPATH,
                self.ZIP_CODE_INPUT_UIAUTOMATOR,
            ),
            hide_keyboard_after=True,
        )

    def enter_company(self, value):
        self.LOGGER.info("Entering company on Edit Profile screen.")
        self._scroll_into_view(self.COMPANY_INPUT_XPATH, max_swipes=4)
        self._enter_text_with_fallbacks(
            value,
            "company",
            (
                self.COMPANY_INPUT,
                self.COMPANY_INPUT_XPATH,
                self.COMPANY_INPUT_UIAUTOMATOR,
            ),
            hide_keyboard_after=True,
        )

    def click_save_button(self):
        self.LOGGER.info("Saving Edit Profile changes.")
        self._scroll_into_view(self.SAVE_BUTTON_XPATH, max_swipes=4)
        self._click_with_fallbacks(
            "save button",
            (
                self.SAVE_BUTTON,
                self.SAVE_BUTTON_XPATH,
                self.SAVE_BUTTON_UIAUTOMATOR,
            ),
        )

    def click_change_password(self):
        self.LOGGER.info("Opening Change Password on Edit Profile screen.")
        locators = (
            self.CHANGE_PASSWORD_LINK_XPATH,
            self.CHANGE_PASSWORD_LINK,
        )
        self._scroll_into_view(locators[0], max_swipes=6)
        self._click_with_fallbacks("Change Password", locators)
        time.sleep(0.5)

    def enter_change_password_old(self, value):
        self.LOGGER.info("Entering old password on Change Password screen.")
        locators = (
            self.CHANGE_PASSWORD_OLD_INPUT_XPATH,
            self.CHANGE_PASSWORD_OLD_INPUT,
            self.CHANGE_PASSWORD_OLD_INPUT_UIAUTOMATOR,
        )
        last_err = None
        for locator in locators:
            try:
                self._scroll_into_view(locator, max_swipes=4)
                element = self.wait.until(ec.visibility_of_element_located(locator))
                self._scroll_into_view_element(element)
                try:
                    element.click()
                except StaleElementReferenceException:
                    self.LOGGER.info(
                        "Old password field became stale after tap; "
                        "Google Password Manager sheet likely opened."
                    )
                time.sleep(0.5)
                self._dismiss_password_manager_popup_if_present()
                element = self.wait.until(ec.visibility_of_element_located(locator))
                self._set_field_text(element, value)
                self.LOGGER.info("Old password entered.")
                return
            except (TimeoutException, StaleElementReferenceException) as exc:
                last_err = exc
                self.LOGGER.debug(
                    "Old password entry attempt failed via `%s`: %s", locator[1], exc
                )
        raise AssertionError(
            f"Unable to enter old password on Change Password screen. Last error: {last_err!r}"
        )

    def _dismiss_password_manager_popup_if_present(self):
        """Dismiss Google Password Manager sheet when it blocks the old-password field."""
        wait = WebDriverWait(self.driver, 5)
        dismiss_locators = (
            self.PASSWORD_MANAGER_CLOSE_ACCESSIBILITY,
            self.PASSWORD_MANAGER_CLOSE_BUTTON,
            self.PASSWORD_MANAGER_CLOSE_XPATH,
            self.PASSWORD_MANAGER_CLOSE_CLICKABLE_XPATH,
            self.PASSWORD_MANAGER_CLOSE_UIAUTOMATOR,
            self.PASSWORD_MANAGER_CANCEL_XPATH,
            self.PASSWORD_MANAGER_CANCEL,
        )
        for locator in dismiss_locators:
            try:
                dismiss_btn = wait.until(ec.element_to_be_clickable(locator))
                dismiss_btn.click()
                self.LOGGER.info(
                    "Google Password Manager popup dismissed via `%s`.", locator[1]
                )
                time.sleep(0.4)
                return True
            except TimeoutException:
                continue
        try:
            self.driver.press_keycode(4)
            self.LOGGER.info("Google Password Manager popup dismissed via device Back key.")
            time.sleep(0.4)
            return True
        except Exception as exc:
            self.LOGGER.debug("Back key dismiss for password manager failed: %s", exc)
        self.LOGGER.info("Google Password Manager popup not shown; continuing.")
        return False

    def enter_change_password_new(self, value):
        self._enter_text_with_fallbacks(
            value,
            "new password",
            (
                self.CHANGE_PASSWORD_NEW_INPUT,
                self.CHANGE_PASSWORD_NEW_INPUT_XPATH,
                self.CHANGE_PASSWORD_NEW_INPUT_UIAUTOMATOR,
            ),
        )

    def enter_change_password_repeat(self, value):
        self._enter_text_with_fallbacks(
            value,
            "repeat new password",
            (
                self.CHANGE_PASSWORD_REPEAT_INPUT,
                self.CHANGE_PASSWORD_REPEAT_INPUT_XPATH,
                self.CHANGE_PASSWORD_REPEAT_INPUT_UIAUTOMATOR,
            ),
            hide_keyboard_after=True,
        )

    def click_save_password_button(self):
        self.LOGGER.info("Saving Change Password.")
        self._click_with_fallbacks(
            "save password button",
            (
                self.SAVE_PASSWORD_BUTTON,
                self.SAVE_PASSWORD_BUTTON_XPATH,
                self.SAVE_PASSWORD_BUTTON_UIAUTOMATOR,
            ),
        )
        time.sleep(0.5)

    def _locate_first_name_input(self):
        locators = (
            self.FIRST_NAME_INPUT,
            self.FIRST_NAME_INPUT_XPATH,
            self.FIRST_NAME_INPUT_UIAUTOMATOR,
        )
        last_err = None
        for locator in locators:
            try:
                elements = WebDriverWait(self.driver, Settings.EXPLICIT_WAIT).until(
                    ec.visibility_of_all_elements_located(locator)
                )
                for element in elements:
                    if element.is_displayed():
                        return element
            except TimeoutException as exc:
                last_err = exc
        raise AssertionError(
            "First name field (`editText`) not visible on Edit Profile screen. "
            f"Last error: {last_err!r}"
        )

    def _enter_text_with_fallbacks(self, value, label, locators, hide_keyboard_after=False):
        last_err = None
        for locator in locators:
            try:
                element = self.wait.until(ec.visibility_of_element_located(locator))
                self._replace_field_text(
                    element, value, label, hide_keyboard_after=hide_keyboard_after
                )
                return
            except TimeoutException as exc:
                last_err = exc
        raise AssertionError(
            f"Unable to enter {label} on Edit Profile screen. Last error: {last_err!r}"
        )

    def _replace_field_text(self, element, value, label, hide_keyboard_after=False):
        self._scroll_into_view_element(element)
        self._set_field_text(element, value)
        self.LOGGER.info("%s updated to: %s", label.capitalize(), value)
        if hide_keyboard_after:
            self._hide_soft_keyboard_quietly()

    def _clear_field_text(self, element, label, hide_keyboard_after=False):
        self._scroll_into_view_element(element)
        self._set_field_text(element, "")
        self.LOGGER.info("%s cleared.", label.capitalize())
        if hide_keyboard_after:
            self._hide_soft_keyboard_quietly()

    def _set_field_text(self, element, value):
        element.click()
        try:
            element.clear()
        except Exception:
            pass
        try:
            element.set_value(value)
            return
        except Exception:
            pass
        try:
            self.driver.execute_script(
                "mobile: setText",
                {"elementId": element.id, "text": value},
            )
            return
        except Exception:
            pass
        element.send_keys(value)

    def _hide_soft_keyboard_quietly(self):
        try:
            self.driver.hide_keyboard()
        except Exception:
            try:
                self.driver.execute_script("mobile: hideKeyboard")
            except Exception:
                pass
        time.sleep(0.3)

    def _click_with_fallbacks(self, label, locators):
        last_err = None
        for locator in locators:
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Clicked %s via `%s`.", label, locator[1])
                return
            except TimeoutException as exc:
                last_err = exc
        raise AssertionError(
            f"Unable to click {label} on Edit Profile screen. Last error: {last_err!r}"
        )

    def _locate_visible_with_fallbacks(self, label, locators):
        last_err = None
        for locator in locators:
            try:
                return self.wait.until(ec.visibility_of_element_located(locator))
            except TimeoutException as exc:
                last_err = exc
        raise AssertionError(
            f"Unable to locate {label} on Edit Profile screen. Last error: {last_err!r}"
        )

    def _scroll_into_view(self, locator, max_swipes=5):
        for _ in range(max_swipes):
            if self.driver.find_elements(*locator):
                return
            self._swipe_up()
        if not self.driver.find_elements(*locator):
            raise AssertionError(f"Element not found after scrolling: {locator}")

    def _scroll_into_view_element(self, element):
        try:
            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                    "elementId": element.id,
                    "direction": "down",
                    "percent": 0.75,
                },
            )
        except Exception:
            pass

    def _scroll_random_months_back(self, max_months=18):
        steps = random.randint(0, max_months)
        if steps == 0:
            return

        self.LOGGER.info("Scrolling date picker %s month(s) backwards.", steps)
        short_wait = WebDriverWait(self.driver, 2)
        for _ in range(steps):
            clicked = False
            for locator in self.DATE_PICKER_PREV_MONTH_BUTTONS:
                try:
                    short_wait.until(ec.element_to_be_clickable(locator)).click()
                    clicked = True
                    break
                except TimeoutException:
                    continue
            if not clicked:
                self.LOGGER.info(
                    "Previous month control is not visible; continuing with current month."
                )
                break
            time.sleep(0.1)

    def _select_random_day_cell(self):
        day_cells = self.wait.until(
            ec.presence_of_all_elements_located(self.DATE_PICKER_DAY_CELLS)
        )
        valid_cells = [
            cell
            for cell in day_cells
            if (cell.text or "").strip().isdigit() and cell.is_enabled() and cell.is_displayed()
        ]
        if not valid_cells:
            raise AssertionError("No selectable day cells found in date picker.")

        target = random.choice(valid_cells)
        chosen_day = target.text.strip()
        target.click()
        return chosen_day

    def _swipe_up(self):
        size = self.driver.get_window_size()
        x = size["width"] // 2
        start_y = int(size["height"] * 0.78)
        end_y = int(size["height"] * 0.35)
        self.driver.swipe(x, start_y, x, end_y, 350)
        time.sleep(0.2)

    def _swipe_down(self):
        size = self.driver.get_window_size()
        x = size["width"] // 2
        start_y = int(size["height"] * 0.35)
        end_y = int(size["height"] * 0.78)
        self.driver.swipe(x, start_y, x, end_y, 350)
        time.sleep(0.2)

    def _randomize_height_picker(self, pickers_container):
        number_pickers = self._find_height_number_pickers(pickers_container)
        if len(number_pickers) < 2:
            raise AssertionError(
                "Expected at least two NumberPicker wheels in height picker (`llPickers`). "
                f"Found {len(number_pickers)}."
            )

        column_specs = (
            ("feet", 0, 5),
            ("inches", 1, 11),
        )
        for label, column_index, max_steps in column_specs:
            if column_index >= len(number_pickers):
                continue
            steps = random.randint(1, max_steps)
            direction = random.choice(("up", "down"))
            self._rotate_number_picker(
                number_pickers[column_index], steps, direction, label
            )

        unit = random.choice(("CMS", "FT"))
        unit_picker = number_pickers[2] if len(number_pickers) > 2 else None
        self._select_height_unit(unit, unit_picker)

    def _find_height_number_pickers(self, container):
        pickers = container.find_elements(AppiumBy.CLASS_NAME, "android.widget.NumberPicker")
        if len(pickers) >= 2:
            return pickers

        pickers = self.driver.find_elements(*self.HEIGHT_NUMBER_PICKERS_XPATH)
        if len(pickers) >= 2:
            return pickers

        inputs = container.find_elements(*self.HEIGHT_NUMBER_PICKER_INPUT)
        pickers = []
        for input_el in inputs:
            try:
                picker = input_el.find_element(
                    AppiumBy.XPATH, "./ancestor::android.widget.NumberPicker[1]"
                )
                if picker not in pickers:
                    pickers.append(picker)
            except Exception:
                continue
        return pickers

    def _get_number_picker_value(self, picker_element):
        try:
            input_el = picker_element.find_element(*self.HEIGHT_NUMBER_PICKER_INPUT)
            return (input_el.text or input_el.get_attribute("text") or "").strip()
        except Exception:
            return ""

    def _rotate_number_picker(self, picker_element, steps, direction, label):
        rect = picker_element.rect
        if rect.get("height", 0) <= 0 or rect.get("width", 0) <= 0:
            raise AssertionError(f"{label} picker has invalid bounds; cannot rotate wheel.")

        left = int(rect["x"] + (rect["width"] * 0.15))
        top = int(rect["y"] + (rect["height"] * 0.15))
        width = max(1, int(rect["width"] * 0.7))
        height = max(1, int(rect["height"] * 0.7))
        for _ in range(max(1, int(steps))):
            self.driver.execute_script(
                "mobile: swipeGesture",
                {
                    "left": left,
                    "top": top,
                    "width": width,
                    "height": height,
                    "direction": direction,
                    "percent": 0.75,
                },
            )
            time.sleep(0.2)
        self.LOGGER.info(
            "Height picker %s rotated %s step(s), direction=%s.",
            label,
            steps,
            direction,
        )

    def _select_height_unit(self, unit, unit_picker=None):
        unit = unit.upper()
        current = self._get_number_picker_value(unit_picker) if unit_picker else ""
        if current.upper() == unit:
            self.LOGGER.info("Height unit already set to %s.", unit)
            return

        if unit == "CMS":
            cms_locators = (
                self.HEIGHT_UNIT_CMS_XPATH,
                self.HEIGHT_UNIT_CMS,
                (AppiumBy.XPATH, '//*[@text="CMS"]'),
            )
            if self._try_click_locators("height unit CMS", cms_locators):
                self.LOGGER.info("Height unit selected: CMS.")
                return
            if unit_picker is not None:
                self._rotate_number_picker(unit_picker, 1, "up", "height unit")
                if self._get_number_picker_value(unit_picker).upper() == "CMS":
                    self.LOGGER.info("Height unit selected: CMS (via wheel).")
                    return

        if unit == "FT":
            ft_locators = (self.HEIGHT_UNIT_FT_XPATH, self.HEIGHT_UNIT_FT_UIAUTOMATOR)
            if self._try_click_locators("height unit FT", ft_locators):
                self.LOGGER.info("Height unit selected: FT.")
                return
            if unit_picker is not None:
                self._rotate_number_picker(unit_picker, 1, "down", "height unit")
                if self._get_number_picker_value(unit_picker).upper() == "FT":
                    self.LOGGER.info("Height unit selected: FT (via wheel).")
                    return

        raise AssertionError(f"Unable to select height unit {unit}.")

    def _try_click_locators(self, label, locators):
        for locator in locators:
            try:
                self.wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Clicked %s via `%s`.", label, locator[1])
                return True
            except TimeoutException:
                continue
        return False

    def _confirm_profile_modal(self, label):
        self._click_with_fallbacks(
            f"{label} OK",
            (
                self.PROFILE_MODAL_OK_BUTTON,
                self.PROFILE_MODAL_OK_BUTTON_XPATH,
                self.PROFILE_MODAL_OK_BUTTON_UIAUTOMATOR,
            ),
        )

    def _select_weight_unit(self, unit):
        if unit == "Kg":
            locators = (
                self.WEIGHT_KG_XPATH,
                self.WEIGHT_KG,
                self.WEIGHT_KG_UIAUTOMATOR,
            )
        else:
            locators = (
                self.WEIGHT_LB_XPATH,
                self.WEIGHT_LB,
                self.WEIGHT_LB_UIAUTOMATOR,
            )
        self._click_with_fallbacks(f"weight unit {unit}", locators)
        self.LOGGER.info("Weight unit selected: %s.", unit)

    def _random_weight_value(self, unit):
        if unit == "Kg":
            return str(random.randint(45, 120))
        return str(random.randint(100, 280))

    def _is_field_available(self, locators, timeout=3):
        short_wait = WebDriverWait(self.driver, timeout)
        for locator in locators:
            try:
                element = short_wait.until(ec.visibility_of_element_located(locator))
                if element.is_displayed() and element.is_enabled():
                    return True
            except TimeoutException:
                continue
        return False

    def _locate_simple_list_recycler(self, label):
        return self._locate_visible_with_fallbacks(
            label,
            (
                self.SIMPLE_LIST_RECYCLER,
                self.SIMPLE_LIST_RECYCLER_XPATH,
                self.SIMPLE_LIST_RECYCLER_UIAUTOMATOR,
            ),
        )

    def _tap_random_item_from_recycler(self, recycler, list_name):
        max_scrolls = 4
        candidates = []

        for scroll_idx in range(max_scrolls + 1):
            rows = recycler.find_elements(AppiumBy.XPATH, ".//android.widget.RelativeLayout")
            for row in rows:
                if not row.is_displayed():
                    continue
                item_label = self._list_row_label(row)
                if not item_label:
                    continue
                if any(existing_label == item_label for existing_label, _ in candidates):
                    continue
                candidates.append((item_label, row))

            if candidates and (scroll_idx > 0 or len(candidates) >= 3):
                break
            if scroll_idx < max_scrolls:
                self._scroll_simple_list(recycler)

        if not candidates:
            rows = self.driver.find_elements(*self.SIMPLE_LIST_ITEM_IN_RECYCLER_XPATH)
            if not rows:
                rows = self.driver.find_elements(*self.SIMPLE_LIST_ITEM_CUSTOM_XPATH)
            for row in rows:
                if not row.is_displayed():
                    continue
                item_label = self._list_row_label(row)
                if item_label:
                    candidates.append((item_label, row))

        if not candidates:
            raise AssertionError(f"No selectable rows found in Choose {list_name} list.")

        random.shuffle(candidates)
        for item_label, row in candidates:
            try:
                row.click()
                return item_label
            except Exception:
                continue

        raise AssertionError(f"Unable to tap any row in Choose {list_name} list.")

    def _list_row_label(self, row):
        texts = row.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        parts = [(element.text or "").strip() for element in texts if (element.text or "").strip()]
        return " ".join(parts)

    def _scroll_simple_list(self, recycler):
        try:
            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                    "elementId": recycler.id,
                    "direction": "down",
                    "percent": 0.65,
                },
            )
        except Exception:
            rect = recycler.rect
            if rect.get("height", 0) > 0 and rect.get("width", 0) > 0:
                self.driver.execute_script(
                    "mobile: swipeGesture",
                    {
                        "left": int(rect["x"] + rect["width"] * 0.1),
                        "top": int(rect["y"] + rect["height"] * 0.2),
                        "width": int(rect["width"] * 0.8),
                        "height": int(rect["height"] * 0.6),
                        "direction": "up",
                        "percent": 0.65,
                    },
                )
        time.sleep(0.3)
