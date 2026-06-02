import logging
import os

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.config.settings import Settings
from framework.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGGER = logging.getLogger("cubii_login_page")

    EMAIL = "neha01@yopmail.com"
    PASSWORD = "123123s"

    EDIT_TEXT_COMMON = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="com.cubii:id/editText"]',
    )
    EMAIL_FIELD_FALLBACK = (
        AppiumBy.XPATH,
        '//android.widget.EditText[contains(@text,"Email") or contains(@hint,"Email")]',
    )
    PASSWORD_FIELD_FALLBACK = (
        AppiumBy.XPATH,
        '//android.widget.EditText[contains(@text,"Password") or contains(@hint,"Password")]',
    )
    SIGN_IN_BUTTON = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@resource-id="com.cubii:id/cnsLayoutSignIn"]',
    )
    SIGN_IN_BUTTON_FALLBACK = (
        AppiumBy.XPATH,
        '//*[@text="SIGN IN" and (self::android.widget.TextView or self::android.widget.Button)]',
    )
    POST_LOGIN_INDICATOR = (
        AppiumBy.XPATH,
        os.getenv(
            "CUBII_POST_LOGIN_XPATH",
            '//*[@resource-id="com.cubii:id/homeRoot" or @content-desc="home_screen"]',
        ),
    )

    GOOGLE_LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login with Google")
    GOOGLE_LOGIN_BUTTON_ID = (AppiumBy.ID, "com.cubii:id/fabGoogle")
    GOOGLE_LOGIN_BUTTON_FALLBACK = (
        AppiumBy.XPATH,
        '//com.google.android.material.floatingactionbutton.FloatingActionButton'
        '[@content-desc="Login with Google"]',
    )

    AGREE_LOGIN_BUTTON = (AppiumBy.ID, "com.cubii:id/btn_agree")
    AGREE_LOGIN_BUTTON_FALLBACK = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="com.cubii:id/btn_agree"]',
    )

    CHOOSE_ACCOUNT_POPUP = (
        AppiumBy.XPATH,
        '//*[contains(@text,"Choose an account") '
        'or contains(@content-desc,"Choose an account")]',
    )
    CHOOSE_ACCOUNT_POPUP_FALLBACK = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(6)',
    )

    GOOGLE_ACCOUNT_ROW = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(1)',
    )
    GOOGLE_ACCOUNT_ROW_FALLBACK = (
        AppiumBy.XPATH,
        '(//android.widget.Button)[2]',
    )
    GOOGLE_ACCOUNT_BY_EMAIL_TEMPLATE = 'new UiSelector().textContains("{email}")'

    FACEBOOK_LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login with Facebook")
    FACEBOOK_LOGIN_BUTTON_ID = (AppiumBy.ID, "com.cubii:id/fabFacebook")
    FACEBOOK_LOGIN_BUTTON_FALLBACK = (
        AppiumBy.XPATH,
        '//com.google.android.material.floatingactionbutton.FloatingActionButton'
        '[@content-desc="Login with Facebook"]',
    )

    FACEBOOK_EMAIL_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(32)',
    )
    FACEBOOK_EMAIL_FIELD_FALLBACK = (
        AppiumBy.XPATH,
        '//android.view.View[@resource-id="root_0_0_Ki"]/android.view.View'
        '/android.view.View/android.view.View[3]/android.view.View/android.view.View'
        '/android.view.View/android.view.View/android.view.View/android.view.View'
        '/android.view.View/android.view.View/android.view.View/android.view.View[3]'
        '/android.view.View[1]/android.view.View/android.view.View/android.view.View',
    )

    FACEBOOK_PASSWORD_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(40)',
    )
    FACEBOOK_PASSWORD_FIELD_FALLBACK = (
        AppiumBy.XPATH,
        '//android.view.View[@resource-id="root_0_0_Ki"]/android.view.View'
        '/android.view.View/android.view.View[3]/android.view.View/android.view.View'
        '/android.view.View/android.view.View/android.view.View/android.view.View'
        '/android.view.View/android.view.View/android.view.View/android.view.View[3]'
        '/android.view.View[2]/android.view.View/android.view.View/android.view.View',
    )

    # Pre-authorized Facebook session: "Continue as …" (resource id is dynamic).
    FACEBOOK_CONTINUE_AS_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("u_0_0_8P")',
    )
    FACEBOOK_CONTINUE_AS_BUTTON_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[@resource-id="u_0_0_8P"]',
    )
    # Must match the blue CTA ("Continue as …"), not footer copy ("By continuing…").
    FACEBOOK_CONTINUE_AS_BUTTON_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Continue as").className("android.widget.Button")',
    )
    FACEBOOK_CONTINUE_AS_BUTTON_TEXT_XPATH = (
        AppiumBy.XPATH,
        '//android.widget.Button[contains(@text,"Continue as")]',
    )
    FACEBOOK_CONTINUE_AS_CLICKABLE_XPATH = (
        AppiumBy.XPATH,
        '//*[@clickable="true" and contains(@text,"Continue as")]',
    )
    FACEBOOK_CONTINUE_PROMPT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Would you like to continue")',
    )

    # Facebook "Log in" button labels per locale. Whichever the device
    # currently renders is matched. Add more entries to support more languages.
    FACEBOOK_SUBMIT_BUTTON_LABELS = (
        "Log in",         # en
        "લૉગ ઇન કરો",   # gu
    )

    FACEBOOK_EMAIL = os.getenv("CUBII_FB_EMAIL", "cubiilworkout@gmail.com")
    FACEBOOK_PASSWORD = os.getenv("CUBII_FB_PASSWORD", "Aubie@99")

    def launch_application(self):
        self.LOGGER.info("Launching Cubii application explicitly for login scenario.")
        if Settings.APP_PACKAGE and Settings.APP_ACTIVITY:
            try:
                # `component` satisfies drivers that otherwise raise "No intent supplied" for startActivity.
                self.driver.execute_script(
                    "mobile: startActivity",
                    {
                        "appPackage": Settings.APP_PACKAGE,
                        "appActivity": Settings.APP_ACTIVITY,
                        "component": f"{Settings.APP_PACKAGE}/{Settings.APP_ACTIVITY}",
                    },
                )
                self.LOGGER.info(
                    "Started app using mobile:startActivity `%s/%s`.",
                    Settings.APP_PACKAGE,
                    Settings.APP_ACTIVITY,
                )
                return
            except WebDriverException as exc:
                self.LOGGER.warning(
                    "mobile:startActivity failed, falling back to activate_app. Error: %s",
                    exc,
                )

        if Settings.APP_PACKAGE:
            try:
                self.driver.terminate_app(Settings.APP_PACKAGE)
                self.LOGGER.info("Terminated app package `%s` before relaunch.", Settings.APP_PACKAGE)
            except WebDriverException:
                self.LOGGER.info(
                    "App package `%s` was not running before relaunch; continuing.",
                    Settings.APP_PACKAGE,
                )

            self.driver.activate_app(Settings.APP_PACKAGE)
            self.LOGGER.info("Activated app package `%s`.", Settings.APP_PACKAGE)
            return

        self.LOGGER.info("No app package/activity configured; relying on existing app session.")

    def wait_for_login_screen(self):
        self.LOGGER.info("Waiting for login screen to be visible.")
        self._get_sign_in_button()
        self._get_email_field()
        self._get_password_field()
        self.LOGGER.info("Login screen is visible.")

    def enter_email(self, email):
        self.LOGGER.info("Entering email into login form.")
        email_field = self._get_email_field()
        email_field.clear()
        email_field.send_keys(email)
        self.LOGGER.info("Email entered.")

    def enter_password(self, password):
        self.LOGGER.info("Entering password into login form.")
        password_field = self._get_password_field()
        password_field.clear()
        password_field.send_keys(password)
        self.LOGGER.info("Password entered.")

    def tap_sign_in(self):
        self.LOGGER.info("Tapping SIGN IN button.")
        sign_in_button = self._get_sign_in_button(clickable=True)
        sign_in_button.click()
        self.LOGGER.info("SIGN IN tapped.")

    def login_with_credentials(self, email, password):
        self.LOGGER.info("Logging in with email `%s`.", email)
        self.wait_for_login_screen()
        self.enter_email(email)
        self.enter_password(password)
        self.tap_sign_in()

    def is_logged_in(self):
        self.LOGGER.info("Verifying successful login using post-login indicator.")
        try:
            self.wait.until(ec.visibility_of_element_located(self.POST_LOGIN_INDICATOR))
            self.LOGGER.info("Post-login indicator is visible.")
            return True
        except TimeoutException:
            self.LOGGER.warning(
                "Post-login indicator not found using `%s`. Falling back to SIGN IN disappearing check.",
                self.POST_LOGIN_INDICATOR[1],
            )
            self.wait.until_not(ec.presence_of_element_located(self.SIGN_IN_BUTTON))
            self.LOGGER.info("SIGN IN is no longer visible. Login considered successful.")
            return True

    def _get_email_field(self):
        fields = self.driver.find_elements(*self.EDIT_TEXT_COMMON)
        if len(fields) >= 2:
            self.LOGGER.info("Using duplicate EditText locator index 1 for email.")
            return self.get_visible_element_by_index(self.EDIT_TEXT_COMMON, 1, "login input field")

        self.LOGGER.info("Falling back to Email hint/text locator.")
        return self.wait.until(ec.visibility_of_element_located(self.EMAIL_FIELD_FALLBACK))

    def _get_password_field(self):
        fields = self.driver.find_elements(*self.EDIT_TEXT_COMMON)
        if len(fields) >= 2:
            self.LOGGER.info("Using duplicate EditText locator index 2 for password.")
            return self.get_visible_element_by_index(self.EDIT_TEXT_COMMON, 2, "login input field")

        self.LOGGER.info("Falling back to Password hint/text locator.")
        return self.wait.until(ec.visibility_of_element_located(self.PASSWORD_FIELD_FALLBACK))

    def _get_sign_in_button(self, clickable=False):
        condition = ec.element_to_be_clickable if clickable else ec.visibility_of_element_located
        short_wait = WebDriverWait(self.driver, 4)
        try:
            return short_wait.until(condition(self.SIGN_IN_BUTTON))
        except TimeoutException:
            self.LOGGER.info("Primary SIGN IN locator failed; trying text-based fallback locator.")
            return self.wait.until(condition(self.SIGN_IN_BUTTON_FALLBACK))

    def tap_continue_with_google(self):
        self.LOGGER.info("Tapping 'Login with Google' FAB.")
        short_wait = WebDriverWait(self.driver, 6)
        for locator in (
            self.GOOGLE_LOGIN_BUTTON,
            self.GOOGLE_LOGIN_BUTTON_ID,
        ):
            try:
                short_wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Google FAB tapped using locator `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Google FAB not found via `%s`; trying next locator.", locator[1]
                )

        self.LOGGER.info("Falling back to XPath for Google FAB.")
        self.wait.until(
            ec.element_to_be_clickable(self.GOOGLE_LOGIN_BUTTON_FALLBACK)
        ).click()
        self.LOGGER.info("Google FAB tapped via XPath fallback.")

    def is_agree_login_popup_visible(self):
        self.LOGGER.info("Waiting for 'Agree and Login' popup to appear.")
        try:
            self.wait.until(ec.visibility_of_element_located(self.AGREE_LOGIN_BUTTON))
            self.LOGGER.info("'Agree and Login' popup is visible.")
            return True
        except TimeoutException:
            try:
                self.wait.until(
                    ec.visibility_of_element_located(self.AGREE_LOGIN_BUTTON_FALLBACK)
                )
                self.LOGGER.info("'Agree and Login' popup visible via fallback locator.")
                return True
            except TimeoutException:
                self.LOGGER.warning("'Agree and Login' popup did not appear.")
                return False

    def tap_agree_and_login(self):
        self.LOGGER.info("Tapping AGREE AND LOGIN button.")
        try:
            btn = self.wait.until(ec.element_to_be_clickable(self.AGREE_LOGIN_BUTTON))
        except TimeoutException:
            self.LOGGER.info("Primary btn_agree locator failed; trying XPath fallback.")
            btn = self.wait.until(
                ec.element_to_be_clickable(self.AGREE_LOGIN_BUTTON_FALLBACK)
            )
        btn.click()
        self.LOGGER.info("AGREE AND LOGIN tapped.")

    def is_choose_account_popup_visible(self):
        self.LOGGER.info("Waiting for Google 'Choose an account' chooser.")
        try:
            self.wait.until(ec.visibility_of_element_located(self.CHOOSE_ACCOUNT_POPUP))
            self.LOGGER.info("Google chooser detected via text locator.")
            return True
        except TimeoutException:
            try:
                self.wait.until(
                    ec.visibility_of_element_located(self.CHOOSE_ACCOUNT_POPUP_FALLBACK)
                )
                self.LOGGER.info("Google chooser detected via UiSelector fallback.")
                return True
            except TimeoutException:
                self.LOGGER.warning("Google account chooser did not appear.")
                return False

    def select_google_account(self, email=None):
        """
        Select an account from the Google chooser.

        If `email` (or env var `CUBII_GOOGLE_EMAIL`) is provided, taps the row whose
        text contains that email. Otherwise taps the first selectable account
        (the second `android.widget.Button`, per chooser layout).
        """
        target_email = email or os.getenv("CUBII_GOOGLE_EMAIL")
        self.LOGGER.info(
            "Selecting Google account (target=%s).", target_email or "<first available>"
        )

        if target_email:
            email_locator = (
                AppiumBy.ANDROID_UIAUTOMATOR,
                self.GOOGLE_ACCOUNT_BY_EMAIL_TEMPLATE.format(email=target_email),
            )
            try:
                self.wait.until(ec.element_to_be_clickable(email_locator)).click()
                self.LOGGER.info("Selected account by email match `%s`.", target_email)
                return
            except TimeoutException:
                self.LOGGER.warning(
                    "Email-based account locator failed for `%s`; falling back to first account.",
                    target_email,
                )

        try:
            self.wait.until(ec.element_to_be_clickable(self.GOOGLE_ACCOUNT_ROW)).click()
            self.LOGGER.info("Selected first available account via UiSelector.")
        except TimeoutException:
            self.LOGGER.info(
                "Primary account locator failed; trying XPath fallback for first account."
            )
            self.wait.until(
                ec.element_to_be_clickable(self.GOOGLE_ACCOUNT_ROW_FALLBACK)
            ).click()
            self.LOGGER.info("Selected first available account via XPath fallback.")

    def tap_continue_with_facebook(self):
        self.LOGGER.info("Tapping 'Login with Facebook' FAB.")
        short_wait = WebDriverWait(self.driver, 6)
        for locator in (
            self.FACEBOOK_LOGIN_BUTTON,
            self.FACEBOOK_LOGIN_BUTTON_ID,
        ):
            try:
                short_wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Facebook FAB tapped using locator `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Facebook FAB not found via `%s`; trying next locator.", locator[1]
                )

        self.LOGGER.info("Falling back to XPath for Facebook FAB.")
        self.wait.until(
            ec.element_to_be_clickable(self.FACEBOOK_LOGIN_BUTTON_FALLBACK)
        ).click()
        self.LOGGER.info("Facebook FAB tapped via XPath fallback.")

    def _type_into_view(self, view_element, text):
        """
        Type text into a non-EditText View (Facebook WebView). Focuses the field
        by tapping it, then uses `mobile: type` against the active field.
        Falls back to send_keys if `mobile: type` is unavailable.
        """
        view_element.click()
        try:
            self.driver.execute_script("mobile: type", {"text": text})
            return
        except WebDriverException as exc:
            self.LOGGER.info(
                "`mobile: type` failed (%s); falling back to send_keys.", exc
            )
        view_element.send_keys(text)

    def _find_facebook_continue_as_button(self):
        """Return the visible 'Continue as …' CTA, avoiding footer 'By continuing…' text."""
        resource_id_locators = {
            self.FACEBOOK_CONTINUE_AS_BUTTON[1],
            self.FACEBOOK_CONTINUE_AS_BUTTON_XPATH[1],
        }
        candidates = []
        for locator in (
            self.FACEBOOK_CONTINUE_AS_BUTTON,
            self.FACEBOOK_CONTINUE_AS_BUTTON_XPATH,
            self.FACEBOOK_CONTINUE_AS_BUTTON_TEXT,
            self.FACEBOOK_CONTINUE_AS_BUTTON_TEXT_XPATH,
            self.FACEBOOK_CONTINUE_AS_CLICKABLE_XPATH,
        ):
            try:
                elements = self.driver.find_elements(*locator)
            except WebDriverException:
                continue
            for element in elements:
                if not element.is_displayed() or not element.is_enabled():
                    continue
                label = (element.text or element.get_attribute("content-desc") or "").strip()
                if locator[1] in resource_id_locators or "continue as" in label.lower():
                    candidates.append((element, locator[1], label))

        if not candidates:
            return None

        # Prefer the primary blue button (usually the only Button with that label).
        for element, locator_name, label in candidates:
            if "button" in (element.tag_name or "").lower():
                self.LOGGER.info(
                    "Facebook continue-as candidate via `%s` (text=`%s`).",
                    locator_name,
                    label,
                )
                return element

        element, locator_name, label = candidates[0]
        self.LOGGER.info(
            "Facebook continue-as candidate via `%s` (text=`%s`).",
            locator_name,
            label,
        )
        return element

    def _wait_facebook_continue_screen_dismissed(self, timeout=None):
        """Confirm OAuth left the 'Would you like to continue?' Facebook screen."""
        wait_sec = timeout or int(os.getenv("CUBII_FB_OAUTH_WAIT_SEC", "25"))
        oauth_wait = WebDriverWait(self.driver, wait_sec)
        try:
            oauth_wait.until(ec.invisibility_of_element_located(self.FACEBOOK_CONTINUE_PROMPT))
            self.LOGGER.info("Facebook continue prompt dismissed.")
            return True
        except TimeoutException:
            pass

        try:
            oauth_wait.until(
                ec.visibility_of_element_located(self.POST_LOGIN_INDICATOR)
            )
            self.LOGGER.info("Cubii home indicator visible after Facebook continue.")
            return True
        except TimeoutException:
            self.LOGGER.warning(
                "Facebook continue screen still visible after tap (waited %ss).",
                wait_sec,
            )
            return False

    def _try_tap_facebook_continue_as(self, timeout=None):
        """
        Tap Facebook 'Continue as …' when a saved session exists on the device.
        Returns True if that path was used (credential form should be skipped).
        """
        wait_sec = timeout or int(os.getenv("CUBII_FB_CONTINUE_PROBE_SEC", "8"))
        probe_wait = WebDriverWait(self.driver, wait_sec)
        try:
            probe_wait.until(
                ec.presence_of_element_located(self.FACEBOOK_CONTINUE_PROMPT)
            )
        except TimeoutException:
            self.LOGGER.info(
                "Facebook 'Would you like to continue' prompt not shown; using credential form."
            )
            return False

        button = self._find_facebook_continue_as_button()
        if button is None:
            self.LOGGER.warning(
                "Facebook continue prompt is visible but no 'Continue as' button was found."
            )
            return False

        button.click()
        self.LOGGER.info("Facebook 'Continue as' button tapped.")
        if self._wait_facebook_continue_screen_dismissed():
            return True

        self.LOGGER.warning(
            "Facebook continue tap did not dismiss OAuth screen; credential form may be required."
        )
        return False

    def enter_facebook_credentials(self, email=None, password=None):
        self._facebook_skipped_credential_form = False

        if self._try_tap_facebook_continue_as():
            self._facebook_skipped_credential_form = True
            return

        target_email = email or self.FACEBOOK_EMAIL
        target_password = password or self.FACEBOOK_PASSWORD
        self.LOGGER.info("Entering Facebook credentials in webview surface.")

        try:
            email_field = self.wait.until(
                ec.element_to_be_clickable(self.FACEBOOK_EMAIL_FIELD)
            )
        except TimeoutException:
            self.LOGGER.info(
                "Facebook email primary locator failed; using XPath fallback."
            )
            email_field = self.wait.until(
                ec.element_to_be_clickable(self.FACEBOOK_EMAIL_FIELD_FALLBACK)
            )
        self._type_into_view(email_field, target_email)

        try:
            password_field = self.wait.until(
                ec.element_to_be_clickable(self.FACEBOOK_PASSWORD_FIELD)
            )
        except TimeoutException:
            self.LOGGER.info(
                "Facebook password primary locator failed; using XPath fallback."
            )
            password_field = self.wait.until(
                ec.element_to_be_clickable(self.FACEBOOK_PASSWORD_FIELD_FALLBACK)
            )
        self._type_into_view(password_field, target_password)
        self.LOGGER.info("Facebook credentials entered.")

    def submit_facebook_login(self):
        if getattr(self, "_facebook_skipped_credential_form", False):
            self.LOGGER.info(
                "Skipping Facebook 'Log in' submit; Continue-as path was already used."
            )
            return

        self.LOGGER.info(
            "Submitting Facebook login form (locale labels: %s).",
            ", ".join(f"`{lbl}`" for lbl in self.FACEBOOK_SUBMIT_BUTTON_LABELS),
        )
        short_wait = WebDriverWait(self.driver, 4)

        candidates = []
        for label in self.FACEBOOK_SUBMIT_BUTTON_LABELS:
            candidates.extend(
                [
                    (AppiumBy.ACCESSIBILITY_ID, label),
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiSelector().description("{label}")',
                    ),
                    (
                        AppiumBy.XPATH,
                        f'//android.widget.Button[@content-desc="{label}"]',
                    ),
                ]
            )

        last_locator = candidates[-1]
        for locator in candidates[:-1]:
            try:
                short_wait.until(ec.element_to_be_clickable(locator)).click()
                self.LOGGER.info("Facebook 'Log in' tapped via `%s`.", locator[1])
                return
            except TimeoutException:
                self.LOGGER.info(
                    "Facebook submit locator `%s` failed; trying next.", locator[1]
                )

        self.LOGGER.info(
            "Falling back to long-wait XPath for `%s`.", last_locator[1]
        )
        self.wait.until(ec.element_to_be_clickable(last_locator)).click()
        self.LOGGER.info("Facebook 'Log in' tapped via final fallback `%s`.", last_locator[1])
