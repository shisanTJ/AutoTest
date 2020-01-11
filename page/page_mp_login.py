from selenium.webdriver.common.by import By

import page
from base.base import Base
from tools.get_log import GetLog

log = GetLog().get_logger()


class PageMpLogin(Base):
    # 输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.mp_phone, phone)

    # 输入验证码
    def page_input_verify_code(self, verify_code):
        self.base_input(page.mp_verify_code, verify_code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    # 组合登录业务脚本
    def page_mp_login(self, phone, verify_code):
        log.info("正在登录,用户名:{},验证码:{}".format(phone, verify_code))
        self.base_input(page.mp_phone, phone)
        self.base_input(page.mp_verify_code, verify_code)
        self.base_click(page.mp_login_btn)

        # 组合登录成功业务脚本

    def page_mp_login_success(self, phone="13812345678", verify_code="246810"):
        log.info("登录成功了".format(phone, verify_code))
        self.base_input(page.mp_phone, phone)
        self.base_input(page.mp_verify_code, verify_code)
        self.base_click(page.mp_login_btn)
