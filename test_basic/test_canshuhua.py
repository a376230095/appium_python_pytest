from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

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
            "unicodeKeyboard":True,

        }
        #运行appium，前提是要打开appium server
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
        self.driver.implicitly_wait(5)

    #这个加不加都行，因为参数化运行都会有setup的，setup就是启动app的过程了，这个就显得有点多余了
    #但好像setup并不会初始化整个app，还会停留在前一个页面上，所以还是加上比较好
    def teardown(self):
        self.driver.find_element(By.XPATH,'//*[@text="取消"]').click()

    #这是参数化的函数，第一部分是参数化的名字，得和下面的函数参数一模一样，用字符串包含进去
    #列表里面的元祖接受具体的参数化的数据，用逗号隔开，和list一样
    @pytest.mark.parametrize('searchkey,type,price',[
        ('alibaba','BABA',180),
        ('xiaomi','01810',10)
    ])
    #参数哈的函数的参数要和上面的参数名字保持一致
    def test_search(self,searchkey,type,price):
        """
        1.打开雪球app
        2.点击搜索输入框
        3.向搜索输入框输入“阿里巴巴”
        4.在搜索的结果里选择阿里巴巴，然后点击
        5.获取这只上香港 阿里巴巴的股价，并判断这只股价的价格>200
        6.通过参数化的方法，用一个用例判断阿里巴巴和小米的股价
        :return:
        """
        #显示等待进入主页，等主页的元素都加载好了
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@text="我的"]')))
        #点击搜索框
        self.driver.find_element(By.ID,"com.xueqiu.android:id/tv_search").click()
        #向搜索框输入阿里巴巴，小米等参数化的东西f"{searchkey}"是一个好用的东西
        self.driver.find_element(By.ID,"com.xueqiu.android:id/search_input_text").send_keys(f"{searchkey}")
        #找到搜索框预览结果的阿里巴巴，并点击
        self.driver.find_element(By.XPATH,f"//*[@text='{type}']").click()
        #选择HK股价的元素，这里是通过父类的方法去定位的
        current_price=self.driver.find_element(By.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        #提取股价的text属性
        current_price=float(current_price.text)

        #判断股价是否大于200
        assert current_price > price