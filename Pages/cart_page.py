# Created by Paulo Fratoni (01/03/2024)

import conftest
from selenium.webdriver.common.by import By
from Pages.base_page import Fratoni_BasePage


class CartPage(Fratoni_BasePage):
    
    def __init__(self):
        self.driver = conftest.driver
        self.product_class = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.btn_back_shop = (By.ID, "continue-shopping")
        self.btn_back_products = (By.ID, "back-to-products")

    def Verify_Product_Cart(self, item_name):
        item = (self.product_class[0], self.product_class[1].format(item_name))
        self.Verify_Element_Exist(item)
    
    def Back_To_Shopping(self):
        self.Click(self.btn_back_shop)

    def Back_To_Products(self):
        self.Click(self.btn_back_products)