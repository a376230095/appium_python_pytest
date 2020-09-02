from commom.basepage import BasePage
from commom.config_log import log
from pages.contact import Contact


class Index(BasePage):
    eles = BasePage.ele_yml("../ele_data/index.yml")
    def goto_index(self):
        self.open_url("https://work.weixin.qq.com/wework_admin/frame")
        log.info("start get cookies")
        self.get_cookies()
        log.info("get cookies ok")
        return self


    def goto_Contact(self):
        self.find(self.eles["contact"]).click()
        # self.find(".ww_indexImg_AddMember").click()
        return Contact(self.driver)



