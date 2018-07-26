from selenium import webdriver
import unittest
from time import sleep

class unitTest01(unittest.TestCase):

    def setUp(self):
        print ("--------start---------")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        # 脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []
        # 是否继续接受下一个警告
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        print ("-------end--------")
        # pass

    def test_Button(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()

        # 将滚动条移动到页面的底部
        # js = "var q=document.Body.scrollTop=100000"
        # driver.execute_script(js)
        # sleep(3)
        # 将页面滚动条拖到底部，需要设置sleep(1)
        sleep(1)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, 10000);")
        sleep(3)


    # def swipeDown(driver, t=500, n=1):
    #     '''向下滑动屏幕'''
    #     l = driver.get_window_size()
    #     x1 = l['width'] * 0.5  # x坐标
    #     y1 = l['height'] * 0.25  # 起始y坐标
    #     y2 = l['height'] * 0.75  # 终点y坐标
    #     for i in range(n):
    #         driver.swipe(x1, y1, x1, y2, t)

if __name__ == '__main__':
    unittest.main()
