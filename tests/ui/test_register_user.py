from playwright.sync_api import expect, TimeoutError

class TestRegister:
    def test_successful_user_register(self, page, config, header, cookie_modal, home_page, login_page, signup_page, new_user_data, account_creation_confirmation_page):
        home_page.goto()

        expect(page).to_have_url(f"{config["base_url"]}{home_page.PATH}")
        
        cookie_modal.accept_default_value()
        header.go_to_login()

        expect(login_page.signup_form_heading).to_be_visible()

        login_page.complete_new_user_data_form(new_user_data)
        login_page.submit_new_user_data_form()

        expect(signup_page.signup_heading).to_be_visible()

        signup_page.complete_registration_form(new_user_data)
        signup_page.submit_registration_form()

        expect(account_creation_confirmation_page.confirmation_heading).to_be_visible()

    def test_register_existing_email(self, page, config, header, cookie_modal, home_page, login_page, correct_login_data):
        home_page.goto()

        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()
        header.go_to_login()

        expect(login_page.signup_form_heading).to_be_visible()

        login_page.complete_new_user_data_form(correct_login_data)
        login_page.submit_new_user_data_form()

        expect(login_page.error_signup_paragraph).to_be_visible()

    def test_register_while_checkout(self, page, config, home_page, cookie_modal, product_listing_page, cart_modal, header, basket_page, checkout_register_login_modal, login_page, new_user_data, signup_page, account_creation_confirmation_page, checkout_page, payment_details_page, credit_card_details, order_success_page, account_delete_confirmation_page):
        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        product_listing_page.add_to_cart_nth_product(1)
        cart_modal.continue_shopping_after_add_to_cart()

        header.go_to_cart()

        expect(page).to_have_url(f"{config['base_url']}{basket_page.PATH}")

        basket_page.go_to_checkout()

        checkout_register_login_modal.go_to_register_login_form()

        login_page.complete_new_user_data_form(new_user_data)
        login_page.submit_new_user_data_form()

        signup_page.complete_registration_form(new_user_data)
        signup_page.submit_registration_form()

        expect(account_creation_confirmation_page.confirmation_heading).to_be_visible()
        account_creation_confirmation_page.continue_from_confirmation_page()

        expect(header.logged_in_user_name).to_contain_text(new_user_data["name"])

        header.go_to_cart()
        basket_page.go_to_checkout()

        expect(checkout_page.delivery_address_list.locator(checkout_page.title_fname_lname)).to_have_text(f"{new_user_data["title"]} {new_user_data["address"]["first_name"]} {new_user_data["address"]["last_name"]}")
        expect(checkout_page.delivery_address_list.locator(checkout_page.city_state_postcode)).to_have_text(f"{new_user_data["address"]["city"]} {new_user_data["address"]["state"]} {new_user_data["address"]["zipcode"]}")
        expect(checkout_page.delivery_address_list.locator(checkout_page.country)).to_have_text(f"{new_user_data["address"]["country"]}")
        expect(checkout_page.delivery_address_list.locator(checkout_page.phone)).to_have_text(f"{new_user_data["address"]["mobile_number"]}")

        expect(checkout_page.invoice_address_list.locator(checkout_page.title_fname_lname)).to_have_text(f"{new_user_data["title"]} {new_user_data["address"]["first_name"]} {new_user_data["address"]["last_name"]}")
        expect(checkout_page.invoice_address_list.locator(checkout_page.city_state_postcode)).to_have_text(f"{new_user_data["address"]["city"]} {new_user_data["address"]["state"]} {new_user_data["address"]["zipcode"]}")
        expect(checkout_page.invoice_address_list.locator(checkout_page.country)).to_have_text(f"{new_user_data["address"]["country"]}")
        expect(checkout_page.invoice_address_list.locator(checkout_page.phone)).to_have_text(f"{new_user_data["address"]["mobile_number"]}")

        checkout_page.click_place_order_button()

        payment_details_page.complete_card_details(credit_card_details)
        payment_details_page.submit_order()

        expect(page).to_have_url(f"{config["base_url"]}{order_success_page.PATH}")

        header.delete_account()

        expect(account_delete_confirmation_page.confirmation_heading).to_be_visible()
        account_delete_confirmation_page.continue_confirmation()