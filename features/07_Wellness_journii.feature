Feature: Cubii Wellness Journii
  As an onboarded Cubii user
  I want to open the Wellness Journii tab and review the current program
  So that the current month Journii details and daily tasks are displayed correctly

  @smoke @wellness @wellness_journii
  Scenario: Open Wellness Journii and verify current month program and tasks
    When the user opens the Wellness Journii tab
    Then the current and previous Journii tabs should be visible
    Then the current month Journii image should be displayed
    Then the current month Journii title should be displayed
    Then the joined Journii members highlight should be displayed
    Then all visible Journii tasks should show date name and people joined count

  @wellness @wellness_journii @previous_journii
  Scenario: Previous Journii segment shows programs or No Journiis empty state
    When the user opens the Wellness Journii tab
    When the user taps the Previous Journii segment tab
    Then the Previous Journii list should show No Journiis when there are no past programs
    Then the user click on the current tab

  @wellness @wellness_journii @view_all
  Scenario: Open Journii detail scroll to View All and tap the button
    When the user opens the Wellness Journii tab
    #When the user taps the Journii banner card on the Wellness screen
    #Then the Wellness Journii detail screen title should be displayed
    When the user scrolls down to the View All button on the Journii detail screen
    When the user taps the View All button on the Journii detail screen
    Then the user click on back button


  @wellness @wellness_journii @filter
  Scenario: Filter upcoming tasks by Incomplete Completed and All and verify results
    When the user opens the Wellness Journii tab
   # When the user taps the Journii banner card on the Wellness screen
    When the user scrolls down to the View All button on the Journii detail screen
    When the user taps the View All button on the Journii detail screen
    When the user taps the filter option
    When the user taps the Incomplete filter option
    When the user taps Show Results on the upcoming tasks filter
    Then all filtered incomplete upcoming Journii tasks should show date name and people joined
    When the user taps the filter option
    When the user taps the Completed filter option
    When the user taps Show Results on the Completed tasks filter
    Then all filtered complete upcoming Journii tasks should show date name and people joined
    When the user taps the filter option
    When the user taps the All filter option
    When the user taps Show Results on the All tasks filter
    Then all filtered All upcoming Journii tasks should show date name and people joined
    Then the user click on back button


  @wellness @wellness_journii @banner
  Scenario: Open Journii banner detail, verify content, and join when button is shown
    When the user opens the Wellness Journii tab
    When the user taps the Journii banner card on the Wellness screen
    Then the Wellness Journii detail screen title should be displayed
    Then the Wellness Journii detail description should match the join button state
    When the user taps the Journii join button if it is displayed
    Then the user click on back button


  @wellness @wellness_journii @banner_pdf
  Scenario: Open Journii banner, verify progress, expand description, and download PDF
    When the user opens the Wellness Journii tab
    When the user taps the Journii banner card on the Wellness screen
    Then the Journii banner image month title and tasks progress should be displayed
    When the user taps the Wellness Journii title description arrow
    Then the Wellness Journii description link should be displayed
    When the user taps the Wellness Journii Download PDF link
    Then the PDF link should open in Chrome with a cubii.com URL
    When the user returns to the Cubii app from Chrome
    Then the Upcoming Tasks and Previous Tasks tabs should be visible
    Then all upcoming Journii tasks should show date name progress and people joined
    When the user scrolls up to the Journii banner
    When the user taps the Previous Tasks tab
    Then all previous Journii tasks should show date name and people joined
    When the user taps the Back button on the Journii detail screen
    Then the user click on back button

