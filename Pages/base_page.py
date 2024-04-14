# Created by Paulo Fratoni (01/03/2024)

import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys


class Fratoni_BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def Locate_Element(self, locator):
        return self.driver.find_element(*locator)
    
    def Locate_Elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def Write(self, locator, text):
        self.Locate_Element(locator).send_keys(text)
    
    def Click(self, locator):
        self.Locate_Element(locator).click()

    def Verify_Element_Exist(self, locator):
        assert self.Locate_Element(locator).is_displayed(), "The element '{locator}' isn't founded on screen"

    def Get_Text_Element(self, locator):
        self.Wait_Show_Element(locator)
        return self.Locate_Element(locator).text

    # Verify if element will show after timeout
    def Wait_Show_Element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(*locator))

    # Check if the especific element exist on the screen.
    def Check_Element_Exist(self, locator):
        assert self.check_element(locator), "Element '{locator}' no exist, but it have to exist."
    
    # Check if the especific element not exist on the screen.
    def Check_Element_NoExist(self, locator):
        assert len(self.Locate_Elements(locator)) == 0, "Element '{locator}' exist, but it can't."

    # Double Click (mouse)
    def Double_Click(self, locator):
        doubleclick_element = self.Wait_Show_Element(locator)
        ActionChains(self.driver).double_click(doubleclick_element).perform()
    
    # Right button click (mouse)
    def Right_Click(self, locator):
        rightclick_element = self.Wait_Show_Element(locator)
        ActionChains(self.driver).context_click(rightclick_element).perform()

    # Keyboards (physical)
    def Keyboard_Command(self, locator, key):
        keyboard_element = self.Locate_Element(locator)
        if key == "F1":
            keyboard_element.send_keys(Keys.F1)
        elif key == "F2":
            keyboard_element.send_keys(Keys.F2)
        elif key == "F3":
            keyboard_element.send_keys(Keys.F3)
        elif key == "F4":
            keyboard_element.send_keys(Keys.F4)
        elif key == "F5":
            keyboard_element.send_keys(Keys.F5)
        elif key == "F6":
            keyboard_element.send_keys(Keys.F6)
        elif key == "F7":
            keyboard_element.send_keys(Keys.F7)
        elif key == "F8":
            keyboard_element.send_keys(Keys.F8)
        elif key == "F9":
            keyboard_element.send_keys(Keys.F9)
        elif key == "F10":
            keyboard_element.send_keys(Keys.F10)
        elif key == "F11":
            keyboard_element.send_keys(Keys.F11)
        elif key == "F12":
            keyboard_element.send_keys(Keys.F12)
        if key == "ENTER":
            keyboard_element.send_keys(Keys.ENTER)
        elif key == "SPACE":
            keyboard_element.send_keys(Keys.SPACE)
        elif key == "BACKSPACE":
            keyboard_element.send_keys(Keys.BACKSPACE)
        elif key == "SHIFT":
            keyboard_element.send_keys(Keys.SHIFT)
        elif key == "LEFT_SHIFT":
            keyboard_element.send_keys(Keys.LEFT_SHIFT)
        elif key == "ALT":
            keyboard_element.send_keys(Keys.ALT)
        elif key == "LEFT_ALT":
            keyboard_element.send_keys(Keys.LEFT_ALT)
        elif key == "PAGE_UP":
            keyboard_element.send_keys(Keys.PAGE_UP)
        elif key == "PAGE_DOWN":
            keyboard_element.send_keys(Keys.PAGE_DOWN)
        elif key == "ARROW_UP":
            keyboard_element.send_keys(Keys.ARROW_UP)
        elif key == "ARROW_DOWN":
            keyboard_element.send_keys(Keys.ARROW_DOWN)
        elif key == "ARROW_RIGHT":
            keyboard_element.send_keys(Keys.ARROW_RIGHT)
        elif key == "ARROW_LEFT":
            keyboard_element.send_keys(Keys.ARROW_LEFT)