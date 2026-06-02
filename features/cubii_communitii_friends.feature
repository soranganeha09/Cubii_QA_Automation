Feature: Cubii Communitii Friends
  As an onboarded Cubii user
  I want to open the Friends segment on Communitii
  So that I can view my friends list on the community screen

  @smoke @communitii @communitii_friends
  Scenario: Open Communitii Friends tab via Communitii navigation
    When the user opens the Communitii Friends tab from any tab
    Then the Communitii Friends tab should be displayed

  @communitii @communitii_friends @invite_friends
  Scenario: Invite friends via search
    When the user opens the Communitii Friends tab from any tab
    And the user taps Invite Friends
    And the user taps the add friend search field
    And the user enters the invite friend name "Hetvee Sakariya"
    Then the invite friend add icon should be visible
    When the user taps the invite friend add icon
    And the user taps Navigate up

  @communitii @communitii_friends @friend_chat_profile
  Scenario: Open friend chat profile and verify name and status
    When the user opens the Communitii Friends tab from any tab
    When the user taps the first friend chat profile in the list
    Then the friend chat profile name and status should be displayed
    When the user taps the chat message input field
    And the user sends a random chat message
    And the user taps the Chiir motivation strides target if available
    When the user taps Navigate up

  @communitii @communitii_friends @view_info
  Scenario: View Info from friend chat
    When the user opens the Communitii Friends tab from any tab
    When the user taps the first friend chat profile in the list
    When the user taps the chat conversation options menu
    Then the View Info option should be visible in the chat menu
    When the user taps View Info from the chat options
    Then the View Info screen should display profile and action options
    When the user taps Close on the View Info screen
    When the user taps Navigate up

  @communitii @communitii_friends @view_profile
  Scenario: View Profile from friend chat View Info
    When the user opens the Communitii Friends tab from any tab
    When the user taps the first friend chat profile in the list
    When the user taps the chat conversation options menu
    Then the View Info option should be visible in the chat menu
    When the user taps View Info from the chat options
    When the user taps View Profile on the View Info screen
    Then the friend View Profile screen should show available profile sections
    When the user taps the profile back button
    When the user taps Navigate up

  @communitii @communitii_friends @unfriend_menu
  Scenario: Unfriend user from friend chat options menu
    When the user opens the Communitii Friends tab from any tab
    When the user taps the first friend chat profile in the list
    When the user taps the chat conversation options menu
    Then the View Info option should be visible in the chat menu
    When the user taps Unfriend from the chat options
    When the user taps Yes on the unfriend confirmation


  @communitii @communitii_friends @unfriend_view_info
  Scenario: Unfriend user from friend chat View Info
    When the user opens the Communitii Friends tab from any tab
    When the user taps the first friend chat profile in the list
    When the user taps the chat conversation options menu
    Then the View Info option should be visible in the chat menu
    When the user taps View Info from the chat options
    When the user taps Unfriend on the View Info screen
    When the user taps Yes on the unfriend confirmation

  @communitii @communitii_friends @report_user_menu
  Scenario: Report user from friend chat options menu
    When the user opens the Communitii Friends tab from any tab
    When the user taps the first friend chat profile in the list
    When the user taps the chat conversation options menu
    When the user taps Report from the chat options
    Then the Report button on the View Info screen should be disabled
    When the user enters the report subject and description for reporting
    When the user taps the REPORT button on the report form
    When the user taps Navigate up


  @communitii @communitii_friends @block_user_menu
  Scenario: Block and unblock user from friend chat options menu
    When the user opens the Communitii Friends tab from any tab
    When the user taps the first friend chat profile in the list
    When the user taps the chat conversation options menu
    When the user taps Block from the chat options
    When the user taps Block on the block confirmation dialog
    When the user taps Unblock on the blocked chat conversation
    When the user taps Unblock on the unblock confirmation dialog

  @communitii @communitii_friends @report_user_view_info
  Scenario: Report user from friend chat View Info
    When the user opens the Communitii Friends tab from any tab
    When the user taps the first friend chat profile in the list
    When the user taps the chat conversation options menu
    Then the View Info option should be visible in the chat menu
    When the user taps View Info from the chat options
    When the user taps Report on the View Info screen
    Then the Report button on the View Info screen should be disabled
    When the user enters the report subject and description for reporting
    When the user taps the REPORT button on the report form
    When the user taps Navigate up


  @communitii @communitii_friends @block_user_view_info
  Scenario: Block and unblock user from friend chat View Info
    When the user opens the Communitii Friends tab from any tab
    When the user taps the first friend chat profile in the list
    When the user taps the chat conversation options menu
    Then the View Info option should be visible in the chat menu
    When the user taps View Info from the chat options
    When the user taps Block on the View Info screen
    When the user taps Cancel on the block confirmation dialog
    When the user taps the chat conversation options menu
    When the user taps View Info from the chat options
    When the user taps Block on the View Info screen
    When the user confirms block in the dialog if shown
    Then the blocked chat conversation should show unblock option
    When the user taps Navigate up
    When the user opens the More menu on the toolbar
    When the user taps Blocked users in the menu
    Then the blocked user should be listed on the Blocked users screen
    When the user taps the blocked user profile on the Blocked users screen
    When the user taps the Unblock button on the Blocked users screen
    When the user taps Unblock on the unblock confirmation dialog
    When the user taps the back button

