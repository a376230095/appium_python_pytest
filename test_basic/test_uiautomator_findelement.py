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
        1.打开雪球app
        2.点击我的，进入到个人信息页面
        3.点击登录，进入到登录页面
        4.输入用户名，输入密码
        5.点击登录
        6.弹出手机号输入失败的提示，并assert这个提示对不对
        :return:
        """
        #雪球太慢了，只能10秒了，懒得用显示等等
        sleep(10)
        #在首页找到我的元素，然后点击
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        #不睡2秒回导致下一个页面的元素刷新太快识别不到
        sleep(2)
        #识别账号密码登录的元素，然后点击
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        #不睡2秒回导致下一个页面的元素刷新太快识别不到
        sleep(2)
        #输入账号名为tongtong
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("tongtong")
        #输入密码为tongtong
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("tongtong")
        #不睡2秒回导致下一个页面的元素刷新太快识别不到
        sleep(2)
        #点击登录按钮
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
        #不睡2秒回导致下一个页面的元素刷新太快识别不到
        sleep(2)
        #找到错误提示框，里面有一个确定的元素
        login_incorrect=self.driver.find_element_by_android_uiautomator('new UiSelector().text("确定")')
        #当确定的元素可见，表示登录失败，用例pass
        assert login_incorrect.is_displayed()