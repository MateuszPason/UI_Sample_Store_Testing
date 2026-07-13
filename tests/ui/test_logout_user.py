from playwright.sync_api import expect

class TestLogout:
    def test_user_logout(self, page, home_page, config, cookie_modal, login_page, header, correct_login_data):
        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()
        header.go_to_login()

        expect(login_page.login_form_heading).to_be_visible()

        login_page.complete_login_form(correct_login_data["email"], correct_login_data["password"])
        login_page.submit_login_form()

        expect(header.logged_in_user_name).to_be_visible()

        header.logout_user()

        expect(page).to_have_url(f"{config['base_url']}{login_page.PATH}")


