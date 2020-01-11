import page
from base.app_base import AppBase


class PageAppLogin(AppBase):
    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.app_username,username)
    # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.app_pwd,pwd)
    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)
    # 获取昵称
    def page_get_nickname(self):
        try:
            el =self.base_find(page.app_nickname)
            print("找到我的元素了他在{}".format(el.location))
            return True
        except:
            print("未找到我的元素")
            return False
    # 组合业务方法
    def page_app_login(self,username,pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
    # 登录成功方法
    def page_app_login_success(self,username="13812345678",pwd="246810"):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
