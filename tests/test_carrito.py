from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_cart_shows_added_product(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.wait_until_loaded()
    inventory_page.add_backpack()
    inventory_page.open_cart()
    cart_page.wait_until_loaded()

    assert cart_page.item_names() == ["Sauce Labs Backpack"]



def test_remove_product_from_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.wait_until_loaded()
    inventory_page.add_backpack()
    inventory_page.open_cart()
    cart_page.wait_until_loaded()
    cart_page.remove_backpack()

    assert cart_page.item_count() == 0
