Feature: Cubii Goals
  As a logged-in Cubii user
  I want to add a goal from the home screen
  So that I can set and track my daily fitness goals


  @goals @goals_validation 
  Scenario: Verify validation for goal input fields
    When the user scrolls down to Today's Goals on the home screen
    Then Today's Goals section should be visible on the home screen
    When the user scrolls down and taps the add goal button
    When the user taps Next on the goal introduction if present
    When the user taps Got it on the goal introduction if present
    Then the goal introduction should be dismissed if present
    When the user click on Strides
    When the user click on Calories
    When the user click on Miles
    When the user click on Time
    Then the user click on the SAVE GOALS option
    Then the user scrolls down and verifies the validation for the strides
    Then the user scrolls down and verifies the validation for the calories
    Then the user scrolls down and verifies the validation for the kms
    Then the user scrolls down and verifies the validation for the time
    When the user click on the goals back button
    Then the user verify the Save changes pop-up on the screen
    Then the user click on the no

  @goals @add_goal
  Scenario: Add a goal from home screen and complete the goal introduction
    When the user scrolls down to Today's Goals on the home screen
    Then Today's Goals section should be visible on the home screen
    When the user scrolls down and taps the add goal button
    When the user taps Next on the goal introduction if present
    When the user taps Got it on the goal introduction if present
    Then the goal introduction should be dismissed if present
    Then the user verify the goal metrics Strides Calories Miles and Time
    When the user click on Strides
    Then the user verify the details of Strides
    Then the user add the strides goals 100
    When the user click on Calories
    Then the user add the calories goals 0.1
    When the user click on Miles
    Then the user add the miles goals 0.1
    When the user click on Time
    Then the user add the time goals 1
    When the user click on Save goals


  @goals @edit_goals
  Scenario: Edit the goals
    When the user scrolls down to Today's Goals on the home screen
    Then Today's Goals section should be visible on the home screen
    When the user scrolls down and taps the edit goal button
    When the user taps Next on the goal introduction if present
    When the user taps Got it on the goal introduction if present
    Then the goal introduction should be dismissed if present
    Then the user scrolls down and edits strides goals
    Then the user scrolls down and edits the Calories
    Then the user scrolls down and edits the KMS/Miles
    Then the user scrolls down and edits the time
    Then the user click on the Done button
    Then the user verify the updated goals


  @goals @remove_goals
  Scenario: Remove the goals
    When the user scrolls down to Today's Goals on the home screen
    Then Today's Goals section should be visible on the home screen
    When the user taps Next on the goal introduction if present
    When the user taps Got it on the goal introduction if present
    Then the goal introduction should be dismissed if present
    Then the user verify the goal metrics Strides Calories Miles and Time
    When the user click on Strides
    Then the user click on the goal cancel option
    When the user click on Calories
    Then the user click on the goal cancel option
    When the user click on Miles
    Then the user click on the goal cancel option
    When the user click on Time
    Then the user click on the goal cancel option
    When the user click on the goals back button


  @goals @delete_goals
  Scenario: Delete all saved goals from the Add Goal screen
    When the user scrolls down to Today's Goals on the home screen
    Then Today's Goals section should be visible on the home screen
    When the user scrolls down and taps the edit goal button
    When the user taps Next on the goal introduction if present
    When the user taps Got it on the goal introduction if present
    Then the goal introduction should be dismissed if present
    # Then the user verify that goals are added and present
    When the user click on DELETE ALL GOALS
