from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def start_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        self.wait.until(EC.url_contains("checkout-step-one.html"))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))

    def fill_customer_information(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)
        self.wait.until(EC.url_contains("checkout-step-two.html"))

    def finish_order(self):
        self.click(self.FINISH_BUTTON)
        self.wait.until(EC.url_contains("checkout-complete.html"))

    def confirmation_message(self):
        return self.get_text(self.COMPLETE_HEADER)
