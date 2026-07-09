Feature: Cubii Report a Problem
  As a logged-in Cubii user
  I want to open Report a Problem from the home settings menu
  So that I can submit feedback about issues in the app

  @report_a_problem
  Scenario: Open Report a Problem from More menu and verify form fields
    Then the user clicks on the three dot
    Then the user click on the Report a Problem
    Then the user verify the fields
    Then the user click on the cancel button
    Then the user click on the Report a Problem
    Then the user verify that SEND button display in disable mode without adding subject and Description
    Then the user click on the cancel button
    Then the user click back option of the more screen

  @report_a_problem @submit
  Scenario: Submit Report a Problem with subject and description
    Then the user clicks on the three dot
    Then the user click on the Report a Problem
    Then the user verify that SEND button display in disable mode without adding subject and Description
    Then the user add the subject and Description
    Then the user click on send button
    Then the user close the application
