class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator, timeout=5000):
        try:
            self.page.locator(locator).wait_for(
                state="visible",
                timeout=timeout
            )
            return True

        except Exception as e:
            print(f"Element not visible: {locator}")
            print(f"Error: {e}")
            return False