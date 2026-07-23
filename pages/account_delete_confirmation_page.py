from pages.base_page import BasePage
from playwright.sync_api import Page

class AccountDeleteConfirmationPage(BasePage):

    PATH = "/delete_account"

    def __init__(self, page: Page):
        super().__init__(page)

        self.confirmation_heading = self.page.get_by_test_id("account-deleted")
        self.continue_button = self.page.get_by_test_id("continue-button")

    def continue_confirmation(self) -> None:
        self.continue_button.click()