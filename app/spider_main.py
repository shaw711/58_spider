#!/usr/bin/env python3
# -*- conding: utf-8 -*-

import html_downloader, html_output, html_parser
import time

class SpiderMain(object):
	def __init__(self):
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_output.HtmlOutputer()
		
	def craw(self, root_url):
		for i in range(1, 71):
			full_url = root_url + str(i)
			print('craw :', i, full_url)
			html_page_cont = self.downloader.download(full_url)
			new_urls = self.parser.parse_urls(html_page_cont)
			for url in new_urls:
				print('craw', i, url)
				try:
					html_cont = self.downloader.download(url)
					data = self.parser.parse_data(url, html_cont)
					print(data)
					self.outputer.collect_data(data)
				except:
					print('craw fail')
			
			self.outputer.output_html()
			time.sleep(2)
	
if __name__ == '__main__':
	root_url = 'http://gz.58.com/ershouche/pn'
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
	