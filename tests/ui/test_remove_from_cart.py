from playwright.sync_api import expect

class TestRemoveFromCart:
    def test_remove_single_product_from_cart(self, home_page, page, config, cookie_modal, product_listing_page, basket, cart_modal):
        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        product_listing_page.add_to_cart_nth_product(1)

        cart_modal.view_cart()

        basket.remove_nth_product_row_from_basket(1)

        expect(basket.cart_table).to_be_hidden()
        expect(basket.empty_cart_message).to_be_visible()