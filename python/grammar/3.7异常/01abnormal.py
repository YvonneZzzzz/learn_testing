#!/usr/bin/env python
# -*- coding: utf-8 -*-

try :
    open('abc.txt','r')
except FileNotFoundError:
    print("异常了")

try:
    print(aa)
except NameError:
    print("this is name 异常了")

# ---Exception 所有异常类的基类，但继承BaseException类 ---
try :
    open('abc.txt','r')
except Exception :
    print("Exception 异常了")

# ---BaseException 新的所有异常类的基类 ---
try :
    open('abc.txt','r')
    # print(aa)
except BaseException :
    print("BaseException  异常了")
# ----msg用于接收异常信息------------
try :
    # open('abc.txt','r')
    print(aa)
except BaseException as msg:
    print(msg)
# --------
try :
    open('abc.txt','r')
    # print(aa)
except BaseException as msg:
    print(msg)