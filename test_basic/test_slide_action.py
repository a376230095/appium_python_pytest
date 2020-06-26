from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class TestFind():
    def setup(self):
        self.desire_cap= {
            "platformName":"android",
            "deviceName":"127.0.0.1:7555",
            "appPackage":"com.xueqiu.android",
            "appActivity":".view.WelcomeActivityAlias",
            "noReset":"true",
            "unicodeKeyboard":True
        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
        self.driver.implicitly_wait(5)

    def test_search(self):
        """
        1.进入雪球应用
        2.再主页从下往上滑动
        3.避免使用坐标
        :return:
        """
        #由于雪球真的是太慢了，所以睡10秒
        sleep(10)
        #定义一个TouchAcion对象
        aciton=TouchAction(self.driver)
        #获取整个屏幕的右下角的坐标
        window_rect=self.driver.get_window_rect()
        #提取屏幕的最大的宽
        width=window_rect["width"]
        #提取屏幕的最大的高度
        height=window_rect['height']
        #x的坐标定义为最大宽的一半，也就是中心的x坐标
        x1=int(width/2)
        #定义起始的y坐标，在4/5的底部位置
        y_start=int(height* 4/5)
        #定义终点的y坐标，在1/5顶部的位置，这样就可以模拟从下往上滑动的动作
        y_end=int(height* 1/5)
        #先press点击初始的坐标，然后按住不放等2秒再move_to到终点坐标，然后再release()释放坐标点，用perform()去执行一系列action操作
        aciton.press(x=x1,y=y_start).wait(2000).move_to(x=x1,y=y_end).release().perform()
        #重复两次，看的效果更明显
        aciton.press(x=x1, y=y_start).wait(2000).move_to(x=x1, y=y_end).release().perform()
        aciton.press(x=x1, y=y_start).wait(2000).move_to(x=x1, y=y_end).release().perform()
        sleep(3)
