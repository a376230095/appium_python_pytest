from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By

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
        #By.name方法不是对应text的，千万不要用
        #self.driver.find_element(By.NAME,"我的")
        #用显示等待，element_to_be_clickable(locator)，里面的locator记得用元祖
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@text="我的"]')))
        #在首页找到我的元素，然后点击
        self.driver.find_element(By.XPATH,'//*[@text="我的"]').click()
        '''
        lambda返回元素
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH,'//*[@text="我的"]'))
        这里找到元素后，不用等待，实测证明过了
        element.click()
        '''
        #显示等待找到账号密码登录的元素
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@text="帐号密码登录"]')))
        #识别账号密码登录的元素，然后点击
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        #显示等待找到账号的元素
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@resource-id="com.xueqiu.android:id/login_account"]')))
        #输入账号名为tongtong
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("tongtong")
        #输入密码为tongtong
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("tongtong")
        #显示等待找到登录的按钮
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@text="登录"]')))
        #点击登录按钮
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
        #显示等待找到确定的元素
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@text="确定"]')))
        #找到错误提示框，里面有一个确定的元素
        login_incorrect=self.driver.find_element_by_android_uiautomator('new UiSelector().text("确定")')
        #当确定的元素可见，表示登录失败，用例pass
        assert login_incorrect.is_displayed()