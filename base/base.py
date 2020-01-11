from selenium.webdriver.support.wait import WebDriverWait
import allure
from tools.get_log import GetLog

log = GetLog().get_logger()


class Base:
    # 初始化driver
    def __init__(self, driver):
        log.info("正在初始化driver:{}".format(driver))
        self.driver = driver

    # 查找元素方法-->给输入点击获取文本方法使用
    def base_find(self, loc, timeout=30, poll=1):
        log.info("正在查找元素:{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(loc[0], loc[1]))

        # 查找一组元素元素方法-->给输入点击获取文本方法使用
    def base_finds(self, loc, timeout=30, poll=1):
        log.info("正在查找元素:{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                lambda x: x.find_elements(loc[0], loc[1]))

    # 输入方法
    def base_input(self, loc, value):
        # 调用查找元素方法
        el = self.base_find(loc)
        # 清空
        log.info("正在清空输入框")
        el.clear()
        # 输入
        log.info("正在输入:{}".format(value))
        el.send_keys(value)

    # 点击方法
    def base_click(self, loc):
        log.info("正在点击操作")
        self.base_find(loc).click()

    # 获取文本方法
    def base_get_text(self, loc):
        log.info("正在获取文本:{}".format(self.base_find(loc).text))
        return self.base_find(loc).text

    # 获取截图方法
    def base_get_screenshot(self):
        log.error("出现异常,正在截图")
        self.driver.get_screenshot_as_file("./images/err.png")
        self.__base_write_img()

    # 将图片写入报告
    def __base_write_img(self):
        log.error("异常处理！正在截图写入报告")
        with open("./images/err.png", "rb")as f:
            allure.attach("错误原因：", f.read(), allure.attach_type.PNG)
