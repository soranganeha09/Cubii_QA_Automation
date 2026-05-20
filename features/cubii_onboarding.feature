Feature: Cubii onboarding
  As a new Cubii user
  I want to start onboarding from the home screen
  So that I can begin using the app quickly

  @smoke @onboarding
  Scenario: Launch app and open onboarding
    Given the user is on the Cubii home screen
    When the user taps the Get Started button
    Then the onboarding screen is displayed
