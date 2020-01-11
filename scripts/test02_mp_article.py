import page
import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import readyaml

log = GetLog.get_logger()


class TestArticle():
    # 初始化
    def setup_class(self):
        driver = GetDriver.get_driver(page.url_mp)
        # 统一入口类
        self.page = PageIn(driver)
        # 调用登录案例
        self.page.page_get_PageMpLogin().page_mp_login_success()
        # 获取PageMpArticle对象
        self.article = PageIn(driver).page_get_PageMpArticle()

    # 结束
    def teardown_class(self):
        GetDriver.quit_driver()

    # 测试方法
    @pytest.mark.parametrize('value,content,expect', readyaml("mp_article.yaml"))
    def test_mp_article(self, value, content, expect):
        self.article.page_publish_article(value, content)
        try:
            assert expect == self.article.page_get_commit_result()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_screenshot()
            # 抛异常
            raise
