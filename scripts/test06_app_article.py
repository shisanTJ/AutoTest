from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestAppArticle():
    # 初始化
    def setup_class(self):
        driver =GetDriver.get_app_driver()
        # 获取统一入口类
        self.page =PageIn(driver)
        # 获取登录成功
        self.page.page_get_PageAppLogin().page_app_login_success()
        # 获取pageapparticle对象
        self.article =self.page.page_get_PageAppArticle()
    # 结束
    def teardown_class(self):
        GetDriver.quit_app_driver()
    # 测试方法
    def test_app_article(self):

        self.article.page_app_article(find_text='python',title_text="python")