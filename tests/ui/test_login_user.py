from playwright.sync_api import expect
import pytest

def build_login_scenarios_data(correct_login_data: dict) -> dict:
    valid_email = correct_login_data["email"]
    valid_password = correct_login_data["password"]
    return {
        "valid": {
            "email": valid_email,
            "password": valid_password,
            "expected_success": True
        },
        "invalid_email": {
            "email": f"invalid_{valid_email}",
            "password": valid_password,
            "expected_success": False
        },
        "invalid_password": {
            "email": valid_email,
            "password": f"invalid_{valid_password}",
            "expected_success": False
        },
        "invalid_email_password": {
            "email": f"invalid_{valid_email}",
            "password": f"invalid_{valid_password}",
            "expected_success": False
        }
    }

class TestLogin:
    @pytest.mark.parametrize("scenario_key", ["valid", "invalid_email", "invalid_password", "invalid_email_password"])
    def test_login_variants(self, scenario_key, page, config, home_page, header, cookie_modal, login_page, correct_login_data):
        login_scenarios_data = build_login_scenarios_data(correct_login_data)
        scenario = login_scenarios_data[scenario_key]

        home_page.goto()

        expect(page).to_have_url(f"{config['base_url']}{home_page.PATH}")

        cookie_modal.accept_default_value()
        header.go_to_login()

        expect(login_page.login_form_heading).to_be_visible()

        login_page.complete_login_form(scenario["email"], scenario["password"])
        login_page.submit_login_form()

        if scenario["expected_success"]:
            expect(header.logged_in_user_name).to_be_visible()
            expect(header.logout_link).to_be_visible()
        else:
            expect(login_page.error_login_paragraph).to_be_visible()