#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
	
	def _get_new_urls(self, soup):
		new_urls = set()
		
		links = soup.find_all('h2', class_ ="title")
		
		for link in links:
			new_url = link.find('a')['href']
#			
			new_urls.add(new_url)
		return new_urls
		
	def _get_new_data(self, page_url, soup):
		res_data = {}
		
		res_data['url'] = page_url

		phone = soup.find('p', class_="phone-num").get_text()
		res_data['title'] = phone
		
		res_data['price'] = float('0')
		
		return res_data
	
	def parse_urls(self, html_cont):
		if html_cont is None:
			return
		# print(html_cont)
		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		new_urls = self._get_new_urls(soup)
		return new_urls 
		
	def parse_data(self, page_url, html_cont):
		if html_cont is None:
			return
		
		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		new_data = self._get_new_data(page_url, soup)
		
		return new_data