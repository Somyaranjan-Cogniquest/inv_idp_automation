from utils.config_reader import Config
from locators import dashboard_locators as loc

def test_valid_login(login_page):

    assert login_page.page.locator(loc.MODEL_TABLE_HEADER).is_visible()