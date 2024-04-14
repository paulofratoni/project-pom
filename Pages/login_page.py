# Created by Paulo Fratoni (01/03/2024)

import conftest
from selenium.webdriver.common.by import By
from Pages.base_page import Fratoni_BasePage


class LoginPage(Fratoni_BasePage):
    
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.btn_login = (By.ID, "login-button")

    # LOGIN SAUCIDEMO
    def Make_Login(self, username, passwd):
        self.Write(self.username_field, username)
        self.Write(self.password_field, passwd)
        self.Click(self.btn_login)
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.element_error_login = (By.XPATH, "//*[@data-test='error']")
        self.text_error_login = (By.XPATH, "//*[@data-test='error']")

    # For Correct Login    
    def Verify_Success_Login(self):
        self.Verify_Element_Exist(self.page_title)

    # For Incorrect Login
    def Invalid_Login_Element(self):
        self.Verify_Element_Exist(self.element_error_login)
    
    def Get_Text_Error(self, locator):
        self.Verify_Element_Exist(locator)

