from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    # Locators
    PAYMENT_METHOD = (By.CSS_SELECTOR, "[data-test='payment-method']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    
    def select_payment_method(self, method):
        self.select_dropdown(*self.PAYMENT_METHOD, method)
        
    def confirm_order(self):
        self.click(*self.CONFIRM_BUTTON) 