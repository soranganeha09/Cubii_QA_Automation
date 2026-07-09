Feature: Setting
  As a logged-in Cubii user
  I want to open Settings from the home settings menu
  So that I can view and manage my app settings

  @setting
  Scenario: Open Settings from More menu
    Then the user clicks on the three dot
    Then the user click on the Setting

  @setting @select_style
  Scenario: Select dark style and verify theme on menu screens
    Then the user clicks on the three dot
    Then the user click on the Setting
    Then the user click on the dark mode
    Then the user click on the back button
    Then the user click on the more screen back button
    Then the user clicks on the three dot
    Then the user verify the More screen is in dark mode
    Then the user clicks on the my account
    Then the user verify the My Account screen is in dark mode
    Then the user clicks on the back button of my account
    Then the user click on the Setting
    Then the user verify the Settings screen is in dark mode
    Then the user click on the back button
    Then the user click on the more screen back button
    Then the user clicks on the three dot
    Then the user click on the Setting
    Then the user switch to light mode
    Then the user click on the back button
    Then the user clicks on the my account
    Then the user verify that My Account screen is in light mode
    Then the user clicks on the back button of my account
    Then the user click on the Setting
    Then the user verify the Settings screen is in light mode
    Then the user click on the back button
    Then the user click on the more screen back button

  @setting @distance_unit
  Scenario: Switch distance unit to KMS and verify confirmation popup
    Then the user clicks on the three dot
    Then the user click on the Setting
    Then the user click on the KMS
    Then the user verify the pop-up Miles -> KM
    Then the user click on the OK option of the pop-up
    Then the user click on the setting back button
    Then the user click on the more option back button
    Then the user verify that KMS display on the home screen
    Then the user clicks on the three dot
    Then the user click on the Setting
    Then the user click on the Miles
    Then the user verify the pop-up KM -> Miles
    Then the user click on the OK option of the pop-up
    Then the user click on the setting back button
    Then the user click on the more option back button
    Then the user verify that Miles display on the home screen
