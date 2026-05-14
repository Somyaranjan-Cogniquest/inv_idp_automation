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

    def is_documents_sidebar_selected(self):

        return self.page.locator(
        loc.SIDEBAR_DOCUMENTS
      ).first.is_visible()    
    
    def apply_doc_status(self, status):

        status_map = {
        "processed": loc.DOC_PROCESSED,
        "unprocessed": loc.DOC_UNPROCESSED,
       }

        self.page.locator(
        status_map[status]
       ).first.check()
        
    def are_charts_visible(self):

        return self.page.locator("svg.recharts-surface").count() > 0  

    def apply_color_filter(self, color):

        color_map = {
        "green": loc.COLOR_GREEN,
        "red": loc.COLOR_RED,
       }

        self.page.locator(
        color_map[color]
       ).first.check()  
        
    
    def get_table_row_count(self):
        return self.page.locator(loc.TABLE_ROWS).count()   

    def clear_filters(self):
        self.page.locator(loc.CLEAR_FILTERS_BTN).first.click()

    def is_table_visible(self):
        return self.page.locator(loc.TABLE).is_visible()

    def is_pagination_visible(self):
        return self.page.locator(loc.PAGINATION).count() > 0    
 