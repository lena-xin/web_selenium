# 导包
from Lib.selenium import webdriver

# 实例化火狐
from time import sleep

driver = webdriver.Firefox()
url = r"D:\测试\selenium\新用户注册 - 当当网.html"
url1 = "file:///D:/%E6%B5%8B%E8%AF%95/selenium/%E6%96%B0%E7%94%A8%E6%88%B7%E6%B3%A8%E5%86%8C%20-%20%E5%BD%93%E5%BD%93%E7%BD%91.html"
driver.get(url1)

driver.find_element_by_id("txt_username").send_keys("13412345678")
driver.find_element_by_id("txt_password").send_keys("9876543")

sleep(3)
driver.quit()


