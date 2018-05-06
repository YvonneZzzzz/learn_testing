#客户端
'''
我们有一个简单的客户端实现，用来访问一个URL，
当访问正常时，需要返回状态码200，
不正常时，需要返回状态码404。首先，我们的客户端代码实现如下：
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def send_request(url):
    r = requests.get(url)
    return r.status_code


def visit_ustack():
    return send_request('http://www.ustack.com')