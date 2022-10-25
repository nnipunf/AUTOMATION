import unittest
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from ERP.page.login_page import LoginPage
from ERP.page.myInfo_page import MyInfo_Page
from ERP.utils import excel_utils02


# Read data and implement in test
# Write data in Excel

class MyInfoTest(unittest.TestCase):

    def test_ec_add(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        #Implement login
        lp = LoginPage(driver)
        lp.login_orange("Admin", "admin123")

        #Implement My info
        mi = MyInfo_Page(driver)
        mi.emergency_contact_add("Dario Naharis", "Second Son", "000999000")

        ######try doing with datadriven technique using excel for multiple emergency contacts######


        driver.close()




