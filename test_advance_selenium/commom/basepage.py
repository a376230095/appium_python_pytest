import json
import os
from datetime import datetime
from typing import List, Dict

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
Select().select_by_visible_text()
from commom.config_log import log
import time
class BasePage():
    def __init__(self,driver:WebDriver=None):
        if driver==None:
            self.driver=webdriver.Chrome()
            self.driver.implicitly_wait(5)
        else:
            self.driver=driver
            self.driver.implicitly_wait(5)

    def open_url(self,url):
        self.driver.get(url)
        log.info(f"open {url}")

    @classmethod
    def ele_yml(cls,filename):
        with open(filename, encoding="utf8") as f:
            data = yaml.safe_load(f)
        return data

    def get_cookies(self):
        cookies_name = str(datetime.today().strftime("%Y-%m-%d")) + "_cookies.json"
        with open(f"../config/{cookies_name}", ) as f:
            cookies: List[Dict] = json.load(f)
            for cookie in cookies:
                if "exiry" in cookie.keys():
                    cookie.pop("expiry")
                self.driver.add_cookie(cookie)
        self.driver.refresh()

    def save_screenshot(self,img_name=""):
        screenshot_date_path="../err_png/"+datetime.today().strftime("%Y-%m-%d")
        if not os.path.exists(screenshot_date_path):
            os.mkdir(screenshot_date_path)
        current_date=datetime.today().strftime("%Y-%m-%d-%H-%M-%S")

        screenshot_date_file=os.path.join(screenshot_date_path,f"{current_date}_{img_name}.png")
        log.info(screenshot_date_file)
        self.driver.save_screenshot(screenshot_date_file)
        log.info("screenshot save ok")


    def find(self,ele,timeout=15):
        try:
            WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,ele)))
        except:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ele)))
        try:
            element=self.driver.find_element(By.CSS_SELECTOR, ele)
            log.info(f"find {ele} element")
        except Exception as e:
            self.save_screenshot(ele)
            log.error(f"{ele} not found")
            log.exception(e)
        return element

    def finds(self,ele,timeout=7):
        try:
            WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,ele)))
        except:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ele)))
        try:
            elements=self.driver.find_elements(By.CSS_SELECTOR, ele)
            log.info("find {ele} element")
        except Exception as e:
            self.save_screenshot(ele)
            log.error(f"{ele} not found")
            log.exception(e)
        return elements

    # def send(self,*ele):
    #      try:




    @staticmethod
    def sleep(secs):
        time.sleep(secs)
        log.info(f"wait {secs} second")








if __name__=="__main__":
    a=BasePage()
    a.log.error("abc")


