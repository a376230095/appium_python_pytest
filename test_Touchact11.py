from selenium import webdriver
from selenium.webdriver import TouchActions
import time

class Test_TouchAction():
    def setup(self):
        option=webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver=webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_Touchaction(self):
        self.driver.get("https://baidu.com")
        ele = self.driver.find_element_by_id("kw")
        ele_se = self.driver.find_element_by_id("su")
        ele.send_keys("helloword")

        action = TouchActions(self.driver)
        action.tap(ele_se).perform()

#        action.scroll_from_element(ele, 0, 100000).perform()
        time.sleep(3)
