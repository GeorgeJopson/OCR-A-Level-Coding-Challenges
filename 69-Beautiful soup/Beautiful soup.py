#Scrap all links from pythonforbeginners.com
from bs4 import BeautifulSoup
import requests

url = "https://www.bbc.co.uk/news"

page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")

newsArticles=list(map(lambda news:news.contents,soup.find_all("h3")))
def flattenList(inputList):
    if(len(inputList)==1):
        return inputList[0]
titles=list(map(flattenList,newsArticles))

for title in titles:
    print(title)
