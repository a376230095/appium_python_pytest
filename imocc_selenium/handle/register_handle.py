from common.basepage import BasePage
from page.register_ele import RegisterEle
class RegisterHandle(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.rh=RegisterEle(driver)

    def send_username(self,value):
        self.rh.get_username().send_keys(value)


    def send_email(self,value):
        self.rh.get_email().send_keys(value)

    def send_password(self,value):
        self.rh.get_password().send_keys(value)

    def send_password_repeat(self,value):
        self.rh.get_password_repeat().send_keys(value)

    def send_phone(self,value):
        self.rh.get_phone().send_keys(value)

    def get_ele_text(self,ele):
        try:
            if ele=="username_error":
                text=self.rh.get_username_error().text
            elif ele=="email_error":
                text=self.rh.get_email_error().text
            elif ele=="password_error":
                text=self.rh.get_password_error().text
            elif ele=="password_error_repeat_error":
                text=self.rh.get_password_repeat_error().text
        except:
            text=None
        return text

    def click_register_button(self):
        self.rh.get_register_button().click()

if __name__=="__main__":
    a=RegisterHandle()
    a.re.fe.open_url("http://129.204.62.26/fsmarket/user.php?act=register")
    a.send_username("abc")