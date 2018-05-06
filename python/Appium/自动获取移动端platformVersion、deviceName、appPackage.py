# -*- coding: utf-8 -*-
from appium import webdriver
# 使用正则表达式筛选设备 id
import re
# 使用time.sleep(xx)函数进行等待
from time import sleep
# 使用 os 模块调用命令
import os

# 测试的包的路径和包名
appLocation = "C:\\Users\\a\\Desktop\\dingding_431.apk"
# 读取设备 id
read_DeviceId = list(os.popen('adb devices').readlines())
'''执行cmd命令，将结果保存为列表read_DeviceId '''
print read_DeviceId
device_Id=read_DeviceId[1].split('\t')[0]
'''取列表中的第二项，进行字符串切分，切分后的列表取第一项
此处有个问题，若有多个设备连入，则只能处理第一个
此处看可用正则实现？
'''
print device_Id


# 读取设备系统版本号
device_Android_Version = list(os.popen('adb shell getprop ro.build.version.release').readlines())
print device_Android_Version
device_Version=device_Android_Version[0].split('\r\n')[0]
print device_Version

# 读取 APK 的 package 信息
appPackageAdb = list(os.popen('aapt dump badging ' + appLocation ).readlines())
appPackage = re.findall(r'\'com\w*.*?\'', appPackageAdb[0])[0]
print appPackage