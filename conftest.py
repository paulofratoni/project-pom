# Created by Paulo Fratoni (01/03/2024)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
#from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager
#from selenium.webdriver.chrome import service
#from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.common.by import By
#pip install webdriver-manager was installed.

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    
    # setup
    global driver
    
    # For use browser and update.
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    #driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # run test
    yield

    # teardown
    driver.quit()