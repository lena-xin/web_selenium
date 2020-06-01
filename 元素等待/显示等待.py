from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

driver = webdriver.Firefox()
url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)
# 设置隐式等待
driver.implicitly_wait(3)
userEle = driver.find_element_by_css_selector("#txt_username1").send_keys("halelo")
eleLoc = (By.CSS_SELECTOR, "#txt_username")
# 设置显示等待
# res = WebDriverWait(driver, 3).until(EC.presence_of_element_located(eleLoc)).send_keys("dfasd")

