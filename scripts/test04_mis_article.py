import time

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestMisArticle():
    def setup_class(self):
        # 初始化
        self.driver = GetDriver.get_driver(page.url_mis)
        # 统一入口类
        self.page = PageIn(self.driver)
        # 获取PageMisAudit对象
        self.article = self.page.page_get_PageMisAudit()
        # 获取登录成功对象
        self.page.page_get_PageMisLogin().page_mis_login_success()

    # 结束
    def teardown_class(self):
        GetDriver.quit_driver()

    # 测试方法
    def test_mis_article(self, title=page.article_title, channel=page.article_channel):
        # 调用审核业务方法
        self.article.page_mis_audit(title, channel)
        # 断言
        try:

            assert self.article.web_base_assert_success(title='2020tj',channel='数据库')
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_screenshot()
            # 抛异常
            raise
