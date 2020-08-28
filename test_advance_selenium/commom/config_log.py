# -*- coding: utf-8 -*-
import logging
import logging.config
import time
import os

# logging.basicConfig(filename="log.log",filemode="w",level=logging.INFO,format="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s",level=logging.INFO,
# #                     datefmt="%Y-%m-%d %H:%M:%S")
# logging.basicConfig(format="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s",level=logging.INFO,
#                     datefmt="%Y-%m-%d %H:%M:%S")
# a=10
# logging.info(f"abc{a}")

#记录器
logger=logging.getLogger("tong")
logger.setLevel(logging.DEBUG)

#处理器
consolehandle=logging.StreamHandler()
consolehandle.setLevel(logging.DEBUG)

#文件处理器
filehandle=logging.FileHandler(filename="demo.log")
filehandle.setLevel(logging.DEBUG)


#格式
formatter=logging.Formatter("%(asctime)s|%(levelname)-8s|%(filename)s:%(lineno)4s|%(message)s")

#处理器添加格式
consolehandle.setFormatter(formatter)
filehandle.setFormatter(formatter)

#记录器添加处理器
logger.addHandler(consolehandle)
logger.addHandler(filehandle)
logger.debug("abc")
logger.error("abc")