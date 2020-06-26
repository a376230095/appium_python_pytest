import pytest
import allure

@allure.feature("login module")
class TestLogin():
    @allure.story("login success")
    def test_login_success(self):
        print("this is login success case")

    @allure.story("login unsuccessful")
    def test_login_unsuccessful(self):
        print("this is login unsuccessful case")

    @allure.story("login no password")
    def test_login_no_password(self):
        with allure.step("click username"):
            print("input username")
        with allure.step("click password"):
            print("input password")