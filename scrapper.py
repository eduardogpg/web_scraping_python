# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

from datetime import datetime
from pymongo import MongoClient

import threading

GOOGLE_NEWS_URL = 'https://news.google.com.mx/'
CUSTOME_TARGET = 'www.eluniversal.com'

class Article(object):
	def __init__(self, title, url, author, content):
		self.title = title
		self.url = url
		self.author = author
		self.content = content
		self.release_date = datetime.now()

	def get_document(self):
		return {'title': self.title, 'url': self.url, 
						'author': self.author, 'content': self.content, 'release_date': self.release_date }

def get_beautiful_soup(url):
	request = requests.get(url)
	if request.status_code == 200:
		return BeautifulSoup(request.text, "html.parser")

def set_spider(article, db):
	title = article.find('span', {'class': 'titletext'}).getText()
	url = article.find('a').get('href')
	if CUSTOME_TARGET in url:
		soup = get_beautiful_soup(url)
		if soup is not None:
			author = soup.find('div', {'class': 'field-item even'}).getText()
			container = soup.find('div', {'class': 'field field-name-body field-type-text-with-summary field-label-hidden'})
			paragraphs = container.find_all('p')
			content_article = ""
			for paragraph in paragraphs:
				content_article = "{a}\n{p}".format(a=content_article, p=paragraph)
			
			db.articles.insert_one({"title": title, "url": url, "author": author, "content": content_article})

def scrap_site():
	soup = get_beautiful_soup(GOOGLE_NEWS_URL)#Creamos una funcion que nos permita abstraer esto
	client = MongoClient('localhost', 27017)
	db = client['taller']

	if soup is not None:
		articles = soup.find_all('h2', {'class': 'esc-lead-article-title'})
		for article in articles:
			sender = threading.Thread(name='set_spider', target=set_spider, args=(article, db))
			sender.start()

if __name__ == '__main__':
	scrap_site()
	print "Hola mundo"
	