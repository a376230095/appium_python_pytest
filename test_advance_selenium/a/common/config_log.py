# @Author：LOUIE
# @Time：2020/3/10 19:25

import logging
import time
import os
import threading
from config.read_config import rc


class ConfigLog():

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 日志存放路径
        LOG_PATH = os.path.join(rc.PROJECT_PATH, "log")
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        # 以时间命名日志文件
        log_name = LOG_PATH + "//" + date + ".log"

        # 日志显示格式
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s")

        # fh = logging.FileHandler(log_name)
        # fh.setLevel(logging.DEBUG)
        # fh.setFormatter(formatter)
        # self.logger.addHandler(fh)

        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(formatter)
        self.logger.addHandler(sh)


    def get_logger(self):
        return self.logger


class MyLog():

    Log = None
    mutex = threading.Lock()

    @staticmethod
    def get_log():
        if MyLog.Log is None:
            MyLog.mutex.acquire()
            MyLog.Log = ConfigLog()
            MyLog.mutex.release()
        return MyLog.Log


mylog = MyLog.get_log()
log = mylog.get_logger()


if __name__ == '__main__':
    log.info("###  test message ")

