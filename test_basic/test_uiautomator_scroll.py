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
        0.你的雪球app先关注一个人，然后往下滑，找到一个关键字，用textContains来模糊匹配
        1.打开雪球app
        2.点击关注，让屏幕往下滑，直到找到病人的模糊匹配的text元素后点击
        :return:
        """
        #雪球太慢了，只能10秒了，懒得用显示等等
        sleep(10)
        #点击关注的元素
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        #睡4秒，怕跳转页面太快，搜索不到元素
        sleep(4)
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("病人").'
                                                        'instance(0));').click()
        sleep(4)

