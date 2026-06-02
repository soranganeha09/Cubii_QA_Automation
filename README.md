# Cubii Mobile BDD Automation Framework

Scalable Appium + Python framework using Gherkin/BDD with Behave.

## Project Structure

```text
Cubii_QA_Automation/
├── behave.ini
├── pytest.ini
├── requirements.txt
├── framework/
│   ├── config/
│   │   ├── settings.py
│   │   └── capabilities/
│   │       └── android_cubii.json
│   ├── core/
│   │   └── driver_manager.py
│   └── pages/
│       ├── base_page.py
│       ├── home_page.py
│       └── login_page.py
├── features/
│   ├── environment.py
│   ├── cubii_login.feature
│   ├── cubii_onboarding.feature
│   └── steps/
│       ├── onboarding_steps.py
│       └── login_steps.py
├── scripts/
│   └── run_features_sequential.sh
└── tests/
    └── test_bdd_runner.py
```

## Run Setup

1. Install dependencies:
   - `pip install -r requirements.txt`
   - `npm install` (installs Allure CLI locally in `node_modules/` — no `sudo` or global npm needed)
2. Start Appium server (with chromedriver autodownload enabled for WebView handling):
   - `appium --allow-insecure chromedriver_autodownload`
3. (Optional) Override capabilities file path:
   - `export CAPABILITIES_FILE=/absolute/path/to/capabilities.json`
4. Configure app/device environment variables (only if you need to override file/default values), for example:
   - `export APPIUM_SERVER_URL=http://127.0.0.1:4723`
   - `export PLATFORM_NAME=Android`
   - `export DEVICE_NAME="Android Device"`
   - `export APP_PATH=/absolute/path/to/cubii.apk`
5. Run BDD tests:
   - Report generation and browser open are enabled by default for every run (pass or fail):
     - JUnit XML reports in `reports/`
     - Allure results in `allure-results/`
     - Allure HTML report in `reports/allure-html/` (auto-generated after run)
     - Report opens automatically in your default browser when the run finishes
   - Run full test suite (all feature files in one session): `behave`
   - Run a single feature file: `behave features/cubii_login.feature`
   - Run all feature files one by one (separate session per file): `./scripts/run_features_sequential.sh`
   - Run scenarios by single tag: `behave --tags=@smoke`
   - Run a specific tag from a specific feature file: `behave features/cubii_login.feature --tags=@smoke`
   - Run scenarios by multiple tags (OR): `behave --tags=@smoke,@regression`
   - Run scenarios by multiple tags (AND): `behave --tags=@smoke --tags=@android`
   - Exclude tag(s): `behave --tags=~@wip`
6. Allure CLI (required for HTML report + auto-open):
   - Preferred: `npm install` in this repo (uses `node_modules/.bin/allure`)
   - Optional global install (needs admin): `sudo npm install -g allure-commandline`
   - Fallback: `npx --yes allure-commandline` if neither local nor global CLI exists
   - Manual open: `./node_modules/.bin/allure serve allure-results` or `allure open reports/allure-html`
   - Disable auto HTML generation: `export CUBII_AUTO_REPORT=0`
   - Disable auto-open in browser: `export CUBII_AUTO_OPEN_REPORT=0`

## Run Feature Files One by One

Use this when you want each `.feature` file to run in its own Behave session (fresh Appium driver and login/FTUE bootstrap per file). This differs from `behave`, which runs every feature in a single session and reuses bootstrap state across scenarios.

### Automated (recommended)

From the repo root (with Appium running):

```bash
./scripts/run_features_sequential.sh
```

The script:

- Runs each file in a fixed order (see `FEATURE_FILES` in `scripts/run_features_sequential.sh`)
- Stops on the first failure (set `CONTINUE_ON_FAIL=1` to run all files even when some fail)
- Disables per-run browser popups and HTML generation during the loop (`CUBII_AUTO_OPEN_REPORT=0`, `CUBII_AUTO_REPORT=0`)
- Generates one combined Allure HTML report at the end in `reports/allure-html/`

### Manual (single feature at a time)

```bash
behave features/cubii_login.feature
behave features/cubii_onboarding.feature
behave features/cubii_ftue_dynamic_wellness.feature
behave features/cubii_non_ble_connection.feature
behave features/cubii_in_progress_validation.feature
behave features/cubii_community.feature
behave features/cubii_communitii_friends.feature
behave features/cubii_wellness_journii.feature
behave features/cubii_studio.feature
behave features/cubii_notification.feature
# BLE disabled: rename cubii_ble_connection.feature.disabled → .feature to re-enable
# behave features/cubii_ble_connection.feature
```

Add tags when needed, e.g. `behave features/cubii_login.feature --tags=@smoke`.

### Shell loop (without the script)

```bash
export CUBII_AUTO_OPEN_REPORT=0
export CUBII_AUTO_REPORT=0

for f in \
  features/cubii_login.feature \
  features/cubii_ftue_dynamic_wellness.feature \
  features/cubii_non_ble_connection.feature \
  features/cubii_in_progress_validation.feature \
  features/cubii_community.feature \
  features/cubii_communitii_friends.feature \
  features/cubii_wellness_journii.feature \
  features/cubii_studio.feature \
  features/cubii_notification.feature
do
  echo "========== Running $f =========="
  behave "$f" || exit 1
done

./node_modules/.bin/allure generate allure-results --clean -o reports/allure-html
```

| Approach | Driver sessions | Bootstrap | Reports |
|----------|-----------------|-----------|---------|
| `behave` | One | Reused across scenarios | One report at end |
| One-by-one | One per feature file | Reset each file | Combined HTML after loop (script) |

## Framework Conventions

- Keep locators and UI actions inside POM classes under `framework/pages/`.
- Keep step definitions thin; call page methods instead of raw driver actions.
- Reuse `BasePage` wait/actions to avoid duplicated utility code.
- Add one feature file per behavior domain (onboarding, login, workout, profile, etc.).
- Use tags (`@smoke`, `@regression`, `@ios`, `@android`) to control execution scope.