from behave import *

from selenium import webdriver

from features.lib.pages.login_page import LoginPage
from features.lib.pages.products_page import ProductsPage


@given('I am on {url} page')
def step_impl(context, url):
    page = LoginPage(context)
    page.visit(url=url)


@then("I should see Login page")
def verifyLoginButton(context):
    status = context.browser.find_element("xpath", "//input[@id='login-button']").is_displayed()
    assert status is True


@when("I loging with {username} and {password}")
def step_impl(context, username, password):
    page = LoginPage(context)
    page.login(username=username, password=password)


@then("I should be logged in")
def step_impl(context):
    current_url = context.browser.current_url
    assert "https://www.saucedemo.com/inventory.html" in current_url, f"Current URL {current_url} is not matching with Expected URL"


@step("I should see {heading} heading on the page")
def step_impl(context, heading):
    page = ProductsPage(context)
    page.verify_page_heading(expected_title=heading)


@when("I click on Login button")
def step_impl(context):
    page = LoginPage(context)
    page.click_login_button()


@then("I should see {expected_error} error on page")
def step_impl(context, expected_error):
    page = LoginPage(context)
    page.verify_login_error(expected_error=expected_error)


@when("I enter {username}")
def step_impl(context, username):
    page = LoginPage(context)
    page.enter_username(username)
