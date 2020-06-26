from page.base_page import BasePage
# from page.member_invite_page import MemberInvitePage
from appium.webdriver.common.mobileby import MobileBy as By

#通讯录页面
class AddressListPage(BasePage):
    def click_addmember(self):

        #进入手动输入添加页面
        from page.member_invite_page import MemberInvitePage
        #下滑直到找到添加成员
        self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("添加成员").'
                                                        'instance(0));').click()
        # 点击通讯录的元素
        self.find(By.XPATH, "//*[@text='手动输入添加']").click()

        # 进入到邀请联系人的页面
        return MemberInvitePage(self._driver)