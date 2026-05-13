from locators import dashboard_locators as loc

def test_valid_login(page):
    assert page.locator(loc.MODEL_TABLE_HEADER).is_visible()