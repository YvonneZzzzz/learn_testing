#!/usr/bin/env python
# -*- coding: utf-8 -*-

# try:
#     open("abc.txt",'r')
# except IOError：
#     pass
#=================================#
# a=10
# b=0
# try:
#     c=b/a
#     print(c)
# except(IOError, ZeroDivisionError) as x:
#     print(x)
# else:
#     print("no error")
# print("done")
#=================================#
# a=10
# b=0
# try:
#     c=a/b
#     print(c)
# except ZeroDivisionError as e:
#     print (e)
# print("done")
#=================================#
# try:
#     print("try...")
#     r = 10/0
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally...')
# print('END')
#=================================#
# try:
#     print("try...")
#     r = 10/2
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally...')
# print('END')
#=================================#
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#捕捉百度输入框异常
try:
    driver.find_element_by_id('kwss').send_keys("selenium")
    driver.find_element_by_id('su').click()
except:
    driver.get_screenshot_as_file("D:/error_png.png")
driver.quit()
