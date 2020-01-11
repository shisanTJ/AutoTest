import time

from selenium import webdriver

import appium.webdriver

import page


class GetDriver():
    __driver = None
    __app_driver = None

    @classmethod
    def get_driver(cls, url):
        # 判断
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.get(url)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        time.sleep(2)
        if cls.__driver is not None:
            cls.__driver.quit()
            # 滞空大坑
            cls.__driver = None

        # 获取app应用 driver

    @classmethod
    def get_app_driver(cls):
        cap = {}
        if cls.__app_driver is None:
            # server 启动参数
            # 设备信息
            cap['platformName'] = 'Android'
            cap['platformVersion'] = '5.1'
            cap['deviceName'] = 'CSX0217728000025'
            # app的信息
            cap['appPackage'] = page.AppPackage
            cap['appActivity'] = page.appActivity
            # 中文
            cap['unicodeKeyboard'] = True
            cap['resetKeyboard'] = True
            # 不重置应用
            # cap['noReset'] = False
            cls.__app_driver=appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
        return cls.__app_driver
    # 关闭app应用 driver
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None



