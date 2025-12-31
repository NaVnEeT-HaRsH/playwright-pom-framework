import os
import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL,EMAIL,PASSWORD
from pages.login_page import Login

# Define screenshots directory name
SCREENSHOTS_DIR = "screenshots"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL+"/login")

    yield page
    context.close()


@pytest.fixture(scope="function")
def logged_in_page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"{BASE_URL}/login")

    login = Login(page)
    login.login(EMAIL, PASSWORD)
    assert login.is_user_logged_in(), "Login failed in fixture"

    yield page   # Logged-in page is returned
    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = (item.funcargs.get("page") or item.funcargs.get("logged_in_page"))

        if page:
            # Create screenshots folder if not exists
            os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

            screenshot_path = os.path.join(SCREENSHOTS_DIR,f"{item.name}.png")

            page.screenshot(path=screenshot_path, full_page=True)