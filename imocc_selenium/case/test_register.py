import time
import pytest
from business.register_business import RegisterBusiness
from selenium import webdriver
from assertpy import assert_that
from common.readExecl import ReadExecl
ids=["username_error","email_error","password_error"]
from common.config_log import log
class TestRegister():
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.login=RegisterBusiness(self.driver)
        log.info("start register test")

    def setup(self):

        self.driver.get("http://129.204.62.26/fsmarket/user.php?act=register")

    @pytest.mark.parametrize(("username", "email", "passwd", "r_passwd", "phone", "error_ele", "error_text"),
                              ReadExecl("../data/text.xls").get_data())
    def test_register_execl(self,username,email,passwd,r_passwd,phone,error_ele,error_text):
        result=self.login.register(username,email,passwd,r_passwd,phone,error_ele,error_text)
        assert result is True

    # def test_login_success(self):
    #     self.login.login_ok("a376230095","37623001@qq.com","12345678","12345678")
    @pytest.mark.parametrize(("username","email","passwd","r_passwd","phone","error_ele","error_text"),
    [("a3", "37623001@qq.com", "12345678", "12345678","13172661165","username_error","用户名"),
    ("a376230095", "37623001qq.com", "12345678", "12345678","13172661165","email_error", "邮件地址不合法"),
    ("a376230095", "37623001@qq.com", "12", "12","13172661165","password_error", "登录密码不能少于")],ids=ids
    )
    def test_register(self,username,email,passwd,r_passwd,phone,error_ele,error_text):
        result=self.login.register(username,email,passwd,r_passwd,phone,error_ele,error_text)
        assert result is True

    def test_login_username_error(self):
        result = self.login.login_username_error("a3", "37623001@qq.com", "12345678", "12345678","13172661165")
        # assert_that(result).is_false()
        assert result is False

    @pytest.mark.add
    def test_login_email_error(self):
        self.login.login_email_error("a376230095", "37623001qq.com", "12345678", "12345678","13172661165")



    def test_login_password_error(self):
        self.login.login_password_error("a376230095", "37623001@qq.com", "12", "12","13172661165")

    def teardown(self):
        time.sleep(3)


if __name__=="__main__":
    # pytest.
    pass