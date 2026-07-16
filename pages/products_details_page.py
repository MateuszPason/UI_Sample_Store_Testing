from playwright.sync_api import Page
from pages.base_page import BasePage
import re


class ProductDetailsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.product_information = self.page.locator("div.product-information")
        self.product_name = self.product_information.get_by_role("heading", level=2)
        self.product_category = self.product_information.locator(
            "p", has_text=re.compile(r"^Category:\s*.+$")
        )
        self.product_price = self.product_information.locator(
            "span", has_text=re.compile(r"^Rs\.\s*\d+")
        )
        self.product_availability = self.product_information.locator(
            "p", has_text=re.compile(r"^Availability:\s*.+$")
        )
        self.product_condition = self.product_information.locator(
            "p", has_text=re.compile(r"^Condition:\s*.+$")
        )
        self.product_brand = self.product_information.locator(
            "p", has_text=re.compile(r"^Brand:\s*.+$")
        )
        self.product_quantity_input = self.page.locator("#quantity")
        self.add_to_cart_button = self.page.get_by_role("button", name="Add to cart")

    def change_product_quantity(self, expected_quantity: str) -> None:
        self.product_quantity_input.clear()
        self.product_quantity_input.fill(expected_quantity)

    def add_product_to_cart(self) -> None:
        self.add_to_cart_button.click()
