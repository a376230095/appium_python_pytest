import pytest
import yaml
from page.app import App

#测试添加联系人的用例的类
class TestAddTcontact():

    #初始化app，并且到主页的位置
    def setup(self):
        self.main=App().strat().main()

    #参数化添加数据，用yaml数据驱动的方法
    @pytest.mark.parametrize("name,address,gender,input_phone",yaml.safe_load(open(r"../data/contact_add.yml",encoding="UTF-8")))
    def test_add_contact(self,name,address,gender,input_phone):
        #进入到通讯录，点击增加联系人，点击手动添加联系人，输入名字，输入地址、输入性别、输入电话、点击保存、确认添加成功的toast，点击back返回到通讯录页面
        self.main.goto_addresslist().click_addmember().\
            click_manual_add().input_name(name).input_address(address).\
            input_gender(gender).input_phone(input_phone).\
            click_save().verify_toast().click_back()