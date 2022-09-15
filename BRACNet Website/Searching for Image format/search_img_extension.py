from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata("https://en.wikipedia.org/wiki/Main_Page")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])


######################################################################################################
"""
class Firefox_WDM():

    global driver
    global dr

    def img_ext(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.implicitly_wait(30)
        driver.get('https://www.aci-bd.com/')


        for element in driver.find_element_by_tag_name('img'):
            print(element.text)
            print(element.tag_name)


        for element in driver.find_element(By.TAG_NAME, 'img'):
            print(element.text)
            print(element.tag_name)


        attr_name = driver.find_element(By.XPATH, '/html/body/div/header/section[1]/div/div[1]/a/img').get_attribute("src")
        print(attr_name)


obj = Firefox_WDM()
obj.img_ext()

"""

##################################################################################################

