# @Author：LOUIE
# @Time：2020/3/11 23:10

import unittest
from utils.open_browser import browser
import time


class CaseFrame(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = browser.open_browser()
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()