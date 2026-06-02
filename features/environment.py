import logging
import os
import shutil
import subprocess
import webbrowser
from pathlib import Path

from framework.core.driver_manager import DriverManager
from framework.pages.edit_profile_page import EditProfilePage
from framework.pages.preview_profile_page import PreviewProfilePage
from framework.pages.ftue_page import FTUEPage
from framework.pages.home_page import HomePage
from framework.pages.in_progress_page import InProgressPage
from framework.pages.login_page import LoginPage
from framework.pages.signup_page import SignupPage
from framework.pages.communitii_page import CommunitiiPage
from framework.pages.cubii_studio_page import CubiiStudioPage
from framework.pages.non_ble_connection import NonBleConnectionPage
from framework.pages.wellness_journii_page import WellnessJourniiPage
from framework.pages.notification_page import NotificationPage
from framework.pages.upper_body_workout_page import UpperBodyWorkoutPage
from framework.pages.workout_reminder_page import WorkoutReminderPage

LOGGER = logging.getLogger("cubii_environment")

# By default, all scenarios get onboarded-user bootstrap.
# Add any of these tags to skip automatic login+FTUE bootstrap for a scenario.
BOOTSTRAP_SKIP_TAGS = {
    "skip_bootstrap",
    "no_bootstrap",
    "raw_ftue",
    "google_login",
    "facebook_login",
}

# Module-level flag: persist bootstrap state across Behave scenarios in one run.
_BOOTSTRAP_COMPLETED = False


def reset_bootstrap_state(context=None) -> None:
    """Reset bootstrap so the next scenario runs login+FTUE again."""
    global _BOOTSTRAP_COMPLETED
    _BOOTSTRAP_COMPLETED = False
    if context is not None:
        context.bootstrap_completed = False


def _bootstrap_already_done(context) -> bool:
    global _BOOTSTRAP_COMPLETED
    return _BOOTSTRAP_COMPLETED or getattr(context, "bootstrap_completed", False)


def _mark_bootstrap_completed(context) -> None:
    global _BOOTSTRAP_COMPLETED
    _BOOTSTRAP_COMPLETED = True
    context.bootstrap_completed = True


def before_all(context):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    LOGGER.info("Starting BDD test run and creating driver.")
    context.driver = DriverManager.create_driver()
    context.home_page = HomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.signup_page = SignupPage(context.driver)
    context.edit_profile_page = EditProfilePage(context.driver)
    context.preview_profile_page = PreviewProfilePage(context.driver)
    context.ftue_page = FTUEPage(context.driver)
    context.non_ble_connection_page = NonBleConnectionPage(context.driver)
    context.communitii_page = CommunitiiPage(context.driver, context.non_ble_connection_page)
    context.cubii_studio_page = CubiiStudioPage(
        context.driver, context.non_ble_connection_page
    )
    context.wellness_journii_page = WellnessJourniiPage(
        context.driver, context.non_ble_connection_page
    )
    context.notification_page = NotificationPage(
        context.driver, context.non_ble_connection_page
    )
    context.in_progress_page = InProgressPage(context.driver)
    context.upper_body_workout_page = UpperBodyWorkoutPage(context.driver)
    context.workout_reminder_page = WorkoutReminderPage(context.driver)
    reset_bootstrap_state(context)


def after_all(context):
    try:
        if getattr(context, "driver", None):
            LOGGER.info("Closing driver after BDD run.")
            context.driver.quit()
    finally:
        # Always generate/open the report, even when scenarios failed.
        _generate_reports_after_run()


def before_scenario(context, scenario):
    scenario_tags = set(getattr(scenario, "effective_tags", []) or [])
    if scenario_tags.intersection(BOOTSTRAP_SKIP_TAGS):
        LOGGER.info(
            "Skipping automatic login+FTUE bootstrap for `%s` due to skip tag(s): %s",
            scenario.name,
            sorted(scenario_tags.intersection(BOOTSTRAP_SKIP_TAGS)),
        )
        return

    if _bootstrap_already_done(context):
        LOGGER.info(
            "Bootstrap already completed earlier in this run. Reusing app state for `%s`.",
            scenario.name,
        )
        return

    notification_page = getattr(context, "notification_page", None)
    if notification_page is not None:
        try:
            if notification_page.is_on_notifications_screen():
                LOGGER.info(
                    "Already on notifications screen; skipping login+FTUE bootstrap "
                    "for `%s`.",
                    scenario.name,
                )
                _mark_bootstrap_completed(context)
                return
        except Exception as exc:
            LOGGER.debug(
                "Notifications screen check before bootstrap failed: %s", exc
            )

    LOGGER.info(
        "Running automatic login+FTUE bootstrap before scenario `%s`.",
        scenario.name,
    )
    context.ftue_page.execute_ftue_dynamic_flow()
    _mark_bootstrap_completed(context)
    LOGGER.info("Automatic login+FTUE bootstrap completed.")


def _project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _allure_command_prefix():
    """Return argv prefix for Allure CLI (project-local, PATH, or npx)."""
    local_allure = _project_root() / "node_modules" / ".bin" / "allure"
    if local_allure.is_file():
        return [str(local_allure)]

    allure_bin = shutil.which("allure")
    if allure_bin:
        return [allure_bin]

    npx_bin = shutil.which("npx")
    if npx_bin:
        return [npx_bin, "--yes", "allure-commandline"]
    return None


def _open_report_in_browser(allure_cmd, allure_html_dir, allure_results_dir):
    """Open the Allure report in the default browser (pass or fail)."""
    if os.getenv("CUBII_AUTO_OPEN_REPORT", "1") == "0":
        LOGGER.info("Auto-open report disabled via CUBII_AUTO_OPEN_REPORT=0.")
        return

    index_html = Path(allure_html_dir) / "index.html"
    if index_html.is_file():
        if allure_cmd:
            try:
                subprocess.Popen(
                    [*allure_cmd, "open", allure_html_dir],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    start_new_session=True,
                )
                LOGGER.info("Opening Allure HTML report in browser.")
                return
            except OSError as exc:
                LOGGER.warning("Could not run `allure open`: %s", exc)

        report_url = index_html.resolve().as_uri()
        if webbrowser.open(report_url):
            LOGGER.info("Opened Allure HTML report in browser: %s", report_url)
        else:
            LOGGER.warning("Could not open browser for report at %s", report_url)
        return

    if allure_cmd and os.path.isdir(allure_results_dir):
        try:
            subprocess.Popen(
                [*allure_cmd, "serve", allure_results_dir],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
            LOGGER.info(
                "Opening live Allure report from `%s` in browser (`allure serve`).",
                allure_results_dir,
            )
        except OSError as exc:
            LOGGER.warning("Could not run `allure serve`: %s", exc)


def _generate_reports_after_run():
    """
    Auto-generate a browsable Allure HTML report after each Behave run and
    open it in the default browser (whether scenarios passed or failed).
    JUnit XML (`reports/`) and raw Allure results (`allure-results/`) are
    already produced by behave.ini.
    """
    if os.getenv("CUBII_AUTO_REPORT", "1") == "0":
        LOGGER.info("Auto-report generation disabled via CUBII_AUTO_REPORT=0.")
        return

    allure_results_dir = "allure-results"
    allure_html_dir = "reports/allure-html"

    if not os.path.isdir(allure_results_dir):
        LOGGER.info(
            "Skipping Allure HTML generation: `%s` directory not found.",
            allure_results_dir,
        )
        return

    allure_cmd = _allure_command_prefix()
    if not allure_cmd:
        LOGGER.warning(
            "Allure CLI not found (install: npm install -g allure-commandline). "
            "Raw results are in `%s`.",
            allure_results_dir,
        )
        return

    os.makedirs("reports", exist_ok=True)
    cmd = [*allure_cmd, "generate", allure_results_dir, "--clean", "-o", allure_html_dir]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        LOGGER.info("Allure HTML report generated at `%s`.", allure_html_dir)
    except subprocess.CalledProcessError as exc:
        LOGGER.warning(
            "Allure HTML generation failed (exit=%s). stderr: %s",
            exc.returncode,
            (exc.stderr or "").strip(),
        )

    _open_report_in_browser(allure_cmd, allure_html_dir, allure_results_dir)
