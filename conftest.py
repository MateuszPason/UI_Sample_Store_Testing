import pytest
from config.config_reader import get_config
from playwright.sync_api import Playwright, Page
from pages.components.header_component import HeaderComponent
from pages.components.cookie_component import CookieComponent
from pages.components.footer_component import FooterComponent
from pages.components.basket_component import BasketComponent
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_creation_confirmation_page import AccountCreationConfirmationPage
from pages.account_delete_confirmation_page import AccountDeleteConfirmationPage
from pages.contact_form_page import ContactFormPage
from pages.tst_cases_page import TestCasesPage
from pages.products_listing_page import ProductListingPage
from pages.products_details_page import ProductDetailsPage
from utils.data_generator import generate_new_user_data, get_correct_login_data, get_form_data, get_search_data, generate_user_email


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
def footer(page: Page) -> FooterComponent:
    return FooterComponent(page)

@pytest.fixture
def basket(page: Page) -> BasketComponent:
    return BasketComponent(page)

@pytest.fixture
def cookie_modal(page: Page) -> CookieComponent:
    return CookieComponent(page)

@pytest.fixture
def home_page(page: Page, config: dict) -> HomePage:
    return HomePage(page, config["base_url"])

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def signup_page(page: Page) -> SignupPage:
    return SignupPage(page)

@pytest.fixture
def contact_us_page(page: Page) -> ContactFormPage:
    return ContactFormPage(page)

@pytest.fixture
def account_creation_confirmation_page(page: Page) -> AccountCreationConfirmationPage:
    return AccountCreationConfirmationPage(page)

@pytest.fixture
def account_delete_confirmation_page(page: Page) -> AccountDeleteConfirmationPage:
    return AccountDeleteConfirmationPage(page)

@pytest.fixture
def test_cases_page(page: Page) -> TestCasesPage:
    return TestCasesPage(page)

@pytest.fixture
def product_listing_page(page: Page) -> ProductListingPage:
    return ProductListingPage(page)

@pytest.fixture
def product_details_page(page: Page) -> ProductDetailsPage:
    return ProductDetailsPage(page)

@pytest.fixture
def user_email() -> str:
    return generate_user_email()

@pytest.fixture
def new_user_data() -> dict:
    return generate_new_user_data()

@pytest.fixture
def correct_login_data() -> dict:
    return get_correct_login_data()

@pytest.fixture
def get_contact_form_data() -> dict:
    return get_form_data()

@pytest.fixture
def get_search_term_data() -> dict:
    return get_search_data()