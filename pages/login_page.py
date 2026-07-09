from pages.base_page import BasePage
from playwright.sync_api import Page
from typing import Self

class LoginPage(BasePage):

    PATH = "/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.signup_form_heading = self.page.get_by_role("heading", name="New User Signup!")
        self.login_form_heading = self.page.get_by_role("heading", name="Login to your account")
        self.error_login_paragraph = self.page.get_by_text("Your email or password is incorrect!")
        self.error_signup_paragraph = self.page.get_by_text("Email Address already exist!")
        self._signup_name_input = self.page.get_by_test_id("signup-name")
        self._signup_email_input = self.page.get_by_test_id("signup-email")
        self._signup_button = self.page.get_by_role("button", name="Signup")
        self._login_email_input = self.page.get_by_test_id("login-email")
        self._login_password_input = self.page.get_by_test_id("login-password")
        self._login_submit_button = self.page.get_by_test_id("login-button")

    def goto(self, base_url: str) -> Self:
        self.page.goto(f"{base_url}{self.PATH}")
        return self

    def complete_new_user_data_form(self, user_data: dict) -> None:
        self._signup_name_input.fill(user_data["name"])
        self._signup_email_input.fill(user_data["email"])

    def submit_new_user_data_form(self) -> None:
        self._signup_button.click()

    def complete_login_form(self, email: str, password: str) -> None:
        self._login_email_input.fill(email)
        self._login_password_input.fill(password)

    def submit_login_form(self) -> None:
        self._login_submit_button.click()