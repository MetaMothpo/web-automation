from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='nav-sign-in']")
    EMAIL = (By.CSS_SELECTOR, "[data-test='email']")
    PASSWORD = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-submit']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://practicesoftwaretesting.com/#/"
        
    def login(self, email, password):
        # First navigate to home page
        self.driver.get(self.url)
        
        # Click Sign in link
        self.click(*self.SIGN_IN_LINK)
        
        # Fill in login form
        self.input_text(*self.EMAIL, email)
        self.input_text(*self.PASSWORD, password)
        
        # Click login button
        self.click(*self.LOGIN_BUTTON) 