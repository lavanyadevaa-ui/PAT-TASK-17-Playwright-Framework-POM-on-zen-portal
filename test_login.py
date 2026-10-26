# tests/test_login.py
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils import config
@pytest.fixture
def setup(page):
    page.goto("https://v2.zenclass.in/login")
    return LoginPage(page)

def test_successful_login(setup):
    login = setup
    login.enter_email("lavanyadevaa@gmail.com")
    login.enter_password("Hasmith@123003")
    login.click_login()
    # Assert on actual page content
    assert "GUVI" in login.page.title()

def test_unsuccessful_login(setup):
    login = setup
    login.enter_email("wrong@example.com")
    login.enter_password("wrongpassword")
    login.click_login()
    msg = login.get_invalid_user_message()
    assert "*Invalid email!" in msg

def test_validate_input_boxes(setup):
    login = setup
    assert login.email_input.is_visible()
    assert login.password_input.is_visible()

from playwright.sync_api import expect

def test_logout_functionality(setup):
    login = setup
    login.enter_email("lavanyadevaa@gmail.com")
    login.enter_password("Hasmith@123003")
    login.click_login()

    # Step 1: Close the ad popup
    login.close_ad()

    # Step 2: Click profile icon
    login.click_profile_icon()

    # Step 3: Click logout
    login.click_logout()

    # Step 4: Verify login button reappears
    assert login.is_login_button_visible()
