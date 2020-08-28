# @Author：LOUIE
# @Time：2020/3/10 19:24

from config.read_config import rc
import unittest
from config.read_config import rc
from common.config_log import log
from common.config_email import ce
from utils.BSTestRunner import BSTestRunner
import time
import os


class RunTest():

    def __init__(self):
        self.on_off = rc.get_report("of_off")
        self.title = rc.get_report("title")
        self.description = rc.get_report("description")

    def set_suit(self):
        """
        构建测试套件
        先拿到testcase目录下所有文件名
        再使用遍历所有文件夹嵌套遍历所有文件夹中的test开头的py文件
        识别文件中的test*开头的testcase，添加进testsuit
        :return:
        """
        testsuit = unittest.TestSuite()
        CASE_PATH = os.path.join(rc.PROJECT_PATH, "testcase")
        dir_list = os.listdir(CASE_PATH)
        print(dir_list)
        for dir in dir_list:
            case_list = unittest.defaultTestLoader.discover(dir)
            for case in case_list:
                testsuit.addTests(case)
        print(testsuit)
        return testsuit

    def main(self):
        suit = self.set_suit()
        REPORT_DIR = os.path.join(rc.PROJECT_PATH, "report")
        date = time.strftime("%Y-%m-%d %H:%M")
        reportname = REPORT_DIR + date + ".html"
        try:
            if suit is not None:
                log.info("********************   TEST START  ********************")
                with open(reportname, "w+", encoding="utf-8") as file:
                    bstrunner = BSTestRunner(stream=file, title=self.title, description=self.description)
                    bstrunner.run(suit)
        except Exception as e:
            log.error("run test 失败，错误：%s" %e)
        finally:
            log.info("********************   TEST END   ********************")
            if self.on_off == "on":
                ce.send_email()
            elif self.on_off == "off":
                log.info("邮件控制器选择：不发送邮件")


if __name__ == '__main__':
    pass


