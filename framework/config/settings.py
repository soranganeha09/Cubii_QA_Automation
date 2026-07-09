import os


class Settings:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
    CAPABILITIES_FILE = os.getenv(
        "CAPABILITIES_FILE",
        os.path.join(BASE_DIR, "framework", "config", "capabilities", "android_cubii.json"),
    )
    PLATFORM_NAME = os.getenv("PLATFORM_NAME", "Android")
    DEVICE_NAME = os.getenv("DEVICE_NAME", "Android Device")
    AUTOMATION_NAME = os.getenv("AUTOMATION_NAME", "UiAutomator2")
    APP_PATH = os.getenv("APP_PATH", "")
    APP_PACKAGE = os.getenv("APP_PACKAGE", "com.cubii")
    APP_ACTIVITY = os.getenv("APP_ACTIVITY", "com.cubii.ui.SplashActivity")
    NO_RESET = os.getenv("NO_RESET", "true").lower() == "true"
    AUTO_GRANT_PERMISSIONS = (
        os.getenv("AUTO_GRANT_PERMISSIONS", "true").lower() == "true"
    )
    DISABLE_WINDOW_ANIMATION = (
        os.getenv("DISABLE_WINDOW_ANIMATION", "true").lower() == "true"
    )
    IGNORE_HIDDEN_API_POLICY_ERROR = (
        os.getenv("IGNORE_HIDDEN_API_POLICY_ERROR", "true").lower() == "true"
    )
    SKIP_DEVICE_INITIALIZATION = (
        os.getenv("SKIP_DEVICE_INITIALIZATION", "true").lower() == "true"
    )
    SKIP_SERVER_INSTALLATION = (
        os.getenv("SKIP_SERVER_INSTALLATION", "true").lower() == "true"
    )
    NEW_COMMAND_TIMEOUT = int(os.getenv("NEW_COMMAND_TIMEOUT", "300"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "15"))
