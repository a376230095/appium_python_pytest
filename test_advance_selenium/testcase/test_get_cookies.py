import json
from datetime import datetime
from time import sleep
from typing import List, Dict

from commom.config_log import log_root

from commom.basepage import BasePage

class TestGetCooies():
    def setup(self):
        self.b=BasePage()

    def test_save_cookies(self):
        self.b.open_url("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        log_root.info("open qiye weixin url:https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        sleep(20)
        log_root.info("sleep 20")
        cookies_name=str(datetime.today().strftime("%Y-%m-%d"))+"_cookies.json"
        log_root.info(f"获取日期的cookies：{cookies_name}")+

        with open(f"../config/{cookies_name}","w") as f:
            cookies=self.b.driver.get_cookies()
            log_root.info(f"获取的cookies为{cookies}")
            json.dump(cookies,f)
            log_root.info("cookies获取成功")

    def test_get_cookies(self):
        self.b.open_url("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        log_root.info("open qiye weixin url:https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        cookies_name = str(datetime.today().strftime("%Y-%m-%d")) + "_cookies.json"
        with open(f"../config/{cookies_name}",) as f:
            cookies:List[Dict]=json.load(f)
            for cookie in cookies:
                if "exiry" in cookie.keys():
                    cookie.pop("expiry")
                self.b.driver.add_cookie(cookie)
        self.b.driver.refresh()

    def teardown(self):
        sleep(3)
