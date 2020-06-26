from page.address_list_page import AddressListPage
from page.base_page import BasePage
# from page.contact_add_page import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy as By

#请联系人的页面
class MemberInvitePage(BasePage):

    # 点击进入邀请联系人的方法
    def click_manual_add(self):
        #通过local导入，防止python循环导入的问题
        from page.contact_add_page import ContactAddPage
        # 滚动寻找添加成员的元素，怕联系人太多，所以用这个万能的滚动公式
        self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("添加成员").'
                                                        'instance(0));').click()
        # 进入到添加联系人的页面
        return ContactAddPage(self._driver)

    # 返回上一级菜单
    def click_back(self):
        #点击返回的按钮，回到通讯录的页面
        self.find(By.XPATH,"//*[@resource-id='com.tencent.wework:id/h9e']").click()
        #返回通讯录页面
        return AddressListPage(self._driver)

    def verify_toast(self):
        #保存之后页面会有toast，捕捉到添加成功的toast，用asset去判断即可
        #但是没什么返回值，怎么确认呢？这个老师没有优化
        self.find(By.XPATH,"//*[@class='android.widget.Toast']")
        return self