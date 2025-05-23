import os
import time
import pytest
import allure
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(viewport={'width': 1280, 'height': 800})
    page = context.new_page()
    yield page
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and item.get_closest_marker("screenshot"):
        page = item.funcargs.get("page")
        if page:
            try:
                page.wait_for_load_state('networkidle', timeout=5000)
            except Exception:
                pass
            test_name = item.nodeid.split("::")[-1]
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")

            page.screenshot(path=screenshot_path)
            allure.attach(
                body=page.screenshot(),
                name=f"{test_name}_screenshot",
                attachment_type=allure.attachment_type.PNG
            )