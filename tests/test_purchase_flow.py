import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestPurchaseFlow:
    def test_add_product_to_cart(self, driver):
        # Go to home page and select product
        home_page = HomePage(driver)
        home_page.driver.get(home_page.url)
        home_page.go_home()
        home_page.select_product("Combination Pliers")
        
        # Add to cart
        product_page = ProductPage(driver)
        product_page.add_to_cart()
        
        # Proceed through checkout
        cart_page = CartPage(driver)
        cart_page.proceed_through_checkout()
        
        # Select payment method and confirm
        checkout_page = CheckoutPage(driver)
        checkout_page.select_payment_method("cash-on-delivery")
        checkout_page.confirm_order() 