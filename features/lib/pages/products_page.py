from selenium.webdriver.common.by import By
from features.lib.pages.base_page_object import BasePage


class ProductsPage(BasePage):
    locator_dictionary = {
        "heading": (By.CLASS_NAME, 'title')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='https://www.saucedemo.com/')

    def verify_page_heading(self, expected_title):
        current_title = self.find_element(*self.locator_dictionary['heading']).text
        assert current_title == expected_title, f"Current page title '{current_title}' does not match with expected" \
                                                f" title '{expected_title}' "
