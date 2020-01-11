from tools.read_yaml import readyaml

import page, pytest
from tools.get_driver import GetDriver
from page.page_in import PageIn
from tools.get_log import GetLog

log = GetLog().get_logger()


class TestLogin():

    def setup_class(self):
        self.driver = GetDriver.get_driver(page.url_mp)
        self.login = PageIn(self.driver).page_get_PageMpLogin()

    def teardown_class(self):
        GetDriver.quit_driver()

    @pytest.mark.parametrize('phone,code,expect', readyaml("mp_login.yaml"))
    def test01(self, phone, code, expect):
        self.login.page_mp_login(phone, code)
        # 获取昵称
        try:
            print("获取的昵称为:", self.login.page_get_nickname())
            assert expect == self.login.page_get_nickname()
        except  Exception as e:
            log.error(e)
            self.login.base_get_screenshot()
            raise
