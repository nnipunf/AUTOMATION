from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class Alert():
    def alert_automation_01(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.implicitly_wait(30)

        #normal alert
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button').click()
        driver.switch_to.alert.accept() #clicking an ok button
        #time.sleep(5)

        #confirmation alert
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click()
        driver.switch_to.alert.dismiss() #clicking a cancle button
        #time.sleep(5)

        # prompt alert
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
        driver.switch_to.alert.send_keys('Test Automation')
        driver.switch_to.alert.accept()
        time.sleep(5)
        

test01 = Alert()
test01.alert_automation_01()
