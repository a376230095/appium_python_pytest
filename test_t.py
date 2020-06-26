from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



class TestA():

    def test_a(self):
        option = Options()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.ID, 'kw').send_keys('selenium test')
        sleep(2)
        touch_action = TouchActions(self.driver)
        el_click = self.driver.find_element(By.ID, 'su')
        touch_action.tap(el_click)
        touch_action.perform()
        sleep(3)