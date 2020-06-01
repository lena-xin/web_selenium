# 导包
from Lib.selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)

driver.find_element_by_link_text("当当首页").click()

sleep(3)
driver.quit()
