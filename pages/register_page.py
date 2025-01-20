from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegisterPage(BasePage):
    # Locators
    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='first-name']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='last-name']")
    DOB = (By.CSS_SELECTOR, "[data-test='dob']")
    ADDRESS = (By.CSS_SELECTOR, "[data-test='address']")
    POSTCODE = (By.CSS_SELECTOR, "[data-test='postcode']")
    CITY = (By.CSS_SELECTOR, "[data-test='city']")
    STATE = (By.CSS_SELECTOR, "[data-test='state']")
    COUNTRY = (By.CSS_SELECTOR, "[data-test='country']")
    PHONE = (By.CSS_SELECTOR, "[data-test='phone']")
    EMAIL = (By.CSS_SELECTOR, "[data-test='email']")
    PASSWORD = (By.CSS_SELECTOR, "[data-test='password']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[data-test='register-submit']")
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='nav-sign-in']")
    REGISTER_LINK = (By.CSS_SELECTOR, "[data-test='register-link']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://practicesoftwaretesting.com/#/"

    def register_new_user(self, user_data):
        # Navigate to home page first
        self.driver.get(self.url)
        # Click Sign in
        self.click(*self.SIGN_IN_LINK)
        # Click Register link
        self.click(*self.REGISTER_LINK)
        # Fill in registration form
        self.input_text(*self.FIRST_NAME, user_data['first_name'])
        self.input_text(*self.LAST_NAME, user_data['last_name'])
        self.input_text(*self.DOB, user_data['dob'])
        self.input_text(*self.ADDRESS, user_data['address'])
        self.input_text(*self.POSTCODE, user_data['postcode'])
        self.input_text(*self.CITY, user_data['city'])
        self.input_text(*self.STATE, user_data['state'])
        self.select_dropdown(*self.COUNTRY, user_data['country'])
        self.input_text(*self.PHONE, user_data['phone'])
        self.input_text(*self.EMAIL, user_data['email'])
        self.input_text(*self.PASSWORD, user_data['password'])
        self.click(*self.REGISTER_BUTTON) 