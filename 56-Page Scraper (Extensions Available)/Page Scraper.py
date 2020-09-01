#Scrap all links from pythonforbeginners.com
from bs4 import BeautifulSoup
import requests

url = "https://www.pythonforbeginners.com"

page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")

links=list(map(lambda a:a["href"],soup.find_all("a",href=True)))
for link in links:
    print(link)
