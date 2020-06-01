import unittest
'''
unittest.defaultTestLoader.discover(testdir,pattern='iWeb*.py') 检索testdir目录下，格式为pattern的py文件
配合TextTestRunner 执行测试套件
该方法用于需要批量执行多个文件中的，测试方法式使用
'''

unittest.TextTestRunner().run(unittest.defaultTestLoader.discover("../测试用例",pattern='iWeb*.py'))
