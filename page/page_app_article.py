import time

import page
from base.app_base import AppBase


class PageAppArticle(AppBase):
    # 查找频道
    def page_find_channel(self,find_text):
        self.base_app_right_left(page.app_area,find_text)
    # 查找文章
    def page_find_article(self,title_text):
        time.sleep(2)
        self.base_down_up(page.app_article,title_text)
    # 组合业务方法
    def page_app_article(self,find_text,title_text):
        # 查找频道
        self.page_find_channel(find_text)
        self.page_find_article(title_text)