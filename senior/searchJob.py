# 导包
import time
import xlwt
from selenium import webdriver
# from time import sleep, time
import unittest
# import xlrd
import sys
from time import sleep


class testJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

        self.driver.get("https://mkt.51job.com/tg/sem/pz_v2.html?from=baidupz")
        self.driver.maximize_winddow()

        self.driver.implicitly_wait(3)

    # 将数据写入Excel
    def writeExc(self):

        # 数据写入Excel 表
        row = 0
        jobs = self.driver.find_elements_by_css_selector('#resultList div[class="el"]')
        # 创建Excel 对象
        book = xlwt.Workbook()
        # 创建一个sheet 页
        sh = book.add_sheet("检索数据")
        for job in jobs:
            fields = job.find_elements_by_tag_name('span')
            col = 0
            for field in fields:
                # print()
                sh.write(row, col, field.text)
                col += 1
            row += 1

        book.save('../ExcelReport/51job_search_%s.xls' % time.strftime("%Y_%m_%d %H_%M_%S"))

    # 登录
    def testLogin(self):
        # cur_win = self.driver.current_window_handle
        self.driver.find_element_by_link_text("已有帐号，去登录").click()
        all_win = self.driver.window_handles

        for win in all_win:
            if win == all_win[len(all_win)-1]:
                self.driver.switch_to.window(win)

        self.driver.find_element_by_css_selector("#loginname").send_keys("*****")  # 此处填写测试数据 -- 用户名
        self.driver.find_element_by_css_selector("#password").send_keys("******")  # 此处填写测试数据 -- 密码
        self.driver.find_element_by_css_selector("#isread_em").click()
        self.driver.find_element_by_css_selector("#login_btn").click()

        try:
            # 设置bool型断言，相等则fail
            self.assertEqual('*****', self.driver.find_element_by_css_selector(".tle a").text)
        except AssertionError:
            # 获取当前时间
            now_time = time.strftime("%Y_%m_%d %H_%M_%S")
            # 获取错误信息
            info = sys.exc_info()
            # 保存截图，并以时间戳，错误信息命名图片文件
            self.driver.get_screenshot_as_file('../img/%s_%s.jpg' % (now_time, info[1]))
            # 抛出断言的错误异常
            raise AssertionError

        # 职位检索
        # def testJobSearch(self):
        self.driver.find_element_by_link_text("职位搜索").click()
        self.driver.find_element_by_css_selector("#kwdselectid").send_keys("软件测试")
        self.driver.find_element_by_css_selector("#work_position_input").send_keys("西安")
        self.driver.find_element_by_css_selector(".p_but").click()
        # sleep(3)
        # 展开选项
        self.driver.find_element_by_css_selector('.op span').click()

        # 选择月薪范围
        self.driver.find_element_by_css_selector('#filter_providesalary span[class="dx dicon Dm"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_providesalary"] li[data-value="05"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_providesalary"] li[data-value="06"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_providesalary"] li[data-value="07"]').click()
        self.driver.find_element_by_css_selector('#submit_providesalary').click()

        # 选择公司性质
        self.driver.find_element_by_css_selector('#filter_cotype span[class="dx dicon Dm"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_cotype"] li[data-value="03"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_cotype"] li[data-value="04"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_cotype"] li[data-value="05"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_cotype"] li[data-value="10"]').click()
        self.driver.find_element_by_css_selector('#submit_cotype').click()

        # 选择工作年限
        self.driver.find_element_by_css_selector('#filter_workyear span[class="dx dicon Dm"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_workyear"] li[data-value="02"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_workyear"] li[data-value="03"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_workyear"] li[data-value="04"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_workyear"] li[data-value="06"]').click()
        self.driver.find_element_by_css_selector('#submit_workyear').click()

        # 选择学历要求
        self.driver.find_element_by_css_selector('#filter_degreefrom span[class="dx dicon Dm"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_degreefrom"] li[data-value="03"]').click()
        self.driver.find_element_by_css_selector('*[id="multichoices_degreefrom"] li[data-value="04"]').click()
        self.driver.find_element_by_css_selector('#submit_degreefrom').click()

        # 薪资福利
        self.driver.find_element_by_css_selector('*[id="otherFilter"] span').click()
        self.driver.find_element_by_link_text("五险一金").click()

        # 工作类型
        # self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[13]/ul/li[2]/span[1]").click()
        self.driver.find_elements_by_css_selector('*[id="otherFilter"] span')[2].click()
        # sleep(1)
        self.driver.find_elements_by_css_selector('p[id="filter_p_jobterm"] a')[1].click()
        '''
        # 地区地标
        self.driver.find_elements_by_css_selector('*[id="otherFilter"] span')[4].click()
        self.driver.find_element_by_link_text("雁塔区").click()
        '''

        # 排除关键字
        keys = "实习,校招,手机"
        self.driver.find_element_by_css_selector('[name="excludekeyword"]').send_keys(keys)
        self.driver.find_element_by_link_text("确定").click()
        # 按照发布时间排序
        self.driver.find_element_by_link_text("发布时间").click()
        # 全选
        self.driver.find_element_by_css_selector("#top_select_all_jobs_checkbox").click()

        # 滚动条滑倒底部查看选中情况
        js_bottom = "window.scrollTo(0,3000)"
        self.driver.execute_script(js_bottom)
        sleep(0.5)
        # 返回到顶部
        js_top = "window.scrollTo(0, 0)"
        self.driver.execute_script(js_top)
        sleep(0.5)

        # 申请职位
        # self.driver.find_elements_by_css_selector('*[class="dw_tlc"] i[class="dicon Dm"]')[0].click()

        # 收藏职位
        self.driver.find_elements_by_css_selector('*[class="dw_tlc"] i[class="dicon Dm"]')[1].click()

        # 将检索的数据写入Excel
        self.writeExc()

    def tearDown(self):
        self.driver.quit()
        # pass


if __name__ == '__main__':
    unittest.main()

