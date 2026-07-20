import re
from core.base_page import BasePage
from locators import training_locators as loc

class TrainingPage(BasePage):

    # ---------- Navigation ----------
    def is_training_page_open(self):
        return "Training" in self.page.locator(loc.BREADCRUMB_CONTAINER).inner_text()

    # ---------- Charts ----------
    def are_charts_visible(self):
        return self.page.locator(loc.PIE_CHART).count() > 0

    def extract_chart_data(self):
        legends = self.page.locator(loc.LEGEND_ITEM).all_inner_texts()
        data = {}

        for text in legends:
            m = re.match(r"(.+?):\s*(\d+)", text.strip())
            if m:
                data[m.group(1)] = int(m.group(2))

        print("\n[Training Chart Data]")
        for k, v in data.items():
            print(f"{k}: {v}")

        return data

    # ---------- Documents ----------
    def get_documents_count(self):
        txt = self.page.locator(loc.DOCUMENTS_COUNT).inner_text()
        m = re.search(r"Documents:\s*(\d+)", txt)
        return int(m.group(1)) if m else 0

    def is_documents_table_visible(self):
        return self.page.locator(loc.TABLE).is_visible()

    def get_table_row_count(self):
        return self.page.locator(loc.TABLE_ROWS).count()

    # ---------- Monitoring ----------
    def is_monitoring_disabled(self):
        return self.page.locator(loc.MONITORING_BUTTON).first.is_disabled()

    def select_first_document(self):
        self.page.locator(loc.ROW_CHECKBOX).first.check()

    def open_monitoring(self):
        self.select_first_document()
        btn = self.page.locator(loc.MONITORING_BUTTON).first
        assert not btn.is_disabled(), "Monitoring should be enabled after checkbox"
        btn.click()