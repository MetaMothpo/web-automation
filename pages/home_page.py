from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    # Locators
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='nav-sign-in']")
    REGISTER_LINK = (By.CSS_SELECTOR, "[data-test='nav-sign-up']")
    PRODUCTS_GRID = (By.CSS_SELECTOR, ".products-grid")
    HOME_LINK = (By.CSS_SELECTOR, "[data-test='nav-home']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='product-name']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://practicesoftwaretesting.com/#/"
        
    def go_to_login(self):
        self.click(*self.SIGN_IN_LINK)
        
    def go_to_register(self):
        self.click(*self.REGISTER_LINK)
        
    def go_home(self):
        self.click(*self.HOME_LINK)
        
    def select_product(self, product_name):
        products = self.driver.find_elements(*self.PRODUCT_NAME)
        for product in products:
            if product_name in product.text:
                product.click()
                break 