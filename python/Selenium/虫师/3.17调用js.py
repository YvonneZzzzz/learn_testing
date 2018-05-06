#coding = utf-8

from selenium import webdriver
import os,time

driver =  webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('3.17js.html')
driver.get(file_path)

#通过js隐藏选中的元素#第一种方法
#隐藏文字信息
#execute_script() 接口用来调用 js 代码
driver.execute_script('$("#tooltip").fadeOut();')
time.sleep(3)

#隐藏按钮
button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut',button)
time.sleep(3)

