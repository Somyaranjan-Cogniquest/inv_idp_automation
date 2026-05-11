import sys
import os
import pytest

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from utils.config_reader import Config
from core.playwright_manager import PlaywrightManager
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.model_landing_page import ModelLandingPage
from locators import dashboard_locators as dloc
from locators import login_locators as lloc
from pages.processing_dashboard_page import ProcessingDashboardPage



@pytest.fixture(scope="session")
def browser_context():
    """
    Launch browser once per test session and reuse the same context.
    """
    manager = PlaywrightManager()
    playwright, browser, context, page = manager.start_browser()

    yield manager, playwright, browser, context

    manager.stop_browser(playwright, browser)


@pytest.fixture
def page(browser_context):
    """
    Fresh page per test.
    Always navigates to URL and ensures login.
    """
    manager, playwright, browser, context = browser_context
    page = context.new_page()
    page.goto(Config.BASE_URL)

    if page.locator(lloc.EMAIL_INPUT).count() > 0:
        lp = LoginPage(page)
        lp.login(Config.USERNAME, Config.PASSWORD)
    page.locator(dloc.MODEL_TABLE_HEADER).wait_for(state="visible", timeout=30000)

    yield page
    page.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

@pytest.fixture
def model_landing_page(page):
    return ModelLandingPage(page)

@pytest.fixture
def processing_dashboard_page(page):
    return ProcessingDashboardPage(page)

@pytest.fixture
def login_page_no_auth():
    manager = PlaywrightManager()
    playwright, browser, context, page = manager.start_browser()

    page.goto(Config.BASE_URL)

    login_page = LoginPage(page)

    yield login_page

    manager.stop_browser(playwright, browser)

