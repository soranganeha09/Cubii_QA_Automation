Feature: Cubii Notifications
  As an onboarded Cubii user
  I want to open in-app notifications from any tab
  So that I can view my notification list

  # Ignores empty checks when the account already has notifications.
  @notification @empty
  Scenario: Verify empty state when no notifications are available
    When the user taps the notification icon from any tab
    Then the user verifies that there are no notifications available


  @smoke @notification
  Scenario: Verify the notification
    When the user taps the notification icon from any tab
    Then the notifications screen should be displayed
    Then the user verify the clear all and back button header
    Then the user verify all the notifications


  @notification @clear_all
  Scenario: Clear all notifications and verify empty state
    When the user taps the notification icon from any tab
    Then the notifications screen should be displayed
    Then the user click on the clear all option
    Then the user verify that clear all notification pop-up open
    Then the user click on the go back option
    Then the user click on the clear all option
    Then the user click on the pop-up clear all option
    Then the user verify that the empty state is displayed


