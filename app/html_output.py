#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

class HtmlOutputer(object):

	def __init__(self):
		self.datas = []

	def collect_data(self, data):
		if data is None:
			return
		
		self.datas.append(data)
		
	def output_html(self):
		
		conn = sqlite3.connect('used_card.db')
		cursor = conn.cursor()
		cursor.execute("select count(*) from sqlite_master where type = 'table' and name = 'agent_phone'")
		if cursor.fetchone()[0] == 0:
			cursor.execute("create table agent_phone (id integer primary key autoincrement, title varchar(255), price float, url varchar(255))")
		for data in self.datas:
			cursor.execute("insert into agent_phone (title, price, url) values (?, ?, ?)", (data['title'], data['price'], data['url']))
			cursor.rowcount
			
		cursor.close()
		conn.commit()
		conn.close()
		self.datas = []