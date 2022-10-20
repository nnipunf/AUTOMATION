import time

from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login_orange(self, username, password):
        username_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        password_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")

        username_field.clear()
        username_field.send_keys(username)
        time.sleep(2)

        password_field.clear()
        password_field.send_keys(password)
        time.sleep(2)

        login_button.click()
        time.sleep(4)
