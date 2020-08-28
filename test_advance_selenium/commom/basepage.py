from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import logging
class BasePage():
    def __init__(self,driver:WebDriver=None):
        if driver==None:
            self.driver=webdriver.Chrome()
        else:
            self.driver=driver

    def log(self,mes):
        logging.debug(mes)



if "__main__"=="__name__":
    pass


