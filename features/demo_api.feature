@regression @regression_api
Feature: POST request

    @post
    Scenario Outline:
        Given I have endpoint with request body <email> and <password>
        When I make an http post call
        Then I should get a response with status code 200
        And I should get a token in response

        Examples:
            | email              | password   |
            | eve.holt@reqres.in | cityslicka |