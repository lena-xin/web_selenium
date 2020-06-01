# 导包
from Lib.selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()

url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)

driver.find_element_by_css_selector("#txt_username").send_keys("18612348776")   #id
sleep(1)
driver.find_element_by_css_selector('[name="txt_password"]').send_keys('querenmima')  #属性选择
sleep(1)
driver.find_element_by_css_selector('[name="txt_repassword"]').send_keys('querenmima')  #属性选择
sleep(1)
driver.find_element_by_css_selector("#txt_vcode").send_keys('验证码')
sleep(1)
driver.find_element_by_css_selector("#txt_vcode").clear()
sleep(1)
driver.find_element_by_css_selector("#txt_vcode").send_keys('khuy')
sleep(1)
driver.find_element_by_css_selector(".btn_login").click()


sleep(3)

driver.quit()