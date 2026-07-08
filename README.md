# Automation Exercise Sample Store Testing

A comprehensive UI test automation suite for the [Automation Exercise](https://automationexercise.com) e-commerce platform, demonstrating modern testing best practices using Playwright and pytest.

## What This Project Does

This project provides automated UI tests for the Automation Exercise sample store, covering critical user journeys including user registration, login, account management, and account deletion. It showcases professional test automation practices using industry-standard tools and patterns.

## Key Features

- **Page Object Model (POM)** architecture for maintainable test code
- **Playwright** for reliable cross-browser automation
- **Pytest** framework with data-driven testing capabilities
- **Component-based testing** for reusable UI interactions
- **Fixture-based test setup** for clean, DRY test code
- **Parameterized tests** for comprehensive scenario coverage
- **YAML configuration** for environment and browser settings
- **Dynamic test data generation** with UUID-based unique identifiers

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd AutomationExerciseSampleStoreTesting
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install playwright pytest pyyaml
   playwright install
   ```

4. **Verify installation:**
   ```bash
   pytest --version
   ```

### Project Structure

```
AutomationExerciseSampleStoreTesting/
├── config/                    # Configuration files
│   ├── config_reader.py      # Config loader
│   ├── paths.py              # Path utilities
│   └── settings.yaml         # Browser and test settings
├── data/                      # Test data
│   └── users.json            # User credentials and registration data
├── pages/                     # Page Object Models
│   ├── base_page.py          # Base class for all pages
│   ├── home_page.py          # Home page object
│   ├── login_page.py         # Login page object
│   ├── signup_page.py        # Signup page object
│   ├── account_creation_confirmation_page.py
│   ├── account_delete_confirmation_page.py
│   └── components/           # Reusable UI components
│       ├── header_component.py
│       └── cookie_component.py
├── tests/                     # Test cases
│   └── ui/
│       ├── test_login_user.py
│       └── test_register_user.py
├── utils/                     # Utility functions
│   └── data_generator.py     # Test data generators
├── conftest.py               # Pytest fixtures and configuration
└── pytest.ini                # Pytest configuration
```

### Running Tests

**Run all tests:**
```bash
pytest
```

**Run specific test file:**
```bash
pytest tests/ui/test_login_user.py
```

**Run specific test class or method:**
```bash
pytest tests/ui/test_login_user.py::TestLogin
pytest tests/ui/test_login_user.py::TestLogin::test_login_variants
```

**Run with verbose output:**
```bash
pytest -v
```

**Run with detailed output and capture disabled:**
```bash
pytest -vv -s
```

### Test Examples

#### User Registration Test
```python
def test_successful_user_register(self, page, config, header, cookie_modal, 
                                   home_page, login_page, signup_page, 
                                   new_user_data, account_creation_confirmation_page):
    home_page.goto(config["base_url"])
    cookie_modal.accept_default_value()
    header.go_to_login()
    login_page.complete_new_user_data_form(new_user_data)
    login_page.submit_new_user_data_form()
    signup_page.complete_registration_form(new_user_data)
    signup_page.submit_registration_form()
```

#### User Login Test (Parameterized)
```bash
pytest tests/ui/test_login_user.py::TestLogin::test_login_variants -v
```
This runs 4 scenarios: valid credentials, invalid email, invalid password, and both invalid.

### Configuration

Edit `config/settings.yaml` to customize test settings:

```yaml
base_url: "https://automationexercise.com"
default_timeout_ms: 10000
locale: "en-US"
viewport:
  width: 1280
  height: 720
```

### Test Data

Test user credentials and registration data are defined in `data/users.json`:

```json
{
    "register": {
        "title": "Mr.",
        "password": "testpass",
        "address": { ... }
    },
    "correct_login_data": {
        "email": "automationtestingexercise@testing.com",
        "password": "automationtestingpassword"
    }
}
```

New registration tests automatically generate unique email addresses using `data_generator.py`.

## Technical Details

### Page Object Model

Each page has a corresponding Page Object class that encapsulates page-specific selectors and interactions:

```python
class LoginPage(BasePage):
    def complete_new_user_data_form(self, user_data: dict):
        # Implementation
        pass
    
    def submit_new_user_data_form(self):
        # Implementation
        pass
```

### Fixtures

Pytest fixtures provide reusable test setup:

- `page` - Playwright page object
- `header` - Header component instance
- `cookie_modal` - Cookie consent modal component
- `home_page`, `login_page`, `signup_page` - Page objects
- `config` - Test configuration
- `new_user_data` - Randomly generated user data
- `correct_login_data` - Pre-configured login credentials

### Components

Reusable UI components abstract common interactions:

```python
# HeaderComponent
class HeaderComponent(BasePage):
    def go_to_login(self):
        # Navigate to login
        pass

# CookieComponent
class CookieComponent(BasePage):
    def accept_default_value(self):
        # Accept cookies
        pass
```

## Support & Documentation

- **Playwright Documentation**: https://playwright.dev/python/
- **Pytest Documentation**: https://docs.pytest.org/
- **Automation Exercise**: https://automationexercise.com
- **Page Object Model Pattern**: https://playwright.dev/python/docs/pom


### Code Guidelines

- Follow PEP 8 style guidelines
- Use descriptive test names following the pattern `test_<action>_<expected_result>`
- Keep Page Object methods focused and single-responsibility
- Add docstrings to complex test logic
- Maintain fixture reusability and avoid duplication

## Maintainer

Created as part of the Automation Projects Portfolio.

## License

This project is provided as-is for educational and testing purposes.

---

**Happy Testing! 🚀**
