import time
from selenium.webdriver.common.by import By


class MyInfo_Page():

    def __int__(self, driver):
        self.driver = driver


    def emergency_contact_add(self):
        # open my info page
        my_info = self.driver.find_element(By.LINK_TEXT, 'My Info')
        my_info.click()
        time.sleep(2)

        # Open emergency contact page
        emergency_contact = self.driver.find_element(By.LINK_TEXT, 'Emergency Contacts')
        emergency_contact.click()
        time.sleep(2)

