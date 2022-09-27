##iteration in test schedule a test

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
import smtplib
from email.message import EmailMessage


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.com/")
driver.implicitly_wait(30)
driver.find_element(By.XPATH, "//input[contains(@id, 'searchtextbox')]").send_keys("Samsung phones")
driver.find_element(By.XPATH,"//input[contains(@value, 'Go')]").click()
driver.find_element(By.XPATH,"//span[text()='SAMSUNG']").click()
phonenames = driver.find_elements(By.XPATH, "//span[contains(@class, 'a-size-medium a-color-base a-text-normal')]")
prices = driver.find_elements(By.XPATH, "//span[contains(@class, 'price-whole')]")

myphone = []
myprice = []

for phone in phonenames:
    #print(phone.text)
    myphone.append(phone.text)

print("*"*50)

for price in prices:
    #print(price.text)
    myprice.append(price.text)

finalList = zip(myphone, myprice)
#for data in list(finalList):
    #print(data)

print("PART01")
###########################################################################


###store data in a excel file with openpyXL
###object of workbook class
wb = Workbook()
wb['Sheet'].title = 'Samsung Data'
#sheet01 of workbook
sheet1 = wb.active
sheet1.append(['Name', 'Price'])


for x in list(finalList):
    sheet1.append(x)

wb.save("FinalRecords.xlsx")

print("PART02")



############################################################################

msg = EmailMessage()
msg['Subject'] = 'Amazon Scrapping Report'
msg['From'] = 'Nipun Ferdous'
msg['To'] = 'nipun.ferdous@bracmail.net'
#msg.set_content("The scrapping test file is attached")
#read text file

with open('EmailTemplate.txt') as myfile:
    email_data = myfile.read()
    msg.set_content(email_data)


with smtplib.SMTP_SSL('smtp.office365.com', 587) as sending_server:
    sending_server.login("nipun.ferdous@bracmail.net", "Duv87153")
    sending_server.send_message(msg)


print('Email Sent!')




#driver.quit()

