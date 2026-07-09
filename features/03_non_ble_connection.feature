# Feature file: validates Non-BLE device setup from Android Home tab
Feature: Cubii Non-BLE end-to-end connection from Home tab
  # User story: stakeholder role for this behaviour
  As a Cubii user
  # User story: capability the user expects from the flow
  I want to connect a Non-Bluetooth Cubii device
  # User story: outcome used to judge success on Home
  So that I can validate connectivity and device card details on Home

  # Execution tags: quick smoke; logical non_ble group; exercised from Home
  @smoke @non_ble @home
  # Scenario headline shown in behave / Allure reports
  Scenario: Execute Non-BLE connection flow with conditional app state handling
    # Precondition step: resolves login vs FTUE and confirms Home CTAs
    Given the app is launched and user is resolved to home for Non-BLE flow
    # Action step: invokes NonBleConnectionPage end-to-end method
    When the user completes the end-to-end Cubii Non-BLE connection flow
    # Acceptance: Add Workout = imgNonBleBanner | imageView35; device card; Change device
    Then the Non-BLE Cubii device should be saved and visible on Home

  @non_ble @manual_workout
  Scenario: Add Manual Workout for Current Date (Non-BLE)
   # Given the app is launched and user is resolved to home for Non-BLE flow
    When the user opens Add Manual Workout from Home ensuring Non-BLE connectivity
    Then the Add Manual Workout screen should show title and manual entry fields
    When the user selects Start Date as current date and confirms
    And the user selects Start Time as a past time and confirms
    And the user selects Duration and submits
    And the user enters valid Strides value
    And the user sets a valid Resistance level
    And the user taps Save on Add Manual Workout
    Then if time validation is shown it should say either "You cannot enter data for future time" or "This time is overlapping another workout entry."
    And the user selects Start Time as a random past time and confirms
    And the user taps Save on Add Manual Workout
    Then the manual workout form should be saved without validation errors
    And the manual workout confirmation pop-up should display saved workout details

  @non_ble @manual_workout @manual_workout_from_progress
  Scenario: Add manual workout from Progress tab (Non-BLE)
    Given the app is launched and user is resolved to home for Non-BLE flow
    When the user opens Add Manual Workout from Home ensuring Non-BLE connectivity
    And the user opens In Progress tab
    And the user clicks on the Add Manual Workout button
    When the user selects Start Time as a past time and confirms
    And the user selects Duration and submits
    And the user enters valid Strides value
    And the user sets a valid Resistance level
    And the user taps Save on Add Manual Workout
    Then the manual workout form should be saved without validation errors
    And the manual workout confirmation pop-up should display saved workout details

  @non_ble @manual_workout @manual_workout_yesterday
  Scenario: Add Manual Workout with yesterday start date (Non-BLE)
   # Given the app is launched and user is resolved to home for Non-BLE flow
    When the user opens Add Manual Workout from Home ensuring Non-BLE connectivity
    Then the Add Manual Workout screen should show title and manual entry fields
    When the user selects Start Date as yesterday and confirms
    And the user selects Start Time as a past time and confirms
    And the user enters valid Strides value
    And the user sets a valid Resistance level
    And the user taps Save on Add Manual Workout
    Then the manual workout form should be saved without validation errors
    And the manual workout confirmation pop-up should display saved workout details

  @non_ble @manual_workout @manual_workout_random_past_time
  Scenario: Add Manual Workout with Random Past Start Time (Non-BLE)
    #Given the app is launched and user is resolved to home for Non-BLE flow
    When the user opens Add Manual Workout from Home ensuring Non-BLE connectivity
    Then the Add Manual Workout screen should show title and manual entry fields
    When the user selects Start Date as current date and confirms
    And the user selects Start Time as a random past time and confirms
    And the user selects Duration and submits
    And the user enters valid Strides value
    And the user sets a valid Resistance level
    And the user taps Save on Add Manual Workout
    Then if time validation is shown it should say either "You cannot enter data for future time" or "This time is overlapping another workout entry."
    And the user selects Start Time as a random past time and confirms
    And the user taps Save on Add Manual Workout
    And the manual workout confirmation pop-up should display saved workout details
    And the user opens In Progress tab
    Then the manually added workout should be visible in In Progress
    And the user refreshes the page
    And the user clicks on the Home tab


  @non_ble @manual_workout @strides_validation
  Scenario: Strides validation for the add workout screen
    #Given the app is launched and user is resolved to home for Non-BLE flow
    When the user opens Add Manual Workout from Home ensuring Non-BLE connectivity
    Then the Add Manual Workout screen should show title and manual entry fields
    And the user taps Save on Add Manual Workout and save button should be in disable 
    And the user enters 0 Strides value
    And the user taps Save on Add Manual Workout and save button should be in disable
    And the user clicks on the Home tab

  @non_ble @manual_workout @strides_validation @strides_max_for_duration
  Scenario: Strides cannot exceed 14000 for duration of one hour (Non-BLE)
    When the user opens Add Manual Workout from Home ensuring Non-BLE connectivity
    Then the Add Manual Workout screen should show title and manual entry fields
    When the user selects Start Date as current date and confirms
    And the user selects Start Time as a random past time and confirms
    And the user selects Duration and submits
    And the user enters strides value 15000
    And the user sets a valid Resistance level
    And the user taps Save on Add Manual Workout
    Then the strides validation error should be "Cannot exceed 14000 for duration of 1hr."
    When the user enters valid Strides value
    And the user taps Save on Add Manual Workout
    Then if time validation is shown it should say either "You cannot enter data for future time" or "This time is overlapping another workout entry."
    And the user selects Start Time as a random past time and confirms
    And the user taps Save on Add Manual Workout
    And the manual workout confirmation pop-up should display saved workout details



  @non_ble @manual_workout @edit_manual_workout
  Scenario: Edit manual workout from In Progress (Non-BLE)
    #Given the app is launched and user is resolved to home for Non-BLE flow
    When the user opens Add Manual Workout from Home ensuring Non-BLE connectivity
    And the user opens In Progress tab
    When the user opens the first manual workout entry for editing
    Then the Edit Workout screen should be displayed
    When the user selects Start Time as a past time and confirms
    And the user selects Duration and submits
    And the user enters valid Strides value
    And the user sets a valid Resistance level
    And the user taps Save on Add Manual Workout
    Then if time validation is shown it should say either "You cannot enter data for future time" or "This time is overlapping another workout entry."
    And the user selects Start Time as a random past time and confirms
    And the user taps Save on Add Manual Workout
    Then the manual workout form should be saved without validation errors
    #And the manual workout confirmation pop-up should display saved workout details
    #When the user opens In Progress tab
    Then the edited manual workout should be visible in In Progress with expected details

