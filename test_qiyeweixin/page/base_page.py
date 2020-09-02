import logging
from typing import List
import yaml
from appium.webdriver.common.mobileby import MobileBy as By, MobileBy
from appium.webdriver.webdriver import WebDriver

class BasePage():
    #定义了一个log的日志，等级是INFO
    logging.basicConfig(level=logging.INFO)

    #定义了一个
    _black_list=[
        (By.XPATH,"//*[@text='允许']")
    ]
    #定义查找黑名单的初始尝试次数
    _error_time=0
    #定义了查找黑名单的最多尝试测试
    _error_max_time=3
    #定义步骤驱动中，send的value的值
    _param = {}

    #定义一个初始值为None的driver，方便复用driver
    def __init__(self,driver:WebDriver=None):
        self._driver=driver

    #封装find_element的函数，具备查找弹框的处理机制
    def find(self,locator,value):
        #通过log日志打印出要传的locator和value
        logging.info(locator)
        logging.info(value)

        # if isinstance(locator,tuple):
        #     return self._driver.find_element(*locator)
        # else:
        #     return self._driver.find_element(locator,value)
        # 把上面的变成一个三元的表达式

        try:
            #这里是一个三元的传值，里面的locator可以写成(By.ID,"id")或者By.ID,"id"两者都行
            return self._driver.find_element(*locator) if isinstance(locator,tuple) else self._driver.find_element(locator,value)
        #把异常定义为e
        except Exception as e:
            #当尝试的次数大于最大的尝试次数，就报错，不让这个try死循环
            if self._error_time > self._error_max_time:
                raise e
            #当尝试一次，尝试查找弹窗次数+1
            self._error_time+=1
            #循环遍历黑名单的locator
            for ele in self._black_list:
                #查找黑名单的元素
                black_elements=self._driver.find_elements(*ele)
                #当元素的值大于1，表示找到了黑名单弹窗的元素
                if len(black_elements) > 0:
                    # 就点击一下，让弹窗消失
                    # 但是如果弹框不消失，出现了bug，就会一直调用下面的find的函数
                    # 元素又找不到，因为卡在黑名单对应元素的弹框了，死循环了
                    # 因此要加入最大的尝试定位黑名单的次数，解除死循环
                    black_elements[0].click()
                    #由于弹窗消失了，所以可以找到元素了，调用自己
                    self.find(locator,value)
            #找不到元素就抛出异常
            raise e

    #封账步骤数据的方法，传一个steps的yaml文件
    def step(self,file):
        #打开yaml文件
        with open(file,encoding="UTF-8") as yaml_file:
            #为了编写的方法，编译器不知道yaml处理后就是一个列表外层的字典类型
            #用List[dict]定义steps的数据类型，方便pycharm编译器，方便我们，让steps变成python的数据类型
            steps:List[dict]=yaml.safe_load(yaml_file)
            #方便编译器知道我们是一个元素，调用方法方便
            element:WebDriver

            #循环遍历整个steps的数据
            for step in steps:
                #日志文件打印出当前的step是怎么样的
                logging.info(step)
                #进一步解析step的key中的by。主要是定位用的，By
                if 'by' in step.keys():
                    #定义一个变量，进一步解析by的value
                    myby=step['by']
                    #当by的value为ID，直接调用find，由于传ID，等于默认传By.ID，所以不需要写成MobileBy.ID
                    if myby == 'ID':
                        element=self.find(myby,step['locator'])
                    #当by的value为XPATH，直接调用find，传入locator的value的值step['locator']
                    #记住不要写成MobileBy.myby，是识别不出来的
                    if myby == 'XPATH':
                        element = self.find(MobileBy.XPATH, step['locator'])

                #进一步解析step的key中的action,主要是click、send_keys等行为
                if 'action' in step.keys():
                    #定义一个变量，进一步解析action的value
                    myaction=step['action']
                    #当行为的value是点击，就点击这个元素
                    if myaction == 'click':
                        element.click()
                    #当行为的value是send，就发送，当然这里没有去写
                    if myaction == 'send':
                        pass