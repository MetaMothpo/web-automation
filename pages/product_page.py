from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    # Locators
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product-item")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".card-title")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='add-to-cart']")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "[data-test='quantity']")
    CART_ICON = (By.CSS_SELECTOR, ".fa-cart-shopping")  # Using class since it's an icon
    
    def select_product(self, product_name):
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        for product in products:
            title = product.find_element(*self.PRODUCT_TITLE).text
            if product_name.lower() in title.lower():
                product.click()
                break
    
    def add_to_cart(self, quantity=1):
        if quantity > 1:
            self.input_text(*self.QUANTITY_INPUT, str(quantity))
        self.click(*self.ADD_TO_CART_BUTTON)
        
    def go_to_cart(self):
        self.click(*self.CART_ICON) 