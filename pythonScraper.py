from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://en.wikipedia.org/wiki/Fall_armyworm'

page = uReq(my_url)
page_html = page.read()
page.close()

page_soup = soup(page_html, "html.parser")

tables = page_soup.findAll("div", {"class":"mw-parser-output"})


print(len(tables))

print(tables)