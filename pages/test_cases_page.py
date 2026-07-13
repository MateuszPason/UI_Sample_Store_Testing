from playwright.sync_api import Page
from pages.base_page import BasePage

class TestCasesPage(BasePage):

    PATH = "/test_cases"

    def __init__(self, page: Page):
        super().__init__(page)

        self.test_cases_heading = self.page.get_by_role("heading", name="Test Cases", exact=True)
        