from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")
    service_obj = Service()

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)

    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver

    try:
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        profile_icon = wait.until(
            EC.visibility_of_element_located((By.ID, "nav-link-accountList-nav-line-1"))
        )
        actions.move_to_element(profile_icon).perform()

        signout_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Sign Out']"))
        )
        signout_btn.click()
        print("Logged out successfully")

    except Exception as e:
        print("Logout skipped:", e)

    finally:
        driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browserInstance")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"screenshot_{datetime.now()}",
                attachment_type=AttachmentType.PNG
            )
