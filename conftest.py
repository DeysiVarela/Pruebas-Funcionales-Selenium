import os
from pathlib import Path

import pytest
import pytest_html
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox", "edge"],
        help="Navegador en el que corren las pruebas",
    )
    parser.addoption(
        "--grid-url",
        default=None,
        help="Dirección de un Selenium Grid, por ejemplo http://localhost:4444",
    )


def build_options(browser_name, headless):
    if browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        return options

    if browser_name == "edge":
        options = webdriver.EdgeOptions()
    else:
        options = webdriver.ChromeOptions()
        # Evita la ventana de Chrome "cambia tu contraseña" al usar saucedemo
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
            },
        )

    if headless:
        # Modo headless: el navegador trabaja sin abrir ventana
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")
    return options


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    grid_url = request.config.getoption("--grid-url")
    headless = os.getenv("HEADLESS") == "1"
    options = build_options(browser_name, headless)

    if grid_url:
        # El navegador corre en otra máquina (o contenedor), no en este equipo
        browser = webdriver.Remote(command_executor=grid_url, options=options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox(options=options)
    elif browser_name == "edge":
        browser = webdriver.Edge(options=options)
    else:
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
