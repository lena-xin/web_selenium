import time
import unittest
from selenium import webdriver

import sys


class TestLogin(unittest.TestCase):
    def setUp(self):
        # pass
        # 实例化浏览器
        self.driver = webdriver.Firefox()
        # 打开项目网站
        self.driver.get("https://www.xxsy.net/")
        # 最大化浏览器
        self.driver.maximize_window()
        # 设置隐式等待
        self.driver.implicitly_wait(3)

    def test01(self):
        print("iWebLogin_test01 被执行")

    def test_iweb_login(self):
        # 单击登录按钮，跳转页面
        self.driver.find_element_by_link_text("登录").click()
        # 定位用户名和密码，并操作,添加cookie 跳过验证码登录页面
        self.driver.add_cookie({'name': 'name4js', 'value': '18629627232'})
        self.driver.add_cookie({'name': 'userid', 'value': '16457573'})
        self.driver.refresh()
        # 设置断言
        try:
            # 设置bool型断言，相等则fail
            self.assertNotEqual("18629627232", self.driver.find_element_by_css_selector("#username").text)
        except AssertionError:
            # 获取当前时间
            nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
            # 获取错误信息
            info = sys.exc_info()
            print(nowtime, info)
            # 保存截图，并以时间戳，错误信息命名图片文件
            self.driver.get_screenshot_as_file('../iWebImg/%s_%s.jpg' % (nowtime, info[1]))
            # 抛出断言的错误异常
            raise AssertionError

        # pass
    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
