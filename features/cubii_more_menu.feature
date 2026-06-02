Feature: Cubii More Menu
  As a logged-in Cubii user
  I want to open the More menu from the home screen
  So that I can verify all listed options are displayed

  @my_account @more_menu
  Scenario: Verify More menu profile name and all listed options
    Then the user clicks on the three dot
    Then the user verifies the More menu profile name
    Then the user verifies all the More menu options
    Then the user clicks on the back button of the more screen
