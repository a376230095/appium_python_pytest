# -*- coding: utf-8 -*-
import logging
import logging.config

class Config_log():

    def __init__(self):
        with open("../config/config_log.ini",encoding="utf8") as f:
            logging.config.fileConfig(f)
            self.tong_log=logging.getLogger("tong")
            self.root_log=logging.getLogger("root")

    def get_tong_log(self):
        return self.tong_log

    def get_root_log(self):
        return self.root_log


a=Config_log()
log=a.get_tong_log()
log_root=a.get_root_log()

if __name__=="__main__":
    pass