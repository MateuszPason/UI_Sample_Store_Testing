from pages.base_page import BasePage
from playwright.sync_api import Page

class SignupPage(BasePage):

    PATH = "/signup"

    def __init__(self, page: Page):
        super().__init__(page)

        self.signup_heading = self.page.get_by_role("heading", name="Enter Account Information")
        self._title_radio = self.page.locator("[value='Mr']")
        self._password_input = self.page.get_by_test_id("password")
        self._dob_day_dropdown = self.page.get_by_test_id("days")
        self._dob_month_dropdown = self.page.get_by_test_id("months")
        self._dob_year_dropdown = self.page.get_by_test_id("years")
        self._newsletter_checkbox = self.page.get_by_label("Sign up for our newsletter!")
        self._special_offers_checkbox = self.page.get_by_label("Receive special offers from our partners!")
        self._first_name_input = self.page.get_by_test_id("first_name")
        self._last_name_input = self.page.get_by_test_id("last_name")
        self._company_input = self.page.get_by_test_id("company")
        self._address_line_1_input = self.page.get_by_test_id("address")
        self._address_line_2_input = self.page.get_by_test_id("address2")
        self._country_dropdown = self.page.get_by_test_id("country")
        self._state_input = self.page.get_by_test_id("state")
        self._city_input = self.page.get_by_test_id("city")
        self._zipcode_input = self.page.get_by_test_id("zipcode")
        self._mobile_number_input = self.page.get_by_test_id("mobile_number")
        self._create_account_button = self.page.get_by_test_id("create-account")

    def goto(self, base_url):
        self.page.goto(f"{base_url}{self.PATH}")

    def complete_registration_form(self, user_data: dict) -> None:
        self._title_radio.check()
        self._password_input.fill(user_data["password"])
        self._dob_day_dropdown.select_option(user_data["date_of_birth"]["day"])
        self._dob_month_dropdown.select_option(user_data["date_of_birth"]["month"])
        self._dob_year_dropdown.select_option(user_data["date_of_birth"]["year"])
        self._newsletter_checkbox.check()
        self._special_offers_checkbox.check()
        self._first_name_input.fill(user_data["address"]["first_name"])
        self._last_name_input.fill(user_data["address"]["last_name"])
        self._company_input.fill(user_data["address"]["company"])
        self._address_line_1_input.fill(user_data["address"]["line_1"])
        self._address_line_2_input.fill(user_data["address"]["line_2"])
        self._country_dropdown.select_option(user_data["address"]["country"])
        self._state_input.fill(user_data["address"]["state"])
        self._city_input.fill(user_data["address"]["city"])
        self._zipcode_input.fill(user_data["address"]["zipcode"])
        self._mobile_number_input.fill(user_data["address"]["mobile_number"])

    def submit_registration_form(self) -> None:
        self._create_account_button.click()