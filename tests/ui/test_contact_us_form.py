from playwright.sync_api import Page, expect


class TestContactUsForm:
    def test_successful_message_send(self, page: Page, config, home_page, cookie_modal, header, contact_us_page, get_contact_form_data):
        home_page.goto(config["base_url"])
        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()

        header.go_to_contact_us_form()
        expect(contact_us_page.contact_form_heading).to_be_visible()

        page.once("dialog", lambda dialog: dialog.accept())

        contact_us_page.complete_contact_us_form(get_contact_form_data)
        contact_us_page.submit_contact_us_form()

        expect(contact_us_page.success_message).to_be_visible()