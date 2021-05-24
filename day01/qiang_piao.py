# -*- coding: utf-8 -*-
'''
@Time    : 2021/5/24 0024 下午 12:06
@Author  : 大白
@File    : qiang_piao.py
'''


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")

driver.find_element_by_id("fromStationText").click()