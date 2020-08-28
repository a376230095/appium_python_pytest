# @Author：LOUIE
# @Time：2020/3/10 19:52

from utils.open_browser import browser
from utils.case_frame import CaseFrame
from pages.baidu_page import BaiDuPage
import unittest


class TestSearch(unittest.TestCase):

    def setUpClass(cls):
        cls.driver = browser.open_browser()
        cls.driver.implicitly_wait(30)
        cls.BaiDu = BaiDuPage(cls.driver)

    def testSearch1(self):
        self.BaiDu.input_value("python")
        self.BaiDu.click_baidu()

    def testSearch2(self):
        self.BaiDu.input_value("selenium3")
        self.BaiDu.click_baidu()

    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()