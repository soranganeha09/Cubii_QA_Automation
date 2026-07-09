Feature: Cubii Communitii
  As an onboarded Cubii user
  I want to open the Communitii tab after login and FTUE
  So that the Community main screen and its controls are reachable

  @smoke @community
  Scenario: Open Communitii tab and verify main screen
    When the user opens the Communitii tab
    Then the Community main screen should show Groups, Friends, Explore Groups, My Groups, and Create Group

  @community @explore_groups @join_group
  Scenario: Join a group from the Explore Groups list
    When the user opens the Communitii tab
    Then the Community main screen should show Groups, Friends, Explore Groups, My Groups, and Create Group
    When the user taps the Explore Groups banner and waits for the explore list
    When the user taps the first visible join group plus icon on the explore list
    When the user taps the toolbar back control
    When the user taps the Explore Groups screen back button

  @community @joined_groups @group_self_you
  Scenario: Joined group member list shows current user as You
    When the user opens the Communitii tab
    Then the Community main screen should show Groups, Friends, Explore Groups, My Groups, and Create Group
   # When the user taps the Groups segment on the community main screen
    When the user taps a random visible joined group card
    Then the group details screen should show name member summary visibility and member list
    Then the group member list should show the current user labeled You
    When the user taps Navigate up


  @community @explore_groups
  Scenario: Explore Groups banner opens list and user opens a group
    When the user opens the Communitii tab
    Then the Community main screen should show Groups, Friends, Explore Groups, My Groups, and Create Group
    When the user taps the Explore Groups banner and waits for the explore list
    When the user opens a random Explore group card
    Then the group details screen should show name member summary visibility and member list
    When the user scrolls the group member list down and back up
    When the user taps any visible group member list card
    Then the user details sheet should show card name View Profile Report Block and Add Friend
    When the user taps the cancel button on the user details sheet
    When the user taps Navigate up
    When the user taps the toolbar back control
    When the user taps the Explore Groups screen back button

  @community @explore_groups @add_friend
  Scenario: Add Friend from member user details sheet
    When the user opens the Communitii tab
    Then the Community main screen should show Groups, Friends, Explore Groups, My Groups, and Create Group
    When the user taps the Explore Groups banner and waits for the explore list
    When the user opens a random Explore group card
    Then the group details screen should show name member summary visibility and member list
    When the user scrolls the group member list down and back up
    When the user taps any visible group member list card
    Then the user details sheet should show card name View Profile Report Block and Add Friend
    When the user taps the Add Friend button on the user details sheet
    When the user taps Navigate up
    When the user taps the toolbar back control
    When the user taps the Explore Groups screen back button

  @community @explore_groups @block_user
  Scenario: Block user from member profile and open Blocked users list
    When the user opens the Communitii tab
    Then the Community main screen should show Groups, Friends, Explore Groups, My Groups, and Create Group
    When the user taps the Explore Groups banner and waits for the explore list
    When the user opens a random Explore group card
    Then the group details screen should show name member summary visibility and member list
    When the user scrolls the group member list down and back up
    When the user taps any visible group member list card
    Then the user details sheet should show card name View Profile Report Block and Add Friend
    When the user taps Block on the user details sheet
    When the user confirms block in the dialog if shown
    When the user taps Navigate up
    When the user taps the toolbar back control
    When the user taps the Explore Groups screen back button
    When the user opens the More menu on the toolbar
    When the user taps Blocked users in the menu
    Then the Blocked users screen should show the users list
    When the user taps unblock on the blocked user at list position 1
    When the user taps Cancel on the unblock confirmation dialog
    When the user taps unblock on the blocked user at list position 1
    When the user taps Unblock on the unblock confirmation dialog
    When the user taps the back button

  @community @explore_groups @report_user
  Scenario: Report user from member user details sheet
    When the user opens the Communitii tab
    Then the Community main screen should show Groups, Friends, Explore Groups, My Groups, and Create Group
    When the user taps the Explore Groups banner and waits for the explore list
    When the user opens a random Explore group card
    Then the group details screen should show name member summary visibility and member list
    When the user scrolls the group member list down and back up
    When the user taps any visible group member list card
    Then the user details sheet should show card name View Profile Report Block and Add Friend
    When the user taps the Report button on the user details sheet
    Then the Report button on the user details sheet should be disabled
    # When the user taps the Report button on the user details sheet
    When the user enters the report subject and description for reporting
    When the user taps the REPORT button on the report form
    When the user taps Navigate up
    When the user taps the toolbar back control
    When the user taps the Explore Groups screen back button

  @community @explore_groups @view_profile
  Scenario: View Profile from group member opens profile with image name and badges
    When the user opens the Communitii tab
    Then the Community main screen should show Groups, Friends, Explore Groups, My Groups, and Create Group
    When the user taps the Explore Groups banner and waits for the explore list
    When the user opens a random Explore group card
    Then the group details screen should show name member summary visibility and member list
    When the user scrolls the group member list down and back up
    When the user taps any visible group member list card
    Then the user details sheet should show card name View Profile Report Block and Add Friend
    When the user taps View Profile on the user details sheet
    # Focus / Interests: asserted when visible; skipped if not on this profile (see page object).
    Then the viewed member profile screen should show profile image name and badges
    When the user taps the back button on the viewed member profile screen
    When the user taps Navigate up
    When the user taps the toolbar back control
    When the user taps the Explore Groups screen back button

  @community @explore_groups @group_date_filter
  Scenario: Group date filters Yesterday, Last 7 days, and Last 30 days refresh member list
    When the user opens the Communitii tab
    Then the Community main screen should show Groups, Friends, Explore Groups, My Groups, and Create Group
    When the user taps the Explore Groups banner and waits for the explore list
    When the user opens a random Explore group card
    Then the group details screen should show name member summary visibility and member list
    Then the group date duration filter card should be visible
    When the user taps the group date duration filter card
    When the user taps the Yesterday option in the date filter
    When the user waits for the group member list to refresh after the date filter
    Then the group member list should show at least one visible user row
    When the user taps the group date duration filter card
    When the user taps the Last 7 Days option in the date filter
    When the user waits for the group member list to refresh after the date filter
    Then the group member list should show at least one visible user row
    When the user taps the group date duration filter card
    When the user taps the Last 30 Days option in the date filter
    When the user waits for the group member list to refresh after the date filter
    Then the group member list should show at least one visible user row
    When the user taps Navigate up
    When the user taps the toolbar back control
    When the user taps the Explore Groups screen back button


  @community @explore_groups @all_data_filter
  Scenario: All Data filter Automated Manual and Both Data updates member list
    When the user opens the Communitii tab
   # Then the Community main screen should show Groups, Friends, Explore Groups, My Groups, and Create Group
    When the user taps the Explore Groups banner and waits for the explore list
    When the user opens a random Explore group card
    Then the group details screen should show name member summary visibility and member list
    When the user taps the All Data filter card
    #When the user taps the ALL DATA option in the All Data filter
    When the user taps the Automated Data option in the All Data filter
    When the user waits for the group member list to refresh after the All Data filter
    Then the group member list should show at least one visible user row
    Then the All Data filter card should show the selected Automated Data filter
    When the user taps on the All Data data filter card
    When the user taps the Manual Data option in the All Data filter
    When the user waits for the group member list to refresh after the All Data filter
    Then the group member list should show at least one visible user row
    Then the All Data filter card should show the selected Manual Data filter
    When the user taps on the All Data data filter card
    When the user taps the Both Data option in the All Data filter
    When the user waits for the group member list to refresh after the All Data filter
    Then the group member list should show at least one visible user row
    Then the All Data filter card should show the selected Both Data filter
    When the user taps Navigate up
    When the user taps the toolbar back control
    When the user taps the Explore Groups screen back button

  @community @create_group
  Scenario: Create group form with public switches and invite member
    When the user opens the Communitii tab
    When the user taps the Create Group button
    When the user enters a create group name and description
    When the user turns on the Make the group public switch
    When the user turns on the Allow members to add more friends switch
    When the user taps the Invite members button on the create group screen
    When the user selects an invite member checkbox if one is shown
    When the user taps the Done button on the create group screen
    When the user scrolls down and taps the Create button on the create group screen

  @community @create_group @create_group_validation
  Scenario: Create group rejects empty name then creates successfully
    When the user opens the Communitii tab
    When the user taps the Create Group button
    When the user scrolls down and taps the Create button on the create group screen
    Then the create group screen should show the group name error message
    When the user enters a create group name and description
    When the user scrolls down and taps the Create button on the create group screen
    Then the created group should be visible after scrolling on the community screen

  @community @create_group @create_group_validation @create_group_special_chars
  Scenario: Create group rejects special characters in name then creates successfully
    When the user opens the Communitii tab
    When the user taps the Create Group button
    When the user enters a create group name with special characters
    When the user scrolls down and taps the Create button on the create group screen
    Then the create group screen should show the special character error message
    When the user enters a create group name and description
    When the user scrolls down and taps the Create button on the create group screen
    Then the created group should be visible after scrolling on the community screen


  @community @edit_group
  Scenario: Edit joined group name description toggles and save updates details
    When the user opens the Communitii tab
    Then the created group should be visible after scrolling on the community screen
    When the user scrolls down on the Groups list and taps the created QA group
    When the user taps the group details overflow menu
    When the user taps Edit Group from the group options menu
    When the user updates the edit group name and description
    When the user flips the public and allow-friends toggles on the edit group form
    When the user taps the Save button on the edit group form
    Then the group details screen should show the edited group name
    When the user taps Navigate up
   # When the user taps the toolbar back control
   # When the user taps the Explore Groups screen back button


  @community @explore_groups @leave_group_cancel
  Scenario: Group details leave flow cancel with No then confirm leave with Yes
    When the user opens the Communitii tab
    When the user taps a random visible joined group card
    When the user taps the group details overflow menu
    When the user taps Leave Group in the overflow menu
    When the user taps No on the leave group confirmation
    When the user taps the group details overflow menu
    When the user taps Leave Group in the overflow menu
    When the user taps Yes on the leave group confirmation
    When the user opens the Communitii tab
    Then the Community main screen should show Groups, Friends, Explore Groups, My Groups, and Create Group
    Then the left group should not appear on the community Groups list


  @community @joined_groups @delete_group
  Scenario: Group details delete flow cancel with No then confirm delete with Yes
    When the user opens the Communitii tab
    When the user scrolls down on the Groups list and taps the created QA group for delete
    When the user taps the group details overflow menu
    When the user taps Delete Group in the overflow menu
    When the user taps No on the delete group confirmation
    When the user taps the group details overflow menu
    When the user taps Delete Group in the overflow menu
    When the user taps Yes on the delete group confirmation
    Then the deleted group should not appear on the community Groups list


  @community @explore_groups @metrics_filter
  Scenario: Group metrics filter Calories Miles Strides and Time updates member list
    When the user opens the Communitii tab
    When the user taps the Explore Groups banner and waits for the explore list
    When the user opens a random Explore group card
    Then the group details screen should show name member summary visibility and member list
    When the user taps the group metrics filter card
    When the user taps the Calories option in the metrics filter
    When the user waits for the group member list to refresh after the metrics filter
    Then the group member list should show at least one visible user row
    Then the metrics filter card should show the selected Calories filter
    Then the group member list visible rows should indicate calories
    When the user taps the group metrics filter card
    When the user taps the Miles option in the metrics filter
    When the user waits for the group member list to refresh after the metrics filter
    Then the group member list should show at least one visible user row
    Then the metrics filter card should show the selected Miles filter
    Then the group member list visible rows should indicate miles
    When the user taps the group metrics filter card
    When the user taps the Strides option in the metrics filter
    When the user waits for the group member list to refresh after the metrics filter
    Then the group member list should show at least one visible user row
    Then the metrics filter card should show the selected Strides filter
    Then the group member list visible rows should indicate strides
    When the user taps the group metrics filter card
    When the user taps the Time option in the metrics filter
    When the user waits for the group member list to refresh after the metrics filter
    Then the group member list should show at least one visible user row
    Then the metrics filter card should show the selected Time filter
    Then the group member list visible rows should indicate time
    When the user taps the toolbar back control
    When the user taps the Explore Groups screen back button

  @community @explore_groups @explore_search
  Scenario: Explore Groups search invalid query then valid group name
    When the user opens the Communitii tab
    When the user taps the Explore Groups banner and waits for the explore list
    When the user taps the explore groups search field
    When the user enters the valid group name in the explore search field
    Then the explore search results should show a card matching the valid group search
    When the user enters an invalid group name in the explore search field
    When the user taps the Explore Groups screen back button

