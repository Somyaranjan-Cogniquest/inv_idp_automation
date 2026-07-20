class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).first.click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator, timeout=5000):
        loc = self.page.locator(locator)
        try:
            loc.first.wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False
        
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).first.click()

    def fill(self, locator, value):
        self.page.locator(locator).first.fill(value)

    def is_visible(self, locator):
        return self.page.locator(locator).count() > 0    