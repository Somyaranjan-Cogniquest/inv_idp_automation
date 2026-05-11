from core.base_page import BasePage
from locators import login_locators as loc

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def enter_email(self, email):
        self.fill(loc.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.fill(loc.PASSWORD_INPUT, password)

    def click_sign_in(self):
        self.click(loc.SIGN_IN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in()

    def is_error_displayed(self):
        return self.is_visible(loc.ERROR_MESSAGE)
    
    def is_login_page(self):
        return self.page.locator(loc.EMAIL_INPUT).count() > 0

    def ensure_logged_in(self, username, password, dashboard_locator):
    # already logged in
        if self.page.locator(dashboard_locator).count() > 0:
         return
        if self.is_login_page():
         self.login(username, password)