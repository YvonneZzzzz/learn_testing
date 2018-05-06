#coding=utf-8
from appium import webdriver
import time

# time.sleep(30)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
# desired_caps['deviceName'] = '25db1664'
desired_caps['deviceName'] = '76P4C16514020753'
desired_caps['appPackage'] = 'com.alibaba.android.rimet'
desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'

# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.4.2'
# desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['appPackage'] = 'com.alibaba.android.rimet'
# desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'

#4734接受webdriver端口，4724用于和andorid通信,4723
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# time.sleep(30)

#通过id查找元素
# driver.find_element_by_id("com.alibaba.android.rimet:id/home_bottom_tab_icon_highlight").click()
#通过文本查找元素
# driver.find_element_by_name("工作").click()
# driver.find_element_by_name("考勤打卡").click()

# driver.find_element_by_xpath("//android.widget.TextView[@text='考勤打卡']").click()
# driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='9']").click()

#设定等待时间，来获取查找时间
# time.sleep(12)

#成功获取“下班打卡”元素
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[@index='2']/android.view.View[@index='4']").click()
# 更新打卡
# driver.find_element_by_xpath("//android.view.View[@content-desc='更新打卡']").click()
# driver.find_element_by_id("android:id/button2").click()
# driver.find_element_by_xpath("//android.widget.Button[@content-desc='我知道了']").click()
# driver.find_element_by_content("我知道了").click()

#下面这些尝试下班打卡均未成功
	# driver.find_element_by_xpath("//*[@class='android.view.View' and @index='4']").click()
	# driver.find_element_by_xpath("//*android.webkit.WebView/android.view.View[contains(@index,'4')]").click()
	# driver.find_element_by_xpath("//android.widget.FrameLayout[@resource-id="com.alibaba.android.rimet:id/common_webview"]/com.uc.webkit.as/android.webkit.WebView/android.view.View[5]").click()
	# driver.find_element_by_accessibility_id("2017.06.20").click()
	# action.press (756,252)
	# driver.find_element_by_accessibility_id("下班打卡").click()
	# driver.find_element_by_id("下班打卡").click()
	# driver.find_element_by_name("下班打卡").click()
	# driver.find_element_by_xpath("//android.webkit.WebView/android.view.View[@index='0']/android.view.View[@index='4']").click()
	# driver.find_element_by_xpath("//android.webkit.WebView/android.widget.ListView[@index='5']/android.view.View[@index='2']/android.view.View[@index='3']").click()

# driver.quit()
