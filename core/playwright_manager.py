from playwright.sync_api import sync_playwright

class PlaywrightManager:

    def start_browser(self):
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        return playwright, browser, context, page

    def stop_browser(self, playwright, browser):
        browser.close()
        playwright.stop()