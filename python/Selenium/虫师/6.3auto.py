#coding= utf-8

from widget import Widget
import unittest

#执行测试的类
    #让所有执行测试的类都继承于 TestCase 类，
    #可以将 TestCase 看成是对特定类进行测试的方法的集合
class WidgetTestCase(unittest.TestCase):

    # setUp()方法中进行测试前的初始化工作
    def setUp(self):
        self.widget = Widget()

    # 在 testSize()中调用 assertEqual()方法，
    # 对 Widget 类中 getSize()方法的返回值和预期值进行比较，确保两者是相等的，
    # assertEqual()也是 TestCase 类中定义的方法。
    def testSize(self):
        self.assertEqual(self.widget.getSize(),(40,40))

    #tearDown()方法中执行测试后的清除工作
    def tearDown(self):
        self.widget = None

#构造测试集
    #提供名为 suite()的全局方法，
    #PyUnit 在执行测试的过程调用suit()方法来确定有多少个测试用例需要被执行，
    #可以将 TestSuite 看成是包含所有测试用例的一个容器。
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    return suite

#测试
if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')
