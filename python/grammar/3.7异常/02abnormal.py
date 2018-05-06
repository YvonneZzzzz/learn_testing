#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    aa = '异常测试'
    print(aa)
except Exception as msg1:
    print(msg1)
else:
    print('没有异常ha')


try :
    print(bb)
except Exception as msg2:
    print(msg2)
finally:
    print("不管是否异常，finally都将执行")

try :
    cc = "yicang："
    print(cc)
except Exception as msg2:
    print(msg2)
finally:
    print("不管是否异常，finally都将执行")