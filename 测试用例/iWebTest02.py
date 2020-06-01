import unittest


class Test02(unittest.TestCase):
    def setUp(self):
        print("[Test02--setUp]被执行")

    def test1(self):
        print("[Test02--test_fun01]被执行")

    def test2(self):
        print("[Test02--test_fun02]被执行")

    def test3(self):
        print("[Test02--test_fun03]被执行")

    def tearDown(self):
        print("[Test02--tearDown]被执行")
