from pages.base_page import BasePage
from playwright.sync_api import Page

class AccountCreationConfirmationPage(BasePage):

    PATH = "/account_created"

    def __init__(self, page: Page):
        super().__init__(page)

        self.confirmation_heading = self.page.get_by_role("heading", name="Account Created!")
        self.continue_button = self.page.get_by_test_id("continue-button")

    def continue_from_confirmation_page(self) -> None:
        self.continue_button.click()