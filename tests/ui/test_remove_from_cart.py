from playwright.sync_api import expect


class TestRemoveFromCart:
    def test_remove_single_product_from_cart(
        self,
        home_page,
        page,
        config,
        cookie_modal,
        product_listing_page,
        basket_page,
        cart_modal,
    ):
        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        product_listing_page.add_to_cart_nth_product(1)

        cart_modal.view_cart()

        basket_page.remove_nth_product_row_from_basket(1)

        expect(basket_page.cart_table).to_be_hidden()
        expect(basket_page.empty_cart_message).to_be_visible()

    def test_remove_multiple_products_from_cart(
        self,
        page,
        home_page,
        config,
        cookie_modal,
        product_listing_page,
        cart_modal,
        header,
        basket_page,
    ):
        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        product_listing_page.add_to_cart_nth_product(1)
        cart_modal.continue_shopping_after_add_to_cart()
        product_listing_page.add_to_cart_nth_product(2)
        cart_modal.continue_shopping_after_add_to_cart()
        product_listing_page.add_to_cart_nth_product(3)
        cart_modal.continue_shopping_after_add_to_cart()

        header.go_to_cart()
        expect(page).to_have_url(f"{config['base_url']}{basket_page.PATH}")

        product_name_first = basket_page.get_product_name(1)
        product_name_second = basket_page.get_product_name(2)
        product_name_third = basket_page.get_product_name(3)

        basket_page.remove_nth_product_row_from_basket(1)
        expect(basket_page.get_product_row_by_row_number(1)).not_to_be_visible()
        expect(
            basket_page.cart_table.get_by_text(product_name_first, exact=True)
        ).to_have_count(0)

        basket_page.remove_nth_product_row_from_basket(2)
        expect(basket_page.get_product_row_by_row_number(2)).not_to_be_visible()
        expect(
            basket_page.cart_table.get_by_text(product_name_second, exact=True)
        ).to_have_count(0)

        basket_page.remove_nth_product_row_from_basket(3)
        expect(basket_page.get_product_row_by_row_number(3)).not_to_be_visible()
        expect(
            basket_page.cart_table.get_by_text(product_name_third, exact=True)
        ).to_have_count(0)
