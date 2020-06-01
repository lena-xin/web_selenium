# 导包
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)

# 实例化Keys 对象
pwdEle = driver.find_element_by_css_selector("#txt_vcode")
userEle = driver.find_element_by_css_selector("#txt_username")
pwdEle.send_keys("admin")
sleep(1)
pwdEle.send_keys(Keys.BACK_SPACE)
pwdEle.send_keys(Keys.CONTROL, 'a')
pwdEle.send_keys(Keys.CONTROL, 'c')
userEle.send_keys(Keys.CONTROL, 'v')

sleep(2)

driver.close()
