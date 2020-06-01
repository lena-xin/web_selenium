# 导包
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
# url = r"D:\测试\selenium\软媒通行证.html"
driver.get(r"D:\测试\selenium\软媒通行证.html")

driver.find_element_by_css_selector(".regbtn").click()
# 转向获取对话框
alter = driver.switch_to.alert
# 获取对话框的文本信息
print(alter.text)
# 接受对话框 确认  取消式dismiss
alter.accept()

# 填写对应输入框的文本信息
driver.find_element_by_css_selector("#phone").send_keys("13487651234")
driver.find_element_by_css_selector("#code").send_keys("121237797")

sleep(2)

driver.quit()