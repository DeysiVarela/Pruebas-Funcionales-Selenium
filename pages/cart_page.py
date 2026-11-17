from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    URL_PATH = "/cart.html"

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
 
    def wait_until_loaded(self):
        self.wait.until(EC.url_contains(self.URL_PATH))

    def item_names(self):
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [element.text for element in elements]

    def item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)
        self.wait.until(EC.invisibility_of_element_located(self.REMOVE_BACKPACK))
