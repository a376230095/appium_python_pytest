# 导入logging.config去运行配置文件，已经帮我们封装好去查找配置文件的方法了
import logging.config
import logging

from os import path
# 获取文件的绝对路径
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'config_log.ini')
# 由于文件注释有中文，所以转化成utf8
with open(log_file_path,encoding="utf8") as f:
    # fileConfig(f)中的f是流，写成f.read()字符串就不对了
    logging.config.fileConfig(f)
    # 获取记录器tong，就拥有了配置文件中的流处理器和文件处理器和格式化器了
    logger=logging.getLogger("tong")
    #和平时一样用即可
    logger.info("abc")