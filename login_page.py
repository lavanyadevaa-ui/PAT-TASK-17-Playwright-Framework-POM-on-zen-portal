# pages/login_page.py
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.email_input = page.locator("//input[@placeholder='Enter your mail']")
        self.password_input = page.locator("//input[@type='password']")
        self.login_button = page.locator("//button[normalize-space()='Sign in']")
        self.ad_close_button = page.locator("xpath=/html/body/div[2]/div[3]/div/div/button")
        self.profile_icon = page.locator("//img[@id='profile-click-icon']")
        self.logout_button = page.locator("//div[normalize-space()='Log out']")
        self.invalid_user_error = page.locator("//p[@id=':r1:-helper-text']")

    # Actions
    def enter_email(self, email: str):
        expect(self.email_input).to_be_visible(timeout=5000)
        self.email_input.fill(email)

    def enter_password(self, password: str):
        expect(self.password_input).to_be_visible(timeout=5000)
        self.password_input.fill(password)

    def click_login(self):
        expect(self.login_button).to_be_visible(timeout=10000)
        self.login_button.click()

    def close_ad(self):
        if self.ad_close_button.is_visible():
            expect(self.ad_close_button).to_be_visible(timeout=50000)
            self.page.locator("xpath=/html/body/div[2]/div[3]/div/div/button").click()

    def click_profile_icon(self):
        from playwright.sync_api import expect
        expect(self.profile_icon).to_be_visible(timeout=10000)
        self.profile_icon.click()

    def click_logout(self):
        from playwright.sync_api import expect
        expect(self.logout_button).to_be_visible(timeout=10000)
        self.logout_button.click()

    def is_login_button_visible(self):
        from playwright.sync_api import expect
        expect(self.login_button).to_be_visible(timeout=10000)
        return self.login_button.is_visible()

    def get_invalid_user_message(self):
        # Wait until error message is visible, then return text
        from playwright.sync_api import expect
        expect(self.invalid_user_error).to_be_visible(timeout=5000)
        return self.invalid_user_error.text_content()
