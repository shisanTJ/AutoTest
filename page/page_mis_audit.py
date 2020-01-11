import time

import page
from base.web_base import WebBase


class PageMisAudit(WebBase):
    # 点击信息管理
    def page_click_info_manage(self):
        time.sleep(2)
        self.base_click(page.mis_info_manage)

    # 点击内容审核
    def page_click_content_audit(self):
        time.sleep(2)
        self.base_click(page.mis_content_audit)

    # 输入文章标题
    def page_input_title(self,title):
        self.base_input(page.mis_title,title)

    # 输入频道
    def page_input_channel(self,channel):
        self.base_input(page.mis_channel,channel)

    # 选择状态 - -待审核
    def page_click_status(self):
        time.sleep(2)
        self.web_base_click_ul_li("请选择状态","待审核")

    # 点击查询按钮
    def page_click_select_btn(self):
        self.base_click(page.mis_select)

    # 点击通过
    def page_click_pass(self):
        time.sleep(1)
        self.base_click(page.mis_pass)

    # 确认通过
    def page_click_pass_ok(self):
        time.sleep(1)
        self.base_click(page.mis_pass_ok)
    # 获取文章id
    def page_get_article_id(self):
        return self.base_get_text(page.mis_id)
    # 组合业务方法
    def page_mis_audit(self,title,channel):
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_select_btn()
        time.sleep(3)  # 不能少此步
        self.article_id = self.page_get_article_id()
        print("正在审核的文章id为：", self.article_id)
        self.page_click_pass()
        self.page_click_pass_ok()
    # 断言
    def web_base_assert_success(self,title,channel):
        # 先刷新
        self.driver.refresh()
        # 输入标题
        self.page_input_title(title)
        # 输入频道
        self.page_input_channel(channel)
        # 点击请选择状态---审核通过
        time.sleep(2)
        self.web_base_click_ul_li("请选择状态","审核通过")
        # 点击查询
        self.base_click(page.mis_select)
        # 判断结果是否存在
        time.sleep(2)
        return self.web_base_element(self.article_id)