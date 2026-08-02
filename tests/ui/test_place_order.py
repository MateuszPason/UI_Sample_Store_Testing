from playwright.sync_api import expect


class TestPlaceOrder:
    def test_login_before_checkout(
        self,
        page,
        home_page,
        config,
        header,
        login_page,
        cookie_modal,
        correct_login_data,
        product_listing_page,
        cart_modal,
        basket_page,
        checkout_page,
        new_user_data,
        payment_details_page,
        credit_card_details,
        order_success_page,
        account_delete_confirmation_page,
    ):
        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        header.go_to_login()
        login_page.complete_login_form(
            correct_login_data["email"], correct_login_data["password"]
        )
        login_page.submit_login_form()
        expect(header.logged_in_user_name).to_contain_text(correct_login_data["name"])

        product_listing_page.add_to_cart_nth_product(1)

        cart_modal.view_cart()
        expect(page).to_have_url(f"{config['base_url']}{basket_page.PATH}")

        basket_page.go_to_checkout()

        expect(
            checkout_page.delivery_address_list.locator(checkout_page.title_fname_lname)
        ).to_have_text(
            f"{correct_login_data["title"]} {correct_login_data["address"]["first_name"]} {correct_login_data["address"]["last_name"]}"
        )
        expect(
            checkout_page.delivery_address_list.locator(
                checkout_page.city_state_postcode
            )
        ).to_have_text(
            f"{correct_login_data["address"]["city"]} {correct_login_data["address"]["state"]} {correct_login_data["address"]["zipcode"]}"
        )
        expect(
            checkout_page.delivery_address_list.locator(checkout_page.country)
        ).to_have_text(f"{correct_login_data["address"]["country"]}")
        expect(
            checkout_page.delivery_address_list.locator(checkout_page.phone)
        ).to_have_text(f"{correct_login_data["address"]["mobile_number"]}")

        expect(
            checkout_page.invoice_address_list.locator(checkout_page.title_fname_lname)
        ).to_have_text(
            f"{correct_login_data["title"]} {correct_login_data["address"]["first_name"]} {correct_login_data["address"]["last_name"]}"
        )
        expect(
            checkout_page.invoice_address_list.locator(
                checkout_page.city_state_postcode
            )
        ).to_have_text(
            f"{correct_login_data["address"]["city"]} {correct_login_data["address"]["state"]} {correct_login_data["address"]["zipcode"]}"
        )
        expect(
            checkout_page.invoice_address_list.locator(checkout_page.country)
        ).to_have_text(f"{correct_login_data["address"]["country"]}")
        expect(
            checkout_page.invoice_address_list.locator(checkout_page.phone)
        ).to_have_text(f"{correct_login_data["address"]["mobile_number"]}")

        checkout_page.enter_comment("Test comment")
        checkout_page.click_place_order_button()

        payment_details_page.complete_card_details(credit_card_details)
        payment_details_page.submit_order()

        expect(page).to_have_url(f"{config["base_url"]}{order_success_page.PATH}")
