Feature: Cubii email sign up
  As a new Cubii user
  I want to sign up using email with valid details
  So that I can create a new account from the mobile app

  @signup @skip_bootstrap @ui_validation
  Scenario: Sign up button is disabled when no form data is entered
    Given the user opens the Cubii application for sign up
    When the user taps Sign up with email
    Then the sign up button should be disabled
    And the user accepts terms and conditions
    Then the user clicks on the sign up button
    Then the user verifies the error message of the first name
    Then the user verifies the error message of the last name
    Then the user verifies the error message of the email
    Then the user verifies the error message of the password
    Then the user verifies the error message of the repeat password
    Then the user verifies the error message of the birthday


  @signup @skip_bootstrap
  Scenario: Successful email sign up submission with random user details
    Given the user opens the Cubii application for sign up
    When the user taps Sign up with email
    And the user enters random sign up details
    And the user selects a random birthdate and confirms it
    And the user accepts terms and conditions
    And the user clicks on the sign up button
    Then the sign up request is submitted
    And the user completes FTUE if required
    And the user is redirected to the Cubii home screen


