from playwright.sync_api import Page

class HeaderComponent:
    def __init__(self, page: Page):
        self.page = page

        self.login_signup_link = self.page.get_by_role("link", name="Signup / Login")

    def go_to_login(self) -> None:
        self.login_signup_link.click()