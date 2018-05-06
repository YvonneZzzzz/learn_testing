# -*- coding: utf-8 -*-
from widget import Widget
import  unittest

#执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def testSize(self):
        self.assertEqual(self.widget.getSize(),(40,40))

    def testResize(self):
        self.widget.resize(100,100)
        self.assertEqual(self.widget.getSize(),(100,100))

#测试
if __name__ == "__main__":
    unittest.main()
    #构造测试集
    suit = unittest.TestSuite()
    suit.addTest(WidgetTestCase("testSize"))
    suit.addTest(WidgetTestCase("testResize"))

    #执行测试
    runner = unittest.TextTestResult()
    runner.run(suite)
