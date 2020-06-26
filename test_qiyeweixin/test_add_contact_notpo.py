from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFind():
    #由于启动app只需要一次即可，所以setup_class只在类中启动一次
    def setup_class(self):
        self.desire_cap= {
            "platformName":"android",
            "platformVersion":"6.0",
            "deviceName":"127.0.0.1:7555",
            "noReset":"true",
            "appPackage": "com.tencent.wework",
            "appActivity":".launch.WwMainActivity",
            "autoGrantPermissions":"true"
        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
        self.driver.implicitly_wait(5)

    #由于关闭app只需要关一次，所以用teardown_class
    def teardown_class(self):
        self.driver.quit()

    #在每条用例结束后，都加入一个返回上一级菜单，也就是通讯录的页面
    #这里就省去了teardown了，不过好像直接写teardown更加直接，但是这里有两个用例，我只需要在add_contact才使用
    @pytest.fixture
    def add_contact(self):
        #yiled后面都是teardown的效果
        yield
        #点击返回的按钮，回到通讯录的页面
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.tencent.wework:id/h9e']").click()

    #参数化名字、邮箱，性别，地址，电话，这里的参数化用一个大列表，元祖就是每组的数据
    @pytest.mark.parametrize("name,email,address,phone,gender",
                             [("tong1","376230096@qq.com","xiaotong1","13172661161","女"),
                             ("tong2","376230097@qq.com","xiaotong2","13172661162","女"),
                             ("tong3","376230098@qq.com","xiaotong3","13172661163","男")
                             ])
    def test_add_contact(self,add_contact,name,email,address,phone,gender):

        #第一次进入企业微信，担心有延迟，写显示等待确保首页的元素都加载好了
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.wework:id/dyx" and @text="通讯录"]')))

        #点击通讯录的元素
        self.driver.find_element(By.XPATH,'//*[@resource-id="com.tencent.wework:id/dyx" and @text="通讯录"]').click()

        #滚动寻找添加成员的元素，怕联系人太多，所以用这个万能的滚动公式
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("添加成员").'
                                                        'instance(0));').click()
        #点击手动添加的元素
        self.driver.find_element(By.XPATH,"//*[@text='手动输入添加']").click()
        #其实好像可以不睡3秒都ok
        sleep(3)

        #添加联系人的名字
        self.driver.find_element(By.XPATH,'//*[@resource-id="com.tencent.wework:id/b5t"]//*[@text="必填"]').send_keys(name)

        #由于选填有两个，所以第一个元素就是添加email
        elements=self.driver.find_elements(By.XPATH,'//*[@text="选填"]')
        elements[0].send_keys(email)

        #选择性别是男的还是女的，如果性别是男的，就默认不选就好了，因为默认的性别就是男的
        if gender=="女":
            #如果性别是女生，就先点击一下选择联系人的控件
            self.driver.find_element(By.XPATH, f'//*[@text="男"]').click()
            #第一个元素是男，第二个元素是女的，选择第二个元素女生，点击即可
            gender_girl=self.driver.find_elements(By.XPATH, '//*[@resource-id="com.tencent.wework:id/bce"]')[1]
            gender_girl.click()


        #第二个元素就是添加地址了
        elements[1].click()
        #点击之后进入另一个页面，然后输入地址
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.tencent.wework:id/he']").send_keys(address)
        #点击保存，保存地址
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.tencent.wework:id/h9w']").click()

        #输入手机号码
        self.driver.find_element(By.XPATH, '//*[@text="手机号"]').send_keys(phone)

        #点击保存联系人的按钮
        self.driver.find_element(By.XPATH, '//*[@text="保存"]').click()

        #保存之后页面会有toast，捕捉到添加成功的toast，用asset去判断即可
        add_conditon=self.driver.find_element(By.XPATH,"//*[@class='android.widget.Toast']").text
        assert "添加成功"==add_conditon

    #循环删除联系人
    def test_delete_contact(self):
        #用while+break的操作循环删除联系人
        while True:
            # 第一次进入企业微信，担心有延迟，写显示等待确保首页的元素都加载好了
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, '//*[@resource-id="com.tencent.wework:id/dyx" and @text="通讯录"]')))

            #点击通讯录的按钮
            self.driver.find_element(By.XPATH, '//*[@resource-id="com.tencent.wework:id/dyx" and @text="通讯录"]').click()

            # 去滚动查找符合tong的联系人，保存为一个elements
            contact_lens=self.driver.find_elements_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                            'scrollable(true).instance(0)).'
                                                            'scrollIntoView(new UiSelector().textContains("tong").'
                                                            'instance(0));')
            # 当elements的个数为0，就break整个循环
            if len(contact_lens)==0:
                break
            else:
                #先保存联系人的名字
                contact_name=contact_lens[0].text
                #获取第一个联系人点击
                contact_lens[0].click()
                #点击左上角的三个...
                self.driver.find_element(By.ID,"com.tencent.wework:id/h9p").click()
                #点击编辑成员
                self.driver.find_element(By.XPATH,'//*[@text="编辑成员"]').click()
                #点击删除成员
                self.driver.find_element(By.XPATH,'//*[@text="删除成员"]').click()
                #点击确定删除
                self.driver.find_element(By.XPATH,'//*[@text="确定"]').click()
                #睡3秒，让程序真的删除了联系人
                sleep(3)
                #当联系人的名字已经不再page_page了，就打印联系人被删除了
                if contact_name not in self.driver.page_source:
                    print(f"{contact_name} is deleted")