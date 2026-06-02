Feature: Cubii BLE end-to-end connection from Home tab
  As a Cubii user
  I want to pair and connect my BLE Cubii device from Home
  So that I can see connected status and connection time


  @smoke @ble @home @ble_power_off
  Scenario: Device powered OFF during BLE scan
    Given the user is on the Cubii home tab for BLE pairing
    When the user scans for Cubii while the device is powered off
    Then the powered-off BLE scan should show retry guidance and handle retry or skip safely

  @smoke @ble @home
  Scenario: Execute BLE connection flow with conditional permission and optional screens
    Given the user is on the Cubii home tab for BLE pairing
    When the user completes the end-to-end Cubii BLE connection flow
    Then the Cubii device should be connected and connection details should be visible

#  @smoke @ble @home @bluetooth_off
 # Scenario: Connection attempt when Bluetooth is OFF
  #  Given the user is on the Cubii home tab for BLE pairing
   # When the user attempts BLE connection while phone Bluetooth is off
    #Then the Bluetooth-off flow should enforce enable, recover, and continue BLE connection

  @smoke @ble @disconnect
  Scenario: User manually disconnects the Cubii device
    Given the user has a connected Cubii device on the home page
    When the user manually disconnects the Cubii device from the control card
    Then the Cubii device should show disconnected state with connect and change devices actions

  @ble @stability @restart
  Scenario: App restart - device auto-reconnects after reopening app
    Given the app is ready with a logged-in user and a connected Cubii device
    When the user restarts the app
    Then the Cubii device should auto-reconnect after app relaunch
    And the connect button should not be visible on the device control card after restart

  @ble @stability @foreground
  Scenario Outline: App in foreground - BLE remains connected and metric behavior is validated
    Given the app is ready with a logged-in user and a connected Cubii device
    When the user is <activity> for 30 seconds with the app in foreground
    Then the BLE connection should remain active during the foreground session
    And the pedal metric should <expected_behavior> from the baseline for <activity>

    Examples:
      | activity     | expected_behavior |
      | pedaling     | increase          |
      | not pedaling | remain unchanged  |

  @ble @stability @background
  Scenario Outline: App in background - BLE remains active and metric behavior is validated
    Given the app is ready with a logged-in user and a connected Cubii device
    When the user is <activity> while the app is in background for 45 seconds
    Then the BLE connection should remain active after app returns to foreground
    And the pedal metric should <expected_behavior> from the baseline for <activity>

    Examples:
      | activity     | expected_behavior |
      | pedaling     | increase          |
      | not pedaling | remain unchanged  |
