# 导包
from Lib.selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)
# find_element_by_tag_name 找到第一个与之匹配的元素
# find_elements_by_tag_name 返回列表形式，多个匹配元素，需要使用下标访问
driver.find_elements_by_tag_name("input")[1].send_keys("123987182743")
driver.find_element_by_tag_name("a").click()

sleep(3)

driver.quit()
