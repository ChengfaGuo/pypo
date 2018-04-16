# -*- coding: utf-8 -*-

from selenium import webdriver
from baidu_Page import BaiduPage, BaiduNews
import unittest

class BaiduTest(unittest.TestCase):

	def setUp(self):
		self.dr = webdriver.Chrome()

	def test_baidu_search(self):
		b_page = BaiduPage(self.dr)
		b_page.open()
		b_page.search_input('page object')
		b_page.search_button()

	def test_baidu_news_search(self):
		news_page = BaiduNews(self.dr)
		news_page.open()
		news_page.search_news_input('海南')
		news_page.search_news_button()
		news_page.search_result()


	def tearDown(self):
		self.dr.quit()

if __name__ == '__main__':
	unittest.main()