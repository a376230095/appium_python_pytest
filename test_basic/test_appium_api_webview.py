from time import sleep
from appium import  webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestFind():
    def setup(self):
        self.desire_cap= {
            "platformName":"android",
            "platformVersion":"6.0",
            "deviceName":"127.0.0.1:7555",
            "noRest":True,
            "appPackage": "io.appium.android.apis",
            "appActivity":"io.appium.android.apis.view.WebView1",
            #想要切换webview，必须得指定chromdriver，或者你的默认地址的chromedriver的版本和手机的版本是对应的
            "chromedriverExecutable": r"c:\chrome\chromedriver.exe"
        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_appium_api_webview(self):
        sleep(3)
        #进入到webview页面，直接打印contexts，肯定有两个，一个是原生的，一个是webview
        print(self.driver.contexts)
        #需要切换到webview的context的，通常是倒数第一个，记得要有chromedriverExecutable
        self.driver.switch_to.context(self.driver.contexts[-1])
        sleep(2)
        #往输入框输入tongtong
        self.driver.find_element(MobileBy.ID,"i_am_a_textbox").send_keys("tongtong")
        #点击链接
        self.driver.find_element(MobileBy.ID,"i am a link").click()
        #打印出当前的页面布局，发现是一个webview的html的布局
        print(self.driver.page_source)