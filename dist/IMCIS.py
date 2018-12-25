#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 18:03
# @Author  : Zhangyp
# @File    : IMCIS_无效.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from locust import TaskSet,task
from locust import HttpLocust
from gettoken import get_token
from readini import *

# 请求头信息的数据类型设置为x-www-form-urlencoded
h1 = {'Content-Type': 'application/x-www-form-urlencoded'}

# 获取token的头信息
h2 = {'Authorization':get_token()}


class IMCISTask(TaskSet):
	def on_start(self): #初始化函数每次执行任务前只执行一次
		print('test start...')
	
	#获取token
	@task(int(s['token_w']))
	def gettoken(self):
		api = 'token_api'
		title = api.split('_')[0]
		payload = s['token_body']
		# payload = 'input={"organizationID":"12330122MB1856687C","account":"zyp","password":"zyp","rememberMe":false}'
		logging.info('test %s: %s' % (api, s[api]))
		response = self.client.post(s[api], data = payload, name=title)
		logging.info('%s result:%s' % (title,response.status_code))
	
	#登录
	@task(int(s['login_w']))
	def login(self):
		api = 'login_api'
		title = api.split('_')[0]
		logging.info('test %s: %s' % (api, s[api]))
		response = self.client.get(s[api], headers=h2, name=title)
		logging.info('%s result:%s' % (title, response.status_code))
	
	# 检查信息查询
	@task(int(s['checklist_w']))
	def getcheckinfolist(self):
		api = 'checklist_api'
		title = api.split('_')[0]
		logging.info('test %s: %s' % (api, s[api]))
		response = self.client.get(s[api], headers=h2, name=title)
		logging.info('%s result:%s' % (title, response.status_code))
	
	# 获取预设方案
	@task(int(s['getpreset_w']))
	def getpreset(self):
		api = 'getpreset_api'
		title = api.split('_')[0]
		logging.info('test %s: %s' % (api, s[api]))
		response = self.client.get(s[api], headers=h2, name=title)
		logging.info('%s result:%s' % (title, response.status_code))
	
	# 获取结果状态
	@task(int(s['getdocstatus_w']))
	def getdocstatus(self):
		api = 'getdocstatus_api'
		title = api.split('_')[0]
		logging.info('test %s: %s' % (api, s[api]))
		response = self.client.get(s[api], headers=h2, name=title)
		logging.info('%s result:%s' % (title, response.status_code))
	
	# 获取文字报告
	@task(int(s['getreport_w']))
	def getreport(self):
		api = 'getreport_api'
		title = api.split('_')[0]
		logging.info('test %s: %s' % (api, s[api]))
		response = self.client.get(s[api], headers=h2, name=title)
		logging.info('%s result:%s' % (title, response.status_code))
	
	# 获取图文报告
	@task(int(s['getdoc_w']))
	def getdoc(self):
		api = 'getdoc_api'
		title = api.split('_')[0]
		logging.info('test %s: %s' % (api, s[api]))
		response = self.client.get(s[api], headers=h2, name=title)
		logging.info('%s result:%s' % (title, response.status_code))
		
	# 获取相关检查
	@task(int(s['getrecordexam_w']))
	def getrecordexam(self):
		api = 'getrecordexam_api'
		title = api.split('_')[0]
		logging.info('test %s: %s'%(api,s[api]))
		response = self.client.get(s[api], headers = h2, name = title)
		logging.info('%s result:%s'%(title,response.status_code))
	
	
	"""以下是模拟用户操作行为，会调一系列的API"""
	@task(0)
	def Userbehavior(self):
		logging.info('test User behavior')
		#先获取token
		payload = 'input={"organizationID":"12330122MB1856687C","account":"zyp","password":"zyp","rememberMe":false}'
		response = self.client.post(s['token_api'], data=payload, name='token')
		logging.info('gettoken result:%s' % response.status_code)
		#再登录
		response = self.client.get(s['login_api'], headers=h2, name='login')
		logging.info('login result:%s' % response.status_code)
		#最后检查信息查询
		response = self.client.get(s['checklist_api'], headers=h2, name='getcheckinfolist')
		logging.info('getcheckinfolist result:%s' % response.status_code)
		

class IMCISUser(HttpLocust):
	task_set = IMCISTask
	host = s['host']
	min_wait = int(s['min_wait'])
	max_wait = int(s['max_wait'])
	
	