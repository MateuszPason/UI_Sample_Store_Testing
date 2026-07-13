from playwright.sync_api import Page, expect

class TestTestCases:
    def test_page_visibility(self, page: Page, config, home_page, cookie_modal, header, test_cases_page):
        home_page.goto(f"{config['base_url']}")
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        header.go_to_test_cases_page()

        expect(page).to_have_url(f"{config['base_url']}{test_cases_page.PATH}")
        expect(test_cases_page.test_cases_heading).to_be_visible()

