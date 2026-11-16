from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_inventory_has_six_products(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.wait_until_loaded()

    assert inventory_page.product_count() == 6


def test_products_can_be_sorted_by_price(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.wait_until_loaded()
    inventory_page.select_sort_option("lohi")

    prices = inventory_page.prices()
    assert prices == sorted(prices)
