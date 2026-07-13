from typing import Self
from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):

    PATH = "/"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page)
        self._base_url = base_url.rstrip("/")

    def goto(self, base_url: str | None = None) -> Self:
        target_base_url = (base_url or self._base_url).rstrip("/")
        self.page.goto(f"{target_base_url}{self.PATH}")
        return self