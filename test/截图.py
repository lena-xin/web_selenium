from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get(r"D:\测试\selenium\登录 - 当当网.html")

# driver.find_element_by_link_text("知道了").click()

driver.find_element_by_link_text("立即注册").click()
driver.find_element_by_css_selector("#txt_username").send_keys("13498762345")
# 截取当前窗口
driver.get_screenshot_as_file("../img/img.png")

# currentWin = driver.current_window_handle

sleep(2)

driver.quit()