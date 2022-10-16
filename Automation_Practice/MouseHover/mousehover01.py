from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
"""
class hover():
    def hover_01(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(30)

        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys('Admin')
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

        time.sleep(20)
"""

class hover():
    def hover_01(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        driver.implicitly_wait(30)

        morebutton = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        achains = ActionChains(driver)
        achains.move_to_element(morebutton).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()





        time.sleep(20)



t1 = hover()
t1.hover_01()