# Validates authenticated entry (login + FTUE paths) and In Progress analytics UI.
Feature: Cubii In Progress validation and authenticated entry
  As a QA engineer
  I want the app to reach a stable Home state and validate In Progress UI
  So that login, FTUE, and Progress analytics are covered by automation

  # skip_bootstrap: run full flow in-step; avoids duplicate execute_ftue_dynamic_flow in environment.before_scenario
  @login @ftue @home @skip_bootstrap
  Scenario: Application launch with login and FTUE resolution
    When the user opens the application and completes login and FTUE as required
    Then the Home screen should be displayed

  # Locator reference — resource-id (UiAutomator: new UiSelector().resourceId("<id>"))
  # Period tabs: Day com.cubii:id/cardTabDay | Week com.cubii:id/txtTabWeek | Month com.cubii:id/txtTabMonth | Year com.cubii:id/txtTabYear
  # Categories: Lower Body com.cubii:id/txtTabLowerBody | Upper Body com.cubii:id/txtUpperBody
  # Upper Body editor + ADD SETS: com.cubii:id/llAddSets | post-save reps list: com.cubii:id/rcyUpwEntryReps
  # Date: com.cubii:id/txtTitleDateRange
  # Summary: Strides com.cubii:id/linLayoutStrides | Calories com.cubii:id/linLayoutCalories | Miles com.cubii:id/linLayoutDistance | Time com.cubii:id/linLayoutTime
  # Chart: com.cubii:id/combinedChart
  @login @ftue @home @in_progress @ui_validation @skip_bootstrap
  Scenario: In Progress screen UI validation
    Given the user has reached the Home screen with login and FTUE resolved
    When the user opens the In Progress tab
    Then the user should see the complete In Progress primary layout

  @login @ftue @home @in_progress @ui_validation @period_tabs @skip_bootstrap
  Scenario: Progress period tabs Day Week Month Year display date range and metric data
    Given the user has reached the Home screen with login and FTUE resolved
    When the user opens the In Progress tab
    And the user navigates each Progress period tab and verifies data for Day Week Month and Year

  # Activity log cnsLayoutActivityLogRoot → drill Week→Day, Month→Week, Year→Month; strides txtMetricsValue1
  @login @ftue @home @in_progress @ui_validation @activity_log_drill @skip_bootstrap
  Scenario: Progress activity log row drills down with matching strides
    Given the user has reached the Home screen with login and FTUE resolved
    When the user opens the In Progress tab
    When the user verifies Progress activity log drill-down stride parity across Week Month and Year

  # Next imgNext com.cubii:id/imgNext | Previous imgPrevious com.cubii:id/imgPrevious (any Day/Week/Month/Year active)
  @login @ftue @home @in_progress @ui_validation @date_navigation @skip_bootstrap
  Scenario: Progress date Next inactive and Previous shows prior period with metrics
    Given the user has reached the Home screen with login and FTUE resolved
    When the user opens the In Progress tab
    Then the Cubii Progress Next date control should be disabled at the latest period
    When the user opens the prior Progress period with the date arrow and validates metrics

  # + ADD SETS: com.cubii:id/llAddSets — third set row; post-save popup rcyUpwEntryReps may need scroll
  @login @ftue @home @in_progress @ui_validation @upper_body @upper_body_three_sets @workout_entry @skip_bootstrap
  Scenario: Upper Body workout with + ADD SETS confirms all sets in scrollable popup
    Given the user has reached the Home screen with login and FTUE resolved
    When the user opens the In Progress tab
    And the user clicks on the Upper Body workout tab
    When the user adds an Upper Body workout with rows 1 to 3 reps 10 10 12 using plus-minus entry
    Then the Upper Body workout entry popup should confirm rows 1 through 3 reps 10 10 12 with scroll
    And the user dismisses the Upper Body workout entry popup

  @login @ftue @home @in_progress @ui_validation @upper_body @workout_entry @skip_bootstrap
  Scenario Outline: Upper Body workout set entry supports plus minus and manual reps
    Given the user has reached the Home screen with login and FTUE resolved
    When the user opens the In Progress tab
    And the user clicks on the Upper Body workout tab
    And the user adds an Upper Body workout set with row 1 reps <row1_reps> and row 2 reps <row2_reps> using <input_mode> entry
    Then the Upper Body workout entry popup should confirm row 1 reps <row1_reps> and row 2 reps <row2_reps>
    And the user dismisses the Upper Body workout entry popup
    #And the new Upper Body workout entry should be persisted with row 1 reps <row1_reps> and row 2 reps <row2_reps>

    Examples:
      | input_mode | row1_reps | row2_reps |
      | plus-minus | 10        | 10        |
      | manual     | 8         | 12        |
