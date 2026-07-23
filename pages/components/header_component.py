from playwright.sync_api import Page

class HeaderComponent:
    def __init__(self, page: Page):
        self.page = page

        self.login_signup_link = self.page.get_by_role("link", name="Signup / Login")
        self.logged_in_user_name = self.page.locator("ul.nav li", has_text="Logged in as")
        self.delete_account_button_link = self.page.get_by_role("link", name="Delete Account")
        self.logout_link = self.page.get_by_role("link", name="Logout")
        self.contact_us_link = self.page.get_by_role("link", name="Contact us")
        self.test_cases_link = self.page.locator("ul.nav a:has-text('Test Cases')")
        self.products_link = self.page.get_by_role("link", name="Products")
        self.cart_link = self.page.get_by_role("link", name="Cart")

    def go_to_login(self) -> None:
        self.login_signup_link.click()

    def logout_user(self) -> None:
        self.logout_link.click()

    def go_to_contact_us_form(self) -> None:
        self.contact_us_link.click()

    def go_to_test_cases_page(self) -> None:
        self.test_cases_link.click()

    def go_to_products_listing(self) -> None:
        self.products_link.click()

    def go_to_cart(self) -> None:
        self.cart_link.click()

    def get_username(self) -> str:
        return self.logged_in_user_name.inner_text().strip()

    def delete_account(self) -> None:
        self.delete_account_button_link.click()