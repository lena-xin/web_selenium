# 导包
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Firefox()
url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)

# driver.maximize_window()

# username 文本框输入用户名
driver.find_element_by_css_selector("#txt_username").send_keys("13490873456")
sleep(1)
# 实例化ActionChains 对象
action = ActionChains(driver)

# 鼠标双击
action.double_click(driver.find_element_by_css_selector("#txt_username")).perform()
# 执行
# action.perform()

sleep(2)

driver.close()
