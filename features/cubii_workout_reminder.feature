Feature: Cubii Workout Reminder
  As a logged-in Cubii user
  I want to open Workout Reminder from the home settings menu
  So that I can view and manage my workout reminder settings

  @workout_reminder
  Scenario: Open Workout Reminder from More menu
    Then the user clicks on the three dot
    Then the user clicks on the Workout Reminder
    Then the user handles the Set Reminder Permission pop-up if present
    Then the user verifies the Workout Reminder screen
    Then the user verifies the No Workout Reminder empty state if no reminder is set

