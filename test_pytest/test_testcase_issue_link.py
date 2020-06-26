import allure
import pytest

@allure.link("http://www.baidu.com",name="链接")
def test_with_link():
    print("this is add link test")

Tset_case_link="https://www.zhihu.com"
@allure.testcase(Tset_case_link,"login testcase")
def test_with_testcase():
    print("this is test case link")

#{}就是140了，自动引用下面#的参数
# --allure-link-pattern=issue:http://www.baidu.com/{}
@allure.issue('140','这是一个issue')
def test_with_issue_link():
    pass