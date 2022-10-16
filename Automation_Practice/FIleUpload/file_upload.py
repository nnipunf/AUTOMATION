from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import unittest



class fileUpload(unittest.TestCase):
    def fUp_01(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.implicitly_wait(30)

        choose_file_bttn = driver.find_element(By.XPATH, '//*[@id="file-upload"]')
        choose_file_bttn.send_keys(r"C:\Users\NIPUN\Downloads\full stack qa engineer.png")

        upld_bttn = driver.find_element(By.XPATH, "//input[@id='file-submit']")
        upld_bttn.click()


        success_msg = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/h3')

        self.assertEqual("Uploaded!", success_msg.text)

        time.sleep(10)




t1 = fileUpload()
t1.fUp_01()