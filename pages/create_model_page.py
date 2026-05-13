from core.base_page import BasePage
from locators import create_model_locators as loc
import time

class CreateModelPage(BasePage):

    # ---------- Page load / navigation helpers ----------
    def is_open(self) -> bool:
        # Any unique element that exists only on Create Model page
        return self.page.locator(loc.CREATE_MODEL_TITLE).count() > 0

    def wait_until_loaded(self, timeout=30000):
        # Wait for form or title
        self.page.locator(loc.CREATE_MODEL_FORM).wait_for(state="visible", timeout=timeout)

    def ensure_open(self, dashboard_page=None):
        """
        Ensures we are on Create Model page.
        If already open → do nothing.
        If not open and dashboard_page provided → click Create Model.
        """
        if self.is_open():
            return
        if dashboard_page:
            dashboard_page.click_create_model()
        self.wait_until_loaded()

    # ---------- Actions used by tests ----------
    def click_next(self):
        self.page.locator(loc.NEXT_BUTTON).first.click()

    def click_cancel(self):
        self.page.locator(loc.CANCEL_BUTTON).first.click()

    def click_breadcrumb_home(self):
        self.page.locator(loc.BREADCRUMB_HOME).first.click()

    # ---------- Field interactions ----------
    def enter_model_name(self, name: str):
        inp = self.page.locator(loc.MODEL_NAME_INPUT).first
        inp.click()
        inp.fill("")  # clear
        inp.type(name, delay=30)

    def get_model_name_value(self) -> str:
        return self.page.locator(loc.MODEL_NAME_INPUT).first.input_value().strip()

    # ---------- Validations ----------
    def is_error_visible(self) -> bool:
        return self.page.locator(loc.ERROR_MESSAGE).count() > 0

    def is_dashboard_open(self) -> bool:
        # This should check dashboard element (table header, etc.)
        # Put your existing stable dashboard locator here
        from locators import dashboard_locators as dloc
        return self.page.locator(dloc.MODEL_TABLE_HEADER).count() > 0

    # ---------- Mandatory fields ----------
    def fill_mandatory_fields(self):
        """
        Replace this with actual interactions once DOM is confirmed.
        This is intentionally structured so you can plug in selectors later.
        """
        # Example pattern:
        # self.select_project("LUY")
        # self.select_model_type("Invoice")
        # self.enter_model_name("AutoModel")
        pass

    # ---------- Full workflow ----------
    def create_model(self, model_name: str):
        """
        Fill required fields and click Create.
        """
        self.enter_model_name(model_name)
        self.fill_mandatory_fields()

        # Prefer Create Model if it exists, else Next flows.
        if self.page.locator(loc.CREATE_BUTTON).count() > 0:
            self.page.locator(loc.CREATE_BUTTON).first.click()
        else:
            self.click_next()

        # wait for navigation back to dashboard or success toast
        self.page.wait_for_load_state("networkidle")