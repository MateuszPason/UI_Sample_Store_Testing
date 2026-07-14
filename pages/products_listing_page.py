from playwright.sync_api import Locator, Page
from pages.base_page import BasePage

class ProductListingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.all_products_heading = self.page.get_by_role("heading", name="All Products")
        self.searched_products_heading = self.page.get_by_role("heading", name="Searched Products")
        self.product_grid = self.page.locator("div.features_items")
        self.product_card = self.product_grid.locator("div.col-sm-4")
        self.product_name = self.product_card.get_by_role("paragraph").first
        self.product_search_input = self.page.get_by_placeholder("Search Product")
        self.submit_search_button = self.page.locator("[id='submit_search']")

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

    def type_search_term(self, search_term: str) -> None:
        self.product_search_input.fill(search_term)

    def submit_search_term(self) -> None:
        self.submit_search_button.click()

    def get_all_searched_product_title_locators(self) -> list:
        number_of_results = self.product_card.count()
        title_locator_of_searched_products = []
        for i in range(number_of_results):
            product_title = self.product_card.nth(i).locator("div.productinfo p")
            title_locator_of_searched_products.append(product_title)

        return title_locator_of_searched_products