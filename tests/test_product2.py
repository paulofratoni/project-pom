import pytest
import time
from selenium.webdriver.common.by import By
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.cart_page import CartPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.products2
class Test_Products2():
    def test_products2(self):
        
        # Objects used on test
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()

        product3 = "Sauce Labs Backpack"
        product4 = "Sauce Labs Bike Light"

        # Make login
        login_page.Make_Login("standard_user", "secret_sauce")

        # Add BackPack to cart
        home_page.ProductClass_to_Cart(product3)

        # Back to Shopping
        cart_page.Back_To_Products()

        # Add Bike Light to cart
        home_page.ProductClass_to_Cart(product4)
        
        # Back to Shopping
        cart_page.Back_To_Products()

        # Access cart and verify if product was add.
        home_page.GoToCart()
        cart_page.Verify_Product_Cart(product3)
        cart_page.Verify_Product_Cart(product4)
