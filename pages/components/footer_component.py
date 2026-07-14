from playwright.sync_api import Page

class FooterComponent:
    def __init__(self, page: Page):
        self.page = page

        self.footer_heading = self.page.get_by_role("heading", name="Subscription")
        self._newsletter_email_input = self.page.locator("[id='susbscribe_email']")
        self._newsletter_submit_button = self.page.locator("[id='subscribe']")
        self.newsletter_subscription_confirmation = self.page.get_by_text("You have been successfully subscribed!")

    def complete_newsletter_input(self, user_email):
        self._newsletter_email_input.fill(user_email)

    def submit_newsletter_form(self):
        self._newsletter_submit_button.click()