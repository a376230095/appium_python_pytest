import os
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestFind():
    def setup(self):
        desire_cap= {
            "platformName":"android",
            #如果只运行一个设备，比如一个设备6.0，一个设备9.0，就会自动执行9.0的设备
            #"platformVersion": "9.0",
            "appPackage":"com.xueqiu.android",
            "appActivity":".view.WelcomeActivityAlias",
            "noReset":"true",
            "unicodeKeyboard":True
        }
        #定义一个唯一的uuid，通常是sn号，通过windows的set uuid="abc",就可以定义
        uuid=os.getenv("uuid")
        uuid="sdfsdfsdfsdf"
        #把uuid加入到cap中
        desire_cap["uuid"]=uuid
        #定义Android的版本
        # platformVersion=os.getenv("platformVersion")
        # #把Android版本加入到cap中，都是用set的方法去弄
        # desire_cap["platformVersion"]=platformVersion
        #4444端口是hub的情况，这样就可以通过hub去控制其他设备
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
        self.driver.implicitly_wait(5)

    def test_appium_grid(self):
        #显示等待等待主页的元素都显示出来
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,'//*[@text="我的"]')))
        #点击我的
        self.driver.find_element(MobileBy.XPATH,'//*[@text="我的"]').click()

    def teardown(self):
        sleep(5)
        self.driver.quit()