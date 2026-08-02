from playwright.sync_api import expect


class TestNewsletter:
    def test_newsletter_registration_footer(
        self, home_page, page, config, cookie_modal, footer, user_email
    ):
        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        expect(footer.footer_heading).to_be_visible()
        footer.complete_newsletter_input(user_email)
        footer.submit_newsletter_form()

        expect(footer.newsletter_subscription_confirmation).to_be_visible()

    def test_newsletter_registration_basket(
        self, home_page, page, config, cookie_modal, header, footer, user_email
    ):
        home_page.goto()
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        header.go_to_cart()

        expect(footer.footer_heading).to_be_visible()
        footer.complete_newsletter_input(user_email)
        footer.submit_newsletter_form()

        expect(footer.newsletter_subscription_confirmation).to_be_visible()
