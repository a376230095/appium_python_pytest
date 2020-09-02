from time import sleep

from commom.basepage import BasePage
from pages.index import Index
from commom.config_log import log
class TestBaidu():
    def setup(self):
        log.info("strat TestBaidu")
        self.index=Index()

    def test_a(self):
        self.index.goto_index().goto_Contact().goto_addMember()

    def teardown(self):
        sleep(2)
        self.index.save_screenshot()
        self.index.driver.quit()
