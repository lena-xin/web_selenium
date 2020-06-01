# 导包
from Lib.selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = r"D:\测试\selenium\新用户注册 - 当当网.html"
driver.get(url)

# 绝对路径 /html/body/form[2]/div/div/div/div[3]/table/tbody/tr[1]/td[2]/input
# 相对路径 //*[@id="txt_username"]  //input[@id="txt_username"]
driver.find_element_by_xpath("/html/body/form[2]/div/div/div/div[3]/table/tbody/tr[1]/td[2]/input").send_keys("admin")
# driver.find_element_by_xpath('//*[@id="txt_password"]').send_keys("123456")
driver.find_element_by_xpath('/html/body/form[2]/div/div/div/div[3]/table/tbody/tr[2]/td[2]/input').send_keys("pwd")
sleep(3)
driver.quit()
