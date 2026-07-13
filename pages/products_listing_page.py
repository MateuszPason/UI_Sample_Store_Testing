from playwright.sync_api import Locator, Page
from pages.base_page import BasePage

class ProductListingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.all_products_heading = self.page.get_by_role("heading", name="All Products")
        self.product_grid = self.page.locator("div.features_items")
        self.product_card = self.product_grid.locator("div.col-sm-4")

    def get_product_card(self, position: int) -> Locator:
        if position < 1:
            raise ValueError("Product position must be 1 or greater.")

        product_count = self.product_card.count()
        if position > product_count:
            raise IndexError(f"Product position {position} is out of range. Found {product_count} products.")

        return self.product_card.nth(position - 1)

    def view_product(self, position: int = 1) -> None:
        selected_product = self.get_product_card(position)
        selected_product.get_by_role("link", name="View Product").click()
