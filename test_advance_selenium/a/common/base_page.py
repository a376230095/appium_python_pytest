# @Author：LOUIE
# @Time：2020/3/10 19:25

import os
import time
try:
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
except:
    os.system("pip install selenium")
from config.read_config import rc
from common.config_log import log


class BasePage(object):

    def __init__(self, driver):
        self._driver = webdriver.Chrome()
        self._url = rc.get_browser("url")

    def _open(self):
        """
        打开浏览器获取url地址
        :param url:
        :return:
        """
        self._driver.get(self._url)
        log.info("打开 URL 地址：%s" %self._url)

    def _is_located(self, *loc):
        locator = EC.visibility_of_element_located(*loc)
        return locator

    def _find_element(self, *loc):
        try:
            # WebDriverWait(self._driver, 10).until(lambda x: x.find_element(*loc).is_displayed())
            # WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(*loc))
            WebDriverWait(self._driver, 10).until(self._is_located(*loc))
        except Exception as e:
            print("页面未能找到：（%s） 元素" %(loc))
            log.error("页面未能找到：（%s） 元素" %(loc))
        return self._driver.find_element(*loc)

    def _send_value(self, value, clear=True, *loc):
        """
        重写 send_keys 方法
        :param loc:
        :param value:
        :param clear:
        :return:
        """
        element = self._find_element(*loc)
        if clear:
            element.clear()
        try:
            element.send_keys(value)
        except Exception as e:
            print("值：%s 输入失败, 错误：%s" %(value, e))
            log.error("值：%s 输入失败" %value)

    def _click(self, *loc):
        """
        重写元素点击方法
        :param loc:
        :return:
        """
        element = self._find_element(*loc)
        try:
            element.click()
        except Exception as e:
            log.error("Error：元素点击失败， 错误：%s" %e)

    def _switch_to(self, *loc):
        """
        切入 frame
        :param loc:
        :return:
        """
        try:
            frame = self._find_element(*loc)
            self._driver.switch_to.frame(frame)
            log.info("切入 frame 成功")
        except:
            log.error("切入 frame 失败")

    @staticmethod
    def _sleep(secs):
        time.sleep(secs)
        log.info("等待 %s 秒" %secs)

    def _excute_script(self, script):
        """
        执行 script 语句
        :param script:
        :return:
        """
        try:
            self._driver.execute_script(script)
            log.info("执行 script 语句： %s" %script)
        except Exception as e:
            print("Error：script语句执行失败， 错误：%s" %e)
            log.error("script语句执行失败， 错误：%s" %e)

    def _get_screen_short(self):
        """
        1.在error_img文件夹下创建一个以当前日期的文件夹
        2.再在当前日期的文件夹中创建一个以时分秒命名的文件夹
        3.将文件存入文件夹中
        """
        current_date = time.strftime("%Y-%m-%s", time.localtime(time.time()))
        currrent_time = time.strftime("%H-%M-%S", time.localtime(time.time()))
        error_img_path = os.path.join(rc.PROJECT_PATH, "error_img")
        # listdir = os.listdir(error_img_path)
        img_path = os.path.join(error_img_path, current_date)
        if not os.path.exists(img_path):
            os.mkdir(img_path)
            self._driver.get_screenshot_as_png()
            self._driver.save_screenshot(img_path)
        else:
            print("当前路径已存在：%s" %img_path)
            log.error("当前路径已存在：%s" %img_path)

    def _get_text(self, *loc):
        try:
            text = self._find_element(*loc).text
            log.error("获取到文本：%s" %text)
            return text
        except:
            log.error("Error：未获取到文本内容")

    def _get_attribute(self, name, *loc):
        try:
            attribute = self._find_element(*loc).get_attribute(name)
            log.info("获取到元素属性：%s" %name)
            return attribute
        except:
            log.error("Error：未获取元素到属性：%s" %name)

    def _get_property(self, name, *loc):
        try:
            property = self._find_element(*loc).get_property(name)
            log.info("获取到元素属性：%s" %name)
            return property
        except:
            log.error("Error：未获取元素到属性：%s" %name)
