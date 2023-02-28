@regression @regression_ui
Feature: Sauce Demo - Login Functionality
    As a tester
    I would like to verify login functionality of Souce Demo website

    Background:
        Given I am on https://www.saucedemo.com/ page

    @navigate
    Scenario: Navigate to the Login page
        Then I should see Login page

    @login
    Scenario Outline: Verify Login - Happy Path
        When I loging with <username> and <password>
        Then I should be logged in
        And I should see <heading> heading on the page

        Examples:
            | username      | password     | heading  |
            | standard_user | secret_sauce | Products |

    @login_error_handling
    Scenario: Verify Login - error handling - username error
        When I click on Login button
        Then I should see Epic sadface: Username is required error on page

    @login_error_handling
    Scenario: Verify Login - error handling - password error
        When I enter username standard_user
        And I click on Login button
        Then I should see Epic sadface: Password is required error on page
