#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 16:24
# @Author  : Zhangyp
# @File    : readini.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import configparser
import logging

logging.basicConfig(level = logging.DEBUG, filemode = 'a',filename = 'run.log' ,format = ('''[时间]:%(asctime)s
[线程]:%(thread)s
[级别]:%(levelname)s
[路径]:%(pathname)s
[函数]:%(funcName)s
[行号]:%(lineno)d
[信息]:%(message)s
------------------
'''))
#日志启用开关,注释掉即开启日志
# logging.disable(logging.DEBUG)

# 处理BOM字符（当配置文件被记事本编辑过后，会插入一个bom头）
BOM  = b'\xef\xbb\xbf'
with open('config.ini','r+b') as f:
    if BOM == f.read(3):
        content = f.read()
        f.seek(0)
        f.write(content)
        f.truncate()

cf = configparser.ConfigParser()
cf.read('config.ini',encoding='utf-8')
# 获取配置节点列表
section = cf.sections()

'''将获取到的各节点的key-value放入字典，便于读取'''
s = {}
for i in range(len(section)):
	kv = cf.items(section[i])
	for j in range(len(kv)):
		s[kv[j][0]] = kv[j][1]

# print(s)