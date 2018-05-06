#coding = utf-8

from selenium import webdriver
import os,time

driver = webdriver.Chrome()

#打开上传文件页面
file_path = 'file:///' + os.path.abspath('3.15upload_file.html')
driver.get(file_path)
time.sleep(2)

#定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('G:/FFos 架构/ce.txt')
time.sleep(2)

driver.quit()