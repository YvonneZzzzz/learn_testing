#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #badiu_read_data.py
# from selenium import webdriver
# import os,time

# source = open("G:\\Git\\python\\4.3data.txt","r")
# #readlines方法是逐行的读取文件内容
# values = source.readlines()
# source.close()

# #执行循环
# for serch in values:
#     browser = webdriver.Chrome()
#     browser.get("http://www.baidu.com")
#     browser.find_element_by_id("kw").send_keys(serch)
#     browser.find_element_by_id("su").click()
#     time.sleep(3)
#     browser.quit()

# #登录参数化(读取txt文件)
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchAttributeException
# import time,os,unittest

# source = open("G:\\Git\\python\\4.3username.txt")
# un = source.read()#读取用户名
# source.close()

# source2 = open("G:\\Git\\python\\4.3password.txt")
# pw = source2.read()#读取密码
# source2.close()

# def login(self):
#     driver = self.driver
#     driver.maximize_window()
#     driver.find_element_by_id("user_name").clear()
#     driver.find_element_by_id("user_name").send_keys(un)
#     driver.find_element_by_id("user_pwd").clear()
#     driver.find_element_by_id("user_pwd").send_keys(pw)
#     driver.find_element_by_id("dl_an_submit").click()
#     time.sleep(3)


# #登陆参数化（函数）
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchAttributeException
# import unittest,time
# #导入函数
# import userinfo

# #通过两个变量，来接受调用函数获得用户名&密码
# us,pw = userinfo.fun()
# #打印两个变量
# print(us,pw)

# def login(self):
#     driver = self.driver
#     driver.maximize_window()
#     driver.find_element_by_id("user_name").clear()
#     driver.find_element_by_id("user_name").send_keys(un)
#     driver.find_element_by_id("user_pwd").clear()
#     driver.find_element_by_id("user_pwd").send_keys(pw)
#     driver.find_element_by_id("dl_an_submit").click()
#     time.sleep(3)

# # def fun(un='testing',pw=123456):
# #     print("success")
# #     return un,pw

# #登陆参数化（读取字典）
#创建字典用大括号，数据由 key/value 键值对组成，keys()方法返回字典中的键列表。
#values()返回字典中的值列表，items()返回（key，value）元组。
# >>> data = {'abc':'123','def':'456'}
# >>> print data
# {'abc': '123', 'def': '456'}
# >>> data.keys()
# ['abc', 'def']
# >>> data.values()
# ['123', '456']
# >>> data.items()
# [('abc', '123'), ('def', '456')]
# import userinfo
# #获取字典数据
# info = userinfo.zidian()
# #通过items()循环读取元组（键/值对）
# for us,pw in info.items():
#     print(us,pw)
#     # print(pw)

#表单参数化（csv）
import csv
#读取本地csv文件
my_file='G:\\Git\\python\\userinfo.csv'
data = csv.reader(file(my_file,'rb'))
# with open('userinfo.csv','rb') as csvfile:
#     data = csv.reader(csvfile,dialect ='excel')
#循环输出每一行信息
for user in data:
    print(user[0])
    print(user[1])
    print(user[2])
    print(user[3])
