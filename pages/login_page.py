from pages.base_page import BasePage
from playwright.sync_api import Page
from typing import Self

class LoginPage(BasePage):

    PATH = "/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.signup_form_heading = self.page.get_by_role("heading", name="New User Signup!")
        self._signup_name_input = self.page.get_by_test_id("signup-name")
        self._signup_email_input = self.page.get_by_test_id("signup-email")
        self._signup_button = self.page.get_by_role("button", name="Signup")

    def goto(self, base_url: str) -> Self:
        self.page.goto(f"{base_url}{self.PATH}")
        return self

    def complete_new_user_data_form(self, user_data: dict) -> None:
        self._signup_name_input.fill(user_data["name"])
        self._signup_email_input.fill(user_data["email"])

    def submit_new_user_data_form(self) -> None:
        self._signup_button.click()