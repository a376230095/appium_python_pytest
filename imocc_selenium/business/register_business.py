from common.basepage import BasePage
from handle.register_handle import RegisterHandle
from common.config_log import log
class RegisterBusiness(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.register_h=RegisterHandle(driver)

    def check_text(self,text,confirm_text):
        log.info(f"{text}:{self.register_h.get_ele_text(text)},{confirm_text}:confirm_text")
        if confirm_text in self.register_h.get_ele_text(text):
            print("获取错误信息成功")
            return True
        else:
            print("获取错误信息失败")
            return False

    def login(self, username, email, passwd, r_passwd,phone):
        self.register_h.send_username(username)
        self.register_h.send_email(email)
        self.register_h.send_password(passwd)
        self.register_h.send_password_repeat(r_passwd)
        self.register_h.send_phone(phone)


    def login_ok(self,username, email, passwd, r_passwd,phone):
        self.login(username, email, passwd, r_passwd,phone)
        self.register_h.click_register_button()

    def register(self,username,email,passwd,r_passwd,phone,error_ele,error_text):
        self.login(username, email, passwd, r_passwd, phone)
        return self.check_text(error_ele, error_text)




    def login_username_error(self,username,email,passwd,r_passwd,phone):
        self.login(username, email, passwd, r_passwd,phone)
        return self.check_text("username_error","用户名")

    def login_email_error(self, username, email, passwd, r_passwd,phone):
        self.login(username, email, passwd, r_passwd,phone)
        return self.check_text("email_error", "邮件地址不合法")


    def login_password_error(self, username, email, passwd, r_passwd,phone):
        self.login(username, email, passwd, r_passwd,phone)
        return self.check_text("password_error", "登录密码不能少于")

    def login_password_repeat_error(self, username, email, passwd, r_passwd,phone):
        self.login(username, email, passwd, r_passwd,phone)
        return self.check_text("password_repeat_error", "两次输入密码不一致")




