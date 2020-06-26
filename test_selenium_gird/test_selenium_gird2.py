from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

class TestGrid:
    def test_grid(self):
        #定义一个hub的地址，和node的hud地址一样，后面加/wd/hub
        hub_url = "http://localhost:4444/wd/hub"
        #定义一个capability的参数，并用CHROME指定是chrome的浏览器
        #用copy是深拷贝esiredCapabilities.CHROME，这样不会改变原来他们的值，也是官方推荐的写法
        capability=DesiredCapabilities.CHROME.copy()
        #运行4次
        for i in range(1,5):
            #启动driver
            driver=Remote(command_executor=hub_url,desired_capabilities=capability)
            #打开百度浏览器
            driver.get("https://www.baidu.com")