import unittest
from unittest import TextTestRunner

from UnitTest框架.test01 import MyClassTest01

suite = unittest.TestSuite()
# 一个测试用例中，多个方法的调用繁琐
'''
suite.addTest(MyClassTest01("test_fun01"))
suite.addTest(MyClassTest01("test_fun02"))
suite.addTest(MyClassTest01("test_fun03"))
'''
# unittest.makeSuite 方法遗弃 ，替代方法如下
# 批量执行一个类中所有以test开头的方法
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(MyClassTest01))

# TestSuite 需要配合 TextTestRunner 才能被调用
TextTestRunner().run(suite)
