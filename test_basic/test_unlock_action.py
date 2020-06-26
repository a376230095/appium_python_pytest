from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
from appium.webdriver.common.touch_action import TouchAction

class TestFind():
    def setup(self):
        self.desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "cn.kmob.screenfingermovelock",
            "appActivity": "com.samsung.ui.MainActivity",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desire_cap)
        self.driver.implicitly_wait(5)

    def test_search(self):
        """
        1.进入解锁的页面
        2.设置解锁密码为一个7字
        3.意外发现appium可以指定去不同的初始的activity，好像也是看应用的
        :return:
        """
        sleep(3)
        #定义一个TouchAcion对象
        aciton=TouchAction(self.driver)
        #找到7个坐标点，通过连续的press，wait，move_to，最后释放手势release()，然后perform()执行即可
        aciton.press(x=142,y=190).wait(200).move_to(x=408,y=190).wait(200).move_to(x=678,y=190).wait(200).move_to(x=678,y=464) \
        .wait(200).move_to(x=678,y=740).release().perform()
        sleep(2)

