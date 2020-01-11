import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import readyaml

log = GetLog.get_logger()


class TestMisLogin():
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_driver(page.url_mis)
        # 获取统一入口类mislogin对象
        self.mis_login = PageIn(self.driver).page_get_PageMisLogin()

    # 结束
    def teardown_class(self):
        GetDriver.quit_driver()

    # 测试方法
    @pytest.mark.parametrize("username,pwd,expect", readyaml("mis_login.yaml"))
    def test_mis_login(self, username, pwd, expect):
        # 登录
        self.mis_login.page_mis_login(username, pwd)
        # 获取昵称
        # 断言
        try:

            assert expect == self.mis_login.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_login.base_get_screenshot()
            # 抛异常
            raise
