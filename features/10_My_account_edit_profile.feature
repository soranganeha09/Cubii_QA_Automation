Feature: Cubii My Account Edit Profile
  As a logged-in Cubii user
  I want to open Edit Profile from the home settings menu
  So that I can view and update my account details

  @my_account @edit_profile
  Scenario: Open Edit Profile from home settings menu
    Then the user clicks on the three dot
    Then the user clicks on the my account
    Then the user clicks on the EDIT PROFILE
    Then the user verifies the Edit profile screen
    Then the user edits the first name
    Then the user edits the last name
    Then the user edits the email
    Then the user edits the birthdate
    Then the user selects a random gender
    Then the user clicks on the Height
    Then the user selects a random height
    Then the user clicks on the Weight
    Then the user selects a random weight
    Then the user clicks on the Country
    Then the user selects a random country
    Then the user selects a random state if available
    Then the user selects a random city if available
    Then the user scrolls down
    Then the user adds the zip code
    Then the user adds a random company name
    Then the user clicks on the save button
    Then the user clicks on the back button
    Then the user clicks on the logout option
    Then the user confirms logout from the pop-up
    Then the user logs in with the updated edit profile credentials

  @my_account @edit_profile @validation
  Scenario: Verify Edit Profile validation errors
    Then the user clicks on the three dot
    Then the user clicks on the my account
    Then the user clicks on the EDIT PROFILE
    Then the user verifies the Edit profile screen
    Then the user removes the first name
    Then the user removes the last name
    Then the user removes the email
    Then the user clicks on the save button
    Then the user scrolls up
    Then the user verifies the error message for first name
    Then the user adds the first name
    Then the user verifies the error message for last name
    Then the user adds the last name
    Then the user adds an invalid email
    Then the user scrolls down
    Then the user clicks on the save button
    Then the user scrolls up
    Then the user verifies the email error message
    Then the user adds the valid email
    Then the user clicks on Change Password
    Then the user enters the old password on change password screen
    Then the user enters the new password on change password screen
    Then the user enters the repeat new password on change password screen
    Then the user clicks on the save password button
    Then the user scrolls down
    Then the user clicks on the save button
    Then the user clicks on the back button
    Then the user clicks on the logout option
    Then the user confirms logout from the pop-up
    Then the user logs in with the updated edit profile email and new password

  @my_account @edit_profile @validation @change_password
  Scenario: Verify Change Password validation errors
    Then the user clicks on the three dot
    Then the user clicks on the my account
    Then the user clicks on the EDIT PROFILE
    Then the user verifies the Edit profile screen
    Then the user scrolls down
    Then the user clicks on Change Password
    Then the user clicks on the save password button
    Then the user verifies the error message of the old password on change password screen
    Then the user verifies the new password error message on change password screen
    Then the user verifies the repeat new password error message on change password screen
    Then the user adds the OLD password on change password screen
    Then the user adds the new password on change password screen
    Then the user adds the wrong password on change password screen
    Then the user clicks on the save password button
    Then the user verifies the error message of the Repeat New Password on change password screen
    Then the user adds the Repeat New Password on change password screen
    Then the user clicks on the save password button
