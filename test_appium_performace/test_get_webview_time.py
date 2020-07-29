from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestFind():
    def setup(self):
        self.desire_cap= {
            "platformName":"android",
            "deviceName":"LR6PFUPFS4YSM7BM",
            # "deviceName":"ee04b625",
            "appPackage":"com.xueqiu.android",
            "appActivity":".view.WelcomeActivityAlias",
            "noReset":"true",
            "unicodeKeyboard":True,
            #凡是涉及到webview的，都需要有chromedriver的执行地址，并且和手机的driver版本对应
            "chromedriverExecutable": r"C:\chrome_driver_79\chromedriver.exe"

        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
        self.driver.implicitly_wait(5)

    def test_search(self):
        #显示等待页面元素完全加载
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@text="我的"]')))
        #点击交易
        self.driver.find_element(By.XPATH,'//*[@text="交易"]').click()
        #要加载webview的交易页面，睡3秒
        sleep(3)
        #打印出当前是否有webview
        print(self.driver.contexts)
        #通常最后一个都是webview
        webview =self.driver.contexts[-1]
        #切换到webview
        self.driver.switch_to.context(webview)
        #最好是睡3秒，让系统缓一下
        sleep(3)
        #获取到当前页面的性能情况
        all_time=self.driver.execute_script("return window.performance.timing")
        #计算出响应花费的时间
        response_time=all_time["responseEnd"]-all_time["responseStart"]
        print(response_time)