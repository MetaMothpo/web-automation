from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    # Locators
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='proceed-checkout']")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart-item")
    PROCEED_1 = (By.CSS_SELECTOR, "[data-test='proceed-1']")
    PROCEED_2 = (By.CSS_SELECTOR, "[data-test='proceed-2']")
    PROCEED_3 = (By.CSS_SELECTOR, "[data-test='proceed-3']")
    
    def proceed_to_checkout(self):
        self.click(*self.CHECKOUT_BUTTON)
        
    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def proceed_through_checkout(self):
        self.click(*self.PROCEED_1)
        self.click(*self.PROCEED_2)
        self.click(*self.PROCEED_3) 