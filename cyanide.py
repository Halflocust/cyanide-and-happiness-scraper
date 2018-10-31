import requests
import bs4 as bs 
import os
import urllib.request




if not os.path.exists("comics"):
	os.makedirs("comics")

res = requests.get("http://explosm.net/comics/latest")
soup = bs.BeautifulSoup(res.text,"html.parser")
link = soup.find(id = "main-comic")["src"]
url = "http:" + link
number = 1
prev_page_url = True

# while not url

while prev_page_url:
	print("Getting cartoon # {}".format(number))
	try:
		urllib.request.urlretrieve(url,"comics/comic-{}.png".format(number))
	except:
		pass
	number += 1
	prev_page_url = soup.find(class_="nav-previous ")["href"]
	prev_url = "http://explosm.net" + prev_page_url
	res = requests.get(prev_url)
	res.raise_for_status()
	soup = bs.BeautifulSoup(res.text,"html.parser")
	link = soup.find(id = "main-comic")["src"]
	url = "http:" + link



