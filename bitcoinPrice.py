from bs4 import BeautifulSoup
import requests
import datetime

URL = "https://www.google.com/search?q="
QUERY = "bitcoin+price+in+euro"

# Time Methods #
time = datetime.datetime.now()
current_time = time.strftime("%c")

# Scraping Method # 
def scrape():
	r = requests.get(URL+QUERY)
	s = BeautifulSoup(r.text, 'html.parser')
	ans = s.find("div", class_ ="BNeawe iBp4i AP7Wnd")
	return ans.text

# DB info #
price_bitcoin = scrape()
num_price = price_bitcoin.strip(" Euro") # later use

db_info = current_time + ": " + price_bitcoin
print(db_info)

# Write to DB #
f = open("bitcoinPrice.txt", "a")
f.write(db_info+"\n")
f.close()