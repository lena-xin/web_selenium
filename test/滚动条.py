from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get(r"D:\测试\selenium\新用户注册 - 当当网.html")

# 准备js脚本
js_bottom = "window.scrollTo(0,1000)"
# 执行js脚本
driver.execute_script(js_bottom)
sleep(2)
# 执行滚动条滑倒顶部操作
driver.execute_script(r"window.scrollTo(0,0)")
sleep(2)

driver.quit()
