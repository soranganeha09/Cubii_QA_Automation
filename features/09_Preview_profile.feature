Feature: Cubii My Account Preview Profile
  As a logged-in Cubii user
  I want to open Preview Profile from My Account
  So that I can verify my profile details are displayed correctly

  @my_account @preview_profile
  Scenario: Open Preview Profile and verify profile details
    Then the user clicks on the three dot
    Then the user clicks on the my account
    Then the user clicks on the preview
    Then the user verifies the Preview profile screen
    Then the user verifies all the preview profile details
    Then the user clicks on the back option on preview profile
    Then the user clicks on the back button of my account
    Then the user clicks on the back button of the more screen
