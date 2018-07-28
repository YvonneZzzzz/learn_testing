from selenium import webdriver
import unittest
from time import sleep

from selenium.webdriver import TouchActions
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.keys import Keys
from mymodule.module import DiaoYong
# from mymodule import module

class unitTest01(unittest.TestCase):

    def setUp(self):
        print ("--------start---------")
        self.driver = webdriver.Chrome()
        # sd = diaoyong(driver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        # 脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []
        # 是否继续接受下一个警告
        self.accept_next_alert = True
        # diaoyong=module.diaoyong(self)

    def tearDown(self):
        self.driver.quit()
        print ("-------end--------")
        # pass

    # def swipeDown(self, site):
    #     driver = self.driver
    #     sleep(2)
    #     button = driver.find_element_by_xpath(site)
    #     sleep(3)
    #     """从button元素像下滑动200元素"""
    #     Action = TouchActions(driver)
    #     Action.scroll_from_element(button, 0, -200).perform()
    #     sleep(3)
    #     print("success")


    def test_Button(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        # self.swipeDown('//*[@id="kw"]')     #class内部调用
        # diaoyong = mymodule()
        # diaoyong.swipeDown("//*[@id='kw']")
        # mymodule().swipeDown("//*[@id='kw']")
        # diaoyong=module.diaoyong(driver)
        # diaoyong.swipeDown('//*[@id="1"]/h3/a/em[2]')
        sd = DiaoYong(driver)
        sd.swipeDown('//*[@id="1"]/h3/a/em[2]')
        # swipeDown("//*[@id='kw']")


if __name__ == '__main__':
     unittest.main()
        # 将滚动条移动到页面的底部
        # js = "var q=document.Body.scrollTop=100000"
        # driver.execute_script(js)
        # sleep(3)
        # 将页面滚动条拖到底部，需要设置sleep(1)
        # sleep(1)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.execute_script("window.scrollTo(0, 10000);")
        # sleep(3)
        # driver.find_element_by_id('kw').send_keys(Keys.PAGE_DOWN)
        # sleep(2)
        # driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.PAGE_DOWN)
        # sleep(4)



