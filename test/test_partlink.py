# 导包
from Lib.selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)

# partial_link_text 为模糊匹配，模糊匹配的文字必须具有唯一性
driver.find_element_by_partial_link_text("首页").click()

sleep(3)
driver.quit()
