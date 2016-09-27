# -*- coding: utf-8 -*-

#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

GOOGLE_NEWS_URL = 'https://news.google.com.mx/'

def scrap_site():
	request = requests.get(GOOGLE_NEWS_URL)
	if request.status_code == 200:
		soup = BeautifulSoup(request.text, "html.parser")

		if soup is not None:
			articles = soup.find_all('h2', {'class': 'esc-lead-article-title'})
			for article in articles:
				title = article.find('span', {'class': 'titletext'}).getText()
				print title

if __name__ == '__main__':
	scrap_site()
