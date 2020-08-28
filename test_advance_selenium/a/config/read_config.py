# @Author：LOUIE
# @Time：2020/3/10 19:23

"""
1.导入ConfigParser模块
2.实例化一个ConfigParser对象
3.构建配置文件路径
4.读取配置文件
5.定义读取配置函数
"""
from configparser import ConfigParser
import os


class ReadConfig():

    # 项目路径
    PROJECT_PATH = os.path.dirname(os.path.abspath(os.getcwd()))

    def __init__(self):
        self.cf = ConfigParser()
        CONFIG_PATH = os.path.join(self.PROJECT_PATH, "config", "config.ini")
        self.cf.read(CONFIG_PATH, "utf-8")

    def get_report(self, option):
        """
        读取 REPORT 配置
        :param option:
        :return:
        """
        value = self.cf.get("REPORT", option)
        return value

    def get_email(self, option):
        """
        读取 EMAIL 配置
        :param option:
        :return:
        """
        value = self.cf.get("EMAIL", option)
        return value

    def get_browser(self, option):
        """
        读取 BROWSER 配置
        :param option:
        :return:
        """
        value = self.cf.get("BROWSER", option)
        return value

    def set_section(self, section):
        """
        设置 section
        :return:
        """
        self.cf.add_section(section)

    def set_value(self):
        pass


rc = ReadConfig()


if __name__ == '__main__':
    print(rc.get_browser("browser"))