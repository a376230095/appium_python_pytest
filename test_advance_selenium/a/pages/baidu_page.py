# @Author：LOUIE
# @Time：2020/3/10 19:48

from selenium.webdriver.common.by import By
from common.base_page import BasePage

class BaiDuPage(BasePage):

    # 百度输入框
    _input_box_loc = (By.ID, "kw")
    # 百度一下按钮
    _submit_btn_loc = (By.ID, "su")

    def input_value(self, value="python"):
        self._send_value(*self._input_box_loc, value)

    def click_baidu(self):
        self._click(*self._submit_btn_loc)

    def assert_title(self):
        self._get_text()