from selenium.webdriver.common.by import By

from tools.read_yaml import readyaml

"""网址"""
# 自媒体登录页面网址
url_mp = "http://ttmp.research.itcast.cn/#/login"
# 自媒体后台页面网址
url_mis = "http://ttmis.research.itcast.cn/#/"
# 输入元素
mp_phone = (By.CSS_SELECTOR, '[placeholder = "请输入手机号"]')
# 验证码元素
mp_verify_code = (By.CSS_SELECTOR, '[placeholder = "验证码"]')
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, ".el-button--primary")
# 获取昵称
mp_nickname = (By.CSS_SELECTOR, ".user-name")

# 文章标题配置数据
article_title = readyaml("mp_article.yaml")[0][0]
# 文章频道
article_channel = "数据库"

# app包名启动名com.itcast.toutiaoApp/.MainActivity
AppPackage = "com.itcast.toutiaoApp"
appActivity = ".MainActivity"

"""发布文章管理页面"""
# 点击内容管理元素
mp_content_manage = By.XPATH, "//*[text()='内容管理']"
# 点击发布文章
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 输入标题
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# 输入内容之前要切换iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 输入内容
mp_content = By.CSS_SELECTOR, "#tinymce"
# 选择封面
mp_cover = By.XPATH, "//*[text()='自动']"
# 选择点击请选
mp_select = By.CSS_SELECTOR, "[placeholder='请选择']"
# 点击具体频道
mp_select_database = By.XPATH, "//*[text()='{}']".format(article_channel)
# 点击发表
mp_commit = By.CSS_SELECTOR, ".el-button.filter-item.el-button--primary"
# 获取发表结果
mp_commit_result = By.XPATH, "//*[contains(text(),'成功')]"

"""后台登录页面"""
# 用户名
mis_username = By.CSS_SELECTOR, "[placeholder='用户名']"
# 密码
mis_pwd = By.CSS_SELECTOR, "[placeholder='密码']"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR, "#inp1"
# 获取昵称
mis_nickname = By.CSS_SELECTOR, ".user_info>span"

# 后台信息管理
mis_info_manage = By.XPATH, "//*[@class='menu']//*[text()='信息管理']"
# 内容审核
mis_content_audit = By.XPATH, "//*[@class='menu']//*[text()='内容审核']"
# 文章标题
mis_title = By.CSS_SELECTOR, "[placeholder ='请输入: 文章名称']"
# 频道
mis_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"
# 查询
mis_select = By.CSS_SELECTOR, ".find"
# 通过
mis_pass = By.XPATH, "//*[text()='通过']/.."  # ------???
# 确认通过
mis_pass_ok = By.CSS_SELECTOR, ".el-button--primary"
# 获取id
mis_id = By.CSS_SELECTOR, ".cell>span"

# app用户名
app_username = By.XPATH, "//*[@index='1' and @class='android.widget.EditText']"
# app密码
app_pwd = By.XPATH, "//*[@index='2' and @class='android.widget.EditText']"
# app登录
app_login_btn = By.XPATH, "//*[@index='4' and @class='android.widget.Button']"
# 获取我的
app_nickname = By.XPATH, "//*[@index='3'and contains(@text,'我的')] "

# 主页面
# 频道区域
app_area =By.XPATH,"//*[@class='android.widget.HorizontalScrollView']"
# 文章区域
app_article =By.XPATH,"//*[@bounds ='[0,260][720,1144]']"