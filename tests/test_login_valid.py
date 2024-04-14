# Created by Paulo Fratoni (01/03/2024)

import pytest
from selenium.webdriver.common.by import By
from Pages.login_page import LoginPage
from Pages.home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login_valid
class Test_Login_valid():
    def test_login_valid(self):
        
        # Objects used on test
        login_page = LoginPage()
        #home_page = HomePage()

        # Make valid login
        login_page.Make_Login("standard_user", "secret_sauce")
        
        # Verify if login is correct
        login_page.Verify_Success_Login()
        
