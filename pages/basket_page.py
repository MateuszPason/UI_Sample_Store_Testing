from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class BasketPage(BasePage):

    PATH = "/view_cart"

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_table = self.page.locator("#cart_info_table")
        self.empty_cart_message = self.page.get_by_text("Cart is empty!")
        self.proceed_to_checkout_button = self.page.locator(
            "a.btn.btn-default.check_out", has_text="Proceed To Checkout"
        )

        self.cart_row_price = ".cart_price"
        self.cart_row_quantity = ".cart_quantity"
        self.cart_row_total = ".cart_total"
        self.cart_row_product_name = ".cart_description h4"

    def get_product_row_by_row_number(self, row_number: int) -> Locator:
        return self.cart_table.locator(f"tr#product-{row_number}")

    def get_nth_product_row_price_locator(self, row_number: int) -> Locator:
        return self.get_product_row_by_row_number(row_number).locator(
            self.cart_row_price
        )

    def get_nth_product_row_quantity_locator(self, row_number: int) -> Locator:
        return self.get_product_row_by_row_number(row_number).locator(
            self.cart_row_quantity
        )

    def get_nth_product_row_total_locator(self, row_number: int) -> Locator:
        return self.get_product_row_by_row_number(row_number).locator(
            self.cart_row_total
        )

    def remove_nth_product_row_from_basket(self, row_number: int) -> None:
        self.cart_table.locator(f"[data-product-id='{row_number}']").click()

    def go_to_checkout(self) -> None:
        self.proceed_to_checkout_button.click()

    def get_product_name(self, row_number: int) -> str:
        return (
            self.get_product_row_by_row_number(row_number)
            .locator(self.cart_row_product_name)
            .inner_text()
        )
