from common.basepage import BasePage
from common.find_register_ele import FindElement
class RegisterEle(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.fe=FindElement("../config/element_ini.ini","RegisterElement",driver)

    def get_username(self):
        return self.fe.get_element("username")

    def get_username_error(self):
        return self.fe.get_element("username_error")

    def get_email(self):
        return self.fe.get_element("email")

    def get_email_error(self):
        return self.fe.get_element("email_error")

    def get_password(self):
        return self.fe.get_element("password")

    def get_password_error(self):
        return self.fe.get_element("password_error")

    def get_password_repeat(self):
        return self.fe.get_element("password_repeat")

    def get_password_repeat_error(self):
        return self.fe.get_element("password_repeat_error")

    def get_register_button(self):
        return self.fe.get_element("register_button")

    def get_phone(self):
        return self.fe.get_element("phone")



if __name__=="__main__":
    # a=RegisterEle()
    # a.fe.open_url("http://129.204.62.26/fsmarket/user.php?act=register")
    # a.get_username("username").send_s("abc")
    pass
