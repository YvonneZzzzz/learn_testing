from unittest import mock   #导入mock

'''
Mock对象的一般用法是这样的：
1、找到你要替换的对象，这个对象可以是一个类，或者是一个函数，或者是一个类实例。
2、然后实例化Mock类得到一个mock对象，并且设置这个mock对象的行为，比如被调用的时候返回什么值，被访问成员的时候返回什么值等。
3、使用这个mock对象替换掉我们想替换的对象，也就是步骤1中确定的对象。
4、之后就可以开始写测试代码，这个时候我们可以保证我们替换掉的对象在测试用例执行的过程中行为和我们预设的一样。
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

# import mock

import client


class TestClient(unittest.TestCase):

    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        client.send_request = success_send
        self.assertEqual(client.visit_ustack(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        client.send_request = fail_send
        self.assertEqual(client.visit_ustack(), '404')

if __name__ == ' __main__':
    unittest.main()
