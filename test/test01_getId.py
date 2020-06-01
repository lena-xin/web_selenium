# 导入selenium
from Lib.selenium import webdriver
from time import sleep

# 实例化火狐浏览器
driver = webdriver.Firefox()

# 打开url
driver.get("D:\\测试\\selenium\\新用户注册 - 当当网.html")

# 定位元素: 根据id找到指定文本框
phone_ele = driver.find_element_by_id("txt_username")

# 定位元素: 根据id找到指定密码框
pwd_ele = driver.find_element_by_id("txt_password")

# 给对应的文本框发送值
phone_ele.send_keys("admin")
pwd_ele.send_keys("123456")

# 暂停3秒钟
sleep(3)

# 关闭浏览器
driver.close()
