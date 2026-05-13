import os
import sys
import pytest
from playwright.sync_api import sync_playwright

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from utils.config_reader import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.model_landing_page import ModelLandingPage
from pages.processing_dashboard_page import ProcessingDashboardPage
from pages.create_model_page import CreateModelPage
from locators import dashboard_locators as dloc

DEFAULT_MODEL_NAME = os.getenv("MODEL_NAME", "TAAS")


@pytest.fixture(scope="session")
def pw():

    p = sync_playwright().start()

    yield p

    p.stop()


@pytest.fixture(scope="session")
def browser(pw):

    browser = pw.chromium.launch(headless=False)

    yield browser

    browser.close()


@pytest.fixture(scope="session")
def storage_state(browser, tmp_path_factory):
    """Login once and save storage state."""

    state_file = tmp_path_factory.mktemp("state") / "storage.json"

    context = browser.new_context()

    page = context.new_page()

    page.goto(Config.BASE_URL)

    lp = LoginPage(page)

    lp.login(Config.USERNAME, Config.PASSWORD)

    # wait for dashboard to confirm login (using FIXED locator)
    page.locator(dloc.MODEL_TABLE_HEADER).wait_for(
        state="visible",
        timeout=30000
    )

    context.storage_state(path=str(state_file))

    context.close()

    return str(state_file)


@pytest.fixture
def page(browser, storage_state):
    context = browser.new_context(storage_state=storage_state)
    page = context.new_page()
    page.goto(Config.BASE_URL)

    lp = LoginPage(page)

    # ✅ Try dashboard quickly
    try:
        page.locator(dloc.MODEL_TABLE_HEADER).wait_for(state="visible", timeout=5000)
    except Exception:
        # ✅ If redirected to login, login again
        if lp.is_login_page():
            lp.login(Config.USERNAME, Config.PASSWORD)
            page.locator(dloc.MODEL_TABLE_HEADER).wait_for(state="visible", timeout=30000)
        else:
            raise AssertionError(
                f"Neither dashboard nor login page detected. URL: {page.url}"
            )

    yield page
    context.close()


@pytest.fixture
def unauth_page(browser):
    """Unauthenticated page for login negative tests."""

    context = browser.new_context()

    page = context.new_page()

    page.goto(Config.BASE_URL)

    yield page

    context.close()


# ---------- Page object fixtures ----------

@pytest.fixture
def login_page_no_auth(unauth_page):

    return LoginPage(unauth_page)


@pytest.fixture
def dashboard_page(page):

    return DashboardPage(page)


@pytest.fixture
def model_landing_page(page):

    return ModelLandingPage(page)


@pytest.fixture
def processing_page(page):
    """Navigate from dashboard -> model -> processing dashboard."""

    dp = DashboardPage(page)

    dp.open_model_by_name(DEFAULT_MODEL_NAME)

    mp = ModelLandingPage(page)

    mp.open_processing_dashboard()

    page.wait_for_load_state("networkidle")

    yield page


@pytest.fixture
def processing_dashboard_page(processing_page):

    return ProcessingDashboardPage(processing_page)


@pytest.fixture
def create_model_page(page, dashboard_page):
    if not dashboard_page.is_create_model_button_visible():
        pytest.skip("Create Model feature not available")
    cmp = CreateModel