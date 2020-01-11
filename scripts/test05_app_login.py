from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import readyaml

log = GetLog.get_logger()
rd =readyaml("mp_login.yaml")[0]

class TestAppLogin():
    def setup_class(self):
        # 初始化
        driver = GetDriver.get_app_driver()
        # 获取统一入口类
        self.pagein = PageIn(driver)
        # 获取PageAppLogin对象
        self.app_login = self.pagein.page_get_PageAppLogin()
        # 结束

    def teardown_class(self):
        GetDriver.quit_app_driver()
        # 测试方法

    def test_app_login(self, username=rd[0], pwd=rd[1]):
        self.app_login.page_app_login(username, pwd)

        # 断言
        try:
            assert self.app_login.page_get_nickname()

        except Exception as  e:
            # 截图
            self.app_login.base_get_screenshot()
            # 日志
            log.error(e)
            # 抛异常
            raise
