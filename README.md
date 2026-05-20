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
   - Run full test suite (all feature files): `behave`
   - Run a single feature file: `behave features/cubii_login.feature`
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

## Framework Conventions

- Keep locators and UI actions inside POM classes under `framework/pages/`.
- Keep step definitions thin; call page methods instead of raw driver actions.
- Reuse `BasePage` wait/actions to avoid duplicated utility code.
- Add one feature file per behavior domain (onboarding, login, workout, profile, etc.).
- Use tags (`@smoke`, `@regression`, `@ios`, `@android`) to control execution scope.