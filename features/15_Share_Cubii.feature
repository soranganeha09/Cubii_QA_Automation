Feature: Cubii Share Cubii
  As a logged-in Cubii user
  I want to open Share Cubii from the home settings menu
  So that I can share the Cubii app with others

  @share_cubii @share_chrome
  Scenario: Open Share Cubii from More menu
    Then the user clicks on the three dot
    Then the user click on the Share Cubii
    Then the user select the chrome browser
    Then the user click on the cancel option
    Then the user verify the link is open into chrome browser
    Then the user go back to application
    Then the user click back option of the more screen

  @share_cubii @share_gmail
  Scenario: Share Cubii link via Gmail
    Then the user clicks on the three dot
    Then the user click on the Share Cubii
    Then the user click on the gmail option
    Then the user select the aubergine account
    Then the user click on the search and search the Neha
    Then the user share the link with user and click on send message
    Then the user go back to the application

  @share_cubii @share_drive
  Scenario: Share Cubii link via Google Drive
    Then the user clicks on the three dot
    Then the user click on the Share Cubii
    Then the user click on the drive option
    Then the user verify the details file name, email and drive location
    Then the user click on the upload button
    Then the user go back to the application

