from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL_PATH = "/inventory.html"

    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    PRICE_VALUES = (By.CLASS_NAME, "inventory_item_price")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")

    def wait_until_loaded(self):
        self.wait.until(EC.url_contains(self.URL_PATH))
        self.wait.until(EC.visibility_of_element_located(self.PRODUCTS))

    def product_count(self):
        return len(self.driver.find_elements(*self.PRODUCTS))

    def select_sort_option(self, value):
        from selenium.webdriver.support.ui import Select

        select = Select(self.wait.until(EC.visibility_of_element_located(self.SORT_SELECT)))
        select.select_by_value(value)

    def prices(self):
        elements = self.driver.find_elements(*self.PRICE_VALUES)
        return [float(element.text.replace("$", "")) for element in elements]

    def add_backpack(self):
        self.click(self.ADD_BACKPACK)

    def cart_count(self):
        return int(self.get_text(self.CART_BADGE))

    def open_cart(self):
        self.click(self.CART_LINK)
