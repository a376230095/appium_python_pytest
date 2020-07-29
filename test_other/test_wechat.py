# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         test_wechat
# Description:  
# Author:       yanghao
# Date:         2020/7/1
#-------------------------------------------------------------------------------
import time
from appium import webdriver
import pytest
import yaml

def getdata():
    with open("./wework_data.yaml",encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas


class TestWechat:
    def setup_class(self):
        desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'platformVersion': '6.0.1',
        'appPackage': 'com.tencent.wework',
        'appActivity': 'com.tencent.wework.launch.WwMainActivity',
        "noReset": "true",
        "unicodeKeyboard": "true",
        'resetKeyboard': 'true'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)
    def teardown_class(self):
        self.driver.quit()
    @pytest.fixture()
    def click_return(self):
        yield
        self.driver.find_element_by_xpath("//*[@text='添加成员']/../../../../android.widget.TextView").click()

    @pytest.mark.parametrize('username,sex,iphone',getdata())
    def test_add_contact(self,username,sex,iphone,click_return):
        sleep(10)

        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("添加成员").instance(0));').click()


        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text='姓名')]/../android.widget.EditText").send_keys(username)
        self.driver.find_element_by_xpath("//*[text='性别']/..//[@text='男']").click()
        if sex == '女':
            self.driver.find_element_by_xpath("//*[@text='女']").click()
        else:
            self.driver.find_element_by_xpath("//*[@text='男']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='手机号']").send_keys(iphone)

        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        time.sleep(2)
        toast_text=self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert toast_text == "添加成功"


