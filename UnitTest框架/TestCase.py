import unittest


class MyTest(unittest.TestCase):   # 光标放在此处，该类中所有的方法均会执行
    def test01(self):   # 光标放在此处，只能执行对应的方法  test01
        print("测试用例01")

    def test02(self):
        print("测试用例02")
