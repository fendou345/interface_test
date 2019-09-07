# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  : lileilei
# @Site    : 
# @File    : testHttp.py
from common.test_requests import requ
reques=requ()
class TestApi(object):
	def __init__(self, method, url, header, param):
		self.url = url
		self.method = method
		self.header = header
		self.param = param
	def testapi(self):
		if self.method=='post':
			self.response = reques.post(url=self.url, params=self.param, header=self.header)
		elif self.method=="get":
			self.response = reques.get(url=self.url, params=self.param, header=self.header)
		return self.response
	def getJson(self):
		json_data = self.testapi()
		return json_data