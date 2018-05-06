#  -*- coding:utf-8 -*-

# from selenium import webdriver     #导入webdriver包
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# #导入friefox webdriver 包
# import  time  #调入time函数
#
# binary = FirefoxBinary("E:\\firefox-50.0.1.win64.sdk\\firefox-sdk\\bin\\firefox.exe")    #加入Firefox的路径
# driver = webdriver.Firefox(firefox_binary=binary)    #### 定义driver 要操控火狐浏览器 webdriver.firefox
#
# driver.get("http://www.baidu.com")
# time.sleep(0.3)  #休眠0.3秒
# # driver.find_element_by_id("kw").click()
# driver.find_element_by_id("kw").send_keys("aaaa")
# ####一个控件有若干属性id 、name、（也可以用其它方式定位），百度输入框的id 叫kw  我要在输入框里输入 selenium 。
# driver.find_element_by_id("su").click()
# ####搜索的按钮的id 叫su ，我需要点一下按钮（ click() ）。
# time.sleep(3)  # 休眠3秒
# print(driver.title)  # 把页面title 打印出来    当没看到整个脚本执行过程时，看到打印出这句话，就说明页面被正确打开了
# driver.quit()  #退出并关闭窗口的每一个相关的驱动程序 类似的表弟为 driver.close()
# # driver.close()     #关闭当前窗口

#=========================#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

# baidu类继承unittest.TestCase类，
# 从TestCase类继承是告诉unittest模块的方式。
class Baidu(unittest.TestCase):
    # setUp用于设置初始化部分，在测试用例执行前，这个方法中的函数将先被调用
    # 这里将浏览器的调用和URL的访问放到初试化部分。
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        # 脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []
        # 是否继续接受下一个警告
        self.accept_next_alert = True

    # test_baidu中放置的是我们的测试脚本，执行脚本
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        driver.close()

    # is_element_present函数来查找页面元素是否存在
    # try...except...为python语音的异常捕捉
    # is_element_present函数在这里用处不大，通常删除，
    # 判断页面元素是否存在一般都加载testcase中
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    # 对弹窗的异常处理
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    # 关闭警告以及对得到文本框的处理，if判断语句前面已经多次使用
    # try...finally...为python的异常处理
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    # tearDown方法在每个测试方法执行后调用，
    # 这个地方所有测试用例执行完的清理工作，如退出浏览器
    def tearDown(self):
        self.driver.quit()
        # 这个是难点
        # 前面对verificationErrors方法获得的列表进行比较；
        # 如查verificationErrors的列表不为空，输出列表中的报错信息
        self.assertEqual([], self.verificationErrors)

# unittest.main()函数用来测试类中以test开头的测试用例
if __name__ == "__main__":
    unittest.main()

  #定义个报告存放路径，支持相对路径
    filename = 'D:\\selenium\\result1.html'
    fp = open (filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp ,
        title = u'百度搜索测试报告' ,
        description= u'用例执行情况：')
    # 运行测试用例
    runner.run(testunit)
    fp.close()
