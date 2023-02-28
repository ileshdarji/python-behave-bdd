from selenium.webdriver.common.by import By
from features.lib.pages.base_page_object import BasePage


class LoginPage(BasePage):
    locator_dictionary = {
        "username": (By.ID, 'user-name'),
        "password": (By.ID, 'password'),
        "login_button": (By.ID, 'login-button'),
        "username_error": (By.TAG_NAME, 'h3'),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='https://www.saucedemo.com/')

    def login(self, username, password):
        self.find_element(*self.locator_dictionary['username']).send_keys(username)
        self.find_element(*self.locator_dictionary['password']).send_keys(password)
        self.find_element(*self.locator_dictionary['login_button']).click()

    def click_login_button(self):
        self.find_element(*self.locator_dictionary['login_button']).click()

    def verify_login_error(self, expected_error):
        actual_error = self.find_element(*self.locator_dictionary['username_error']).text
        assert actual_error == expected_error, f"Current error '{actual_error}' does not match with expected" \
                                                 f" error '{expected_error}' "

    def enter_username(self, username):
        self.find_element(*self.locator_dictionary['username']).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.locator_dictionary['password']).send_keys(password)
