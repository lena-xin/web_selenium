from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(r"D:\测试\selenium\新用户注册 - 当当网.html")
# 切换页签，<a>标签  选用link_text or partial_link_text
driver.find_element_by_link_text("企业用户注册").click()
# 定位select 元素，使用id定位
selectEle = driver.find_element_by_css_selector("#province_id")
# 实例化Select 对象
selectObj = Select(selectEle)
# 采用Select 类提供的方法根据索引定位
selectObj.select_by_index(1)
sleep(2)
# 采用Select类 提供的方法根据value 值定位
selectObj.select_by_value("131")
sleep(2)
# 采用Select类 提供的方法根据文本信息定位
selectObj.select_by_visible_text("陕西")

sleep(2)

driver.quit()

