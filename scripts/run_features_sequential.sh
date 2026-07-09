#!/usr/bin/env bash
# Run each feature file in features/ as its own Behave session (one driver/bootstrap per file).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Avoid opening the browser or regenerating HTML after every feature file.
export CUBII_AUTO_OPEN_REPORT="${CUBII_AUTO_OPEN_REPORT:-0}"
export CUBII_AUTO_REPORT="${CUBII_AUTO_REPORT:-0}"

# Set to 1 to keep running after a feature file fails (default: stop on first failure).
CONTINUE_ON_FAIL="${CONTINUE_ON_FAIL:-0}"

if [[ -x "$ROOT/.venv/bin/behave" ]]; then
  BEHAVE="$ROOT/.venv/bin/behave"
elif command -v behave >/dev/null 2>&1; then
  BEHAVE="behave"
else
  echo "error: behave not found. Run: pip install -r requirements.txt" >&2
  exit 1
fi

ALLURE="$ROOT/node_modules/.bin/allure"
FAILED=()
PASSED=0

# ---------------------------------------------------------------------------
# Report management — always start with a clean slate
# ---------------------------------------------------------------------------
ARCHIVE_DIR="$ROOT/reports/archive"
KEEP_ARCHIVES="${KEEP_ARCHIVES:-10}"   # how many past reports to retain

# 1. Archive the previous HTML report before it gets overwritten.
if [[ -d "$ROOT/reports/allure-html" ]]; then
  TIMESTAMP=$(date '+%Y-%m-%d_%H-%M-%S')
  mkdir -p "$ARCHIVE_DIR"
  mv "$ROOT/reports/allure-html" "$ARCHIVE_DIR/allure-html_$TIMESTAMP"
  echo "Archived previous report → reports/archive/allure-html_$TIMESTAMP"
fi

# 2. Prune archives older than the most recent KEEP_ARCHIVES entries.
if [[ -d "$ARCHIVE_DIR" ]]; then
  mapfile -t OLD_ARCHIVES < <(ls -t "$ARCHIVE_DIR" 2>/dev/null | tail -n +$((KEEP_ARCHIVES + 1)))
  for old in "${OLD_ARCHIVES[@]}"; do
    rm -rf "$ARCHIVE_DIR/$old"
    echo "Removed old archive: reports/archive/$old"
  done
fi

# 3. Wipe raw Allure results so this run's report contains only current data.
echo "Clearing allure-results/ for a fresh run..."
rm -rf "$ROOT/allure-results"
mkdir -p "$ROOT/allure-results"
# ---------------------------------------------------------------------------

# Explicit run order (not alphabetical). BLE is disabled via .feature.disabled suffix.
FEATURE_FILES=(
  cubii_login.feature
  cubii_onboarding.feature
  cubii_ftue_dynamic_wellness.feature
  cubii_non_ble_connection.feature
  cubii_in_progress_validation.feature
  cubii_community.feature
  cubii_communitii_friends.feature
  cubii_wellness_journii.feature
  cubii_studio.feature
  cubii_notification.feature
)

echo "Running feature files one by one from: $ROOT/features/"
echo "Behave: $BEHAVE"
echo "Stop on failure: $([[ "$CONTINUE_ON_FAIL" == 1 ]] && echo no || echo yes)"
echo

for name in "${FEATURE_FILES[@]}"; do
  f="$ROOT/features/$name"
  [[ -f "$f" ]] || continue
  rel="features/$name"
  echo "========== Running $rel =========="
  if "$BEHAVE" "$rel"; then
    PASSED=$((PASSED + 1))
  else
    FAILED+=("$rel")
    if [[ "$CONTINUE_ON_FAIL" != 1 ]]; then
      echo "Stopped: $rel failed." >&2
      break
    fi
  fi
  echo
done

# Generate one combined Allure HTML report at the end (if CLI is available).
if [[ -x "$ALLURE" ]] && [[ -d "$ROOT/allure-results" ]]; then
  mkdir -p "$ROOT/reports"
  echo "Generating combined Allure HTML report..."
  "$ALLURE" generate "$ROOT/allure-results" --clean -o "$ROOT/reports/allure-html"
  echo "Report: $ROOT/reports/allure-html/index.html"
fi

echo
echo "Summary: $PASSED feature file(s) passed, ${#FAILED[@]} failed."
if ((${#FAILED[@]} > 0)); then
  printf '  Failed:\n'
  printf '    - %s\n' "${FAILED[@]}"
  exit 1
fi
