import time

import page
from base.base import Base


class PageMpArticle(Base):
    # 点击内容管理
    def page_click_content_manage(self):
        time.sleep(2)
        self.base_click(page.mp_content_manage)

    # 点击发布文章
    def page_click_publish_article(self):
        time.sleep(2)
        self.base_click(page.mp_publish_article)

    # 输入标题
    def page_input_title(self, value):
        self.base_input(page.mp_title, value)

    # 输入内容
    def page_input_article_content(self, content):
        # 切换ifname
        el = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(el)
        # 输入内容
        self.base_input(page.mp_content, content)
        # 切换默认目录
        self.driver.switch_to.default_content()

    # 选择封面
    def page_click_cover(self):
        self.base_click(page.mp_cover)

    # 选择频道
    def page_click_channel(self):
        self.base_click(page.mp_select)
        #     点击请选择
        #     点击具体频道
        time.sleep(1)
        self.base_click(page.mp_select_database)

    # 点击发表
    def page_click_commit(self):
        self.base_click(page.mp_commit)

    # 获取发表结果
    def page_get_commit_result(self):
        return self.base_get_text(page.mp_commit_result)

    # 组合业务方法
    def page_publish_article(self, value, content):
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(value)
        self.page_input_article_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_commit()
