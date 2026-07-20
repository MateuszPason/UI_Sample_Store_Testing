from playwright.sync_api import Page

class CheckoutRegisterLoginModalComponent:
    def __init__(self, page: Page):
        self.page = page

        self.register_login_button = self.page.get_by_role("link", name="Register / Login")

    def go_to_register_login_form(self) -> None:
        self.register_login_button.click()