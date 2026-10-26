# pages/base_page.py
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def find(self, selector: str):
        """
        Playwright auto-waits for elements, but we can still
        enforce visibility before returning the locator.
        """
        locator = self.page.locator(selector)
        expect(locator).to_be_visible(timeout=5000)
        return locator

    def click(self, selector: str):
        self.find(selector).click()

    def type(self, selector: str, text: str):
        self.find(selector).fill(text)
