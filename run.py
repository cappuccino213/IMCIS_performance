#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 10:10
# @Author  : Zhangyp
# @File    : run.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""运行locust程序，自动打开浏览器测试地址"""
import os
from readini import *
import webbrowser
from time import sleep
import threading

# cmd中运行locust
def locust():
	log = s['iflogsv']
	cmd = 'locust -f %s\IMCIS.py -P %s %s'%(os.getcwd(),int(s['port']),log)
	logging.info('运行命令：%s' % cmd)
	p = os.popen(cmd)
	print(p.read())

# 查找浏览器的路径
def find_browser(path):
	if 'firefox' in path:
		return 'firefox'
	elif 'chrome' in path:
		return 'chrome'
	else:
		return False

# 打开浏览器
def open_browser():
	sleep(2)
	logging.info('正在打开locust测试控制台...')
	try:
		webbrowser.register(find_browser(s['browserpath']), None, webbrowser.BackgroundBrowser(s['browserpath']))
		webbrowser.get(find_browser(s['browserpath'])).open('http://localhost:%s'%int(s['port']), new=1, autoraise=True)
	except Exception as e:
		logging.info('打开浏览器失败:', str(e))
		
t = threading.Thread(target=open_browser)


if __name__== '__main__':
	if find_browser(s['browserpath']) != False:
		t.setDaemon(True)
		t.start()
	else:
		logging.info('浏览器路径未配置，请自行打开浏览器访问：http://localhost:%s' % int(s['port']))
	locust()