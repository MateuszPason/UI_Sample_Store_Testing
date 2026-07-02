from pages.base_page import BasePage
from playwright.sync_api import Page
from typing import Self

class LoginPage(BasePage):

    PATH = "/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.signup_form_heading = self.page.get_by_role("heading", name="New User Signup!")
        self.signup_name_input = self.page.get_by_test_id("signup-name")
        self.signup_email_input = self.page.get_by_test_id("signup-email")
        self.signup_button = self.page.get_by_role("button", name="Signup")

    def goto(self, base_url: str) -> Self:
        self.page.goto(f"{base_url}{self.PATH}")
        return self