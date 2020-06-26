from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

class TestFind():
    #设置caps的值
    def setup(self):
        self.desire_cap= {
            "platformName":"android",
            "deviceName":"127.0.0.1:7555",
            "appPackage":"com.xueqiu.android",
            "appActivity":".view.WelcomeActivityAlias",
            "noReset":"true",
            "unicodeKeyboard":True,
            "chromedriverExecutable": r"c:\chrome\chromedriver.exe"
        }


        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_xueqiu_webview(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@text='交易']")))
        self.driver.find_element(By.XPATH,"//*[@text='交易']").click()
        sleep(3)
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ACCESSIBILITY_ID,"A股开户")))



        self.driver.find_element(By.ACCESSIBILITY_ID,"A股开户").click()


        # self.driver.switch_to.window(self.driver.window_handles[-1])

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID,"输入11位手机号")))
        a=self.driver.find_element(By.ACCESSIBILITY_ID,"输入11位手机号")
        a.click()

        self.driver.find_element(By.ACCESSIBILITY_ID,"立即开户").click()
        sleep(3)
        a.
        self.driver.find_element(By.ACCESSIBILITY_ID,"输入验证码").send_keys(123456)

