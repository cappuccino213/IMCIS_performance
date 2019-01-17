#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 10:10
# @Author  : Zhangyp
# @File    : run.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import os
from readini import *
import webbrowser
from time import sleep
import threading


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
	try:
		sleep(2)
		logging.info('正在打开locust测试控制台...')
		try:
			webbrowser.register(find_browser(s['browserpath']), None, webbrowser.BackgroundBrowser(s['browserpath']))
			webbrowser.get(find_browser(s['browserpath'])).open('http://localhost:%s'%int(s['port']), new=1, autoraise=True)
		except Exception as e:
			logging.info('打开浏览器失败,', str(e))
	except Exception as e:
		logging.info('浏览器路径未配置，请自行打开浏览器访问：http://localhost:%s ,原因:' % int(s['port']),str(e))


# cmd中运行locust
def locust():
	log = s['iflogsv']
	cmd = 'locust -f %s\IMCIS.py -P %s %s'%(os.getcwd(), int(s['port']), log)
	logging.info('运行命令：%s' % cmd)
	p = os.popen(cmd)
	print(p.read())
	

def main():
	t1 = threading.Thread(target=locust)
	t2 = threading.Thread(target=open_browser)
	t1.start()
	t2.start()


if __name__ == '__main__':
	main()
