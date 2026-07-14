from playwright.sync_api import Page

class BasketComponent:

    PATH = "/view_cart"

    def __init__(self, page: Page):
        self.page = page