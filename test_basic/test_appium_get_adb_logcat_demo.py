from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
import threading
import subprocess
import time
def get_adb_logcat():
    a=subprocess.Popen("adb logcat -v time",stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    with open("../test_thread/adb_logcat.txt", "w") as f:
        for i in a.stdout:
            f.writelines(str(i).lstrip(r"b'").rstrip(r"\r\r\n'")+"\n")
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
        t = threading.Thread(target=get_adb_logcat)
        t.setDaemon(True)
        t.start()
        sleep(3)