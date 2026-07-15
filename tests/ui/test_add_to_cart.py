from playwright.sync_api import expect

class TestAddToCart:
    def test_add_to_cart_two_products(self, home_page, page, config, cookie_modal, header, product_listing_page, cart_modal, basket):
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
