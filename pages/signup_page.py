from pages.base_page import BasePage
from playwright.sync_api import Page

class SignupPage(BasePage):

    PATH = "/signup"

    def __init__(self, page: Page):
        super().__init__(page)

    def goto(self, base_url):
        self.page.goto(f"{base_url}{self.PATH}")