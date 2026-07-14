# Copilot Instructions — AutomationExerciseSampleStoreTesting

## What this repo does
A UI test automation suite that exercises the public practice e-commerce site
**https://automationexercise.com** (no local app to run/build — tests drive the real,
live external site over the network). The current implemented suite covers user
registration, login/logout, contact form submission, product listing to product
details navigation, product search, and test-cases page visibility. Built with
**Playwright (Python, sync API)** + **pytest**, using the **Page Object Model (POM)**.
The repo also includes account creation and account deletion confirmation page
objects for related account flows.

## Tech stack
- Python 3.11+ minimum (repo's `.venv` currently uses 3.14.3, which satisfies this)
- `playwright` (sync API) + `pytest-playwright` plugin (provides the `page`, `browser`,
  `browser_context_args` fixtures) + `pytest-base-url`
- `pytest` as the test runner
- `pyyaml` for reading `config/settings.yaml`
- No JS/TS, no bundler, no local server — this is Python-only, test-only code

## Critical setup steps (do these before running anything)
`requirements.txt` exists and should be the default install source. There is still
**no `pyproject.toml`**. For a fresh environment:
```bash
pip install -r requirements.txt
playwright install chromium   # downloads browser binaries (only needed once per machine)
```
**Always activate the project venv before running Python/pytest commands**, even mid-session:
```bash
source .venv/bin/activate
```
A new terminal's `python`/`pytest` often resolve to a pyenv shim or system Python instead
of `.venv`, even if the same version number is reported — this silently causes
`ModuleNotFoundError: No module named 'yaml'` even when the package is installed in the
venv. If you see that error, activate the venv first before troubleshooting further.

`pytest.ini` exists but is currently **empty** — no custom markers, `addopts`, or
`testpaths` are registered. Don't assume markers like `smoke`/`regression` exist.

## Running tests
```bash
pytest                                   # run everything (hits the live site, ~3s/test)
pytest tests/ui/test_login_user.py       # single file
pytest tests/ui/test_login_user.py::TestLogin::test_login_variants   # single test/class
pytest tests/ui/test_search.py           # product search coverage
pytest --collect-only -q                 # verify current collected inventory
pytest -v            # verbose
pytest -vv -s        # verbose + show print output
```
Tests require internet access to `automationexercise.com`; there's no mock/offline mode.
If tests fail due to network errors or unexpected site responses (e.g., HTTP 5xx, changed
selectors), note this in your response and do not suggest retrying indefinitely or adding
`time.sleep()`. Instead, recommend checking site availability or updating the affected locator.
Current collection is 12 Chromium-backed tests via `pytest-playwright` parametrization.
No CI workflow exists yet (`.github/workflows/` is empty) — validate changes locally with
the commands above before considering a change complete.

## Site-specific gotchas
- A fresh terminal's `python`/`pytest` often resolve to a pyenv shim or system Python even
  when the version string looks correct. If `yaml` or Playwright imports fail unexpectedly,
  first re-activate `.venv`.
- The live site can be flaky around the Contact Us flow when navigating there from the header
  under automation. The current reliable test goes directly to `ContactFormPage.PATH`.
- Contact form success text may appear more than once on the page. Prefer scoped locators over
  loose text-only assertions for that flow.

## Project structure
```
conftest.py            # session-scoped fixtures: config, page objects, components, test data
pytest.ini              # pytest config (currently empty)
requirements.txt        # pinned Python dependencies for the suite
config/
  settings.yaml         # base_url, default_timeout_ms, locale, viewport
  config_reader.py      # get_config() -> loads settings.yaml
  paths.py               # ROOT_DIR / DATA_DIR path constants
data/
  users.json             # static registration + known-good login credentials
  form.json              # contact form field data
  contact_us_form.txt    # message body/file support for contact form scenario
  search.json            # valid and invalid search terms
pages/                   # Page Object Model — one class per page, all extend BasePage
  base_page.py           # holds self.page only
  home_page.py, login_page.py, signup_page.py
  account_creation_confirmation_page.py, account_delete_confirmation_page.py
  contact_form_page.py, products_listing_page.py, products_details_page.py,
  tst_cases_page.py
  components/            # cross-page reusable pieces (header, cookie-consent banner)
tests/ui/                # current UI coverage lives here
  test_contact_us_form.py
  test_login_user.py
  test_logout_user.py
  test_plp_pdp_combined.py
  test_register_user.py
  test_search.py
  test_test_cases.py
utils/
  data_generator.py       # generate_new_user_data() (uuid-based unique email/name),
                           # get_correct_login_data(), get_form_data(), get_search_data()
reports/                 # git-ignored output dir (currently empty; no reporter configured yet)
```

## Coding guidelines (follow existing conventions)
- **Page Objects**: extend `BasePage`; build all Playwright locators as `self._xxx`
  instance attributes inside `__init__` (locators are lazy/auto-retrying — safe to store,
  unlike Selenium WebElements). If a locator is ever referenced directly in a test file
  (e.g., passed to `expect()`), store it without a leading underscore. Locators that are
  only accessed through page object methods and never referenced in test files directly
  use a leading underscore.
- Locator selection priority:
  1. If the element has a `data-qa` attribute, use `page.get_by_test_id(...)` (remapped to
     `data-qa` by the `configure_test_id_attribute` fixture — no config change needed).
  2. Otherwise, prefer `get_by_role`, `get_by_label`, or `get_by_text`.
  3. Use raw CSS/XPath only if no accessible alternative exists.
- Use Playwright's `expect()` web-first assertions in tests; **never** use `time.sleep()`.
- Prefer direct page-object navigation when the live site is known to be less stable through
  a longer UI path, as in the current contact form test.
- Each Page Object method should do one thing (fill a form, submit a form, navigate) —
  compose them in tests rather than adding multi-step "do everything" methods.
- New fixtures (page objects, components, generated data) go in the root `conftest.py`,
  following the existing pattern of one small fixture per object.
- Test naming: `test_<action>_<expected_result>`; group related tests in a
  `class Test<Feature>:` per file under `tests/ui/`.
- Follow PEP 8. Add docstrings only for non-obvious/multi-step test logic (existing code
  is largely self-documenting via method names — don't over-comment simple locators).
- Test data: prefer extending `data/users.json` + `utils/data_generator.py` over hardcoding
  values in tests, so data stays reusable and unique-per-run (see `uuid`-based email/name
  generation).

## Existing docs/resources
- [README.md](../README.md) — current setup and usage guide aligned with the repo's present
  structure and `requirements.txt`-based installation flow.
- No CONTRIBUTING.md, no linting config (no ruff/flake8/black config file present) — just
  follow PEP 8 and match surrounding code style.
