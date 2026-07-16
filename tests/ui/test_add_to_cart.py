from playwright.sync_api import expect
import re

class TestAddToCart:
    def test_add_to_cart_two_separate_products(self, home_page, page, config, cookie_modal, header, product_listing_page, cart_modal, basket):
        first_product_index = 1
        second_product_index = 2

        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        header.go_to_products_listing()

        product_listing_page.add_to_cart_nth_product(first_product_index)
        first_product_price = product_listing_page.get_product_card_price(first_product_index)

        cart_modal.continue_shopping_after_add_to_cart()

        product_listing_page.add_to_cart_nth_product(second_product_index)
        second_product_price = product_listing_page.get_product_card_price(second_product_index)

        cart_modal.view_cart()

        expected_cart_rows = [
            {"row": first_product_index, "price": first_product_price, "quantity": "1"},
            {"row": second_product_index, "price": second_product_price, "quantity": "1"},
        ]

        for item in expected_cart_rows:
            row = item["row"]
            price = item["price"]
            quantity = item["quantity"]

            expect(basket.get_nth_product_row_price_locator(row)).to_have_text(price)
            expect(basket.get_nth_product_row_quantity_locator(row)).to_have_text(quantity)
            expect(basket.get_nth_product_row_total_locator(row)).to_have_text(price)

    def test_add_multiple_quantities_of_the_same_product(self, home_page, page, config, cookie_modal, product_listing_page, product_details_page, cart_modal, basket):
        product_quantity = "4"

        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        product_listing_page.view_product()

        expect(page).to_have_url(re.compile(".*product_details.*"))

        product_details_page.change_product_quantity(product_quantity)
        product_details_page.add_product_to_cart()

        cart_modal.view_cart()

        expect(basket.get_nth_product_row_quantity_locator(1)).to_have_text(product_quantity)