from core.base_page import BasePage
from locators import dashboard_locators as loc


class DashboardPage(BasePage):

    def is_logo_visible(self):
        return self.is_visible(loc.COGNIQUEST_LOGO)

    def is_home_breadcrumb_visible(self):
        breadcrumb = self.page.locator(loc.BREADCRUMB_CONTAINER)
        return breadcrumb.is_visible() and "Home" in breadcrumb.inner_text()

    def is_sidebar_home_selected(self):
        return self.is_visible(loc.SIDEBAR_HOME_ICON)

    def is_table_header_visible(self):

        self.page.wait_for_load_state("networkidle")

        self.page.wait_for_timeout(8000)

        return self.is_visible(loc.MODEL_TABLE_HEADER)

    def get_table_row_count(self):
        return self.page.locator(loc.TABLE_ROWS).count()

    def click_first_model_name(self):
        self.page.locator(loc.MODEL_NAME_CELL).first.click()

    def is_trained_status_present(self):
        return (
            self.is_visible(loc.TRAINED_STATUS_ICON)
            or self.is_visible(loc.NOT_TRAINED_STATUS_ICON)
        )

    def is_action_menu_present(self):
        return self.is_visible(loc.ACTION_MENU_BUTTON)

    def open_model_by_name(self, model_name: str):

        model_locator = self.page.locator(
            f"{loc.MODEL_NAME_CELL}:has-text('{model_name}')"
        )

        model_locator.first.click()