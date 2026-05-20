Feature: Cubii FTUE with dynamic Wellness Journii flow
  As a first-time Cubii user
  I want FTUE to complete even with dynamic Wellness Journii interruptions
  So that onboarding remains stable across screens

  @smoke @ftue @dynamic @raw_ftue
  Scenario: Execute FTUE flow with dynamic Wellness Journii handling
    Given the user starts the Cubii FTUE flow
    When the user completes login and FTUE steps with dynamic checks
    Then the FTUE flow should complete without failing on optional screens


