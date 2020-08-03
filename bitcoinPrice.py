from bs4 import BeautifulSoup
import requests

URL = "https://www.google.com/search?q="
QUERY = "bitcoin+price+in+euro"

def scrape():
	r = requests.get(URL+QUERY)
	s = BeautifulSoup(r.text, 'html.parser')
	ans = s.find("div", class_ ="BNeawe iBp4i AP7Wnd")
	return ans.text

price = scrape()
print(price)