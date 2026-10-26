# pages/home_page.py
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Playwright locators
        self.logout_button = page.locator("#logoutBtn")
        self.login_button = page.locator("#login")

    def logout(self):
        # Click the logout button
        self.logout_button.click()

    def is_logged_out(self):
        # Verify login button is visible after logout
        try:
            expect(self.login_button).to_be_visible(timeout=5000)
            return True
        except Exception:
            return False
