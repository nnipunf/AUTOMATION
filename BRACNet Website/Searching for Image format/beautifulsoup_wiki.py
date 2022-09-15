from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Bobby_Flay"

result = requests.get(url)
#print(result.text)

doc = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify())


locators = doc.find_all('img')
for item in locators:
    print(item['src'])
print(locators)


