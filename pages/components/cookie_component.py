from playwright.sync_api import Page

class CookieComponent:
    def __init__(self, page: Page):
        self.page = page

        self.consent_button = self.page.get_by_role("button", name="Consent")

    def accept_default_value(self):
        self.consent_button.click()