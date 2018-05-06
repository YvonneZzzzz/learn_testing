#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 抛出异常
from random import randint

# 生成一个1到9之间的随机整数
number = randint(1,9)

if number %2 == 0:
    raise NameError("%d is 偶数 " % number)
else :
    raise NameError("%d is 奇数" % number)
