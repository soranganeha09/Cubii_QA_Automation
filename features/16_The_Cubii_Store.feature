Feature: The Cubii Store
  As a logged-in Cubii user
  I want to open The Cubii Store from the home settings menu
  So that I can browse Cubii products online

  @cubii_store
  Scenario: Open The Cubii Store from More menu
    Then the user clicks on the three dot
    Then the user click on the The Cubii Store option
    Then the user click on the cancel icon
    Then the user verify the cubii store link is open
    Then the user go back to the application

    
