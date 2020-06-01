import time
import unittest
from HTMLTestRunner import HTMLTestRunner

# 加载测试用例
discover = unittest.defaultTestLoader.discover("./",pattern='iWeb*.py')

if __name__ == '__main__':
    filePath = "../HtmlReportFile/" + time.strftime("%Y_%m_%d %H_%M_%S")+"report.html"
    print(filePath)
    # 打开指定文件，以二进制的形式写
    with open(filePath, "wb") as f:
        # HTMLTestRunner 运行测试套件，生成测试报告
        HTMLTestRunner(stream=f, title="web自动化测试", description="os:win10").run(discover)
