import requests
from bs4 import BeautifulSoup

#empty list
urls = []


def scrape(site):
    #getting request from url
    r = requests.get(site)

    #converting the text
    s = BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("a"):
        href = i.attrs['href']
        if href.startswith("/"):
            site = site + href
            if site not in urls:
                urls.append(site)
                print(site)
                #calling the getdata function itself
                #generally called recurssion
                scrape(site)


#main function
if __name__ == "__main__":
    site = "https://www.daraz.com.bd/"
    scrape(site)
