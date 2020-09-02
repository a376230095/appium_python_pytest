from appium import webdriver
from common.base_page import BasePage
from common.main import Main

#这是app的类，负责启动，关闭，重启等操作
class App(BasePage):

    #启动app
    def strat(self):
        self.desire_cap = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "noReset": "true",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "autoGrantPermissions": "true"
        }
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desire_cap)
        self._driver.implicitly_wait(5)
        return self

    def stop(self):
        pass

    def restart(self):
        return self

    #返回main的主页方法
    def main(self):
        #返回主页
        return Main(self._driver)