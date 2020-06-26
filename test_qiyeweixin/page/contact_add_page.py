from page.base_page import BasePage
from page.member_invite_page import MemberInvitePage
from appium.webdriver.common.mobileby import MobileBy as By

#添加联系人的详细内容的页面
class ContactAddPage(BasePage):
    #添加联系人
    def input_name(self,name):
        # 添加联系人的名字
        self.find(By.XPATH, '//*[@resource-id="com.tencent.wework:id/b5t"]//*[@text="必填"]').send_keys(
            name)
        return self

    #添加姓名
    def input_gender(self,gender):
        # 选择性别是男的还是女的，如果性别是男的，就默认不选就好了，因为默认的性别就是男的
        if gender == "女":
            # 如果性别是女生，就先点击一下选择联系人的控件
            self.find(By.XPATH, f'//*[@text="男"]').click()
            # 第一个元素是男，第二个元素是女的，选择第二个元素女生，点击即可
            gender_girl = self._driver.find_elements(By.XPATH, '//*[@resource-id="com.tencent.wework:id/bce"]')[1]
            gender_girl.click()
        return self

    #添加地址
    def input_address(self,address):
        elements = self._driver.find_elements(By.XPATH, '//*[@text="选填"]')
        # 第二个元素就是添加地址了
        elements[1].click()
        # 点击之后进入另一个页面，然后输入地址
        self.find(By.XPATH, "//*[@resource-id='com.tencent.wework:id/he']").send_keys(address)
        # 点击保存，保存地址
        self.find(By.XPATH, "//*[@resource-id='com.tencent.wework:id/h9w']").click()
        return self

    #添加手机号码
    def input_phone(self,phone):
        # 输入手机号码
        self.find(By.XPATH, '//*[@text="手机号"]').send_keys(phone)
        return self

    #点击保存联系人
    def click_save(self):
        # 点击保存联系人的按钮
        self.find(By.XPATH, '//*[@text="保存"]').click()
        return MemberInvitePage(self._driver)

