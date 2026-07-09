Feature: Cubii Help
  As a logged-in Cubii user
  I want to open Help from the home settings menu
  So that I can view all help and support options

  @help
  Scenario: Open Help from More menu and verify the whole list
    Then the user clicks on the three dot
    Then the user click on the Help
    Then the user verify whole list
    Then the user click on back option of the help screen
    Then the user click on back option of the more screen

  @help @customer_support
  Scenario: Open Customer Support from Help menu
    Then the user clicks on the three dot
    Then the user click on the Help
    Then the user click on the customer support
    Then verify user redirect to the Customer Support screen
    Then the user verify all the available details on the screen
    Then the user click on the Getting Started
    Then the user redirect to the cubii video into the youtube and verify the video name "How To Set Up Your Cubii"
    Then the user go back to cubii application
    Then the user click on the Email us
    Then the user verify that the cubii logo and "What can we help you with today?" text
    Then the user click on the close button
    Then the user click on the Call us
    Then the user verify the dial screen open with the number
    Then the user go back to cubii application
    Then the user click on the Customer support back button
    Then the user click on back option of the help screen
    Then the user click on back option of the more screen

  @help @faq
  Scenario: Open FAQ from Help menu
    Then the user clicks on the three dot
    Then the user click on the Help
    Then the user click on the FAQ option
    Then the user redirect to the FAQ screen
    Then the user verify the text "How can we help"
    Then the user scroll down and verify all FAQ questions are listed
    Then the user click on back option of the FAQ screen
    Then the user click on back option of the help screen
    Then the user click on back option of the more screen

  @help @faq @search
  Scenario: Search for a FAQ question using the search bar
    Then the user clicks on the three dot
    Then the user click on the Help
    Then the user click on the FAQ option
    Then the user redirect to the FAQ screen
    Then the user search for "RPM" in the FAQ search bar
    Then the user verify the FAQ search result contains "RPM"
    Then the user clear the FAQ search bar
    Then the user click on back option of the FAQ screen
    Then the user click on back option of the help screen
    Then the user click on back option of the more screen

  @help @faq @expand
  Scenario: Expand and collapse FAQ questions and verify each interaction
    Then the user clicks on the three dot
    Then the user click on the Help
    Then the user click on the FAQ option
    Then the user redirect to the FAQ screen
    Then the user tap on the FAQ question "How can I view RPM on Home Screen?" and verify it is expanded
    Then the user tap on the FAQ question "How can I view RPM on Home Screen?" and verify it is collapsed
    Then the user tap on the FAQ question "How can I delete my Cubii app account and data?" and verify it is expanded
    Then the user tap on the FAQ question "How can I delete my Cubii app account and data?" and verify it is collapsed
    Then the user tap on the FAQ question "Why can't I log into the app using my website credentials?" and verify it is expanded
    Then the user tap on the FAQ question "Why can't I log into the app using my website credentials?" and verify it is collapsed
    Then the user tap on the FAQ question "Why is Cubii asking for permission to scan nearby devices and my GPS location?" and verify it is expanded
    Then the user tap on the FAQ question "Why is Cubii asking for permission to scan nearby devices and my GPS location?" and verify it is collapsed
    Then the user tap on the FAQ question "How do I manually enter my workout data into the Cubii app?" and verify it is expanded
    Then the user tap on the FAQ question "How do I manually enter my workout data into the Cubii app?" and verify it is collapsed
    Then the user tap on the FAQ question "How do I disconnect my device from the App?" and verify it is expanded
    Then the user tap on the FAQ question "How do I disconnect my device from the App?" and verify it is collapsed
    Then the user scroll down on the FAQ screen
    Then the user tap on the FAQ question "iOS Devices: Issues Connecting to my Cubii" and verify it is expanded
    Then the user tap on the FAQ question "iOS Devices: Issues Connecting to my Cubii" and verify it is collapsed
    Then the user tap on the FAQ question "Why doesn't my manual entry data in the app match the calories reported on my Cubii JR1/Cubii JR2/Cubii Go monitor?" and verify it is expanded
    Then the user tap on the FAQ question "Why doesn't my manual entry data in the app match the calories reported on my Cubii JR1/Cubii JR2/Cubii Go monitor?" and verify it is collapsed
    Then the user tap on the FAQ question "Can multiple people track their progress using one Bluetooth enabled device?" and verify it is expanded
    Then the user tap on the FAQ question "Can multiple people track their progress using one Bluetooth enabled device?" and verify it is collapsed
    Then the user click on back option of the FAQ screen
    Then the user click on back option of the help screen
    Then the user click on back option of the more screen

  @help @product_manual
  Scenario: Open Product Manual from Help menu
    Then the user clicks on the three dot
    Then the user click on the Help
    Then the user click on the Product Manual
    Then verify that product manual screen open
    Then the user click on back option for the Product Manual
    Then the user click on back option of the help screen
    Then the user click on back option of the more screen

  @help @assembly_video
  Scenario: Open Assembly Video from Help menu
    Then the user clicks on the three dot
    Then the user click on the Help
    Then the user click on the Assembly Video
    Then the user verify that Assembly video screen open
    Then the user click on back option of Assembly video
    Then the user click on back option of the help screen
    Then the user click on back option of the more screen

  @help @privacy_policy
  Scenario: Open Privacy Policy from Help menu and verify content
    Then the user clicks on the three dot
    Then the user click on the Help
    Then the user click on the Privacy policy
    Then the user verify the Privacy policy screen
    Then the user verify the Privacy policy description
    Then the user swipe left and comeback to help screen
   # Then the user click on back option of the more screen

  @help @terms_of_service
  Scenario: Open Terms of Service from Help menu and dismiss cookie consent
    Then the user clicks on the three dot
    Then the user click on the Help
    Then the user click on the Terms of Service
    Then the user redirect to the Terms of Service screen
    Then the user verify the Terms of Service description and click on the cancel icon
    Then the user click on back option of the help screen
    Then the user click on back option of the more screen
