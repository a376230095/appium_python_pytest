from commom.basepage import BasePage

class Contact(BasePage):
    ele=BasePage.ele_yml("../ele_data/contact.yml")
    def goto_addMember(self):
        self.finds(self.eles["addMember"])[2].click()
        # self.find(".js_add_member").click()

    def