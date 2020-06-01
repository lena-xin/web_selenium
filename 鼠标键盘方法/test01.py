# 导包
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Firefox()
url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)

driver.maximize_window()

# 实例化ActionChains 对象
action = ActionChains(driver)
# 鼠标右键
action.context_click(driver.find_element_by_css_selector("#txt_username"))
# 执行
action.perform()

sleep(2)

driver.close()
