import pytest
from utils.config_reader import Config

def test_login_invalid_password(login_page_no_auth):
    login_page_no_auth.login(Config.USERNAME, "wrongPassword")
    assert login_page_no_auth.is_error_displayed()

def test_login_invalid_username(login_page_no_auth):
    login_page_no_auth.login("wrong@user.com", Config.PASSWORD)
    assert login_page_no_auth.is_error_displayed()

def test_login_empty_username(login_page_no_auth):
    login_page_no_auth.login("", Config.PASSWORD)
    assert login_page_no_auth.is_error_displayed()

def test_login_empty_password(login_page_no_auth):
    login_page_no_auth.login(Config.USERNAME, "")
    assert login_page_no_auth.is_error_displayed()

def test_login_empty_username_password(login_page_no_auth):
    login_page_no_auth.login("", "")
    assert login_page_no_auth.is_error_displayed()

def test_password_is_masked(login_page_no_auth):
    assert login_page_no_auth.page.locator("#formBasicPassword").get_attribute("type") == "password"

def test_login_button_disabled_when_empty(login_page_no_auth):
    assert login_page_no_auth.page.locator("button[type='submit']").is_disabled()