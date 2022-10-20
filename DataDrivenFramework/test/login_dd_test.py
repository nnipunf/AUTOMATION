import unittest
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from DataDrivenFramework.page.login_dd_page import LoginPage
from DataDrivenFramework.utils import excel_utils



class LoginTest(unittest.TestCase):

    def test_dd_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        #Excel Implementation
        file = r"G:\NIPUN_BRACNET\Software QA\AUTOMATION\DataDrivenFramework\data\login_data.xlsx"
        sheet = "Sheet1"

        number_of_row = excel_utils.get_row_count(file, sheet)

        for r in range(2, number_of_row+1):
            username_data = excel_utils.read_data(file, sheet, r, 1)
            password_data = excel_utils.read_data(file, sheet, r, 2)

            lp = LoginPage(driver)
            lp.login_orange(username_data, password_data)

        driver.close()




