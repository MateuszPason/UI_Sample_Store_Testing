from playwright.sync_api import Page, TimeoutError

class CookieComponent:
    def __init__(self, page: Page):
        self.page = page

        self.consent_button = self.page.get_by_role("button", name="Consent")

    def accept_default_value(self) -> None:
        try:
            self.consent_button.wait_for(state="visible", timeout=5000)
            self.consent_button.click()
        except TimeoutError:
            pass