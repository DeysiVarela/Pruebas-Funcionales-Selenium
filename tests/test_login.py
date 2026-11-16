from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.wait_until_loaded()

    assert inventory_page.URL_PATH in driver.current_url


def test_invalid_password_shows_error(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("standard_user", "wrong_password")

    assert "Username and password do not match" in login_page.error_message()


def test_locked_user_shows_error(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.error_message()
