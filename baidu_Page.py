# -*- coding: utf-8 -*-

class BasePage(object):
	
	def __init__(self, driver, base_url = '.baidu.com'):
		self.driver = driver
		self.base_url = base_url

	def _open(self, url):
		url_ = 'https://' + url + self.base_url
		self.driver.get(url_)

	def open(self):
		self._open(self.url)

	def search_result(self):
		results = self.driver.find_elements_by_class_name('c-title')
		for result in results:
			print(result.text)

		

class BaiduPage(BasePage):

	url = 'www'

	
	# 搜索关键字
	def search_input(self, search_key):
		self.driver.find_element_by_id('kw').send_keys(search_key)

	# 搜索按钮
	def search_button(self):
		self.driver.find_element_by_id('su').click()

class BaiduNews(BasePage):

	url = 'news'

	
	# 搜索关键字
	def search_news_input(self, search_key):
		self.driver.find_element_by_id('ww').send_keys(search_key)

	# 搜索按钮
	def search_news_button(self):
		self.driver.find_element_by_id('s_btn_wr').click()