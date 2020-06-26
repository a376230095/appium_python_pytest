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

    def test_element_function(self):
        """
        1.打开雪球首页
        2.定位首页的搜索框
        3.判断搜索框是否可用，并查看搜索框name属性值
        4.打印搜索框这个元素的左上角坐标和它的宽高
        5.向搜索框输入：alibaba
        6.判断阿里巴巴是否可见
        7.如果可见，打印搜索成功点击，如果不可见，打印搜索失败
        :return:
        """
        sleep(8)
        #找到搜索框的元素
        search=self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search")
        #当搜索框是可用（类似可点击）后才进行下面的操作，is_enabled()返回Ture or False
        if search.is_enabled():
            #打印搜索框的text值
            print(search.text)
            #打印搜索框左上角的坐标
            print(search.location)
            #打印搜索框的高和宽
            print(search.size)
            #点击搜索框，才可以进行下面的操作
            search.click()
            #在搜索框中输入阿里巴巴
            self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            #定义找到预览结果的阿里巴巴的元素
            alibaba=self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            #当alibaba元素可见，打开搜索成功，否则打印搜索失败
            if alibaba.is_displayed():
                print("搜索成功")
            else:
                print("搜索失败")
