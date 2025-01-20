import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import get_test_user_data
from utils.test_results import save_test_result

class TestE2EFlow:
    registered_user = None  # Class variable to store registered user data

    def test_01_user_registration(self, driver):
        """Test user registration process"""
        # Get test data and store it in class variable
        TestE2EFlow.registered_user = get_test_user_data()
        
        register_page = RegisterPage(driver)
        register_page.register_new_user(TestE2EFlow.registered_user)
        
        print(f"\n✅ PASS: Registration successful")
        print(f"Created user with email: {TestE2EFlow.registered_user['email']} and password: {TestE2EFlow.registered_user['password']}")
        
        # Save test result
        save_test_result("Registration", "PASS", 
                        TestE2EFlow.registered_user['email'], 
                        TestE2EFlow.registered_user['password'])

    def test_02_user_login(self, driver):
        """Test user login process"""
        # Use the stored credentials from registration
        if not TestE2EFlow.registered_user:
            TestE2EFlow.registered_user = get_test_user_data()
            
        login_page = LoginPage(driver)
        login_page.login(TestE2EFlow.registered_user['email'], 
                        TestE2EFlow.registered_user['password'])
        
        # Wait for login to complete and products to be visible
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='product-name']")))
        
        print("\n✅ PASS: Login successful")
        save_test_result("Login", "PASS")

    def test_03_add_to_cart(self, driver):
        """Test adding product to cart"""
        # Products are already visible after login, just select product
        home_page = HomePage(driver)
        home_page.select_product("Combination Pliers")
        
        # Wait for add to cart button and click it
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='add-to-cart']")))
        product_page = ProductPage(driver)
        product_page.add_to_cart()
        
        # Wait and click cart icon
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa-cart-shopping")))
        product_page.go_to_cart()
        
        # Wait for proceed button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='proceed-1']")))
        
        print("\n✅ PASS: Product added to cart")
        
        # Save test result
        save_test_result("Add to Cart", "PASS")

    def test_04_checkout_process(self, driver):
        """Test checkout process"""
        cart_page = CartPage(driver)
        cart_page.proceed_through_checkout()
        
        # Wait for payment section
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='payment-method']")))
        
        print("\n✅ PASS: Proceeded through checkout")
        
        # Save test result
        save_test_result("Checkout", "PASS")

    def test_05_payment_completion(self, driver):
        """Test payment process"""
        checkout_page = CheckoutPage(driver)
        checkout_page.select_payment_method("cash-on-delivery")
        
        # Wait for payment method to be selected
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='finish']")))
        
        checkout_page.confirm_order()
        
        print("\n✅ PASS: Payment completed")
        
        # Save test result
        save_test_result("Payment", "PASS") 