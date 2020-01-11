import time

import page
from base.base import Base
from tools.get_log import GetLog

log =GetLog.get_logger()

class PageMisLogin(Base):
    # 输入用户名方法
    def page_input_username(self, username):

        self.base_input(page.mis_username, username)

    # 输入密码方法
    def page_input_pwd(self, pwd):

        self.base_input(page.mis_pwd, pwd)

    # 点击登录方法
    def page_click_login_btn(self):

        # 调用js方法
        js = "document.getElementById('inp1').disabled = false"
        self.driver.execute_script(js)
        time.sleep(2)
        self.base_click(page.mis_login_btn)

    # 获取昵称方法
    def page_get_nickname(self):

        return self.base_get_text(page.mis_nickname)

    # 组合业务方法
    def page_mis_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
    # 登录成功方法
    def page_mis_login_success(self, username="testid", pwd="testpwd123"):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
