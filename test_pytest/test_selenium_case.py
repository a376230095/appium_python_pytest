import pytest
import allure
from selenium import webdriver
from time import sleep

#这是链接到测试用例的地址，估计是链接到手工测试的用例吧，对应这个的自动化测试用例
@allure.testcase("http://github.com")
#添加大的模块feature
@allure.feature("百度搜索")
#使用pytest的参数化，定义好keyword的关键字，一共执行3次用例
@pytest.mark.parametrize("keyword",['allure','tongtong','test'])
def test_baidu_search(keyword):

    #定义好一个step步骤，这里是打开百度浏览器
    with allure.step("open baidu link"):
        driver=webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        sleep(2)

    #定义好一个step步骤，这里是搜索内容并点击搜索
    with allure.step(f"input {keyword:} ,and then click search element"):
        driver.find_element_by_css_selector("#kw").send_keys(keyword)
        sleep(2)
        driver.find_element_by_css_selector("#su").click()
        sleep(2)

    # 定义好一个step步骤，这里是保存截图
    with allure.step("screenshot the picture"):
        #selenium的截图的方法，这个路径的文件夹必须存在才行
        driver.save_screenshot(f"./report/{keyword}.png")
        #获取截图路径，并在allure展示出来
        allure.attach.file(f"./report/{keyword}.png",name=f"{keyword} picture",attachment_type=allure.attachment_type.PNG)

    # 定义好一个step步骤，这里是关闭浏览器
    with allure.step("close browser"):
        driver.quit()