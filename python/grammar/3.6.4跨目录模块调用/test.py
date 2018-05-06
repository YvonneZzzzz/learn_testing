#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------找不到‘count’模块---------
# from model import new_count
# test = new_count.B()
# test.add(2, 5)

import sys
# 将model目录添加到环境变量path下
sys.path.append("./model")
from model import new_count
test = new_count.B()
test.add(2,5)