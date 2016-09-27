# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

from datetime import datetime
from pymongo import MongoClient

import threading

GOOGLE_NEWS_URL = 'https://news.google.com.mx/'
CUSTOME_TARGET = 'www.eluniversal.com'

def set_spider(article):
	title = article.find('span', {'class': 'titletext'}).getText()
	url = article.find('a').get('href')
	print url


def scrap_site():
	request = requests.get(GOOGLE_NEWS_URL)
	if request.status_code == 200:
		soup = BeautifulSoup(request.text, "html.parser")

		if soup is not None:
			articles = soup.find_all('h2', {'class': 'esc-lead-article-title'})
			for article in articles:
				sender = threading.Thread(name='set_spider', target=set_spider, args=(article,))
				sender.start()

if __name__ == '__main__':
	scrap_site()
	