# @Author：LOUIE
# @Time：2020/3/11 19:40

from config.read_config import rc
from selenium import webdriver

class OpenBrowser():

    def __init__(self):
        # 获取选择的browser
        self.value = rc.get_browser("browser")
        self.browser = str(self.value).lower()

    def open_browser(self):
        """
        选择浏览器驱动，获取driver
        :return:
        """
        if self.browser == "chrome":
            self.driver = webdriver.Chrome()
        elif self.browser == "firefox":
            self.driver = webdriver.Firefox()
        elif self.browser == "safari":
            self.driver = webdriver.Safari()
        elif self.browser == "opera":
            self.driver = webdriver.Opera()
        elif self.browser == "ie":
            self.driver = webdriver.Ie()
        return self.driver


browser = OpenBrowser()


if __name__ == '__main__':
    browser.open_browser()