# 导包
from Lib.selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)
# find_element_by_css_selector  id 定位 #id
# driver.find_element_by_css_selector("#txt_username").send_keys('nihao')
# class 定位  .class
# driver.find_elements_by_css_selector(".text")[1].send_keys("密码")
driver.find_element(By.ID, "txt_username").send_keys('hhhh')
driver.find_elements(By.CSS_SELECTOR, ".text")[1].send_keys('pse')
sleep(3)

driver.quit()
