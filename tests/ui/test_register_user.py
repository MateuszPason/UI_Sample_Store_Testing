from playwright.sync_api import expect

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