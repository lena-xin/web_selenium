# 导包
from Lib.selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)
# find_element_by_tag_name 找到第一个与之匹配的元素
driver.find_element_by_class_name("text").send_keys("123987182743")

sleep(3)

driver.quit()

