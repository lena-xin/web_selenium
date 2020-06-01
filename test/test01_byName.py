# 导包
from Lib.selenium import webdriver
from time import sleep

# 打开浏览器
driver = webdriver.Firefox()
# 打开url
url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)

# 根据name查找元素
user_ele = driver.find_element_by_name("txt_username")
pwd_ele = driver.find_element_by_name("txt_password")

# 给元素发送数据
user_ele.send_keys("hello")
pwd_ele.send_keys("pwd_hello")
# 等待
sleep(3)
# 关闭
driver.close()