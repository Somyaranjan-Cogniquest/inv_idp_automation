from core.base_page import BasePage
from locators import dashboard_locators as loc



class DashboardPage(BasePage):

    def is_dashboard_loaded(self):

        return self.page.locator(loc.MODEL_TABLE_HEADER).count() > 0

    def get_table_row_count(self):

        return self.page.locator(loc.TABLE_ROWS).count()

    def open_model_by_name(self, model_name: str):

        self.page.locator(
            f"{loc.MODEL_NAME_CELL}:has-text('{model_name}')"
        ).first.click()

    # --- Methods required by test_model_dashboard_extended.py ---

    def is_create_model_button_visible(self):

        return self.page.locator(loc.CREATE_MODEL_BUTTON).count() > 0

    def is_trained_count_visible(self):

        return self.page.locator(
            "th:has-text('Trained Count')"
        ).count() > 0

    def is_action_menu_present(self):

        # multiple exist -> check first
        return self.page.locator(
            loc.ACTION_MENU_ICON
        ).first.is_visible()

    def click_refresh_on_first_model(self):

        # open the first action menu icon (if refresh exists in dropdown)
        self.page.locator(
            loc.ACTION_MENU_ICON
        ).first.click()

        # Adjust these labels based on actual menu
        for label in ["Refresh", "refresh", "Reload", "reload"]:

            item = self.page.locator(f"text={label}")

            if item.count() > 0:

                item.first.click()

                return

    def sort_by_column(self, col_name: str):

        self.page.locator(
            f"th:has-text('{col_name}')"
        ).first.click()

    def is_logo_visible(self):
        return self.page.locator(loc.COGNIQUEST_LOGO).count() > 0  

    def is_home_breadcrumb_visible(self):
        bc = self.page.locator(loc.BREADCRUMB_CONTAINER) 
        return bc.is_visible() and "Home" in bc.inner_text()

    def is_sidebar_home_selected(self):
        return self.page.locator(loc.SIDEBAR_HOME_ICON).count() > 0 

    def is_create_model_button_visible(self):
        return self._create_model_button() is not None

    def click_create_model(self):
        btn = self._create_model_button()
        assert btn is not None, "Create Model button not available for this user/environment"
        btn.click()

    def click_create_model(self):
        # robust click
        if self.page.get_by_role("button", name="Create Model").count() > 0:
            self.page.get_by_role("button", name="Create Model").first.click()
        else:
            self.page.locator(loc.CREATE_MODEL_BUTTON).first.click() 

    def is_create_model_page_open(self):
        # checks Create Model page title
        return self.page.locator("text=Create Model").count() > 0

    def is_model_present(self, model_name: str):
        return self.page.locator(f"{loc.MODEL_NAME_CELL}:has-text('{model_name}')").count() > 0


    def sort_by_column(self, col_name: str):
        self.page.locator(loc.HEADER_BY_TEXT.format(col=col_name)).first.click()

    def apply_doc_status(self, status):
        status_map = {
        "processed": loc.DOC_PROCESSED,
        "unprocessed": loc.DOC_UNPROCESSED
             }
        self.page.locator(status_map[status]).first.check()

    def apply_color_filter(self, color):
        color_map = {
        "green": loc.COLOR_GREEN,
        "red": loc.COLOR_RED
           }
        self.page.locator(color_map[color]).first.check()

    def clear_filters(self):
        self.page.locator(loc.CLEAR_FILTERS_BTN).first.click()

    def is_documents_sidebar_selected(self):
        return self.page.locator(loc.SIDEBAR_DOCUMENTS).count() > 0
    
    def _create_model_button(self):
    # Try multiple possible labels
     candidates = [
        self.page.get_by_role("button", name="Create Model"),
        self.page.get_by_role("button", name="Create"),
        self.page.get_by_role("button", name="New Model"),
        self.page.locator("button:has-text('Create Model')"),
        self.page.locator("button:has-text('New Model')"),
        self.page.locator("button:has-text('Create')")
         ]
     for c in candidates:
        if c.count() > 0 and c.first.is_visible():
            return c.first
     return None