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
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',level=logging.DEBUG)
#日志启用开关,注释掉即开启日志
# logging.disable(logging.DEBUG)

cf = configparser.ConfigParser()
cf.read('config.ini',encoding='utf-8')
#获取配置节点列表
section = cf.sections()

"""将获取到的各节点的key-value放入字典，便于读取"""
s = {}
for i in range(len(section)):
	kv = cf.items(section[i])
	for j in range(len(kv)):
		s[kv[j][0]]=kv[j][1]

# print(d)