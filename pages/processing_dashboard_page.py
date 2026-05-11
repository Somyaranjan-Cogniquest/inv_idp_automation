from core.base_page import BasePage
from locators import processing_locators as loc

class ProcessingDashboardPage(BasePage):

    # ---------- Page identity ----------
    def is_processing_dashboard_loaded(self):
        return self.is_visible(loc.BREADCRUMB_PROCESSING)

    def is_documents_sidebar_selected(self):
        return self.is_visible(loc.SIDEBAR_DOCUMENTS)

    # ---------- Filters ----------
    def apply_review_status(self, status):
        status_map = {
            "approved": loc.REVIEW_APPROVED,
            "not approved": loc.REVIEW_NOT_APPROVED,
            "rejected": loc.REVIEW_REJECTED,
            "deleted": loc.REVIEW_DELETED
        }
        self.click(status_map[status])

    def apply_doc_status(self, status):
        if status == "processed":
            self.click(loc.DOC_PROCESSED)
        else:
            self.click(loc.DOC_UNPROCESSED)

    def apply_color_filter(self, color):
        if color == "green":
            self.click(loc.COLOR_GREEN)
        else:
            self.click(loc.COLOR_RED)

    def clear_filters(self):
        self.click(loc.CLEAR_FILTERS_BTN)

    # ---------- KPIs ----------
    def get_document_count_text(self):
        return self.page.locator(loc.DOCUMENT_COUNT).inner_text()

    def are_charts_visible(self):
        return self.page.locator(loc.PIE_CHART).count() > 0

    # ---------- Table ----------
    def is_table_visible(self):
        return self.is_visible(loc.TABLE)

    def get_table_row_count(self):
        return self.page.locator(loc.TABLE_ROWS).count()

    def click_first_document(self):
        self.page.locator(loc.DOC_NAME_CELL).first.click()

    # ---------- Pagination ----------
    def is_pagination_visible(self):
        return self.is_visible(loc.PAGINATION)