Feature: Cubii Studio
  As an onboarded Cubii user
  I want to browse Studio categories and open a video
  So that I can view video details on the Studio detail screen

  @smoke @studio
  Scenario: Open Cubii Studio, select a video, and verify video details
    When the user opens the Cubii Studio tab
    When the user taps any visible video card on the Studio screen
    When the user taps any visible video in the Studio category list
    Then the video detail screen should show scroll view title duration bookmark equipment and music played cards
    Then the video player should show start time end time title fullscreen and play controls
    When the user taps the Full Screen button on the video player
    Then the video player should be in full screen mode
    When the user taps the Exit Full Screen button on the video player
    Then the Full Screen button should be displayed on the video player
    When the user pauses the video on the video player
    Then the user click on the back button
    Then the user click on video screen back button
    

  @studio @search
  Scenario: User searches Studio with valid search text and validates empty results
    When the user opens the Cubii Studio tab
    Then the user click on the search bar
    Then the user add the valid data with text "10-Min Grip and Go with Anne"
    Then the user click on the search video
    Then the user click on the back button
    Then the user click on the search cancel button
    Then the user add the invalid video name
    Then the user verify the search no results empty state
    Then the user click on the back button

  @studio @saved_videos_empty
  Scenario: Verify empty Saved Videos screen when no videos are saved
    When the user opens the Cubii Studio tab
    Then the user scroll down to identify the My Library section
    Then the user click on the bookmarks option
    Then the user verify the empty saved videos screen
    Then the user click on the explore video button

  @studio @bookmark
  Scenario: Bookmark and unbookmark the video from video detail screen
    When the user opens the Cubii Studio tab
    When the user taps any visible video card on the Studio screen
    When the user taps any visible video in the Studio category list
    When the user taps the bookmark option on the video detail screen
    Then the bookmark button should display Bookmarked text
    Then the user click on the back button
    Then the user click on video screen back button
    Then the user scroll down to identify the My Library section
    Then the user click on the bookmarks option
    Then the user verify the bookmarked videos
    Then the user click on unbookmark the video
    Then the user verify that video removed from saved list
    Then the user click on the back button on the saved videos screen

  @studio @bookmark_category
  Scenario: Verify user can bookmark from category, confirm on detail, and remove from saved videos
    When the user opens the Cubii Studio tab
    When the user taps any visible video card on the Studio screen
    Then the user verifies a category video card and bookmarks it on the category screen
    When the user opens the same bookmarked video from the category list
    Then the bookmark button should display Bookmarked text
    Then the user click on the back button
    Then the user click on video screen back button
    Then the user scroll down to identify the My Library section
    Then the user click on the bookmarks option
    Then the user verify the bookmarked videos
    Then the user click on unbookmark the video
    Then the user verify that video removed from saved list
    Then the user click on the back button on the saved videos screen

  @studio @view_all
  Scenario Outline: Verify View All opens each Studio category list
    When the user opens the Cubii Studio tab
    Then the user verifies the "<category>" category is visible on Studio
    When the user taps View All for "<category>" on the Studio screen
    Then the user verify all the video list
    Then the user click on the back button

    Examples:
      | category                      |
      | Class Collections             |
      | Choose by Class Format        |
      | Choose by Class Length        |
      | Choose by Instructor          |
      | Choose by Class Functionality |


