from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("https://www.xxsy.net/")

# 避过验证码登录
driver.add_cookie({'name': 'name4js', 'value': '18629627232'})
driver.add_cookie({'name': 'userid', 'value': '16457573'})
driver.refresh()
sleep(2)

# driver.quit()