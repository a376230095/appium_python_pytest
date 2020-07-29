import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestFind():
    def setup(self):
        self.desire_cap= {
            "platformName":"android",
            "deviceName":"LR6PFUPFS4YSM7BM",
            "appPackage":"com.xueqiu.android",
            "appActivity":".view.WelcomeActivityAlias",
            "noReset":"true",
            "unicodeKeyboard":True,
            "chromedriverExecutable": r"C:\chrome_driver_79\chromedriver.exe"
        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
        self.driver.implicitly_wait(5)

    @pytest.mark.skip
    def test_search(self):
        #显示等待页面元素完全加载
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@text="我的"]')))
        #点击交易
        self.driver.find_element(By.XPATH,'//*[@text="交易"]').click()
        webview =self.driver.contexts[-1]
        #切换到webview
        self.driver.switch_to.context(webview)
        #打印出当前的url的值出来
        print(self.driver.execute_script("return window.location.href"))

    def test_search(self):
        #显示等待页面元素完全加载
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@text="我的"]')))
        #点击交易
        self.driver.find_element(By.XPATH,'//*[@text="交易"]').click()
        self.driver.find_element(By.XPATH,'//*[@text="港美"]').click()
        webview =self.driver.contexts[-1]
        #切换到webview
        self.driver.switch_to.context(webview)
        #打印出当前的url的值出来
        print(self.driver.execute_script("return window.location.href"))