import json

import requests
from behave import *


@given("I have endpoint with request body {email} and {password}")
def step_impl(context, email, password):
    context.url = 'https://reqres.in/api/login'
    context.headers = {'content-type': 'application/json'}
    context.body = {
        "email": email,
        "password": password
    }


@when("I make an http post call")
def step_impl(context):
    context.res = requests.post(context.url, data=json.dumps(context.body), headers=context.headers)


@then("I should get a response with status code 200")
def step_impl(context):
    resp = context.res
    print(f"This is the Response Code: {resp.status_code}")
    print(f"This is the Response Text: {resp.text}\n")
    assert context.res.status_code == 200, f"expected 200 but returned {resp.status_code}"


@step("I should get a token in response")
def step_impl(context):
    resp = context.res
    print(f"Response: {resp.headers['Content-Type']}\n")
    assert "token" in resp.text, f"Response: {resp.text}"
