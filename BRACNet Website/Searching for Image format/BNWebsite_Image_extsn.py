from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text

print('___HOMEPAGE___')
htmldata = getdata("https://bracnet.vercel.app/")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])


######################################################################################################
print('___CORPORATE INTERNET___')
htmldata = getdata("https://bracnet.vercel.app/corporate-internet")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])


######################################################################################################
print('___DATA CONNECTIVITY___')
htmldata = getdata("https://bracnet.vercel.app/data-connectivity")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___HOME INTERNET CONNECTIVITY___')
htmldata = getdata("https://bracnet.vercel.app/home-internet")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___software-development___')
htmldata = getdata("https://bracnet.vercel.app/software-development")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___cyber-security___')
htmldata = getdata("https://bracnet.vercel.app/cyber-security")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___network-security___')
htmldata = getdata("https://bracnet.vercel.app/network-security")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___surveillance___')
htmldata = getdata("https://bracnet.vercel.app/surveillance")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___voice-and-sms___')
htmldata = getdata("https://bracnet.vercel.app/voice-and-sms")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___network-infrastructure___')
htmldata = getdata("https://bracnet.vercel.app/network-infrastructure")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___cloud-solutions___')
htmldata = getdata("https://bracnet.vercel.app/cloud-solutions")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___iot-solutions___')
htmldata = getdata("https://bracnet.vercel.app/iot-solutions")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___web-hosting___')
htmldata = getdata("https://bracnet.vercel.app/web-hosting")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___email-hosting___')
htmldata = getdata("https://bracnet.vercel.app/email-hosting")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___vps___')
htmldata = getdata("https://bracnet.vercel.app/vps")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___business-suite___')
htmldata = getdata("https://bracnet.vercel.app/business-suite")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])


######################################################################################################
print('___request-for-quote___')
htmldata = getdata("https://bracnet.vercel.app/request-for-quote")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___about-us___')
htmldata = getdata("https://bracnet.vercel.app/about-us")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___board-of-directors___')
htmldata = getdata("https://bracnet.vercel.app/board-of-directors")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___leadership-team___')
htmldata = getdata("https://bracnet.vercel.app/leadership-team")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___contact___')
htmldata = getdata("https://bracnet.vercel.app/contact")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___career___')
htmldata = getdata("https://bracnet.vercel.app/career")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___blog___')
htmldata = getdata("https://bracnet.vercel.app/blog")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___gallery___')
htmldata = getdata("https://bracnet.vercel.app/gallery")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

######################################################################################################
print('___news-events___')
htmldata = getdata("https://bracnet.vercel.app/news-events")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])






