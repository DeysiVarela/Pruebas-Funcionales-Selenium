from pathlib import Path

import pytest
import pytest_html
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS") == "1":
        # Modo headless: Chrome trabaja sin abrir ventana
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")
    # Evita la ventana de Chrome "cambia tu contraseña" al usar saucedemo
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(0)
    yield browser
    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed and "driver" in item.funcargs:
        browser = item.funcargs["driver"]
        name = item.nodeid.replace("::", "_").replace("/", "_")
        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(exist_ok=True)
        browser.save_screenshot(str(screenshot_dir / f"{name}.png"))
        # La misma captura queda incrustada dentro del reporte HTML
        extras = getattr(report, "extras", [])
        extras.append(pytest_html.extras.png(browser.get_screenshot_as_base64()))
        report.extras = extras
