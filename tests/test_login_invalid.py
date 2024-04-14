# Created by Paulo Fratoni (01/03/2024)

import pytest
from selenium.webdriver.common.by import By
from Pages.login_page import LoginPage
from Pages.home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login_invalid
class Test_Login_invalid():
    def test_login_invalid(self):
        expected_text = "Epic sadface: Username and password do not match any user in this service"

        # Objects used on test
        login_page = LoginPage()
        #home_page = HomePage()

        # Make invalid login
        login_page.Make_Login("invalid_user", "invalid_passwd")
        
        # Verify if element of erro show on screen
        login_page.Invalid_Login_Element()

        # Verify if error text show on screen
        #login_page.Get_Text_Error().text()
        
