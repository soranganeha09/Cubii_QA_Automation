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
    Then the user click on the ADD REMINDER button
    Then the user verify the Add Reminder screen
    Then the user set the reminder time for the workout
    Then the user click on the SAVE button
    Then the user verify the reminder
    Then the user click on the back option
    Then the user click on the more back option

  @workout_reminder @reminder_name
  Scenario: Set Workout Reminder with name from More menu
    Then the user clicks on the three dot
    Then the user clicks on the Workout Reminder
    Then the user handles the Set Reminder Permission pop-up if present
    Then the user verifies the Workout Reminder screen
    Then the user verifies the No Workout Reminder empty state if no reminder is set
    Then the user click on the ADD REMINDER button
    Then the user verify the Add Reminder screen
    Then the user set the reminder time for the workout
    Then the user set the reminder name
    Then the user click on the SAVE button
    Then the user verify the reminder
    Then the user click on the back option
    Then the user click on the more back option

  @workout_reminder @reminder_notification
  Scenario: Verify Workout Reminder notification is received
    Then the user clicks on the three dot
    Then the user clicks on the Workout Reminder
    Then the user handles the Set Reminder Permission pop-up if present
    Then the user verifies the Workout Reminder screen
    Then the user verifies the No Workout Reminder empty state if no reminder is set
    Then the user click on the ADD REMINDER button
    Then the user verify the Add Reminder screen
    Then the user sets the reminder for 1 minute ahead of the current time
    Then the user click on the SAVE button
    Then the user waits for the scheduled workout reminder notification
    Then the user verifies the workout reminder notification is displayed
    Then the user click on the notification
    Then the user click on the back option
    Then the user click on the more back option

  @workout_reminder @edit_reminder
  Scenario: Edit Workout Reminder from More menu
    Then the user clicks on the three dot
    Then the user clicks on the Workout Reminder
    Then the user handles the Set Reminder Permission pop-up if present
    Then the user verifies the Workout Reminder screen
    Then the user click on the reminder
    Then the user edit the reminder time and select all the days and add the name
    Then the user click on the SAVE button
    Then the user verify the reminder
    Then the user click on the back option
    Then the user click on the more back option

  @workout_reminder @off_reminder
  Scenario: Toggle off Workout Reminder from More menu
    Then the user clicks on the three dot
    Then the user clicks on the Workout Reminder
    Then the user handles the Set Reminder Permission pop-up if present
    Then the user verifies the Workout Reminder screen
    Then the user toggle off the reminder
    Then the user click on the back option
    Then the user click on the more back option

  @workout_reminder @remove_reminder
  Scenario: Remove Workout Reminder from More menu
    Then the user clicks on the three dot
    Then the user clicks on the Workout Reminder
    Then the user handles the Set Reminder Permission pop-up if present
    Then the user verifies the Workout Reminder screen
    Then the user click on remove option
    Then the user select the reminder
    Then click on the remove option
    Then the user click on the back option
    Then the user click on the more back option

  @workout_reminder @cancel_reminder
  Scenario: Cancel Workout Reminder screen from More menu
    Then the user clicks on the three dot
    Then the user clicks on the Workout Reminder
    Then the user handles the Set Reminder Permission pop-up if present
    Then the user verifies the Workout Reminder screen
    Then the user click on the Workout Reminder cancel button
    Then the user click on the back option
    Then the user click on the more back option

