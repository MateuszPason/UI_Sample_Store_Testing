from playwright.sync_api import expect, Page
import pytest

@pytest.mark.parametrize("scenario_key", ["valid_term", "invalid_term"])
class TestSearch:
    def test_search_by_term(self, scenario_key, home_page, page: Page, config, cookie_modal, header, product_listing_page, get_search_term_data):
        scenario = get_search_term_data[scenario_key]

        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        header.go_to_products_listing()
        expect(product_listing_page.all_products_heading).to_be_visible()

        product_listing_page.type_search_term(scenario["term"])
        product_listing_page.submit_search_term()

        expect(product_listing_page.searched_products_heading).to_be_visible()


        if scenario["expect_results"]:
            searched_products_locators = product_listing_page.get_all_searched_product_title_locators()
            for single_locator in searched_products_locators:
                expect(single_locator).to_contain_text(scenario["term"])
        else:
            expect(product_listing_page.product_card).to_have_count(0)
