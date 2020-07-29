from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By

class TestFind():
    #设置caps的值
    def setup(self):
        self.desire_cap= {
            #默认是Android
            "platformName":"android",
            #adb devices的sn名称
            "deviceName":"127.0.0.1:7555",
            #包名
            "appPackage":"com.xueqiu.android",
            #activity名字
            "appActivity":".view.WelcomeActivityAlias",
            "noReset":"true",
            "unicodeKeyboard":True
        }
        #运行appium，前提是要打开appium server
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
        self.driver.implicitly_wait(5)
        self.driver.launch_app()

    def test_search(self):
        """
        1.打开雪球app
        2.点击搜索输入框
        3.向搜索输入框输入“阿里巴巴”
        4.在搜索的结果里选择阿里巴巴，然后点击
        5.获取这只上香港 阿里巴巴的股价，并判断这只股价的价格>200
        :return:
        """
        sleep(3)
        #点击搜索框
        self.driver.find_element(By.ID,"com.xueqiu.android:id/tv_search").click()
        #向搜索框输入阿里巴巴
        self.driver.find_element(By.ID,"com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        #找到搜索框预览结果的阿里巴巴，并点击
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        #选择HK股价的元素
        prices=self.driver.find_elements(By.ID,"com.xueqiu.android:id/current_price")[1]
        #提取股价的text属性
        price=float(prices.text)

        #判断股价是否大于200
        assert price > 200