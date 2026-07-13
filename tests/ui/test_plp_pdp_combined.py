from playwright.sync_api import expect

class TestProductListingProductDetails:
    def test_product_listing_product_detail_progression(self, page, home_page, config, header, cookie_modal, product_listing_page, product_details_page):
        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        header.go_to_products_listing()
        expect(product_listing_page.all_products_heading).to_be_visible()
        expect(product_listing_page.product_grid).to_be_visible()

        product_listing_page.view_product()

        expect(product_details_page.product_name).to_be_visible()
        expect(product_details_page.product_category).to_be_visible()
        expect(product_details_page.product_price).to_be_visible()
        expect(product_details_page.product_availability).to_be_visible()
        expect(product_details_page.product_condition).to_be_visible()
        expect(product_details_page.product_brand).to_be_visible()