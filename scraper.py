import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Fall_armyworm'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='mw-content-text')
tab = soup.find("table", {"class": "infobox biota"})

print(tab.prettify())
