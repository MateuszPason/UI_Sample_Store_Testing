from playwright.sync_api import Page

class CartModalComponent:
    def __init__(self, page: Page):
        self.page = page

        self.continue_shopping_button = self.page.locator("#cartModal").get_by_role("button", name="Continue Shopping")
        self.view_cart_link = self.page.locator("#cartModal").get_by_role("link", name="View Cart")

    def continue_shopping_after_add_to_cart(self) -> None:
        self.continue_shopping_button.click()

    def view_cart(self) -> None:
        self.view_cart_link.click()