Feature: Cubii login
  As an existing Cubii user
  I want to sign in with valid credentials
  So that I can access the app home screen

  @smoke @login
  Scenario: Successful Login
    Given the Cubii application is launched
    And the Cubii login screen is visible
    When the user enters valid email and password
    And the user taps the SIGN IN button
    Then the user should be successfully logged in
    When the user taps the three dots menu
    And the user taps Logout from the menu
    And the user confirms Logout
    Then the user is signed out and the login screen is visible

  @google_login @authentication
  Scenario: Login with Google account and logout
    Given the Cubii application is launched
    And the Cubii login screen is visible
    When the user taps Continue with Google
    Then the Agree and Login popup is displayed
    When the user taps Agree and Login
    Then the Choose an account popup is displayed
    When the user selects an available Google account
    Then the user is redirected to the Cubii home screen
    When the user taps the three dots menu
    And the user taps Logout from the menu
    And the user confirms Logout
    Then the user is signed out and the login screen is visible

  @facebook_login @authentication
  Scenario: Login with Facebook account
    Given the Cubii application is launched
    And the Cubii login screen is visible
    When the user taps Continue with Facebook
    Then the Agree and Login popup is displayed
    When the user taps Agree and Login
    And the user enters valid Facebook credentials
    And the user submits the Facebook login form
    Then the user is redirected to the Cubii home screen
    When the user taps the three dots menu
    And the user taps Logout from the menu
    And the user confirms Logout
    Then the user is signed out and the login screen is visible
