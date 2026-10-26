# conftest.py
import pytest
from playwright.sync_api import sync_playwright
from utils import config

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        if config.BROWSER == "chrome":
            browser = p.chromium.launch(headless=False)
        elif config.BROWSER == "firefox":
            browser = p.firefox.launch(headless=False)
        elif config.BROWSER == "edge":
            browser = p.chromium.launch(channel="msedge", headless=False)
        else:
            raise ValueError("Unsupported browser in config.py")
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.goto(config.BASE_URL)
    page.set_viewport_size({"width": 1280, "height": 800})
    yield page
    page.close()
