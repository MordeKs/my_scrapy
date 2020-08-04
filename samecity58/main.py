# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2020/8/4 15:55
@Author  : Morde
@Software: PyCharm
@Description:
"""

from scrapy.cmdline import execute

execute(['scrapy','crawl','tongcheng','-o','items.json'])