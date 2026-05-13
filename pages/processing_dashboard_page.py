from core.base_page import BasePage
from locators import processing_locators as loc


class ProcessingDashboardPage(BasePage):

    def is_processing_dashboard_loaded(self):

        bc = self.page.locator(loc.BREADCRUMB_CONTAINER)

        if not bc.is_visible():

            return False

        return "Processing Dashboard" in bc.inner_text()

    def apply_review_status(self, status):

        status_map = {
            "approved": loc.REVIEW_APPROVED,
            "not approved": loc.REVIEW_NOT_APPROVED,
            "rejected": loc.REVIEW_REJECTED,
            "deleted": loc.REVIEW_DELETED,
        }

        self.page.locator(status_map[status]).first.check()