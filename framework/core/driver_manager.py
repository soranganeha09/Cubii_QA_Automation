import json
import os

from appium import webdriver
from appium.options.common import AppiumOptions

from framework.config.settings import Settings


class DriverManager:
    @staticmethod
    def _load_capabilities_file():
        if not Settings.CAPABILITIES_FILE or not os.path.exists(Settings.CAPABILITIES_FILE):
            return {}

        with open(Settings.CAPABILITIES_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}

    @staticmethod
    def create_driver():
        capabilities = DriverManager._load_capabilities_file()
        capabilities.update(
            {
            "platformName": Settings.PLATFORM_NAME,
            "appium:automationName": Settings.AUTOMATION_NAME,
            "appium:deviceName": Settings.DEVICE_NAME,
            "appium:noReset": Settings.NO_RESET,
            "appium:newCommandTimeout": Settings.NEW_COMMAND_TIMEOUT,
            "appium:autoGrantPermissions": Settings.AUTO_GRANT_PERMISSIONS,
            "appium:disableWindowAnimation": Settings.DISABLE_WINDOW_ANIMATION,
            "appium:ignoreHiddenApiPolicyError": Settings.IGNORE_HIDDEN_API_POLICY_ERROR,
            "appium:skipDeviceInitialization": Settings.SKIP_DEVICE_INITIALIZATION,
            "appium:skipServerInstallation": Settings.SKIP_SERVER_INSTALLATION,
            }
        )

        if Settings.APP_PATH:
            capabilities["appium:app"] = Settings.APP_PATH
        if Settings.APP_PACKAGE:
            capabilities["appium:appPackage"] = Settings.APP_PACKAGE
        if Settings.APP_ACTIVITY:
            capabilities["appium:appActivity"] = Settings.APP_ACTIVITY

        options = AppiumOptions()
        options.load_capabilities(capabilities)

        return webdriver.Remote(
            command_executor=Settings.APPIUM_SERVER_URL,
            options=options,
        )
