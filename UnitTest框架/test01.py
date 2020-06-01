import unittest


class MyClassTest01(unittest.TestCase):
    def setUp(self):
        print("[test01--setUp]被执行")

    def test_fun01(self):
        print("[test01--test_fun01]被执行")

    def test_fun02(self):
        print("[test01--test_fun02]被执行")

    def test_fun03(self):
        print("[test01--test_fun03]被执行")

    def tearDown(self):
        print("[test01--tearDown]被执行")
