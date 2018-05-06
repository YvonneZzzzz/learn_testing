# 使用unittest 单元测试框架对 Calculator类 的方法进行测试 【P97】

import unittest
from module import Calculator


class ModuleTest(unittest.TestCase):
    
    def setUp(self):
        self.cal = Calculator(8, 4)

    def tearDown(self):
        pass

    # unittest要求测试用例（方法）必须以“test”开头
    def test_add(self):
        result = self.cal.add()
        self.assertEqual(result, 12)

    def test_sub(self):
        result = self.cal.sub()
        self.assertEqual(result, 4)

    def test_mul(self):
        result = self.cal.mul()
        self.assertEqual(result, 32)

    def test_div(self):
        result = self.cal.div()
        self.assertEqual(result, 2)
    

if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    # 调用unittest.TestSuite()类的 addTest()方法 向测试套件中添加 测试用例。
    # 可以将测试套件理解为运用测试用例的集合
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest("test_sub"))
    suite.addTest(ModuleTest("test_mul"))
    suite.addTest(ModuleTest("test_div"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
    # 用“.”表示一条运行通过的 测试用例， 总共运行4条测试用例
    



