from business.register_business import RegisterBusiness
from selenium import webdriver
class First_case():

    def __init__(self):
        self.driver=webdriver.Chrome()
        self.login=RegisterBusiness(self.driver)

    def login_success(self):
        self.login.login_ok("a376230095","37623001@qq.com","12345678","12345678","13172661165")

    # def login_username_error(self):
    #     login("aa", "bb")
    #
    # def login_email_error(self):
    #     login("aa", "bb")
    #
    # def login_password_error(self):
    #     login("aa", "bb")

if __name__=="__main__":
    a=First_case()
    a.driver.get("http://129.204.62.26/fsmarket/user.php?act=register")
    a.login_success()