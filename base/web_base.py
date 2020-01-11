import time

from selenium.webdriver.common.by import By

from base.base import Base


class WebBase(Base):
    # 点击元素选择状态
    def web_base_click_ul_li(self, placeholder_text, click_text):
        # 组合placeholder文本元素定位信息
        loc1 = By.XPATH, "//*[@placeholder='{}']".format(placeholder_text)
        # 查找元素并点击
        self.base_click(loc1)
        time.sleep(2)
        # 定位ul>li---->列表
        loc2 = By.CSS_SELECTOR, "ul>li"
        # 遍历text 内容等于 clicktext
        for el in self.base_finds(loc2):
            if el.text == click_text:
                el.click()
                break

    # 判断元素是否存在
    def web_base_element(self, text):
        loc = By.XPATH, "//*[contains(text,'{}')]".format(text)
        # 判断
        try:
            self.base_find(loc, timeout=3)
            print("元素存在")
            return True
        except:
            print("没有此元素")
            return False
