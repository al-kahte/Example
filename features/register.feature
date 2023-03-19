Feature: Registration of users
  As a user
  I want to register for the application
  So that I can access my account

  Scenario: Registering a user
    Given the following user is not registered
      | username   | email               | password |
      | alkahte    | alkahte@outlook.com | password |
    When the user registers with the following information
      | username | email                | password |
      | algahte  | algahte@gmail.com    | 12345    |
    Then the user is registered successfully
    And the user can authenticate with the following information
      | username | password |
      | algahte  | 12345    |
