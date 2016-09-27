# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

from datetime import datetime
from pymongo import MongoClient

import threading

GOOGLE_NEWS_URL = 'https://news.google.com.mx/'
CUSTOME_TARGET = 'www.eluniversal.com'

def get_beautiful_soup(url):
	request = requests.get(url)
	if request.status_code == 200:
		return BeautifulSoup(request.text, "html.parser")

def set_spider(article):
	title = article.find('span', {'class': 'titletext'}).getText()
	url = article.find('a').get('href')
	if CUSTOME_TARGET in url:
		soup = get_beautiful_soup(url)
		if soup is not None:

			container = soup.find('div', {'class': 'field field-name-body field-type-text-with-summary field-label-hidden'})
			paragraphs = container.find_all('p')
			
			#print " ".join( paragraphs )
			#print type(paragraphs)
			final_article = ""
			for paragraph in paragraphs:
				final_article = "{} {}".format(final_article, paragraphs)

			#print "\n\n\n\n\n"
			#print type(final_article)
			"""
			author = soup.find('div', {'class': 'field-item even'})
			if author is not None:
				print author.getText()
			else:
				print url
			"""

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
	