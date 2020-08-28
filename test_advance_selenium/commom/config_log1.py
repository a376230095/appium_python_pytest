import logging


# filename是保存的路径
# filemode是保存的模式，w是重写，a是追加
# level是默认的日志等级

# format是输出的格式，显示都是通过%(指定变量)s的方式
# -指定的变量有asctime绝对的时间，levelname日志等级，filename当前运行的文件，message是输出当前日志的内容，lineno是当前的日志输出的行号

# datefmt是时间输出的格式
#
# logging.basicConfig(filename="log.log",filemode="w",level=logging.INFO,
#                     format=f"{a}%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s",
#                      datefmt="%Y-%m-%d %H:%M:%S")

# 最终的显示2020-08-25 19:03:51|ERROR|config_log1.py:8|abc
# 由于我们这里指定了文件，所以不会在控制台中输出
# logging.error("abc")
# logging.basicConfig(format="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s",level=logging.INFO,
#                     datefmt="%Y-%m-%d %H:%M:%S")
# a=10
# logging.info(f"abc{a}")

#
import logging
# 生成记录器，名字为"tong",其实是用logger调用，这里估计是给配置文件用的
logger=logging.getLogger("tong")
# 默认等级都是最低级别的DEBUG，因为记录器的默认等级优先级高于处理器的
logger.setLevel(logging.DEBUG)

# 生成处理器流处理器
consolehandle=logging.StreamHandler()
# 默认等级为DEBUG
consolehandle.setLevel(logging.DEBUG)

# 文件处理器，文件名为demo.log
filehandle=logging.FileHandler(filename="demo.log")
# 默认等级为INFO
filehandle.setLevel(logging.INFO)

# 生成的格式花器
formatter=logging.Formatter("%(asctime)s|%(levelname)-8s|%(filename)s:%(lineno)4s|%(message)s")

# 处理器添加格式，这里都添加同一个
consolehandle.setFormatter(formatter)
filehandle.setFormatter(formatter)

# 记录器添加处理器，就拥有了屏幕输出的和文件输出的日志了
logger.addHandler(consolehandle)
logger.addHandler(filehandle)

# 文件只输出error，因为默认等级是info，大于debug，流都输出
logger.debug("debug")
logger.error("abc")