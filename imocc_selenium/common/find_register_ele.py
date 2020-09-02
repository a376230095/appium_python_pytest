from time import sleep

from common.basepage import BasePage
from common.readini import ReadIni
class FindElement(BasePage):
    def __init__(self,filename,node,driver):
        super().__init__(driver)
        self.find_e=ReadIni(filename,node)


    def get_element(self,key):
        return self.find(self.find_e.get_data(key))


if __name__=="__main__":
    a=FindElement("../config/element_ini.ini","RegisterElement")
    # a.open_url("http://129.204.62.26/fsmarket/user.php?act=register")
    # a.get_element("username").send_keys("abc")
    # sleep(2)
