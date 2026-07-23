from playwright.sync_api import Page
from pages.base_page import BasePage

class PaymentDetailsPage(BasePage):

    PATH = "/payment"

    def __init__(self, page: Page):
        super().__init__(page)

        self.name_on_card_input = self.page.get_by_test_id("name-on-card")
        self.card_number_input = self.page.get_by_test_id("card-number")
        self.cvc_input = self.page.get_by_test_id("cvc")
        self.expiry_month_input = self.page.get_by_test_id("expiry-month")
        self.expiry_year_input = self.page.get_by_test_id("expiry-year")
        self.pay_and_confirm_order_button = self.page.get_by_test_id("pay-button")
        self.success_message = "#success_message"

    def complete_card_details(self, card_details: dict) -> None:
        self.name_on_card_input.fill(card_details["name"])
        self.card_number_input.fill(card_details["number"])
        self.cvc_input.fill(card_details["cvc"])
        self.expiry_month_input.fill(card_details["expiry_month"])
        self.expiry_year_input.fill(card_details["expiry_year"])

    def submit_order(self) -> None:
        self.pay_and_confirm_order_button.click()
