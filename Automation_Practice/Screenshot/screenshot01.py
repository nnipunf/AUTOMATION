from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class scrnshot():
    def scsht_01(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("http://202.168.254.37:8081/cdr_data/")
        driver.implicitly_wait(30)

        driver.get_screenshot_as_file(r'G:\NIPUN_BRACNET\Software QA\AUTOMATION\Automation_Practice\Screenshot\ScreenShotFiles\image02.png')
        time.sleep(5)



t1 = scrnshot()
t1.scsht_01()