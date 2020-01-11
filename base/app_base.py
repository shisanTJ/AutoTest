from selenium.webdriver.common.by import By

from base.base import Base


class AppBase(Base):
    # 获取拖拽方法从右向左
    def base_app_right_left(self, area_loc, find_text):
        # 获取区域元素
        el = self.base_find(area_loc)
        # 获取区域位置
        location = el.location
        y = location["y"]
        # 获取元素宽高
        size = el.size
        width = size["width"]
        height = size["height"]
        # 计算开始坐标结束坐标
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5
        # 组合find_text包含的元素定位信息
        loc = By.XPATH, "//android.widget.HorizontalScrollView//*[contains(@text,'{}')]".format(find_text)

        # 获取当前页面结构
        page_source = self.driver.page_source
        while True:
            try:
                el = self.base_find(loc,timeout=2)
                print("找到频道元素了")
                el.click()
                break
            except:
                print("没找到")
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y,2000)
            if page_source == self.driver.page_source:
                print("不能✿了啊")
                raise Exception("异常,没找到,最后一行了")
            else:
                # 更新 paage_source的值
                page_source = self.driver.page_source
    # 获取从下到上的方法
    def base_down_up(self,area_loc,find_text):
        # 获取区域元素
        el = self.base_find(area_loc)

        # 获取元素宽高
        size = el.size
        width = size["width"]
        height = size["height"]
        # 计算开始坐标结束坐标
        start_x = width * 0.5
        start_y =height * 0.85
        end_x = width * 0.5
        end_y = height * 0.15
        # 组合find_text包含的元素定位信息
        loc = By.XPATH, "//*[@bounds ='[0,260][720,1144]']//*[contains(@text,'{}')]".format(find_text)

        # 获取当前页面结构
        page_source = self.driver.page_source
        while True:
            try:
                print("正在查找文章")
                el = self.base_find(loc, timeout=2)
                print("找到文章了:{}".format(el.text))
                el.click()
                break
            except:
                print("没找到")
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
            if page_source == self.driver.page_source:
                print("不能✿了啊")
                raise Exception("异常,没找到,最后一行了")
            else:
                # 更新 paage_source的值
                page_source = self.driver.page_source