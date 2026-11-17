from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.wait_until_loaded()
    inventory_page.add_backpack()

    assert inventory_page.cart_count() == 1


def test_complete_purchase(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.wait_until_loaded()
    inventory_page.add_backpack()
    inventory_page.open_cart()
    checkout_page.start_checkout()
    checkout_page.fill_customer_information("Deysi", "Varela", "760001")
    checkout_page.finish_order()

    assert checkout_page.confirmation_message() == "Gracias por su compra"
