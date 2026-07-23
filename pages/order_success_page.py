from playwright.sync_api import Page
from pages.base_page import BasePage

class OrderSuccessPage(BasePage):

    PATH = "/payment_done/500"

    def __init__(self, page: Page):
        super().__init__(page)