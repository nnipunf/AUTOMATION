import unittest
from selenium import webdriver
import pytest

class SearchEnginessTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path = r"G:\NIPUN_BRACNET\Software QA\Learning\BITM\Tools\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(30)
        print("Title of the page: " + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()