from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page.address_list_page import AddressListPage
from test_qiyeweixin.page.base_page import BasePage

#进入的主页面
class Main(BasePage):

    def goto_message(self):
        pass

    # 进入通讯录的页面
    def goto_addresslist(self):
        #进入通讯页面
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@resource-id="com.tencent.wework:id/dyx" and @text="通讯录"]')))
        # self._driver.find_element(By.XPATH, '//*[@resource-id="com.tencent.wework:id/dyx" and @text="通讯录"]').click()

        #封装了步骤的方法，直接调用步骤的数据即可，这里是点击进入通讯录的按钮
        self.step("../steps/main_steps.yml")

        #进入通讯录的页面的page
        return AddressListPage(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass