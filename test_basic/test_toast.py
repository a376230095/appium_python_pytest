from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By

class TestFind():
    def setup(self):
        self.desire_cap= {
            "platformName":"android",
            "deviceName":"127.0.0.1:7555",
            "appPackage":"io.appium.android.apis",
            "appActivity":"io.appium.android.apis.view.PopupMenu1",
            "noReset":"true",
            "unicodeKeyboard":True
        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
        self.driver.implicitly_wait(5)

    def test_search(self):
        """
        1.打开appium的演示app
        2.直接进入到测试toast的界面
        3.点击显示toast的按钮，然后通过driver.page_source获取页面
        4.找到toast的伪控件
        5.打印出toast的值出来
        :return:
        """
        #点击Make a Popup的控件
        self.driver.find_element(By.XPATH,'//*[@text="Make a Popup!"]').click()
        #点击search的控件
        self.driver.find_element(By.XPATH, '//*[@text="Search"]').click()
        #打印整个布局页面的xml出来
        print(self.driver.page_source)
        #打印出toast的值
        print(self.driver.find_element(By.XPATH, '//*[contains(@text,"popup menu")]').text)