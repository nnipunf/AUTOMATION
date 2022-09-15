##itration in test schedule a test

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.com/")
driver.implicitly_wait(30)
driver.find_element(By.XPATH, "//input[contains(@id, 'searchtextbox')]").send_keys("Samsung phones")
driver.find_element(By.XPATH,"//input[contains(@value, 'Go')]").click()
driver.find_element(By.XPATH,"//span[text()='SAMSUNG']").click()
phonenames = driver.find_elements(By.XPATH, "//span[contains(@class, 'a-size-medium a-color-base a-text-normal')]")
prices = driver.find_elements(By.XPATH, "//span[contains(@class, 'price-whole')]")

for phone in phonenames:
    print(phone.text)
print("*"*50)

for price in prices:
    print(price.text)

driver.quit()