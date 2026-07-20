import re
from core.base_page import BasePage
from locators import monitoring_locators as loc

class MonitoringPage(BasePage):

    def is_monitoring_page_open(self):
        return self.page.locator(loc.HEADER_BAR).count() > 0

    def get_summary_data(self):
        txt = self.page.locator(loc.SUMMARY_BAR).inner_text()

        def grab(label):
            m = re.search(rf"{label}\s*:\s*(\d+)", txt)
            return int(m.group(1)) if m else 0

        data = {
            "total_docs": grab("Total Docs"),
            "approved": grab("Approved"),
            "failed": grab("Failed"),
        }

        print("\n[Monitoring Summary]")
        for k, v in data.items():
            print(f"{k}: {v}")

        return data

    def is_monitoring_table_visible(self):
        return self.page.locator(loc.LEFT_TABLE).is_visible()

    def select_topic(self, topic):
        self.page.locator(loc.TOPIC_INPUT).click()
        self.page.locator(loc.TOPIC_INPUT).fill(topic)
        self.page.keyboard.press("Enter")

    def go_back(self):
        self.page.locator(loc.GO_BACK).first.click()