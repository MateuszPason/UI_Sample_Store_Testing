from playwright.sync_api import Page
from pages.base_page import BasePage
from config.paths import DATA_DIR

class ContactFormPage(BasePage):

    PATH = "/contact_us"

    def __init__(self, page: Page):
        super().__init__(page)

        self.contact_form_heading = self.page.get_by_role("heading", name="Get In Touch")
        self.name_input = self.page.get_by_test_id("name")
        self.email_input = self.page.get_by_test_id("email")
        self.subject_input = self.page.get_by_test_id("subject")
        self.message_input = self.page.get_by_test_id("message")
        self.file_input = self.page.locator("input[name='upload_file']")
        self.submit_form_button = self.page.get_by_test_id("submit-button")
        self.success_message = self.page.locator("div.status.alert.alert-success").filter(has_text="Success! Your details have been submitted successfully.")
        self.home_button = self.page.locator("a.btn.btn-success").filter(has_text="Home")

    def complete_contact_us_form(self, form_data: dict) -> None:
        self.name_input.fill(form_data["name"])
        self.email_input.fill(form_data["email"])
        self.subject_input.fill(form_data["subject"])
        self.message_input.fill(form_data["message"])
        self.file_input.set_input_files(DATA_DIR / form_data["file_name"])

    def submit_contact_us_form(self) -> None:
        self.submit_form_button.click()