from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get(r"D:\测试\selenium\注册新浪通行证.html")

# 获取当前窗口
current_win1 = driver.current_window_handle
print("current_win", current_win1)

# 获取切换窗口的元素
driver.find_element_by_link_text("《新浪网络服务使用协议》").click()
# 获取所有窗口
all_win1 = driver.window_handles

# 打印窗口信息
print("all_win[0]", all_win1[0])
print("all_win[1]", all_win1[1])
print(len(all_win1))
# 遍历窗口，是否有符合新窗口
for handle in all_win1:
    if handle == all_win1[len(all_win1)-1]:  # if handle != current_win:
        driver.switch_to.window(handle)
        driver.execute_script("window.scrollTo(0,1000)")
        sleep(2)
        driver.execute_script("window.scrollTo(0,0)")
        sleep(2)
        driver.find_element_by_link_text("关闭本页").click()
'''
current_win2 = driver.current_window_handle
driver.find_element_by_link_text("新浪发布2019年第四季度及全年未经审计财报").click()
all_win2 = driver.window_handles
for handle in all_win2:
    if handle != current_win2:
        driver.switch_to.window(handle)
print("all_win2", all_win2)
'''
sleep(2)

driver.quit()
