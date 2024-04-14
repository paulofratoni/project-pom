# Created by Paulo Fratoni (01/03/2024)

import conftest
from selenium.webdriver.common.by import By
from Pages.base_page import Fratoni_BasePage


class HomePage(Fratoni_BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.product_class = (By.XPATH, "//*[@class='inventory_item_name ' and text()='{}']")
        self.product_id = (By.ID, "'{}'")
        self.add_cart = (By.XPATH, "//*[text()='Add to cart']")
        self.cart_icon = (By.XPATH, "//*[@class='shopping_cart_link']")

    # For Add Product to Card By Class
    def ProductClass_to_Cart(self, item_name):
        item = (self.product_class[0], self.product_class[1].format(item_name))
        self.Click(item)
        self.Click(self.add_cart)
    
    # Access Cart
    def GoToCart(self):
        self.Click(self.cart_icon)