import pytest
from config.config_reader import get_config
from playwright.sync_api import Playwright, Page
from pages.components.header_component import HeaderComponent
from pages.components.cookie_component import CookieComponent
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_creation_confirmation_page import AccountCreationConfirmationPage
from pages.account_delete_confirmation_page import AccountDeleteConfirmationPage
from utils.data_generator import generate_user_data


@pytest.fixture(scope="session")
def config() -> dict:
    return get_config()

@pytest.fixture(scope="session", autouse=True)
def configure_test_id_attribute(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-qa")

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict, config: dict) -> dict:
    return {
        **browser_context_args,
        "locale": config["locale"],
        "viewport": config["viewport"]
    }

@pytest.fixture
def header(page: Page) -> HeaderComponent:
    return HeaderComponent(page)

@pytest.fixture
def cookie_modal(page: Page) -> CookieComponent:
    return CookieComponent(page)

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def signup_page(page: Page) -> SignupPage:
    return SignupPage(page)

@pytest.fixture
def account_creation_confirmation_page(page: Page) -> AccountCreationConfirmationPage:
    return AccountCreationConfirmationPage(page)

@pytest.fixture
def account_delete_confirmation_page(page: Page) -> AccountDeleteConfirmationPage:
    return AccountDeleteConfirmationPage(page)

@pytest.fixture
def new_user_data() -> dict:
    return generate_user_data()