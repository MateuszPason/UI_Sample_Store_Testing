from pages.base_page import BasePage
from playwright.sync_api import Page

class CheckoutPage(BasePage):

    PATH = "/checkout"

    def __init__(self, page: Page):
        super().__init__(page)

        self.delivery_address_list = self.page.locator("#address_delivery")
        self.invoice_address_list = self.page.locator("#address_invoice")
        self.comment_text_area = self.page.locator("[name='message']")
        self.place_order_button = self.page.get_by_role("link", name="Place Order")

        self.title_fname_lname = "li.address_firstname.address_lastname"
        self.city_state_postcode = "li.address_city.address_state_name.address_postcode"
        self.country = "li.address_country_name"
        self.phone = "li.address_phone"

    def enter_comment(self, comment_content: str) -> None:
        self.comment_text_area.fill(comment_content)

    def click_place_order_button(self) -> None:
        self.place_order_button.click()