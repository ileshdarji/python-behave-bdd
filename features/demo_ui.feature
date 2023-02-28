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
    Scenario Outline: Verify Login - error handling
        When I click on Login button
        Then I should see <username_error> error on page
        When I enter <username>
        And I click on Login button
        Then I should see <password_error> error on page

        Examples:
            | username_error                     | password_error                     |
            | Epic sadface: Username is required | Epic sadface: Password is required |