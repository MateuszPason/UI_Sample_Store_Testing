# Automation Exercise Sample Store Testing

UI test automation for the live [Automation Exercise](https://automationexercise.com) sample store, built with Playwright's Python sync API and pytest. The suite exercises real user journeys against the public site and uses the Page Object Model to keep selectors and interactions maintainable.

## What This Project Does

This repository validates core storefront and account flows on Automation Exercise, including:

- User registration with unique test data
- Login success and negative login scenarios
- Logout flow
- Contact Us form submission
- Products listing to product details navigation
- Product search with matching and no-result cases
- Test Cases page navigation and visibility checks

The tests run directly against the live site, so there is no local application server to start.

## Why This Project Is Useful

- Demonstrates a practical Playwright + pytest automation stack in Python
- Uses page objects and reusable components for cleaner, scalable test code
- Separates static test data, generated data, and runtime configuration
- Shows how to cover both positive and negative UI scenarios with pytest parametrization
- Provides a compact reference project for portfolio work, practice, or framework bootstrapping

## Getting Started

### Prerequisites

- Python 3.11 or newer
- Git
- Internet access to [automationexercise.com](https://automationexercise.com)

### Installation

```bash
git clone https://github.com/MateuszPason/UI_Sample_Store_Testing.git
cd UI_Sample_Store_Testing
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

### Quick Verification

```bash
source .venv/bin/activate
pytest --collect-only -q
```

### Running the Test Suite

Run everything:

```bash
source .venv/bin/activate
pytest
```

Run a single file:

```bash
source .venv/bin/activate
pytest tests/ui/test_search.py
```

Run a single test:

```bash
source .venv/bin/activate
pytest tests/ui/test_login_user.py::TestLogin::test_login_variants -v
```

Run with verbose output:

```bash
source .venv/bin/activate
pytest -vv -s
```

### Configuration

Runtime settings live in [config/settings.yaml](config/settings.yaml).

```yaml
base_url: "https://automationexercise.com"
default_timeout_ms: 10000
locale: "en-US"
viewport:
  width: 1280
  height: 720
```

### Test Data

- [data/users.json](data/users.json) stores registration defaults and known-good login credentials.
- [data/form.json](data/form.json) and [data/contact_us_form.txt](data/contact_us_form.txt) support the contact form scenario.
- [data/search.json](data/search.json) contains valid and invalid search terms.
- [utils/data_generator.py](utils/data_generator.py) generates unique registration identities per run.

## Project Structure

```text
.
|-- config/
|   |-- config_reader.py
|   |-- paths.py
|   `-- settings.yaml
|-- data/
|   |-- contact_us_form.txt
|   |-- form.json
|   |-- search.json
|   `-- users.json
|-- pages/
|   |-- account_creation_confirmation_page.py
|   |-- account_delete_confirmation_page.py
|   |-- base_page.py
|   |-- contact_form_page.py
|   |-- home_page.py
|   |-- login_page.py
|   |-- products_details_page.py
|   |-- products_listing_page.py
|   |-- signup_page.py
|   |-- tst_cases_page.py
|   `-- components/
|       |-- cookie_component.py
|       `-- header_component.py
|-- tests/
|   `-- ui/
|       |-- test_contact_us_form.py
|       |-- test_login_user.py
|       |-- test_logout_user.py
|       |-- test_plp_pdp_combined.py
|       |-- test_register_user.py
|       |-- test_search.py
|       `-- test_test_cases.py
|-- utils/
|   `-- data_generator.py
|-- conftest.py
|-- pytest.ini
|-- README.md
`-- requirements.txt
```

## Test Architecture

The suite follows a straightforward Page Object Model:

- Page classes in [pages](pages) encapsulate page-specific locators and actions.
- Shared UI pieces such as the header and cookie consent are modeled under [pages/components](pages/components).
- Fixtures in [conftest.py](conftest.py) create page objects, components, config, and data for tests.
- Playwright is configured to treat `data-qa` as the test-id attribute, which matches the target site markup.

## Help and Documentation

- Use the GitHub Issues tab in this repository for bugs, questions, or suggested improvements.
- See [README.md](README.md) for setup and execution basics.
- See [.github/copilot-instructions.md](.github/copilot-instructions.md) for contributor-oriented project conventions and testing notes.
- Playwright Python docs: [https://playwright.dev/python/](https://playwright.dev/python/)
- Pytest docs: [https://docs.pytest.org/](https://docs.pytest.org/)
- Automation Exercise site: [https://automationexercise.com/](https://automationexercise.com/)