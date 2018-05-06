#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import  webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.back()   #浏览器后退
driver.forward()    #浏览器前进
driver.quit()
driver.refresh() #手动刷新
driver.set_window_size(480,800) #控制浏览器显示尺寸

driver.find_element_by_id("kw").clear()  #清除文本
driver.find_element_by_id("kw").send_keys(u"模拟按键输入")
driver.find_element_by_id("kw").click()     #点击元素
driver.find_element_by_id("kw").submit()     #提交搜索框内容

size = driver.find_element_by_id("kw").size     #获得输入框尺寸
text = driver.find_element_by_id("kw").text     #返回信息
attribute = driver.find_element_by_id("kw").get_attribute('type')       #返回元素属性id/name/type
result = driver.find_element_by_id("kw").is_displayed()     #返回元素结果是否可见，true false

# ----------4.4鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
test = driver.find_element_by_id("kw")
ActionChains(driver).context_click(test).perform()  #鼠标右击
ActionChains(driver).move_to_element(test).perform()  #鼠标悬停
ActionChains(driver).double_click(test).perform()  #鼠标双击
target = driver.find_element_by_id("su")
ActionChains(driver).drag_and_drop(test, target).perform()  #鼠标拖放

# ----------4.5键盘事件
from selenium.webdriver.common.keys import Keys
dirver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE) #删除键
dirver.find_element_by_id("kw").send_keys(Keys.SPACE) #空格键
dirver.find_element_by_id("kw").send_keys(Keys.TAB) #TAB键
dirver.find_element_by_id("kw").send_keys(Keys.ESCAPE) #Esc键
dirver.find_element_by_id("kw").send_keys(Keys.ENTER)
dirver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a') #全选crtl+a
dirver.find_element_by_id("kw").send_keys(Keys.CONTROL,'c')
dirver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
dirver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
dirver.find_element_by_id("kw").send_keys(Keys.F1) #键盘F1

# ----------4.6获得验证信息
title = driver.title    #获得当前页面的标题
now_url = driver.current_url    #当前页面的url

# ----------4.7设置元素等待
#----- 显式等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((BY.ID,"kw"))) #判断元素是否存在
element = WebDriverWait(driver,10).until(lambda driver : driver.find_element_by_id("kw"))
    # WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
    # driver - WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)
    # timeout - 最长超时时间，默认以秒为单位
    # poll_frequency - 休眠时间的间隔（步长）时间，默认为 0.5 秒
    # ignored_exceptions - 超时后的异常信息，默认情况下抛 NoSuchElementException 异常。
    # until(method, message=’’)调用该方法提供的驱动程序作为一个参数，直到返回值不为 False。
    # until_not(method, message=’’)调用该方法提供的驱动程序作为一个参数，直到返回值为 False
# -----隐式等待
driver.implicitly_wait(10)  #默认单位为秒
# -----sleep休眠
from time import sleep
sleep(3)

# ----------4.8定位一组元素
find_elements_by_id()
find_elements_by_name()
find_elements_by_class_name()
find_elements_by_tag_name()
find_elements_by_link_text()
find_elements_by_partial_link_text()
find_elements_by_xpath()
find_elements_by_css_selector()
# ----打开本地的html文件
import os
file_path = 'file:///' + os.path.abspath('checkbox.html')   #path.abspath()方法获得当前路径下的文件
# ----获取列表中的一个元素
pop() #默认获取一组元素中的最后一个
pop(0)  #默认获取一组元素中的第一个
pop(1)  #默认获取一组元素中的第二个

# ----------4.9多表单切换
driver.switch_to.frame("if")     #切换到iframe(id="if")
xf = driver.find_element_by_xpath('//*[class="if"]')
driver.switch_to.frame(xf) #将定位对象传给switch_to.frame()

# ----------4.10多窗口切换
search_windows = driver.current_window_handle #获得窗口句柄
all_handles  =driver.window_handles #获得当前所有打开窗口的句柄

# ----------4.11警告框处理
driver.switch_to_alert().text()   #返回alert/confirm/prompt中的文字信息
driver.switch_to_alert().accept()   #接受告警框
driver.switch_to_alert().dismiss()   #解散现有告警框
driver.switch_to_alert().send_keys(keystosend)   #发送文本到告警框

# ----------4.12上传文件
# -----send_keys实现上传
import os
file_path = 'file:///' + os.path.abspath('upfile.html') #浏览器开打需要上传的网址
driver.get(file_path)
driver.find_element_by_id("file").send_keys('D:\\ben di lu jing .txt')  #要上传的文件本地路径
# -----Autolt实现上传

# ----------4.13下载文件

# ----------4.14操作cookie
cookie = driver,get_cookies()   #获得素有的cookies信息







