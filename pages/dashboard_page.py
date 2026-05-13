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