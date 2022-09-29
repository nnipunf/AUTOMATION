from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class Alert():
    def multiplewindow_01(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/windows")
        driver.implicitly_wait(30)

        parent_window = driver.current_window_handle
        print(parent_window)

        driver.find_element(By.LINK_TEXT, 'Click Here').click()
        #time.sleep(10)

        all_windows = driver.window_handles
        print(all_windows)

        #switch to child window
        for child in all_windows:
            if child not in parent_window:
                driver.switch_to.window(child)
                print("this is child window: "+driver.title)
        #time.sleep(5)

        # switch to parent window
        for child in all_windows:
            if child not in parent_window:
                driver.switch_to.window(parent_window)
                print("this is parent window: "+driver.title)

        #to close one window
        driver.close()

        time.sleep(20)
        

t1 = Alert()
t1.multiplewindow_01()