from time import sleep
from appium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestFind():
    def setup(self):
        self.desire_cap= {
            "platformName":"android",
            "platformVersion":"6.0",
            "deviceName":"127.0.0.1:7555",
            #想要使用原生的浏览器就选择，Browser。想要选择chrome浏览器就输入Chrome
            "browserName":"Browser",
            "noRest":True,
            #这里是指定chromedriver的路径，记得路径要全到包括chromedriver.exe
            "chromedriverExecutable":r"c:\chrome\chromedriver.exe"
        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        #打开移动端的百度浏览器
        self.driver.get("http://m.baidu.com")
        #显示等待找到搜索框是否可见，expected_conditions里面传的locator必须是一个元祖
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#index-kw")))
        #搜索框输入tongtong
        self.driver.find_element(By.CSS_SELECTOR,"#index-kw").send_keys("tongtong")
        sleep(2)
        #百度一下点击一下
        self.driver.find_element(By.CSS_SELECTOR, "#index-bn").click()
        sleep(3)