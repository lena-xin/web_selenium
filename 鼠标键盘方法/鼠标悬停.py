# 导包
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Firefox()
url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)

# 鼠标悬停显示下拉列表
ActionChains(driver).move_to_element(driver.find_element_by_css_selector("#a_myddchannel")).perform()

sleep(2)

driver.close()



# a_myddchannel