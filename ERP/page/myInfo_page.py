import time
from selenium.webdriver.common.by import By


class MyInfo_Page():

    def __init__(self, driver):
        self.driver = driver


    def emergency_contact_add(self, name, relationship, telephone):
        # open my info page
        my_info = self.driver.find_element(By.LINK_TEXT, 'My Info')
        my_info.click()
        time.sleep(2)

        # Open emergency contact page
        emergency_contact = self.driver.find_element(By.LINK_TEXT, 'Emergency Contacts')
        emergency_contact.click()
        time.sleep(2)

        # Add button click
        add_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button')
        add_button.click()
        time.sleep(2)

        ####xpath finding format - "XPath=//tagname[@attribute='value']"

        # input name
        name_field = self.driver.find_element(By.XPATH, '//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]')
        name_field.send_keys(name)
        time.sleep(2)

        # input relationship
        relationship_field = self.driver.find_element(By.XPATH, '//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]')
        relationship_field.send_keys(relationship)
        time.sleep(2)

        # input telephone
        telephone_field = self.driver.find_element(By.XPATH, '//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]')
        telephone_field.send_keys(telephone)
        time.sleep(2)

        # save inputs
        save_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        save_button.click()
        time.sleep(2)


